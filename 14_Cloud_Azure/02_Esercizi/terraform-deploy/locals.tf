locals {
  # Suffisso univoco: usa quello fornito o genera uno randomico
  suffix                = var.suffix != \"\" ? var.suffix : random_id.suffix.hex
  
  # Storage Account (max 24 char, lowercase, alnum)
  storage_account_name  = \"sta\\"
  
  # Function App (globalmente univoco)
  function_app_name     = \"func-\\"
  func_plan_name        = \"plan-func-\\"
  
  # Frontend Web App
  frontend_app_name     = \"web-\\"
  frontend_plan_name    = \"plan-web-\\"
  
  # Cosmos DB (3-44 char, lowercase)
  cosmos_account_name   = \"cosmos\\"
  
  # Key Vault (globalmente univoco)
  key_vault_name        = \"kv-\\"
  
  # Application Insights
  app_insights_name     = \"ai-\\"
  
  # Azure Container Registry (5-50 char, alnum)
  acr_name              = \"acr\\"
  acr_image             = \"frontend:\\"
  
  # Database e container names
  cosmos_db_name        = \"appdb\"
  requests_container    = \"richieste\"
  summaries_container   = \"riepiloghi\"
  
  # Queue name
  queue_name            = \"richieste-da-elaborare\"
}