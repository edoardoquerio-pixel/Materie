# glances

## Panoramica
Monitoraggio Avanzato del Sistema

## Argomenti trattati
Linux, Reti, API REST, Docker, Data Analytics

---
## Appunti

Wolfgang Cecchin
UNITA’ FORMATIVA
Monitoraggio Avanzato del Sistema
ITS ICT Piemonte | Corso Linux Server | A.F. 2025-2026
Strumento di monitoraggio di sistema scritto in
Python che fornisce una panoramica completa
delle risorse in tempo reale in un'unica
schermata interattiva.
Rispetto a top e htop integra CPU, RAM, swap,
disco, rete, processi, temperatura e container —
tutto in un'interfaccia coerente e configurabile.
Caratteristiche principali
Interfaccia ncurses a colori con soglie
• Modalità standalone, client/server e web
Export verso CSV, InfluxDB, Prometheus...
• API REST integrata
Supporto Docker/Podman
ITS ICT Piemonte | Linux Server
Tre Modi per Installare Pacchetti Python
Comando esempio
apt install glances
pip3 install glances
pipx install glances
Pacchetti di sistema; spesso versioni datate o incomplete
Librerie per progetti in sviluppo; usare dentro un venv
Strumenti CLI: ambiente isolato, comando nel PATH
Nota: pipx si installa con apt, non con pip3
apt install pipx -y
pipx ensurepath && source ~/.bashrc
ITS ICT Piemonte | Linux Server
Installazione di Glances
Metodo 1 — pip3 (VM di laboratorio)
Metodo 2 — pipx (sistemi reali)
# Installare pip3 se non presente
apt install python3-pip -y
# Installare Glances con moduli web
pip3 install --break-system-packages \
apt install pipx -y
pipx ensurepath && source ~/.bashrc
pipx install glances
pipx inject glances fastapi uvicorn
Attenzione: la versione apt è incompleta per la modalità web (mancano i file statici). Usare sempre pip3
glances --version
ITS ICT Piemonte | Linux Server
Avvio e Navigazione di Base
Avvio standalone
Avvia l'interfaccia interattiva sul terminale
Dettaglio per CPU core
Ordina per CPU / memoria
Cancella avvisi
Filtra processi per nome
ITS ICT Piemonte | Linux Server
L'Interfaccia di Glances
┌─────────────────────────────────────────────────────────────┐
│ hostname uptime load avg utente ora │
├──────────────┬─────────────────────┬────────────────────────┤
│ CPU │ MEMORIA │ SWAP │
├──────────────┴─────────────────────┴────────────────────────┤
│ RETE (interfacce, TX/RX) | DISCO (I/O) | FILESYSTEM │
├─────────────────────────────────────────────────────────────┤
│ PROCESSI (PID, utente, CPU%, MEM%, nome) │
└─────────────────────────────────────────────────────────────┘
Verde — Normale
Giallo — Careful
Arancio — Warning
Rosso — Critical
ITS ICT Piemonte | Linux Server
Modalità Web — glances -w
Avvia Glances come web server: accessibile da qualsiasi browser senza installare client sulle macchine
di monitoraggio.
# Avviare il web server (porta default: 61208)
# Porta e bind address personalizzati
glances -w --port 61208 --bind 0.0.0.0
Richiede l'installazione con moduli web:
IP-SERVER:61208
pip3 install --break-system-packages 'glances[web]' # oppure: pipx inject glances fastapi uvicorn
ITS ICT Piemonte | Linux Server
Modalità Server/Client e Non Interattiva
Server/Client — monitoraggio remoto
Non Interattiva

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_glances.md*
