# glances doc

**File:** `glances doc.pdf`
**Tipo:** `.pdf`
**Dimensione:** 3918.1 KB
**Ultima modifica:** 02/07/2026 09:22

---

ITS ICT Piemonte  |  Corso Linux Server 
Glances — Monitoraggio Avanzato del Sistema 
Glances 
Monitoraggio Avanzato del Sistema 
ITS ICT Piemonte  |  Corso Linux Server  |  A.F. 2025-2026 
1. Introduzione 
Glances è uno strumento di monitoraggio di sistema scritto in Python che fornisce 
una panoramica completa delle risorse in tempo reale, in un'unica schermata 
interattiva. Rispetto a top e htop, Glances integra CPU, RAM, swap, disco, rete, 
processi, temperatura, container e molto altro, tutto in un'interfaccia coerente e 
altamente configurabile. 
  
Caratteristiche principali: 
• Interfaccia ncurses a colori con soglie visive (verde / giallo / arancio / rosso) 
• Modalità standalone, client/server e web browser 
• Export dei dati verso CSV, InfluxDB, Prometheus, Elasticsearch e altri 
• API REST integrata 
• Supporto per container Docker/Podman 
2. Tre Modi per Installare Pacchetti Python 
Prima di installare Glances è utile capire le differenze tra i metodi di installazione 
disponibili su Debian. 
  
Metodo Comando esempio Quando usarlo 
apt apt install glances Pacchetti di sistema; spesso versioni datate o 
incomplete 
pip3 pip3 install glances Librerie per progetti in sviluppo; usare sempre 
dentro un venv 
pipx pipx install glances Strumenti CLI: ambiente isolato, comando 
disponibile globalmente 
  
Perché non pip3 install globale?  Su Debian 12, pip3 install globale è bloccato per 
default. Il flag --break-system-packages lo forza, ma può sovrascrivere librerie di 
sistema e causare conflitti. Il nome del flag è già un avviso. 
pipx è la soluzione corretta per strumenti CLI come Glances: ogni applicazione vive 
nel proprio ambiente virtuale isolato, il sistema rimane pulito, il comando è 
disponibile nel PATH come un normale programma. 
  
Nota: pipx si installa con apt, non con pip3 
Usare apt per installare pipx, poi pipx per installare Glances: 

ITS ICT Piemonte  |  Corso Linux Server 
Glances — Monitoraggio Avanzato del Sistema 
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
# apt install glances   <-- NON usare per la modalità web 
  
Verifica dell'installazione 
glances --version 
4. Avvio e Navigazione di Base 
Avvio standalone 
glances 
  
Navigazione da tastiera 
Tasto Azione 
q / ESC Uscire dall'interfaccia 
h Mostrare la guida 
1 Dettaglio per ogni CPU core 
d Mostrare/nascondere I/O disco 
n Mostrare/nascondere rete 

ITS ICT Piemonte  |  Corso Linux Server 
Glances — Monitoraggio Avanzato del Sistema 
Tasto Azione 
f Mostrare/nascondere filesystem 
p Ordinare processi per CPU% 
m Ordinare processi per memoria 
i Ordinare per I/O 
t Statistiche di rete aggregate 
w Cancellare log di avvisi 
/ Filtrare processi per nome 
5. Anatomia dell'Interfaccia 
┌─────────────────────────────────────────────────────┐ 
│  hostname   uptime   load avg   utente   ora         │ 
├──────────┬──────────────────┬────────────────────────┤ 
│  CPU     │   MEMORIA        │   SWAP                 │ 
├──────────┴──────────────────┴────────────────────────┤ 
│  RETE (interfacce, TX/RX)                            │ 
│  DISCO (I/O, lettura/scrittura)                      │ 
│  FILESYSTEM (partizioni, uso %)                      │ 
├──────────────────────────────────────────────────────┤ 
│  PROCESSI (PID, utente, CPU%, MEM%, nome)            │ 
└──────────────────────────────────────────────────────┘ 
  
