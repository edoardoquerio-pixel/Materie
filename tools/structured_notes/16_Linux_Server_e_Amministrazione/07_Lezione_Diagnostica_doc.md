# Lezione Diagnostica doc

## Panoramica
ITS ICT Piemonte — Linux Server

## Argomenti trattati
Linux, Configurazione, Reti, API REST, Database

---
## Appunti

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
*Fonte: 999_Lezione_Diagnostica_doc.md*
