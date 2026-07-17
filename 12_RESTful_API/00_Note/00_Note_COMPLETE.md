# RESTful API — Note Complete

## 1. REST Principles

**REST** (Representational State Transfer, Fielding 2000):
1. **Stateless**: ogni richiesta contiene tutto il necessario
2. **Client-Server**: separazione UI da data storage
3. **Cacheable**: risposte marcate come cacheable/non-cacheable
4. **Uniform Interface**: risorse identificate da URI, rappresentazioni standard
5. **Layered System**: proxy, load balancer, gateway intermedi
6. **Code on Demand** (opzionale): codice eseguibile dal client

## 2. HTTP Methods & Status Codes

| Method | CRUD | Idempotent | Safe |
|--------|------|-----------|------|
| GET | Read | ✅ | ✅ |
| POST | Create | ❌ | ❌ |
| PUT | Update (full) | ✅ | ❌ |
| PATCH | Update (partial) | ❌ | ❌ |
| DELETE | Delete | ✅ | ❌ |

**Status codes:**
| Code | Significato |
|------|-------------|
| 200 OK | GET/PUT/PATCH success |
| 201 Created | POST success |
| 204 No Content | DELETE success |
| 400 Bad Request | Errore client (validation) |
| 401 Unauthorized | Autenticazione mancante/fallita |
| 403 Forbidden | Autorizzazione insufficiente |
| 404 Not Found | Risorsa inesistente |
| 409 Conflict | Stato conflittuale (es. duplicato) |
| 422 Unprocessable | Validazione semantica fallita |
| 429 Too Many Requests | Rate limiting |
| 500 Internal Server Error | Errore server |

## 3. API Design

**Endpoint naming:**
```
GET    /api/v1/libri                 # Lista
GET    /api/v1/libri/{id}            # Singolo
POST   /api/v1/libri                 # Crea
PUT    /api/v1/libri/{id}            # Aggiorna tutto
PATCH  /api/v1/libri/{id}            # Aggiorna parziale
DELETE /api/v1/libri/{id}            # Elimina

GET    /api/v1/libri/{id}/recensioni  # Sub-risorsa
GET    /api/v1/libri?autore=Mario     # Filtri
GET    /api/v1/libri?page=1&limit=20  # Paginazione
```

**Best practices:**
- Nomi plurali, lowercase, kebab-case
- Versioning in URI (`/api/v1/`, `/api/v2/`)
- Filtri, sorting, paginazione via query params
- Relazioni nidificate per sub-risorse
- HATEOAS (link nelle risposte) — opzionale

## 4. Progetto: LibreriaOnline (v1 → v2)

**v1 — In memoria:**
```javascript
let libri = [{ id:1, titolo:"...", autore:"...", prezzo:9.99 }];

app.get('/api/v1/libri', (req, res) => res.json(libri));
app.post('/api/v1/libri', (req, res) => {
    const libro = { id: nextId++, ...req.body };
    libri.push(libro);
    res.status(201).json(libro);
});
```

**v2 — SQLite:**
```javascript
import sqlite3 from 'sqlite3';
const db = new sqlite3.Database('libreria.db');

app.get('/api/v2/libri', (req, res) => {
    db.all('SELECT * FROM libri WHERE ? OR 1=1', (err, rows) => {
        res.json(rows);
    });
});
```

## 5. Autenticazione e Sicurezza

**JWT (JSON Web Token):**
```
Header: { "alg": "HS256", "typ": "JWT" }
Payload: { "sub": "user123", "role": "admin", "iat": 1516239022 }
Signature: HMAC-SHA256(base64(header) + "." + base64(payload), secret)
```

**HttpOnly cookie vs Bearer token:**
| | Bearer (Authorization header) | HttpOnly cookie |
|---|-------------------------------|-----------------|
| XSS protection | No (esposto a JS) | ✅ (inaccessibile a JS) |
| CSRF protection | ✅ (non automatico) | ❌ (richiede CSRF token) |
| Mobile/3rd party | ✅ | ❌ |
| Storage | LocalStorage | Cookie |

**Other security:**
- Rate limiting (express-rate-limit)
- CORS configuration
- Input validation/sanitization
- HTTPS obbligatorio
- Helmet middleware (security headers)

## 6. Documentazione (Swagger/OpenAPI)

```yaml
openapi: 3.0.0
info:
  title: LibreriaOnline API
  version: 2.0.0
paths:
  /api/v2/libri:
    get:
      summary: Elenco libri
      responses:
        '200':
          description: Lista libri
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Libro'
```

## 7. Stack Tecnologico (ITS)

- **Runtime**: Node.js (ESM, `"type": "module"`)
- **Framework**: Express (`express.Router()`)
- **Body parsing**: `body-parser` con `json()`
- **Database**: SQLite (`sqlite3` package)
- **Documentazione**: `swagger-ui-express` + `swagger.json` (OpenAPI 2.0)
- **Auth**: JWT (`jsonwebtoken`), bcrypt, HttpOnly cookies
