# ─── Random suffix ──────────────────────────────────────────────────────────
resource "random_id" "suffix" {
  byte_length = 4
}

locals {
  suffix = random_id.suffix.hex
  name_prefix = "e2e${random_id.suffix.hex}"

  cosmos_account   = "cosmos-${local.name_prefix}"
  cosmos_db        = "appdb"
  cosmos_container = "richieste"
  cosmos_riepiloghi = "riepiloghi"

  function_app = "funcapp-${local.name_prefix}"
  acr_name     = "acr${random_id.suffix.hex}"
  webapp_name  = "webappfrontend-${random_id.suffix.hex}"
  webapp_plan  = "planfrontend-${random_id.suffix.hex}"

  key_vault       = "kv-${local.name_prefix}"
  app_insights    = "ai-${local.name_prefix}"
  storage_account = "sa${random_id.suffix.hex}"

  queue_name = "richieste-da-elaborare"

  tags = {
    project = "azure-e2e-lab"
  }
}

# ─── Resource Group ──────────────────────────────────────────────────────────
resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
  tags     = local.tags
}

# ─── Cosmos DB ───────────────────────────────────────────────────────────────
resource "azurerm_cosmosdb_account" "cosmosdb" {
  name                = local.cosmos_account
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"

  consistency_policy {
    consistency_level = "Session"
  }

  geo_location {
    location          = azurerm_resource_group.rg.location
    failover_priority = 0
  }

  capabilities {
    name = "EnableServerless"
  }

  tags = local.tags
}

resource "azurerm_cosmosdb_sql_database" "db" {
  name                = local.cosmos_db
  resource_group_name = azurerm_resource_group.rg.name
  account_name        = azurerm_cosmosdb_account.cosmosdb.name
}

resource "azurerm_cosmosdb_sql_container" "container" {
  name                = local.cosmos_container
  resource_group_name = azurerm_resource_group.rg.name
  account_name        = azurerm_cosmosdb_account.cosmosdb.name
  database_name       = azurerm_cosmosdb_sql_database.db.name
  partition_key_paths = ["/categoria"]

  indexing_policy {
    indexing_mode = "consistent"
    included_path {
      path = "/*"
    }
  }
}

resource "azurerm_cosmosdb_sql_container" "riepiloghi" {
  name                = local.cosmos_riepiloghi
  resource_group_name = azurerm_resource_group.rg.name
  account_name        = azurerm_cosmosdb_account.cosmosdb.name
  database_name       = azurerm_cosmosdb_sql_database.db.name
  partition_key_paths = ["/tipo"]
}

# ─── Storage Account ─────────────────────────────────────────────────────────
resource "azurerm_storage_account" "func_storage" {
  name                     = local.storage_account
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  tags                     = local.tags
}

resource "azurerm_storage_queue" "richieste" {
  name                 = local.queue_name
  storage_account_name = azurerm_storage_account.func_storage.name
}

# ─── Container Registry ──────────────────────────────────────────────────────
resource "azurerm_container_registry" "acr" {
  name                = local.acr_name
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = false
  tags                = local.tags
}

# ─── App Service Plan (Linux B1) ─────────────────────────────────────────────
resource "azurerm_service_plan" "frontend_plan" {
  name                = local.webapp_plan
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  os_type             = "Linux"
  sku_name            = "B1"
  tags                = local.tags
}

# ─── Web App for Containers (Frontend) ───────────────────────────────────────
resource "azurerm_linux_web_app" "frontend" {
  name                = local.webapp_name
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  service_plan_id     = azurerm_service_plan.frontend_plan.id

  identity {
    type = "SystemAssigned"
  }

  site_config {
    application_stack {
      docker_image_name   = "frontend:v1"
      docker_registry_url = "https://${azurerm_container_registry.acr.login_server}"
    }

    container_registry_use_managed_identity = true
  }

  tags = local.tags
}

# ─── Application Insights ────────────────────────────────────────────────────
resource "azurerm_application_insights" "appinsights" {
  name                = local.app_insights
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  application_type    = "web"
  tags                = local.tags
}

