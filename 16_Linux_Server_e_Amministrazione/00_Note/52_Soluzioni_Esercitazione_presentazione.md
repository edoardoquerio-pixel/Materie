# Soluzioni Esercitazione presentazione

**File:** `Soluzioni Esercitazione presentazione.pdf`
**Tipo:** `.pdf`
**Dimensione:** 153.9 KB
**Ultima modifica:** 02/07/2026 09:22

---

SOLUZIONI
Diagnostica e messa in sicurezza
Esercitazione WordPress
Docente: Wolfgang Cecchin

Panoramica dei guasti
# Macchina Livello Guasto Causa
1 debian3 Rete IP rete interna errato 10.0.0.11 → 10.0.0.1
2 debian3 Firewall HTTP bloccato No regola porta 80
3 debian3 Servizio nginx root sbagliata /var/www/html → /wordpress
4 debian3 Applicazione Nome sito errato server_name + wp_options
5 debian4 Rete Interfaccia spenta enp0s8 DOWN
6 debian4 Firewall MariaDB bloccato No regola porta 3306
7 debian4 Servizio bind-address errato 127.0.0.1 → 10.0.0.2

debian3
Frontend — Diagnosi e soluzioni

debian3 — Guasto 1 Rete
IP rete interna errato
DIAGNOSI
ip a show enp0s9
# Mostra 10.0.0.11/24
# Dovrebbe essere 10.0.0.1/24
# Il ping verso 10.0.0.2 funziona
# (stessa subnet) ma WordPress
# non si collega al DB: wpuser
# autorizzato solo per 10.0.0.1
SOLUZIONE
sudo nano /etc/network/interfaces
# Cambiare:
#  address 10.0.0.11
# in:
#  address 10.0.0.1
sudo systemctl restart networking
# Verifica:
ip a show enp0s9
Subdolo: ping OK ma connessione DB fallisce — lo studente deve collegare IP e permessi MySQL.

debian3 — Guasto 2 Firewall
Firewall blocca HTTP
DIAGNOSI
sudo iptables -L INPUT -n --line-numbers
# Policy: DROP
# Regole: lo, ESTABLISHED, SSH:2222
# Manca: porta 80
# Conferma:
curl -I http://localhost   # OK
# Browser Windows: timeout
SOLUZIONE
sudo iptables -A INPUT \
-p tcp --dport 80 -j ACCEPT
# Salvare:
sudo iptables-save | \
sudo tee /etc/iptables/rules.v4
# Verifica:
sudo iptables -L INPUT -n \
--line-numbers
SSH funziona → lo studente pensa che la rete sia OK. Deve capire che il blocco è solo su HTTP.

debian3 — Guasto 3 Servizio
nginx root sbagliata
DIAGNOSI
sudo nginx -T | grep root
# Mostra: root /var/www/html
# Dovrebbe: root /var/www/wordpress
# nginx risponde ma serve la
# pagina di default Debian
# invece di WordPress
SOLUZIONE
sudo nano /etc/nginx/\
sites-available/wordpress
# Cambiare:
#  root /var/www/html;
# in:
#  root /var/www/wordpress;
sudo nginx -t
sudo systemctl reload nginx
Distinguere tra 'il servizio risponde' e 'il servizio risponde con il contenuto giusto'.

debian3 — Guasto 4 Applicazione
Nome sito errato → acme.local
Due modifiche necessarie: nginx + database WordPress
PASSO 1 — nginx server_name
# In sites-available/wordpress
# Cambiare:
#  server_name wordpress;
# in:
#  server_name acme.local;
sudo nginx -t
sudo systemctl reload nginx
PASSO 2 — URL nel database
mysql -h 10.0.0.2 -u wpuser
-p wordpress
UPDATE wp_options
SET option_value =
'http://acme.local'
WHERE option_name = 'siteurl';
UPDATE wp_options
SET option_value =
'http://acme.local'
WHERE option_name = 'home';
Senza il passo 2, WordPress fa redirect al vecchio nome anche con nginx corretto.

debian4
Backend — Diagnosi e soluzioni

debian4 — Guasto 5 Rete
Interfaccia rete interna spenta
DIAGNOSI
ip a show enp0s8
# State: DOWN, no IP
cat /etc/network/interfaces
# #auto enp0s8  (commentato!)
# Da debian3:
ping 10.0.0.2  # NESSUNA RISPOSTA
SOLUZIONE
sudo nano /etc/network/interfaces
# Decommentare:
#  #auto enp0s8
# in:
#  auto enp0s8
sudo ip link set enp0s8 up
sudo systemctl restart networking
# Verifica da debian3:
ping -c 4 10.0.0.2  # OK
Accesso solo via console VirtualBox — come andare fisicamente in sala server.

debian4 — Guasto 6 Firewall
Firewall blocca porta 3306
DIAGNOSI
sudo iptables -L INPUT -n \
--line-numbers
# Policy: DROP
# Regole: solo lo, ESTABLISHED
# No regola per 3306
# ping da debian3: OK
# ma mysql: TIMEOUT
SOLUZIONE
# MariaDB dalla rete interna
sudo iptables -A INPUT \
-i enp0s8 -p tcp \
--dport 3306 -j ACCEPT
# SSH dalla rete interna
sudo iptables -A INPUT \
-i enp0s8 -p tcp \
--dport 2222 -j ACCEPT
# Salvare:
sudo iptables-save | \
sudo tee /etc/iptables/rules.v4
Ping OK ma servizio KO → il 'qualcosa in mezzo' è il firewall.

debian4 — Guasto 7 Servizio
MariaDB bind-address a localhost
DIAGNOSI
sudo ss -tulnp | grep 3306
# 127.0.0.1:3306
# Ascolta SOLO su loopback!
grep bind-address \
/etc/mysql/mariadb.conf.d/\
50-server.cnf
# bind-address = 127.0.0.1
SOLUZIONE
sudo nano /etc/mysql/\
mariadb.conf.d/50-server.cnf
# Cambiare:
#  bind-address = 127.0.0.1
# in:
#  bind-address = 10.0.0.2
sudo systemctl restart mariadb
# Verifica:
sudo ss -tulnp | grep 3306
# Deve mostrare 10.0.0.2:3306
Il guasto più subdolo: rete OK + firewall OK ma servizio non raggiungibile. Serve ss -tulnp.

Verifica finale
192.168.56.111  acme.local
→ C:\Windows\System32\drivers\etc\hosts
Aprire http://acme.local nel browser
Il sito WordPress di Acme deve essere visibile e funzionante.
debian3 — Ruleset finale
-P INPUT DROP
-P FORWARD DROP
-P OUTPUT ACCEPT
-A INPUT -i lo -j ACCEPT
-A INPUT -m state ... -j ACCEPT
-A INPUT -i enp0s8 --dport 2222
-A INPUT --dport 80 -j ACCEPT
debian4 — Ruleset finale
-P INPUT DROP
-P FORWARD DROP
-P OUTPUT ACCEPT
-A INPUT -i lo -j ACCEPT
-A INPUT -m state ... -j ACCEPT
-A INPUT -i enp0s8 --dport 2222
-A INPUT -i enp0s8 --dport 3306
