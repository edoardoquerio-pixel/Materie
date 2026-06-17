# Piano: Completamento Progetto Agenzia Viaggi

## TL;DR

> **Quick Summary**: Completare il progetto `agenziaViaggi` con struttura identica a `libreriaOnlinev2`, implementando 3 entità (viaggi ampliati, clienti, prenotazioni con FK) con API CRUD complete (incluso PUT, assente in libreriaOnlinev2), frontend Bootstrap 5 e documentazione Swagger.
>
> **Deliverables**:
> - 3 database script file (script_viaggi.js, script_clienti.js, script_prenotazioni.js)
> - 3 router (viaggiRouter.js, clientiRouter.js, prenotazioniRouter.js)
> - server.js con inizializzazione DB e configurazione Express
> - Frontend public/index.html con Bootstrap 5 (3 sezioni)
> - Documentazione Swagger (swagger/swagger.json)
> - package.json aggiornato con dipendenze
>
> **Estimated Effort**: Medium (~11 file tra creazioni e modifiche)
> **Parallel Execution**: YES — 2 waves
> **Critical Path**: Task 2 (database scripts) → Task 3 (server.js) → Waves parallele (Tasks 4-8)

---

## Context

### Original Request
"Terminare tutto il progetto di agenziaViaggi, voglio una struttura uguale a libreriaOnlinev2, ottimizzando il tutto e ampliandolo se necessario o non completo."

### Interview Summary
**Key Discussions**:
- **3 entità**: viaggi (ampliata), clienti, prenotazioni (FK a entrambi)
- **Range valutazione**: 1-5 INTEGER
- **Trasporto**: enum vincolato (aereo, treno, nave, bus, auto)
- **data_prenotazione**: auto-generata dal server
- **Cascade DELETE**: RESTRICT (impedisce cancellazione con prenotazioni attive)
- **Naming**: lowercase come libreriaOnlinev2
- **Frontend**: tutti e 3 gli entity con Bootstrap 5
- **PUT**: implementato (mancante in libreriaOnlinev2)
- **Porta**: 3000
- **Test**: nessun test automatico

