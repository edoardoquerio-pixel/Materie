# glances doc

## Panoramica
ITS ICT Piemonte | Corso Linux Server

## Argomenti trattati
Linux, Reti, API REST, Docker, Installazione

---
## Appunti

ITS ICT Piemonte | Corso Linux Server
Monitoraggio Avanzato del Sistema
ITS ICT Piemonte | Corso Linux Server | A.F. 2025-2026
1. Introduzione
Glances è uno strumento di monitoraggio di sistema scritto in Python che fornisce
una panoramica completa delle risorse in tempo reale, in un'unica schermata
interattiva. Rispetto a top e htop, Glances integra CPU, RAM, swap, disco, rete,
processi, temperatura, container e molto altro, tutto in un'interfaccia coerente e
altamente configurabile.
Caratteristiche principali:
Interfaccia ncurses a colori con soglie visive (verde / giallo / arancio / rosso)
• Modalità standalone, client/server e web browser
• Export dei dati verso CSV, InfluxDB, Prometheus, Elasticsearch e altri
• API REST integrata
• Supporto per container Docker/Podman
2. Tre Modi per Installare Pacchetti Python
Prima di installare Glances è utile capire le differenze tra i metodi di installazione
disponibili su Debian.
Comando esempio
apt install glances
pip3 install glances
pipx install glances
Pacchetti di sistema; spesso versioni datate o
Librerie per progetti in sviluppo; usare sempre
Strumenti CLI: ambiente isolato, comando
disponibile globalmente
Perché non pip3 install globale? Su Debian 12, pip3 install globale è bloccato per
default. Il flag --break-system-packages lo forza, ma può sovrascrivere librerie di
sistema e causare conflitti. Il nome del flag è già un avviso.
pipx è la soluzione corretta per strumenti CLI come Glances: ogni applicazione vive
nel proprio ambiente virtuale isolato, il sistema rimane pulito, il comando è
disponibile nel PATH come un normale programma.
Nota: pipx si installa con apt, non con pip3
Usare apt per installare pipx, poi pipx per installare Glances:
Glances — Monitoraggio Avanzato del Sistema
ITS ICT Piemonte | Corso Linux Server
apt install pipx -y
pipx ensurepath && source ~/.bashrc
3. Installazione
Metodo 1 — pip3 (adatto a VM di laboratorio)
# Installare pip3 se non presente
apt install python3-pip -y
# Installare Glances con i moduli web
pip3 install --break-system-packages 'glances[web]'
Metodo 2 — pipx (consigliato su sistemi reali)
apt install pipx -y
pipx ensurepath && source ~/.bashrc
pipx install glances
pipx inject glances fastapi uvicorn jinja2 aiofiles
Metodo da evitare per la modalità web
# La versione apt è incompleta: mancano i file statici per glances -w
# apt install glances <-- NON usare per la modalità web
Verifica dell'installazione
glances --version
4. Avvio e Navigazione di Base
Avvio standalone
Navigazione da tastiera
Uscire dall'interfaccia
Mostrare la guida
Dettaglio per ogni CPU core
Mostrare/nascondere I/O disco
Mostrare/nascondere rete
Glances — Monitoraggio Avanzato del Sistema
ITS ICT Piemonte | Corso Linux Server
Mostrare/nascondere filesystem
Ordinare processi per CPU%
Ordinare processi per memoria
Ordinare per I/O
Statistiche di rete aggregate
Cancellare log di avvisi
Filtrare processi per nome
5. Anatomia dell'Interfaccia
┌─────────────────────────────────────────────────────┐
│ hostname uptime load avg utente ora │
├──────────┬──────────────────┬────────────────────────┤
│ CPU │ MEMORIA │ SWAP │
├──────────┴──────────────────┴────────────────────────┤
│ RETE (interfacce, TX/RX) │
│ DISCO (I/O, lettura/scrittura) │
│ FILESYSTEM (partizioni, uso %) │

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_glances_doc.md*
