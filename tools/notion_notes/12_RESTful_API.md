# [12] RESTful API

## 📋 Panoramica

Materia dedicata alla progettazione e implementazione di API RESTful. Si costruisce progressivamente una libreria online partendo da semplici array in memoria fino a database SQLite con autenticazione JWT e Swagger.

**Tecnologie**: Node.js (Express), SQLite, Swagger/OpenAPI, JWT, HTTPS, body-parser, ESM (ECMAScript Modules)

---

## 📚 Indice degli argomenti

### 1. Fondamenti REST

- **REST** (Representational State Transfer): architettura stateless basata su risorse
- **Verbi HTTP**: GET (leggi), POST (crea), PUT (aggiorna completo), PATCH (aggiorna parziale), DELETE (elimina)
- **Stateless**: ogni richiesta contiene tutte le info necessarie
- **URI risorse**: `/api/v1/libri`, `/api/v1/libri/123`
- **Codici di stato**: 200 OK, 201 Created, 204 No Content, 400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Server Error

### 2. JSON e Formato Dati

```json
{
  "id": 1,
  "titolo": "Il Nome della Rosa",
  "autore": "Umberto Eco",
  "anno": 1980
}
```
- **Content-Type**: `application/json`
- **Request/Response** strutturati e consistenti

### 3. Progettazione API

- **URL naming**: sostantivi plurali (`/libri`, non `/libro`)
- **Filtri**: `GET /api/libri?autore=Eco&anno=1980`
- **Paginazione**: `GET /api/libri?page=1&limit=10`
- **Versioning**: `/api/v1/...`, `/api/v2/...`

### 4. Implementazione con Express (Node.js)

```javascript
import express from 'express';
import bodyParser from 'body-parser';

const app = express();
app.use(bodyParser.json());

const PORT = 3000;

// GET tutti i libri
app.get('/api/v1/libri', (req, res) => {
  res.json(libri);
});

// POST nuovo libro
app.post('/api/v1/libri', (req, res) => {
  const nuovoLibro = { id: nextId++, ...req.body };
  libri.push(nuovoLibro);
  res.status(201).json(nuovoLibro);
});

app.listen(PORT, () => console.log(`Server su porta ${PORT}`));
```
- **Evoluzione**: v1 (array in memoria) → v2 (SQLite persistente)
- **Middleware**: body-parser, logger, CORS, auth

### 5. SQLite come Storage

```javascript
import sqlite3 from 'sqlite3';
const db = new sqlite3.Database('libreria.db');

db.run(`CREATE TABLE IF NOT EXISTS libri (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  titolo TEXT NOT NULL,
  autore TEXT NOT NULL,
  anno INTEGER
)`);
```

### 6. HTTPS / JWT / Autenticazione

- **HTTPS**: TLS/SSL per crittografia del canale
- **JWT** (JSON Web Token): autenticazione stateless
  ```
  Header.Payload.Signature
  ```
- **Flusso**: login → JWT → token in `Authorization: Bearer <token>`
- **Middleware di autenticazione**: `jwt.verify(token, secret)`
- **JWT vs HttpOnly Cookie**: JWT per SPA/mobile, cookie per SSR

### 7. Swagger / OpenAPI

- Documentazione automatica delle API
- Formato: `swagger.json` (OpenAPI 2.0) o `openapi.yaml` (3.0)
- UI interattiva: `swagger-ui-express`
- **Try it out**: test diretto dalla documentazione

---

## ⚡ Punti Chiave

1. **REST non è CRUD**: i verbi HTTP esprimono azioni, non solo operazioni database
2. **Versiona le API**: non rompere i client esistenti
3. **Valida sempre input**: mai fidarsi di req.body
4. **Usa HTTPS in produzione**: sempre, sempre, sempre
5. **Password mai in chiaro**: hashing con bcrypt, non scrivere in DB
6. **Middleware**: incapsula auth, log, errori in middleware riutilizzabili

---

## 📎 Risorse Collegate

- **02_Esercizi/** — Esercizi su routing, middleware, database
- **03_Progetti/** — LibreriaOnline (v1, v2.1, v2.2, v2-final), MUSICLAB
- **Materiale**: PDF lezioni 1-5, guida HTML, Swagger, JWT, test DOCX