**Research Findings**:
- `libreriaOnlinev2` struttura: server.js → database/script_*.js + routes/*Router.js + public/index.html + swagger/
- API prefix: /api/v2/
- Pattern architetturale: Express + SQLite3 + ESM, db creato in server.js ed esportato
- libreriaOnlinev2 manca di PUT endpoint (solo in swagger, non nei router)
- libreriaOnlinev2 ha bug search: doppia query parallela senza return in libriRouter.js

### Metis Review
**Identified Gaps** (addressed):
- Scope OUT aggiunto con 9 esclusioni esplicite (auth, paginazione, Docker, test, ORM, ecc.)
- Naming convention risolta: lowercase come libreriaOnlinev2
- Cascade delete policy risolta: RESTRICT
- FK constraints: PRAGMA foreign_keys = ON in server.js
- package.json da aggiornare con dipendenze mancanti
- Vecchio database/queries.js da eliminare (sostituito da 3 script_*.js)

---

## Work Objectives

### Core Objective
Completare il progetto `agenziaViaggi` con API Express + SQLite per gestione viaggi, clienti e prenotazioni, con frontend Bootstrap e documentazione Swagger.

### Concrete Deliverables
- 8 nuovi file, 1 file da aggiornare (package.json), 1 file da eliminare (database/queries.js)
- API completa sotto /api/v2/ con CRUD + search per 3 entità
- Frontend navigabile con Bootstrap 5 (tabella viaggi, clienti, prenotazioni + modali CRUD)
- Swagger UI disponibile su /api-docs

### Definition of Done
- [ ] `npm start` avvia il server senza errori
- [ ] Tutti gli endpoint CRUD rispondono correttamente (200/201/400/404)
- [ ] Frontend carica e mostra dati, permette CRUD
- [ ] Swagger UI accessibile su /api-docs
- [ ] FK constraints funzionanti (RESTRICT su delete con prenotazioni attive)

### Must Have
- Struttura identica a libreriaOnlinev2 (server.js → database/ → routes/ → public/ + swagger/)
- 3 entità: viaggi, clienti, prenotazioni
- CRUD completo (GET, GET/:id, POST, PUT, DELETE) + search per ogni entità
- Frontend con Bootstrap 5 per tutte e 3 le entità
- Swagger documentation
- package.json con tutte le dipendenze
- PRAGMA foreign_keys = ON attivo

### Must NOT Have (Guardrails)
- ❌ **Niente autenticazione/autorizzazione** — nessun login, JWT, sessioni
- ❌ **Niente test automatici**
- ❌ **Niente paginazione lato API**
- ❌ **Niente containerizzazione/Docker**
- ❌ **Niente librerie di validazione esterne** — validazione inline
- ❌ **Niente ORM/query builder** — raw SQL
- ❌ **Niente PATCH endpoints** — solo PUT per update completi
- ❌ **Niente logging strutturato** — solo console.log
- ❌ **Niente HTTPS o rate limiting**

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — ALL verification is agent-executed.

### Test Decision
- **Infrastructure exists**: NO
- **Automated tests**: NONE (esplicitamente escluso)
- **Verification**: solo agent-executed QA scenarios (curl per API, Playwright per frontend)

### QA Policy
- **API/Backend**: Use Bash (curl) — Send requests, assert status + response fields
- **Frontend/UI**: Use Playwright — Navigate, interact, assert DOM, screenshot

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Foundation — tutto parallelo, nessuna dipendenza):
├── Task 1: Aggiornare package.json [quick]
├── Task 2: Creare database scripts (3 file) [quick]
├── Task 3: Creare server.js [quick]
├── Task 4: Creare public/index.html [visual-engineering]
├── Task 5: Creare swagger/swagger.json [writing]

Wave 2 (Routers — dopo Wave 1, MA paralleli tra loro):
├── Task 6: Creare viaggiRouter.js [unspecified-high]
├── Task 7: Creare clientiRouter.js [unspecified-high]
├── Task 8: Creare prenotazioniRouter.js [unspecified-high]

Wave FINAL (dopo TUTTI i task — 4 review parallele):
├── Task F1: Plan compliance audit (oracle)
├── Task F2: Code quality review (unspecified-high)
├── Task F3: Manual QA (unspecified-high)
└── Task F4: Scope fidelity check (deep)
-> Present results -> Get explicit user ok
```

### Dependency Matrix
- **1**: - → 6-8, F1-F4
- **2**: - → 3, 6-8, F1-F4
- **3**: 2 → 6-8, F1-F4
- **4**: - → F1-F4
- **5**: - → F1-F4
- **6**: 2, 3 → F1-F4
- **7**: 2, 3 → F1-F4
- **8**: 2, 3 → F1-F4

### Agent Dispatch Summary
- **Wave 1**: 5 task — 3× [quick], 1× [visual-engineering], 1× [writing]
- **Wave 2**: 3 task — 3× [unspecified-high]
- **FINAL**: 4 task — 1× [oracle], 2× [unspecified-high], 1× [deep]

---

## TODOs

- [x] 1. Aggiornare package.json con dipendenze e script

  **What to do**:
  - Leggere il package.json esistente
  - Aggiungere `"scripts": { "start": "nodemon server.js" }`
  - Aggiungere dipendenze: express, sqlite3, cors, body-parser, swagger-ui-express, nodemon
  - Eseguire `npm install` per aggiornare node_modules e package-lock.json

  **Must NOT do**:
  - Non cambiare "type": "module"
  - Non modificare altre sezioni esistenti

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: [] (task semplice)

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 2, 3, 4, 5)
  - **Blocks**: None
  - **Blocked By**: None (can start immediately)

  **References**:
  - `libreriaOnlinev2/package.json` — pattern esatto da replicare

  **Acceptance Criteria**:
  - [ ] `package.json` contiene `"dependencies"` con express, sqlite3, cors, body-parser, swagger-ui-express, nodemon
  - [ ] `package.json` contiene `"scripts": { "start": "nodemon server.js" }`
  - [ ] `npm install` eseguito senza errori

  **QA Scenarios**:
  ```
  Scenario: Verifica package.json aggiornato
    Tool: Bash
    Steps:
      1. cat package.json | node -e "const p=require('fs').readFileSync('/dev/stdin','utf8');const j=JSON.parse(p);console.log(Object.keys(j.dependencies||{}).length)"
    Expected Result: Output >= 6 (tutte le dipendenze presenti)
    Evidence: .omo/evidence/task-01-deps-check.txt
  ```

  **Commit**: NO (raggruppa con altri task)

---

- [x] 2. Creare database scripts (script_viaggi.js, script_clienti.js, script_prenotazioni.js)

  **What to do**:
  - ELIMINARE il vecchio file `database/queries.js`
  - Creare `database/script_viaggi.js` con:
    - CREATE_TABLE_VIAGGI: `CREATE TABLE IF NOT EXISTS viaggi (id INTEGER PRIMARY KEY AUTOINCREMENT, destinazione TEXT NOT NULL, descrizione TEXT, durata INTEGER NOT NULL, prezzo REAL NOT NULL, assicurazione INTEGER NOT NULL DEFAULT 0, data_partenza TEXT, data_ritorno TEXT, trasporto TEXT NOT NULL CHECK(trasporto IN ('aereo','treno','nave','bus','auto')), posti_disponibili INTEGER, valutazione INTEGER CHECK(valutazione BETWEEN 1 AND 5))`
    - SELECT_ALL, SELECT_BY_ID, SELECT_BY_DESTINAZIONE (LIKE), INSERT_VIAGGIO, UPDATE_VIAGGIO, DELETE_VIAGGIO
    - Search query: Search con parametri multipli opzionali (destinazione LIKE, trasporto, data_partenza, prezzo_min, prezzo_max)
  - Creare `database/script_clienti.js` con:
    - CREATE_TABLE_CLIENTI: `CREATE TABLE IF NOT EXISTS clienti (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, cognome TEXT NOT NULL, email TEXT NOT NULL UNIQUE, telefono TEXT)`
    - SELECT_ALL, SELECT_BY_ID, SELECT_BY_NOME (LIKE), SELECT_BY_COGNOME (LIKE), INSERT_CLIENTE, UPDATE_CLIENTE, DELETE_CLIENTE
  - Creare `database/script_prenotazioni.js` con:
    - CREATE_TABLE_PRENOTAZIONI: `CREATE TABLE IF NOT EXISTS prenotazioni (id INTEGER PRIMARY KEY AUTOINCREMENT, viaggio_id INTEGER NOT NULL REFERENCES viaggi(id), cliente_id INTEGER NOT NULL REFERENCES clienti(id), data_prenotazione TEXT NOT NULL, partecipanti INTEGER NOT NULL DEFAULT 1, note TEXT)`
    - SELECT_ALL, SELECT_BY_ID, SELECT_BY_VIAGGIO_ID, SELECT_BY_CLIENTE_ID, INSERT_PRENOTAZIONE, UPDATE_PRENOTAZIONE, DELETE_PRENOTAZIONE

  **Must NOT do**:
  - Non usare AUTO_INCREMENT (MySQL) → usare AUTOINCREMENT di SQLite
  - Non usare BOOLEAN → usare INTEGER (0/1) per assicurazione
  - Non mescolare UPPERCASE/lowercase → tutto lowercase come convenzione decisa

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: [] (task di definizione SQL)

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 3, 4, 5)
  - **Blocks**: Task 3, Tasks 6-8 (server.js e router dipendono da questi file)
  - **Blocked By**: None (can start immediately)

  **References**:
  - `libreriaOnlinev2/database/script_libri.js` — pattern per struttura query
  - `libreriaOnlinev2/database/script_clienti.js` — pattern per struttura query

  **Acceptance Criteria**:
  - [ ] `database/script_viaggi.js` esiste con tutte le costanti SQL
  - [ ] `database/script_clienti.js` esiste con tutte le costanti SQL
  - [ ] `database/script_prenotazioni.js` esiste con tutte le costanti SQL
  - [ ] Vecchio `database/queries.js` NON esiste più
  - [ ] Ogni file esporta CREATE_TABLE_*, SELECT_ALL, SELECT_BY_ID, INSERT_*, UPDATE_*, DELETE_*
  - [ ] Le query usano sintassi SQLite corretta (AUTOINCREMENT, non AUTO_INCREMENT)

  **QA Scenarios**:
  ```
  Scenario: Verifica file script creati e sintassi corretta
    Tool: Bash
    Steps:
      1. node -e "import('./database/script_viaggi.js').then(m => console.log(Object.keys(m).length, 'exports'))"
    Expected Result: Script si importa senza errori
    Evidence: .omo/evidence/task-02-scripts-check.txt
  ```
  ```
  Scenario: Verifica sintassi SQLite corretta
    Tool: Bash
    Steps:
      1. grep -n "AUTO_INCREMENT\|AUTOINCREMENT" database/script_viaggi.js
    Expected Result: Contiene AUTOINCREMENT (non AUTO_INCREMENT)
    Evidence: .omo/evidence/task-02-autoincrement-check.txt
  ```

  **Commit**: NO (raggruppa)

---

- [x] 3. Creare server.js (entry point Express)

  **What to do**:
  - Creare `server.js` seguendo il pattern di `libreriaOnlinev2/server.js`
  - Importare Express, body-parser, cors, sqlite3, swagger-ui-express
  - Importare CREATE_TABLE da tutti e 3 gli script database (script_viaggi.js, script_clienti.js, script_prenotazioni.js)
  - Importare tutti e 3 i router (viaggiRouter.js, clientiRouter.js, prenotazioniRouter.js)
  - Creare app Express sulla porta 3000
  - Applicare middleware: cors(), bodyParser.json(), express.static('public')
  - Montare router: /api/v2/viaggi, /api/v2/clienti, /api/v2/prenotazioni
  - Montare Swagger UI su /api-docs
  - Creare ed esportare `const db = new sqlite3.Database("./database/agenzia.db")`
  - All'avvio (app.listen): eseguire `initializeDatabase()` che crea tutte e 3 le tabelle
  - **CRITICO**: Eseguire `db.run("PRAGMA foreign_keys = ON")` subito dopo la creazione del db
  - Messaggio di avvio: "Il server è attivo sulla porta 3000"

  **Must NOT do**:
  - Non usare file-scoped db.js (seguire pattern libreriaOnlinev2: db in server.js)
  - Non dimenticare PRAGMA foreign_keys = ON (default OFF in SQLite)

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES (dipende solo da naming convention, non da file già esistenti)
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 4, 5)
  - **Blocks**: Tasks 6-8 (router dipendono da db export)
  - **Blocked By**: Task 2 (deve conoscere le costanti CREATE_TABLE e i percorsi)

  **References**:
  - `libreriaOnlinev2/server.js` — pattern esatto da replicare (48 righe)

  **Acceptance Criteria**:
  - [ ] `server.js` esiste e importa tutti e 3 gli script database
  - [ ] `server.js` importa tutti e 3 i router
  - [ ] `server.js` esporta `const db`
  - [ ] `PRAGMA foreign_keys = ON` è eseguito
  - [ ] `npm start` avvia il server senza errori

  **QA Scenarios**:
  ```
  Scenario: Verifica server si avvia
    Tool: Bash
    Steps:
      1. npm start &
      2. sleep 3
      3. curl -s http://localhost:3000/ | head -c 100
    Expected Result: Output contiene "<!DOCTYPE html>" (frontend servito)
    Evidence: .omo/evidence/task-03-server-start.txt
  ```

  **Commit**: NO (raggruppa)

---

- [x] 4. Creare public/index.html (frontend Bootstrap 5)

  **What to do**:
  - Creare `public/index.html` seguendo il pattern di `libreriaOnlinev2/public/index.html` MA con 3 sezioni
  - Usare Bootstrap 5 CDN, Bootstrap Icons
  - HTML statico con 3 sezioni card (viaggi, clienti, prenotazioni) + navbar
  - Ogni sezione ha: header con titolo + bottone "Nuovo", input search, tabella con colonne appropriate
  - Modali per create/edit (uno per entità) + modale conferma eliminazione
  - Toast notification per feedback
  - JavaScript inline con:
    - `const API = 'http://localhost:3000/api/v2'`
    - Funzioni CRUD asincrone per ogni entità (load, search, create, update, delete)
    - `escHtml()` helper per XSS prevention
    - `showToast()`, `confirmDelete()` helper
    - Init: load automatico all'avvio di tutte e 3 le entità
    - Enter key per search fields
  - **Sezione VIAGGI**: tabella con id, destinazione, durata, prezzo, assicurazione (si/no), data_partenza, data_ritorno, trasporto, posti_disponibili, valutazione (stelline), azioni
  - **Sezione CLIENTI**: tabella con id, nome, cognome, email, telefono, azioni
  - **Sezione PRENOTAZIONI**: tabella con id, viaggio_id, cliente_id, data_prenotazione, partecipanti, note, azioni
  - Stile: navbar dark bg-dark, viaggi header bg-primary, clienti header bg-success, prenotazioni header bg-warning

  **Must NOT do**:
  - Non usare framework JS (React/Vue) — solo vanilla JS inline
  - Non usare jQuery

  **Recommended Agent Profile**:
  - **Category**: `visual-engineering`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 3, 5)
  - **Blocks**: None
  - **Blocked By**: None (can start immediately)

  **References**:
  - `libreriaOnlinev2/public/index.html` — pattern esatto da replicare (488 righe, 3 sezioni invece di 2)

  **Acceptance Criteria**:
  - [ ] `public/index.html` esiste con 3 sezioni (viaggi, clienti, prenotazioni)
  - [ ] La pagina si carica su http://localhost:3000/
  - [ ] Ogni sezione ha tabella, modale CRUD, search
  - [ ] Load automatico all'avvio

  **QA Scenarios**:
  ```
  Scenario: Frontend si carica correttamente
    Tool: Bash
    Steps:
      1. curl -s http://localhost:3000/ | grep -c "api/v2"
    Expected Result: Output >= 3 (chiamate API per ogni entità)
    Evidence: .omo/evidence/task-04-frontend-load.txt
  ```

  **Commit**: NO (raggruppa)

---

- [x] 5. Creare swagger/swagger.json (documentazione API)

  **What to do**:
  - Creare directory `swagger/`
  - Creare `swagger/swagger.json` in formato Swagger 2.0
  - Includere tutti gli endpoint per tutte e 3 le entità (GET, GET/:id, POST, PUT, DELETE + search)
  - Usare `"host": "localhost:3000"`, `"basePath": "/api/v2"`
  - Definire schemi per: Viaggio, Cliente, Prenotazione (nelle definitions)
  - Definire schemi per input POST/PUT (NuovoViaggio, NuovoCliente, NuovaPrenotazione)
  - Tag: "Viaggi", "Clienti", "Prenotazioni"

  **Must NOT do**:
  - Non usare OpenAPI 3.0 — mantenere Swagger 2.0 come libreriaOnlinev2

  **Recommended Agent Profile**:
  - **Category**: `writing`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 3, 4)
  - **Blocks**: None
  - **Blocked By**: None (can start immediately)

  **References**:
  - `libreriaOnlinev2/swagger/swagger.json` — pattern esatto

  **Acceptance Criteria**:
  - [ ] `swagger/swagger.json` esiste in formato Swagger 2.0
  - [ ] Tutti gli endpoint sono documentati
  - [ ] Swagger UI si carica su http://localhost:3000/api-docs

  **QA Scenarios**:
  ```
  Scenario: Swagger UI accessibile
    Tool: Bash
    Steps:
      1. curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/api-docs
    Expected Result: 200
    Evidence: .omo/evidence/task-05-swagger-ui.txt
  ```

  **Commit**: NO (raggruppa)

---

- [x] 6. Creare viaggiRouter.js

  **What to do**:
  - Creare `routes/viaggiRouter.js` seguendo il pattern di `libreriaOnlinev2/routes/libriRouter.js`
  - Importare Express, `db` da server.js, e tutte le costanti query da database/script_viaggi.js
  - Implementare:
    - `GET /` — db.all(SELECT_ALL) → res.json(rows)
    - `GET /search` — db.all con query dinamicamente costruita per: destinazione (LIKE), trasporto (esatto), data_partenza, prezzo_min, prezzo_max
    - `GET /:id` — db.get(SELECT_BY_ID) → 200 o 404
    - `POST /` — valida body, db.run(INSERT_VIAGGIO) → 201
    - `PUT /:id` — valida body, db.run(UPDATE_VIAGGIO) → 200 (this.changes === 0 → 404)
    - `DELETE /:id` — db.run(DELETE_VIAGGIO) → 200 (this.changes === 0 → 404)
  - Funzione di validazione `validaViaggio(body)`: verifica campi obbligatori (destinazione, durata, prezzo, trasporto), che durata > 0, prezzo > 0, trasporto in ['aereo','treno','nave','bus','auto'], valutazione tra 1-5 se presente

  **Must NOT do**:
  - Non dimenticare return dopo res.status().json() per evitare "headers already sent"
  - Non lasciare il bug della doppia risposta in search (come libreriaOnlinev2)

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 7, 8)
  - **Blocks**: None
  - **Blocked By**: Task 2 (script_viaggi.js), Task 3 (server.js)

  **References**:
  - `libreriaOnlinev2/routes/libriRouter.js` — pattern esatto (126 righe)

  **Acceptance Criteria**:
  - [ ] Tutti e 6 gli endpoint funzionano (GETAll, GETSearch, GETById, POST, PUT, DELETE)
  - [ ] Validazione funziona (400 su body vuoto)
  - [ ] 404 su ID inesistente (GET, PUT, DELETE)
  - [ ] Search combinato funziona

  **QA Scenarios**:
  ```
  Scenario: CRUD base viaggi
    Tool: Bash
    Steps:
      1. curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/api/v2/viaggi
      2. curl -s -X POST http://localhost:3000/api/v2/viaggi -H "Content-Type: application/json" -d "{\"destinazione\":\"Roma\",\"durata\":7,\"prezzo\":1200,\"trasporto\":\"aereo\"}" -o /dev/null -w "%{http_code}"
      3. curl -s http://localhost:3000/api/v2/viaggi/1 | node -e "process.stdin.resume();let d='';process.stdin.on('data',c=>d+=c);process.stdin.on('end',()=>{const j=JSON.parse(d);console.log(j.destinazione)})"
    Expected Result: Step 1: 200, Step 2: 201, Step 3: "Roma"
    Evidence: .omo/evidence/task-06-viaggi-crud.txt
  ```
  ```
  Scenario: Validazione viaggi
    Tool: Bash
    Steps:
      1. curl -s -X POST http://localhost:3000/api/v2/viaggi -H "Content-Type: application/json" -d "{}" -o /dev/null -w "%{http_code}"
    Expected Result: 400
    Evidence: .omo/evidence/task-06-viaggi-validation.txt
  ```
  ```
  Scenario: PUT e DELETE
    Tool: Bash
    Steps:
      1. curl -s -X PUT http://localhost:3000/api/v2/viaggi/1 -H "Content-Type: application/json" -d "{\"destinazione\":\"Milano\",\"durata\":5,\"prezzo\":800,\"trasporto\":\"treno\"}" -o /dev/null -w "%{http_code}"
      2. curl -s -X DELETE http://localhost:3000/api/v2/viaggi/1 -o /dev/null -w "%{http_code}"
      3. curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/api/v2/viaggi/1
    Expected Result: Step 1: 200, Step 2: 200, Step 3: 404
    Evidence: .omo/evidence/task-06-viaggi-put-delete.txt
  ```

  **Commit**: NO (raggruppa)

---

- [x] 7. Creare clientiRouter.js

  **What to do**:
  - Creare `routes/clientiRouter.js` seguendo il pattern di libreriaOnlinev2 MA con PUT aggiunto
  - Importare Express, db, e costanti query da database/script_clienti.js
  - Implementare:
    - `GET /` — tutti i clienti
    - `GET /search` — search per nome (LIKE) e/o cognome (LIKE), combinabili
    - `GET /:id` — singolo cliente (200 o 404)
    - `POST /` — validazione, INSERT_CLIENTE (201, gestire UNIQUE constraint violazione → 409)
    - `PUT /:id` — validazione, UPDATE_CLIENTE (200 o 404)
    - `DELETE /:id` — DELETE_CLIENTE (200 o 404, RESTRICT se ha prenotazioni)
  - Funzione `validaCliente(body)`: nome, cognome, email obbligatori; email valida con regex
  - Funzione `isValidEmail(email)`: regex

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 6, 8)
  - **Blocked By**: Task 2 (script_clienti.js), Task 3 (server.js)

  **References**:
  - `libreriaOnlinev2/routes/clientiRouter.js` — pattern

  **Acceptance Criteria**:
  - [ ] Tutti gli endpoint funzionano
  - [ ] Email duplicata → 409
  - [ ] Search nome+cognome combinato

  **QA Scenarios**:
  ```
  Scenario: CRUD clienti
    Tool: Bash
    Steps:
      1. curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/api/v2/clienti
      2. curl -s -X POST http://localhost:3000/api/v2/clienti -H "Content-Type: application/json" -d "{\"nome\":\"Mario\",\"cognome\":\"Rossi\",\"email\":\"mario@test.it\"}" -o /dev/null -w "%{http_code}"
    Expected Result: Step 1: 200, Step 2: 201
    Evidence: .omo/evidence/task-07-clienti-crud.txt
  ```
  ```
  Scenario: Email duplicata
    Tool: Bash
    Steps:
      1. curl -s -X POST http://localhost:3000/api/v2/clienti -H "Content-Type: application/json" -d "{\"nome\":\"Luca\",\"cognome\":\"Bianchi\",\"email\":\"mario@test.it\"}" -o /dev/null -w "%{http_code}"
    Expected Result: 409
    Evidence: .omo/evidence/task-07-clienti-duplicate.txt
  ```

  **Commit**: NO (raggruppa)

---

- [x] 8. Creare prenotazioniRouter.js

  **What to do**:
  - Creare `routes/prenotazioniRouter.js`
  - Importare Express, db, e costanti query da database/script_prenotazioni.js
  - Implementare:
    - `GET /` — tutte le prenotazioni (db.all con JOIN a viaggi e clienti per mostrare destinazione e nome cliente)
    - `GET /search` — search per viaggio_id, cliente_id, data_prenotazione
    - `GET /:id` — singola prenotazione (200 o 404)
    - `POST /` — validazione, data_prenotazione auto-generata (new Date().toISOString().split('T')[0]), INSERT_PRENOTAZIONE (201, gestire FK violation → 400)
    - `PUT /:id` — validazione, UPDATE_PRENOTAZIONE (200 o 404)
    - `DELETE /:id` — DELETE_PRENOTAZIONE (200 o 404)
  - Funzione `validaPrenotazione(body)`: viaggio_id e cliente_id obbligatori (numerici), partecipanti >= 1
  - Verifica esistenza viaggio e cliente PRIMA di inserire (per messaggi di errore migliori di FK violation)
  - **Nota**: data_prenotazione NON deve essere passata dal client — viene generata dal server

  **Must NOT do**:
  - Non accettare data_prenotazione dal body (deve essere auto-generata)
  - Non dimenticare di validare partecipanti >= 1

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 6, 7)
  - **Blocked By**: Task 2 (script_prenotazioni.js), Task 3 (server.js)

  **References**:
  - `libreriaOnlinev2/routes/clientiRouter.js` — pattern per struttura router

  **Acceptance Criteria**:
  - [ ] Tutti gli endpoint funzionano
  - [ ] data_prenotazione auto-generata (non dal client)
  - [ ] FK violation → 400 con messaggio chiaro
  - [ ] DELETE su viaggio con prenotazioni → errore (RESTRICT)

  **QA Scenarios**:
  ```
  Scenario: CRUD prenotazioni
    Tool: Bash
    Steps:
      1. curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/api/v2/prenotazioni
      2. curl -s -X POST http://localhost:3000/api/v2/prenotazioni -H "Content-Type: application/json" -d "{\"viaggio_id\":1,\"cliente_id\":1,\"partecipanti\":2}" -o /dev/null -w "%{http_code}"
    Expected Result: Step 1: 200, Step 2: 201 (se viaggio e cliente con ID 1 esistono)
    Evidence: .omo/evidence/task-08-prenotazioni-crud.txt
  ```
  ```
  Scenario: FK violation
    Tool: Bash
    Steps:
      1. curl -s -X POST http://localhost:3000/api/v2/prenotazioni -H "Content-Type: application/json" -d "{\"viaggio_id\":999,\"cliente_id\":1,\"partecipanti\":2}" -o /dev/null -w "%{http_code}"
      2. curl -s -X DELETE http://localhost:3000/api/v2/viaggi/1 -o /dev/null -w "%{http_code}"  # se viaggio 1 ha prenotazioni
    Expected Result: Step 1: 400, Step 2: 400 (RESTRICT)
    Evidence: .omo/evidence/task-08-prenotazioni-fk.txt
  ```

  **Commit**: Group 2
  - Message: `feat(agenzia-viaggi): add CRUD routers for prenotazioni`
  - Files: `routes/prenotazioniRouter.js`

---

## Final Verification Wave

- [x] F1. **Plan Compliance Audit** — `oracle`
  Read the plan end-to-end. For each "Must Have": verify implementation exists (read file, curl endpoint, run command). For each "Must NOT Have": search codebase for forbidden patterns — reject with file:line if found. Check evidence files exist in .omo/evidence/. Compare deliverables against plan.
  Output: `Must Have [N/N] | Must NOT Have [N/N] | Tasks [N/N] | VERDICT: APPROVE/REJECT`

- [x] F2. **Code Quality Review** — `unspecified-high`
  Run `npm start` and verify server starts. Review all changed files for: type suppression, empty catches, debug logging in prod, commented-out code, unused imports. Check AI slop: excessive comments, over-abstraction, generic names (data/result/item/temp).
  Output: `Build [PASS/FAIL] | Files [N clean/N issues] | VERDICT`

- [x] F3. **Real Manual QA** — `unspecified-high`
  Execute EVERY QA scenario from EVERY task — follow exact steps, capture evidence. Test cross-task integration (CRUD su viaggi → prenotazioni che referenziano viaggi). Test edge cases: FK violation, delete con prenotazioni attive (RESTRICT), email duplicata, valutazione fuori range. Save to `.omo/evidence/final-qa/`.
  Output: `Scenarios [N/N pass] | Integration [N/N] | Edge Cases [N tested] | VERDICT`

- [x] F4. **Scope Fidelity Check** — `deep`
  For each task: read "What to do", read actual diff (git log/diff). Verify 1:1 — everything in spec was built (no missing), nothing beyond spec was built (no creep). Check "Must NOT do" compliance.
  Output: `Tasks [N/N compliant] | Contamination [CLEAN/N issues] | VERDICT`

---

## Commit Strategy

- **Gruppo 1** (Tasks 1-5, Wave 1 foundation): `feat(agenzia-viaggi): add project foundation (server, database, frontend, swagger)`
- **Gruppo 2** (Tasks 6-8, Wave 2 routers): `feat(agenzia-viaggi): add CRUD routers for viaggi, clienti, prenotazioni`

---

## Success Criteria

### Verification Commands
```bash
# Server avviato
npm start  # Expected: "Il server è attivo sulla porta 3000"

# API viaggi
curl http://localhost:3000/api/v2/viaggi  # Expected: 200, []
curl -X POST http://localhost:3000/api/v2/viaggi -H "Content-Type: application/json" -d "{\"destinazione\":\"Roma\",\"durata\":7,\"prezzo\":1200,\"trasporto\":\"aereo\"}"  # Expected: 201
curl http://localhost:3000/api/v2/viaggi/1  # Expected: 200, {...}
curl -X PUT http://localhost:3000/api/v2/viaggi/1 -H "Content-Type: application/json" -d "{\"destinazione\":\"Milano\",\"durata\":5,\"prezzo\":800,\"trasporto\":\"treno\"}"  # Expected: 200
curl -X DELETE http://localhost:3000/api/v2/viaggi/1  # Expected: 200

# API clienti
curl http://localhost:3000/api/v2/clienti  # Expected: 200, []

# API prenotazioni
curl http://localhost:3000/api/v2/prenotazioni  # Expected: 200, []

# FK constraint
curl -X DELETE http://localhost:3000/api/v2/viaggi/1  # Expected: 400 se viaggio ha prenotazioni

# Frontend
curl http://localhost:3000/  # Expected: 200, HTML
curl http://localhost:3000/api-docs  # Expected: 200, Swagger UI
```

### Final Checklist
- [x] Server si avvia senza errori su porta 3000
- [x] Tutti gli endpoint CRUD funzionano per viaggi, clienti, prenotazioni
- [x] Search funziona per ogni entità
- [x] FK constraints attivi (RESTRICT su delete)
- [x] Frontend mostra tutte e 3 le sezioni
- [x] Swagger UI accessibile
- [x] Nessuna esclusione violata (non auth, non test, non paginazione, etc.)
