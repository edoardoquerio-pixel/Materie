resource \"random_id\" \"suffix\" {
  byte_length = 4
}

resource \"azurerm_resource_group\" \"rg\" {
  name     = var.resource_group_name
  location = var.location

  tags = {
    Environment = \"lab\"
    Project     = \"azure-e2e\"
  }
}

# =============================================================================
# STORAGE ACCOUNT (per AzureWebJobsStorage + Queue)
# =============================================================================
resource \"azurerm_storage_account\" \"func_storage\" {
  name                     = local.storage_account_name
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = \"Standard\"
  account_replication_type = \"LRS\"
  https_traffic_only_enabled = true

  tags = {
    Environment = \"lab\"
  }
}

# Queue per disaccoppiamento async (Lab 25)
resource \"azurerm_storage_queue\" \"richieste_queue\" {
  name                  = local.queue_name
  storage_account_name  = azurerm_storage_account.func_storage.name
}

# =============================================================================
# COSMOS DB (SQL API, Serverless)
# =============================================================================
resource \"azurerm_cosmosdb_account\" \"cosmosdb\" {
  name                = local.cosmos_account_name
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  offer_type          = \"Standard\"
  kind                = \"GlobalDocumentDB\"

  consistency_policy {
    consistency_level = \"Session\"
  }

  geo_location {
    location          = azurerm_resource_group.rg.location
    failover_priority = 0
  }

  capabilities {
    name = \"EnableServerless\"
  }

  tags = {
    Environment = \"lab\"
  }
}

resource \"azurerm_cosmosdb_sql_database\" \"db\" {
  name                = local.cosmos_db_name
  resource_group_name = azurerm_resource_group.rg.name
  account_name        = azurerm_cosmosdb_account.cosmosdb.name
}

# Container per le richieste - Partition key: /categoria (per query di riepilogo efficienti)
resource \"azurerm_cosmosdb_sql_container\" \"requests\" {
  name                = local.requests_container
  resource_group_name = azurerm_resource_group.rg.name
  account_name        = azurerm_cosmosdb_account.cosmosdb.name
  database_name       = azurerm_cosmosdb_sql_database.db.name
  partition_key_path  = \"/categoria\"
}

# Container per i riepiloghi - Partition key: /tipo
resource \"azurerm_cosmosdb_sql_container\" \"summaries\" {
  name                = local.summaries_container
  resource_group_name = azurerm_resource_group.rg.name
  account_name        = azurerm_cosmosdb_account.cosmosdb.name
  database_name       = azurerm_cosmosdb_sql_database.db.name
  partition_key_path  = \"/tipo\"
}

# =============================================================================
# APPLICATION INSIGHTS (Osservabilita - Lab 24)
# =============================================================================
resource \"azurerm_application_insights\" \"appinsights\" {
  name                = local.app_insights_name
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  application_type    = \"web\"
  workspace_id        = azurerm_log_analytics_workspace.law.id

  tags = {
    Environment = \"lab\"
  }
}

resource \"azurerm_log_analytics_workspace\" \"law\" {
  name                = \"law-\\"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = \"PerGB2018\"
  retention_in_days   = 30

  tags = {
    Environment = \"lab\"
  }
}

# =============================================================================
# KEY VAULT + SECRET (Segreti sicuri - Lab 24)
# =============================================================================
resource \"azurerm_key_vault\" \"kv\" {
  name                        = local.key_vault_name
  location                    = azurerm_resource_group.rg.location
  resource_group_name         = azurerm_resource_group.rg.name
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  sku_name                    = \"standard\"
  soft_delete_retention_days  = 7
  purge_protection_enabled    = false
  enable_rbac_authorization   = true

  tags = {
    Environment = \"lab\"
  }
}

data \"azurerm_client_config\" \"current\" {}

# Secret con la connection string di Cosmos DB
resource \"azurerm_key_vault_secret\" \"cosmos_secret\" {
  name         = \"cosmosdb-connection-string\"
  key_vault_id = azurerm_key_vault.kv.id
  value        = azurerm_cosmosdb_account.cosmosdb.connection_strings[0]
}

# =============================================================================
# FUNCTION APP (Backend serverless - Labs 23, 24, 25)
# =============================================================================
# Piano App Service dedicato (B1) - NECESSARIO per Always On + Timer Trigger
resource \"azurerm_service_plan\" \"func_plan\" {
  name                = local.func_plan_name
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type             = \"Linux\"
  sku_name            = var.function_app_sku

  tags = {
    Environment = \"lab\"
  }
}

