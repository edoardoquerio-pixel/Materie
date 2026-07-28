# Task 6: PDF Report Template

## Context
This is the sixth task in an Azure E2E lab project. Tasks 1-5 created all application code. This task creates the PDF report template in Markdown format.

**Working directory:** `C:\Users\edoardo.querio\Desktop\Materie\14_Cloud_Azure\labs`

## What to do

### Step 1: Write `docs/report/report.md`

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

### Step 2: Commit
```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs
git add docs/report/
git commit -m "docs: add PDF report template with all sections"
```

## Report
Write your report to: `C:\Users\edoardo.querio\Desktop\Materie\14_Cloud_Azure\.superpowers\sdd\task-6-report.md`

Include: status (DONE/BLOCKED/NEEDS_CONTEXT), files created/modified, any concerns.
