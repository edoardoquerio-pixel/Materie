# Design Spec — Applicazione E2E Azure (Lab 23 + 24 + 25)

## 1. Contesto

Esercitazione pratica end-to-end per il corso Microsoft Azure (100 ore).  
Costruire un servizio di registrazione richieste su Azure con:
- Frontend containerizzato
- Backend serverless (Azure Functions)
- Database NoSQL (Cosmos DB)
- Osservabilità (Application Insights)
- Sicurezza dei segreti (Key Vault + Managed Identity)
- Disaccoppiamento asincrono (Azure Storage Queue)
- Elaborazione schedulata (Timer Trigger)

**Stack scelto:** Python (Azure Functions v4)  
**Infrastruttura:** Terraform (plan prima del deploy)  
**Delivery:** PDF finale con screenshot, codice, schema architettura, motivazioni

---

## 2. Architettura

### 2.1 Componenti Azure

| Servizio | Ruolo | Piano |
|---|---|---|
| Resource Group | Contenitore logico | — |
| Azure Container Registry | Archivio immagini Docker | Basic |
| App Service Plan | Pianificazione Linux per il frontend | B1 (Linux) |
| App Service (Web App) | Frontend nginx containerizzato | — |
| Azure Functions | Backend serverless (5 function) | Consumption |
| Azure Cosmos DB | Database NoSQL (2 container) | Serverless |
| Application Insights | Telemetria e log | — |
| Azure Key Vault | Custodia segreti (connection string) | Standard |
| Storage Account | Coda + storage interno Functions | — |

### 2.2 Flussi

```
Flusso 1 (Sincrono):
  Utente → POST /api/crea_richiesta → crea_richiesta → Cosmos DB (richieste) → 201

Flusso 2 (Asincrono):
  Utente → POST /api/pubblica_richiesta → pubblica_richiesta → Coda → 202
  Coda → elabora_richiesta → Cosmos DB (richieste)

Flusso 3 (Lettura):
  Utente → GET /api/lista_richieste → lista_richieste → Cosmos DB (richieste) → 200

Flusso 4 (Timer):
  Timer (*/2 min) → riepilogo → legge Cosmos (richieste) → scrive Cosmos (riepiloghi)

Flusso 5 (Segreti):
  Functions (Managed Identity) → Key Vault → legge COSMOS_CONNECTION_STRING
```

### 2.3 Partition Key

**Scelta:** `/categoria`  
**Motivazione:** Le query di riepilogo raggruppano per categoria. La distribuzione è sufficientemente uniforme (supporto, bug, feature, generica). Il volume per singolo utente non giustifica una partizione per utente.

### 2.4 Naming Convention

```
SUFFIX=e2e07171436
RG=rg-e2e-lab-e2e07171436
COSMOS=cosmos-e2e07171436
FUNCTION_APP=funcapp-e2e07171436
ACR=acre2e07171436
WEBAPP=webappfrontend-e2e07171436
KEY_VAULT=kv-e2e07171436
APP_INSIGHTS=ai-e2e07171436
```

---

## 3. Struttura del Progetto

```
labs/
├── infra/
│   ├── main.tf              ← Tutte le risorse Azure
│   ├── variables.tf          ← Variabili (suffix, location, nomi)
│   ├── outputs.tf            ← Output (URL frontend, Function App, etc.)
│   ├── versions.tf           ← Provider Terraform
│   └── terraform.tfvars      ← Valori delle variabili
├── backend/
│   ├── function_app.py       ← 5 function Azure Functions
│   ├── host.json             ← Configurazione runtime + extension bundle
│   ├── requirements.txt      ← Dipendenze Python
│   └── local.settings.json   ← Configurazione locale (emulatore)
├── frontend/
│   ├── index.html            ← UI completa (3 form + elenco)
│   ├── Dockerfile            ← nginx:alpine
│   └── .dockerignore         ← Esclusioni build
├── scripts/
│   ├── deploy-acr.sh         ← Build + push immagine
│   ├── deploy-frontend.sh    ← Deploy App Service
│   └── setup-queue.sh        ← Creazione coda
└── docs/
    ├── report/
    │   └── report.md         ← Template PDF (Markdown → PDF)
    └── superpowers/
        └── specs/
            └── 2026-07-23-azure-e2e-design.md  ← Questo file
```

---

## 4. Backend — Azure Functions (Python)

### 4.1 Function: crea_richiesta
- **Trigger:** HTTP POST
- **Output binding:** Cosmos DB → container `richieste`
- **Response:** 201 Created con il documento creato
- **Auth:** Anonymous

### 4.2 Function: lista_richieste
- **Trigger:** HTTP GET
- **Input binding:** Cosmos DB ← container `richieste` (query: `SELECT * FROM c ORDER BY c.timestamp DESC`)
- **Response:** 200 OK con array di documenti
- **Auth:** Anonymous

### 4.3 Function: pubblica_richiesta
- **Trigger:** HTTP POST
- **Output binding:** Queue `richieste-da-elaborare`
- **Response:** 202 Accepted (messaggio preso in carico)
- **Auth:** Anonymous

### 4.4 Function: elabora_richiesta
- **Trigger:** Queue `richieste-da-elaborare`
- **Output binding:** Cosmos DB → container `richieste`
- **Logica:** Parsifica il messaggio dalla coda, aggiunge `elaborato_il` e `partitionKey`, scrive su Cosmos
- **Nessuna risposta HTTP** (non è raggiungibile dal web)

### 4.5 Function: riepilogo
- **Trigger:** Timer `0 */2 * * * *` (ogni 2 minuti)
- **Input binding:** Cosmos DB ← container `richieste` (query: `SELECT * FROM c`)
- **Output binding:** Cosmos DB → container `riepiloghi`
- **Logica:** Conta le richieste per categoria, genera documento riepilogo con id `riepilogo-<timestamp>`

