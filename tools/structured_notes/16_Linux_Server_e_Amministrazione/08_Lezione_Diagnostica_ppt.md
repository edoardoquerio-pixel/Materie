# Lezione Diagnostica ppt

## Panoramica
Ragionare dal basso verso l'alto, un livello alla volta.

## Argomenti trattati
Linux, Reti, Configurazione, API REST, Database

---
## Appunti

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
*Fonte: 999_Lezione_Diagnostica_ppt.md*
