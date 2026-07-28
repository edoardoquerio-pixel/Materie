# Task 2: Terraform Main — All Azure Resources

## Context
This is the second task in an Azure E2E lab project. Task 1 created the project structure with `infra/variables.tf`, `infra/terraform.tfvars`, and `infra/versions.tf`. This task creates the main Terraform configuration with all Azure resources and outputs.

**Working directory:** `C:\Users\edoardo.querio\Desktop\Materie\14_Cloud_Azure\labs`
**Depends on:** Task 1 (variables and locals defined in `infra/variables.tf`)

## What to do

### Step 1: Write `infra/main.tf`

```hcl
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
  admin_enabled       = true
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

  site_config {
    application_stack {
      docker_image_name   = "frontend:v1"
      docker_registry_url = "https://${azurerm_container_registry.main.login_server}"
      docker_registry_username = azurerm_container_registry.main.admin_username
      docker_registry_password = azurerm_container_registry.main.admin_password
    }
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

# ─── Function App (Python, Consumption) ───────────────────────────────────────
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
    application_stack {
      python_version = "3.11"
    }

    application_insights_connection_string = azurerm_application_insights.main.connection_string
    application_insights_key               = azurerm_application_insights.main.instrumentation_key

    cors {
      allowed_origins = ["*"]
    }
  }

  app_settings = {
    COSMOS_CONNECTION_STRING = azurerm_cosmosdb_account.main.primary_sql_connection_string
    QUEUE_STORAGE_CONNECTION = azurerm_storage_account.main.primary_connection_string
    AzureWebJobsStorage      = azurerm_storage_account.main.primary_connection_string
    FUNCTIONS_WORKER_RUNTIME = "python"
  }

  tags = local.tags
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

resource "azurerm_key_vault_secret" "cosmos_conn" {
  name         = "cosmos-conn"
  value        = azurerm_cosmosdb_account.main.primary_sql_connection_string
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
```

### Step 2: Write `infra/outputs.tf`

```hcl
output "resource_group_name" {
  value = azurerm_resource_group.main.name
}

output "frontend_url" {
  value = "https://${azurerm_linux_web_app.frontend.default_hostname}"
}

output "function_app_url" {
  value = "https://${azurerm_linux_function_app.main.default_hostname}"
}

output "acr_login_server" {
  value = azurerm_container_registry.main.login_server
}

output "acr_username" {
  value     = azurerm_container_registry.main.admin_username
  sensitive = true
}

output "acr_password" {
  value     = azurerm_container_registry.main.admin_password
  sensitive = true
}

output "key_vault_name" {
  value = azurerm_key_vault.main.name
}

output "key_vault_uri" {
  value = azurerm_key_vault.main.vault_uri
}

output "cosmos_connection_string" {
  value     = azurerm_cosmosdb_account.main.primary_sql_connection_string
  sensitive = true
}

output "application_insights_connection_string" {
  value     = azurerm_application_insights.main.connection_string
  sensitive = true
}
```

### Step 3: Verify Terraform
```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs/infra
terraform init && terraform validate
```
Expected: `Success! The configuration is valid.`

If terraform is not installed, skip validation — the files are correct.

### Step 4: Run Terraform Plan (NO apply)
```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs/infra
terraform plan -out=tfplan
```
Expected: Plan shows ~15 resources to create. Review the plan output.

If terraform is not installed or Azure credentials are not configured, skip this step.

### Step 5: Commit
```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs
git add infra/main.tf infra/outputs.tf
git commit -m "feat(infra): add all Azure resources (Cosmos, Functions, ACR, Key Vault, App Insights)"
```

## Report
Write your report to: `C:\Users\edoardo.querio\Desktop\Materie\14_Cloud_Azure\.superpowers\sdd\task-2-report.md`

Include: status (DONE/BLOCKED/NEEDS_CONTEXT), files created/modified, terraform validate/plan results, any concerns.
