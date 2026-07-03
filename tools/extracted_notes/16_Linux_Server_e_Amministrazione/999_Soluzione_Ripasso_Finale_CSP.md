# Soluzione Ripasso Finale CSP

Fonte: `Soluzione Ripasso Finale CSP.pdf`

ITS ICT Piemonte · Linux Server 

SOLUZIONE — StudioFoto Arcobaleno 

ITS ICT Piemonte 
Corso Linux Server — CSP — Cloud Specialist 

SOLUZIONE 

Ripasso finale — Linux Server 
Scenario: StudioFoto Arcobaleno 

Comandi, configurazioni e verifiche 
Durata: 2 ore · Valutazione: 16 punti (1 per punto) — sufficienza a 10 

Pag. 1 

 
 
 
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
auto enp0s8 
iface enp0s8 inet static 
 address 192.168.56.120 
 netmask 255.255.255.0 

Applica e verifica 

sudo systemctl restart networking 
ip a show enp0s8 # inet 192.168.56.120/24 

Pag. 2 

 
 
 
 
 
 
 
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

Installazione 

sudo apt update 
sudo apt install -y nginx php-fpm # Debian 12 -> php8.2-fpm 

Pagina info.php 

sudo mkdir -p /var/www/arcobaleno 
echo '<?php phpinfo();' | sudo tee /var/www/arcobaleno/info.php 

/etc/nginx/sites-available/arcobaleno 

server { 
 listen 80; 
 server_name arcobaleno.local; 
 root /var/www/arcobaleno; 
 index index.php info.php; 
 location / { try_files $uri $uri/ =404; } 
 location ~ \.php$ { 
 include snippets/fastcgi-php.conf; 
 fastcgi_pass unix:/run/php/php8.2-fpm.sock; 
 } 
} 

Pag. 3 

 
 
 
 
 
 
 
ITS ICT Piemonte · Linux Server 

SOLUZIONE — StudioFoto Arcobaleno 

Abilita e verifica 

sudo ln -s /etc/nginx/sites-available/arcobaleno /etc/nginx/sites-enabled/ 
sudo nginx -t && sudo systemctl reload nginx 
curl -s http://localhost/info.php | head # HTML, non sorgente PHP 

Parte 5 — Database MariaDB (~15 min) 

Installazione e hardening 

sudo apt install -y mariadb-server 
sudo mysql_secure_installation 

Database e utente (console come root) 

sudo mariadb 
CREATE DATABASE arcobaleno_db; 
CREATE USER 'wpuser'@'localhost' IDENTIFIED BY 'PasswordSicura'; 
GRANT ALL PRIVILEGES ON arcobaleno_db.* TO 'wpuser'@'localhost'; 
FLUSH PRIVILEGES; 
EXIT; 

Verifica login applicativo 

mariadb -u wpuser -p -e 'SHOW DATABASES;' 
# deve mostrare solo: information_schema, arcobaleno_db 

Parte 6 — Processi e servizi (~10 min) 

Stato e avvio automatico 

sudo systemctl enable --now nginx php8.2-fpm mariadb 
systemctl is-enabled nginx php8.2-fpm mariadb # enabled x3 
systemctl status nginx php8.2-fpm mariadb --no-pager 

Processo in background e terminazione 

sleep 1000 & 
jobs -l # mostra [1] <PID> 
ps aux | grep sleep 
kill <PID> # SIGTERM (15); kill -9 <PID> solo se necessario 

Parte 7 — Automazione (cron) e firewall (iptables) (~15 min) 

/usr/local/bin/backup-scatti.sh 

#!/bin/bash 
SRC="/srv/scatti" 
DEST="/var/backups" 

Pag. 4 

 
 
 
 
 
 
 
ITS ICT Piemonte · Linux Server 

SOLUZIONE — StudioFoto Arcobaleno 

DATA=$(date +%F) # AAAA-MM-GG 
mkdir -p "$DEST" 
tar -czf "$DEST/scatti-$DATA.tar.gz" "$SRC" 

Esegui-bilità e cron 

sudo chmod +x /usr/local/bin/backup-scatti.sh 
sudo crontab -e 
# riga da aggiungere (min ora * * *): 
30 2 * * * /usr/local/bin/backup-scatti.sh 

iptables — installazione e regole 

sudo apt install -y iptables iptables-persistent 
sudo iptables -A INPUT -i lo -j ACCEPT 
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT 
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT # SSH 
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT # HTTP 
sudo iptables -P INPUT DROP # policy DROP DOPO gli ACCEPT 
sudo iptables -P FORWARD DROP 

Persistenza e verifica 

sudo netfilter-persistent save 
sudo iptables -L -n -v 

Parte 8 — Diagnostica (~5 min) 

1. Rete 

ip a # interfaccia su e con IP corretto? 
ip route # gateway presente? 
ping 192.168.56.120 

2. Firewall 

sudo iptables -L -n -v # la porta 80 e' permessa in INPUT? 

3. Servizio 

systemctl status nginx php8.2-fpm 
ss -tlnp | grep :80 # nginx in ascolto sulla 80? 
sudo nginx -t 

4. Applicazione 

curl -I http://localhost/ 
sudo tail /var/log/nginx/error.log 
# es. errore DB: verificare socket php-fpm e credenziali MariaDB 

Pag. 5