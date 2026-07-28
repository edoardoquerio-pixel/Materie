# Azure E2E Lab (23+24+25) — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a complete Azure E2E application with containerized frontend, serverless Python backend, Cosmos DB, Application Insights, Key Vault, queue-based decoupling, and timer-based summarization.

**Architecture:** Frontend (nginx container on App Service) calls Azure Functions (Python, consumption plan). Functions use Cosmos DB bindings (no connection code). Queue decouples write path. Timer generates periodic summaries. Key Vault stores secrets via managed identity. Application Insights provides observability.

**Tech Stack:** Python 3.11+, Azure Functions v4, Cosmos DB (SQL API, serverless), Azure Container Registry, App Service for Containers (Linux B1), Azure Storage Queue, Application Insights, Azure Key Vault, Terraform, nginx, HTML/CSS/JS vanilla.

## Global Constraints

- Python 3.11+ for Azure Functions
- Azure Functions Extension Bundle `[4.*, 5.0.0)`
- Cosmos DB API: SQL (Core)
- Partition key: `/categoria` for `richieste`, `/tipo` for `riepiloghi`
- Connection string name: `COSMOS_CONNECTION_STRING` (uniform across all functions)
- Queue name: `richieste-da-elaborare`
- Timer schedule: `0 */2 * * * *` (6-field CRON, every 2 minutes)
- Auth level: Anonymous for all HTTP triggers
- Location: `francecentral`
- Suffix: `e2e07171436`

---

## File Map

| File | Action | Purpose |
|---|---|---|
| `infra/variables.tf` | Create | Input variables |
| `infra/versions.tf` | Modify | Provider config (exists, needs update) |
| `infra/terraform.tfvars` | Create | Variable values |
| `infra/main.tf` | Create | All Azure resources |
| `infra/outputs.tf` | Create | Resource outputs |
| `backend/function_app.py` | Rewrite | All 5 functions |
| `backend/host.json` | Rewrite | Runtime config |
| `backend/requirements.txt` | Rewrite | Python deps |
| `backend/local.settings.json` | Rewrite | Local dev config |
| `frontend/index.html` | Rewrite | Complete UI |
| `frontend/Dockerfile` | Rewrite | nginx build |
| `frontend/.dockerignore` | Rewrite | Build exclusions |
| `scripts/deploy-acr.sh` | Create | Build + push image |
| `scripts/deploy-frontend.sh` | Create | Deploy App Service |
| `scripts/setup-queue.sh` | Create | Create Storage Queue |
| `docs/report/report.md` | Create | PDF template |

---

### Task 1: Project Structure + Terraform Variables

**Files:**
- Create: `infra/variables.tf`
- Create: `infra/terraform.tfvars`
- Modify: `infra/versions.tf`

**Interfaces:**
- Consumes: None (first task)
- Produces: Variable definitions consumed by `main.tf`

- [ ] **Step 1: Create infra directory**

```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs
mkdir -p infra scripts docs/report
```

- [ ] **Step 2: Write `infra/variables.tf`**

```hcl
variable "suffix" {
  description = "Unique suffix for all resources"
  type        = string
  default     = "e2e07171436"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "francecentral"
}

variable "resource_group_name" {
  description = "Resource group name"
  type        = string
  default     = "rg-e2e-lab"
}

locals {
  name_prefix = "e2e${var.suffix}"

  cosmos_account   = "cosmos-${local.name_prefix}"
  cosmos_db        = "appdb"
  cosmos_container = "richieste"
  cosmos_riepiloghi = "riepiloghi"

  function_app = "funcapp-${local.name_prefix}"
  acr_name     = "acr${local.name_prefix}"
  webapp_name  = "webappfrontend-${local.name_prefix}"
  webapp_plan  = "planfrontend-${local.name_prefix}"

  key_vault     = "kv-${local.name_prefix}"
  app_insights  = "ai-${local.name_prefix}"
  storage_account = "st${local.name_prefix}"

  queue_name = "richieste-da-elaborare"

  tags = {
    project = "azure-e2e-lab"
    suffix  = var.suffix
  }
}
```

- [ ] **Step 3: Write `infra/terraform.tfvars`**

```hcl
suffix          = "e2e07171436"
location        = "francecentral"
resource_group_name = "rg-e2e-lab"
```

- [ ] **Step 4: Update `infra/versions.tf`**

```hcl
terraform {
  required_version = ">= 1.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.30"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {
    resource_group {
      prevent_deletion_if_contains_resources = false
    }
    key_vault {
      purge_soft_delete_on_destroy = true
    }
  }
}
```

