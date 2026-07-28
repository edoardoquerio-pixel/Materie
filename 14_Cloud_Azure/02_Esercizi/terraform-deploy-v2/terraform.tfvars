# Terraform Variables Example
# Copia questo file in terraform.tfvars e modifica i valori

# Nome del Resource Group (deve essere univoco nella subscription)
resource_group_name = "rg-azure-e2e-lab-esercizio"

# Regione Azure per tutte le risorse
location = "francecentral"

# Suffisso univoco per i nomi delle risorse globali (ACR, Key Vault, Cosmos DB, Function App)
# Se vuoto, viene generato automaticamente (4 caratteri esadecimali)
suffix = ""

# Versione Python per Azure Functions
python_version = "3.12"

# Tag per l immagine Docker del frontend
frontend_image_tag = "v1"

# SKU per il piano App Service della Function App
# B1 = Basic (necessario per Always On + Timer Trigger)
# Nota: Consumption NON supporta Always On, quindi i Timer Trigger non funzionerebbero
function_app_sku = "B1"

# SKU per il piano App Service del Frontend
frontend_sku = "B1"

# Abilita modalita serverless per Cosmos DB
cosmos_serverless = true
