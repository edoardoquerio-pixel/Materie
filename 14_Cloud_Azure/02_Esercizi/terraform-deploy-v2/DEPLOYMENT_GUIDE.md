# Guida al Deployment - Azure E2E Lab (Esercitazioni 23, 24, 25)

> **Progetto:** Applicazione end-to-end Azure con Container (Frontend), Functions (Backend), Cosmos DB, Application Insights, Key Vault, Storage Queue, Timer Trigger
> **Target:** Azure via Terraform
> **Cartella:** `terraform-deploy-v2` (standalone, non usa file da `labs/`)

---

## Prerequisiti

- **Azure CLI** installato e autenticato (`az login`)
- **Terraform** >= 1.0 installato
- Subscription Azure selezionata (`az account set --subscription <SUBSCRIPTION_ID>`)
- Permessi: **Owner** o **Contributor + User Access Administrator** sulla subscription/RG

---

## Struttura Progetto

```
terraform-deploy-v2/
+-- versions.tf                 # Provider e versioni
+-- variables.tf                # Variabili di input
+-- locals.tf                   # Nomi risorse e naming convention
+-- main.tf                     # 21 risorse Azure + null_resource per deploy
+-- outputs.tf                  # Output utili (URL, connection string, nomi)
+-- terraform.tfvars.example    # Template per valori deployment
+-- backend/
|   +-- function_app.py         # 5 Functions Python (HTTP, Queue, Timer)
|   +-- host.json               # Extension bundle + logging
|   `-- requirements.txt        # Dipendenze Python
`-- frontend/
    +-- Dockerfile              # nginx:alpine per static files
    +-- index.html              # Frontend HTML+JS inline
    `-- .dockerignore
```

---

## Architettura Coperta (Labs 23+24+25)

```
+-----------+     HTTPS      +------------------+
|  Frontend |  ------------> |  Function App    |
| (Container)|                |  (5 Functions)   |
+-----------+                +--------+---------+
                                    |
         +--------------------------+--------------------------+
         v                          v                          v
   +-----------+            +------------+            +------------+
   |  Cosmos DB|<-- Output  |   Queue    |---> Queue  |  Timer     |
   |(2 container)   Binding |  Storage   |   Trigger  |  Trigger   |
   +-----------+            +------------+ (ElaboraRi) | (Riepilogo)|
        ^                                                    |
        |                          +-------------------------+
        |                          v
        |                    +------------+
        +------------------->|Key Vault   |
                             |(COSMOS_CONN)|
                             +------------+
                             
Application Insights (telemetria automatica + log custom)
```

### 5 Functions nel Function App

| Funzione | Trigger | Binding | Descrizione |
|----------|---------|---------|-------------|
| `crea_richiesta` | HTTP POST | Cosmos Output | Scrive direttamente su Cosmos (sync, 201) |
| `lista_richieste` | HTTP GET | Cosmos Input | Legge da Cosmos (query SQL) |
| `pubblica_richiesta` | HTTP POST | Queue Output | Mette in coda, risponde **202 Accepted** |
| `ElaboraRichiesta` | Queue Trigger | Cosmos Output | Svegliata dalla coda, scrive su Cosmos |
| `Riepilogo` | Timer (`*/2 * * * *`) | Cosmos In + Out | Legge richieste, conta per categoria, salva riepilogo |

---

## Variabili Principali (`terraform.tfvars`)

Copia `terraform.tfvars.example` -> `terraform.tfvars` e modifica:

```hcl
resource_group_name = "rg-azure-e2e-lab-mio-suffix"  # Deve essere univoco
location            = "polandcentral"                 # O la tua regione
suffix              = "lab01"                         # Suffisso nomi globali (ACR, KV, Cosmos, FuncApp)
python_version      = "3.12"
frontend_image_tag  = "v1"
function_app_sku    = "B1"        # OBBLIGATORIO per Always On + Timer
frontend_sku        = "B1"
cosmos_serverless   = true
```

> **Nota su `suffix`**: Se vuoto, Terraform genera 4 caratteri esadecimali casuali. Deve rendere univoci globalmente: ACR, Key Vault, Cosmos DB, Function App.

---

## Deployment Fase per Fase (Consigliato)

Il deployment **fase per fase** evita timeout e problemi di propagazione RBAC.

```bash
cd C:\Users\edoardo.querio\Desktop\Materie\14_Cloud_Azure\02_Esercizi\terraform-deploy-v2

