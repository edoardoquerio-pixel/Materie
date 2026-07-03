# wordpress due macchine doc

Fonte: `wordpress due macchine doc.pdf`

WordPress su Architettura a Due 
Macchine 
Guida pratica per ITS Academy — Linux Server 

1. Architettura dell'esercitazione 

L'obiettivo è mettere in rete due macchine virtuali Debian in modo che: 

• debian1 esponga WordPress su nginx, accessibile dall'esterno 
• debian2 ospiti MariaDB, raggiungibile solo da debian1 tramite rete interna 
• L'accesso SSH a debian2 avvenga esclusivamente passando per debian1 

(ProxyJump) 

1.1 Schema di rete 

Macchina 

NIC 1 

NIC 2 

NIC 3 

debian1 

NAT (internet) 

Solo Host (SSH da 
host) 

Rete interna 
intnet 

debian2 

NAT (internet) 

Rete interna 
intnet 

— 

Macchina 

IP Solo Host 

IP Rete Interna 

debian1 

debian2 

192.168.56.110 

— 

10.0.0.1 

10.0.0.2 

2. Preparazione delle macchine virtuali in VirtualBox 

2.1 Clonare la macchina di base 

Partendo da una macchina Debian già configurata (debian1), clonare la VM in VirtualBox per 
ottenere debian2. Durante il clone, scegliere di rigenerare i MAC address. 

⚠️ Nota: Se il MAC address non viene rigenerato automaticamente, farlo manualmente 
dalle impostazioni di ogni scheda di rete: Impostazioni → Rete → Impostazioni avanzate → 
icona 🔄 

2.2 Configurazione NIC in VirtualBox 

Su debian2 

• NIC 1: NAT (tenere per apt) 

 
 
 
 
 
 
• NIC 2: Rete interna → nome: intnet 

Su debian1 

