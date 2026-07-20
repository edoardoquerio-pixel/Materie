resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

/* Optional random suffix for unique names (if suffix var is empty we can still use random_id for uniqueness) */
resource "random_id" "suffix" {
  byte_length = 4
}

locals {
  suffix                = var.suffix != "" ? var.suffix : random_id.suffix.hex
  storage_account_name  = "sa${var.resource_group_name}${local.suffix}"
  function_app_name     = "funcapp${var.resource_group_name}${local.suffix}"
  app_service_plan_name = "asp${var.resource_group_name}${local.suffix}"
  frontend_app_name     = "webappfrontend${var.resource_group_name}${local.suffix}"
  frontend_plan_name    = "planfrontend${var.resource_group_name}${local.suffix}"
  cosmos_account_name   = "cosmos${var.resource_group_name}${local.suffix}"
  app_insights_name     = "ai${var.resource_group_name}${local.suffix}"
}

/* Storage account for function app (needed for AzureWebJobsStorage) */
resource "azurerm_storage_account" "func_storage" {
  name                      = local.storage_account_name
  resource_group_name       = azurerm_resource_group.rg.name
  location                  = azurerm_resource_group.rg.location
  account_tier              = "Standard"
  account_replication_type  = "LRS"
  enable_https_traffic_only = true
}

/* App Service Plan for Function App (Linux Consumption) */
resource "azurerm_app_service_plan" "func_plan" {
  name                = local.function_app_name # reuse function app name for plan? better separate
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  kind                = "FunctionApp"
  reserved            = true # Linux

  sku {
    tier = "Y1"
    size = "Y1"
  }
}

/* Function App (Linux) */
resource "azurerm_linux_function_app" "functionapp" {
  name                       = local.function_app_name
  location                   = azurerm_resource_group.rg.location
  resource_group_name        = azurerm_resource_group.rg.name
  service_plan_id            = azurerm_app_service_plan.func_plan.id
  storage_account_name       = azurerm_storage_account.func_storage.name
  storage_account_access_key = azurerm_storage_account.func_storage.primary_access_key

  site_config {
    application_stack {
      python_version = "3.12"
    }
    cors {
      allowed_origins = [
        "https://${azurerm_windows_web_app.frontend.default_hostname}"
      ]
    }
  }

  identity {
    type = "SystemAssigned"
  }

  app_settings = {
    "FUNCTIONS_WORKER_RUNTIME"           = "python"
    "WEBSITE_RUN_FROM_PACKAGE"           = "1"
    "COSMOS_CONNECTION_STRING"           = "@Microsoft.KeyVault(SecretUri=${azurerm_key_vault_secret.cosmos_secret.id})"
    "APPLICATIONINSIGHTS_CONNECTION_STRING" = azurerm_application_insights.appinsights.connection_string
  }

  depends_on = [
    azurerm_cosmosdb_account.cosmosdb,
    azurerm_application_insights.appinsights,
    azurerm_key_vault_secret.cosmos_secret
  ]
}

/* Application Insights */
resource "azurerm_application_insights" "appinsights" {
  name                = local.app_insights_name
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  application_type    = "web"
}

/* Key Vault (Standard, RBAC, Soft Delete) */
resource "azurerm_key_vault" "kv" {
  name                        = local.cosmos_account_name
  location                    = azurerm_resource_group.rg.location
  resource_group_name         = azurerm_resource_group.rg.name
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  sku_name                    = "standard"
  soft_delete_retention_days  = 7
  purge_protection_enabled    = false
  enable_rbac_authorization   = true

  tags = {
    Environment = "lab"
  }
}

/* Data source for current tenant ID (needed for Key Vault) */
data "azurerm_client_config" "current" {}

/* Key Vault Secret: Cosmos DB connection string */
resource "azurerm_key_vault_secret" "cosmos_secret" {
  name         = "cosmosdb-connection-string"
  key_vault_id = azurerm_key_vault.kv.id
  value        = azurerm_cosmosdb_account.cosmosdb.connection_strings[0]
}

/* Role Assignment: Function App -> Key Vault Secrets User */
resource "azurerm_role_assignment" "kv_secrets_user" {
  scope                = azurerm_key_vault.kv.id
  role_definition_name = "Key Vault Secrets User"
  principal_id         = azurerm_linux_function_app.functionapp.identity[0].principal_id
  principal_type       = "ServicePrincipal"

  depends_on = [
    azurerm_linux_function_app.functionapp,
    azurerm_key_vault.kv
  ]
}