# 1. Inizializza
terraform init

# 2. Crea tfvars
copy terraform.tfvars.example terraform.tfvars
# Modifica terraform.tfvars con i tuoi valori

# 3. Plan (vedi cosa verra creato)
terraform plan -var="suffix=lab01" -out=tfplan
```

### Fase 1: Infrastruttura Core (Storage, Cosmos, AppInsights, Key Vault, ACR, Piani)
```bash
terraform apply -target=azurerm_resource_group.rg `
  -target=random_id.suffix `
  -target=azurerm_storage_account.func_storage `
  -target=azurerm_storage_queue.richieste_queue `
  -target=azurerm_cosmosdb_account.cosmosdb `
  -target=azurerm_cosmosdb_sql_database.db `
  -target=azurerm_cosmosdb_sql_container.requests `
  -target=azurerm_cosmosdb_sql_container.summaries `
  -target=azurerm_log_analytics_workspace.law `
  -target=azurerm_application_insights.appinsights `
  -target=azurerm_key_vault.kv `
  -target=azurerm_key_vault_secret.cosmos_secret `
  -target=azurerm_container_registry.acr `
  -target=azurerm_service_plan.func_plan `
  -target=azurerm_service_plan.frontend_plan
```

### Fase 2: Function App + Key Vault Integration (RBAC + Restart)
```bash
terraform apply -target=azurerm_linux_function_app.functionapp `
  -target=azurerm_role_assignment.kv_secrets_user `
  -target=null_resource.restart_functionapp
```
> **Importante**: Il `null_resource.restart_functionapp` riavvia la Function App dopo l'assegnazione del ruolo `Key Vault Secrets User` per propagare il Key Vault Reference.

### Fase 3: Frontend (ACR Build + Deploy)
```bash
terraform apply -target=null_resource.build_push_frontend `
  -target=null_resource.deploy_frontend
```

### Fase 4: Backend Code Deploy
```bash
terraform apply -target=null_resource.deploy_backend
```

### Fase 5: Apply Completo (verifica tutto)
```bash
terraform apply
```

---

## Verifica Post-Deployment

```bash
# URL utili
terraform output function_app_url
terraform output frontend_url

# Test funzione sincrona (crea_richiesta)
curl -X POST $(terraform output -raw function_app_url)/api/crea_richiesta `
  -H "Content-Type: application/json" `
  -d '{"utente":"test","messaggio":"ciao sincrono","categoria":"test"}'

# Test funzione asincrona (pubblica_richiesta) - deve tornare 202
curl -X POST $(terraform output -raw function_app_url)/api/pubblica_richiesta `
  -H "Content-Type: application/json" `
  -d '{"utente":"test","messaggio":"async","categoria":"test"}'

# Lista richieste
curl $(terraform output -raw function_app_url)/api/lista_richieste

# Verifica frontend
curl -I $(terraform output -raw frontend_url)
```

### Controlli nel Portale Azure
1. **Function App** -> Functions: vedi 5 funzioni (crea_richiesta, lista_richieste, pubblica_richiesta, ElaboraRichiesta, Riepilogo)
2. **Storage Account** -> Queue `richieste-da-elaborare`: messaggi in coda
3. **Cosmos DB** -> Data Explorer: container `richieste` (partition `/categoria`) e `riepiloghi` (partition `/tipo`)
4. **Application Insights** -> Live Metrics, Failures, Performance, Logs (tabella `traces`)
5. **Key Vault** -> Secret `cosmosdb-connection-string` + Access Policies / RBAC

---

## Criticita Note e Fix Applicati

