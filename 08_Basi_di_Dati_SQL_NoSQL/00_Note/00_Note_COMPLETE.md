# Basi di Dati SQL/NoSQL — Note Complete

## 1. Modello Relazionale

- **Tabelle** (relazioni): righe (record) + colonne (attributi)
- **Chiave Primaria (PK)**: identificatore univoco per riga
- **Chiave Esterna (FK)**: riferimento a PK altra tabella
- **Vincoli**: NOT NULL, UNIQUE, CHECK, DEFAULT, PRIMARY KEY, FOREIGN KEY
- **Normalizzazione**: 1NF (atomico), 2NF (dipendenza totale), 3NF (nessuna dipendenza transitiva)

## 2. SQL — DDL

```sql
CREATE TABLE Studenti (
    id INT PRIMARY KEY IDENTITY(1,1),
    nome VARCHAR(50) NOT NULL,
    cognome VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    data_nascita DATE,
    corso_id INT FOREIGN KEY REFERENCES Corsi(id)
);

ALTER TABLE Studenti ADD telefono VARCHAR(20);
ALTER TABLE Studenti DROP COLUMN telefono;
DROP TABLE Studenti;
```

## 3. SQL — DML

```sql
INSERT INTO Studenti (nome, cognome, email) VALUES ('Mario', 'Rossi', 'm.rossi@example.com');
UPDATE Studenti SET email = 'm.rossi@nuovo.it' WHERE id = 1;
DELETE FROM Studenti WHERE id = 1;

SELECT s.nome, s.cognome, c.nome AS corso
FROM Studenti s
JOIN Corsi c ON s.corso_id = c.id
WHERE c.nome LIKE '%Cloud%'
ORDER BY s.cognome;
```

- **JOIN**: INNER, LEFT, RIGHT, FULL, CROSS
- **Aggregazione**: COUNT, SUM, AVG, MIN, MAX + GROUP BY + HAVING
- **Subquery**: scalari, di tabella, correlate
- **CTE (WITH)**: query temporanee ricorsive e non
- **Window functions**: ROW_NUMBER, RANK, LAG, LEAD, SUM OVER(PARTITION BY)

## 4. SQL — DCL / TCL

```sql
GRANT SELECT, INSERT ON Studenti TO utente;
REVOKE INSERT ON Studenti FROM utente;

BEGIN TRANSACTION;
UPDATE Conti SET saldo = saldo - 100 WHERE id = 1;
UPDATE Conti SET saldo = saldo + 100 WHERE id = 2;
COMMIT;  -- o ROLLBACK
```

## 5. Indici e Performance

- **Clustered index**: ordine fisico tabella (1 per tabella)
- **Non-clustered index**: struttura separata (molteplici)
- **Execution plan**: analisi costo query
- **Statistiche**: aggiornamento per query optimizer
- **SARGability**: condizioni che usano indici (`col = value`, non `FUNC(col)`)

## 6. NoSQL

| Tipo | Esempi | Use case |
|------|--------|----------|
| Document | MongoDB, CouchDB | JSON, dati flessibili, cataloghi |
| Key-Value | Redis, DynamoDB | Cache, session, lookup |
| Column-family | Cassandra, HBase | Time series, big data |
| Graph | Neo4j, ArangoDB | Relazioni, social, recommendation |

**Vantaggi rispetto SQL:** schema-less, scalabilità orizzontale, performance per use case specifici
**Compromessi:** BASE vs ACID, consistenza eventuale, query complexity

## 7. SQL Server

- **Versioni**: Express (free, 10GB), Standard, Enterprise
- **Management Studio (SSMS)**: GUI amministrazione
- **BACKUP/RESTORE**: `.bak` files, FULL/DIFF/LOG
- **Utilità**: `sqlcmd`, query store, profiler, index tuning advisor
- **Operatori**: IDENTITY, SEQUENCE, TRIGGER, VIEW, STORED PROCEDURE

## 8. Progetto: PrestitiVideoteca

- Schema: Clienti, Film, Noleggi
- FK: `Noleggi.id_cliente → Clienti.id`, `Noleggi.id_film → Film.id`
- Queries: film in ritardo, clienti attivi, storico noleggi
- Vincoli: data_restituzione > data_noleggio, UNIQUE per copie film
