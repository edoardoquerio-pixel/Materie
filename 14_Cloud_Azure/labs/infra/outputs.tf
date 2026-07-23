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