- [ ] **Step 5: Verify Terraform syntax**

Run: `cd infra && terraform init && terraform validate`
Expected: `Success! The configuration is valid.`

- [ ] **Step 6: Commit**

```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs
git add infra/variables.tf infra/terraform.tfvars infra/versions.tf
git commit -m "feat(infra): add Terraform variables and provider config"
```

---

### Task 2: Terraform Main — All Azure Resources

**Files:**
- Create: `infra/main.tf`
- Create: `infra/outputs.tf`

**Interfaces:**
- Consumes: Variables from Task 1 (`locals.*`, `var.*`)
- Produces: Resource IDs used in outputs

- [ ] **Step 1: Write `infra/main.tf`**

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

- [ ] **Step 2: Write `infra/outputs.tf`**

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

- [ ] **Step 3: Verify Terraform**

Run: `cd infra && terraform init && terraform validate`
Expected: `Success! The configuration is valid.`

- [ ] **Step 4: Run Terraform Plan (NO apply)**

Run: `cd infra && terraform plan -out=tfplan`
Expected: Plan shows ~15 resources to create. Review the plan output.

- [ ] **Step 5: Commit**

```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs
git add infra/main.tf infra/outputs.tf
git commit -m "feat(infra): add all Azure resources (Cosmos, Functions, ACR, Key Vault, App Insights)"
```

---

### Task 3: Backend — Azure Functions (All 5)

**Files:**
- Rewrite: `backend/function_app.py`
- Rewrite: `backend/host.json`
- Rewrite: `backend/requirements.txt`
- Rewrite: `backend/local.settings.json`

**Interfaces:**
- Consumes: `COSMOS_CONNECTION_STRING` and `QUEUE_STORAGE_CONNECTION` from app settings
- Produces: HTTP endpoints `/api/crea_richiesta`, `/api/lista_richieste`, `/api/pubblica_richiesta`; queue consumer `ElaboraRichiesta`; timer `Riepilogo`

- [ ] **Step 1: Write `backend/requirements.txt`**

```txt
azure-functions
```

- [ ] **Step 2: Write `backend/host.json`**

```json
{
  "version": "2.0",
  "logging": {
    "applicationInsights": {
      "samplingSettings": {
        "isEnabled": true,
        "excludedTypes": "Request"
      }
    }
  },
  "extensionBundle": {
    "id": "Microsoft.Azure.Functions.ExtensionBundle",
    "version": "[4.*, 5.0.0)"
  }
}
```

- [ ] **Step 3: Write `backend/local.settings.json`**

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "COSMOS_CONNECTION_STRING": "AccountEndpoint=https://localhost:8081/;AccountKey=C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==;",
    "QUEUE_STORAGE_CONNECTION": "UseDevelopmentStorage=true"
  }
}
```

- [ ] **Step 4: Write `backend/function_app.py`**

```python
import azure.functions as func
import json
import uuid
import logging
from datetime import datetime, timezone

app = func.FunctionApp()


