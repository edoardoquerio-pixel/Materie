# docker-compose

**File:** `docker-compose.yaml`
**Tipo:** `.yaml`
**Dimensione:** 0.1 KB
**Ultima modifica:** 15/06/2026 11:35

---

services:
  api:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - db_data:/app/data

volumes:
  db_data:
