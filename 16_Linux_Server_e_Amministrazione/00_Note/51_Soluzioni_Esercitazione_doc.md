# Soluzioni Esercitazione doc

**File:** `Soluzioni Esercitazione doc.pdf`
**Tipo:** `.pdf`
**Dimensione:** 138.7 KB
**Ultima modifica:** 02/07/2026 09:22

---

ITS ICT Piemonte — Linux Server — SOLUZIONI 
Pagina 1 
 
SOLUZIONI 
Diagnostica e messa in sicurezza — Esercitazione WordPress 
Docente: Wolfgang Cecchin 
Panoramica dei guasti 
# Macchina Livello Guasto Causa 
1 debian3 Rete IP rete interna errato 10.0.0.11 invece di 10.0.0.1 
2 debian3 Firewall HTTP bloccato Policy DROP, no regola 
porta 80 
3 debian3 Servizio nginx root sbagliata /var/www/html invece di 
/var/www/wordpress 
4 debian3 Applicazione Nome sito errato server_name e 
wp_options da cambiare 
5 debian4 Rete Interfaccia intnet spenta enp0s8 DOWN, auto 
commentato 
6 debian4 Firewall MariaDB bloccato Policy DROP, no regola 
porta 3306 
7 debian4 Servizio bind-address errato 127.0.0.1 invece di 10.0.0.2 
  

ITS ICT Piemonte — Linux Server — SOLUZIONI 
Pagina 2 
DEBIAN3 — DIAGNOSI E SOLUZIONI 
 
Guasto 1 — IP rete interna errato 
Diagnosi 
ip a show enp0s9 
L'interfaccia mostra 10.0.0.11/24 invece di 10.0.0.1/24. Anche se il ping verso 10.0.0.2 funziona 
(stessa subnet), WordPress non riesce a connettersi al database perché l'utente MariaDB 
wpuser è autorizzato solo per connessioni dall'IP 10.0.0.1. 
Soluzione 
sudo nano /etc/network/interfaces 
 
# Modificare la riga: 
#   address 10.0.0.11 
# in: 
#   address 10.0.0.1 
Applicare: 
sudo systemctl restart networking 
Verifica: 
ip a show enp0s9 
# Deve mostrare 10.0.0.1/24 
Guasto 2 — Firewall blocca HTTP 
Diagnosi 
sudo iptables -L INPUT -n --line-numbers 
La policy è DROP. Le regole permettono solo loopback, ESTABLISHED/RELATED e SSH sulla 
porta 2222. Non c'è nessuna regola per la porta 80. 
Test di conferma: 
curl -I http://localhost 
# Funziona (loopback aperto) 
 
# Ma dal browser Windows: timeout 
# (la porta 80 e' bloccata dall'esterno) 
Soluzione 
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT 
 
# Salvare per la persistenza: 
sudo iptables-save | sudo tee /etc/iptables/rules.v4 

ITS ICT Piemonte — Linux Server — SOLUZIONI 
Pagina 3 
Verifica: 
sudo iptables -L INPUT -n --line-numbers 
# Deve mostrare la regola ACCEPT per dpt:80 
Guasto 3 — nginx root sbagliata 
Diagnosi 
sudo nginx -T | grep root 
Il virtual host punta a root /var/www/html invece di root /var/www/wordpress. nginx 
risponde, ma serve la pagina di default Debian. 
Soluzione 
sudo nano /etc/nginx/sites-available/wordpress 
 
# Modificare: 
#   root /var/www/html; 
# in: 
#   root /var/www/wordpress; 
Applicare: 
sudo nginx -t 
sudo systemctl reload nginx 
Guasto 4 — Nome sito errato (acme.local) 
Il sito è configurato per rispondere al nome "wordpress". Acme richiede che risponda a 
"acme.local". La modifica va fatta in due punti: nginx e il database WordPress.  
Passo 1 — nginx server_name 
sudo nano /etc/nginx/sites-available/wordpress 
 
# Modificare: 
#   server_name wordpress; 
# in: 
#   server_name acme.local; 
sudo nginx -t 
sudo systemctl reload nginx 
Passo 2 — URL nel database WordPress 
Da debian3, connettersi al database su debian4: 
mysql -h 10.0.0.2 -u wpuser -p wordpress 
Aggiornare i due campi: 
UPDATE wp_options SET option_value = 'http://acme.local' 

ITS ICT Piemonte — Linux Server — SOLUZIONI 
Pagina 4 
WHERE option_name = 'siteurl'; 
 
UPDATE wp_options SET option_value = 'http://acme.local' 
WHERE option_name = 'home'; 
Verifica: 
SELECT option_name, option_value FROM wp_options 
WHERE option_name IN ('siteurl', 'home'); 
 