/* Restart Function App after role assignment propagates (Key Vault reference resolution) */
resource "null_resource" "restart_functionapp" {
  depends_on = [
    azurerm_role_assignment.kv_secrets_user
  ]

  provisioner "local-exec" {
    command     = "az functionapp restart --resource-group ${azurerm_resource_group.rg.name} --name ${azurerm_linux_function_app.functionapp.name}"
    interpreter = ["PowerShell", "-Command"]
  }

  triggers = {
    role_assignment = azurerm_role_assignment.kv_secrets_user.id
  }
}

/* Cosmos DB Account (SQL API, Serverless) */
resource "azurerm_cosmosdb_account" "cosmosdb" {
  name                = local.cosmos_account_name
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
}

/* Cosmos DB SQL Database */
resource "azurerm_cosmosdb_sql_database" "db" {
  name                = "appdb"
  resource_group_name = azurerm_resource_group.rg.name
  account_name        = azurerm_cosmosdb_account.cosmosdb.name
}

/* Cosmos DB SQL Container */
resource "azurerm_cosmosdb_sql_container" "container" {
  name                = "richieste"
  resource_group_name = azurerm_resource_group.rg.name
  account_name        = azurerm_cosmosdb_account.cosmosdb.name
  database_name       = azurerm_cosmosdb_sql_database.db.name
  partition_key_path  = "/utente"
}

/* App Service Plan for Frontend (Windows Free) */
resource "azurerm_app_service_plan" "frontend_plan" {
  name                = local.frontend_plan_name
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  kind                = "app"
  reserved            = false

  sku {
    tier = "F1"
    size = "F1"
  }
}

/* Frontend Web App (static site, Windows) */
resource "azurerm_windows_web_app" "frontend" {
  name                = local.frontend_app_name
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  service_plan_id     = azurerm_app_service_plan.frontend_plan.id

  site_config {
    # No specific runtime needed for static content; we use default.
    # We'll deploy via zip later.
    # Ensure always on etc not needed.
  }

  # Deploy the frontend code from the local ./frontend folder zipped
  # We'll use a null_resource to create zip and then az cli via local-exec (or use deploymentsource)
  # For simplicity, we rely on external zip deployment; but we can also use app_service_source.
  # Using app_service_source requires a zip file; we'll generate it via local-exec.
}

# Create zip of frontend folder (path corrected: frontend is inside labs/)
resource "null_resource" "create_frontend_zip" {
  provisioner "local-exec" {
    command     = "powershell -Command \"Compress-Archive -Path '${path.module}/frontend/*' -DestinationPath '${path.module}/frontend.zip' -Force\""
    interpreter = ["PowerShell", "-Command"]
  }
  triggers = {
    source_path = filesha256("${path.module}/frontend/index.html")
  }
}

# Deploy zip to web app
resource "null_resource" "deploy_frontend" {
  depends_on = [
    null_resource.create_frontend_zip,
    azurerm_windows_web_app.frontend
  ]
  provisioner "local-exec" {
    command     = <<EOT
      az webapp deployment source config-zip `
        --resource-group ${azurerm_resource_group.rg.name} `
        --name ${azurerm_windows_web_app.frontend.name} `
        --src "${path.module}/frontend.zip"
    EOT
    interpreter = ["PowerShell", "-Command"]
  }
}

/* Outputs */
output "function_app_url" {
  description = "Base URL of the Function App"
  value       = "https://${azurerm_linux_function_app.functionapp.default_hostname}"
}

output "frontend_url" {
  description = "URL of the frontend web app"
  value       = "https://${azurerm_windows_web_app.frontend.default_hostname}"
}

output "cosmos_connection_string" {
  description = "Connection string for Cosmos DB (sensitive)"
  value       = azurerm_cosmosdb_account.cosmosdb.connection_strings[0]
  sensitive   = true
}

output "frontend_app_service_plan_id" {
  value = azurerm_app_service_plan.frontend_plan.id
}

output "key_vault_uri" {
  description = "URI of the Key Vault"
  value       = azurerm_key_vault.kv.vault_uri
}

output "key_vault_secret_uri" {
  description = "Full URI of the Cosmos DB connection string secret (for Key Vault reference)"
  value       = azurerm_key_vault_secret.cosmos_secret.id
  sensitive   = true
}