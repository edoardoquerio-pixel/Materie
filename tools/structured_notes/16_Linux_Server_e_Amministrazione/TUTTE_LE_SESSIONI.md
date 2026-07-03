# 16 - Linux Server e Amministrazione — Tutte le Sessioni


---

## Sessione 1: Consegna Esercitazione doc


ITS ICT Piemonte — Linux Server
Diagnostica e messa in sicurezza di un'infrastruttura WordPress
Docente: Wolfgang Cecchin
L'azienda Acme S.r.l. ha commissionato a un fornitore esterno la realizzazione del proprio sito
web WordPress, ospitato su un'infrastruttura a due macchine virtuali Debian:
Frontend — nginx + WordPress + PHPFPM
Solo Host + rete interna
Backend — MariaDB
Solo rete interna
Le due macchine comunicano attraverso una rete interna privata (intnet, rete 10.0.0.0/24). Il
sito WordPress su debian3 si collega al database MariaDB su debian4 tramite questa rete.
Al momento della consegna, l'azienda Acme scopre che il sito non funziona e che
l'infrastruttura presenta diversi problemi di configurazione. L'azienda vi incarica di intervenire.
Informazioni di accesso
SSH dalla macchina Windows, porta 2222, autenticazione con
username e password
Non raggiungibile via SSH. Accesso esclusivamente dalla console
VirtualBox (equivalente all'accesso fisico in sala server)
Fase 1 — Report diagnostico
Prima di intervenire sulla configurazione, Acme chiede un report scritto da presentare al
fornitore che ha eseguito il lavoro. Il report deve documentare ogni problema riscontrato,
indicando per ciascuno:
• Cosa non funziona — il sintomo osservato (es. "il sito non risponde nel browser")
• Dove si trova il problema — il file di configurazione, la regola o il servizio coinvolto
• Perché non funziona — la causa tecnica (es. "il firewall blocca la porta 80 in ingresso")
Suggerimento: procedete con metodo, verificando un livello alla volta — prima la rete, poi il
firewall, poi i servizi — su ciascuna macchina.
Fase 2 — Ripristino e messa in sicurezza
Una volta completato il report, Acme chiede di correggere tutti i problemi individuati e
rendere il sito WordPress raggiungibile dal PC Windows.
ITS ICT Piemonte — Linux Server
Per visualizzare il sito dal browser Windows, aggiungere una riga nel file
C:\Windows\System32\drivers\etc\hosts:
192.168.56.111 acme.local
Il sito deve rispondere al nome acme.local — L'infrastruttura è attualmente configurata con
un nome generico scelto dal fornitore. Acme richiede che il sito risponda al nome
acme.local, sia nella configurazione di nginx che in quella di WordPress.
Oltre alla correzione dei guasti, Acme richiede che l'infrastruttura rispetti i seguenti requisiti di
Requisiti di sicurezza
Firewall su entrambe le macchine — Entrambe le VM devono avere un firewall iptables
attivo con policy di default DROP sulla catena INPUT. Le porte aperte devono essere
esclusivamente quelle necessarie:
• debian3: SSH (2222), HTTP (80), traffico dalla rete interna
• debian4: SSH (2222) solo dalla rete interna, MariaDB (3306) solo dalla rete interna
Accesso SSH a debian4 solo da debian3 — Nessun accesso diretto dall'esterno a debian4.
L'unico modo per raggiungerla via SSH deve essere passando da debian3 attraverso la rete
MariaDB non esposto all'esterno — Il database deve essere in ascolto esclusivamente
sull'interfaccia di rete interna (10.0.0.2), non su tutte le interfacce.
Persistenza — Tutte le configurazioni (rete, firewall, servizi) devono sopravvivere a un riavvio
della macchina.
Alla fine dell'esercitazione, consegnare:
1. Report diagnostico della Fase 1 (formato libero, ma chiaro e strutturato)
2. Descrizione degli interventi eseguiti nella Fase 2, con i comandi utilizzati e una breve
motivazione per ciascuno

---

## Sessione 2: Consegna Esercitazione ppt


Diagnostica e messa in sicurezza
di un'infrastruttura WordPress
Docente: Wolfgang Cecchin
L'azienda Acme S.r.l. ha commissionato a un fornitore esterno un sito WordPress su due VM
Debian. Alla consegna, il sito non funziona.
Frontend — nginx + WordPress + PHP-FPM
Solo Host + rete interna
Backend — MariaDB
Solo rete interna
Comunicazione via rete interna privata intnet (10.0.0.0/24)
debian3 (frontend)
debian4 (backend)
intnet 10.0.0.0/24
Informazioni di accesso
SSH dalla macchina Windows, porta 2222
Autenticazione con username e password
Non raggiungibile via SSH
Accesso dalla console VirtualBox
Fase 1 — Report diagnostico
Acme chiede un report scritto da presentare al fornitore. Per ogni problema:
Cosa non funziona
Perché non funziona
Il sintomo osservato
File, regola o servizio
La causa tecnica
Suggerimento: procedete per livelli — rete → firewall → servizi — su ciascuna macchina.
Fase 2 — Ripristino e messa in sicurezza
Correggere i guasti e rendere il sito raggiungibile come acme.local
192.168.56.111 acme.local
→ aggiungere in C:\Windows\System32\drivers\etc\hosts
Il sito deve rispondere al nome acme.local — sia nella configurazione di nginx (server_name) che
in WordPress (tabella wp_options nel database).
Requisiti di sicurezza
Firewall su entrambe le macchine
SSH a debian4 solo da debian3
iptables attivo, policy DROP su INPUT.
debian3: SSH (2222), HTTP (80)
debian4: SSH (2222) + MariaDB (3306) solo da
Nessun accesso diretto dall'esterno.
Passare per la rete interna.
MariaDB non esposto
In ascolto solo su 10.0.0.2,
non su tutte le interfacce.
Tutte le configurazioni devono
sopravvivere a un riavvio.
1 Report diagnostico
Formato libero, chiaro e strutturato
2 Descrizione degli interventi
Comandi utilizzati e motivazione

---

## Sessione 3: DevOps per non DevOps- slides del Meet tenuto all'Agile Community Torino, 2018


+Agile meetup | 5 Dicembre:
INTRODUZIONE A DEVOPS
IN COLLABORAZIONE CON
© 2018 DropletBENVENUTI!
WOLFGANG CECCHIN
SOCIO FONDATORE DI DROPLET*
MARCO BOZZOLAN,
GESTORE SISTEMI DROPLET*
*DROPLET SI OCCUPA DI
© 2018 Droplet 2
COME ARRIVIAMO A DEVOPS?,
WOLFGANG CECCHIN
CONSIDERAZIONI FINALI
© 2018 Droplet 3
© 2018 Droplet 4
© 2018 Droplet 5DEV
© 2018 Droplet 6N
© 2018 Droplet 7MA
COME ARRIVIAMO A
© 2018 Droplet 8FACCIAMO UN
RIAVVOLGIAMO IL NASTRO…
© 2018 Droplet© 2018 DropletMMM…
LO ABBIAMO RIAVVOLTO
© 2018 DropletRIAVVOLGIAMO IL NASTRO:
OK, FERMIAMOCI UN PÒ PRIMA E PARLIAMO DI “STORIA” E DI
RIAVVOLGIAMO IL NASTRO:
L’ETÀ DEL FERRO
PRIMA DEL 2001 D.C.
© 2018 Droplet 14
ETÀ “DEL FERRO”
OPERAZIONI SUI SERVER:
• Assemblaggio hardware;
• Installazione sistema operativo;
• Installazione e conﬁgurazione software accessori (utenti, librerie);
• Installazione e conﬁgurazione del software sviluppato.
© 2018 Droplet 15
• CQ (AKA “Test", “System Test”, “Pre-prod”, “Gold”,
© 2018 Droplet 16
RIDONDANZA E SCALING:
• Raid (ridondanza sui dischi);
• Macchine di backup (cloni);
© 2018 Droplet 17
E SE QUALCOSA SI SPACCA?
Repeat again and again:
Assemblaggio hardware;
• Installazione sistema operativo;
• Installazione e conﬁgurazione software accessori (utenti, librerie);
• Installazione e conﬁgurazione del software sviluppato.
© 2018 Droplet 18
RIAVVOLGIAMO IL NASTRO:
L’ETÀ DEL FERRO
PRIMA DEL 2001 D.C.
VIRTUAL MACHINES
© 2018 Droplet 19
ETÀ DELLE VIRTUAL
L’INFRASTRUTTURA
© 2018 Droplet 20
OPERAZIONI SUI SERVER:
• Assemblaggio hardware;
• Installazione sistema operativo;
• Installazione e conﬁgurazione software accessori (utenti, librerie);
• Installazione e conﬁgurazione del software sviluppato.
© 2018 Droplet 21
ETÀ DELLE VIRTUAL
OPERAZIONI SUI SERVER:
• Assemblaggio hardware;
• Installazione sistema operativo; +allocazione risorse;
• Installazione e conﬁgurazione software accessori (utenti, librerie);
• Installazione e conﬁgurazione del software sviluppato.
© 2018 Droplet 22
ETÀ DELLE VIRTUAL
• Le VM si clonano (CQ, Dev, PROD) e si spostano;
• Le risorse delle VM si possono aumentare con pochi click.
© 2018 Droplet 23
ETÀ DELLE VIRTUAL
• Devono essere allocate delle risorse hardware ad hoc.
© 2018 Droplet 24
ETÀ DELLE VIRTUAL
PRODOTTI PRINCIPALI:
• VMWare ESX(i) Server;

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 4: Esercizio Ripasso Finale CSP


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

## Sessione 5: Firewall Linux doc


Wolfgang Cecchin
UNITA’ FORMATIVA
Firewall: iptables, ufw
Firewall in Linux
Cos'è un firewall
Un firewall è un sistema che controlla il traffico di rete in entrata e in uscita sulla base di un
insieme di regole. Su un server Linux, il firewall è fondamentale per proteggere i servizi
esposti: si decide esplicitamente cosa è permesso, e tutto il resto viene bloccato.
Il kernel Linux gestisce il filtraggio dei pacchetti attraverso un sottosistema chiamato
Netfilter. Gli strumenti iptables e ufw sono semplicemente interfacce per scrivere
regole che Netfilter applica.
Nota: Il successore moderno di iptables è nftables, diventato predefinito a partire da Debian 10.
Su sistemi recenti, il comando iptables è in realtà un wrapper che traduce i comandi in regole
nftables sottostanti. Per i server applicativi standard, iptables e ufw restano comunque lo
strumento pratico di riferimento.
Parte 1 — iptables
Come funziona iptables
iptables organizza le regole in tabelle e catene.
La tabella più usata è filter, che contiene tre catene predefinite:
• INPUT — traffico diretto al server stesso
• OUTPUT — traffico generato dal server
• FORWARD — traffico che transita attraverso il server (usato nei router)
Ogni pacchetto viene confrontato con le regole della catena, dall'alto verso il basso. Alla
prima regola che corrisponde viene applicata l'azione (chiamata target):
• ACCEPT — il pacchetto viene accettato
• DROP — il pacchetto viene scartato silenziosamente
• REJECT — il pacchetto viene rifiutato con un messaggio di errore
Se nessuna regola corrisponde, si applica la policy di default della catena.
Su Debian è disponibile nei repository ufficiali:
sudo apt install iptables
Visualizzare le regole correnti
sudo iptables -L -v -n
• -L — elenca le regole
• -v — output verboso (mostra contatori, interfacce)
• -n — mostra IP e porte in formato numerico (non fa lookup DNS)
La sintassi di base
sudo iptables -A CATENA -p protocollo --dport porta -j TARGET
• -A — appende la regola in fondo alla catena (append)
• -I — inserisce la regola in cima (o in una posizione specifica)
• -p — protocollo (tcp, udp, icmp)
• --dport — porta di destinazione
• -j — azione da eseguire (jump)
Accettare le connessioni SSH (porta 22)
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
Accettare il traffico HTTP e HTTPS
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
Accettare traffico sulla loopback
Indispensabile — senza questa regola molti servizi locali smettono di funzionare:
sudo iptables -A INPUT -i lo -j ACCEPT
Accettare connessioni già stabilite
Fondamentale: senza questa regola il server non riceve le risposte alle proprie richieste
(aggiornamenti apt, query DNS, ecc.):
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
Bloccare un indirizzo IP specifico
sudo iptables -A INPUT -s 192.168.1.50 -j DROP
Permettere o bloccare il ping in entrata
# Permettere
sudo iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
# Bloccare
sudo iptables -A INPUT -p icmp --icmp-type echo-request -j DROP
Se la policy di default è già DROP, la regola di blocco è ridondante — il ping verrebbe
ignorato comunque. Diventa necessaria solo se la policy è ACCEPT e si vuole bloccare
esplicitamente il ping lasciando aperto il resto.
Impostare la policy di default a DROP
Supponiamo di avere un server nginx con le regole precedenti già configurate. Si imposta la
policy di default per bloccare tutto il resto:
sudo iptables -P INPUT DROP
Da questo momento il server accetta solo SSH, HTTP, HTTPS e le connessioni già stabilite.
Tutto il resto viene silenziosamente ignorato.
Eliminare regole
Per eliminare una regola, si usa -D con la stessa sintassi usata per aggiungerla:
sudo iptables -D INPUT -p tcp --dport 80 -j ACCEPT
Oppure si elencano le regole con i numeri di riga e si elimina per numero:
sudo iptables -L INPUT --line-numbers
sudo iptables -D INPUT 3
Svuotare tutte le regole (flush)
Durante le prove in laboratorio, per ripartire da zero:
sudo iptables -F
sudo iptables -P INPUT ACCEPT

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 6: Firewall Linux presentazione


Wolfgang Cecchin
UNITA’ FORMATIVA
Firewall: iptables, ufw
Firewall in Linux
iptables & ufw — controllo del traffico di rete
Linux Server · ITS Academy
Cos'è un firewall
Controlla il traffico di rete in entrata e in uscita sulla base di regole
Decide esplicitamente cosa è permesso — tutto il resto viene
Su Linux: il sottosistema Netfilter nel kernel gestisce il filtraggio dei
iptables e ufw sono interfacce per scrivere regole che Netfilter
Nota: nftables è il successore di iptables (Debian 10+). Su sistemi moderni iptables è un wrapper su nftables.
Tabelle e catene
Le catene (tabella filter)
traffico diretto al server
pacchetto accettato
traffico generato dal server
scartato silenziosamente
traffico in transito (router)
rifiutato con messaggio errore
Nota: Se nessuna regola corrisponde, si applica la policy di default della catena.
Installazione e visualizzazione
Visualizzare le regole
Su Debian non è sempre preinstallato:
sudo iptables -L -v -n
sudo apt install iptables
elenca tutte le regole
output verboso (contatori, interfacce)
formato numerico — no lookup DNS
Sintassi di base
sudo iptables -A CATENA -p protocollo --dport porta -j TARGET
Opzioni principali
Protocolli e porte
append — aggiunge in fondo alla catena
tcp / udp / icmp
insert — aggiunge in cima (o posizione N)
porta di destinazione
delete — elimina la regola
porta di origine
policy — imposta comportamento default
flush — elimina tutte le regole
indirizzo IP sorgente
azione: ACCEPT / DROP / REJECT
Permetti servizi
Regole essenziali (sempre necessarie)
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
# Loopback
sudo iptables -A INPUT -i lo -j ACCEPT
Scenario: server nginx
Dopo le regole sopra, imposta la policy a DROP:
sudo iptables -P INPUT DROP
Da questo momento accetta solo SSH, HTTP, HTTPS e connessioni già
# Connessioni già stabilite
sudo iptables -A INPUT -m state \
--state ESTABLISHED,RELATED -j ACCEPT
Senza queste due regole il server non risponde correttamente ai propri
servizi locali e alle risposte di rete.
Ping e blocco IP
Ping in entrata (ICMP echo-request)
Bloccare un IP e eliminare regole
# Permettere
sudo iptables -A INPUT -p icmp \
--icmp-type echo-request -j ACCEPT
# Bloccare
sudo iptables -A INPUT -p icmp \
--icmp-type echo-request -j DROP
Nota: Se la policy è già DROP, il blocco è ridondante. Serve solo se la
policy è ACCEPT.
# Bloccare un IP
sudo iptables -A INPUT -s 192.168.1.50 -j DROP
#### Eliminazione di regole precedentemente impostate ####
# Eliminare per sintassi
sudo iptables -D INPUT -p tcp --dport 80 -j ACCEPT
# Eliminare per numero di riga
sudo iptables -L INPUT --line-numbers
sudo iptables -D INPUT 3
Flush (laboratorio — ripartire da zero):
sudo iptables -F && sudo iptables -P INPUT ACCEPT

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 7: Lezione Diagnostica doc


ITS ICT Piemonte — Linux Server
Strumenti di diagnostica per sistemi Linux
Docente: Wolfgang Cecchin
1. L'approccio a strati
Quando un sistema non funziona, la tentazione è provare soluzioni a caso. L'approccio
professionale è diverso: si ragiona dal basso verso l'alto, verificando un livello alla volta.
Livello 4 — Applicazione WordPress, configurazione virtual host
Livello 3 — Servizio nginx, MariaDB, PHP-FPM, SSH
Livello 2 — Firewall iptables, policy, regole
Livello 1 — Rete interfacce, IP, routing, DNS
💡 Non ha senso indagare il livello superiore se quello inferiore è rotto. Se la rete non
funziona, il firewall è irrilevante. Se il firewall blocca tutto, il servizio non è raggiungibile.
2. Livello 1 — Diagnostica di rete
Interfacce e indirizzi IP
ip a # tutte le interfacce con IP
ip a show enp0s8 # una interfaccia specifica
ip link show # stato UP/DOWN delle interfacce
Cosa cercare: l'interfaccia è UP? Ha un indirizzo IP? L'indirizzo è quello giusto? La netmask è
ip route show # tabella di routing
ip r # forma abbreviata
Cosa cercare: c'è un default gateway? Punta all'indirizzo giusto?
ping -c 4 10.0.0.2 # raggiungibilità di un host sulla LAN
ping -c 4 8.8.8.8 # raggiungibilità di internet
traceroute 8.8.8.8 # percorso dei pacchetti
Cosa cercare: il ping risponde? Se no, il problema è locale (mittente) o remoto
(destinatario)? Traceroute mostra dove si ferma il traffico?
Configurazione persistente
cat /etc/network/interfaces # configurazione Debian
Cosa cercare: le righe auto, iface, address, netmask, gateway corrispondono a quello che
ITS ICT Piemonte — Linux Server
cat /etc/resolv.conf # server DNS configurati
cat /etc/hosts # risoluzione locale
ITS ICT Piemonte — Linux Server
3. Livello 2 — Diagnostica del firewall
Visualizzare le regole attive
sudo iptables -L -n --line-numbers # regole leggibili con numeri di riga
sudo iptables -L INPUT -n -v # solo catena INPUT, con contatori
sudo iptables-save # dump completo in formato restore
L'opzione -n è importante: senza di essa, iptables tenta di risolvere ogni IP in un nome DNS,
rallentando enormemente l'output.
Policy di default: la prima riga dice Chain INPUT (policy DROP) o (policy ACCEPT)? Con
policy DROP, tutto ciò che non è esplicitamente permesso viene scartato.
Ordine delle regole: iptables le legge dall'alto verso il basso e si ferma alla prima che
corrisponde. Una regola di DROP prima di una di ACCEPT vince.
Porte aperte: ci sono regole ACCEPT per le porte dei servizi necessari (22/2222 per SSH, 80 per
HTTP, 3306 per MariaDB)?
Traffico di ritorno: c'è una regola per ESTABLISHED,RELATED? Senza di essa, le risposte alle
connessioni in uscita vengono bloccate (es. apt update non funziona).
File di persistenza
cat /etc/iptables/rules.v4 # regole salvate (iptables-persistent)
💡 Se le regole in memoria (iptables -L) sono diverse da quelle nel file, al prossimo riavvio
si torna alla versione del file.
4. Livello 3 — Diagnostica dei servizi
Stato dei servizi
sudo systemctl status nginx # stato di nginx
sudo systemctl status mariadb # stato di MariaDB
sudo systemctl status ssh # stato di SSH
sudo systemctl status php8.2-fpm # stato di PHP-FPM
Cosa cercare: il servizio è active (running) oppure failed? Se failed, il messaggio d'errore dice
cosa è andato storto.
Porte in ascolto
sudo ss -tulnp # tutte le porte in ascolto
sudo ss -tulnp | grep :80 # solo la porta 80
sudo ss -tulnp | grep :3306 # solo la porta 3306
Questo comando è fondamentale. Mostra non solo se un servizio è in ascolto, ma anche su
quale indirizzo:
nginx ascolta su tutte le interfacce (OK)
ITS ICT Piemonte — Linux Server
Test di configurazione
MariaDB ascolta solo sulla loopback (non
raggiungibile dalla rete)
MariaDB ascolta solo sulla rete interna (corretto per il
sudo nginx -t # verifica sintassi nginx
sudo sshd -t # verifica sintassi SSH
sudo nginx -T # mostra configurazione completa nginx
Questi comandi controllano la sintassi senza toccare il servizio in esecuzione. Sono sicuri da
eseguire in qualsiasi momento.
sudo journalctl -u nginx --no-pager -n 30 # ultimi 30 log di nginx
sudo journalctl -u mariadb --no-pager -n 30 # ultimi 30 log di MariaDB
sudo journalctl -u ssh --no-pager -n 30 # ultimi 30 log di SSH

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 8: Lezione Diagnostica ppt


Strumenti di diagnostica
per sistemi Linux
Docente: Wolfgang Cecchin
L'approccio a strati
Ragionare dal basso verso l'alto, un livello alla volta.
WordPress, virtual host, wp_options
nginx, MariaDB, PHP-FPM, SSH
iptables, policy, regole
Interfacce, IP, routing, DNS
Non ha senso indagare il livello superiore se quello inferiore è rotto.
Livello 1 — Interfacce e IP
L'interfaccia è UP? Ha l'IP giusto? C'è un default gateway?
# Tutte le interfacce con IP
# Una interfaccia specifica
ip a show enp0s8
# Stato UP/DOWN
# Tabella di routing
Livello 1 — Connettività e DNS
Ping risponde? Traceroute dove si ferma? Config persistente corretta?
# Raggiungibilità LAN
ping -c 4 10.0.0.2
# Raggiungibilità internet
ping -c 4 8.8.8.8
# Percorso dei pacchetti
traceroute 8.8.8.8
# Configurazione persistente
cat /etc/network/interfaces
# DNS
cat /etc/resolv.conf
Livello 2 — Regole firewall
# Regole con numeri di riga (-n = no DNS lookup)
sudo iptables -L -n --line-numbers
# Solo catena INPUT con contatori
sudo iptables -L INPUT -n -v
# Dump completo in formato restore
sudo iptables-save
# Regole salvate (persistenza)
cat /etc/iptables/rules.v4
Livello 2 — Cosa cercare
Policy di default
Ordine delle regole
Chain INPUT (policy DROP) o (policy ACCEPT)?
Con DROP, tutto ciò che non è permesso viene
Top-to-bottom, first match wins.
Una regola DROP prima di ACCEPT vince.
Traffico di ritorno
ACCEPT per 2222 (SSH), 80 (HTTP),
3306 (MariaDB)?
Regola per ESTABLISHED,RELATED?
Senza, apt update non funziona.
Livello 3 — Stato dei servizi
active (running) o failed? I log dicono perché.
# Stato dei servizi
sudo systemctl status nginx
sudo systemctl status mariadb
sudo systemctl status ssh
sudo systemctl status php8.2-fpm
# Test sintassi (senza riavviare)
sudo nginx -T # config completa
# Log degli ultimi 30 messaggi
sudo journalctl -u nginx --no-pager -n 30
sudo journalctl -u mariadb --no-pager -n 30
Livello 3 — Porte in ascolto
Mostra non solo SE un servizio è in ascolto, ma anche su QUALE indirizzo:
nginx ascolta su tutte le interfacce
MariaDB ascolta solo su loopback
✗ Non raggiungibile dalla
MariaDB ascolta su rete interna
✓ Corretto per backend
La differenza tra "la porta è aperta sul firewall" e "il servizio è in ascolto su quell'interfaccia" è cruciale.
Livello 4 — Diagnostica applicativa
Se nginx risponde localmente ma non dall'esterno → problema firewall.
# Test connessione DB da debian3
mysql -h 10.0.0.2 -u wpuser -p
# Test web server locale
curl -I http://localhost
curl -s http://localhost | head -20
# Configurazione nginx
sudo nginx -T | grep root
sudo nginx -T | grep server_name

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 9: Linux Server 01 Installazione Debian


UNITA’ FORMATIVA
Wolfgang Cecchin
Intallazione Debian
Differenze nelle architetture:
- Server fisico;
- Virtual Machine(s);
Bare Metal vs. Virtual Machines vs. Containers
https://www.youtube.com/watch?v=TvnZTi_gaNc
https://diveintodocker.com/
Container vs. Severless
https://us.nttdata.com/en/blog/tech-blog/serverless-vs-ec2-vs-containers-a-comparativestudy
Macchine Virtuali
https://en.wikipedia.org/wiki/Virtual_machine
Alcune Virtual Machines:
• Parallels (per Mac OS)
• KVM (per Linux)
Sistema Operativo Qubes OS
https://www.qubes-os.org/
“Security by Isolation”: Qubes utilizza varie Virtual Machines Xen per creare
ambienti isolati.
Distribuzioni Unix
https://en.wikipedia.org/wiki/List_of_Unix_systems
Distribuzioni Linux
https://en.wikipedia.org/wiki/Linux_distribution
https://upload.wikimedia.org/wikipedia/commons/b/b5/Linux_Distribution_Timeline_21_
Principali famiglie di distribuzioni Linux
• Redhat (Fedora, CentOS);
• Debian (Ubuntu);
Installazione Virtual Machine VM Ware Workstation

---

## Sessione 10: Linux Server 02 Comandi Essenziali


Wolfgang Cecchin
Installazione Debian e Comandi Essenziali
Programma odierno:
- Leggere e scrivere files;
- Muoversi nelle directories;
- Creare utenti;
- Substitute User e Sudo;
Installare pacchetti
https://it.wikipedia.org/wiki/Shell_Unix
https://en.wikipedia.org/wiki/Unix_shell
Esistono vari tipi di shell:
Muoversi agevolmente con la shell:
Il tab fornisce l’autocomplete dei comandi noti;
la freccia in su serve per scorrere la history dei comandi (vedi anche il
comando “history”);
CTRL + D effettua il logout;
CTRL + C interrompe un comando;
q serve per uscire dalla modalità lettura di alcuni programmi (man);
~ : è la home directory.
$ clear # “pulisce” il terminale
Struttura dei comandi in Linux
La struttura di un comando in Linux è:
Comando + opzioni + parametri
- l = long listening form
- h = human readable
ls -lah /home =
- l = long listening form
- h = human readable
/home = della directory home
ls -lah /home = fai l’elenco del contenuto (ls) della directory home (/home),
usando la modalità estesa (long listening form), mostrando tutti i file (all), in
modo che siano comprensibile da un utente umano
$ ls -lah /home
Opzioni in forma estesa
$ ls -l --all --human-readable /home
Manuali ed help dei comandi
Creare file e reindirizzare l’input verso un file
$ touch MioFile
$ echo “ciao mondo” > mioFile
$ echo “ciao mondo” >> mioFile
$ ls > output_ls
Leggere un file
Scrivere un file
Oppure (curiosità):
(:i per scrivere
:wq per scrivere e salvare
:q! per forzare l’uscita)
Creare directories, Copiare, rinominare, cancellare un file
$ mkdir miaDir #creo una directory
$ cp source destination # copia
$ cp -R source destination # copia una directory (copia ricorsiva)
$ mv oldName newName # rinomino un file
$ rm file # cancella il file
$ rm -r directory # rimuove una directory e il suo contenuto
L’opzione -f forza (per lo più evitare di usarla).
Muoversi nel file system
$ cd # change directory
$ pwd # quale è la directory corrente?
Simboli “speciali”
. = è la directory stessa;
.. = è la directory superior;
/ = è la directory principale del sistema (la root);
~ = è la home dell’utente (~ è la tilde; su linux usare i tasti: alt gr + ì )
$ cd / # vado nella directory root del sistema
$cd - # torno alla directory precedente
$ tree -L 1 / # vedo l’alberatura del sistema
FHS Filesystem Hierarchy Standard
https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard
Attenzione nelle moderne distribuzioni alcuni directories “puntano” ad altre.
root (individuato con #): è l’amministratore del sistema
su = substitute user
sudo = “substitute user do” (“super user do”); esegue il comando per un
E’ necessario aggiungere l’utente in /etc/sudoers.d
Creare un file con il nome utente e aggiungere all’’interno:
user ALL=(ALL:ALL) ALL
• The first ALL is the users allowed to use the sudo command.
• The second ALL defines the hosts (servers) on which sudo can be
• The third ALL is the user you are running the command as.
• The last ALL defines the commands allowed.
Nota: la home di root è /root

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 11: Linux Server 03 utenti e permessi


Wolfgang Cecchin
UNITA’ FORMATIVA
Utenti e permessi
In Debian è possibile utilizzare:
# useradd
O meglio ancora:
# adduser
Per aggiungere utenti.
# useradd
# useradd -D alberto
# useradd -d /var/marco marco
# groupadd
File che gestiscono gli utenti
Il file /etc/passwd
Il file /etc/group
Il file /etc/shadow
Il file /etc/gshadow
Aggiungere un utente a un gruppo:
sudo usermod -a -G groupname username
groups utente → vedo a quali gruppi appartiene l’utente
Cambiare password di un utente
Cambiare la propria password:
Cambiare la password di un utente:
# passwd marco
Aggiungo un utente:
# useradd marco
Imposto una password per l’utente
# passwd marco
Che cosa è capitato?
Lo vedo nel file:
La cartella /home/marco e /home/alberto non è stata creata,
infatti c’è bisogno
di un parametro.
Cancello l’utente e lo ricreo:
# userdel marco
# useradd -m marco
Creare utenti senza home:
# useradd -M
Creo un secondo utente:
# useradd -m alberto
Imposto una password per l’utente
# passwd alberto
Faccio il login come Alberto.
Che shell sto usando?
$ echo "$SHELL"
Vado a vedere le home directories.
Come Marco provo a entrare nella home di Alberto e creare un
$ touch mioFile
Perché non ho i permessi:
drwxr-xr-x 2 alberto alberto 4,0K nov 13 11:17 alberto
I permessi sono organizzati in 3 gruppi:
Per ciascuno di questi gruppi viene indicato:
- Nessun permesso: -;
- Scrittura: w;
- Esecuzione: x.
La lettera “d” in prima posizione indica che si tratta di una
Per cambiare permessi:
$ chmod permissions filename
Ci sono due modi per cambiare permessi.
Modalità numerica:
Permission Type
Execute + Write
Read + Write +Execute
$ chmod 764 mioFile
- il proprietario ha tutti i permessi;
- il gruppo cui appartiene l’utente può leggere e scrivere;
- Tutti gli altri possono solo leggere.
Modalità simbolica:
Adds a permission to a file or
Removes the permission
Sets the permission and
overrides the permissions set
User Denotations
$ chmod o=rwx mioFile
Tutti gli altri possono leggere, scrivere ed eseguire.
Aggiungo i permessi di esecuzione al gruppo.
$ chmod g-r tolgo i permessi di lettura al gruppo.
Altri comandi utili:
Aggiungere un gruppo:
# groupadd mynewgroup

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 12: Linux Server 03.1 Esercizio-su-utenti-permessi


Wolfgang Cecchin
UNITA’ FORMATIVA
Esercizio su utenti e permessi
Nella home directory (eventualmente in Documenti) creare
- Per il primo file: solo l’utente proprietario può leggere, scrivere,
- Per il secondo file: solo l’utente proprietario e il gruppo ristretto
possono: leggere, scrivere, eseguire;
- Per il terzo file: solo l’utente proprietario e il gruppo users possono:
leggere, scrivere, eseguire;
- Per il quarto file: tutti possono leggere, scrivere eseguire.

---

## Sessione 13: Linux Server 03.2 Esercizio-su-utenti-permessi


Wolfgang Cecchin
UNITA’ FORMATIVA
Esercizio su utenti e permessi
- Creare un utente emilio;
- Creare un utente ignazio;
- Creare un utente ivan;
- Creare un gruppo interni;
- Creare un gruppo esterni;
ignazio e ivan al gruppo interni
emilio al gruppo esterni
ignazio vuole creare una sua cartella Documenti (se non c’è
- All’interno di Documenti creare 3 cartelle:
pvt → solo Ignazio ha accesso in lettura e scrittura;
interni → hanno accesso Ignazio e Ivan in lettura e scrittura,
Emilio non può leggere la cartella.
esterni → hanno accesso tutti, in lettura e scrittura.
All’interno di esterni creare un file
fileEmilio leggibilie e scrivibile solo da Emilio.

---

## Sessione 14: Linux Server 03.3 Esercizio-su-utenti-permessi - passaggi


Wolfgang Cecchin
UNITA’ FORMATIVA
Esercizio su utenti e permessi
1. Creare i seguenti utenti:
o marco, laura, simone, elena
2. Creare i seguenti gruppi:
fotografi, postprod, direzione
3. Assegnare gli utenti ai gruppi:
laura e simone al gruppo fotografi
o elena al gruppo postprod
o marco al gruppo direzione
o marco anche al gruppo fotografi e postprod
4. Creare la struttura directory:
5. Impostare i permessi in modalità ottale:
Proprietario Gruppo
direzione: r-x,
fotografi: rwx,
Proprietario Gruppo
direzione: r-x,
6. Creare i seguenti file e impostare i permessi:
In /home/studio/raw/ creare il file foto001.raw:
▪ Permessi: 660 (proprietario e gruppo leggono e
/home/studio/elaborati/
foto001_edit.jpg:
▪ Permessi: 640 (proprietario legge/scrive, gruppo
In /home/studio/archivio/ creare il file listino_prezzi.txt:
▪ Permessi: 600 (solo il proprietario legge e scrive)
• Accedere come simone e verificare di poter creare un file
in /home/studio/raw/
• Accedere come elena e verificare di NON poter accedere
a /home/studio/raw/
• Accedere come elena e verificare di poter modificare file
in /home/studio/elaborati/
• Accedere come laura e verificare di poter solo leggere i file
in /home/studio/elaborati/ (se aggiunta al gruppo)

---

## Sessione 15: Linux Server 03.3 Esercizio-su-utenti-permessi - soluzione


Wolfgang Cecchin
UNITA’ FORMATIVA
Esercizio su utenti e permessi
1. Creazione degli utenti
sudo adduser marco
sudo adduser laura
sudo adduser simone
sudo adduser elena
Il comando adduser chiederà interattivamente la password e le informazioni aggiuntive
(nome completo, telefono, ecc.). Per le informazioni opzionali puoi premere Invio per
2. Creazione dei gruppi
sudo addgroup fotografi
sudo addgroup postprod
sudo addgroup direzione
3. Assegnazione utenti ai gruppi
sudo usermod -aG fotografi laura
sudo usermod -aG fotografi simone
sudo usermod -aG postprod elena
sudo usermod -aG direzione marco
sudo usermod -aG fotografi marco
sudo usermod -aG postprod marco
4. Creazione della struttura directory
sudo mkdir -p /home/studio/raw
sudo mkdir -p /home/studio/elaborati
sudo mkdir -p /home/studio/archivio
5. Impostazione proprietari e gruppi delle directory
sudo chown marco:direzione /home/studio
sudo chown marco:fotografi /home/studio/raw
sudo chown marco:postprod /home/studio/elaborati
sudo chown marco:direzione /home/studio/archivio
6. Impostazione permessi in modalità ottale
sudo chmod 755 /home/studio
sudo chmod 770 /home/studio/raw
sudo chmod 770 /home/studio/elaborati
sudo chmod 750 /home/studio/archivio
7. Creazione dei file
sudo touch /home/studio/raw/foto001.raw
sudo touch /home/studio/elaborati/foto001_edit.jpg
sudo touch /home/studio/archivio/listino_prezzi.txt
Impostare proprietari dei file:
sudo chown marco:fotografi /home/studio/raw/foto001.raw
sudo chown marco:postprod /home/studio/elaborati/foto001_edit.jpg
sudo chown marco:direzione /home/studio/archivio/listino_prezzi.txt
Impostare permessi dei file:
sudo chmod 660 /home/studio/raw/foto001.raw
sudo chmod 640 /home/studio/elaborati/foto001_edit.jpg
sudo chmod 600 /home/studio/archivio/listino_prezzi.txt
Verificare la struttura creata:
ls -la /home/studio/
ls -la /home/studio/raw/
ls -la /home/studio/elaborati/
ls -la /home/studio/archivio/
Verificare i gruppi degli utenti:
Testare l'accesso come simone (può scrivere in raw):
touch /home/studio/raw/test_simone.raw
ls -la /home/studio/raw/
Testare l'accesso come elena (NON può accedere a raw):
ls /home/studio/raw/ # Dovrebbe dare "Permission denied"
touch /home/studio/elaborati/test_elena.jpg # Dovrebbe funzionare
Testare che elena non possa accedere all'archivio:
ls /home/studio/archivio/ # Dovrebbe dare "Permission denied"

---

## Sessione 16: Linux Server 03.3 Esercizio-su-utenti-permessi


Wolfgang Cecchin
UNITA’ FORMATIVA
Esercizio su utenti e permessi
Marco è il titolare di un piccolo studio fotografico. Ha tre
• Laura - fotografa senior
• Simone - fotografo junior
• Elena - addetta alla post-produzione
Lo studio ha bisogno di organizzare i file sul server Linux in base ai
I fotografi (Laura e Simone) devono poter accedere alle
• Solo la post-produzione (Elena) deve poter modificare le
• Marco deve avere accesso completo a tutto

---

## Sessione 17: Linux Server 03.4 Esercizio-su-utenti-permessi - passaggi


Wolfgang Cecchin
UNITA’ FORMATIVA
Esercizio su utenti e permessi
1. Creare i seguenti utenti:
o giulia, andrea, chiara, luca, sara
2. Creare i seguenti gruppi:
o scrittori, editing, grafica, amministrazione
3. Assegnare gli utenti ai gruppi:
o andrea e chiara al gruppo scrittori
luca al gruppo editing
luca anche al gruppo scrittori (deve
o sara al gruppo grafica
o giulia ai gruppi amministrazione, scrittori, editing,
4. Creare la struttura directory:
/home/casaeditrice/
├── manoscritti/
│ ├── copertine/
│ └── impaginazione/
└── amministrazione/
5. Impostare i permessi in modalità ottale:
Permessi ottali Risultato atteso
Giulia: rwx, tutti: r-x
giulia scrittori
ditrice/grafica
ditrice/grafica
ditrice/grafica
Giulia: rwx, scrittori:
rwx, altri: nessuno
Giulia: rwx, editing:
rwx, altri: nessuno
Giulia: rwx, grafica:
rwx, altri: nessuno
Giulia: rwx, grafica:
rwx, altri: nessuno
Giulia: rwx, grafica:
rwx, altri: nessuno
Solo Giulia: rwx
6. Creare i seguenti file e impostare i permessi:
In /home/casaeditrice/manoscritti/ creare
romanzo_capitolo1.txt:
▪ Proprietario: giulia, Gruppo: scrittori
▪ Permessi: 660
In /home/casaeditrice/bozze/ creare
romanzo_corretto.txt:
▪ Proprietario: giulia, Gruppo: editing
▪ Permessi: 660
In /home/casaeditrice/grafica/copertine/ creare
bozza_copertina.png:
▪ Proprietario: giulia, Gruppo: grafica
▪ Permessi: 660
In /home/casaeditrice/amministrazione/ creare
▪ Proprietario: giulia, Gruppo: amministrazione
▪ Permessi: 600
• Accedere come andrea e verificare di poter creare un file
in /home/casaeditrice/manoscritti/
• Accedere come luca e verificare di poter leggere i file in
/home/casaeditrice/manoscritti/
• Accedere come luca e verificare di poter scrivere in
/home/casaeditrice/bozze/
• Accedere come sara e verificare di NON poter accedere a
/home/casaeditrice/manoscritti/
• Accedere come sara e verificare di poter scrivere in
/home/casaeditrice/grafica/copertine/
• Accedere come andrea e verificare di NON poter
accedere a /home/casaeditrice/amministrazione/

---

## Sessione 18: Linux Server 03.4 Esercizio-su-utenti-permessi - soluzione


Wolfgang Cecchin
UNITA’ FORMATIVA
Esercizio su utenti e permessi
Soluzione - Comandi
1. Creazione degli utenti
sudo adduser giulia
sudo adduser andrea
sudo adduser chiara
sudo adduser luca
sudo adduser sara
Per ogni utente, adduser chiederà la password e le informazioni opzionali (premi Invio per
2. Creazione dei gruppi
sudo addgroup scrittori
sudo addgroup editing
sudo addgroup grafica
sudo addgroup amministrazione
3. Assegnazione utenti ai gruppi
sudo usermod -aG scrittori andrea
sudo usermod -aG scrittori chiara
sudo usermod -aG editing luca
sudo usermod -aG scrittori luca
sudo usermod -aG grafica sara
sudo usermod -aG amministrazione giulia
sudo usermod -aG scrittori giulia
sudo usermod -aG editing giulia
sudo usermod -aG grafica giulia
4. Creazione della struttura directory
sudo mkdir -p /home/casaeditrice/manoscritti
sudo mkdir -p /home/casaeditrice/bozze
sudo mkdir -p /home/casaeditrice/grafica/copertine
sudo mkdir -p /home/casaeditrice/grafica/impaginazione
sudo mkdir -p /home/casaeditrice/amministrazione
5. Impostazione proprietari e gruppi delle directory
sudo chown giulia:amministrazione /home/casaeditrice
sudo chown giulia:scrittori /home/casaeditrice/manoscritti
sudo chown giulia:editing /home/casaeditrice/bozze
sudo chown giulia:grafica /home/casaeditrice/grafica
sudo chown giulia:grafica /home/casaeditrice/grafica/copertine
sudo chown giulia:grafica /home/casaeditrice/grafica/impaginazione
sudo chown giulia:amministrazione /home/casaeditrice/amministrazione
6. Impostazione permessi in modalità ottale
sudo chmod 755 /home/casaeditrice
sudo chmod 770 /home/casaeditrice/manoscritti
sudo chmod 770 /home/casaeditrice/bozze
sudo chmod 770 /home/casaeditrice/grafica
sudo chmod 770 /home/casaeditrice/grafica/copertine
sudo chmod 770 /home/casaeditrice/grafica/impaginazione
sudo chmod 700 /home/casaeditrice/amministrazione
7. Creazione dei file
sudo touch /home/casaeditrice/manoscritti/romanzo_capitolo1.txt
sudo touch /home/casaeditrice/bozze/romanzo_corretto.txt
sudo touch /home/casaeditrice/grafica/copertine/bozza_copertina.png
sudo touch /home/casaeditrice/amministrazione/contratti.txt
Impostare proprietari dei file:
sudo chown giulia:scrittori /home/casaeditrice/manoscritti/romanzo_capitolo1.txt
sudo chown giulia:editing /home/casaeditrice/bozze/romanzo_corretto.txt
sudo chown giulia:grafica /home/casaeditrice/grafica/copertine/bozza_copertina.png
sudo chown giulia:amministrazione /home/casaeditrice/amministrazione/contratti.txt
Impostare permessi dei file:
sudo chmod 660 /home/casaeditrice/manoscritti/romanzo_capitolo1.txt
sudo chmod 660 /home/casaeditrice/bozze/romanzo_corretto.txt
sudo chmod 660 /home/casaeditrice/grafica/copertine/bozza_copertina.png
sudo chmod 600 /home/casaeditrice/amministrazione/contratti.txt
8. Comandi di verifica
Verificare la struttura creata:
ls -la /home/casaeditrice/
ls -la /home/casaeditrice/manoscritti/
ls -la /home/casaeditrice/bozze/
ls -la /home/casaeditrice/grafica/
ls -la /home/casaeditrice/grafica/copertine/
ls -la /home/casaeditrice/amministrazione/
Verificare i gruppi degli utenti:
Test accesso come andrea (scrittore):
touch /home/casaeditrice/manoscritti/nuovo_capitolo.txt # Deve funzionare
ls /home/casaeditrice/bozze/ # Permission denied
ls /home/casaeditrice/amministrazione/ # Permission denied
Test accesso come luca (editor):
cat /home/casaeditrice/manoscritti/romanzo_capitolo1.txt # Deve funzionare (è nel
gruppo scrittori)
touch /home/casaeditrice/bozze/nuova_correzione.txt # Deve funzionare

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 19: Linux Server 03.4 Esercizio-su-utenti-permessi


Wolfgang Cecchin
UNITA’ FORMATIVA
Esercizio su utenti e permessi
Giulia gestisce una piccola casa editrice chiamata "Pagine
Nuove". Il team è composto da:
• Andrea - scrittore
• Chiara - scrittrice
• Luca - editor/correttore di bozze
• Sara - grafica (impaginazione e copertine)
La casa editrice ha bisogno di organizzare i file sul server Linux:
• Gli scrittori (Andrea e Chiara) devono poter lavorare sui
• L'editor (Luca) deve poter leggere i manoscritti e modificare
le bozze corrette
• La grafica (Sara) deve poter accedere solo alla cartella
delle copertine e dell'impaginazione
• Giulia deve avere accesso completo a tutto, inclusi i file

---

## Sessione 20: Linux Server 04 SSH


Wolfgang Cecchin
UNITA’ FORMATIVA
SSH (Secure Shell)
SSH è un servizio (ma anche un protocollo) che consente la
comunicazione sicura via rete (sicura perché crittografata) tra un
client e un server.
Attraverso SSH un utente può inviare comandi a un computer
Precedentemente per collegarsi alle macchine si utilizzava
comunicazione tra client e server avveniva in chiaro.
stato abbandonato, perché
Approfondimenti:
https://en.wikipedia.org/wiki/Secure_Shell
Utilizziamo VM Workstation con NAT
Per evitare di avere conflitti con altre macchine (e con la rete di
ITS) utilizziamo VM Ware Workstation con NAT (“Network Address
Soluzione per Virtual Box:
Utilizzare scheda solo host, eventualmente aggiungendo una
seconda scheda.
https://www.slideshare.net/powerhan96/networking-betweenhost-and-guest-v-ms-in-virtual-box
Installiamo su Debian il server SSH
Aggiorniamo i repositories:
$ sudo apt update
$ sudo apt install openssh-server
Controlliamo di avere installato:
$ sudo systemctl status sshd
Controlliamo che sia in ascolto sulla porta 22:
$ netstat -tulpn | grep 22
Impostiamo il server SSH perché parta all’avvio:
$ sudo systemctl enable ssh
Nel caso in cui sia installato un firewall, dobbiamo consentire l’ingresso per
$ sudo ufw allow ssh
Il file di configurazione di ssh si trova all’interno di /etc
/etc/ssh/ssh_config → è il file di configurazione del client ssh del
/etc/ssh/sshd_config → è il file di configurazione del server ssh
/etc/ssh/ssh_config.d → è una directory. Vengono includi tutti i
files di configurazione del client ssh del sistema
/etc/ssh/sshd_config.d → è una directory. Vengono includi tutti i
files di configurazione del server ssh del sistema
A noi, se vogliamo modificare le configurazioni di ssh, interessa
modificare il file:
/etc/sshd_config
Individiuamo l’IP della macchina
Dalla macchina Windows (cioè la macchina host) possiamo
utilizzare un client ssh per connettersi alla macchina:
$ ssh its-user@ip-della-macchina-guest
Crittografia simmetrica
https://it.wikipedia.org/wiki/Crittografia_simmetrica
Crittografia asimmetrica
https://it.wikipedia.org/wiki/Crittografia_asimmetrica
Connessione tramite SSH
SSH utilizza crittografia simmetrica per crittografare la
connessione tra client e server. La crittografia del canale in
modalità asimmetrica sarebbe troppo onerosa (troppo lenta) a
livello di calcolo.
Tuttavia la fase di autentificazione può avvenire attraverso
crittografia asimmetrica e chiave pubblica.
Nella powershell di Windows generiamo una coppia di chiavi
pubblica/privata (non specificando nulla verrà usato l’algoritmo
Nella home dell’utente è stata creata una cartella .ssh con le
chiavi pubbliche e private.
In Debian andiamo a copiare la chiave pubblica nella cartella
Ci sono molti modi per farlo, ad esempio da Windows:
> scp .\id_rsa.pub its-user@192.168.206.128:/home/its-user
> ssh its-user@192.168.206.128
E poi nella macchina Debian:
$ cat id_rsa.pub >> ~/.ssh/authorized_keys
Il contenuto del file authorizes_keys è una lista di chiavi

---

## Sessione 21: Linux Server 05 dns hosts


Wolfgang Cecchin
DNS, file hosts
Lo scopo di assegnare dei nomi agli indirizzi IP è quello di rendere più facile la
memorizzazione per le persone. In verità, un indirizzo IP identifica un'interfaccia di rete
associata con un dispositivo come una scheda di rete. Poiché ogni macchina può avere più
schede e più interfacce per ogni scheda, un singolo computer può avere più nomi nel
sistema dei nomi di dominio.
https://debian-handbook.info/browse/it-IT/stable/sect.hostname-name-service.html
Il servizio DNS
https://it.wikipedia.org/wiki/Nome_di_dominio
https://it.wikipedia.org/wiki/Domain_Name_System
Interrogare il DNS
$ dig google.com
The most important section is the ANSWER section:
• The first column lists the name of the server that was queried
• The second column is the Time to Live, a set timeframe after which the record is
• The third column shows the class of query – in this case, “IN” stands for Internet
• The fourth column displays the type of query – in this case, “A” stands for an A
(address) record
The final column displays the IP address associated with the domain name
Tipi di record DNS - Wikipedia
A NAME = Address Name
CNAME = Canonical Name
MX = Mail Server
Associare un nome a un IP
E’ possibile associare il nome di un dominio a un server (o meglio a un IP) attraverso il
E’ possibile tuttavia informare la macchina locale dell’associazione di un nome dominio e
IP attraverso il file “hosts”.
Posizione su Linux / Mac:
Nota bene: molti file di configurazione importanti in Linux si trovano nella directory /etc
Posizione su Windows:
c:\Windows\System32\Drivers\etc\hosts
Sintassi del file hosts:
127.0.0.1 localhost
192.168.0.1 mioSito.example.com mioSito
127.0.1.1 mercoledi.local

---

## Sessione 22: Linux Server 05.01 Esercizio nome host


SOFTWARE DEVELOPER
Docente: Wolfgang Cecchin
Titolo argomento: DNS, File Host esercizio
Creare i nomi domini
tuoCognome.local
all’interno della macchina virtuale.
Connettersi alla macchina virtuale usando il nome dominio:
tuCognome.local

---

## Sessione 23: Linux Server 06 http server


Wolfgang Cecchin
UNITA’ FORMATIVA
Httpd Server: nginx, Apache
Negoziazione Client-Server e status code
https://developer.mozilla.org/en-US/docs/Learn/Serverside/First_steps/Client-Server_overview
Codici si stato
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
https://it.wikipedia.org/wiki/Codici_di_stato_HTTP
Architettura statica:
Architettura dinamica:
“Configurazione” di un webserver
• Assegniamo un nome al server;
Troviamo uno spazio per mettere i files;
• Diciamo al webserver come associare il nome ai files da servire;
• Configuriamo i log.
Installazione nginx
$ sudo apt update
$ sudo apt install nginx
Far partire, riavviare, fermare, conoscere lo stato di Nginx
$ sudo systemctl start nginx
$ sudo systemctl restart nginx
$ sudo systemctl stop nginx
$ sudo systemctl status nginx
Di default Nginx è in ascolto sulla porta 80
(di default anche Apache!).
Testare e ricaricare la configurazione di nginx:
$ sudo nginx -t
$ sudo systemctl reload nginx
Configurazione di nginx
I file di configurazione si trovano in:
La configurazione dei siti si trova in:
/etc/nginx/sites-available
Esiste una configurazione di default, quindi se io digito nel browser della mia macchina
locale un sito che ho impostato in /etc/hosts, ad esempio:
http://localhost
http://mercoledi.local
mi risponde la pagina di default di Nginx.
Creiamo una directory in cui inserire i file del sito.
/var/www/mercoledi.local
/srv/www/mercoledi.local
La configurazione del sito devo inserirla in:
/etc/nginx/sites-available
ma il sito va attivato con link simbolico in:
/etc/nginx/sites-enabled
Configurazione minima del file:
/etc/nginx/sites-available/mercoledi.local.conf
listen [::]:80;
server_name mercoledi.local;
root /var/www/mercoledi.local;
index index.html;
try_files $uri $uri/ =404;
In questo modo sto dicendo che chiamando
http://mercoledi.local
mi vengono serviti i files che si trovano nella directory:
/var/www/mercoledi.local
Attenzione! Non abbiamo ancora attivato il sito!
Configuriamo i log del web server
/var/log è la directory in cui si trovano i files di log dei principali servizi su Linux.
I log sono gestiti dal servizio (detto anche “demone”) syslogd, che tra le altre cose si
occupa anche della compressione.
Aggiungiamo i log specifici per questo sito:
listen [::]:80;
server_name mercoledi.local;
root /var/www/mercoledi.local;
index index.html;
try_files $uri $uri/ =404;
access_log /var/log/nginx/mercoledi.local.log;
error_log /var/log/nginx/mercoledi.local.error.log:
Codici di stato http
All’interno dei log sono memorizzate le risposte e gli errori del web server.
Approfondimenti sui codici di risposta http:
https://it.wikipedia.org/wiki/Codici_di_stato_HTTP
Attivazione di un sito
Attiviamo il sito.
La configurazione del sito devo inserirla in:
/etc/nginx/sites-available
ma il sito va attivato con link simbolico in:
/etc/nginx/sites-enabled
Per creare un link usiamo la sintassi:
$ sudo ln -s source nomeLink

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 24: Linux Server 06.1 http server esercizio


Wolfgang Cecchin
Esercizio sulla creazione di un sito
- Creare il dominio socrate.local
• Associare il webserver al dominio socrate.local
• Servire uno più file html
• Reindirizzare i log
- Creare il file di configurazione;
- Nel file di configurazione indicare:
o Posizione dei files;
o Posizione dei log;
- Testare la sintassi;
- Riavviare il server
- Controllare che sia tutto ok.

---

## Sessione 25: Linux Server 06.2 http server esercizio


Wolfgang Cecchin
UNITA’ FORMATIVA
Esercizio sulla creazione di un sito
moleantonelliana.local
palazzomadama.local
Creare il dominio moleantonelliana.local
Associare il webserver al dominio moleantonelliana.local
• Servire uno più file html
• Reindirizzare i log
- Creare il file di configurazione;
- Nel file di configurazione indicare:
o Posizione dei files;
o Posizione dei log;
- Testare la sintassi;
- Riavviare il server
- Controllare che sia tutto ok.

---

## Sessione 26: Linux Server 06.3 http server esercizio


Wolfgang Cecchin
UNITA’ FORMATIVA
Esercizio su utenti e permessi
- Abbiamo creato il sito:
tuoCognome.local
(se non è stato creato, è necessario crearlo);
- Abbiamo uno spazio sul server che contiene i files del sito (una
directory sul server).
Utilizzare Filezilla per scaricare / caricare i files.
Creare un menu e le pagine corrispondenti alle seguenti voci:
- Film (inserire una lista di film / serie TV preferiti);

---

## Sessione 27: Linux Server 06.4 http server esercizio


Wolfgang Cecchin
UNITA’ FORMATIVA
Esercizio sulla configurazione di un sito
- Abbiamo creato il sito:
tuoCognome.local
(se non è stato creato, è necessario crearlo);
- Abbiamo uno spazio sul server che contiene i files del sito (una
directory sul server).
Utilizzare Filezilla per scaricare / caricare i files.
Creare un menu e le pagine corrispondenti alle seguenti voci:
- Film (inserire una lista di film / serie TV preferiti);

---

## Sessione 28: Linux Server 07 mysql


Docente: Wolfgang Cecchin
Titolo argomento:
mysql (mariadb)
“Configurazione” del mysql
Installiamo MySQL;
• Configuriamo MySQL.
Installare mysql (mariadb)
MySQL e MariaDB: differenze e similitudini
1) Origine e storia
MySQL nasce nel 1995 e diventa uno dei database relazionali open source più diffusi al
mondo. Nel 2010 viene acquisito da Oracle, che ne mantiene lo sviluppo con una doppia
licenza: community (GPL) e commerciale.
MariaDB nasce nel 2009 come fork diretto di MySQL, creato dagli stessi fondatori
originali (Michael "Monty" Widenius e altri) proprio in risposta all'acquisizione da parte di
Oracle, temendo una chiusura del progetto. Il nome deriva da Maria, figlia di Widenius
(come MySQL derivava da "My", l'altra figlia).
La sintassi tra le due versioni è comune al 95%. Dalla versione 10.x di MariaDB in poi, la
compatibilità con MySQL non è più garantita al 100% — alcune funzionalità avanzate di
MySQL non esistono in MariaDB e viceversa.
Regola pratica: MariaDB è la scelta più comune nelle distribuzioni Debian/Ubuntu (è il
pacchetto installato di default con apt install mariadb-server), mentre MySQL è più
frequente in ambienti enterprise o su sistemi Red Hat/CentOS.
$ sudo apt install mariadb-server
$ sudo systemctl start mariadb
$ sudo systemctl enable mariadb
$ sudo systemctl status mariadb
Creazione utenti e creazione di un semplice database
Entrare nel mysql, utilizzando il client:
$ sudo mysql -u root -p
Per creare un datbase:
CREATE DATABASE miodatabase;
SHOW DATABASES;
USE miodatabase;
Per creare un utente per utilizzare il database:
CREATE USER 'its-usr'@'localhost' IDENTIFIED BY 'password';
Per attribuire i privilegi:
GRANT ALL PRIVILEGES ON miodatabase.* TO 'username'@'localhost';
FLUSH PRIVILEGES;
Forma deprecata:
GRANT ALL ON nomedb.* TO 'its-usr'@'localhost' IDENTIFIED BY 'password';
(creava utente privilege in un solo passaggio.
L’utente è attivo solo per localhost, cioè solo per la macchina locale.
Per cancellare un utente (revoca anche i privilegi):
DROP USER IF EXISTS 'its-usr'@'localhost';
Creare un utente che si connetta da qualsiasi IP
(sconsigliabile)
CREATE USER 'its-usr'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON miodatabase.* TO 'its-usr'@'%';
FLUSH PRIVILEGES;
Per accedere da remoto è anche necessario modificare il file:
/etc/mysql/mariadb.conf.d/50-server.cnf
Modificare la configurazione:
bind-address = 0.0.0.0
Avvertenze di sicurezza
• Non usare @'%' in produzione — preferire sempre un IP specifico o una subnet
(@'192.168.1.%')
• Non esporre la porta 3306 su Internet — usare una VPN o un tunnel SSH
Il bind su 0.0.0.0 espone il database su tutte le interfacce di rete, inclusa quella
pubblica se present
Approfondimento: Apici singoli, Backtick, Virgolette
' Apici singoli — stringhe e valori
Usati per delimitare valori letterali: stringhe, password, date.
SELECT * FROM utenti WHERE nome = 'Mario';
INSERT INTO prodotti (nome) VALUES ('Laptop');
CREATE USER 'its-usr'@'localhost' IDENTIFIED BY 'password';
` Backtick — identificatory
(Linux / Windows: Altgr + ì; oppure Windows: Alt + 96 su tastierino numerico)
Usati per delimitare nomi di oggetti del database: tabelle, colonne, database. Necessari
quando il nome:
coincide con una parola riservata di SQL
contiene spazi o caratteri speciali
-- "select" è una parola riservata: senza backtick darebbe errore
SELECT `select`, `order` FROM `my-table`;
-- Normalmente non servono, ma non fanno mai male
SELECT `nome`, `cognome` FROM `utenti`;
I backtick servono solo in casi particolari. Se i nomi delle tabelle e colonne sono normali
(niente spazi, niente parole riservate), puoi scrivere senza.
-- Questi sono equivalenti se "utenti" non è una parola riservata:
SELECT nome FROM utenti;
SELECT `nome` FROM `utenti`;

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 29: Linux Server 08 php


Docente: Wolfgang Cecchin
Titolo argomento:
“Configurazione” del php e del mysql
Installiamo il PHP;
Configuriamo Nginx per far funzionare il PHP;
(Configuriamo gli errori);
Installiamo i moduli del PHP che ci occorrono;
Utilizzando un web server PHP può essere eseguito in tre modalità: CGI, FastCGI o come
modulo dedicato del web server.
CGI è l’acronimo di Common Gateway Interface; si tratta di uno standard (RFC 3875)
utilizzato dai web server per interfacciarsi con applicazioni esterne. È stato il primo
strumento utilizzato per lo sviluppo di applicazioni web in C/C++ o Perl all’inizio degli anni
’90. Per ogni richiesta del web server su pagine dinamiche, come ad esempio quelle con
estensione .php, l’interfaccia CGI si preoccupa di eseguire l’interprete del linguaggio e di
restituire la risposta. Questo approccio consente di avere un isolamento dell’esecuzione del
codice tra web server e linguaggio interpretato ma rende il sistema inefficiente dal punto di
vista delle performance, poiché l’interfaccia è riallocata a ogni richiesta HTTP. Ormai questa
tecnologia non viene più utilizzata nelle moderne applicazioni PHP perché considerata poco
efficiente in presenza di altro traffico.
FastCGI è una tecnologia più recente, basata sullo stesso principio di funzionamento del
CGI, ma con la differenza che la comunicazione tra web server e FastCGI è gestita attraverso
socket. Un modulo FastCGI rimane in ascolto di eventuali richieste HTTP in memoria e non
deve essere rieseguito continuamente. Questa soluzione garantisce performance migliori
rispetto al CGI, soprattutto per applicazioni ad altro traffico. Ad esempio, il web server nginx
e Internet Information Service (IIS) utilizzano entrambi la modalità FastCGI per
l’esecuzione di applicazioni PHP.
Un’altra alternativa per eseguire il codice PHP in ambito web è l’utilizzo di un modulo
dedicato del web server. Questa modalità è stata, ed è tuttora, molto utilizzata con il web
server Apache grazie alla sua facilità di installazione e alle sue performance. Utilizzando un
modulo dedicato, le chiamate agli script PHP vengono gestite direttamente dal web server,
senza dover utilizzare un livello ulteriore di comunicazione, come nel caso di CGI o
FastCGI. Apache rimane a tutt’oggi il web server più utilizzato, con una quota di utilizzo
intorno al 50%. Nginx sta diventando sempre più popolare, soprattutto nei casi di
applicazioni web ad altro traffico.
Enrico Zimuel, Sviluppare in PHP 7
Installiamo il PHP
Nginx utilizza il PHP in modalità FastCGI, mentre Apache lo utilizza come modulo.
Infatti per installare il PHP con Nginx si usa il php-fpm (FastCGI Process Manager):
$sudo apt install php php-fpm
Procediamo con l’installazione del PHP_FPM.
$ sudo systemctl start php8.4-fpm
$ sudo systemctl enable php8.4-fpm
$ sudo systemctl status php8.4-fpm
Configuriamo nginx
Nel file di configurazione del nostro sito aggiungiamo:
# pass PHP scripts to FastCGI server
#
location ~ \.php$ {
include snippets/fastcgi-php.conf;
#
# # With php-fpm (or other unix sockets):
fastcgi_pass unix:/var/run/php/php8.4-fpm.sock;
# # With php-cgi (or other tcp sockets):
# fastcgi_pass 127.0.0.1:9000;
Aggiungere anche:
index index.html index.php;
Solo su macchine di sviluppo, configuriamo il PHP perché si vedano gli errori
Dove si trovano i files di configurazione del PHP?
Editiamo il file :
/etc/php/8.4/fpm/php.ini
per lo sviluppo
display_errors = On
error_reporting = E_ALL
Attenzione! In produzione devono essere:
display_errors = Off
error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT

---

## Sessione 30: Linux Server comando at


Wolfgang Cecchin
UNITA’ FORMATIVA
Il comando at serve a eseguire un comando o uno script una sola volta in un momento futuro
specifico, senza che tu debba restare loggato. Si usa quando non vuoi una schedulazione ripetitiva
come con cron.wikipedia
La forma tipica è:
Dopo aver dato il comando, scrivi i comandi da eseguire e poi chiudi con Ctrl+D. at assegna un
numero di job al task pianificato.
echo "Ciao" > /tmp/test.txt
Controllare e rimuovere job
• atq mostra i job in coda per l’utente corrente.
atrm <numero_job> rimuove un job pianificato.
• at -l è un alias comune per elencare i job, e at -r per rimuoverli.
Formati dell’orario
Puoi indicare orari semplici come 09:00, oppure parole come now + 1 hour, noon, midnight a seconda
dell’implementazione e della manpage disponibile. In alcune versioni puoi anche usare il formato
L’uso di at può essere controllato da /etc/at.allow e /etc/at.deny: se esiste at.allow, solo gli utenti lì
elencati possono usarlo. Root può sempre usarlo.man+1
Usalo per cose come:
• un backup che deve partire una volta sola.
l’invio di un file a una certa ora.
• una pulizia temporanea o un riavvio programmato.

---

## Sessione 31: Linux Server cron


Docente: Wolfgang Cecchin
Titolo argomenti:
- Archivi compressi
- Processi per il monitoring
Creazione di un archivio compresso
Comando tar (“tape archive”)
Creazione di un archivio:
$ tar cvf nomeMioArchivio.tar directory1 directory2 dirctory3 file1 file2…
Estrazione di un archivio:
$ tar xvf nomeMioArchivio.tar directory1 directory2 dirctory3 file1 file2…
Creazione di un archivio compresso - compressore gzip – opzione z :
$ tar czvf nomeMioArchivio.tar.gz directory1 directory2 dirctory3 file1
Estrazione di un archivio:
$ tar xzvf nomeMioArchivio.tar.gz directory1 directory2 dirctory3 file1
Creazione di un archivio compresso - compressore bz2 – opzione j:
$ tar cjvf nomeMioArchivio.tar.bz2 directory1 directory2 dirctory3 file1…
Estrazione di un archivio:
$ tar xjvf nomeMioArchivio.tar.bz2 directory1 directory2 dirctory3 file1…
Temporizzare (“schedulare”) comandi
Ogni utente al proprio crontab che permette di gestire lo scheduling dei programmi
https://crontab.guru/
Es (dopo aver creato una cartella du):
0 7 * * * du -shc --exclude=proc --exclude=run /* > /var/log/du/output-du-$(date '+\%Y-
Programmi per il monitoring del sistema
Processi attualmente in uso:
# top
# htop
Carico della macchina:
# uptime
Consumo della memoria:
# vmstat
# free -m
Utilizzo della CPU e IO:
# iostat
Processi attivi:
# ps aux
Trovare un processo:
# ps aux | grep nomeProcesso
Albero dei processi:
# pstree
Uccidere un processo:
# kill -1234
Uccidere un processo e i suoi figli:
# kill -9 1234
# df -h
Dimensione files:
# du – shc /miaDir
Spazio occupato nel disco:
# du -shc --exclude=proc --exclude=run /*
Quali porte sono utilizzate (installare net-tools):
# netstat -tulp

---

## Sessione 32: Linux Server esercizi ripasso meta corso


Wolfgang Cecchin
UNITA’ FORMATIVA
Attività preliminari (facciamo un po’ di pulizia) –
Rimozione degli utenti non necessari:
Backup della macchina:
- Con la macchina virtuale spenta, creare un’istantanea (snapshot) della
Rimozione utenti:
- Accendere la macchina e cancellare gli utenti non necessari (userdel);
- Lasciare solo l’utente principale (che si chiamerà its-usr o avrà il nome
che avete dato voi all’utente).
Consegna esercizio 1
(Effettuare queste operazioni utilizzando la shell).
Siete amministratori della macchina dell’azienda acme srl.
- Come amministratore della macchina creare una cartella acme che si
- Creare due gruppi:
- All’interno della cartella acme creare due cartelle:
Alla cartella dei collaboratori possono accedere tutti;
Alla cartella dei dipendenti possono accedere solo i dipendenti.
Davide Rossi nel gennaio 2022 incomincia a lavorare per l’azienda Acme srl.
- Come amministratore della macchina di Davide Rossi creare un utente
per Davide Rossi;
- Assegnare Davide al gruppo dipendenti;
- Davide all’interno della propria home crea una cartella Documenti.
All’interno della cartella Documenti crea una cartella lavoro.
All’interno della cartella lavoro, Davide crea una cartella con l’anno e
poi crea una cartella per ogni mese.
Si vuole avere la seguente struttura:
--------- lavoro
------------------ 2022
------------------------- gennaio
------------------------- febbraio
------------------------- dicembre
------------------ 2023
------------------------- gennaio
All’interno di ciascuna directory, creare un file che si chiama
- Davide a un certo punto non si ricorda più la sua password. Come
amministratore di sistema cambiargli la password.
- Verificate che Davide possa entrare in SSH con user name e password.
- Come Davide creare una coppia di chiavi dalla macchina Windows (o
Suggerimento: per evitare di sovrascrivere le chiavi, create una nuova
cartella in cui immagazzinare le nuove chiavi.
- Come amministratore di sistema predisponete l’accesso a SSH con
chiave per Davide e disabilitate l’accesso con password.
Suggerimento: Davide può scegliere una chiave privata diversa da
quella di default con cui entrare, usando il comando:
ssh-add \percorsoWindows\chiave
Nel gennaio 2023 Davide Rossi trova un altro impiego e pertanto lascia la
- Prima di cancellare l’utente di Davide, l’amministratore di sistema è
incaricato di salvare una copia della cartella lavoro nella cartella
/home/acme/dipendenti. Predisporre una cartella con il lavoro di
- Tale copia deve poter essere consultata in sola lettura e non modificata
dagli altri utenti;
- L’amministratore di sistema infine cancella l’utenza di Davide.
Nel febbraio 2023 viene assunto l’utente CarloVerdi, che è un collaboratore in
partita iva dell’azienda.
- Creare l’utente Carlo Verdi;
- Assegnare l’utente carlo al gruppo collaboratori;
- Si vuole dare all’utente carlo i permessi di amministratore della
macchina (dare la possibilità all’utente carlo di diventare
amministratore con sudo;
- Accertarsi che l’utente possa accedere in SSH tramite chiave;
Secondo indicazioni della dirigenza, l’utente carlo deve poter modificare i
files che furono di Davide:
- Lasciare una copia dei files in sola lettura nella cartella dipendenti;
- Creare una seconda copia dei files in lettura e scrittura nella cartella
collaboratori, in modo che siano modificabili da carlo e dal gruppo
- Utilizzando un client grafico SFTP (SSH File Transfer Protocol),
caricare dei files all’interno della cartella Documenti di carlo.
L’azienda acme vuole creare il proprio sito aziendale.
Incominciamo a creare l’hostname.
- Creare l’hostname acme e acme.local
- Verificare che:
o E’ possibile effettuare il ping su acme.local;
o E’ possibile entrare un SSH utilizzando il nome host acme.local;
o Che la pagina di default di nginx risponde sull’host acme.local.

---

## Sessione 33: Linux Server esercizi ripasso meta corso2


Wolfgang Cecchin
UNITA’ FORMATIVA
Esercitazioni di ripasso
Attività preliminari (facciamo un po’ di pulizia) –
Rimozione degli utenti non necessari:
Backup della macchina:
- Con la macchina virtuale spenta, creare un’istantanea (snapshot) della
Consegna esercizio 2
Federica ha 45 anni e si occupa di programmazione e sistemi in un’azienda.
Divorziata, si è poi risposata.
La sua famiglia è composta – oltre che dall’attuale compagno (o marito) - da
Paolo e Pietro di 3 e 6 anni;
Giovanni e Giacomo di 12 e 14 anni.
All’interno del proprio computer di casa ha creato un media server, in cui
memorizza i film che acquista o che scarica (legalmente con regolare utilizzo
Il server di casa che utilizza come media server è una piattaforma Linux.
Federica vorrebbe far sì che i figli di 6 e 3 anni abbiano accesso ai contenuti
riservati ai bambini di 6 anni; e che i figli di 12 e 14 abbiano accesso ai
contenuti fino a 18 anni. Infine vorrebbe che lei e l’attuale compagno (che non
è un utente tecnico e che non avrà un account nel sistema) abbiano accesso a
tutti i contenuti.
- Creare i seguenti utenti:
federica, paolo, pietro, giovanni, giacomo
- Aggiungere federica come sudo user;
- Creare i seguenti gruppi:
piccoli, grandi, adulti
- Assegnare paolo e pietro al gruppo piccoli;
- Assegnare giovanni e giacomo al gruppo grandi;
- Assegnare federica al gruppo adulti;
- Creare una directory:
/home/contenuti
- All’interno della directory /home/contenuti creare due directories:
- Fare in modo che:
o Il gruppo piccoli abbia accesso alla sola cartella piccoli;
o Il gruppo grandi abbia accesso alla cartella piccoli e alla cartella
o federica abbia accesso a tutto.
Federica vuol far sì che il figlio giovanni possa caricare i film in SFTP.
Verificare che giovanni possa entrare sul sever in SFTP e possa
caricare un file.
Federica vuole inoltre creare un blog per la famiglia.
famiglia.local e famiglia
e verificare che nginx risponda su quell’host con la pagina di default.

---

## Sessione 34: Linux Server permessi speciali


Wolfgang Cecchin
UNITA’ FORMATIVA
Permessi speciali
Lo sticky bit e un permesso speciale in Linux/Unix che si comporta in modo diverso a seconda che
venga applicato a una directory o a un file eseguibile.
1.1 Applicazione su una directory
Quando lo sticky bit e impostato su una directory, solo il proprietario del file puo eliminare o
rinominare i propri file all'interno di quella directory, anche se altri utenti hanno i permessi di
scrittura sulla directory stessa.
L'esempio classico e la directory /tmp:
drwxrwxrwt 10 root root 4096 feb 26 10:00 /tmp
La t finale nei permessi indica che lo sticky bit e attivo. Tutti gli utenti possono scrivere in /tmp, ma
nessuno puo cancellare i file degli altri.
1.2 Impostare lo sticky bit
E possibile impostare lo sticky bit con chmod in forma simbolica o numerica (il valore 1 come
quarto ottetto):
# Con chmod simbolico
chmod +t /percorso/directory
# Con chmod numerico (il 4° ottetto)
chmod 1777 /percorso/directory
1.3 Rimuovere lo sticky bit
chmod -t /percorso/directory
1.4 Verifica e simboli
Per verificare se lo sticky bit e attivo:
ls -ld /percorso/directory
Differenza tra t e T nella visualizzazione dei permessi:
t (minuscolo) — sticky bit attivo, bit di esecuzione per others attivo
• T (maiuscolo) — sticky bit attivo, bit di esecuzione per others NON attivo
1.5 Caso pratico in ambiente server
Creazione di una directory condivisa tra piu utenti del team in cui ognuno puo scrivere ma non
cancellare i file altrui:
mkdir /srv/shared
chmod 1777 /srv/shared
1.6 Nota: comportamento legacy sui file
Storicamente, lo sticky bit su un file eseguibile indicava al kernel di mantenere l'immagine del
processo in swap dopo l'esecuzione. Nei sistemi moderni questo comportamento e completamente
2. SUID Bit (Set User ID)
La s visibile su /usr/bin/passwd e il SUID bit (Set User ID). Quando impostato su un file eseguibile,
il processo gira con i privilegi del proprietario del file al momento dell'esecuzione,
indipendentemente da chi lo ha lanciato.
$ ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 68208 mag 4 2023 /usr/bin/passwd
La s al posto della x nel gruppo dei permessi del proprietario indica il SUID attivo.
2.1 Perche passwd ne ha bisogno
Le password degli utenti sono salvate nel file /etc/shadow, accessibile solo da root:
$ ls -l /etc/shadow
-rw-r----- 1 root shadow 1234 feb 26 10:00 /etc/shadow
Un utente normale non puo scrivere in /etc/shadow. Grazie al SUID, quando viene eseguito
passwd il processo ottiene temporaneamente i privilegi di root, ma il programma e scritto in modo
da permettere la modifica solo della propria password.
2.2 Impostare il SUID
# Con chmod simbolico
chmod u+s /percorso/file
# Con chmod numerico (il valore 4 come quarto ottetto)
chmod 4755 /percorso/file
2.3 Attenzione: implicazioni di sicurezza
I file con SUID sono un vettore di attacco comune in ambito di privilege escalation. Un file SUID
root mal scritto puo essere sfruttato per ottenere privilegi di root non autorizzati.
E buona pratica monitorare periodicamente quali file hanno il SUID attivo:
find / -perm -4000 -type f 2>/dev/null
3. Riepilogo dei Bit Speciali
Esegue con i privilegi del proprietario del file
Esegue con i privilegi del gruppo proprietario
Solo il proprietario puo eliminare i propri file
4. Nota sul SGID (Set Group ID)
In modo analogo al SUID, il SGID bit (valore 2) puo essere impostato su file o directory:
• Su file eseguibili: il processo gira con i privilegi del gruppo proprietario del file
• Su directory: i nuovi file creati all'interno ereditano il gruppo della directory anziche quello
del creatore — utile per cartelle condivise di gruppo
# Impostare SGID su una directory
chmod g+s /percorso/directory
chmod 2775 /percorso/directory

---

## Sessione 35: Linux Server schede di rete


Wolfgang Cecchin
UNITA’ FORMATIVA
Impostazione schede di rete
Eventualmente fare uno snapshot della macchina virtuale.
La macchina dovrebbe avere già una scheda di rete NAT.
Impostare una seconda scheda di rete “solo host”.
Fare una copia del file interfaces:
$ sudo /etc/network/interfaces /etc/network/interfaces.bk
Modificate il file interfaces:
$ sudo nano /etc/network/interfaces
Cambiare il file in modo che contenga queste righe
(non modificare l’interfaccia di loopback, cioè lo,
queste righe vanno aggiunte in fondo):
# The primary network interface
allow-hotplug enp0s3
iface enp0s3 inet dhcp
# This is an autoconfigured IPv6 interface
iface enp0s3 inet6 auto
allow-hotplug enp0s3: abilita l'interfaccia se detectata (es. USB, PCI hotplug) o all'avvio. Se
non c'è auto, non parte automaticamente al boot.manpages.debian+1
iface enp0s3 inet dhcp: IPv4 via DHCP (chiede IP/gateway/DNS al server DHCP, es.
VirtualBox NAT assegna 10.0.2.15).
iface enp0s3 inet6 auto: IPv6 automatico (SLAAC/RA, senza indirizzo statico).
$ sudo ifdown enp0s3
$ sudo ifup enp0s3

---

## Sessione 36: Linux Server tool di diagnostica


Wolfgang Cecchin
UNITA’ FORMATIVA
Tool di diagnostica
Il comando uptime fornisce in una sola riga le informazioni essenziali sullo stato del
da quanto tempo il sistema e' acceso
quanti utenti sono collegati
il load average degli ultimi 1, 5 e 15 minuti
10:32:04 up 14 days, 3:21, 2 users, load average: 0.12, 0.08, 0.05
Lettura campo per campo:
10:32:04 — ora corrente del sistema
up 14 days, 3:21 — il sistema e' acceso da 14 giorni, 3 ore e 21 minuti. Il formato e' giorni,
2 users — numero di sessioni utente aperte (terminali, SSH...)
load average: 0.12, 0.08, 0.05 — carico medio nell'ultimo 1 minuto, 5 minuti e 15 minuti
Il load average
Indica quanti processi sono in attesa di essere eseguiti dalla CPU, mediato nel
I tre valori rappresentano rispettivamente la media dell'ultimo 1 minuto, 5 minuti e
Il valore di riferimento e' il numero di core della CPU:
load average < numero di core — il sistema e' a riposo, c'e' capacita' libera
load average = 1.0 su 1 core — CPU al 100%, situazione limite ma non critica
load average > numero di core — ci sono processi che aspettano la CPU: il sistema e'
I tre valori vanno letti insieme: un picco solo nel primo (1 min) e' passeggero; se
anche il terzo (15 min) e' alto, il problema e' strutturale.
Esempio: load average 0.12, 0.08, 0.05 su un sistema a 4 core — tutto tranquillo.
Esempio: load average 7.50, 6.20, 4.10 su un sistema a 4 core — il sistema e' sotto
Quanti core ha il mio sistema?
$ lscpu | grep 'CPU(s)'
Analisi della memoria RAM: free
Il comando free mostra la memoria totale, usata, libera e la quota di swap.
L'opzione -h presenta i valori in formato leggibile, scegliendo automaticamente
l'unita' piu' adatta.
total used free shared buff/cache available
Mem: 15Gi 3,2Gi 9,1Gi 283Mi 3,0Gi 11Gi
Swap: 2,0Gi 0B 2,0Gi
Cosa significa buff/cache?
Linux usa la RAM libera come cache disco per migliorare le prestazioni.
La colonna available e' quella che conta davvero: indica quanta memoria puo'
essere usata da nuovi processi.
Messaggi del kernel: dmesg
dmesg mostra i messaggi del kernel dal momento del boot.
E' il primo strumento da consultare in caso di problemi hardware.
Rilevamento e inizializzazione dei dispositivi hardware
Errori di driver
Problemi con dischi e filesystem
Messaggi di errore della rete
$ dmesg | tail -50
$ dmesg | grep -i error
$ dmesg | grep -iE "error|fail|warn|critical"
$ dmesg | grep -i sda
$ dmesg | grep -i nvme
L'opzione -T mostra i timestamp in formato leggibile:
$ dmesg -T | grep -i error
Le parole chiave piu' importanti da cercare:
error, fail — errori generici di dispositivi o driver
I/O error, timeout — il disco non risponde o e' lento
EXT4-fs error — filesystem corrotto
Out of memory — il sistema ha esaurito la RAM
Hardware Error — errore segnalato direttamente dall'hardware
Regola pratica: un messaggio che appare una volta puo' essere normale. Se si
ripete molte volte, c'e' un problema reale.
Log di sistema: journalctl
journalctl e' il tool per consultare il journal di systemd.
Raccoglie in modo centralizzato i log di tutti i servizi e del kernel.
journalctl -b -1
Ultimi log con contesto esteso (errori recenti)
Log del boot corrente
Log del boot precedente
journalctl -b -2
journalctl -u ssh
journalctl -p err
Due boot fa (utile dopo un crash)
Log di un servizio specifico
Segue i log in tempo reale (come tail -f)
Solo messaggi di errore
journalctl -p warning
Messaggi di warning e superiori
journalctl --since '1 hour ago'
Ultimi 60 minuti
journalctl --since 'today'
# journalctl -b -1 -p err
Cosa cercare in journalctl:

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 37: Passaggi Ripasso Finale CSP


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

## Sessione 38: Soluzione Ripasso Finale CSP


ITS ICT Piemonte · Linux Server
SOLUZIONE — StudioFoto Arcobaleno
ITS ICT Piemonte
Corso Linux Server — CSP — Cloud Specialist
Ripasso finale — Linux Server
Scenario: StudioFoto Arcobaleno
Comandi, configurazioni e verifiche
Durata: 2 ore · Valutazione: 16 punti (1 per punto) — sufficienza a 10
ITS ICT Piemonte · Linux Server
SOLUZIONE — StudioFoto Arcobaleno
Nota — Soluzione di riferimento. Le password sono segnaposto; in laboratorio usare
credenziali coerenti con la policy del corso. Comandi verificati su Debian 12 (PHP 8.2).
Parte 1 — Utenti, gruppi e permessi (~25 min)
Hostname persistente
sudo hostnamectl set-hostname arcobaleno-srv
hostnamectl # Static hostname: arcobaleno-srv
Gruppo e utenti
sudo groupadd fotografi
sudo useradd -m -s /bin/bash -G fotografi anna
sudo useradd -m -s /bin/bash -G fotografi luca
sudo passwd anna && sudo passwd luca
id anna # verifica gruppi (groups=...,fotografi)
Directory condivisa + bit speciali
sudo mkdir -p /srv/scatti
sudo chgrp fotografi /srv/scatti
sudo chmod 3770 /srv/scatti # 2=SGID + 1=Sticky
ls -ld /srv/scatti # drwxrws--T root fotografi
Spiegazione bit speciali
Nota — SGID (2) sulla directory: ogni nuovo file/sottocartella eredita automaticamente il
gruppo fotografi invece del gruppo primario di chi scrive. Sticky bit (1): in una directory a
scrittura condivisa, solo il proprietario del file (oltre a root e al proprietario della directory)
può cancellarlo o rinominarlo.
Parte 2 — Rete (~15 min)
/etc/network/interfaces
# NAT - DHCP
allow-hotplug enp0s3
iface enp0s3 inet dhcp
# Solo Host - IP statico
iface enp0s8 inet static
address 192.168.56.120
netmask 255.255.255.0
Applica e verifica
sudo systemctl restart networking
ip a show enp0s8 # inet 192.168.56.120/24
ITS ICT Piemonte · Linux Server
SOLUZIONE — StudioFoto Arcobaleno
Record in /etc/hosts
echo '10.0.0.2 db.arcobaleno.local' | sudo tee -a /etc/hosts
getent hosts db.arcobaleno.local # 10.0.0.2 db.arcobaleno.local
Parte 3 — Accesso remoto SSH (~15 min)
Lato client: chiave e copia
ssh-keygen -t ed25519 -C 'its-usr@arcobaleno'
ssh-copy-id its-usr@192.168.56.120
ssh its-usr@192.168.56.120 # prova: deve entrare senza password
/etc/ssh/sshd_config
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
Test, ricarica, verifica
sudo sshd -t # test sintassi (nessun output = OK)
sudo systemctl reload ssh
sudo systemctl status ssh # active (running)
Parte 4 — Web server nginx + PHP (~20 min)
sudo apt update
sudo apt install -y nginx php-fpm # Debian 12 -> php8.2-fpm
Pagina info.php
sudo mkdir -p /var/www/arcobaleno
echo '<?php phpinfo();' | sudo tee /var/www/arcobaleno/info.php
/etc/nginx/sites-available/arcobaleno
server_name arcobaleno.local;
root /var/www/arcobaleno;
index index.php info.php;
location / { try_files $uri $uri/ =404; }
location ~ \.php$ {
include snippets/fastcgi-php.conf;
fastcgi_pass unix:/run/php/php8.2-fpm.sock;
ITS ICT Piemonte · Linux Server
SOLUZIONE — StudioFoto Arcobaleno
Abilita e verifica
sudo ln -s /etc/nginx/sites-available/arcobaleno /etc/nginx/sites-enabled/

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 39: Soluzioni Esercitazione doc


ITS ICT Piemonte — Linux Server — SOLUZIONI
Diagnostica e messa in sicurezza — Esercitazione WordPress
Docente: Wolfgang Cecchin
Panoramica dei guasti
# Macchina
IP rete interna errato
10.0.0.11 invece di 10.0.0.1
nginx root sbagliata
Applicazione Nome sito errato
Interfaccia intnet spenta
MariaDB bloccato
Policy DROP, no regola
/var/www/html invece di
/var/www/wordpress
wp_options da cambiare
enp0s8 DOWN, auto
Policy DROP, no regola
bind-address errato
127.0.0.1 invece di 10.0.0.2
ITS ICT Piemonte — Linux Server — SOLUZIONI
DEBIAN3 — DIAGNOSI E SOLUZIONI
Guasto 1 — IP rete interna errato
ip a show enp0s9
L'interfaccia mostra 10.0.0.11/24 invece di 10.0.0.1/24. Anche se il ping verso 10.0.0.2 funziona
(stessa subnet), WordPress non riesce a connettersi al database perché l'utente MariaDB
wpuser è autorizzato solo per connessioni dall'IP 10.0.0.1.
sudo nano /etc/network/interfaces
# Modificare la riga:
# address 10.0.0.11
# in:
# address 10.0.0.1
sudo systemctl restart networking
ip a show enp0s9
# Deve mostrare 10.0.0.1/24
Guasto 2 — Firewall blocca HTTP
sudo iptables -L INPUT -n --line-numbers
La policy è DROP. Le regole permettono solo loopback, ESTABLISHED/RELATED e SSH sulla
porta 2222. Non c'è nessuna regola per la porta 80.
Test di conferma:
curl -I http://localhost
# Funziona (loopback aperto)
# Ma dal browser Windows: timeout
# (la porta 80 e' bloccata dall'esterno)
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
# Salvare per la persistenza:
sudo iptables-save | sudo tee /etc/iptables/rules.v4
ITS ICT Piemonte — Linux Server — SOLUZIONI
sudo iptables -L INPUT -n --line-numbers
# Deve mostrare la regola ACCEPT per dpt:80
Guasto 3 — nginx root sbagliata
sudo nginx -T | grep root
Il virtual host punta a root /var/www/html invece di root /var/www/wordpress. nginx
risponde, ma serve la pagina di default Debian.
sudo nano /etc/nginx/sites-available/wordpress
# Modificare:
# root /var/www/html;
# in:
# root /var/www/wordpress;
sudo systemctl reload nginx
Guasto 4 — Nome sito errato (acme.local)
Il sito è configurato per rispondere al nome "wordpress". Acme richiede che risponda a
"acme.local". La modifica va fatta in due punti: nginx e il database WordPress.
Passo 1 — nginx server_name
sudo nano /etc/nginx/sites-available/wordpress
# Modificare:
# server_name wordpress;
# in:
# server_name acme.local;
sudo systemctl reload nginx
Passo 2 — URL nel database WordPress
Da debian3, connettersi al database su debian4:
mysql -h 10.0.0.2 -u wpuser -p wordpress
Aggiornare i due campi:
UPDATE wp_options SET option_value = 'http://acme.local'
ITS ICT Piemonte — Linux Server — SOLUZIONI
WHERE option_name = 'siteurl';
UPDATE wp_options SET option_value = 'http://acme.local'
WHERE option_name = 'home';
SELECT option_name, option_value FROM wp_options
WHERE option_name IN ('siteurl', 'home');

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 40: Soluzioni Esercitazione presentazione


Diagnostica e messa in sicurezza
Esercitazione WordPress
Docente: Wolfgang Cecchin
Panoramica dei guasti
#
IP rete interna errato
10.0.0.11 → 10.0.0.1
No regola porta 80
nginx root sbagliata
/var/www/html → /wordpress
Nome sito errato
server_name + wp_options
Interfaccia spenta
MariaDB bloccato
No regola porta 3306
bind-address errato
127.0.0.1 → 10.0.0.2
Frontend — Diagnosi e soluzioni
debian3 — Guasto 1
IP rete interna errato
ip a show enp0s9
sudo nano /etc/network/interfaces
# Mostra 10.0.0.11/24
# Dovrebbe essere 10.0.0.1/24
# Il ping verso 10.0.0.2 funziona
# (stessa subnet) ma WordPress
# non si collega al DB: wpuser
# autorizzato solo per 10.0.0.1
# Cambiare:
# address 10.0.0.11
# in:
# address 10.0.0.1
sudo systemctl restart networking
# Verifica:
ip a show enp0s9
Subdolo: ping OK ma connessione DB fallisce — lo studente deve collegare IP e permessi MySQL.
debian3 — Guasto 2
Firewall blocca HTTP
sudo iptables -L INPUT -n --line-numbers
# Policy: DROP
# Regole: lo, ESTABLISHED, SSH:2222
# Manca: porta 80
# Conferma:
curl -I http://localhost # OK
# Browser Windows: timeout
sudo iptables -A INPUT \
-p tcp --dport 80 -j ACCEPT
# Salvare:
sudo iptables-save | \
sudo tee /etc/iptables/rules.v4
# Verifica:
sudo iptables -L INPUT -n \
SSH funziona → lo studente pensa che la rete sia OK. Deve capire che il blocco è solo su HTTP.
debian3 — Guasto 3
nginx root sbagliata
sudo nginx -T | grep root
# Mostra: root /var/www/html
# Dovrebbe: root /var/www/wordpress
# nginx risponde ma serve la
# pagina di default Debian
# invece di WordPress
sudo nano /etc/nginx/\
sites-available/wordpress
# Cambiare:
# root /var/www/html;
# in:
# root /var/www/wordpress;
sudo systemctl reload nginx
Distinguere tra 'il servizio risponde' e 'il servizio risponde con il contenuto giusto'.
debian3 — Guasto 4
Nome sito errato → acme.local
Due modifiche necessarie: nginx + database WordPress
PASSO 1 — nginx server_name
PASSO 2 — URL nel database
# In sites-available/wordpress
# Cambiare:
# server_name wordpress;
# in:
# server_name acme.local;
sudo systemctl reload nginx

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 41: glances doc


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

## Sessione 42: glances


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

## Sessione 43: lezione find


Wolfgang Cecchin
UNITA’ FORMATIVA
Il comando find è lo strumento principale di Linux per cercare file e directory nel filesystem in base
a criteri molto diversi: nome, tipo, dimensione, proprietario, permessi, data di modifica e altro
A differenza di ls, che elenca i contenuti di una directory, find esplora ricorsivamente l'albero del
filesystem a partire da un punto di inizio specificato.
1. Sintassi generale
$ find [percorso] [criteri] [azione]
Punto di partenza della ricerca. Si usa / per tutto il filesystem, . per la
directory corrente, /etc per limitare la ricerca
Uno o più filtri: nome, tipo, proprietario, permessi, dimensione, data...
Cosa fare con i file trovati. Se omessa, il default è -print (stampa il
percorso). Si può usare -exec per eseguire comandi
2. Criteri di ricerca principali
2.1 Nome del file (-name, -iname)
find / -name "hosts"
Cerca un file chiamato esattamente "hosts"
find / -name "hosts*"
Cerca file il cui nome inizia con "hosts" (* = qualsiasi
find / -name "*.conf"
Cerca tutti i file con estensione .conf
find / -iname "hosts"
Come -name, ma case-insensitive (HOSTS, Hosts,
📘 NOTA: Il carattere * è un glob (wildcard), non un'espressione regolare. Deve essere
racchiuso tra virgolette per evitare che la shell lo espanda prima di passarlo a find.
2.2 Tipo di file (-type)
2.3 Proprietario (-user, -group)
L'opzione -user filtra i file appartenenti a un utente specifico:
$ find / -user linda
Trova tutti i file nel filesystem il cui proprietario è l'utente linda.
$ find /home -group sviluppo -type f
Trova tutti i file regolari in /home appartenenti al gruppo sviluppo.
2.4 Dimensione (-size)
L'opzione -size accetta un valore con unità e un prefisso che indica il confronto:
find / -size +2G
+ = maggiore di 2 GiB
find / -size -100M
- = minore di 100 MiB
find / -size 4k
find / -type f -
Esattamente 4 KiB (raro in pratica)
Solo file regolari con dimensione superiore a 100 MiB
2.5 Data di modifica (-mtime, -mmin)
find /etc -mtime -1
File modificati nelle ultime 24 ore
find /etc -mtime +7
File non modificati da più di 7 giorni
find /tmp -mmin -30
File modificati negli ultimi 30 minuti
3. Ricerca per permessi (-perm)
L'opzione -perm permette di cercare file in base ai loro permessi in notazione ottale. Esistono tre
formati con significati distinti:
3.1 Tre formati di -perm a confronto
find . -perm 755
find . -perm -111
find . -perm /4000
Corrispondenza esatta: il file deve avere
esattamente quei permessi e nessun altro
Tutti i bit devono essere presenti, ma il file
può averne anche altri (sottoinsieme)
Almeno uno dei bit indicati deve essere
presente (OR logico)
3.2 I permessi speciali: SUID, SGID, Sticky bit
I bit speciali si specificano come quarta cifra ottale (la più significativa). Sono fondamentali per la
sicurezza del sistema.
Su file eseguibile: viene eseguito con i permessi del
proprietario del file (es. passwd esegue come root)
Su file: esegue con i permessi del gruppo. Su directory: i
nuovi file ereditano il gruppo della directory
Su directory (es. /tmp): solo il proprietario può eliminare o
rinominare i propri file, anche se la directory è scrivibile
3.3 Esempi pratici con -perm
find / -perm /4000
find / -perm /2000
File con il bit SUID attivo (formato /)
File con il bit SGID attivo
find / -type d -perm /1000
Directory con sticky bit attivo
find / -perm /7000
find . -perm -111

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 44: lezione grep sed awk


DOCENTE: _______________________________
UNITÀ FORMATIVA: Strumenti Linux per la gestione dei file
ARGOMENTO: Ricerca nei file: grep, sed, awk
Linux mette a disposizione tre strumenti fondamentali per cercare e manipolare il testo nei file:
• grep — cerca righe che contengono un pattern
sed — trasforma il testo (cerca e sostituisce)
• awk — elabora testo strutturato a colonne
I file di esempio utilizzati in questa lezione si trovano nella cartella ~/esercizi/.
1. grep — Cercare nei file
Il comando grep (Global Regular Expression Print) cerca le righe di un file che corrispondono a un
pattern e le stampa sullo standard output. Non modifica mai i file.
$ grep [opzioni] "pattern" file
Opzioni principali
Ricerca case-insensitive (maiuscole = minuscole)
Ricerca ricorsiva in tutte le sottodirectory
Mostra il numero di riga prima di ogni risultato
Inverte la ricerca: mostra le righe che NON corrispondono
Mostra solo i nomi dei file con almeno una corrispondenza
Conta il numero di righe corrispondenti
Abilita le espressioni regolari estese (ERE)
Cerca solo parole intere (word match)
Ricerca semplice
$ grep "ERROR" sistema.log
Cerca tutte le righe che contengono la parola ERROR nel file sistema.log.
Ricerca case-insensitive con numero di riga
$ grep -n -i "error" sistema.log
Trova sia ERROR sia error sia Error, mostrando il numero di riga per ogni risultato.
Ricerca invertita
$ grep -v "^#" webserver.conf
Mostra tutte le righe del file di configurazione che non iniziano con # (cioè esclude i commenti).
Ricerca ricorsiva
$ grep -rl "password" /etc/
Cerca la parola password in tutti i file dentro /etc/ e mostra solo i nomi dei file trovati.
Uso di espressioni regolari
$ grep -E "ERROR|WARNING" sistema.log
Cerca le righe che contengono ERROR oppure WARNING (operatore | = OR).
NOTA: grep non modifica mai i file. Serve solo per trovare e visualizzare righe. Per
modificare il testo si usa sed.
Ancore nelle espressioni regolari
grep "^root" utenti.txt
Righe che iniziano con "root"
grep "bash$" utenti.txt
Righe che terminano con "bash"
grep "er.ore" file.txt
Il punto sostituisce un qualsiasi carattere
2. sed — Modificare il testo
Il comando sed (Stream EDitor) legge un file riga per riga, applica una trasformazione e stampa il
risultato. Di default non modifica il file originale: l'output va sullo standard output. Con l'opzione -i
la modifica avviene direttamente sul file.
$ sed [opzioni] 'comando' file
Il comando di sostituzione: s///
Il comando più usato di sed è s (substitute):
$ sed 's/testo_vecchio/testo_nuovo/flag' file
Sostituisce solo la prima occorrenza per ogni riga
Sostituisce tutte le occorrenze nella riga (global)
Sostituzione case-insensitive
Sostituisce solo la seconda occorrenza
Sostituzione semplice (output su terminale)
$ sed 's/WARNING/ATTENZIONE/' sistema.log
Mostra il file con WARNING sostituito da ATTENZIONE nella prima occorrenza di ogni riga. Il file originale
non viene modificato.
Sostituzione con modifica in-place
$ sed -i 's/porta = 80/porta = 8080/' webserver.conf
Modifica direttamente il file webserver.conf, cambiando il valore della porta.
ATTENZIONE: L'opzione -i modifica il file in modo irreversibile. Prima di usarla, verificare il
risultato senza -i per accertarsi che la sostituzione sia corretta.
Copia di sicurezza automatica con -i
$ sed -i.bak 's/WARNING/ATTENZIONE/g' sistema.log
Crea automaticamente una copia di backup sistema.log.bak prima di modificare il file.
Eliminare righe che corrispondono a un pattern
$ sed '/^#/d' webserver.conf
Il comando d (delete) elimina le righe che corrispondono al pattern. In questo caso elimina tutti i
commenti dall'output.
Visualizzare solo un intervallo di righe
$ sed -n '1,5p' sistema.log
Con -n (no print) e il comando p mostra solo le righe dalla 1 alla 5.
Workflow consigliato: grep + sed
Passo 1 — verificare cosa verrà modificato con grep:
$ grep "livello = WARNING" webserver.conf
Passo 2 — eseguire la sostituzione con sed (senza -i prima):

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 45: networking linux doc


Networking in Linux
Lezione — Linux Server | ITS Academy
1. Introduzione
La configurazione di rete è una competenza fondamentale per chi amministra un server
Linux. In questa lezione vedremo come funziona lo stack di rete, come configurare
interfacce, routing e risoluzione dei nomi, e come diagnosticare problemi di connettività.
2. Concetti fondamentali
Interfacce di rete
Un'interfaccia di rete è il punto di contatto tra il sistema operativo e la rete fisica (o virtuale).
In Linux le interfacce seguono una nomenclatura predittiva (introdotta con systemd/udev):
eth0, enp3s0, ens33
virbr0, docker0
Ethernet fisica
Loopback (127.0.0.1)
Bridge virtuali
Il loopback è un'interfaccia speciale: tutto il traffico inviato a 127.0.0.1 rimane all'interno della
macchina stessa. È usato da servizi che comunicano localmente (es. PHP → MySQL).
Il modello TCP/IP a strati
HTTP, FTP, SSH, DNS
TCP (affidabile), UDP (veloce)
IP, ICMP, routing
Ethernet, ARP, MAC address
3. Comandi essenziali
Networking in Linux — ITS Academy
Comando ip — visualizzare le interfacce
Il comando ip sostituisce il vecchio ifconfig ed è lo strumento principale per la gestione della
rete in Linux moderno.
ip addr show # mostra tutte le interfacce
ip addr show enp3s0 # mostra solo una interfaccia
ip addr add 192.168.1.100/24 dev enp3s0 # assegna IP temporaneo
ip addr del 192.168.1.100/24 dev enp3s0 # rimuove un IP
ip link set enp3s0 up # attiva interfaccia
ip link set enp3s0 down # disattiva interfaccia
Il routing determina come i pacchetti raggiungono la destinazione. La tabella di routing dice
al kernel quale gateway usare per raggiungere una determinata rete.
ip route show # mostra la tabella di routing
ip route add default via 192.168.1.1 # default gateway
ip route add 10.0.0.0/8 via 192.168.1.254 # rotta statica
ip route del default via 192.168.1.1 # elimina rotta
Tutte le modifiche con ip sono temporanee: vengono perse al riavvio del sistema.
4. Configurazione persistente
Debian — /etc/network/interfaces
iface enp3s0 inet static
address 192.168.1.100
netmask 255.255.255.0
gateway 192.168.1.1
dns-nameservers 8.8.8.8 1.1.1.1
systemctl restart networking
Ubuntu moderno — Netplan (/etc/netplan/*.yaml)
addresses: [192.168.1.100/24]
via: 192.168.1.1
addresses: [8.8.8.8, 1.1.1.1]
Best practice: come per MariaDB, preferire i file dedicati nelle directory .d/ invece di
modificare i file di configurazione base.
Networking in Linux — ITS Academy
5. Risoluzione dei nomi (DNS)
Quando si esegue ping google.com il sistema deve tradurre il nome in un indirizzo IP.
Questo processo si chiama risoluzione DNS.
Ordine di risoluzione — /etc/nsswitch.conf
hosts: files dns
Il sistema controlla prima /etc/hosts, poi interroga il server DNS configurato.
/etc/hosts — mappature statiche
127.0.0.1 localhost
192.168.1.10 server-web.lan server-web
192.168.1.20 db.lan
Utile in laboratorio per simulare un DNS senza installarne uno.
/etc/resolv.conf — server DNS
nameserver 8.8.8.8
nameserver 1.1.1.1
Attenzione: su sistemi con systemd-resolved, questo file è un symlink gestito
automaticamente.
6. Diagnostica di rete
La sequenza logica per diagnosticare un problema di connettività parte sempre dal livello più
• Passo 1 — L'interfaccia è attiva?
ip addr show # verificare la presenza di UP e di un indirizzo IP
• Passo 2 — Raggiungo il gateway?
ping -c 4 192.168.1.1
• Passo 3 — Raggiungo Internet per IP?
ping -c 4 8.8.8.8
• Passo 4 — Il DNS funziona?

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 46: networking linux


Wolfgang Cecchin
UNITA’ FORMATIVA
Configurazione, diagnostica e gestione della rete
Linux Server | ITS Academy
1. Concetti fondamentali — stack TCP/IP e interfacce
2. Il comando ip — visualizzare e configurare
3. Routing e tabella di instradamento
4. Configurazione persistente — interfaces e Netplan
5. Risoluzione dei nomi — DNS, /etc/hosts, /etc/resolv.conf
6. Diagnostica — ping, traceroute, ss, tcpdump
7. Porte e servizi comuni
8. Esercizio pratico — Studio Fotografico Bianchi
Networking in Linux — ITS Academy
2. Concetti fondamentali — Stack TCP/IP
HTTP · FTP · SSH · DNS
TCP (affidabile) · UDP (veloce)
IP · ICMP · Routing
Ethernet · ARP · MAC
Networking in Linux — ITS Academy
Interfacce di rete — nomenclatura predittiva
Ethernet fisica
virbr0 / docker0
Loopback — 127.0.0.1 (locale)
Bridge virtuale
⚑ Il loopback è usato da servizi che comunicano localmente — es. PHP → MySQL (127.0.0.1:3306)
Networking in Linux — ITS Academy
3. Il comando ip — operazioni principali
Sostituisce il vecchio ifconfig — strumento principale in Linux moderno
Modificare (temporaneo)
ip addr add 192.168.1.10/24 dev enp3s0
ip addr del 192.168.1.10/24 dev enp3s0
ip link set enp3s0 up
ip link set enp3s0 down
ip addr show enp3s0
ip route add default via 192.168.1.1
ip route add 10.0.0.0/8 via 192.168.1.254
ip route del default via 192.168.1.1
Tutte le modifiche con ip sono temporanee — perse al riavvio!
Networking in Linux — ITS Academy
4. Configurazione persistente
Debian — /etc/network/interfaces
Ubuntu — Netplan /etc/netplan/*.yaml
iface enp3s0 inet static
address 192.168.1.100
netmask 255.255.255.0
gateway 192.168.1.1
dns-nameservers 8.8.8.8
addresses: [192.168.1.100/24]
via: 192.168.1.1
systemctl restart networking
Best practice: usare file dedicati nelle directory .d/ — non modificare i file di configurazione base (come per MariaDB)
Networking in Linux — ITS Academy
5. Risoluzione dei nomi (DNS)
(ping google.com)
/etc/nsswitch.conf
ordine: files → dns
mappature locali
/etc/resolv.conf
/etc/resolv.conf
127.0.0.1 localhost
192.168.1.10 server-web.lan
192.168.1.20 db.lan
nameserver 8.8.8.8
nameserver 1.1.1.1
Con systemd-resolved: /etc/resolv.conf è un symlink gestito automaticamente — modificarlo direttamente potrebbe non avere effetto.
Networking in Linux — ITS Academy
6. Diagnostica di rete — sequenza logica
Interfaccia attiva?
Raggiungo il gateway?
ping -c 4 192.168.1.1
Internet raggiungibile (per IP)?
ping -c 4 8.8.8.8
dig google.com / nslookup google.com
Altri strumenti:
traceroute / tracepath | ss -tuln / ss -tulnp | tcpdump -i enp3s0
Networking in Linux — ITS Academy
7. Porte e servizi comuni
ss -tulnp # mostra porte in ascolto con nome del processo
MySQL / MariaDB
Networking in Linux — ITS Academy

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 47: panoramica guasti


Panoramica dei guasti
#
IP rete interna errato
10.0.0.11 → 10.0.0.1
No regola porta 80
nginx root sbagliata
/var/www/html → /wordpress
Nome sito errato
server_name + wp_options
Interfaccia spenta
MariaDB bloccato
No regola porta 3306
bind-address errato
127.0.0.1 → 10.0.0.2

---

## Sessione 48: presentazione grep sed find


ITS ICT — Linux Server
grep, sed, find
Ricerca e manipolazione di file e testo in Linux
$ grep -rn "error"
/var/log/ 2>/dev/null
$ sed -i 's/old/new/g'
$ find / -perm /4000 \
-type f 2>/dev/null
$ find /etc -name '*.conf'
| xargs grep '127.0.0.1'
Modifica il testo
Cerca nel filesystem
In questa lezione
Cerca righe che contengono un
Opzioni: -i -r -n -v -l -c -E
Ancore: ^ $ e regex estese
Non modifica mai i file
Modifica il testo riga per riga
Comando s/vecchio/nuovo/g
Eliminare righe con /pattern/d
Modifica in-place con -i
Cerca per nome, tipo, proprietario
Filtra per dimensione e data
Permessi: tre formati di -perm
Esegue azioni con -exec
grep — Cercare nei file
Ancore nelle espressioni regolari
$ grep [opzioni] "pattern" file
Non modifica mai i file — solo cerca e mostra.
Opzioni principali
Case-insensitive (MAIUSCOLE = minuscole)
Ricorsiva nelle sottodirectory
Mostra il numero di riga
Inverte: righe che NON corrispondono
Solo nomi file con corrispondenze
Conta le righe corrispondenti
Abilita regex estese (ERE)
Stampa solo la parte corrispondente
Riga che inizia con root
Riga che finisce con bash
Qualsiasi carattere singolo
OR logico (richiede -E)
grep -E "err|warn"
grep — Esempi pratici
Trova ERROR nel log
Righe non vuote e non commentate
$ grep "ERROR" sistema.log
$ grep -v "^#" webserver.conf | grep -v "^$"
Cerca ERROR o WARNING (OR)
Conta i login falliti
$ grep -E "ERROR|WARNING" sistema.log
$ grep -c "Failed password" sistema.log
Con numero di riga, case-insensitive
File che contengono password (ricorsivo)
$ grep -ni "error" sistema.log
$ grep -rl "password" /etc/
Righe che NON sono commenti
Estrai tutti gli IP dal log
$ grep -v "^#" webserver.conf
$ grep -oE "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" sistema.log
sed — Modificare il testo
$ sed [opzioni] 'comando' file
Il comando di sostituzione s/vecchio/nuovo/flag
$ sed 's/vecchio/nuovo/flag' file
Sostituisce la prima occorrenza per riga
Tutte le occorrenze nella riga (global)
Case-insensitive
Solo la seconda occorrenza
Opzione -i (in-place)
Senza -i → output su stdout, file intatto
Con -i → modifica diretta del file
$ sed 's/old/new/' file.txt
$ sed -i 's/old/new/g' file.txt
ATTENZIONE: -i modifica il file in modo irreversibile. Prima di usarla, verificare il risultato senza -i. Per creare una copia di backup automatica: sed -
i.bak 's/old/new/g' file
sed — Esempi pratici e workflow consigliato
Sostituire WARNING con ERROR (solo output)
Eliminare le righe vuote
$ sed 's/WARNING/ERROR/' webserver.conf
$ sed '/^$/d' file.txt

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 49: shell avanzata doc


Wolfgang Cecchin
Reindirizzamento, processi e operatori
1. File descriptor e reindirizzamento
Cos'è un file descriptor
In Linux, tutto è un file: file di testo, directory, dispositivi hardware, socket di rete, la tastiera,
lo schermo. Il kernel gestisce tutto tramite la stessa astrazione.
Quando un processo vuole comunicare con qualcosa — leggere dalla tastiera, scrivere sullo
schermo, aprire un file — non lo fa direttamente. Chiede al kernel di aprire un canale, e il
kernel gli restituisce un numero intero che rappresenta quel canale. Quel numero è il file
descriptor (fd).
Puoi immaginarlo come il numero di un tavolo al ristorante: il cameriere (kernel) sa a quale
tavolo portare il cibo, tu (il processo) usi solo il numero — non ti preoccupi di dove si trova
fisicamente il tavolo.
processo → "voglio scrivere sul canale 1" → kernel → schermo
processo → "voglio scrivere sul canale 1" → kernel → file.txt ← dopo
reindirizzamento
Il processo scrive sempre sullo stesso numero. È il kernel che decide dove quel numero
I tre canali aperti automaticamente
Ogni processo, nel momento in cui viene avviato, riceve già tre file descriptor aperti, ereditati
Collegato a (default)
stdout e stderr puntano entrambi al terminale, ma sono canali separati. Questo è
fondamentale: permette di mandare l'output normale da una parte e gli errori da un'altra,
senza mescolarli.
Perché si chiama "descriptor" e non "file"
Il file descriptor non è il file — è solo un indice nella tabella dei file aperti del processo. Ogni
processo ha la propria tabella. Modificare dove punta l'fd 1 di un processo non cambia nulla
per gli altri processi.
Il reindirizzamento (>, 2>, &>) non fa altro che cambiare la destinazione di questi indici prima
che il processo parta. Il processo non sa nulla di questo: continua a scrivere su 1 e 2 come
Reindirizzamento di stdout (1)
# Salva l'elenco dei file di configurazione su file
ls -l /etc > elenco.txt
# Aggiunge in coda invece di sovrascrivere
ls -l /var/www >> elenco.txt
# Equivalente esplicito con fd 1
ls -l /etc 1> elenco.txt
# Caso pratico: salvare il risultato di una query MySQL su file
mysql -u root -p fotodb -e "SELECT * FROM clienti;" > clienti.txt
Reindirizzamento di stderr (2)
# find genera errori su directory senza permessi — li separiamo
find / -name "*.conf" > risultati.txt 2> errori.log
# Cerca file PHP ignorando silenziosamente le directory protette
find /var/www -name "*.php" 2> /dev/null
# grep: solo i match su stdout, eventuali errori su file separato
grep -r "password" /etc 2> /tmp/grep_errori.log
Reindirizzare entrambi con 2>&1
La sintassi si legge pezzo per pezzo:
│ │ │└─ il numero del file descriptor 1 (stdout)
│ │ └── & significa "questo è un fd, non un nome file"
│ └───── operatore di reindirizzamento
└──────── il file descriptor 2 (stderr)
Traduzione letterale: "punta fd 2 verso lo stesso posto dove punta fd 1".
Il & davanti all'1 è necessario per disambiguare: senza, 2>1 significherebbe "scrivi stderr su
un file chiamato letteralmente 1".
Perché l'ordine conta
La shell legge il reindirizzamento da sinistra a destra. 2>&1 significa "copia la destinazione
attuale di fd 1" — non "tieni fd 2 sempre sincronizzato con fd 1".
# CORRETTO: prima sposta stdout su file, poi aggancia stderr a stdout
find / -name "*.conf" > tutto.log 2>&1
# passo 1 — dopo > tutto.log: fd1 → tutto.log, fd2 → terminale
# passo 2 — dopo 2>&1: fd1 → tutto.log, fd2 → tutto.log ✓
# SBAGLIATO: 2>&1 viene letto prima, quando stdout punta ancora al terminale
find / -name "*.conf" 2>&1 > tutto.log
# passo 1 — dopo 2>&1: fd1 → terminale, fd2 → terminale ← copia fd1
# passo 2 — dopo > tutto.log: fd1 → tutto.log, fd2 → terminale ✗ stderr
rimane sul terminale
# Sintassi moderna equivalente (solo bash)
find / -name "*.conf" &> tutto.log
# Sintassi classica (funziona su sh, dash, bash — preferibile negli script)
find / -name "*.conf" > tutto.log 2>&1
# Backup MySQL: output e errori nello stesso log
mysqldump -u root -p fotodb > /var/log/backup.log 2>&1
# Aggiornamento pacchetti silenzioso, tutto su log
apt-get upgrade > /var/log/upgrade.log 2>&1
# Esecuzione silenziosa — scarta tutto
apt-get update &> /dev/null
Reindirizzamento di stdin (0)
# MySQL legge il dump da file invece che dalla tastiera
mysql -u root -p fotodb < dump.sql
# Invia il contenuto di un file come corpo di una mail

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 50: shell avanzata


Wolfgang Cecchin
UNITA’ FORMATIVA
Reindirizzamento, processi e operatori
ITS Academy — Linux Server
Cos'è un file descriptor
In Linux tutto è un file:
tastiera, schermo, rete, dispositivi
Un processo non comunica direttamente
Chiede al kernel di aprire un canale →
riceve un numero intero: il fd
Il reindirizzamento cambia dove
punta quel numero, non il processo
I tre file descriptor standard
stdout e stderr puntano entrambi al terminale, ma sono canali separati — questo permette di
separare output normale ed errori.
Reindirizzamento: stdout e stderr
# sovrascrive
ls -l /etc > elenco.txt
# aggiunge in coda
ls -l /var/www >> elenco.txt
# equivalente esplicito
ls -l /etc 1> elenco.txt
# separa errori dall'output
find / -name '*.conf' \
> risultati.txt 2> errori.log
# scarta gli errori
find /var/www -name '*.php' \
# grep: errori su file separato
grep -r 'password' /etc \
2> /tmp/errori.log
> sovrascrive >> aggiunge 2> stderr /dev/null cestino
Reindirizzare entrambi: 2>&1
"Punta fd 2 verso lo stesso posto dove punta fd 1"
Senza & davanti all'1: il comando 2>1 scriverebbe stderr su un file chiamato
letteralmente "1"
# Backup MySQL: tutto nello
mysqldump -u root -p fotodb \
> /var/log/backup.log 2>&1
# Scarta tutto (silenzioso)
apt-get update &> /dev/null
# &> equivale a > ... 2>&1
# ma funziona solo in bash
2>&1 — l'ordine conta
La shell legge il reindirizzamento da sinistra a destra.
find / -name '*.conf' > tutto.log 2>&1
find / -name '*.conf' 2>&1 > tutto.log
# passo 1 — > tutto.log:
# fd1 → tutto.log
# fd2 → terminale
# passo 2 — 2>&1:
# fd2 → tutto.log ✓
# passo 1 — 2>&1:
# fd2 → terminale ← copia fd1 ora!
# passo 2 — > tutto.log:
# fd1 → tutto.log
# fd2 → terminale ✗
Regola: prima sposta stdout con > poi aggancia stderr con 2>&1
Sintassi moderna (solo bash): find / -name '*.conf' &> tutto.log
stdin (fd 0) e /dev/null
stdin (fd 0) — leggere da file
/dev/null — il cestino
# MySQL legge da file
# invece che dalla tastiera
mysql -u root -p fotodb < dump.sql
# Invia file come corpo mail
mail -s 'Report' \
admin@studio.it \
< /var/log/backup.log
# Scarta solo stdout
apt-get update > /dev/null
# Scarta solo stderr
find / -name '*.conf' 2> /dev/null
# Scarta tutto
apt-get update &> /dev/null
Tutto quello che viene scritto in /dev/null scompare — nessun output, nessun errore visibile.
Operatori di controllo
Sempre in sequenza
Il secondo comando gira sempre,
indipendentemente dall'esito del primo.
apt-get update ; apt-get upgrade

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 51: soluzioni find


Soluzioni — find
Es. 1 Cercare in tutto il filesystem un file di nome resolv.conf, sopprimendo gli errori.
$ find / -name "resolv.conf" 2>/dev/null
La ricerca parte dalla radice /. Il reindirizzamento 2>/dev/null scarta i messaggi "Permission
denied" su stderr, lasciando l'output pulito.
Es. 2 Trovare tutti i file con estensione .log nella directory /var/log.
$ find /var/log -name "*.log"
Il pattern *.log usa il glob * per qualsiasi prefisso. Le virgolette impediscono alla shell di
espandere il glob prima di passarlo a find.
Es. 3 Trovare tutte le directory che si chiamano backup a partire da /home.
$ find /home -type d -name "backup"
-type d limita la ricerca alle sole directory, escludendo file con lo stesso nome.
Es. 4 Trovare i file di proprietà del tuo utente in /tmp.
$ find /tmp -user $(whoami)
La sostituzione di comando $(whoami) inserisce automaticamente il nome dell'utente corrente.
In alternativa si può scrivere il nome esplicitamente: find /tmp -user mario.
Ricerca per dimensione e data
Es. 5 Trovare tutti i file regolari di dimensione superiore a 100 MiB nel filesystem.
$ find / -type f -size +100M 2>/dev/null
-type f esclude directory e link. +100M significa strettamente maggiore di 100 MiB. 2>/dev/null
sopprime gli errori di accesso negato.
Es. 6 Trovare i file in /etc modificati nelle ultime 24 ore.
$ find /etc -mtime -1
Il valore -1 con -mtime significa «modificati da meno di 1 giorno», ovvero nelle ultime 24 ore. Per
ricerche più precise al minuto si può usare -mmin -60 (ultima ora).
Es. 7 Trovare tutti i file nel sistema con il bit SUID attivo.
$ find / -type f -perm /4000 2>/dev/null
Il formato /4000 (slash) significa «almeno uno dei bit indicati è presente»: qui il bit SUID (4000). -
type f esclude le directory. 2>/dev/null rimuove i messaggi di accesso negato.
⚠️ Sicurezza: I file SUID di proprietà di root vengono eseguiti con privilegi di
amministratore. Censirli periodicamente è una buona pratica di hardening.
Es. 8 Trovare le directory con lo sticky bit attivo (come /tmp).
$ find / -type d -perm /1000 2>/dev/null
Lo sticky bit su una directory (1000) impedisce agli utenti di eliminare i file altrui anche se hanno
il permesso di scrittura sulla directory, come accade in /tmp.
Es. 9 Trovare tutti i file con almeno uno dei permessi speciali attivi (SUID, SGID, Sticky).
$ find / -perm /7000 2>/dev/null
Il valore 7000 è la somma dei tre bit speciali: SUID (4000) + SGID (2000) + Sticky (1000). Con il
formato / basta che sia attivo almeno uno dei tre.
Es. 10 Trovare i file scrivibili da "others" in /home (potenziale rischio sicurezza).
$ find /home -type f -perm -002
Il formato -002 (trattino) significa «il bit 002 deve essere presente»: permesso di scrittura per
others. Un file scrivibile da chiunque in /home è spesso un errore di configurazione da
Azioni e pipeline
Es. 11 Trovare i file *.conf in /etc modificati negli ultimi 7 giorni e visualizzarli con ls -lh.
$ find /etc -name "*.conf" -mtime -7 -exec ls -lh {} \;
Il {} viene sostituito dal percorso di ogni file trovato. Il \; termina il comando -exec: il backslash
previene l'interpretazione del ; da parte della shell.
Es. 12 Cercare in /etc/ tutti i file che contengono la stringa 127.0.0.1 usando find + xargs grep.
$ find /etc/ -name '*' -type f | xargs grep "127.0.0.1"
find produce la lista dei file; xargs la passa a grep come argomenti. È equivalente a grep -r
"127.0.0.1" /etc/ ma il -type f di find garantisce di passare solo file regolari, evitando errori su
directory e link.
💡 Nomi con spazi: Se i percorsi possono contenere spazi, usare la variante sicura: find
/etc/ -type f -print0 | xargs -0 grep "127.0.0.1"
Es. 13 Trovare tutti i file di proprietà dell'utente mario e copiarli in /root/backup_mario/.
$ find / -user mario -type f -exec cp {} /root/backup_mario/ \; 2>/dev/null
Per ogni file trovato viene eseguito cp file /root/backup_mario/. La directory di destinazione
deve esistere prima di lanciare il comando: mkdir -p /root/backup_mario/.
Es. 14 (avanzato) Trovare file chiamati student nel filesystem, escludendo /proc e /tmp,
sopprimendo gli errori.
$ find / -name "student" -type f ! -path '*/proc/*' ! -path '*/tmp/*' 2>/dev/null
Il ! è l'operatore NOT: esclude i percorsi che corrispondono al pattern. */proc/* e */tmp/*
escludono qualsiasi path che contenga quelle directory. È buona pratica escludere /proc e
/sys nelle ricerche di sistema perché sono filesystem virtuali, non contengono file reali e
generano molti falsi risultati.

---

## Sessione 52: soluzioni grep sed awk


Soluzioni — grep, sed, awk
File di riferimento: sistema.log | utenti.txt | webserver.conf | vendite.csv
Es. 1 Mostrare tutte le righe di sistema.log che contengono la parola ERROR.
$ grep "ERROR" sistema.log
Es. 2 Mostrare le righe di sistema.log che contengono ERROR oppure WARNING.
$ grep -E "ERROR|WARNING" sistema.log
-E abilita le espressioni regolari estese; | è l'operatore OR.
Es. 3 Contare quante volte appare "Failed password" nel file di log.
$ grep -c "Failed password" sistema.log
-c stampa il conteggio delle righe corrispondenti, non le righe stesse.
Es. 4 In utenti.txt mostrare solo gli utenti la cui shell è /bin/bash.
$ grep "/bin/bash$" utenti.txt
Il $ ancora il pattern alla fine della riga: esclude eventuali righe che contengono /bin/bash nel
mezzo del testo.
Es. 5 In webserver.conf mostrare tutte le righe non vuote e non commentate.
$ grep -v "^#" webserver.conf | grep -v "^$"
Prima pipeline: esclude le righe che iniziano con #. Seconda: esclude le righe vuote (^$ = inizio
riga immediatamente seguita da fine riga).
Es. 6 In webserver.conf, sostituire WARNING con ERROR solo a video.
$ sed 's/WARNING/ERROR/' webserver.conf
Senza -i l'output va sullo stdout; il file originale non viene modificato.
Es. 7 In webserver.conf, eliminare dall'output le righe di commento.
$ sed '/^#/d' webserver.conf
Il comando d (delete) elimina le righe che corrispondono al pattern. Anche qui senza -i:
nessuna modifica al file.
Es. 8 In sistema.log, sostituire server01 con webserver.lan e salvare in un nuovo file.
$ sed 's/server01/webserver.lan/g' sistema.log > sistema_mod.log
Il flag g sostituisce tutte le occorrenze per riga. Il reindirizzamento > salva l'output in
sistema_mod.log senza toccare l'originale.
Es. 9 Da utenti.txt, estrarre nome utente (campo 1) e home directory (campo 6).
$ awk -F: '{print $1, $6}' utenti.txt
-F: imposta i due punti come separatore di campo.
Es. 10 Da vendite.csv, mostrare le righe della categoria "obiettivi" con prodotto e prezzo unitario.
$ awk -F, '$3 == "obiettivi" {print $2, $5}' vendite.csv
$3 è la categoria, $2 il prodotto, $5 il prezzo unitario.
Es. 11 Da vendite.csv, calcolare il totale delle vendite per ogni venditore.
$ awk -F, 'NR>1 {totale[$7] += $6} END {for (v in totale) print v, totale[v]}'
NR>1 salta la riga di intestazione. $7 è il venditore, $6 il totale della vendita. L'array associativo
totale[] accumula la somma per ciascun venditore; il blocco END stampa i risultati a fine
Es. 12 (avanzato) Da sistema.log, estrarre tutti gli IP e contare quante volte appare ciascuno.
$ grep -oE "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" sistema.log | sort | uniq -c | sort -rn
-o stampa solo la parte corrispondente (non l'intera riga). -E abilita le regex estese per il pattern
dell'IP. sort | uniq -c conta le occorrenze; sort -rn ordina per frequenza decrescente.
💡 Soluzione alternativa con solo awk:
$ awk 'match($0,/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/) {ip=substr($0,RSTART,RLENGTH);
c[ip]++} END {for (ip in c) print c[ip], ip}' sistema.log | sort -rn

---

## Sessione 53: wordpress due macchine doc


WordPress su Architettura a Due
Guida pratica per ITS Academy — Linux Server
1. Architettura dell'esercitazione
L'obiettivo è mettere in rete due macchine virtuali Debian in modo che:
• debian1 esponga WordPress su nginx, accessibile dall'esterno
• debian2 ospiti MariaDB, raggiungibile solo da debian1 tramite rete interna
• L'accesso SSH a debian2 avvenga esclusivamente passando per debian1
1.1 Schema di rete
Solo Host (SSH da
IP Rete Interna
2. Preparazione delle macchine virtuali in VirtualBox
2.1 Clonare la macchina di base
Partendo da una macchina Debian già configurata (debian1), clonare la VM in VirtualBox per
ottenere debian2. Durante il clone, scegliere di rigenerare i MAC address.
⚠️ Nota: Se il MAC address non viene rigenerato automaticamente, farlo manualmente
dalle impostazioni di ogni scheda di rete: Impostazioni → Rete → Impostazioni avanzate →
2.2 Configurazione NIC in VirtualBox
• NIC 1: NAT (tenere per apt)
• NIC 2: Rete interna → nome: intnet
• NIC 2: Solo Host (accesso SSH dall'host)
• NIC 3: Rete interna → nome: intnet (aggiungere una terza scheda)
3. Configurazione hostname su debian2
Dopo il clone, cambiare il nome della macchina su debian2:
echo "debian2" | sudo tee /etc/hostname
sudo sed -i 's/debian1/debian2/' /etc/hosts
sudo hostnamectl set-hostname debian2
4. Configurazione della rete interna (intnet)
4.1 Verificare le interfacce disponibili
Rete interna intnet
Rete interna intnet
4.2 Configurare IP statico su debian1
Aprire /etc/network/interfaces e aggiungere:
# Internal network interface (intnet)
# Static IP for private communication with debian2
iface enp0s9 inet static
address 10.0.0.1
netmask 255.255.255.0
Attivare l'interfaccia:
sudo ip addr add 10.0.0.1/24 dev enp0s9
4.3 Configurare IP statico su debian2
Aprire /etc/network/interfaces e aggiungere:
# Internal network interface (intnet)
# Static IP for private communication with debian1
iface enp0s8 inet static
address 10.0.0.2
netmask 255.255.255.0
Attivare l'interfaccia:
sudo ip addr add 10.0.0.2/24 dev enp0s8
4.4 Verificare la connettività
ping -c 4 10.0.0.2
⚠️ Nota: Usare sempre sudo con i comandi ip addr add, altrimenti il comando viene
ignorato silenziosamente.
5. Configurazione MariaDB su debian2
5.1 Installazione
sudo apt update && sudo apt install mariadb-server -y
5.2 Accesso iniziale
5.3 Sicurezza di base
-- Remove anonymous users
DELETE FROM mysql.user WHERE User='';
-- Disallow root login remotely
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost',
'127.0.0.1', '::1');
-- Remove test database
DROP DATABASE IF EXISTS test;
-- Apply changes
FLUSH PRIVILEGES;
5.4 Creazione database e utente WordPress
-- Create the WordPress database
CREATE DATABASE wordpress CHARACTER SET utf8mb4 COLLATE
utf8mb4_unicode_ci;
-- Create a dedicated user for WordPress
-- Access is restricted to debian1's IP on the internal network
CREATE USER 'wpuser'@'10.0.0.1' IDENTIFIED BY 'its2026';
-- Grant full privileges on the WordPress database only
GRANT ALL PRIVILEGES ON wordpress.* TO 'wpuser'@'10.0.0.1';
-- Apply changes
FLUSH PRIVILEGES;
5.5 Configurazione bind-address
Aprire il file di configurazione:
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 54: wordpress due macchine


WordPress su Architettura
Guida pratica — Linux Server
Obiettivo dell'esercitazione
• Mettere in rete due macchine Debian in VirtualBox
debian1 → frontend: nginx + WordPress (accessibile dall'esterno)
debian2 → backend: MariaDB (accessibile SOLO da debian1 via rete interna)
Accesso SSH a debian2 solo tramite debian1 (ProxyJump)
Scenario realistico: separazione frontend/backend come in produzione
Architettura e configurazione VirtualBox
Configurazione schede di rete (NIC)
Rete interna intnet →
Rete interna intnet →
Clone VM e cambio hostname
Cambiare hostname su debian2:
Clonare debian1 in VirtualBox per ottenere debian2
• Durante il clone: rigenerare i MAC address (o farlo manualmente dopo)
• → echo "debian2" | sudo tee /etc/hostname
• → sudo sed -i 's/debian1/debian2/' /etc/hosts
• → sudo hostnamectl set-hostname debian2
Il clone condivide il MAC address originale: rigenerarlo per evitare conflitti DHCP
Configurazione rete interna (intnet)
Interfacce di rete rilevate
Rete interna intnet
Rete interna intnet
Configurazione /etc/network/interfaces
# --- debian1: aggiungere in fondo ---
# Internal network interface (intnet)
# Static IP for private communication with debian2
iface enp0s9 inet static
address 10.0.0.1
netmask 255.255.255.0
# --- debian2: aggiungere in fondo ---
# Internal network interface (intnet)
# Static IP for private communication with debian1
iface enp0s8 inet static
address 10.0.0.2
netmask 255.255.255.0
Attivare le interfacce e testare
# Attivare su debian1 (usare SEMPRE sudo)
sudo ip addr add 10.0.0.1/24 dev enp0s9
# Attivare su debian2
sudo ip addr add 10.0.0.2/24 dev enp0s8
# Verificare la connettività (da debian1)
ping -c 4 10.0.0.2
# Output atteso: 0% packet loss
Configurazione MariaDB su debian2
Installazione e sicurezza di base
# Installazione
sudo apt update && sudo apt install mariadb-server -y
# Accesso
-- Remove anonymous users
DELETE FROM mysql.user WHERE User='';
-- Disallow root login remotely
DELETE FROM mysql.user WHERE User='root'
AND Host NOT IN ('localhost', '127.0.0.1', '::1');
DROP DATABASE IF EXISTS test;
FLUSH PRIVILEGES;
Creazione database e utente WordPress
-- Create the WordPress database
CREATE DATABASE wordpress
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Create user restricted to debian1's IP only
CREATE USER 'wpuser'@'10.0.0.1' IDENTIFIED BY 'its2026';
-- Grant privileges only on wordpress DB
GRANT ALL PRIVILEGES ON wordpress.* TO 'wpuser'@'10.0.0.1';
FLUSH PRIVILEGES;
Configurazione bind-address in 50-server.cnf
# File: /etc/mysql/mariadb.conf.d/50-server.cnf
# bind-address: IP on which MariaDB listens
# This is debian2's IP on the internal network
# NOTE: NOT the client IP — that's controlled by user privileges
bind-address = 10.0.0.2
# Riavviare il servizio
sudo systemctl restart mariadb
# Verificare
sudo ss -tlnp | grep 3306
# Output atteso: LISTEN ... 10.0.0.2:3306
Installazione WordPress su debian1
Installazione nginx e PHP-FPM
# Installare nginx e PHP (NON usare 'php' generico:

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 55: URL nel database WordPress


URL nel database WordPress
Da debian3, connettersi al database su debian4:
mysql -h 10.0.0.2 -u wpuser -p WordPress
Aggiornare i due campi:
UPDATE wp_options SET option_value = 'http://acme.local'
WHERE option_name = 'siteurl';
UPDATE wp_options SET option_value = 'http://acme.local'
WHERE option_name = 'home';
SELECT option_name, option_value FROM wp_options
WHERE option_name IN ('siteurl', 'home');
# Entrambi devono mostrare http://acme.local
Nota: senza questo passaggio, WordPress continua a generare link e redirect verso il vecchio nome. Lo studente che corregge solo nginx ma non il database vedrà il sito caricarsi in modo anomalo.

---

## Sessione 56: risoluzione problema rete Debian


# risoluzione problema rete Debian 3
# tira su l'interfaccia a mano con l'IP tipico di VirtualBox NAT:
sudo ip link set enp0s3 up
sudo ip addr add 10.0.2.15/24 dev enp0s3
sudo ip route add default via 10.0.2.2
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
# verifica:
ping -c 2 8.8.8.8
# risoluzione permanente (basta reinstallare il client dhcp):
sudo apt install isc-dhcp-client -y
sudo systemctl restart networking


---
*Totale: 56 sessioni generate il 02/07/2026*