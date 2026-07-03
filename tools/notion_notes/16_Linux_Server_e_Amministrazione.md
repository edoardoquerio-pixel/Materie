# 16_Linux_Server_e_Amministrazione

## 📋 Panoramica

Amministrazione di server Linux con Debian/Ubuntu. Copre installazione, comandi essenziali, gestione utenti/permessi, SSH, DNS, web server (Apache/Nginx), MySQL/MariaDB, PHP, firewall (iptables/nftables), shell avanzata (grep, sed, awk), strumenti di diagnostica, networking Linux, WordPress deployment, cron e automazione. Docente: Wolfgang Cecchin.

## 📚 Indice degli argomenti

### 1. Installazione e Architetture
- **Architetture server**: Fisico, VM, Container, Cloud, Serverless
- **Distribuzioni Linux**: Famiglie RedHat (Fedora/CentOS), Debian (Ubuntu), SuSE, Arch, Gentoo
- **Installazione Debian**: Partizionamento, LVM, filesystem, pacchetti base
- **VM su VMware/VirtualBox/KVM**: Setup e configurazione

### 2. Comandi Essenziali
- **Struttura comandi**: `comando [opzioni] [parametri]` (es. `ls -lah /home`)
- **Filesystem**: `/`, `/home`, `/etc`, `/var`, `/tmp`, `/usr`, `/bin`, `/sbin`
- **Shell**: bash, autocomplete (Tab), history (↑↓), `CTRL+D` (logout), `CTRL+C` (interrompi)
- **File operazioni**: `touch`, `cat`, `nano`/`vi`, `cp`, `mv`, `rm`, `mkdir`, `chmod`, `chown`
- **Redirezione**: `>` (sovrascrivi), `>>` (append), `|` (pipe)
- **Manuali**: `man comando`, `comando --help`

### 3. Utenti, Permessi e SSH
- **Utenti**: `useradd`, `usermod`, `userdel`, `passwd`, `/etc/passwd`, `/etc/shadow`
- **Permessi**: rwx (444/644/755/700), `chmod` (ottale e simbolico), `chown`, `chgrp`
- **SU e Sudo**: `su - utente`, configurazione `/etc/sudoers`, gruppo `sudo`
- **Permessi speciali**: SUID (4xxx), SGID (2xxx), Sticky Bit (1xxx)
- **SSH**: `ssh user@host`, chiavi pubbliche/private (Ed25519/RSA), `~/.ssh/authorized_keys`
- **Configurazione SSH**: `/etc/ssh/sshd_config`, porta, PermitRootLogin, PasswordAuthentication

### 4. DNS e Nomi Host
- **hostname**: `hostnamectl`, `/etc/hostname`
- **/etc/hosts**: Risoluzione locale nomi-IP
- **DNS client**: `/etc/resolv.conf`, `systemd-resolved`
- **named (BIND)**: Concetti base, zone file

### 5. Web Server (Apache/Nginx)
- **Apache2**: Installazione, `sites-available`/`sites-enabled`, VirtualHost, `.htaccess`
- **Moduli**: mod_rewrite, mod_ssl, mod_proxy
- **Nginx**: Configurazione, server blocks, proxy inverso, SSL/TLS
- **Esercizi**: Hosting multiplo, HTTPS self-signed, reverse proxy PHP

### 6. Database MySQL/MariaDB
- **Installazione**: `apt install mariadb-server`, `mysql_secure_installation`
- **Comandi SQL**: `CREATE DATABASE`, `CREATE USER`, `GRANT`, `SELECT`, `INSERT`
- **Backup/Ripristino**: `mysqldump`, `mysql < backup.sql`
- **WordPress**: Configurazione LAMP/LNMP, `wp-config.php`

### 7. PHP
- **Installazione**: `php`, `php-fpm`, `php-mysql`, moduli comuni
- **Configurazione**: `php.ini`, pooling FPM, integrazione con Apache/Nginx

### 8. Shell Avanzata e Scripting
- **grep, sed, awk**: Ricerca, sostituzione, elaborazione testo
- **find**: Ricerca avanzata file (nome, tipo, dimensione, data)
- **Espressioni regolari**: Pattern matching in grep/sed/awk
- **Cron e at**: Pianificazione task ricorrenti (`crontab -e`) e singoli (`at`)
- **Script bash**: `#!/bin/bash`, variabili, `if/for/while`, funzioni

### 9. Networking e Firewall
- **Schede di rete**: `ip a`, `ip route`, `ss`, `ping`, `traceroute`
- **Firewall**: `iptables`/`nftables`, catene, regole, NAT, port forwarding
- **Diagnostica**: `tcpdump`, `netstat`, `ss`, `lsof`, `nslookup`, `dig`
- **Networking Linux**: Bridge, bonding, VLAN su Linux

### 10. Diagnostica e Monitoraggio
- **glances**: Monitoraggio sistema completo (CPU, RAM, disco, rete)
- **Strumenti diagnostici**: `dmesg`, `journalctl`, `top`/`htop`, `df`/`du`, `free`
- **Troubleshooting**: `strace`, `lsof`, `systemctl status`

### 11. Deployment WordPress
- **Architettura due macchine**: Web server + DB server separati
- **Configurazione**: VirtualHost, database remoto, permalink, sicurezza
- **Esercizi**: Migrazione, backup, aggiornamento

## ⚡ Punti Chiave

- **Debian** è la distribuzione di riferimento per il corso (famiglia stable/testing)
- Distinguere tra permessi **ottali** (chmod 755) e **simbolici** (chmod u+x)
- **SSH con chiavi** è più sicuro della password — usare `ssh-keygen -t ed25519`
- `iptables` è legacy → **nftables** è il successore moderne
- **mysqldump** è essenziale per backup DB: `mysqldump -u root -p db > backup.sql`
- Il piping (`|`) è il cuore della filosofia Unix — componi comandi semplici
- WordPress: configurare permalink e .htaccess subito dopo installazione

## 📎 Risorse Collegate

- **02_Esercizi/**: Esercizi su utenti/permessi, ripasso meta-corso, find, grep/sed/awk
- **03_Progetti/**: —
- **Materie collegate**: `17_Container_Docker_Kubernetes`, `19_Virtualizzazione`, `06_Reti_e_Sicurezza_Informatica`, `14_Cloud_Azure`
