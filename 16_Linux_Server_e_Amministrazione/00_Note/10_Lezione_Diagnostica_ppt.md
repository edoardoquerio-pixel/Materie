# Lezione Diagnostica ppt

**File:** `Lezione Diagnostica ppt.pdf`
**Tipo:** `.pdf`
**Dimensione:** 170.5 KB
**Ultima modifica:** 02/07/2026 09:22

---

LEZIONE
Strumenti di diagnostica
per sistemi Linux
Docente: Wolfgang Cecchin

L'approccio a strati
Ragionare dal basso verso l'alto, un livello alla volta.
4 Applicazione WordPress, virtual host, wp_options
3 Servizio nginx, MariaDB, PHP-FPM, SSH
2 Firewall iptables, policy, regole
1 Rete Interfacce, IP, routing, DNS
Non ha senso indagare il livello superiore se quello inferiore è rotto.

Livello 1 — Interfacce e IP
L'interfaccia è UP? Ha l'IP giusto? C'è un default gateway?
# Tutte le interfacce con IP
ip a
# Una interfaccia specifica
ip a show enp0s8
# Stato UP/DOWN
ip link show
# Tabella di routing
ip route show

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
cat /etc/hosts

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
Chain INPUT (policy DROP) o (policy ACCEPT)?
Con DROP, tutto ciò che non è permesso viene 
scartato.
Ordine delle regole
Top-to-bottom, first match wins.
Una regola DROP prima di ACCEPT vince.
Porte aperte
ACCEPT per 2222 (SSH), 80 (HTTP),
3306 (MariaDB)?
Traffico di ritorno
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
sudo nginx -t
sudo sshd -t
sudo nginx -T              # config completa
# Log degli ultimi 30 messaggi
sudo journalctl -u nginx --no-pager -n 30
sudo journalctl -u mariadb --no-pager -n 30

Livello 3 — Porte in ascolto
sudo ss -tulnp
Mostra non solo SE un servizio è in ascolto, ma anche su QUALE indirizzo:
Output Significato
0.0.0.0:80 nginx ascolta su tutte le interfacce ✓ OK
127.0.0.1:3306 MariaDB ascolta solo su loopback ✗ Non raggiungibile dalla 
rete
10.0.0.2:3306 MariaDB ascolta su rete interna ✓ Corretto per backend
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
sudo nginx -T | grep php
# Contenuto directory WordPress
ls -la /var/www/wordpress/

Livello 4 — URL di WordPress nel database
WordPress salva il proprio indirizzo nella tabella wp_options. Se nginx risponde ma WordPress fa 
redirect, il problema è qui:
mysql -h 10.0.0.2 -u wpuser -p wordpress
SELECT option_name, option_value
FROM wp_options
WHERE option_name IN ('siteurl', 'home');
siteurl e home devono contenere l'URL corretto (es. http://acme.local).
Se contengono un nome diverso → redirect e link sbagliati.

Buone pratiche di troubleshooting
Cambiare una cosa alla volta
Dopo ogni modifica, verificare. Cambiare tre cose insieme non insegna quale fosse il problema.
Documentare prima, agire poi
Un cat o un iptables -L prima dell'intervento permette di tornare indietro.
Leggere gli errori
Connection refused ≠ Connection timed out.
Il primo: servizio non in ascolto.
Il secondo: firewall blocca.

Il comando tee
sudo iptables-save | sudo tee /etc/iptables/rules.v4
tee legge dallo stdin e scrive su un file E sullo stdout — come un raccordo a T idraulico.
iptables-save tee → stdout
↓ file
/etc/iptables/rules.v4

Riepilogo comandi
Obiettivo Comando
Interfacce e IP ip a
Routing ip route show
Connettività ping / traceroute
Regole firewall iptables -L -n --line-numbers
Stato servizi systemctl status <servizio>
Porte in ascolto ss -tulnp
Test sintassi nginx nginx -t / nginx -T
Log servizi journalctl -u <servizio> -n 30
Test DB remoto mysql -h IP -u utente -p
URL WordPress SELECT ... FROM wp_options
Salvare iptables iptables-save | sudo tee ...
