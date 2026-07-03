# wordpress due macchine doc

## Panoramica
WordPress su Architettura a Due

## Argomenti trattati
Linux, Reti, Configurazione, Installazione, Sicurezza

---
## Appunti

WordPress su Architettura a Due
Guida pratica per ITS Academy — Linux Server
1. Architettura dell'esercitazione
L'obiettivo è mettere in rete due macchine virtuali Debian in modo che:
• debian1 esponga WordPress su nginx, accessibile dall'esterno
• debian2 ospiti MariaDB, raggiungibile solo da debian1 tramite rete interna
• L'accesso SSH a debian2 avvenga esclusivamente passando per debian1
1.1 Schema di rete
Solo Host (SSH da
IP Rete Interna
2. Preparazione delle macchine virtuali in VirtualBox
2.1 Clonare la macchina di base
Partendo da una macchina Debian già configurata (debian1), clonare la VM in VirtualBox per
ottenere debian2. Durante il clone, scegliere di rigenerare i MAC address.
⚠️ Nota: Se il MAC address non viene rigenerato automaticamente, farlo manualmente
dalle impostazioni di ogni scheda di rete: Impostazioni → Rete → Impostazioni avanzate →
2.2 Configurazione NIC in VirtualBox
• NIC 1: NAT (tenere per apt)
• NIC 2: Rete interna → nome: intnet
• NIC 2: Solo Host (accesso SSH dall'host)
• NIC 3: Rete interna → nome: intnet (aggiungere una terza scheda)
3. Configurazione hostname su debian2
Dopo il clone, cambiare il nome della macchina su debian2:
echo "debian2" | sudo tee /etc/hostname
sudo sed -i 's/debian1/debian2/' /etc/hosts
sudo hostnamectl set-hostname debian2
4. Configurazione della rete interna (intnet)
4.1 Verificare le interfacce disponibili
Rete interna intnet
Rete interna intnet
4.2 Configurare IP statico su debian1
Aprire /etc/network/interfaces e aggiungere:
# Internal network interface (intnet)
# Static IP for private communication with debian2
iface enp0s9 inet static
address 10.0.0.1
netmask 255.255.255.0
Attivare l'interfaccia:
sudo ip addr add 10.0.0.1/24 dev enp0s9
4.3 Configurare IP statico su debian2
Aprire /etc/network/interfaces e aggiungere:
# Internal network interface (intnet)
# Static IP for private communication with debian1
iface enp0s8 inet static
address 10.0.0.2
netmask 255.255.255.0
Attivare l'interfaccia:
sudo ip addr add 10.0.0.2/24 dev enp0s8
4.4 Verificare la connettività
ping -c 4 10.0.0.2
⚠️ Nota: Usare sempre sudo con i comandi ip addr add, altrimenti il comando viene
ignorato silenziosamente.
5. Configurazione MariaDB su debian2
5.1 Installazione
sudo apt update && sudo apt install mariadb-server -y
5.2 Accesso iniziale
5.3 Sicurezza di base
-- Remove anonymous users
DELETE FROM mysql.user WHERE User='';
-- Disallow root login remotely
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost',
'127.0.0.1', '::1');
-- Remove test database
DROP DATABASE IF EXISTS test;
-- Apply changes
FLUSH PRIVILEGES;
5.4 Creazione database e utente WordPress
-- Create the WordPress database
CREATE DATABASE wordpress CHARACTER SET utf8mb4 COLLATE
utf8mb4_unicode_ci;
-- Create a dedicated user for WordPress
-- Access is restricted to debian1's IP on the internal network
CREATE USER 'wpuser'@'10.0.0.1' IDENTIFIED BY 'its2026';
-- Grant full privileges on the WordPress database only
GRANT ALL PRIVILEGES ON wordpress.* TO 'wpuser'@'10.0.0.1';
-- Apply changes
FLUSH PRIVILEGES;
5.5 Configurazione bind-address
Aprire il file di configurazione:
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_wordpress_due_macchine_doc.md*
