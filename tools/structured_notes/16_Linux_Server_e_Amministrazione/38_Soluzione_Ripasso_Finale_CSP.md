# Soluzione Ripasso Finale CSP

## Panoramica
ITS ICT Piemonte · Linux Server

## Argomenti trattati
Linux, Cloud, Reti, API REST, Installazione

---
## Appunti

ITS ICT Piemonte · Linux Server
SOLUZIONE — StudioFoto Arcobaleno
ITS ICT Piemonte
Corso Linux Server — CSP — Cloud Specialist
Ripasso finale — Linux Server
Scenario: StudioFoto Arcobaleno
Comandi, configurazioni e verifiche
Durata: 2 ore · Valutazione: 16 punti (1 per punto) — sufficienza a 10
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
iface enp0s8 inet static
address 192.168.56.120
netmask 255.255.255.0
Applica e verifica
sudo systemctl restart networking
ip a show enp0s8 # inet 192.168.56.120/24
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
sudo apt update
sudo apt install -y nginx php-fpm # Debian 12 -> php8.2-fpm
Pagina info.php
sudo mkdir -p /var/www/arcobaleno
echo '<?php phpinfo();' | sudo tee /var/www/arcobaleno/info.php
/etc/nginx/sites-available/arcobaleno
server_name arcobaleno.local;
root /var/www/arcobaleno;
index index.php info.php;
location / { try_files $uri $uri/ =404; }
location ~ \.php$ {
include snippets/fastcgi-php.conf;
fastcgi_pass unix:/run/php/php8.2-fpm.sock;
ITS ICT Piemonte · Linux Server
SOLUZIONE — StudioFoto Arcobaleno
Abilita e verifica
sudo ln -s /etc/nginx/sites-available/arcobaleno /etc/nginx/sites-enabled/

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_Soluzione_Ripasso_Finale_CSP.md*
