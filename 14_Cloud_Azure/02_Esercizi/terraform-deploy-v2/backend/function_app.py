import azure.functions as func
import json
import uuid
import logging
from datetime import datetime, timezone

app = func.FunctionApp()

# ============================================================================
# FUNCTION ORIGINALE: Crearichiesta (sincrono, scrive direttamente su Cosmos)
# ============================================================================
@app.route(route="crea_richiesta", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
@app.cosmos_db_output(
    arg_name="doc",
    database_name="appdb",
    container_name="richieste",
    connection="COSMOS_CONNECTION_STRING",
)
def crea_richiesta(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    """Crea una nuova richiesta e la scrive direttamente su Cosmos DB (sincrono)."""
    logging.info("CreaRichiesta: richiesta POST ricevuta.")

    try:
        req_body = req.get_json()
    except ValueError:
        logging.warning("CreaRichiesta: JSON non valido nella richiesta.")
        return func.HttpResponse(
            json.dumps({"errore": "JSON non valido"}),
            status_code=400,
            mimetype="application/json",
        )

    utente = req_body.get("utente")
    messaggio = req_body.get("messaggio")
    categoria = req_body.get("categoria", "generica")

    if not utente or not messaggio:
        logging.warning("CreaRichiesta: campi obbligatori mancanti (utente=%s, messaggio=%s).", utente, messaggio)
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
        "partitionKey": utente,
    }

    doc.set(func.Document.from_json(json.dumps(documento)))

    logging.info("CreaRichiesta: creata richiesta id='%s' utente='%s'.", documento["id"], utente)

    return func.HttpResponse(
        json.dumps(documento, ensure_ascii=False),
        status_code=201,
        mimetype="application/json",
    )


# ============================================================================
# FUNCTION ORIGINALE: ListaRichieste (lettura da Cosmos)
# ============================================================================
@app.route(route="lista_richieste", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
@app.cosmos_db_input(
    arg_name="docs",
    database_name="appdb",
    container_name="richieste",
    connection="COSMOS_CONNECTION_STRING",
    sql_query="SELECT * FROM c ORDER BY c.timestamp DESC",
)
def lista_richieste(req: func.HttpRequest, docs: func.DocumentList) -> func.HttpResponse:
    """Elenca tutte le richieste da Cosmos DB tramite input binding."""
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


# ============================================================================
# NUOVA FUNCTION: PubblicaRichiesta (HTTP -> Queue, risponde 202 Accepted)
# - Non tocca il database: il suo lavoro finisce quando il messaggio e' in coda
# - Il frontend riceve subito una risposta, l'elaborazione avviene in background
# ============================================================================
@app.route(route="pubblica_richiesta", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
@app.queue_output(
    arg_name="outputQueueItem",
    queue_name="richieste-da-elaborare",
    connection="QUEUE_STORAGE_CONNECTION",
)
def pubblica_richiesta(
    req: func.HttpRequest,
    outputQueueItem: func.Out[str]
) -> func.HttpResponse:
    """Pubblica una richiesta sulla coda e risponde 202 Accepted (asincrono)."""
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

    # Pubblica il messaggio sulla coda (output binding)
    outputQueueItem.set(json.dumps(item, ensure_ascii=False))

    logging.info("PubblicaRichiesta: messaggio pubblicato sulla coda, id='%s'.", item["id"])

    # 202 = "presa in carico", non "salvata"
    return func.HttpResponse(
        json.dumps({
            "messaggio": "Richiesta presa in carico, verra' elaborata a breve",
            "id": item["id"],
        }, ensure_ascii=False),
        status_code=202,
        mimetype="application/json",
    )


# ============================================================================
# NUOVA FUNCTION: ElaboraRichiesta (Queue -> Cosmos)
# - Viene svegliata dalla coda quando un messaggio e' disponibile
# - Scrive il documento su Cosmos DB (output binding)
# - Nessun req, nessuna risposta HTTP: non e' raggiungibile dal web
# ============================================================================
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
    """Elabora un messaggio dalla coda e lo scrive su Cosmos DB."""
    body = queueItem.get_body().decode("utf-8")
    logging.info("ElaboraRichiesta: messaggio ricevuto dalla coda: %s", body)

    item = json.loads(body)

    # Aggiunge campi di elaborazione
    item["elaborato_il"] = datetime.now(timezone.utc).isoformat()
    item["partitionKey"] = item.get("utente", "default")

    outputDocument.set(func.Document.from_json(json.dumps(item)))

    logging.info("ElaboraRichiesta: documento scritto su Cosmos, id='%s'.", item["id"])


# ============================================================================
# NUOVA FUNCTION: Riepilogo (Timer -> Cosmos input -> Cosmos output)
# - Parte da sola ogni 2 minuti (schedule CRON a 6 campi)
# - Legge tutte le richieste, le conta per categoria
# - Salva un riepilogo nel container "riepiloghi"
# ============================================================================
@app.function_name(name="Riepilogo")
@app.timer_trigger(
    arg_name="myTimer",
    schedule="0 */2 * * * *",   # Ogni 2 minuti (6 campi: sec min hour day month weekday)
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
    """Conta le richieste per categoria e salva un riepilogo."""
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