resource \"azurerm_linux_function_app\" \"functionapp\" {
  name                       = local.function_app_name
  location                   = azurerm_resource_group.rg.location
  resource_group_name        = azurerm_resource_group.rg.name
  service_plan_id            = azurerm_service_plan.func_plan.id
  storage_account_name       = azurerm_storage_account.func_storage.name
  storage_account_access_key = azurerm_storage_account.func_storage.primary_access_key

  site_config {
    always_on = true
    application_stack {
      python_version = var.python_version
    }
    cors {
      allowed_origins = [\"*\"]
    }
  }

  identity {
    type = \"SystemAssigned\"
  }

  app_settings = {
    \"FUNCTIONS_WORKER_RUNTIME\"             = \"python\"
    \"WEBSITE_RUN_FROM_PACKAGE\"             = \"1\"
    \"PYTHON_ENABLE_WORKER_EXTENSIONS\"      = \"1\"
    
    # Cosmos DB - via Key Vault Reference (risolto a runtime)
    \"COSMOS_CONNECTION_STRING\"             = \"@Microsoft.KeyVault(SecretUri=\)\"
    
    # Application Insights
    \"APPLICATIONINSIGHTS_CONNECTION_STRING\" = azurerm_application_insights.appinsights.connection_string
    
    # Queue Storage (per output binding queue)
    \"QUEUE_STORAGE_CONNECTION\"             = azurerm_storage_account.func_storage.primary_connection_string
    
    # Alias per binding Cosmos DB (nome uniforme per tutte le function)
    \"COSMOS_DB\"                            = \"@Microsoft.KeyVault(SecretUri=\)\"
  }

  depends_on = [
    azurerm_cosmosdb_account.cosmosdb,
    azurerm_application_insights.appinsights,
    azurerm_key_vault_secret.cosmos_secret
  ]
}

# Role Assignment: Function App MI -> Key Vault Secrets User
resource \"azurerm_role_assignment\" \"kv_secrets_user\" {
  scope                = azurerm_key_vault.kv.id
  role_definition_name = \"Key Vault Secrets User\"
  principal_id         = azurerm_linux_function_app.functionapp.identity[0].principal_id
  principal_type       = \"ServicePrincipal\"

  depends_on = [
    azurerm_linux_function_app.functionapp,
    azurerm_key_vault.kv
  ]
}

# Restart Function App dopo role assignment per propagare KV reference
resource \"null_resource\" \"restart_functionapp\" {
  depends_on = [azurerm_role_assignment.kv_secrets_user]

  provisioner \"local-exec\" {
    command     = \"az functionapp restart --resource-group \ --name \\"
    interpreter = [\"bash\", \"-c\"]
  }

  triggers = {
    role_assignment = azurerm_role_assignment.kv_secrets_user.id
  }
}

# Deploy codice backend sulla Function App
resource \"null_resource\" \"deploy_backend\" {
  depends_on = [
    azurerm_linux_function_app.functionapp,
    azurerm_key_vault_secret.cosmos_secret,
    null_resource.restart_functionapp
  ]

  provisioner \"local-exec\" {
    command     = \"cd \/../../labs/backend && zip -r function_app.zip . -x *.pyc __pycache__/* .venv/* .terraform/* terraform.tfstate* && az functionapp deployment source config-zip --resource-group \ --name \ --src function_app.zip\"
    interpreter = [\"bash\", \"-c\"]
  }

  triggers = {
    function_app = azurerm_linux_function_app.functionapp.id
    source_hash  = filesha256(\"\/../../labs/backend/function_app.py\")
  }
}

# =============================================================================
# AZURE CONTAINER REGISTRY (per immagine frontend)
# =============================================================================
resource \"azurerm_container_registry\" \"acr\" {
  name                = local.acr_name
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = \"Basic\"
  admin_enabled       = true

  tags = {
    Environment = \"lab\"
  }
}

# =============================================================================
# FRONTEND CONTAINERIZZATO (App Service for Containers)
# =============================================================================
resource \"azurerm_service_plan\" \"frontend_plan\" {
  name                = local.frontend_plan_name
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type             = \"Linux\"
  sku_name            = var.frontend_sku

  tags = {
    Environment = \"lab\"
  }
}

resource \"azurerm_linux_web_app\" \"frontend\" {
  name                = local.frontend_app_name
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  service_plan_id     = azurerm_service_plan.frontend_plan.id

  identity {
    type = \"SystemAssigned\"
  }

  site_config {
    application_stack {
      docker_image_name        = local.acr_image
      docker_registry_url      = \"https://\\"
      docker_registry_username = azurerm_container_registry.acr.admin_username
      docker_registry_password = azurerm_container_registry.acr.admin_password
    }
  }

  https_only = true
}

# Role Assignment: Frontend MI -> AcrPull su ACR
resource \"azurerm_role_assignment\" \"frontend_acr_pull\" {
  scope                = azurerm_container_registry.acr.id
  role_definition_name = \"AcrPull\"
  principal_id         = azurerm_linux_web_app.frontend.identity[0].principal_id

  depends_on = [
    azurerm_linux_web_app.frontend,
    azurerm_container_registry.acr
  ]
}

# Build + Push immagine frontend su ACR (az acr build - build in cloud)
resource \"null_resource\" \"build_push_frontend\" {
  depends_on = [
    azurerm_container_registry.acr,
    azurerm_role_assignment.frontend_acr_pull
  ]

  provisioner \"local-exec\" {
    command     = \"az acr build -r \ -t \ \/../../labs/frontend\"
    interpreter = [\"bash\", \"-c\"]
  }

  triggers = {
    source_hash = filesha256(\"\/../../labs/frontend/index.html\")
  }
}

# Deploy container su Web App
resource \"null_resource\" \"deploy_frontend\" {
  depends_on = [
    azurerm_linux_web_app.frontend,
    null_resource.build_push_frontend,
    azurerm_role_assignment.frontend_acr_pull
  ]

  provisioner \"local-exec\" {
    command     = \"az webapp config container set --resource-group \ --name \ --docker-custom-image-name \/\\"
    interpreter = [\"bash\", \"-c\"]
  }
}