# Incident Report – 2026-07-16

## Situazione

L'infrastruttura aziendale basata su container (nginx + Spring Boot + PostgreSQL) subiva un errore generale a partire dalle **09:11:58**. Il sistema non era più raggiungibile esternamente.

## Punti Chiave (riassunto di 5 punti)

* **09:11:58 – app-db** ha fallito la scrittura del WAL (`no space left on device`) → database PostgreSQL si è spento.

* **09:12:03 – app-backend** Spring Boot non è riuscito ad avviarsi (causato da un errore di connessione Java al database).

* **09:12:04 – nginx** non è riuscito a connettersi al backend (`172.18.0.5:8080`) → richieste GET fallite, utenti riescono ad accedere al sito web.

* **Risoluzione**: Problema di spazio su disco pulito, riavviato PostgreSQL, avviato Spring Boot, regolato health-check di nginx.

* **Prevenzione**: Eseguire il monitoraggio tempestivo dello spazio su disco, pulizia automatica dei log, alert su utilizzo del disco, impostazione soft‑limit per dimensione WAL e controlli di integrità.

## Considerazioni (Completamento rimanente)

- Documentare il comportamento anomalo osservato nei log.
- Seguire eventuali ulteriori risoluzioni nel lavoro in corso.
- Preparare report per gli utenti o per gli Amministratori ICT.
- Contattare le due persone menzionate nel Task (staff tecnico + utenti) con le rispettive notifiche al riguardo.