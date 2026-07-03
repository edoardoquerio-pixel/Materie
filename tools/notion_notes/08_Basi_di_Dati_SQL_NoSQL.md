# [08] Basi di Dati SQL/NoSQL

## 📋 Panoramica

Materia dedicata alla progettazione e gestione di database relazionali (SQL) e non relazionali (NoSQL). Si lavora con SQL Server e SQLite su database reali: biblioteche, gallerie d'arte, scuole italiane, statistica ISTAT, gestione esami.

**Tecnologie**: SQL (T-SQL, SQLite), SQL Server Management Studio, ADO.NET (C#)

---

## 📚 Indice degli argomenti

### 1. Modellazione dei Dati

- **Modello concettuale**: entità-relazioni (ER), attributi, chiavi
- **Modello logico**: tabelle, vincoli, normalizzazione
- **Modello fisico**: indici, storage, performance
- **Schema logico** (es. Gestione Esami): entità (Studente, Esame, Corso, Docente) e relazioni

### 2. Linguaggio SQL

- **DDL** (Data Definition Language):
  ```sql
  CREATE TABLE, ALTER TABLE, DROP TABLE
  CREATE INDEX, CREATE VIEW
  ```
- **DML** (Data Manipulation Language):
  ```sql
  SELECT, INSERT, UPDATE, DELETE
  ```
- **DQL** (Data Query Language):
  ```sql
  SELECT con JOIN, GROUP BY, HAVING, ORDER BY, WHERE
  ```
- **DCL** (Data Control Language): GRANT, REVOKE
- **TCL** (Transaction Control): BEGIN TRAN, COMMIT, ROLLBACK

### 3. Vincoli e Relazioni

- **PRIMARY KEY**: identificatore univoco di riga
- **FOREIGN KEY**: relazione tra tabelle, integrità referenziale
- **UNIQUE**: valori non duplicati
- **CHECK**: validazione valori
- **NOT NULL**: campo obbligatorio
- **CASCADE**: aggiornamento/cancellazione a catena su FK

### 4. Join e Sottoquery

- **INNER JOIN**: solo righe corrispondenti in entrambe le tabelle
- **LEFT/RIGHT JOIN**: tutte le righe di una tabella + corrispondenze
- **FULL OUTER JOIN**: tutte le righe di entrambe
- **CROSS JOIN**: prodotto cartesiano
- **Sottoquery**: `SELECT ... WHERE campo IN (SELECT ...)`

### 5. NoSQL

- **Concetti**: schema-less, orizzontalmente scalabile, BASE (non ACID)
- **Tipologie**:
  - **Document store** (MongoDB): dati in JSON/BSON
  - **Key-value** (Redis): accesso rapido per chiave
  - **Column-family** (Cassandra): wide-column store
  - **Graph** (Neo4j): nodi e relazioni
- **Quando usare SQL vs NoSQL**: schemas rigidi vs flessibili, relazioni complesse vs volumi enormi

---

## ⚡ Punti Chiave

1. **Sempre PRIMARY KEY su ogni tabella**: Mai una tabella senza chiave primaria
2. **Vincoli FK per integrità**: Non affidarsi solo all'applicazione
3. **Normalizzazione (3NF)**: evita ridondanza; denormalizzare solo per performance misurate
4. **SELECT \* è dannoso**: Specificare sempre le colonne necessarie
5. **Indicizzare le colonne in WHERE/JOIN**: impatto enorme sulle performance
6. **Sempre backup prima di ALTER/DROP**: I .bak sono tuoi amici

---

## 📎 Risorse Collegate

- **02_Esercizi/** — Query SQL, esercizi di progettazione
- **03_Progetti/** — Progetti con database reali
- **Materiale**: NorthWind.sql, ScuoleItaliane.sql, GalleriaArte-PalazzoMadama.bak, Istat.bak, GestioneEsami.xlsx
