# ─── Resource Group ───────────────────────────────────────────────────────────
resource "azurerm_resource_group" "main" {
  name     = "${var.resource_group_name}-${var.suffix}"
  location = var.location
  tags     = local.tags
}

# ─── Cosmos DB ────────────────────────────────────────────────────────────────
resource "azurerm_cosmosdb_account" "main" {
  name                = local.cosmos_account
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"

  consistency_policy {
    consistency_level = "Session"
  }

  geo_location {
    location          = azurerm_resource_group.main.location
    failover_priority = 0
  }

  capabilities {
    name = "EnableServerless"
  }

  tags = local.tags
}

resource "azurerm_cosmosdb_sql_database" "main" {
  name                = local.cosmos_db
  resource_group_name = azurerm_resource_group.main.name
  account_name        = azurerm_cosmosdb_account.main.name
}

resource "azurerm_cosmosdb_sql_container" "richieste" {
  name                = local.cosmos_container
  resource_group_name = azurerm_resource_group.main.name
  account_name        = azurerm_cosmosdb_account.main.name
  database_name       = azurerm_cosmosdb_sql_database.main.name
  partition_key_path  = "/categoria"

  indexing_policy {
    indexing_mode = "consistent"

    included_path {
      path = "/*"
    }
  }
}

resource "azurerm_cosmosdb_sql_container" "riepiloghi" {
  name                = local.cosmos_riepiloghi
  resource_group_name = azurerm_resource_group.main.name
  account_name        = azurerm_cosmosdb_account.main.name
  database_name       = azurerm_cosmosdb_sql_database.main.name
  partition_key_path  = "/tipo"
}

# ─── Storage Account (Functions + Queue) ──────────────────────────────────────
resource "azurerm_storage_account" "main" {
  name                     = local.storage_account
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  tags                     = local.tags
}

resource "azurerm_storage_queue" "richieste" {
  name                 = local.queue_name
  storage_account_name = azurerm_storage_account.main.name
}

# ─── Container Registry ───────────────────────────────────────────────────────
resource "azurerm_container_registry" "main" {
  name                = local.acr_name
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  sku                 = "Basic"
  admin_enabled       = false
  tags                = local.tags
}

# ─── App Service Plan (Linux B1) ──────────────────────────────────────────────
resource "azurerm_service_plan" "frontend" {
  name                = local.webapp_plan
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  os_type             = "Linux"
  sku_name            = "B1"
  tags                = local.tags
}

# ─── Web App for Containers (Frontend) ────────────────────────────────────────
resource "azurerm_linux_web_app" "frontend" {
  name                = local.webapp_name
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  service_plan_id     = azurerm_service_plan.frontend.id

  identity {
    type = "SystemAssigned"
  }

  site_config {
    application_stack {
      docker_image_name   = "frontend:v1"
      docker_registry_url = "https://${azurerm_container_registry.main.login_server}"
    }

    acr_use_managed_identity_credentials = true
  }

  tags = local.tags
}

# ─── Application Insights ─────────────────────────────────────────────────────
resource "azurerm_application_insights" "main" {
  name                = local.app_insights
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  application_type    = "web"
  tags                = local.tags
}

# ─── Function App (Python, B1) ────────────────────────────────────────────────
resource "azurerm_linux_function_app" "main" {
  name                = local.function_app
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  service_plan_id     = azurerm_service_plan.frontend.id

  storage_account_name       = azurerm_storage_account.main.name
  storage_account_access_key = azurerm_storage_account.main.primary_access_key

  identity {
    type = "SystemAssigned"
  }

  site_config {
    always_on = true

    application_stack {
      python_version = "3.11"
    }

    application_insights_connection_string = azurerm_application_insights.main.connection_string
    application_insights_key               = azurerm_application_insights.main.instrumentation_key

    cors {
      allowed_origins = ["https://${azurerm_linux_web_app.frontend.default_hostname}"]
    }
  }

  app_settings = {
    COSMOS_CONNECTION_STRING = "@Microsoft.KeyVault(SecretUri=${azurerm_key_vault.main.vault_uri}secrets/${azurerm_key_vault_secret.cosmos_conn.name}/)"
    QUEUE_STORAGE_CONNECTION = "@Microsoft.KeyVault(SecretUri=${azurerm_key_vault.main.vault_uri}secrets/${azurerm_key_vault_secret.storage_conn.name}/)"
    AzureWebJobsStorage      = "@Microsoft.KeyVault(SecretUri=${azurerm_key_vault.main.vault_uri}secrets/${azurerm_key_vault_secret.storage_conn.name}/)"
    FUNCTIONS_WORKER_RUNTIME = "python"
  }

  tags = local.tags

  depends_on = [
    azurerm_key_vault_access_policy.function_app,
    azurerm_key_vault_secret.cosmos_conn,
    azurerm_key_vault_secret.storage_conn,
  ]
}

# ─── Key Vault ────────────────────────────────────────────────────────────────
resource "azurerm_key_vault" "main" {
  name                = local.key_vault
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  tenant_id           = data.azurerm_client_config.current.tenant_id
  sku_name            = "standard"

  purge_protection_enabled   = false
  soft_delete_retention_days = 7

  tags = local.tags
}

data "azurerm_client_config" "current" {}

resource "azurerm_key_vault_access_policy" "deployer" {
  key_vault_id = azurerm_key_vault.main.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = data.azurerm_client_config.current.object_id

  secret_permissions = [
    "Get", "List", "Set", "Delete", "Purge",
  ]
}

# ─── Key Vault Secrets ─────────────────────────────────────────────────────────
resource "azurerm_key_vault_secret" "cosmos_conn" {
  name         = "cosmos-conn"
  value        = azurerm_cosmosdb_account.main.primary_sql_connection_string
  key_vault_id = azurerm_key_vault.main.id

  depends_on = [azurerm_key_vault_access_policy.deployer]
}

resource "azurerm_key_vault_secret" "storage_conn" {
  name         = "storage-conn"
  value        = azurerm_storage_account.main.primary_connection_string
  key_vault_id = azurerm_key_vault.main.id

  depends_on = [azurerm_key_vault_access_policy.deployer]
}

# ─── Key Vault Access Policy for Function App Managed Identity ────────────────
resource "azurerm_key_vault_access_policy" "function_app" {
  key_vault_id = azurerm_key_vault.main.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = azurerm_linux_function_app.main.identity[0].principal_id

  secret_permissions = [
    "Get", "List",
  ]

  depends_on = [azurerm_linux_function_app.main]
}

# ─── Key Vault Access Policy for Frontend Web App Managed Identity ────────────
resource "azurerm_key_vault_access_policy" "frontend" {
  key_vault_id = azurerm_key_vault.main.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = azurerm_linux_web_app.frontend.identity[0].principal_id

  secret_permissions = [
    "Get", "List",
  ]

  depends_on = [azurerm_linux_web_app.frontend]
}

# ─── ACR Role Assignment for Frontend Web App ──────────────────────────────────
resource "azurerm_role_assignment" "acr_pull_frontend" {
  scope                = azurerm_container_registry.main.id
  role_definition_name = "AcrPull"
  principal_id         = azurerm_linux_web_app.frontend.identity[0].principal_id

  depends_on = [azurerm_linux_web_app.frontend]
}
