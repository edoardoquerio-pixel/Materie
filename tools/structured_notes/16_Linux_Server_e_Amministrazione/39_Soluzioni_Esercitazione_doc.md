# Soluzioni Esercitazione doc

## Panoramica
ITS ICT Piemonte — Linux Server — SOLUZIONI

## Argomenti trattati
Linux, Sicurezza, Reti, Database, Data Analytics

---
## Appunti

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
*Fonte: 999_Soluzioni_Esercitazione_doc.md*
