# ISTRUZIONI MUSICLAB

## Panoramica
# 🎵 MusicLab — Esercitazione REST API con Node.js, Express e SQLite

## Argomenti trattati
API REST, Database, Data Analytics, Configurazione, Git

---
## Appunti

# 🎵 MusicLab — Esercitazione REST API con Node.js, Express e SQLite
## Obiettivo
Costruire un'API RESTful per gestire una collezione musicale, con un frontend HTML (fornito) che consenta di interagire con essa tramite interfaccia grafica.
Al termine dell'esercitazione avrai un server Node.js con Express che espone endpoint REST, un database SQLite con dati reali, e una pagina HTML funzionante per visualizzare e modificare brani e playlist semplicemente inserendo http://localhost:3000 nella barra degli inidirizzi del browser.
## Prerequisiti
- Node.js installato (v18 o superiore)
- Un editor di codice (VS Code consigliato)
- Postman per testare gli endpoint (opzionale ma consigliato)
## Struttura del progetto
├── server.js          ← entry point del server
├── db.js          ← configurazione e inizializzazione del database
└── musiclab.db    ← file contenente il database
└── index.html     ← file unico contenente la grafica e le logiche di Frontend
│   ├── songs.js       ← endpoint per i brani
│   └── playlists.js   ← endpoint per le playlist (bonus)
├── package.json
├── package-lock.json
## Setup iniziale
### 1. Crea la cartella
Crea una cartella chiamata musiclab; poi da VSC entraci dentro tramite il comando File -> Open Folder
### 2. Inizializza il progetto
Apri il Terminale di VSC e assicurati che sia del tipo Git Bash (NON powershell!) e inizializza il progetto tramite il comando
Ricorda di specificare il file "server.js" come entry point (voce "main" del file package.js) e il type a "module" (non "common").
### 3. Installa le dipendenze e crea lo script di avvio
npm install express sqlite3 nodemon
Terminato il comando, vai nel file package.json appena creato, togli qualsiasi cosa ci sia nell'oggetto "scripts" e al suo interno metti il comando di avvio, in modo che risulti come segue:
"start": "nodemon server.js"
### 4. Crea la struttura di base dell'applicazione evvia il server
Definisci una costante "app" che rappresenti l'applicazione e le altre costanti necessarie (porta, basePath, ...), definisci il comando di avvio del server ( app.listen() ) e avvialo per verificare che tutto parta regolarmente:
## Schema del database
### Tabella `songs`
| Colonna  | Tipo    | Note             |
|----------|---------|------------------|
| id       | INTEGER | PK, autoincrement |
| title    | TEXT    | NOT NULL         |
| artist   | TEXT    | NOT NULL         |
| album    | TEXT    | nullable         |
| genre    | TEXT    | nullable         |
| year     | INTEGER | nullable         |
### Tabella `playlists` *(bonus)*
| Colonna     | Tipo    | Note             |
|-------------|---------|------------------|
| id          | INTEGER | PK, autoincrement |
| name        | TEXT    | NOT NULL         |
| description | TEXT    | nullable         |
### Tabella `playlist_songs` *(bonus)*
| Colonna     | Tipo    | Note                   |
|-------------|---------|------------------------|
| playlist_id | INTEGER | NOT NULL               |
| song_id     | INTEGER | NOT NULL               |
| PK composta su (playlist_id, song_id)  -> Vedi script sotto
CREATE TABLE IF NOT EXISTS playlist_songs (
playlist_id INTEGER NOT NULL,
song_id     INTEGER NOT NULL,
PRIMARY KEY (playlist_id, song_id)
## Parte base — CRUD sui brani (~2 ore)
### Endpoint da implementare
| Metodo   | Path              | Descrizione                              |
|----------|-------------------|------------------------------------------|
| `GET`    | `/songs`          | Recupera tutti i brani                   |
| `GET`    | `/songs?title=..` | Filtra per titolo (query param)          |
| `GET`    | `/songs?artist=..`| Filtra per artista (query param)         |
| `GET`    | `/songs/:id`      | Recupera un brano specifico              |
| `POST`   | `/songs`          | Aggiunge un nuovo brano                  |
| `PUT`    | `/songs/:id`      | Modifica un brano (sostituzione completa)|
| `DELETE` | `/songs/:id`      | Rimuove un brano                         |
### Indicazioni
**`GET /songs`**
- Se non ci sono query params, restituisci tutti i brani
- Se è presente `?title=rock`, filtra i brani il cui titolo contiene quella stringa (usa `LIKE` in SQL, case-insensitive)
- Se è presente `?artist=beatles`, filtra per artista
- I due filtri si possono combinare: `?artist=beatles&title=hey`
- Risposta: array JSON di brani, status 200
**`GET /songs/:id`**
- Se il brano esiste, restituiscilo come oggetto JSON, status 200
- Se non esiste, restituisci `{ error: "Brano non trovato" }`, status 404
**`POST /songs`**
- Il body JSON deve contenere almeno `title` e `artist`
- Se mancano, restituisci `{ error: "title e artist sono obbligatori" }`, status 400
- Dopo l'inserimento, restituisci il brano appena creato con il suo `id`, status 201

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_ISTRUZIONI_MUSICLAB.md*
