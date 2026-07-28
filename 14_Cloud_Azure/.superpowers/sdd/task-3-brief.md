# Task 3: Backend — Azure Functions (All 5)

## Context
This is the third task in an Azure E2E lab project. Tasks 1-2 set up Terraform infrastructure. This task rewrites the backend with all 5 Azure Functions.

**Working directory:** `C:\Users\edoardo.querio\Desktop\Materie\14_Cloud_Azure\labs`

## Bug fix (critical)
The existing `function_app.py` has `connection="COSMOS_DB"` in `elabora_richiesta` (line 171) and `riepilogo` (lines 207, 214). The rewritten code MUST use `connection="COSMOS_CONNECTION_STRING"` everywhere. Do NOT copy the bug from the existing code.

## What to do

### Step 1: Write `backend/requirements.txt`

```
azure-functions
```

### Step 2: Write `backend/host.json`

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

### Step 3: Write `backend/local.settings.json`

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

### Step 4: Write `backend/function_app.py`

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

### Step 5: Verify Python syntax
```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs/backend
python -c "import py_compile; py_compile.compile('function_app.py', doraise=True)"
```
Expected: No output (success)

### Step 6: Commit
```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs
git add backend/
git commit -m "feat(backend): add all 5 Azure Functions (crea, lista, pubblica, elabora, riepilogo)"
```

## Report
Write your report to: `C:\Users\edoardo.querio\Desktop\Materie\14_Cloud_Azure\.superpowers\sdd\task-3-report.md`

Include: status (DONE/BLOCKED/NEEDS_CONTEXT), files created/modified, Python syntax check results, any concerns.
