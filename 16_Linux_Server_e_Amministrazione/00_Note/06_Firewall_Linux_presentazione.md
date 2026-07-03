# Firewall Linux presentazione

**File:** `Firewall Linux presentazione.pdf`
**Tipo:** `.pdf`
**Dimensione:** 464.3 KB
**Ultima modifica:** 02/07/2026 09:27

---

DOCENTE Wolfgang Cecchin
UNITA’ FORMATIVA Linux Server
ARGOMENTO Firewall: iptables, ufw

Firewall in Linux
iptables & ufw — controllo del traffico di rete
Linux Server  ·  ITS Academy

Cos'è un firewall
• Controlla il traffico di rete in entrata e in uscita sulla base di regole
• Decide esplicitamente cosa è permesso — tutto il resto viene 
bloccato
• Su Linux: il sottosistema Netfilter nel kernel gestisce il filtraggio dei 
pacchetti
• iptables e ufw sono interfacce per scrivere regole che Netfilter 
applica
KERNEL
Netfilter
iptables
ufw
Nota: nftables è il successore di iptables (Debian 10+). Su sistemi moderni iptables è un wrapper su nftables.

Parte 1
iptables

Tabelle e catene
Le catene (tabella filter) I target
INPUT traffico diretto al server
OUTPUT traffico generato dal server
FORWARD traffico in transito (router)
ACCEPT pacchetto accettato
DROP scartato silenziosamente
REJECT rifiutato con messaggio errore
Nota: Se nessuna regola corrisponde, si applica la policy di default della catena.

Installazione e visualizzazione
Installazione
Su Debian non è sempre preinstallato:
sudo apt install iptables
Visualizzare le regole
sudo iptables -L -v -n
-L elenca tutte le regole
-v output verboso (contatori, interfacce)
-n formato numerico — no lookup DNS

Sintassi di base
sudo iptables -A CATENA -p protocollo --dport porta -j TARGET
Opzioni principali Protocolli e porte
-A append — aggiunge in fondo alla catena
-I insert — aggiunge in cima (o posizione N)
-D delete — elimina la regola
-P policy — imposta comportamento default
-F flush — elimina tutte le regole
-p tcp / udp / icmp
--dport porta di destinazione
--sport porta di origine
-s indirizzo IP sorgente
-j azione: ACCEPT / DROP / REJECT

Regole comuni
Permetti servizi
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
Regole essenziali (sempre necessarie)
# Loopback
sudo iptables -A INPUT -i lo -j ACCEPT
# Connessioni già stabilite
sudo iptables -A INPUT -m state \
--state ESTABLISHED,RELATED -j ACCEPT
Senza queste due regole il server non risponde correttamente ai propri 
servizi locali e alle risposte di rete.
Scenario: server nginx
Dopo le regole sopra, imposta la policy a DROP:
sudo iptables -P INPUT DROP
Da questo momento accetta solo SSH, HTTP, HTTPS e connessioni già 
stabilite.

Ping e blocco IP
Ping in entrata (ICMP echo-request)
# Permettere
sudo iptables -A INPUT -p icmp \
--icmp-type echo-request -j ACCEPT
# Bloccare
sudo iptables -A INPUT -p icmp \
--icmp-type echo-request -j DROP
Nota: Se la policy è già DROP, il blocco è ridondante. Serve solo se la 
policy è ACCEPT.
Bloccare un IP e eliminare regole
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

File di regole e persistenza
Formato file /etc/iptables.rules
*filter
:INPUT DROP
:FORWARD DROP
:OUTPUT ACCEPT
-A INPUT -i lo -s 127.0.0.1 -d 127.0.0.1 -j 
ACCEPT
-A INPUT -m state --state ESTABLISHED,RELATED -j 
ACCEPT
-A INPUT -p icmp --icmp-type echo-request -j 
ACCEPT
COMMIT
Caricare e rendere persistenti le regole
Caricare il file:
sudo iptables-restore < /etc/iptables.rules
Equivalente a digitare ogni regola a mano — più rapido e riproducibile.
Persistenza al riavvio:
sudo apt install iptables-persistent
sudo netfilter-persistent save
• Regole salvate in /etc/iptables/rules.v4 (IPv4) e rules.v6 (IPv6)
• Caricate automaticamente a ogni avvio

Parte 2
ufw

Uncomplicated Firewall — ufw
Frontend semplificato per iptables
• Scrive regole iptables in automatico — non serve gestirle a mano
• Si lavora con concetti diretti: abilita questa porta, blocca questo IP
• La persistenza è automatica (a differenza di iptables)
Installazione e stato
sudo apt install ufw
sudo ufw status
sudo ufw status numbered
sudo ufw status verbose
Abilitare e disabilitare
sudo ufw enable
sudo ufw disable
sudo ufw reset
Attenzione: Prima di ufw enable su un server remoto, aggiungere sempre la 
regola per SSH.

Regole ufw
Permettere porte e servizi
sudo ufw allow 22/tcp
sudo ufw allow ssh      # per nome
sudo ufw allow http
sudo ufw allow https
# Profilo applicazione (nginx, OpenSSH...)
sudo ufw allow 'Nginx Full'
sudo ufw app list        # profili disponibili
Blocco e restrizioni avanzate
# Bloccare un IP
sudo ufw deny from 192.168.1.50
# Solo da una subnet (es. MySQL interno)
sudo ufw allow from 192.168.10.0/24 \
to any port 3306
# Su interfaccia specifica
sudo ufw allow in on eth0 to any port 80
Nota: Scenario tipico: database MySQL accessibile solo dalla rete interna 192.168.10.0/24.

Policy, logging ed eliminare regole
Policy di default
sudo ufw default deny incoming
sudo ufw default allow outgoing
Nega tutto in entrata, apre solo le porte necessarie. Traffico in uscita 
libero.
Eliminare regole
sudo ufw status numbered
sudo ufw delete 3
sudo ufw delete allow 80/tcp
Logging
sudo ufw logging on
# livelli: low / medium / high / full
• Log in /var/log/ufw.log
• Leggibile anche con: sudo journalctl | grep UFW
Profili applicazione
Alcuni pacchetti installano profili predefiniti in 
/etc/ufw/applications.d/ — es. Nginx Full permette sia la porta 80 
che la 443 con un unico comando.

iptables vs ufw — quando usare quale
iptables ufw
Controllo Granulare, completo Semplificato
Curva di apprendimento Ripida Bassa
Uso tipico Server avanzati, script, router Server applicativi standard
Persistenza Manuale (iptables-persistent) Automatica
Leggibilità regole Bassa Alta
In ambito professionale, iptables per controllo fine (NAT, port forwarding, firewall di rete). ufw per server applicativi standard.
