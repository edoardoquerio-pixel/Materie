# Passaggi Ripasso Finale CSP

## Panoramica
ITS ICT Piemonte · Linux Server

## Argomenti trattati
Linux, Cloud, Reti, Configurazione, API REST

---
## Appunti

ITS ICT Piemonte · Linux Server
PASSAGGI — StudioFoto Arcobaleno
ITS ICT Piemonte
Corso Linux Server — CSP — Cloud Specialist
Ripasso finale — Linux Server
Scenario: StudioFoto Arcobaleno
Guida operativa passo-passo
Durata: 2 ore · Valutazione: 16 punti (1 per punto) — sufficienza a 10
ITS ICT Piemonte · Linux Server
PASSAGGI — StudioFoto Arcobaleno
Nota — Questa guida elenca la sequenza ordinata delle operazioni da svolgere, parte
per parte. Indica il “come” procedurale; la sintassi esatta dei comandi e gli output sono
nel documento Soluzione.
Parte 1 — Utenti, gruppi e permessi (~25 min)
1. Imposta l'hostname con il comando dedicato di systemd, poi rileggilo per
confermare che sia persistente.
2. Crea il gruppo di lavoro, quindi crea i due utenti aggiungendoli al gruppo al
momento della creazione (home + shell bash).
3. Imposta una password per ciascun utente e verifica l'appartenenza ai gruppi.
4. Crea la directory condivisa e assegnala al gruppo fotografi.
5. Applica i permessi con i due bit speciali: SGID (eredità del gruppo) e Sticky bit
(cancellazione solo dei propri file).
6. Verifica i permessi risultanti con un listing della directory.
Parte 2 — Rete (~15 min)
1. Apri il file di configurazione delle interfacce di Debian
(/etc/network/interfaces).
2. Lascia l'interfaccia NAT in DHCP; configura l'interfaccia Solo Host come statica
con indirizzo e netmask richiesti.
3. Riavvia il servizio di rete e verifica l'indirizzo assegnato.
4. Aggiungi la riga di mappatura nome→IP nel file degli host.
5. Verifica la risoluzione del nome con getent o ping.
Parte 3 — Accesso remoto SSH (~15 min)
1. Sul client genera una coppia di chiavi (preferibilmente ed25519).
2. Copia la chiave pubblica sul server nell'account its-usr (ssh-copy-id).
3. Verifica l'accesso con chiave prima di disabilitare la password.
4. Modifica sshd_config: nega il login di root e disattiva l'autenticazione via
password (assicurandoti che la chiave pubblica sia abilitata).
5. Controlla la sintassi della configurazione, ricarica il servizio e verificane lo stato.
Parte 4 — Web server nginx + PHP (~20 min)
1. Aggiorna l'indice dei pacchetti e installa nginx insieme a php-fpm (mai il
metapacchetto php, che trascinerebbe Apache).
2. Crea la document root e la pagina info.php con la chiamata a phpinfo().
3. Crea un file di virtual host in sites-available con root, server_name e il blocco
location per i file .php verso il socket di PHP-FPM.
4. Abilita il sito con un link simbolico in sites-enabled.
5. Controlla la sintassi di nginx, ricarica il servizio e verifica con curl che la pagina
venga interpretata (HTML), non restituita come sorgente PHP.
ITS ICT Piemonte · Linux Server
PASSAGGI — StudioFoto Arcobaleno
Parte 5 — Database MariaDB (~15 min)
1. Installa il pacchetto server di MariaDB.
2. Esegui lo script di hardening iniziale (password root, rimozione utenti anonimi e
3. Entra nella console come amministratore e crea il database applicativo.
4. Crea l'utente applicativo e assegnagli i privilegi solo sul database
arcobaleno_db; ricarica i privilegi.
5. Verifica effettuando il login con il nuovo utente e controllando i database
Parte 6 — Processi e servizi (~10 min)
1. Abilita all'avvio e avvia i tre servizi in un solo comando, poi verifica che siano
enabled e active.
2. Lancia il processo sleep in background.
3. Individua il PID con jobs oppure con ps.
4. Termina il processo con il segnale standard (SIGTERM); ricorri a SIGKILL solo se
Parte 7 — Automazione (cron) e firewall (iptables) (~15 min)
1. Scrivi lo script: variabili per sorgente/destinazione, data nel nome dell'archivio
(date +%F), creazione dell'archivio compresso con tar.
2. Rendi lo script eseguibile e pianificalo nel crontab alle 02:30.
3. Installa iptables e iptables-persistent.
4. Inserisci PRIMA le regole di ACCEPT (loopback, connessioni stabilite, SSH, HTTP)
e SOLO DOPO imposta la policy INPUT su DROP, per non perdere la sessione
5. Salva le regole per renderle persistenti al riavvio e verifica con un listing.
Parte 8 — Diagnostica (~5 min)
1. Parti dal livello più basso e sali: prima la connettività di rete, poi il filtraggio del
firewall, poi lo stato del servizio, infine l'applicazione.
2. Per ogni livello esegui un controllo mirato e procedi al livello superiore solo
quando quello inferiore è confermato funzionante.

---
*Fonte: 999_Passaggi_Ripasso_Finale_CSP.md*
