# Esercizio Ripasso Finale CSP

## Panoramica
ITS ICT Piemonte · Linux Server

## Argomenti trattati
Linux, Cloud, Data Analytics, Database, Installazione

---
## Appunti

ITS ICT Piemonte · Linux Server
ESERCIZIO — StudioFoto Arcobaleno
ITS ICT Piemonte
Corso Linux Server — CSP — Cloud Specialist
Ripasso finale — Linux Server
Scenario: StudioFoto Arcobaleno
Traccia da consegnare allo studente
Durata: 2 ore · Valutazione: 16 punti (1 per punto) — sufficienza a 10
ITS ICT Piemonte · Linux Server
ESERCIZIO — StudioFoto Arcobaleno
Consegna. Ti viene affidata una VM Debian 12 minimale. Lo StudioFoto Arcobaleno
deve disporre di un piccolo server con sito PHP, database e accesso remoto sicuro.
Per ogni punto riporta i comandi usati e/o il contenuto dei file modificati, con
l'output di verifica dove richiesto.
Ambiente di partenza
• VM Debian 12 in installazione minimale
• Utente di lavoro: its-usr / Its2026, con privilegi sudo
• Interfacce VirtualBox: NAT (enp0s3), Solo Host (enp0s8)
Parte 1 — Utenti, gruppi e permessi (~25 min)
1. Imposta l'hostname arcobaleno-srv in modo persistente e verificalo.
2. Crea il gruppo fotografi e gli utenti anna e luca, entrambi membri del gruppo,
con home e shell /bin/bash.
3. Crea la directory condivisa /srv/scatti e configurala affinché: i membri di
fotografi possano leggere/scrivere, ogni nuovo file erediti il gruppo fotografi, e
ciascuno possa cancellare solo i propri file. Spiega quali bit speciali hai usato e
Parte 2 — Rete (~15 min)
4. Configura un IP statico su enp0s8: 192.168.56.120/24, lasciando il NAT (enp0s3)
5. Aggiungi in /etc/hosts un record che associ db.arcobaleno.local a 10.0.0.2 e
verifica la risoluzione.
Parte 3 — Accesso remoto SSH (~15 min)
6. Abilita l'accesso a its-usr tramite chiave pubblica.
7. Configura OpenSSH per disabilitare il login di root e l'autenticazione tramite
password. Ricarica il servizio e verifica che sia attivo.
Parte 4 — Web server nginx + PHP (~20 min)
8. Installa nginx e PHP-FPM (ricorda: NON il metapacchetto generico php).
9. Crea /var/www/arcobaleno/info.php con phpinfo() e configura un virtual host
minimale che lo serva. Verifica che PHP venga interpretato (non scaricato).
Parte 5 — Database MariaDB (~15 min)
10. Installa MariaDB ed esegui la messa in sicurezza iniziale.
11. Crea il database arcobaleno_db e l'utente wpuser con privilegi limitati al solo
arcobaleno_db. Verifica il login con il nuovo utente.
Parte 6 — Processi e servizi (~10 min)
ITS ICT Piemonte · Linux Server
ESERCIZIO — StudioFoto Arcobaleno
12. Verifica lo stato di nginx, php-fpm e mariadb e abilitane l'avvio automatico al
13. Avvia sleep 1000 & , individua il suo PID e terminalo con il segnale appropriato.
Parte 7 — Automazione (cron) e firewall (iptables) (~15 min)
14. Scrivi /usr/local/bin/backup-scatti.sh che crei un archivio scatti-AAAA-MM-
GG.tar.gz di /srv/scatti in /var/backups/. Rendilo eseguibile e pianificalo con
cron ogni notte alle 02:30.
15. Installa iptables (non preinstallato su Debian minimale) e definisci regole con
policy di default DROP in INPUT che consentano: loopback, traffico
ESTABLISHED,RELATED, SSH e HTTP. Rendile persistenti.
Parte 8 — Diagnostica (~5 min)
1. Un fotografo segnala che il sito non risponde. Descrivi la procedura
diagnostica bottom-up (rete → firewall → servizio → applicazione) indicando
almeno un comando di verifica per ogni livello.

---
*Fonte: 999_Esercizio_Ripasso_Finale_CSP.md*
