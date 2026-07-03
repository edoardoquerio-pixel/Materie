# tabella libri

**File:** `tabella libri.sql`
**Tipo:** `.sql`
**Dimensione:** 0.3 KB
**Ultima modifica:** 02/07/2026 09:22

---

CREATE TABLE IF NOT EXISTS libri (
    id          INT             UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    titolo      VARCHAR(255)    NOT NULL,
    autore      VARCHAR(150)    NOT NULL,
    isbn        CHAR(13)        UNIQUE NOT NULL,
    pagine      SMALLINT        UNSIGNED NOT NULL,
    prezzo      DECIMAL(6,2)    UNSIGNED NOT NULL
);
