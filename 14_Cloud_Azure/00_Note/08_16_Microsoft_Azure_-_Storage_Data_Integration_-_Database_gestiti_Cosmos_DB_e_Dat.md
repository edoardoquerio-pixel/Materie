# 16) Microsoft Azure - Storage, Data Integration - Database gestiti, Cosmos DB e Data Integration

**File:** `16) Microsoft Azure - Storage, Data Integration - Database gestiti, Cosmos DB e Data Integration.pptx`
**Tipo:** `.pptx`
**Dimensione:** 73.7 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Storage, Data & Integration: database gestiti, Cosmos DB e Data Integration (4 ore)

---

Dal database al flusso del dato
Database gestiti, Cosmos DB e integrazione dati: dove nasce il dato e dove deve arrivare

---

Argomenti (4 ore)
•  Perché un database gestito (PaaS) e cosa cambia nel modello operativo
•  Relazionali gestiti: Azure SQL (single/MI), PostgreSQL/MySQL Flexible
•  Continuità del servizio: backup, replica, HA, RPO/RTO
•  Cosmos DB: partizionamento, throughput, consistency levels
•  Quando relazionale e quando NoSQL distribuito
•  Il dato non vive da solo: integrazione con Data Factory
•  Pipeline, trigger, orchestrazione e cenni su Synapse

---

Perché scegliere un database gestito
•  Un database gestito riduce il lavoro su patching, backup e manutenzione di base.
•  Il team si concentra più sul dato e meno sul server del database.
•  Non elimina le scelte architetturali: sposta il livello del lavoro.
•  Alta disponibilità, backup e monitoraggio entrano più facilmente nel servizio.
•  È uno dei vantaggi più evidenti del cloud PaaS.

---

Database relazionali gestiti
•  Azure SQL Database — il database relazionale come servizio (single database).
•  Managed Instance — più vicino allo SQL Server tradizionale (migrazioni lift-and-shift).
•  PostgreSQL e MySQL Flexible Server — motori open source gestiti.
•  La scelta dipende da compatibilità applicativa, controllo richiesto e percorso di migrazione.
•  Il tema non è solo il motore: è il modello operativo.

---

Continuità del servizio
•  In un database gestito il tema non è solo scrivere query, ma tenere vivo il servizio.
•  Backup automatici, replica e opzioni HA riducono i rischi operativi.
•  La continuità cambia da servizio a servizio.
•  Va sempre letta insieme a RPO (quanto dato posso perdere) e RTO (in quanto torno su) e ai costi.
•  Il cloud aiuta, ma non sostituisce il ragionamento progettuale.

---

Cosmos DB: idea base
•  Cosmos DB è il servizio NoSQL distribuito di Azure.
•  Supporta più API e modelli di accesso (SQL/Core, MongoDB, Cassandra…).
•  Si usa quando servono scala elevata, bassa latenza e distribuzione globale.
•  Non è un sostituto automatico di ogni database relazionale.

---

Cosmos DB: i tre concetti chiave
•  Partizionamento — la partition key distribuisce i dati: una buona chiave = scala uniforme.
•  Throughput — capacità misurata in RU/s (Request Units), provisioned o serverless.
•  Consistency levels — dal più forte al più disponibile: Strong, Bounded staleness, Session, Consistent prefix, Eventual.
•  Sono leve di costo/prestazioni/coerenza: si scelgono in base al requisito, non a caso.

---

Relazionale o NoSQL
Modello
Quando tende a servire
Relazionale
schema stabile, query strutturate, transazioni forti
NoSQL distribuito
scala ampia, flessibilità, accesso globale e veloce
•  La scelta non è di moda, ma di requisito.
•  Il modello dati influenza sviluppo, costo e integrazione futura.

---

Il dato non vive mai da solo
•  I database entrano in flussi con applicazioni, code, ETL e analytics.
•  Per questo il tema non è solo il motore, ma anche l'integrazione.
•  Un database operativo e una piattaforma analytics hanno scopi diversi.
•  Il progetto vero inizia quando i dati devono muoversi tra servizi diversi.
“Da qui in poi passiamo dal "dove sta il dato" al "come si muove il dato".”

---

Perché serve integrazione dati
•  I dati arrivano da applicazioni, file, database, API e sistemi esterni.
•  Il problema non è solo salvarli, ma spostarli e coordinarli bene.
•  L'integrazione evita passaggi manuali fragili e poco tracciabili.
•  Nel cloud questo significa pipeline, trigger e orchestrazione.
•  Qui inizia il livello più sistemico del dato.

---

Data Factory: idea base
•  Azure Data Factory serve a costruire pipeline di integrazione.
•  Coordina attività tra sorgenti e destinazioni diverse.
•  Concetti base: pipeline, activity, linked service, dataset.
•  Non è un database, ma un motore di orchestrazione del flusso.
•  Il valore è nel movimento controllato del dato.

---

Trigger e orchestrazione
•  Un trigger decide quando parte una pipeline.
•  Può essere orario, ricorrente o legato a un evento.
•  L'orchestrazione mette in ordine i passaggi e le dipendenze.
•  Se un flusso ha più step, non basta copiare dati: bisogna coordinarli.
•  È qui che l'integrazione diventa processo, non solo trasferimento.

---

Synapse: dove entra
•  Synapse entra quando il focus si sposta verso analytics e workspace integrati.
•  Aiuta a collegare ingestione, query e consumo analitico.
•  Non sostituisce Data Factory in tutto, ma può lavorare insieme.
•  Il punto è distinguere orchestrazione del dato da analisi del dato.
•  Quando il progetto cresce, questi ruoli vanno separati bene.

---

Flusso tipico da leggere
•  i dati entrano da app, file o database
•  una pipeline li sposta o li prepara
•  lo storage o il layer analitico li riceve
•  report, query o altri servizi li consumano
•  Il valore non è il singolo servizio, ma il flusso completo.
•  La domanda giusta è sempre: dove nasce il dato e dove deve arrivare?

---

Quando usare cosa
•  Database gestito → il dato operativo dell'applicazione (relazionale o Cosmos).
•  Data Factory → quando il problema è orchestrare passaggi e spostamenti.
•  Synapse → quando il problema è analizzare i dati a livello più ampio.
•  Spesso non si escludono: collaborano.
•  L'integrazione dati è il ponte tra operativo e analitico.
