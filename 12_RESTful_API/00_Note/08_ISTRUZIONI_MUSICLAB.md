# ISTRUZIONI MUSICLAB

**File:** `ISTRUZIONI MUSICLAB.md`
**Tipo:** `.md`
**Dimensione:** 8.6 KB
**Ultima modifica:** 02/07/2026 09:28

---

# 🎵 MusicLab — Esercitazione REST API con Node.js, Express e SQLite

## Obiettivo

Costruire un'API RESTful per gestire una collezione musicale, con un frontend HTML (fornito) che consenta di interagire con essa tramite interfaccia grafica.

Al termine dell'esercitazione avrai un server Node.js con Express che espone endpoint REST, un database SQLite con dati reali, e una pagina HTML funzionante per visualizzare e modificare brani e playlist semplicemente inserendo http://localhost:3000 nella barra degli inidirizzi del browser.


---

## Prerequisiti

- Node.js installato (v18 o superiore)
- Un editor di codice (VS Code consigliato)
- Postman per testare gli endpoint (opzionale ma consigliato)

---

## Struttura del progetto

```
musiclab/
├── server.js          ← entry point del server
├── database
    ├── db.js          ← configurazione e inizializzazione del database
    └── musiclab.db    ← file contenente il database
├── frontend
    └── index.html     ← file unico contenente la grafica e le logiche di Frontend
├── routes/
│   ├── songs.js       ← endpoint per i brani
│   └── playlists.js   ← endpoint per le playlist (bonus)
├── package.json
├── package-lock.json
```

---

## Setup iniziale

### 1. Crea la cartella

Crea una cartella chiamata musiclab; poi da VSC entraci dentro tramite il comando File -> Open Folder

### 2. Inizializza il progetto

Apri il Terminale di VSC e assicurati che sia del tipo Git Bash (NON powershell!) e inizializza il progetto tramite il comando

```bash
npm init
```
Ricorda di specificare il file "server.js" come entry point (voce "main" del file package.js) e il type a "module" (non "common").

### 3. Installa le dipendenze e crea lo script di avvio

```bash
npm install express sqlite3 nodemon
```

Terminato il comando, vai nel file package.json appena creato, togli qualsiasi cosa ci sia nell'oggetto "scripts" e al suo interno metti il comando di avvio, in modo che risulti come segue:

```json
"scripts": {
  "start": "nodemon server.js"
}
```

### 4. Crea la struttura di base dell'applicazione evvia il server

Definisci una costante "app" che rappresenti l'applicazione e le altre costanti necessarie (porta, basePath, ...), definisci il comando di avvio del server ( app.listen() ) e avvialo per verificare che tutto parta regolarmente:

```bash
npm start
```

---

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

```sql
CREATE TABLE IF NOT EXISTS playlist_songs (
      playlist_id INTEGER NOT NULL,
      song_id     INTEGER NOT NULL,
      PRIMARY KEY (playlist_id, song_id)
    )
```

---

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

**`PUT /songs/:id`**
- Sostituisce tutti i campi del brano (escluso `id`)
- Se il brano non esiste, restituisci 404
- Restituisci il brano aggiornato, status 200

**`DELETE /songs/:id`**
- Se il brano non esiste, restituisci 404
- Se l'eliminazione riesce, restituisci `{ message: "Brano eliminato" }`, status 200


---

## Parte bonus — Playlist (~1,5 ore)

### Endpoint da implementare

#### Gestione playlist

| Metodo   | Path              | Descrizione                                   |
|----------|-------------------|-----------------------------------------------|
| `GET`    | `/playlists`      | Recupera tutte le playlist                    |
| `GET`    | `/playlists/:id`  | Recupera una playlist con i brani associati   |
| `POST`   | `/playlists`      | Crea una nuova playlist                       |
| `PUT`    | `/playlists/:id`  | Modifica una playlist                         |
| `DELETE` | `/playlists/:id`  | Rimuove una playlist                          |

#### Gestione brani nelle playlist

| Metodo   | Path                            | Descrizione                     |
|----------|---------------------------------|---------------------------------|
| `POST`   | `/playlists/:id/songs`          | Aggiunge un brano alla playlist |
| `DELETE` | `/playlists/:id/songs/:songId`  | Rimuove un brano dalla playlist |

### Indicazioni

**`GET /playlists/:id`**
Deve restituire la playlist con l'array dei brani associati:
```json
{
  "id": 1,
  "name": "Chill Vibes",
  "description": "Musica rilassante",
  "songs": [
    { "id": 3, "title": "Clair de Lune", "artist": "Debussy", "album": "Suite bergamasque", "genre": "Classica", "year": 1905 }
  ]
}
```
Se la playlist esiste ma non ha brani, restituisci `"songs": []`.
Usa una `JOIN` tra `playlists`, `playlist_songs` e `songs`.

**`POST /playlists/:id/songs`**
- Il body deve contenere `{ "song_id": 5 }`
- Verifica che la playlist esista (404 se non esiste)
- Verifica che il brano esista (404 se non esiste)
- Se il brano è già nella playlist, restituisci `{ error: "Brano già presente nella playlist" }`, status 409
- Se va bene, inserisci la riga in `playlist_songs` e restituisci status 201

**`DELETE /playlists/:id/songs/:songId`**
- Rimuove il brano dalla playlist (non elimina il brano dal database)
- Se la combinazione non esiste, restituisci 404

**`DELETE /playlists/:id`**
- Prima di eliminare la playlist, elimina anche le righe corrispondenti in `playlist_songs`
- Restituisci `{ message: "Playlist eliminata" }`, status 200

---

## Suggerimenti generali

- Usa `sqlite3` per le query: le operazioni sono **asincrone** e usano callback. Le tre principali sono:
  - `db.all(sql, params, (err, rows) => {})` — restituisce un array di righe
  - `db.get(sql, params, (err, row) => {})` — restituisce una singola riga (o `undefined` se non trovata)
  - `db.run(sql, params, function(err) { this.lastID })` — esegue INSERT/UPDATE/DELETE; in caso di INSERT, `this.lastID` contiene l'id della riga appena inserita (attenzione: usare `function`, non arrow function, per accedere a `this`)
- Ricorda di abilitare il parsing del body JSON in Express: `app.use(express.json())`
- Testa ogni endpoint con Postman prima di collegarlo al frontend
- Controlla sempre la console del server se qualcosa non funziona

---

## Consegna

Al termine dell'esercitazione dovrai avere:

**Parte base:**
- [ ] Tutti e 7 gli endpoint per i brani funzionanti
- [ ] Frontend con visualizzazione, ricerca, creazione, modifica ed eliminazione brani

**Bonus:**
- [ ] Tutti gli endpoint per le playlist funzionanti
- [ ] Frontend con visualizzazione, creazione, modifica ed eliminazione playlist
- [ ] Possibilità di aggiungere e rimuovere brani da una playlist