# ─── Function App (Python, B1) ───────────────────────────────────────────────
resource "azurerm_linux_function_app" "main" {
  name                = local.function_app
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  service_plan_id     = azurerm_service_plan.frontend_plan.id

  storage_account_name       = azurerm_storage_account.func_storage.name
  storage_account_access_key = azurerm_storage_account.func_storage.primary_access_key

  identity {
    type = "SystemAssigned"
  }

  site_config {
    always_on = true

    application_stack {
      python_version = "3.11"
    }

    application_insights_connection_string = azurerm_application_insights.appinsights.connection_string
    application_insights_key               = azurerm_application_insights.appinsights.instrumentation_key

    cors {
      allowed_origins = ["https://${azurerm_linux_web_app.frontend.default_hostname}"]
    }
  }

  app_settings = {
    COSMOS_CONNECTION_STRING = "@Microsoft.KeyVault(SecretUri=${azurerm_key_vault.kv.vault_uri}secrets/${azurerm_key_vault_secret.cosmos_conn.name}/)"
    QUEUE_STORAGE_CONNECTION = "@Microsoft.KeyVault(SecretUri=${azurerm_key_vault.kv.vault_uri}secrets/${azurerm_key_vault_secret.storage_conn.name}/)"
    AzureWebJobsStorage      = "@Microsoft.KeyVault(SecretUri=${azurerm_key_vault.kv.vault_uri}secrets/${azurerm_key_vault_secret.storage_conn.name}/)"
    FUNCTIONS_WORKER_RUNTIME = "python"
  }

  tags = local.tags

}

# ─── Key Vault ───────────────────────────────────────────────────────────────
resource "azurerm_key_vault" "kv" {
  name                = local.key_vault
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  tenant_id           = data.azurerm_client_config.current.tenant_id
  sku_name            = "standard"

  purge_protection_enabled   = false
  soft_delete_retention_days = 7

  tags = local.tags
}

data "azurerm_client_config" "current" {}

resource "azurerm_key_vault_access_policy" "deployer" {
  key_vault_id = azurerm_key_vault.kv.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = data.azurerm_client_config.current.object_id

  secret_permissions = ["Get", "List", "Set", "Delete", "Purge"]
}

# ─── Key Vault Secrets ────────────────────────────────────────────────────────
resource "azurerm_key_vault_secret" "cosmos_conn" {
  name         = "cosmos-conn"
  value        = azurerm_cosmosdb_account.cosmosdb.primary_sql_connection_string
  key_vault_id = azurerm_key_vault.kv.id

  depends_on = [azurerm_key_vault_access_policy.deployer]
}

resource "azurerm_key_vault_secret" "storage_conn" {
  name         = "storage-conn"
  value        = azurerm_storage_account.func_storage.primary_connection_string
  key_vault_id = azurerm_key_vault.kv.id

  depends_on = [azurerm_key_vault_access_policy.deployer]
}

# ─── Key Vault Access Policy for Function App Managed Identity ───────────────
resource "azurerm_key_vault_access_policy" "function_app" {
  key_vault_id = azurerm_key_vault.kv.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = azurerm_linux_function_app.main.identity[0].principal_id

  secret_permissions = ["Get", "List"]

  depends_on = [azurerm_linux_function_app.main]
}

# ─── Key Vault Access Policy for Frontend Web App Managed Identity ───────────
resource "azurerm_key_vault_access_policy" "frontend" {
  key_vault_id = azurerm_key_vault.kv.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = azurerm_linux_web_app.frontend.identity[0].principal_id

  secret_permissions = ["Get", "List"]

  depends_on = [azurerm_linux_web_app.frontend]
}

# ─── ACR Role Assignment for Frontend Web App ─────────────────────────────────
resource "azurerm_role_assignment" "acr_pull_frontend" {
  scope                = azurerm_container_registry.acr.id
  role_definition_name = "AcrPull"
  principal_id         = azurerm_linux_web_app.frontend.identity[0].principal_id

  depends_on = [azurerm_linux_web_app.frontend]
}