# Entrambi devono mostrare http://acme.local 
Nota: senza questo passaggio, WordPress continua a generare link e redirect verso il vecchio 
nome. Lo studente che corregge solo nginx ma non il database vedrà il sito caricarsi in 
modo anomalo. 
  

ITS ICT Piemonte — Linux Server — SOLUZIONI 
Pagina 5 
DEBIAN4 — DIAGNOSI E SOLUZIONI 
 
Nota: l'accesso iniziale a debian4 avviene esclusivamente dalla console VirtualBox.  
Guasto 5 — Interfaccia rete interna disattivata 
Diagnosi 
ip a show enp0s8 
# State: DOWN, nessun indirizzo IP 
 
cat /etc/network/interfaces 
# La riga 'auto enp0s8' e' commentata: #auto enp0s8 
L'interfaccia di rete interna è spenta e non si attiva al boot. 
Soluzione 
sudo nano /etc/network/interfaces 
 
# Decommentare la riga: 
#   #auto enp0s8 
# in: 
#   auto enp0s8 
Attivare: 
sudo ip link set enp0s8 up 
sudo systemctl restart networking 
Verifica: 
ip a show enp0s8 
# Deve mostrare 10.0.0.2/24 e state UP 
 
# Da debian3: 
ping -c 4 10.0.0.2 
# Deve rispondere 
Guasto 6 — Firewall blocca porta 3306 
Diagnosi 
sudo iptables -L INPUT -n --line-numbers 
Policy DROP, regole solo per loopback e ESTABLISHED/RELATED. Nessuna regola per la porta 
3306. 
Il ping da debian3 risponde, ma la connessione MariaDB va in timeout. 
Soluzione 
Aggiungere le regole per MariaDB e SSH, esclusivamente dalla rete interna:  

ITS ICT Piemonte — Linux Server — SOLUZIONI 
Pagina 6 
sudo iptables -A INPUT -i enp0s8 -p tcp --dport 3306 -j ACCEPT 
sudo iptables -A INPUT -i enp0s8 -p tcp --dport 2222 -j ACCEPT 
 
# Salvare: 
sudo iptables-save | sudo tee /etc/iptables/rules.v4 
Guasto 7 — MariaDB bind-address a localhost 
Diagnosi 
Anche con l'interfaccia attiva e il firewall aperto, da debian3: 
mysql -h 10.0.0.2 -u wpuser -p 
# Timeout o connessione rifiutata 
Su debian4: 
sudo ss -tulnp | grep 3306 
# Mostra 127.0.0.1:3306 — ascolta solo sulla loopback 
 
grep bind-address /etc/mysql/mariadb.conf.d/50-server.cnf 
# bind-address = 127.0.0.1 
MariaDB ascolta solo sulla loopback, non sull'interfaccia di rete interna. 
Soluzione 
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf 
 
# Modificare: 
#   bind-address = 127.0.0.1 
# in: 
#   bind-address = 10.0.0.2 
Riavviare: 
sudo systemctl restart mariadb 
Verifica: 
sudo ss -tulnp | grep 3306 
# Deve mostrare 10.0.0.2:3306 
 
# Da debian3: 
mysql -h 10.0.0.2 -u wpuser -p 
# Connessione riuscita 
  

ITS ICT Piemonte — Linux Server — SOLUZIONI 
Pagina 7 
VERIFICA FINALE 
 
Verifica dal PC Windows 
1. Aggiungere nel file C:\Windows\System32\drivers\etc\hosts: 
192.168.56.111  acme.local 
 
2. Aprire il browser su http://acme.local 
3. Il sito WordPress di Acme deve essere visibile e funzionante. 
Configurazione firewall completa 
debian3 — Ruleset finale 
sudo iptables -P INPUT DROP 
sudo iptables -P FORWARD DROP 
sudo iptables -P OUTPUT ACCEPT 
 
sudo iptables -A INPUT -i lo -j ACCEPT 
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT 
sudo iptables -A INPUT -i enp0s8 -p tcp --dport 2222 -j ACCEPT 
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT 
 
sudo iptables-save | sudo tee /etc/iptables/rules.v4 
debian4 — Ruleset finale 
sudo iptables -P INPUT DROP 
sudo iptables -P FORWARD DROP 
sudo iptables -P OUTPUT ACCEPT 
 
sudo iptables -A INPUT -i lo -j ACCEPT 
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT 
sudo iptables -A INPUT -i enp0s8 -p tcp --dport 2222 -j ACCEPT 
sudo iptables -A INPUT -i enp0s8 -p tcp --dport 3306 -j ACCEPT 
 
sudo iptables-save | sudo tee /etc/iptables/rules.v4 
 