Colori di soglia: 
Colore Soglia Significato 
Verde -- Normale 
Giallo careful Attenzione 
Arancio warning Avviso 
Rosso critical Critico 
6. Modalità Operative 
6.1 Modalità Web (browser) 
Permette di monitorare il server da qualsiasi browser senza client installato. 
# Avviare il web server (porta default: 61208) 
glances -w 
  
# Specificare porta e bind address 
glances -w --port 61208 --bind 0.0.0.0 
Aprire nel browser: http://IP-SERVER:61208 
  
6.2 Modalità Server/Client (via rete) 

ITS ICT Piemonte  |  Corso Linux Server 
Glances — Monitoraggio Avanzato del Sistema 
Sul server: 
glances -s --port 61209 
Sul client: 
glances -c IP-SERVER --port 61209 
  
6.3 Modalità Non Interattiva (output per script) 
# Output testuale una tantum 
glances --stdout cpu.user,mem.percent,load 
  
# Output CSV 
glances --stdout-csv cpu.user,mem.percent 
7. Configurazione 
Il file di configurazione si trova nei seguenti percorsi: 
/etc/glances/glances.conf       # globale (tutti gli utenti) 
~/.config/glances/glances.conf  # utente corrente 
  
Personalizzare le soglie CPU 
[cpu] 
careful=60 
warning=80 
critical=90 
  
Escludere interfacce di rete 
[network] 
hide=lo,docker0 
  
Abilitare il plugin Docker 
[docker] 
enable=true 
8. Export dei Dati 
# Export verso file CSV 
glances --export csv --export-csv-file /tmp/glances_stats.csv 
  
# Export verso InfluxDB (richiede: pipx inject glances influxdb-client) 
glances --export influxdb 
  

ITS ICT Piemonte  |  Corso Linux Server 
Glances — Monitoraggio Avanzato del Sistema 
Configurazione export CSV in glances.conf 
[csv] 
path=/var/log/glances/stats.csv 
9. Utilizzo in Script e Automazione 
#!/bin/bash 
# Alert via email se CPU supera l'80% 
  
CPU=$(glances --stdout cpu.total --quiet | tail -n1) 
if (( $(echo "$CPU > 80" | bc -l) )); then 
    echo "ALERT: CPU al ${CPU}%" | mail -s "CPU Alert" admin@azienda.it 
fi 
10. Confronto con Altri Strumenti 
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
11. Strumento di Supporto: stress-ng 
stress-ng genera carico artificiale sul sistema. In laboratorio è utile per osservare il 
comportamento di Glances sotto stress e verificare visivamente le soglie di allerta. 
apt install stress-ng -y 
  
Comando Effetto 
stress-ng --cpu 2 --timeout 30s Carica 2 core CPU al 100% per 30 secondi 
stress-ng --vm 2 --vm-bytes 256M --timeout 
30s 
Stress sulla memoria RAM 
stress-ng --hdd 1 --timeout 30s Stress sul disco 
stress-ng --cpu 2 --timeout 30s --metrics-
brief 
Stress CPU con statistiche finali 

ITS ICT Piemonte  |  Corso Linux Server 
Glances — Monitoraggio Avanzato del Sistema 
  
In laboratorio 
Aprire due terminali: Glances in uno, stress-ng nell'altro. 
Osservare i colori CPU passare da verde → giallo → arancio → rosso in tempo reale.  
12. Esercizio Pratico 
Scenario — StudioFoto Arcobaleno 
L'amministratore deve configurare un sistema di monitoraggio leggero sul server Debian  
principale, accessibile anche via browser dai tecnici interni. 
  
Obiettivi: 
1. Installare stress-ng e Glances sul server Debian tramite pip3. 
2. Personalizzare le soglie CPU nel file di configurazione (careful=60, warning=80, 
critical=90). 
3. Avviare Glances in modalità web sulla porta 61208. 
4. Connettersi via browser da un'altra VM e verificare le metriche. 
5. In un secondo terminale, eseguire stress-ng --cpu 2 --timeout 60s e osservare il 
cambio di colore in Glances. 
6. Esportare un campione di statistiche in CSV e verificarne il contenuto. 