### 4.6 Connection String Uniforme

**Bug fix:** Tutte le function useranno `COSMOS_CONNECTION_STRING` come nome della connection string, uniformando il codice attuale che mista `COSMOS_CONNECTION_STRING` e `COSMOS_DB`.

---

## 5. Frontend

### 5.1 Tecnologia
- HTML5 + CSS3 + JavaScript vanilla (nessun framework)
- Nessuna build step: file statici serviti da nginx

### 5.2 Sezioni UI
1. **Form Sincrono** — Nome + Messaggio → POST /api/crea_richiesta (201)
2. **Form Asincrono** — Nome + Messaggio + Categoria → POST /api/pubblica_richiesta (202)
3. **Elenco Richieste** — GET /api/lista_richieste, card per ogni messaggio
4. **Auto-detect** — URL Function App diverso per locale vs produzione

### 5.3 Dockerfile
- Base image: `nginx:alpine`
- Copia file statici in `/usr/share/nginx/html/`
- Expose port 80

---

## 6. Osservabilità (Lab 24)

### 6.1 Application Insights
- Collegato alla Function App tramite Terraform
- Telemetria automatica: requests, dependencies, exceptions, performance
- Log applicativi: `logging.info()` in ogni function

### 6.2 Query KQL documentate nel PDF
```kql
requests
| where timestamp > ago(1h)
| summarize count() by name, resultCode

traces
| where timestamp > ago(1h)
| where message startswith "CreaRichiesta" or message startswith "ListaRichieste"
```

---

## 7. Sicurezza dei Segreti (Lab 24)

### 7.1 Flusso
1. Key Vault creato con segreto `cosmos-conn` (connection string di Cosmos)
2. Managed Identity (System) assegnata alla Function App
3. Ruolo `Key Vault Secrets User` assegnato all'identità sul vault
4. App setting `COSMOS_CONNECTION_STRING` = `@Microsoft.KeyVault(SecretUri=...)`
5. Restart Function App + attesa ~1 min per propagazione

### 7.2 Terraform
- `azurerm_key_vault` + `azurerm_key_vault_secret`
- `azurerm_user_assigned_identity` (o system assigned via `identity { type = "SystemAssigned" }`)
- `azurerm_role_assignment` (Key Vault Secrets User)

---

## 8. Infrastruttura (Terraform)

### 8.1 Risorse da creare
- `azurerm_resource_group`
- `azurerm_cosmosdb_account` (serverless, API SQL)
- `azurerm_cosmosdb_sql_database` (appdb)
- `azurerm_cosmosdb_sql_container` (richieste, partition key /categoria)
- `azurerm_cosmosdb_sql_container` (riepiloghi, partition key /tipo)
- `azurerm_storage_account` (per Functions + coda)
- `azurerm_storage_queue` (richieste-da-elaborare)
- `azurerm_service_plan` (Linux B1)
- `azurerm_linux_web_app` (frontend containerizzato)
- `azurerm_container_registry` (ACR Basic)
- `azurerm_function_app` (Python, consumption)
- `azurerm_application_insights`
- `azurerm_key_vault` + `azurerm_key_vault_secret`
- `azurerm_role_assignment` (Key Vault Secrets User per Function App)

### 8.2 Outputs
- URL Frontend
- URL Function App
- Nome ACR
- Nome Key Vault

---

## 9. Note per il PDF Finale

### 9.1 Contenuto
- Schema architettura (aggiornato con tutti i flussi)
- Screenshot delle risorse nel portale Azure
- Screenshot del frontend online
- Screenshot di Cosmos DB (Data Explorer con item)
- Screenshot di Application Insights (requests, traces)
- Screenshot della coda (messaggi in attesa)
- Screenshot dei riepiloghi nel container
- Codice di ogni function con commenti
- Codice del frontend e Dockerfile
- Motivazioni delle scelte (partition key, App Service vs ACI, piano Consumption, etc.)

### 9.2 Struttura PDF
1. Introduzione e obiettivo
2. Architettura (diagramma + tabella servizi)
3. Lab 23: E2E (Cosmos DB → Functions → Frontend)
4. Lab 24: Osservabilità + Segreti
5. Lab 25: Coda + Timer
6. Errori encounterati e soluzioni
7. Conclusioni e motivazioni

---

## 10. Bug Fix

**Problema:** In `function_app.py`, `elabora_richiesta` e `riepilogo` usano `connection="COSMOS_DB"` mentre le altre usano `connection="COSMOS_CONNECTION_STRING"`. `local.settings.json` definisce solo `COSMOS_CONNECTION_STRING`.

**Fix:** Uniformare tutte le connection a `COSMOS_CONNECTION_STRING`.

**File da modificare:**
- `backend/function_app.py` — righe 171, 208, 214: `COSMOS_DB` → `COSMOS_CONNECTION_STRING`

---

## 11. Errori Tipici Documentati

| Errore | Causa | Soluzione |
|---|---|---|
| CORS bloccato dal browser | Function App senza CORS configurato | Aggiungere `*` o l'URL del frontend nelle CORS settings |
| Container non parte | ACR non autorizzato | Assegnare managed identity o credenziali al servizio |
| 500 dopo Key Vault reference | Permesso non propagato | Restart + attendere ~1 min |
| Timer non scatta | Always On spento | Attivare Always On (piano dedicato) |
| Coda non elaborata | Nome coda diverso tra function | Verificare che entrambe usano `richieste-da-elaborare` |
| Connection string mancante | Nome inconsistente | Uniformare a `COSMOS_CONNECTION_STRING` |
