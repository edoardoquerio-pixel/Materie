# wordpress due macchine

## Panoramica
• Mettere in rete due macchine Debian in VirtualBox

## Argomenti trattati
Linux, Reti, Configurazione, Installazione, Sicurezza

---
## Appunti

WordPress su Architettura
Guida pratica — Linux Server
Obiettivo dell'esercitazione
• Mettere in rete due macchine Debian in VirtualBox
debian1 → frontend: nginx + WordPress (accessibile dall'esterno)
debian2 → backend: MariaDB (accessibile SOLO da debian1 via rete interna)
Accesso SSH a debian2 solo tramite debian1 (ProxyJump)
Scenario realistico: separazione frontend/backend come in produzione
Architettura e configurazione VirtualBox
Configurazione schede di rete (NIC)
Rete interna intnet →
Rete interna intnet →
Clone VM e cambio hostname
Cambiare hostname su debian2:
Clonare debian1 in VirtualBox per ottenere debian2
• Durante il clone: rigenerare i MAC address (o farlo manualmente dopo)
• → echo "debian2" | sudo tee /etc/hostname
• → sudo sed -i 's/debian1/debian2/' /etc/hosts
• → sudo hostnamectl set-hostname debian2
Il clone condivide il MAC address originale: rigenerarlo per evitare conflitti DHCP
Configurazione rete interna (intnet)
Interfacce di rete rilevate
Rete interna intnet
Rete interna intnet
Configurazione /etc/network/interfaces
# --- debian1: aggiungere in fondo ---
# Internal network interface (intnet)
# Static IP for private communication with debian2
iface enp0s9 inet static
address 10.0.0.1
netmask 255.255.255.0
# --- debian2: aggiungere in fondo ---
# Internal network interface (intnet)
# Static IP for private communication with debian1
iface enp0s8 inet static
address 10.0.0.2
netmask 255.255.255.0
Attivare le interfacce e testare
# Attivare su debian1 (usare SEMPRE sudo)
sudo ip addr add 10.0.0.1/24 dev enp0s9
# Attivare su debian2
sudo ip addr add 10.0.0.2/24 dev enp0s8
# Verificare la connettività (da debian1)
ping -c 4 10.0.0.2
# Output atteso: 0% packet loss
Configurazione MariaDB su debian2
Installazione e sicurezza di base
# Installazione
sudo apt update && sudo apt install mariadb-server -y
# Accesso
-- Remove anonymous users
DELETE FROM mysql.user WHERE User='';
-- Disallow root login remotely
DELETE FROM mysql.user WHERE User='root'
AND Host NOT IN ('localhost', '127.0.0.1', '::1');
DROP DATABASE IF EXISTS test;
FLUSH PRIVILEGES;
Creazione database e utente WordPress
-- Create the WordPress database
CREATE DATABASE wordpress
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Create user restricted to debian1's IP only
CREATE USER 'wpuser'@'10.0.0.1' IDENTIFIED BY 'its2026';
-- Grant privileges only on wordpress DB
GRANT ALL PRIVILEGES ON wordpress.* TO 'wpuser'@'10.0.0.1';
FLUSH PRIVILEGES;
Configurazione bind-address in 50-server.cnf
# File: /etc/mysql/mariadb.conf.d/50-server.cnf
# bind-address: IP on which MariaDB listens
# This is debian2's IP on the internal network
# NOTE: NOT the client IP — that's controlled by user privileges
bind-address = 10.0.0.2
# Riavviare il servizio
sudo systemctl restart mariadb
# Verificare
sudo ss -tlnp | grep 3306
# Output atteso: LISTEN ... 10.0.0.2:3306
Installazione WordPress su debian1
Installazione nginx e PHP-FPM
# Installare nginx e PHP (NON usare 'php' generico:

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_wordpress_due_macchine.md*