# ══════════════════════════════════════════════════════════════════════════════
# crea_richiesta — HTTP POST → Cosmos DB (sincrono, 201 Created)
# ══════════════════════════════════════════════════════════════════════════════
@app.route(route="crea_richiesta", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
@app.cosmos_db_output(
    arg_name="doc",
    database_name="appdb",
    container_name="richieste",
    connection="COSMOS_CONNECTION_STRING",
)
def crea_richiesta(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info("CreaRichiesta: richiesta POST ricevuta.")

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            json.dumps({"errore": "JSON non valido"}),
            status_code=400,
            mimetype="application/json",
        )

    utente = req_body.get("utente")
    messaggio = req_body.get("messaggio")
    categoria = req_body.get("categoria", "generica")

    if not utente or not messaggio:
        return func.HttpResponse(
            json.dumps({"errore": "Campi obbligatori mancanti: utente, messaggio"}),
            status_code=400,
            mimetype="application/json",
        )

    documento = {
        "id": str(uuid.uuid4()),
        "utente": utente,
        "messaggio": messaggio,
        "categoria": categoria,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "partitionKey": categoria,
    }

    doc.set(func.Document.from_json(json.dumps(documento)))

    logging.info("CreaRichiesta: creata richiesta id='%s' utente='%s' categoria='%s'.",
                 documento["id"], utente, categoria)

    return func.HttpResponse(
        json.dumps(documento, ensure_ascii=False),
        status_code=201,
        mimetype="application/json",
    )


# ══════════════════════════════════════════════════════════════════════════════
# lista_richieste — HTTP GET ← Cosmos DB (input binding, 200 OK)
# ══════════════════════════════════════════════════════════════════════════════
@app.route(route="lista_richieste", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
@app.cosmos_db_input(
    arg_name="docs",
    database_name="appdb",
    container_name="richieste",
    connection="COSMOS_CONNECTION_STRING",
    sql_query="SELECT * FROM c ORDER BY c.timestamp DESC",
)
def lista_richieste(req: func.HttpRequest, docs: func.DocumentList) -> func.HttpResponse:
    logging.info("ListaRichieste: richiesta GET ricevuta.")

    items = []
    for doc in docs:
        items.append(json.loads(doc.to_json()))

    logging.info("ListaRichieste: restituiti %d documenti.", len(items))

    return func.HttpResponse(
        json.dumps(items, ensure_ascii=False),
        status_code=200,
        mimetype="application/json",
    )


# ══════════════════════════════════════════════════════════════════════════════
# pubblica_richiesta — HTTP POST → Queue (asincrono, 202 Accepted)
# ══════════════════════════════════════════════════════════════════════════════
@app.route(route="pubblica_richiesta", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
@app.queue_output(
    arg_name="outputQueueItem",
    queue_name="richieste-da-elaborare",
    connection="QUEUE_STORAGE_CONNECTION",
)
def pubblica_richiesta(
    req: func.HttpRequest,
    outputQueueItem: func.Out[str],
) -> func.HttpResponse:
    logging.info("PubblicaRichiesta: richiesta POST ricevuta.")

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            json.dumps({"errore": "JSON non valido"}),
            status_code=400,
            mimetype="application/json",
        )

    utente = req_body.get("utente")
    messaggio = req_body.get("messaggio")
    categoria = req_body.get("categoria", "generica")

    if not utente or not messaggio:
        return func.HttpResponse(
            json.dumps({"errore": "Campi obbligatori mancanti: utente, messaggio"}),
            status_code=400,
            mimetype="application/json",
        )

    item = {
        "id": str(uuid.uuid4()),
        "utente": utente,
        "messaggio": messaggio,
        "categoria": categoria,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    outputQueueItem.set(json.dumps(item, ensure_ascii=False))

    logging.info("PubblicaRichiesta: messaggio pubblicato sulla coda, id='%s'.", item["id"])

    return func.HttpResponse(
        json.dumps({
            "messaggio": "Richiesta presa in carico, verra' elaborata a breve",
            "id": item["id"],
        }, ensure_ascii=False),
        status_code=202,
        mimetype="application/json",
    )


# ══════════════════════════════════════════════════════════════════════════════
# elabora_richiesta — Queue Trigger → Cosmos DB (output binding)
# ══════════════════════════════════════════════════════════════════════════════
@app.function_name(name="ElaboraRichiesta")
@app.queue_trigger(
    arg_name="queueItem",
    queue_name="richieste-da-elaborare",
    connection="QUEUE_STORAGE_CONNECTION",
)
@app.cosmos_db_output(
    arg_name="outputDocument",
    database_name="appdb",
    container_name="richieste",
    connection="COSMOS_CONNECTION_STRING",
)
def elabora_richiesta(
    queueItem: func.QueueMessage,
    outputDocument: func.Out[func.Document],
):
    body = queueItem.get_body().decode("utf-8")
    logging.info("ElaboraRichiesta: messaggio ricevuto dalla coda: %s", body)

    item = json.loads(body)
    item["elaborato_il"] = datetime.now(timezone.utc).isoformat()
    item["partitionKey"] = item.get("categoria", "generica")

    outputDocument.set(func.Document.from_json(json.dumps(item)))

    logging.info("ElaboraRichiesta: documento scritto su Cosmos, id='%s'.", item["id"])


# ══════════════════════════════════════════════════════════════════════════════
# riepilogo — Timer Trigger (*/2 min) → Cosmos DB input + output
# ══════════════════════════════════════════════════════════════════════════════
@app.function_name(name="Riepilogo")
@app.timer_trigger(
    arg_name="myTimer",
    schedule="0 */2 * * * *",
)
@app.cosmos_db_input(
    arg_name="documents",
    database_name="appdb",
    container_name="richieste",
    connection="COSMOS_CONNECTION_STRING",
    sql_query="SELECT * FROM c",
)
@app.cosmos_db_output(
    arg_name="outputDocument",
    database_name="appdb",
    container_name="riepiloghi",
    connection="COSMOS_CONNECTION_STRING",
)
def riepilogo(
    myTimer: func.TimerRequest,
    documents: func.DocumentList,
    outputDocument: func.Out[func.Document],
):
    logging.info("Riepilogo: funzione timer attivata.")

    all_docs = list(documents) if documents else []

    conteggio = {}
    for doc in all_docs:
        raw = doc.to_json() if hasattr(doc, "to_json") else json.dumps(doc)
        d = json.loads(raw) if isinstance(raw, str) else raw
        cat = d.get("categoria", "generica")
        conteggio[cat] = conteggio.get(cat, 0) + 1

    riepilogo_doc = {
        "id": "riepilogo-" + datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ"),
        "tipo": "riepilogo",
        "totale": len(all_docs),
        "perCategoria": conteggio,
        "generatoIl": datetime.now(timezone.utc).isoformat(),
    }

    outputDocument.set(func.Document.from_json(json.dumps(riepilogo_doc)))

    logging.info(
        "Riepilogo: %d richieste totali, %d categorie. Riepilogo salvato.",
        len(all_docs),
        len(conteggio),
    )
```

- [ ] **Step 5: Verify Python syntax**

Run: `cd backend && python -c "import py_compile; py_compile.compile('function_app.py', doraise=True)"`
Expected: No output (success)

- [ ] **Step 6: Commit**

```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs
git add backend/
git commit -m "feat(backend): add all 5 Azure Functions (crea, lista, pubblica, elabora, riepilogo)"
```

---

### Task 4: Frontend — HTML + Dockerfile

**Files:**
- Rewrite: `frontend/index.html`
- Rewrite: `frontend/Dockerfile`
- Rewrite: `frontend/.dockerignore`

**Interfaces:**
- Consumes: Function App URL (hardcoded for production, auto-detect for local)
- Produces: Static HTML served by nginx on port 80

- [ ] **Step 1: Write `frontend/index.html`**

```html
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Azure E2E Lab - Richieste</title>
    <style>
        body {font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 20px; background-color: #f5f5f5;}
        .container {max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);}
        h1 {color: #0078d4; text-align: center; margin-bottom: 30px;}
        .section {margin-bottom: 30px; padding: 20px; border: 1px solid #e0e0e0; border-radius: 6px; background-color: #fafafa;}
        .section h2 {margin-top: 0; color: #333;}
        label {display: block; margin-bottom: 5px; font-weight: bold;}
        input[type="text"], textarea {width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; margin-bottom: 15px; font-family: inherit;}
        textarea {resize: vertical; min-height: 80px;}
        button {background-color: #0078d4; color: white; border: none; padding: 12px 24px; border-radius: 4px; cursor: pointer; font-size: 16px; transition: background-color 0.2s;}
        button:hover {background-color: #005a9e;}
        button:disabled {background-color: #cccccc; cursor: not-allowed;}
        .result {margin-top: 15px; padding: 10px; border-radius: 4px;}
        .success {background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb;}
        .error {background-color: #f8d7da; color: #721c24; border: 1px solid #f5c6cb;}
        .message-card {background: #f8f9fa; border-left: 4px solid #0078d4; padding: 15px; margin-bottom: 15px; border-radius: 0 4px 4px 0;}
        .message-header {display: flex; justify-content: space-between; margin-bottom: 8px;}
        .message-author {font-weight: bold; color: #0078d4;}
        .message-time {font-size: 0.85em; color: #666;}
        .message-content {margin-bottom: 10px; line-height: 1.5;}
        .message-category {font-size: 0.8em; color: #888; font-style: italic;}
        .empty-state {text-align: center; color: #666; font-style: italic; padding: 40px 20px;}
        .spinner {display: inline-block; width: 16px; height: 16px; border: 2px solid rgba(255,255,255,0.3); border-radius: 50%; border-top-color: white; animation: spin 0.8s ease-in-out infinite; vertical-align: middle; margin-left: 8px;}
        @keyframes spin {to {transform: rotate(360deg);}}
        .subtitle {color: #666; font-size: 0.9em; margin-bottom: 15px;}
    </style>
</head>
<body>
    <div class="container">
        <h1>Azure E2E Lab - Registrazione Richieste</h1>

        <!-- Form Sincrono (Lab 23) -->
        <div class="section">
            <h2>Invia Richiesta (Sincrono - 201)</h2>
            <p class="subtitle">Scrive direttamente su Cosmos DB. L'utente aspetta la scrittura.</p>
            <form id="syncForm">
                <label for="syncUser">Nome:</label>
                <input type="text" id="syncUser" placeholder="Il tuo nome" required>
                <label for="syncMsg">Messaggio:</label>
                <textarea id="syncMsg" placeholder="Il tuo messaggio" rows="3" required></textarea>
                <button type="submit" id="syncBtn">Invia Messaggio <span class="spinner" style="display:none;"></span></button>
            </form>
            <div id="syncResult" class="result" style="display:none;"></div>
        </div>

        <!-- Form Asincrono (Lab 25) -->
        <div class="section">
            <h2>Invia Richiesta (Asincrono - 202)</h2>
            <p class="subtitle">Mette in coda e risponde subito 202. ElaboraRichiesta la processera' in background.</p>
            <form id="asyncForm">
                <label for="asyncUser">Nome:</label>
                <input type="text" id="asyncUser" placeholder="Il tuo nome" required>
                <label for="asyncMsg">Messaggio:</label>
                <textarea id="asyncMsg" placeholder="Il tuo messaggio" rows="3" required></textarea>
                <label for="asyncCat">Categoria:</label>
                <input type="text" id="asyncCat" placeholder="es. supporto, bug, feature" value="generica">
                <button type="submit" id="asyncBtn">Pubblica in Coda <span class="spinner" style="display:none;"></span></button>
            </form>
            <div id="asyncResult" class="result" style="display:none;"></div>
        </div>

        <!-- Elenco (Lab 23) -->
        <div class="section">
            <h2>Richieste Ricevute</h2>
            <button id="refreshBtn">Aggiorna Elenco <span class="spinner" style="display:none;"></span></button>
            <div id="results" style="margin-top: 20px;"></div>
        </div>
    </div>

    <script>
        const isLocal = window.location.hostname === 'localhost';
        const config = {
            functionAppUrl: isLocal
                ? 'http://localhost:7071'
                : 'https://funcapp-e2e07171436.azurewebsites.net'
        };

        function setBtnLoading(btn, loading) {
            btn.disabled = loading;
            const sp = btn.querySelector('.spinner');
            if (sp) sp.style.display = loading ? 'inline-block' : 'none';
        }

        function showResult(el, msg, type) {
            el.style.display = 'block';
            el.className = 'result ' + type;
            el.textContent = msg;
        }

        // ─── Form Sincrono ──────────────────────────────────────────────
        document.getElementById('syncForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = document.getElementById('syncBtn');
            const result = document.getElementById('syncResult');
            setBtnLoading(btn, true);
            result.style.display = 'none';

            try {
                const res = await fetch(config.functionAppUrl + '/api/crea_richiesta', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        utente: document.getElementById('syncUser').value.trim(),
                        messaggio: document.getElementById('syncMsg').value.trim()
                    })
                });
                const data = await res.json();
                if (!res.ok) throw new Error(data.errore || 'Errore ' + res.status);
                showResult(result, 'Messaggio inviato! ID: ' + data.id, 'success');
                e.target.reset();
                loadMessages();
            } catch (err) {
                showResult(result, 'Errore: ' + err.message, 'error');
            } finally {
                setBtnLoading(btn, false);
            }
        });

        // ─── Form Asincrono ─────────────────────────────────────────────
        document.getElementById('asyncForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = document.getElementById('asyncBtn');
            const result = document.getElementById('asyncResult');
            setBtnLoading(btn, true);
            result.style.display = 'none';

            try {
                const res = await fetch(config.functionAppUrl + '/api/pubblica_richiesta', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        utente: document.getElementById('asyncUser').value.trim(),
                        messaggio: document.getElementById('asyncMsg').value.trim(),
                        categoria: document.getElementById('asyncCat').value.trim() || 'generica'
                    })
                });
                const data = await res.json();
                if (res.status === 202) {
                    showResult(result, '202 Accepted - ' + data.messaggio + ' (ID: ' + data.id + ')', 'success');
                    e.target.reset();
                    setTimeout(loadMessages, 3000);
                } else if (!res.ok) {
                    throw new Error(data.errore || 'Errore ' + res.status);
                } else {
                    showResult(result, 'Risposta ' + res.status + ': ' + JSON.stringify(data), 'success');
                }
            } catch (err) {
                showResult(result, 'Errore: ' + err.message, 'error');
            } finally {
                setBtnLoading(btn, false);
            }
        });

        // ─── Elenco ─────────────────────────────────────────────────────
        async function loadMessages() {
            const el = document.getElementById('results');
            el.innerHTML = '<div style="text-align:center;padding:20px;color:#666;">Caricamento...</div>';

            try {
                const res = await fetch(config.functionAppUrl + '/api/lista_richieste');
                if (!res.ok) throw new Error('Errore ' + res.status);
                const msgs = await res.json();
                renderMessages(msgs, el);
            } catch (err) {
                el.innerHTML = '<div style="text-align:center;padding:20px;color:#d32f2f;">Errore: ' + err.message + '</div>';
            }
        }

        function renderMessages(msgs, el) {
            if (!msgs.length) {
                el.innerHTML = '<div class="empty-state">Nessun messaggio. Invia il primo!</div>';
                return;
            }
            const sorted = [...msgs].sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
            const esc = (s) => { const d = document.createElement('div'); d.appendChild(document.createTextNode(s)); return d.innerHTML; };

            el.innerHTML = sorted.slice(0, 50).map(m => {
                const t = new Date(m.timestamp).toLocaleString('it-IT', { day:'2-digit', month:'2-digit', year:'numeric', hour:'2-digit', minute:'2-digit' });
                return '<div class="message-card">' +
                    '<div class="message-header"><span class="message-author">' + esc(m.utente) + '</span><span class="message-time">' + t + '</span></div>' +
                    '<div class="message-content">' + esc(m.messaggio) + '</div>' +
                    '<div class="message-category">Categoria: ' + esc(m.categoria || 'generica') + '</div>' +
                    '</div>';
            }).join('');
        }

        document.getElementById('refreshBtn').addEventListener('click', loadMessages);
        window.addEventListener('load', loadMessages);
    </script>
</body>
</html>
```

- [ ] **Step 2: Write `frontend/Dockerfile`**

```dockerfile
FROM nginx:alpine

# Remove default nginx html
RUN rm -rf /usr/share/nginx/html/*

# Copy static files (esclusi Dockerfile, .dockerignore, .git tramite .dockerignore)
COPY . /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

# Start nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
```

- [ ] **Step 3: Write `frontend/.dockerignore`**

```
node_modules
npm-debug.log
Dockerfile
.dockerignore
.git
.gitignore
```

- [ ] **Step 4: Verify Docker build**

Run: `cd frontend && docker build -t frontend-test .`
Expected: Build succeeds, image `frontend-test` created

- [ ] **Step 5: Commit**

```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs
git add frontend/
git commit -m "feat(frontend): add complete UI with sync/async forms and Dockerfile"
```

---

### Task 5: Deployment Scripts

**Files:**
- Create: `scripts/deploy-acr.sh`
- Create: `scripts/deploy-frontend.sh`
- Create: `scripts/setup-queue.sh`

**Interfaces:**
- Consumes: Resource names from Terraform outputs or `.env`
- Produces: Deployed resources on Azure

- [ ] **Step 1: Write `scripts/deploy-acr.sh`**

```bash
#!/bin/bash
# Build and push frontend image to Azure Container Registry
# Usage: ./scripts/deploy-acr.sh <resource-group> <acr-name>

set -euo pipefail

RG="${1:?Usage: $0 <resource-group> <acr-name>}"
ACR="${2:?Usage: $0 <resource-group> <acr-name>}"

echo "=== Logging into ACR ==="
az acr login -n "$ACR"

echo "=== Building and pushing image (cloud build) ==="
az acr build -r "$ACR" -t frontend:v1 ../frontend/

echo "=== Done! Image pushed to ${ACR}.azurecr.io/frontend:v1 ==="
```

- [ ] **Step 2: Write `scripts/deploy-frontend.sh`**

```bash
#!/bin/bash
# Deploy frontend to App Service for Containers
# Usage: ./scripts/deploy-frontend.sh <resource-group> <app-name> <acr-name>

set -euo pipefail

RG="${1:?Usage: $0 <resource-group> <app-name> <acr-name>}"
APP="${2:?Usage: $0 <resource-group> <app-name> <acr-name>}"
ACR="${3:?Usage: $0 <resource-group> <app-name> <acr-name>}"

echo "=== Updating App Service to pull new image ==="
az webapp config container set \
  -g "$RG" \
  -n "$APP" \
  --docker-custom-image-name "${ACR}.azurecr.io/frontend:v1" \
  --docker-registry-server-url "https://${ACR}.azurecr.io" \
  --docker-registry-server-user "$(az acr credential show -n "$ACR" --query username -o tsv)" \
  --docker-registry-server-password "$(az acr credential show -n "$ACR" --query 'passwords[0].value' -o tsv)"

echo "=== Restarting App Service ==="
az webapp restart -g "$RG" -n "$APP"

echo "=== Done! Frontend deployed at: https://${APP}.azurewebsites.net ==="
```

- [ ] **Step 3: Write `scripts/setup-queue.sh`**

```bash
#!/bin/bash
# Create the Storage Queue for decoupled processing
# Usage: ./scripts/setup-queue.sh <storage-account-name>

set -euo pipefail

SA="${1:?Usage: $0 <storage-account-name>}"

echo "=== Creating queue 'richieste-da-elaborare' ==="
az storage queue create \
  --name "richieste-da-elaborare" \
  --account-name "$SA" \
  --auth-mode login

echo "=== Done! Queue created in storage account ${SA} ==="
```

- [ ] **Step 4: Make scripts executable**

```bash
chmod +x scripts/*.sh
```

- [ ] **Step 5: Commit**

```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs
git add scripts/
git commit -m "feat(scripts): add deployment scripts for ACR, frontend, and queue"
```

---

### Task 6: PDF Report Template

**Files:**
- Create: `docs/report/report.md`

**Interfaces:**
- Consumes: All code and architecture from previous tasks
- Produces: Markdown template convertible to PDF

- [ ] **Step 1: Write `docs/report/report.md`**

```markdown
# Applicazione E2E Azure — Report di Laboratorio

## 1. Introduzione e Obiettivo

Costruire un servizio di registrazione richieste su Azure composto da:
- Frontend containerizzato (nginx + App Service for Containers)
- Backend serverless (Azure Functions Python con 5 function)
- Database NoSQL (Cosmos DB)
- Osservabilità (Application Insights)
- Sicurezza dei segreti (Key Vault + Managed Identity)
- Disaccoppiamento asincrono (Azure Storage Queue)
- Elaborazione schedulata (Timer Trigger)

**Stack:** Python 3.11, Azure Functions v4, Cosmos DB SQL API, Terraform

---

## 2. Architettura

[INSERIRE DIAGRAMMA ARCHITETTURA]

### Componenti Azure

| Servizio | Ruolo | Piano |
|---|---|---|
| Azure Container Registry | Archivio immagini Docker | Basic |
| App Service for Containers | Frontend nginx | Linux B1 |
| Azure Functions | Backend serverless | Consumption |
| Azure Cosmos DB | Database NoSQL | Serverless |
| Application Insights | Telemetria | — |
| Azure Key Vault | Segreti | Standard |
| Storage Account | Coda + Functions storage | — |

---

## 3. Lab 23 — E2E con Container, Functions e Cosmos DB

### 3.1 Partition Key

**Scelta:** `/categoria`

**Motivazione:** Le query di riepilogo (Lab 25) raggruppano per categoria. La distribuzione e' sufficientemente uniforme. Il volume per singolo utente non giustifica una partizione per utente.

[INSERIRE SCREENSHOT: Cosmos DB Data Explorer con container 'richieste']

### 3.2 Backend — Function crea_richiesta

[INSERIRE CODICE: crea_richiesta]

**Funzione:** HTTP POST, scrive su Cosmos DB tramite output binding, restituisce 201 Created.

[INSERIRE SCREENSHOT: Function App nel portale Azure]

### 3.3 Backend — Function lista_richieste

[INSERIRE CODICE: lista_richieste]

**Funzione:** HTTP GET, legge da Cosmos DB tramite input binding, restituisce 200 OK.

### 3.4 Frontend

[INSERIRE CODICE: index.html (o snippet)]

[INSERIRE CODICE: Dockerfile]

**Scelta App Service vs ACI:** App Service for Containers e' stato scelto perche' fornisce autoscaling, deployment slots, e integrazione nativa con ACR. ACI e' piu' semplice ma meno flessibile per produzione.

[INSERIRE SCREENSHOT: Frontend online che risponde]

### 3.5 Flusso Completo

[INSERIRE SCREENSHOT: Form compilato → 201 Created → item su Cosmos DB]

---

## 4. Lab 24 — Osservabilita' e Segreti

### 4.1 Application Insights

Collegato alla Function App. Raccoglie automaticamente:
- Richieste HTTP (nome, esito, tempi)
- Dipendenze (chiamate a Cosmos DB)
- Eccezioni
- Log applicativi (context.log/logging.info)

[INSERIRE SCREENSHOT: Application Insights — Live Metrics]

### 4.2 Query KQL

```kql
requests
| where timestamp > ago(1h)
| summarize count() by name, resultCode

traces
| where timestamp > ago(1h)
| where message startswith "CreaRichiesta" or message startswith "ListaRichieste"
```

[INSERIRE SCREENSHOT: Risultato query KQL]

### 4.3 Key Vault e Managed Identity

1. Key Vault creato con segreto `cosmos-conn`
2. Managed Identity (System) assegnata alla Function App
3. Ruolo `Key Vault Secrets User` assegnato all'identita'
4. App setting `COSMOS_CONNECTION_STRING` = `@Microsoft.KeyVault(SecretUri=...)`
5. Restart Function App + attesa ~1 min

**Errore tipico:** 500 dopo aver impostato il Key Vault reference. Causa: permesso non ancora propagato. Soluzione: restart + attendere.

[INSERIRE SCREENSHOT: COSMOS_CONNECTION_STRING con stato "Resolved" in App Settings]

---

## 5. Lab 25 — Coda e Timer

### 5.1 PubblicaRichiesta (HTTP → Queue)

[INSERIRE CODICE: pubblica_richiesta]

**Funzione:** Riceve la richiesta HTTP, la deposita nella coda `richieste-da-elaborare`, risponde 202 Accepted. Non tocca il database.

[INSERIRE SCREENSHOT: Coda nel portale Azure con messaggi in attesa]

### 5.2 ElaboraRichiesta (Queue → Cosmos)

[INSERIRE CODICE: elabora_richiesta]

**Funzione:** Viene svegliata dalla coda, scrive il documento su Cosmos DB tramite output binding. Nessuna risposta HTTP.

**Perche' la coda rende il sistema piu' robusto:**
- Se il database e' lento, l'utente non aspetta
- Se il database e' momentaneamente giu', la richiesta non si perde
- Se arrivano molte richieste, vengono elaborate in ordine senza accavallarsi

[INSERIRE SCREENSHOT: 202 Accepted + item che compare su Cosmos DB]

### 5.3 Riepilogo (Timer → Cosmos)

[INSERIRE CODICE: riepilogo]

**Funzione:** Parte da sola ogni 2 minuti (schedule CRON a 6 campi: `0 */2 * * * *`). Legge le richieste, le conta per categoria, salva un riepilogo nel container `riepiloghi`.

**Differenze tra i trigger:**

| Trigger | Cosa lo sveglia | Caso d'uso |
|---|---|---|
| HTTP | Chiamata del client | API REST, form submit |
| Queue | Messaggio nella coda | Elaborazione asincrona, disaccoppiamento |
| Timer | Orologio (CRON) | Report periodici, pulizia dati |

[INSERIRE SCREENSHOT: Container riepiloghi con almeno 2 riepiloghi]

### 5.4 Always On

**Nota:** Se la Function App e' su piano dedicato (B1, S1...), occorre attivare Always On affinche' il timer scatti. Su piano Consumption non serve.

[INSERIRE SCREENSHOT: Always On attivo nelle impostazioni]

---

## 6. Errori Encounterati e Soluzioni

| Errore | Causa | Soluzione |
|---|---|---|
| CORS bloccato | Function App senza CORS | Aggiungere `*` nelle CORS settings |
| 500 dopo Key Vault | Permesso non propagato | Restart + attendere ~1 min |
| Timer non scatta | Always On spento | Attivare Always On |
| Container non parte | ACR non autorizzato | Configurare credenziali ACR |
| Coda non elaborata | Nome coda diverso | Verificare nome identico in entrambe le function |

---

## 7. Conclusioni

[SCRIVERE conclusioni personali sulle scelte effettuate e cosa imparato]
```

- [ ] **Step 2: Commit**

```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs
git add docs/report/
git commit -m "docs: add PDF report template with all sections"
```

---

### Task 7: Final Cleanup and .gitignore

**Files:**
- Create: `.gitignore`
- Modify: `frontend/script.js` (remove or keep empty)

**Interfaces:**
- Consumes: All previous tasks
- Produces: Clean repo ready for commit

- [ ] **Step 1: Write `.gitignore`**

```
# Terraform
infra/.terraform/
infra/*.tfstate
infra/*.tfstate.backup
infra/tfplan
infra/.terraform.lock.hcl

# Python
__pycache__/
*.pyc
.venv/
*.egg-info/

# Node
node_modules/

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/

# Env files
.env
*.env.local

# Docker
docker-compose.override.yml
```

- [ ] **Step 2: Remove empty `frontend/script.js`**

```bash
rm -f frontend/script.js
```

- [ ] **Step 3: Final commit**

```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs
git add .
git commit -m "chore: add .gitignore and clean up empty files"
```

---

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-07-23-azure-e2e-plan.md`. Two execution options:

**1. Subagent-Driven (recommended)** — I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** — Execute tasks in this session using executing-plans, batch execution with checkpoints

Which approach?
