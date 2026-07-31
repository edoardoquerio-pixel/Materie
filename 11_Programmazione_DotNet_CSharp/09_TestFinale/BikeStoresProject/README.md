# BikeStoresProject

Soluzione .NET 10 con tre progetti per la gestione del database BikeStores (SQL Server).

## Architettura

```
BikeStoresProject.slnx
├── BikeStores.Data          — Modelli entità e DbContext (BikeStoresContext)
├── BikeStores.Backend       — Applicazione MVC con Identity (back-office)
└── BikeStores.WebAPI        — Web API RESTful (consumo da app mobile)
```

### BikeStores.Data

Libreria condivisa contenente i modelli del database BikeStores (schemi `production` e `sales`) e il `BikeStoresContext`. Usata da entrambi i progetti applicativi.

### BikeStores.Backend — MVC Back-Office

Applicazione ASP.NET Core MVC classica per amministrazione dati. Pattern identico ai progetti `05_ASP.Net` precedenti (PrestitiBibliotecaMVC, EsempioMVC).

**Autenticazione:**
- Windows Authentication (`Trusted_Connection=True`)
- Identity con ruoli: Administrators, Employees, Customers
- Seed automatico all'avvio: crea 3 ruoli e utenti da tabelle `staffs` e `customers`

**Controller:**

| Controller | Accesso | Descrizione |
|---|---|---|
| HomeController | Pubblico | Pagina iniziale |
| BrandsController | Administrators | CRUD marche |
| CategoriesController | Administrators | CRUD categorie |
| ProductsController | Administrators | CRUD prodotti |
| CustomersController | Administrators | CRUD clienti |
| StoresController | Administrators | CRUD negozi |
| StaffController | Administrators | CRUD staff |
| StocksController | Administrators | Gestione giacenze (chiave composita store+product) |
| OrdersController | Administrators, Employees, Customers | Ordini filtrati per ruolo |

**Dual DbContext:**
- `ApplicationDbContext` — tabelle Identity (AspNetUsers, AspNetRoles, etc.)
- `BikeStoresContext` — dati business negli schemi `production` e `sales`

Endpoint: `https://localhost:5001`

### BikeStores.WebAPI — Web API RESTful

API REST read-only pensata per consumo da applicativo mobile. Nessuna amministrazione dati.

**Caratteristiche:**
- Formato JSON con `ReferenceHandler.IgnoreCycles` (gestisce riferimenti circolari nav properties)
- CORS `AllowAll` (accesso da qualsiasi origine)
- `AsNoTracking()` su tutte le query (sola lettura)
- Filtri su query string per prodotti

**Endpoint:**

| Metodo | Endpoint | Descrizione |
|---|---|---|
| GET | `/api/brands` | Elenco marche ordinate per nome |
| GET | `/api/brands/{id}` | Dettaglio marca |
| GET | `/api/categories` | Elenco categorie ordinate per nome |
| GET | `/api/categories/{id}` | Dettaglio categoria |
| GET | `/api/products` | Prodotti con filtri opzionali |
| GET | `/api/products/{id}` | Dettaglio prodotto con marca e categoria |
| GET | `/api/stores` | Elenco negozi ordinati per nome |
| GET | `/api/stores/{id}` | Dettaglio negozio |

**Filtri Products:**

```
GET /api/products?modelYear=2016&brandId=1&categoryId=3&search=Trek
```

| Parametro | Tipo | Descrizione |
|---|---|---|
| `modelYear` | short (int16) | Filtro anno modello |
| `brandId` | int | Filtro marca |
| `categoryId` | int | Filtro categoria |
| `search` | string | Ricerca per nome prodotto (LIKE) |

Endpoint: `https://localhost:5002`

## Connessione Database

Entrambi i progetti usano la stessa connection string con Windows Authentication:

```json
{
  "ConnectionStrings": {
    "BikeStoreConnection": "Server=localhost;Database=BikeStores;Trusted_Connection=True;TrustServerCertificate=True;"
  }
}
```

Il codice si adatta al database esistente. Nessuna migration altera le tabelle business (`production.*`, `sales.*`). Solo le tabelle Identity (`AspNet*`) sono create da migration automatica all'avvio del Backend.

## Avvio

### Due terminali separati (consigliato)

```powershell
# Terminale 1 — Backend MVC
cd BikeStores.Backend
dotnet run --launch-profile https

# Terminale 2 — Web API
cd BikeStores.WebAPI
dotnet run --launch-profile https
```

### Verifica

- Backend: aprire `https://localhost:5001` nel browser
- WebAPI: test con curl
  ```powershell
  curl -sk https://localhost:5002/api/brands
  curl -sk "https://localhost:5002/api/products?modelYear=2016"
  curl -sk https://localhost:5002/api/products/1
  ```

## Credenziali predefinite (Backend)

| Ruolo | Email | Password |
|---|---|---|
| Administrators | admin@bikes.shop | @Bike-2026 |
| Employees | (email staff dal DB) | @Bike-2026 |
| Customers | (email customer dal DB) | @Bike-2026 |

## Documentazione aggiuntiva

- `GestioneConnessioneDatabase.md` — dettagli su connessione, migration, seed, pattern query e gestione errori
