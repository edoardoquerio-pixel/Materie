# Soluzioni Esercitazione presentazione

## Panoramica
Diagnostica e messa in sicurezza

## Argomenti trattati
Sicurezza, Reti, API REST, Database, Data Analytics

---
## Appunti

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
*Fonte: 999_Soluzioni_Esercitazione_presentazione.md*
