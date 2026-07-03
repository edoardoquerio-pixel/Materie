# glances

Fonte: `glances.pdf`

DOCENTE

Wolfgang Cecchin

UNITA’ FORMATIVA

Linux Server

ARGOMENTO

Glances

Glances

Monitoraggio Avanzato del Sistema

ITS ICT Piemonte | Corso Linux Server | A.F. 2025-2026

Cos'è Glances?

Strumento di monitoraggio di sistema scritto in 
Python che fornisce una panoramica completa 
delle risorse in tempo reale in un'unica 
schermata interattiva.

Rispetto a top e htop integra CPU, RAM, swap, 
disco, rete, processi, temperatura e container —
tutto in un'interfaccia coerente e configurabile.

Caratteristiche principali

•

Interfaccia ncurses a colori con soglie 
visive

• Modalità standalone, client/server e web
•
Export verso CSV, InfluxDB, Prometheus...
• API REST integrata
•

Supporto Docker/Podman

ITS ICT Piemonte | Linux Server

Tre Modi per Installare Pacchetti Python

Metodo

Comando esempio

Quando usarlo

apt

pip3

pipx

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

'glances[web]'

apt install pipx -y
pipx ensurepath && source ~/.bashrc
pipx install glances
pipx inject glances fastapi uvicorn

Attenzione: la versione apt è incompleta per la modalità web (mancano i file statici). Usare sempre pip3 
o pipx.

Verifica:

glances --version

ITS ICT Piemonte | Linux Server

Avvio e Navigazione di Base

Avvio standalone

glances

Avvia l'interfaccia interattiva sul terminale 
corrente.

Tasto

q / ESC

Azione

Uscire

h

1

d

n

f

Guida rapida

Dettaglio per CPU core

I/O disco

Rete

Filesystem

p / m

Ordina per CPU / memoria

i

w

/

Ordina per I/O

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

Soglie visive:

Verde — Normale

Giallo — Careful

Arancio — Warning

Rosso — Critical

ITS ICT Piemonte | Linux Server

Modalità Web — glances -w

Avvia Glances come web server: accessibile da qualsiasi browser senza installare client sulle macchine 
di monitoraggio.

# Avviare il web server (porta default: 61208)
glances -w

# Porta e bind address personalizzati
glances -w --port 61208 --bind 0.0.0.0

Richiede l'installazione con moduli web:

http://

IP-SERVER:61208

pip3 install --break-system-packages 'glances[web]' # oppure: pipx inject glances fastapi uvicorn

ITS ICT Piemonte | Linux Server

Modalità Server/Client e Non Interattiva

Server/Client — monitoraggio remoto

Non Interattiva

Sul server:

glances -s --port 61209

Sul client:

glances -c IP-SERVER --port 61209

Riepilogo delle modalità operative

standalone → glances web → glances -w
server → glances -s client → glances -c IP

# Output testuale
glances --stdout \

cpu.user,mem.percent

# Output CSV
glances --stdout-csv \
cpu.user,mem.percent

ITS ICT Piemonte | Linux Server

Configurazione — glances.conf

Percorsi del file di configurazione:

/etc/glances/glances.conf # globale (tutti gli utenti)
~/.config/glances/glances.conf # utente corrente

Soglie CPU

[cpu]
careful=60
warning=80
critical=90

Escludere rete

Plugin Docker

[network]
hide=lo,docker0

[docker]
enable=true

ITS ICT Piemonte | Linux Server

Export dei Dati e Automazione

Export dei dati

# Export CSV
glances --export csv \

--export-csv-file /tmp/stats.csv

# Export InfluxDB
glances --export influxdb

In glances.conf:

[csv]
path=/var/log/glances/stats.csv

Script di automazione

#!/bin/bash
# Alert se CPU > 80%

CPU=$(glances --stdout \

cpu.total --quiet | tail -n1)

if (( $(echo "$CPU > 80" | bc -l) )); then

echo "ALERT: CPU ${CPU}%" |
mail -s "CPU Alert" admin@it

fi

ITS ICT Piemonte | Linux Server

Confronto: top vs htop vs Glances

top

htop

Glances

Caratteristica

Interfaccia ncurses

Vista rete in tempo reale

Vista disco I/O

Vista filesystem

Modalità web browser

Client/server remoto

Export dati

Docker/container

Soglie visive colorate

ITS ICT Piemonte | Linux Server

Strumento di Supporto: stress-ng

stress-ng genera carico artificiale sul sistema — utile per osservare Glances sotto stress e verificare le 
soglie visive in laboratorio.

apt install stress-ng -y

Comando stress-ng

--cpu 2 --timeout 30s

Effetto

Carica 2 core CPU al 100% per 30s

--vm 2 --vm-bytes 256M --timeout 30s

Stress sulla memoria RAM

--hdd 1 --timeout 30s

Stress sul disco

--cpu 2 --timeout 30s --metrics-brief

Stress CPU con statistiche finali

In laboratorio

Aprire due terminali: Glances in uno, stress-ng nell'altro.
Osservare CPU passare da verde → giallo → arancio → rosso in tempo reale.

ITS ICT Piemonte | Linux Server

Esercizio Pratico — StudioFoto Arcobaleno

Scenario

L'amministratore deve configurare un sistema di monitoraggio leggero sul server Debian principale, accessibile via 
browser dai tecnici interni.

1. Installare stress-ng e Glances sul server Debian tramite pip3.
2. Personalizzare le soglie CPU (careful=60, warning=80, critical=90).
3. Avviare Glances in modalità web sulla porta 61208.
4. Connettersi via browser da un'altra VM e verificare le metriche.
5. Eseguire stress-ng --cpu 2 --timeout 60s e osservare il cambio di colore.
6. Esportare le statistiche in CSV e verificarne il contenuto.

ITS ICT Piemonte | Linux Server

Riepilogo

Glances — vista completa su CPU, RAM, disco, rete e container

Installazione — pip3 o pipx (mai apt per la modalità web)

Tre modalità — standalone, web browser, server/client remoto

Configurazione — soglie visive, export dati, plugin Docker

stress-ng — strumento di test per le soglie in laboratorio

Domande?