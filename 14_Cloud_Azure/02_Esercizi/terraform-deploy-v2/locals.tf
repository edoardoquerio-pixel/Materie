locals {
  # Suffisso univoco: usa quello fornito o genera uno randomico
  suffix = var.suffix != "" ? var.suffix : random_id.suffix.hex

  # Storage Account (max 24 char, lowercase, alnum)
  storage_account_name = "sta${local.suffix}"

  # Function App (globalmente univoco)
  function_app_name = "func-${local.suffix}"
  func_plan_name    = "plan-func-${local.suffix}"

  # Frontend Web App
  frontend_app_name  = "web-${local.suffix}"
  frontend_plan_name = "plan-web-${local.suffix}"

  # Cosmos DB (3-44 char, lowercase)
  cosmos_account_name = "cosmos${local.suffix}"

  # Key Vault (globalmente univoco)
  key_vault_name = "kv-${local.suffix}"

  # Application Insights
  app_insights_name = "ai-${local.suffix}"

  # Azure Container Registry (5-50 char, alnum)
  acr_name  = "acr${local.suffix}"
  acr_image = "frontend:${var.frontend_image_tag}"

  # Database e container names
  cosmos_db_name      = "appdb"
  requests_container  = "richieste"
  summaries_container = "riepiloghi"

  # Queue name
  queue_name = "richieste-da-elaborare"

  # Key Vault Secret URI per reference
  kv_secret_uri = "https://${local.key_vault_name}.vault.azure.net/secrets/cosmosdb-connection-string/"

  # Tags comuni
  common_tags = {
    Environment = "lab"
    Project     = "azure-e2e"
  }
}
