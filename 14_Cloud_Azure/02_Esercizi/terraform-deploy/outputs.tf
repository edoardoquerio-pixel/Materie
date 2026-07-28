output \"function_app_url\" {
  description = \"Base URL della Function App\"
  value       = \"https://\\"
}

output \"frontend_url\" {
  description = \"URL del frontend containerizzato\"
  value       = \"https://\\"
}

output \"acr_login_server\" {
  description = \"Login server dell Azure Container Registry\"
  value       = azurerm_container_registry.acr.login_server
}

output \"key_vault_uri\" {
  description = \"URI del Key Vault\"
  value       = azurerm_key_vault.kv.vault_uri
}

output \"key_vault_secret_uri\" {
  description = \"URI completo del secret Cosmos DB connection string (per Key Vault reference)\"
  value       = azurerm_key_vault_secret.cosmos_secret.id
  sensitive   = true
}

output \"cosmos_connection_string\" {
  description = \"Connection string per Cosmos DB (sensitive)\"
  value       = azurerm_cosmosdb_account.cosmosdb.connection_strings[0]
  sensitive   = true
}

output \"storage_connection_string\" {
  description = \"Connection string per Storage Account (Queue)\"
  value       = azurerm_storage_account.func_storage.primary_connection_string
  sensitive   = true
}

output \"resource_group_name\" {
  description = \"Nome del Resource Group\"
  value       = azurerm_resource_group.rg.name
}

output \"function_app_name\" {
  description = \"Nome della Function App\"
  value       = azurerm_linux_function_app.functionapp.name
}

output \"frontend_app_name\" {
  description = \"Nome della Web App frontend\"
  value       = azurerm_linux_web_app.frontend.name
}

output \"cosmos_account_name\" {
  description = \"Nome dell account Cosmos DB\"
  value       = azurerm_cosmosdb_account.cosmosdb.name
}