| # | Criticita | Fix Applicato |
|---|-----------|---------------|
| 1 | **Function App SKU** | Usato **B1 (Basic)**, non Consumption. *Always On + Timer Trigger richiedono piano dedicato* |
| 2 | **Key Vault Reference** | `COSMOS_CONNECTION_STRING` e `COSMOS_DB` usano `@Microsoft.KeyVault(SecretUri=...)` con URI corretto |
| 3 | **Binding Connection String Uniforme** | Tutte le 5 funzioni usano `connection="COSMOS_CONNECTION_STRING"` (fix: prima `crea_richiesta` e `ElaboraRichiesta` usavano `COSMOS_DB`) |
| 4 | **RBAC Propagation** | `null_resource.restart_functionapp` riavvia la Function App dopo role assignment |
| 5 | **Partition Key Cosmos** | `richieste` su `/categoria` (match query Riepilogo), `riepiloghi` su `/tipo` |
| 6 | **CORS** | Configurato `["*"]` in Terraform (restringere post-deploy via CLI: `az functionapp cors remove ...`) |
| 7 | **ACR Admin + AcrPull** | Admin abilitato per build iniziale, MI del frontend riceve ruolo `AcrPull` |
| 8 | **Single Storage Account** | Usato per Functions (`AzureWebJobsStorage`) + Queue (OK per lab, separare in prod) |
| 9 | **Timer Trigger Schedule** | `0 */2 * * * *` (6 campi: secondi minuti ore giorno mese giorno-settimana) = ogni 2 min |
| 10 | **Python Version** | 3.12 specificata in `variables.tf` e `site_config.application_stack` |
| 11 | **Frontend JS Config** | `index.html` include config auto-detect (localhost vs Azure) per Function App URL |
| 12 | **Null Resource Paths** | Usano `${path.module}/../backend` e `${path.module}/../frontend` (relativi alla cartella terraform) |

---

## Pulizia Risorse

```bash
# Distrugge tutto (attenzione: Key Vault con purge_protection=false)
terraform destroy -auto-approve

# Se Key Vault non si elimina (soft delete), purga manualmente:
az keyvault purge --name <kv-name> --location <location>
```

---

## Troubleshooting Comune

| Errore | Causa | Soluzione |
|--------|-------|-----------|
| `Key Vault reference not resolved` | Ruolo non propagato / Function App non riavviata | Verifica `restart_functionapp` eseguito, attendi 1-2 min |
| `500 Internal Server Error` su funzione | Connection string non risolta / Binding errato | Controlla App Settings -> `COSMOS_CONNECTION_STRING` = `@Microsoft.KeyVault(...)` |
| `CORS error` da browser | Origin non permessa | `az functionapp cors add -g <rg> -n <func> --allowed-origins https://<frontend-url>` |
| `Timer trigger non parte` | Function App su Consumption / Always Off | Verifica SKU = B1 e `always_on = true` in `site_config` |
| `ACR pull failed` | Ruolo `AcrPull` non assegnato / Admin disabled | Verifica `azurerm_role_assignment.frontend_acr_pull` e `admin_enabled = true` |
| `Queue trigger non sveglia` | Connection string errata / Nome coda | Verifica `QUEUE_STORAGE_CONNECTION` e `queue_name = "richieste-da-elaborare"` |

---

## Note per Produzione (Non Applicate Qui)

- [ ] Separare Storage Account per Functions e Queue
- [ ] ACR SKU Premium + geo-replication
- [ ] Key Vault `purge_protection_enabled = true`
- [ ] CORS restrittivo (solo frontend URL)
- [ ] Private Endpoints per Cosmos, Storage, Key Vault
- [ ] Application Insights sampling tuning
- [ ] Managed Identity per Storage/Queue invece di connection string
- [ ] Azure Front Door / App Gateway + WAF davanti al frontend
- [ ] Backup/DR per Cosmos DB
- [ ] Monitoring/Alerting su metriche chiave (errori, latenza, coda length)

---

## Riferimenti Documentazione Microsoft

- [Azure Functions Python Developer Guide](https://learn.microsoft.com/azure/azure-functions/functions-reference-python)
- [Cosmos DB Bindings for Azure Functions](https://learn.microsoft.com/azure/azure-functions/functions-bindings-cosmosdb-v2)
- [Key Vault References for App Service](https://learn.microsoft.com/azure/app-service/app-service-key-vault-references)
- [Application Insights for Azure Functions](https://learn.microsoft.com/azure/azure-functions/configure-monitoring)
- [Queue Storage Trigger/Output Binding](https://learn.microsoft.com/azure/azure-functions/functions-bindings-storage-queue)
- [Timer Trigger](https://learn.microsoft.com/azure/azure-functions/functions-bindings-timer)
- [App Service for Containers](https://learn.microsoft.com/azure/app-service/quickstart-docker)
- [ACR Build](https://learn.microsoft.com/azure/container-registry/container-registry-tutorial-quick-build)
