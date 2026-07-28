# Task 2 Report — Terraform Main: All Azure Resources

## Status: DONE

## Files Created
| File | Description |
|------|-------------|
| `infra/main.tf` | All Azure resources (Resource Group, Cosmos DB, Storage, ACR, App Service Plan, Web App, Function App, Application Insights, Key Vault) |
| `infra/outputs.tf` | 10 outputs (resource group, frontend URL, function URL, ACR creds, Key Vault, Cosmos conn string, App Insights conn string) |

## Terraform Validate
**Result:** `Success! The configuration is valid, but there were some validation warnings.`

- Deprecation warnings about `partition_key_path` (will migrate to `partition_key_paths` in azurerm v4.0)
- Warnings are cosmetic and non-blocking

## Terraform Plan
**Result:** Plan succeeded — ~15 resources to create. Plan saved to `tfplan`.

Resources planned:
- `azurerm_resource_group.main`
- `azurerm_cosmosdb_account.main`
- `azurerm_cosmosdb_sql_database.main`
- `azurerm_cosmosdb_sql_container.richieste`
- `azurerm_cosmosdb_sql_container.riepiloghi`
- `azurerm_storage_account.main`
- `azurerm_storage_queue.richieste`
- `azurerm_container_registry.main`
- `azurerm_service_plan.frontend`
- `azurerm_linux_web_app.frontend`
- `azurerm_application_insights.main`
- `azurerm_linux_function_app.main`
- `azurerm_key_vault.main`
- `azurerm_key_vault_access_policy.deployer`
- `azurerm_key_vault_secret.cosmos_conn`
- `azurerm_key_vault_access_policy.function_app`

## Commit
```
63be493 feat(infra): add all Azure resources (Cosmos, Functions, ACR, Key Vault, App Insights)
```

## Concerns
- `partition_key_path` deprecation warnings — will need migration when upgrading to azurerm v4.0 (future task)
- No `terraform apply` was executed (as instructed — plan only)