• NIC 1: NAT 
• NIC 2: Solo Host (accesso SSH dall'host) 
• NIC 3: Rete interna → nome: intnet (aggiungere una terza scheda) 

3. Configurazione hostname su debian2 

Dopo il clone, cambiare il nome della macchina su debian2: 

echo "debian2" | sudo tee /etc/hostname 
sudo sed -i 's/debian1/debian2/' /etc/hosts 
sudo hostnamectl set-hostname debian2 

Verificare: 

hostnamectl 

4. Configurazione della rete interna (intnet) 

4.1 Verificare le interfacce disponibili 

ip link show 

Macchina 

Interfaccia 

debian1 

debian1 

debian1 

debian2 

debian2 

enp0s3 

enp0s8 

enp0s9 

enp0s3 

enp0s8 

Ruolo 

NAT 

Solo Host 

Rete interna intnet 

NAT 

Rete interna intnet 

4.2 Configurare IP statico su debian1 

Aprire /etc/network/interfaces e aggiungere: 

# Internal network interface (intnet) 
# Static IP for private communication with debian2 
auto enp0s9 
iface enp0s9 inet static 
 address 10.0.0.1 
 netmask 255.255.255.0 

Attivare l'interfaccia: 

 
 
 
 
 
 
 
 
 
sudo ip addr add 10.0.0.1/24 dev enp0s9 

4.3 Configurare IP statico su debian2 

Aprire /etc/network/interfaces e aggiungere: 

# Internal network interface (intnet) 
# Static IP for private communication with debian1 
auto enp0s8 
iface enp0s8 inet static 
 address 10.0.0.2 
 netmask 255.255.255.0 

Attivare l'interfaccia: 

sudo ip addr add 10.0.0.2/24 dev enp0s8 

4.4 Verificare la connettività 

Da debian1: 

ping -c 4 10.0.0.2 

⚠️ Nota: Usare sempre sudo con i comandi ip addr add, altrimenti il comando viene 
ignorato silenziosamente. 

5. Configurazione MariaDB su debian2 

5.1 Installazione 

sudo apt update && sudo apt install mariadb-server -y 

5.2 Accesso iniziale 

sudo mysql 

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

Modificare la riga bind-address: 

# bind-address: the IP on which MariaDB listens for incoming connections 
# This is debian2's IP on the internal network (intnet) 
# NOTE: bind-address is NOT the IP of the client connecting to the 
database 
# The client IP (debian1 = 10.0.0.1) is controlled by user 
privileges instead 
bind-address = 10.0.0.2 

Riavviare MariaDB: 

sudo systemctl restart mariadb 

Verificare che MariaDB ascolti sull'IP corretto: 

sudo ss -tlnp | grep 3306 

Output atteso: 

LISTEN 0 80 10.0.0.2:3306 0.0.0.0:* users:(("mariadbd",...)) 

5.6 Test connessione da debian1 

Installare il client MariaDB su debian1: 

sudo apt install mariadb-client -y 

 
 
 
 
 
 
 
 
 
 
 
Connettersi al database remoto: 

mysql -h 10.0.0.2 -u wpuser -pits2026 wordpress 

6. Installazione WordPress su debian1 

6.1 Installazione nginx e PHP 

sudo apt install nginx php8.4-fpm php8.4-mysql php8.4-curl php8.4-gd 
php8.4-mbstring php8.4-xml php8.4-xmlrpc php8.4-zip -y 

⚠️ Nota: Non usare il metapacchetto generico 'php' perché installa automaticamente 
Apache2, che va in conflitto con nginx sulla porta 80. 

Verificare che entrambi i servizi siano attivi: 

sudo systemctl status nginx 
sudo systemctl status php8.4-fpm 

6.2 Download e installazione WordPress 

cd /tmp && sudo wget https://wordpress.org/latest.tar.gz 
sudo tar -xzf /tmp/latest.tar.gz -C /tmp 
sudo mv /tmp/wordpress /var/www/wordpress 
sudo chown -R www-data:www-data /var/www/wordpress 
sudo find /var/www/wordpress -type d -exec chmod 755 {} \; 
sudo find /var/www/wordpress -type f -exec chmod 644 {} \; 

6.3 Configurazione /etc/hosts su debian1 

Aggiungere il nome wordpress a /etc/hosts: 

sudo nano /etc/hosts 

Aggiungere la riga: 

127.0.0.1 wordpress 

6.4 Configurazione nginx 

sudo nano /etc/nginx/sites-available/wordpress 

server { 
 listen 80; 
 server_name wordpress; 

 root /var/www/wordpress; 
 index index.php index.html; 

 
 
 
 
 
 
 
 
 
 
 
 # Log files 
 access_log /var/log/nginx/wordpress_access.log; 
 error_log /var/log/nginx/wordpress_error.log; 

 # Handle WordPress permalinks 
 location / { 
 try_files $uri $uri/ /index.php?$args; 
 } 

 # Pass PHP files to PHP-FPM 
 location ~ \.php$ { 
 include snippets/fastcgi-php.conf; 
 fastcgi_pass unix:/run/php/php8.4-fpm.sock; 
 } 

 # Deny access to hidden files 
 location ~ /\. { 
 deny all; 
 } 
} 

Abilitare il sito e ricaricare nginx: 

sudo ln -s /etc/nginx/sites-available/wordpress /etc/nginx/sitesenabled/ 
sudo nginx -t 
sudo systemctl reload nginx 

6.5 Configurazione wp-config.php 

sudo cp /var/www/wordpress/wp-config-sample.php /var/www/wordpress/wpconfig.php 
sudo nano /var/www/wordpress/wp-config.php 

Modificare questi parametri: 

define( 'DB_NAME', 'wordpress' ); 
define( 'DB_USER', 'wpuser' ); 
define( 'DB_PASSWORD', 'its2026' ); 
define( 'DB_HOST', '10.0.0.2' ); // debian2 internal IP 

7. Accesso SSH a debian2 tramite ProxyJump 

7.1 Comando diretto 

ssh -J its-usr@192.168.56.110 its-usr@10.0.0.2 

7.2 Configurazione ~/.ssh/config sull'host 

 
 
 
 
 
 
 
 
Aggiungere al file ~/.ssh/config sul proprio PC: 

Host debian1 
 HostName 192.168.56.110 
 User its-usr 

Host debian2 
 HostName 10.0.0.2 
 User its-usr 
 ProxyJump debian1 

Da questo momento è sufficiente: 

ssh debian2 

⚠️ Nota: ProxyJump non è un tunnel SSH. Con ProxyJump SSH apre una sessione su 
debian1 e da lì una nuova connessione SSH verso debian2. Il traffico è cifrato end-to-end. 
Un tunnel SSH (port forwarding) è una cosa diversa. 

8. Firewall su debian1 (ufw) 

Configurare ufw per accettare solo SSH (porta 22) e HTTP (porta 80). Tutto il resto in 
entrata viene bloccato. 

⚠️ Nota: Le regole 'deny incoming' bloccano solo il traffico in entrata su debian1. Le 
connessioni uscenti (verso MariaDB su debian2 e SSH verso debian2) non sono influenzate. 

8.1 Installazione e configurazione 

# Install ufw if not present 
sudo apt install ufw -y 

# Default policy: block all incoming, allow all outgoing 
sudo ufw default deny incoming 
sudo ufw default allow outgoing 

# Allow SSH 
sudo ufw allow 22/tcp 

# Allow HTTP 
sudo ufw allow 80/tcp 

# Enable firewall 
sudo ufw enable 

# Verify 
sudo ufw status verbose 

 
 
 
 
 
 
 
 
 
 
 
 
8.2 Traffico permesso 

Connessione 

Direzione su debian1 Permessa? 

SSH dall'esterno → debian1 
(porta 22) 

HTTP dall'esterno → WordPress 
(porta 80) 

debian1 → MariaDB su debian2 
(porta 3306) 

debian1 → SSH su debian2 (porta 
22) 

Qualsiasi altra connessione in 
entrata 

IN 

IN 

OUT 

OUT 

IN 

Sì 

Sì 

Sì 

Sì 

No — 
bloccata 

9. Riepilogo architettura finale 

Componente 

Macchina 

Dettaglio 

nginx + WordPress 

debian1 

PHP-FPM 8.4 

MariaDB 

debian1 

debian2 

Utente DB 

debian2 

IP 192.168.56.110 (Solo 
Host) / 10.0.0.1 (intnet) 

Gestione script PHP 

IP 10.0.0.2 (intnet) — non 
raggiungibile dall'esterno 

wpuser@10.0.0.1 — solo da 
debian1 

SSH esterno 

SSH debian2 

debian1 

Porta 22, IP 192.168.56.110 

via debian1 

ProxyJump: ssh -J debian1 
debian2