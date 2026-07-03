# glances

**File:** `glances.pdf`
**Tipo:** `.pdf`
**Dimensione:** 363.3 KB
**Ultima modifica:** 02/07/2026 09:22

---

DOCENTE Wolfgang Cecchin
UNITA’ FORMATIVA Linux Server
ARGOMENTO Glances

Glances
Monitoraggio Avanzato del Sistema
ITS ICT Piemonte  |  Corso Linux Server  |  A.F. 2025-2026

Cos'è Glances?
ITS ICT Piemonte  |  Linux Server
Strumento di monitoraggio di sistema scritto in 
Python che fornisce una panoramica completa 
delle risorse in tempo reale in un'unica 
schermata interattiva.
Rispetto a top e htop integra CPU, RAM, swap, 
disco, rete, processi, temperatura e container —
tutto in un'interfaccia coerente e configurabile.
Caratteristiche principali
• Interfaccia ncurses a colori con soglie 
visive
• Modalità standalone, client/server e web
• Export verso CSV, InfluxDB, Prometheus...
• API REST integrata
• Supporto Docker/Podman

Tre Modi per Installare Pacchetti Python
ITS ICT Piemonte  |  Linux Server
Metodo Comando esempio Quando usarlo
apt apt install glances Pacchetti di sistema; spesso versioni datate o incomplete
pip3 pip3 install glances Librerie per progetti in sviluppo; usare dentro un venv
pipx pipx install glances
 Strumenti CLI: ambiente isolato, comando nel PATH
Nota: pipx si installa con apt, non con pip3
apt install pipx -y
pipx ensurepath && source ~/.bashrc

Installazione di Glances
ITS ICT Piemonte  |  Linux Server
Metodo 1 — pip3  (VM di laboratorio)
# Installare pip3 se non presente
apt install python3-pip -y
# Installare Glances con moduli web
pip3 install --break-system-packages \
'glances[web]'
Metodo 2 — pipx  (sistemi reali)
apt install pipx -y
pipx ensurepath && source ~/.bashrc
pipx install glances
pipx inject glances fastapi uvicorn
Attenzione: la versione apt è incompleta per la modalità web (mancano i file statici). Usare sempre pip3 
o pipx.
Verifica: glances --version

Avvio e Navigazione di Base
ITS ICT Piemonte  |  Linux Server
Avvio standalone
glances
Avvia l'interfaccia interattiva sul terminale 
corrente.
Tasto Azione
q / ESC Uscire
h Guida rapida
1 Dettaglio per CPU core
d I/O disco
n Rete
f Filesystem
p / m Ordina per CPU / memoria
i Ordina per I/O
w Cancella avvisi
/ Filtra processi per nome

L'Interfaccia di Glances
ITS ICT Piemonte  |  Linux Server
┌─────────────────────────────────────────────────────────────┐
│  hostname   uptime   load avg   utente   ora                 │
├──────────────┬─────────────────────┬────────────────────────┤
│  CPU         │   MEMORIA           │   SWAP                 │
├──────────────┴─────────────────────┴────────────────────────┤
│  RETE (interfacce, TX/RX)  |  DISCO (I/O)  |  FILESYSTEM   │
├─────────────────────────────────────────────────────────────┤
│  PROCESSI (PID, utente, CPU%, MEM%, nome)                   │
└─────────────────────────────────────────────────────────────┘
Soglie visive:
Verde — Normale Giallo — Careful Arancio — Warning Rosso — Critical

Modalità Web — glances -w
ITS ICT Piemonte  |  Linux Server
Avvia Glances come web server: accessibile da qualsiasi browser senza installare client sulle macchine 
di monitoraggio.
# Avviare il web server (porta default: 61208)
glances -w
# Porta e bind address personalizzati
glances -w --port 61208 --bind 0.0.0.0
http://
IP-SERVER:61208
Richiede l'installazione con moduli web:
pip3 install --break-system-packages 'glances[web]'   # oppure: pipx inject glances fastapi uvicorn

Modalità Server/Client e Non Interattiva
ITS ICT Piemonte  |  Linux Server
Server/Client — monitoraggio remoto
Sul server:
glances -s --port 61209
Sul client:
glances -c IP-SERVER --port 61209
Non Interattiva
# Output testuale
glances --stdout \
cpu.user,mem.percent
# Output CSV
glances --stdout-csv \
cpu.user,mem.percent
Riepilogo delle modalità operative
standalone → glances              web    → glances -w
server     → glances -s           client → glances -c IP

Configurazione — glances.conf
ITS ICT Piemonte  |  Linux Server
Percorsi del file di configurazione:
/etc/glances/glances.conf       # globale (tutti gli utenti)
~/.config/glances/glances.conf  # utente corrente
Soglie CPU
[cpu]
careful=60
warning=80
critical=90
Escludere rete
[network]
hide=lo,docker0
Plugin Docker
[docker]
enable=true

Export dei Dati e Automazione
ITS ICT Piemonte  |  Linux Server
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

Confronto: top vs htop vs Glances
ITS ICT Piemonte  |  Linux Server
Caratteristica top htop Glances
Interfaccia ncurses
Vista rete in tempo reale
Vista disco I/O
Vista filesystem
Modalità web browser
Client/server remoto
Export dati
Docker/container
Soglie visive colorate


Strumento di Supporto: stress-ng
ITS ICT Piemonte  |  Linux Server
stress-ng genera carico artificiale sul sistema — utile per osservare Glances sotto stress e verificare le 
soglie visive in laboratorio.
apt install stress-ng -y
Comando stress-ng Effetto
--cpu 2 --timeout 30s Carica 2 core CPU al 100% per 30s
--vm 2 --vm-bytes 256M --timeout 30s Stress sulla memoria RAM
--hdd 1 --timeout 30s Stress sul disco
--cpu 2 --timeout 30s --metrics-brief Stress CPU con statistiche finali
In laboratorio
Aprire due terminali: Glances in uno, stress-ng nell'altro.
Osservare CPU passare da verde → giallo → arancio → rosso in tempo reale.

Esercizio Pratico — StudioFoto Arcobaleno
ITS ICT Piemonte  |  Linux Server
Scenario
L'amministratore deve configurare un sistema di monitoraggio leggero sul server Debian principale, accessibile via 
browser dai tecnici interni.
1.  Installare stress-ng e Glances sul server Debian tramite pip3.
2.  Personalizzare le soglie CPU (careful=60, warning=80, critical=90).
3.  Avviare Glances in modalità web sulla porta 61208.
4.  Connettersi via browser da un'altra VM e verificare le metriche.
5.  Eseguire stress-ng --cpu 2 --timeout 60s e osservare il cambio di colore.
6.  Esportare le statistiche in CSV e verificarne il contenuto.

Riepilogo
Glances — vista completa su CPU, RAM, disco, rete e container
Installazione — pip3 o pipx (mai apt per la modalità web)
Tre modalità — standalone, web browser, server/client remoto
Configurazione — soglie visive, export dati, plugin Docker
stress-ng — strumento di test per le soglie in laboratorio
Domande?
