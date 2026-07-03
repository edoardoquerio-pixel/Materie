# Firewall Linux presentazione

## Panoramica
iptables & ufw — controllo del traffico di rete

## Argomenti trattati
Linux, Reti, API REST, Installazione, Git

---
## Appunti

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
*Fonte: 999_Firewall_Linux_presentazione.md*
