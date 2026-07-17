# Linux Server e Amministrazione — Note Complete

## 1. Comandi Essenziali

```bash
# Filesystem
ls -la                    # Lista dettagliata
cd, pwd                   # Navigazione
cp -r, mv, rm -rf         # Copia, sposta, elimina
mkdir -p                  # Crea directory (anche nidificate)
find /path -name "*.txt"  # Ricerca file
chmod 755 file            # Permessi (rwx r-x r-x)
chown user:group file     # Proprietà
ln -s target link         # Symlink

# Processi
ps aux                    # Lista processi
top / htop                # Monitoraggio live
kill -9 PID               # Termina processo
kill -15 PID              # Graceful stop
systemctl status nginx    # Systemd service status
journalctl -u nginx -f    # Log service in tempo reale

# Rete
ip addr / ip route        # Configurazione rete
ss -tulpn                 # Porte in ascolto
ping, traceroute, dig     # Diagnostica
curl -v http://localhost   # Test HTTP

# Dischi
df -h                     # Spazio filesystem
du -sh /path              # Dimensione directory
lsblk                     # Dischi e partizioni
mount / umount            # Montaggio
fdisk / parted            # Partizionamento
```

## 2. Gestione Pacchetti

| Distro | Comando | 
|--------|---------|
| Debian/Ubuntu | `apt update && apt install -y <pkg>` |
| RHEL/CentOS | `dnf install -y <pkg>` |
| SUSE | `zypper install <pkg>` |

- `dpkg -l` / `rpm -qa`: lista pacchetti installati
- Repository: `/etc/apt/sources.list` o `/etc/yum.repos.d/`

## 3. Editor

- **nano**: semplice, shortcuts in chiaro in basso
- **vim**: modale (Normal/Insert/Command/Visual)
  - `i` insert, `ESC` normal, `:wq` salva+esci, `dd` cancella riga, `yy` copia riga
  - `/pattern` cerca, `:%s/vecchio/nuovo/g` sostituisci

## 4. Utenti & Permessi

```bash
useradd -m -s /bin/bash nomeutente
passwd nomeutente
usermod -aG sudo nomeutente    # Aggiunge a gruppo sudo
groups nomeutente

# ACL avanzate
setfacl -m u:utente:rwx file
getfacl file
```

## 5. Storage

- **RAID**: 0 (striping), 1 (mirror), 5 (parity), 10 (striped mirror)
- **LVM**: Volume Groups, Logical Volumes, snapshot, resize online
- **Filesystem**: ext4, XFS, Btrfs, ZFS
- **Mount persistente**: `/etc/fstab` entries

## 6. Servizi Tipici

| Servizio | Install | Comando |
|----------|---------|---------|
| Apache | `apt install apache2` | `systemctl restart apache2` |
| Nginx | `apt install nginx` | `systemctl status nginx` |
| MySQL/MariaDB | `apt install mariadb-server` | `mysql -u root -p` |
| PostgreSQL | `apt install postgresql` | `psql -U postgres` |
| Docker | script ufficiale | `docker run nginx` |
| SSH | `apt install openssh-server` | `/etc/ssh/sshd_config` |

## 7. Monitoraggio

- **Glances**: monitoraggio all-in-one (CPU, RAM, disk, network, processi)
- **htop**: processi interattivo colorato
- **iostat / vmstat / netstat**: statistiche specifiche
- **Prometheus + Grafana**: monitoring stack moderno
- **Log**: `/var/log/syslog`, `/var/log/auth.log`, `/var/log/nginx/`

## 8. Bash Scripting

```bash
#!/bin/bash
set -euo pipefail

# Backup script example
SOURCE="/home/user/data"
DEST="/backup/$(date +%Y%m%d)"
mkdir -p "$DEST"
cp -r "$SOURCE" "$DEST"
echo "Backup completato: $DEST"
```

## 9. Laboratori

- Ambiente LAMP/LNMP stack
- MySQL/MariaDB setup + utenti + database
- Glances monitoring setup
- Script backup automatici (cron)
- Docker install + container run
- SSH key auth + hardening
