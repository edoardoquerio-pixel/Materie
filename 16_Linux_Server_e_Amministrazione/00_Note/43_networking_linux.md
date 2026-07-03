# networking linux

**File:** `networking linux.pdf`
**Tipo:** `.pdf`
**Dimensione:** 445.1 KB
**Ultima modifica:** 02/07/2026 09:22

---

DOCENTE Wolfgang Cecchin
UNITA’ FORMATIVA Linux Server
ARGOMENTO Networking

Networking
in Linux
Configurazione, diagnostica e gestione della rete
Linux Server  |  ITS Academy

Agenda
Networking in Linux — ITS Academy
• 1.  Concetti fondamentali — stack TCP/IP e interfacce
• 2.  Il comando ip — visualizzare e configurare
• 3.  Routing e tabella di instradamento
• 4.  Configurazione persistente — interfaces e Netplan
• 5.  Risoluzione dei nomi — DNS, /etc/hosts, /etc/resolv.conf
• 6.  Diagnostica — ping, traceroute, ss, tcpdump
• 7.  Porte e servizi comuni
• 8.  Esercizio pratico — Studio Fotografico Bianchi

2. Concetti fondamentali — Stack TCP/IP
Networking in Linux — ITS Academy
Applicazione HTTP · FTP · SSH · DNS
Trasporto TCP (affidabile) · UDP (veloce)
Rete IP · ICMP · Routing
Collegamento Ethernet · ARP · MAC

Interfacce di rete — nomenclatura predittiva
Networking in Linux — ITS Academy
eth0 / enp3s0
Ethernet fisica
wlan0 / wlp2s0
Wireless
lo
Loopback — 127.0.0.1 (locale)
virbr0 / docker0
Bridge virtuale
⚑ Il loopback è usato da servizi che comunicano localmente — es. PHP → MySQL (127.0.0.1:3306)

3. Il comando ip — operazioni principali
Networking in Linux — ITS Academy
Sostituisce il vecchio ifconfig — strumento principale in Linux moderno
Visualizzare
ip addr show
ip addr show enp3s0
ip route show
ip link show
Modificare (temporaneo)
ip addr add 192.168.1.10/24 dev enp3s0
ip addr del 192.168.1.10/24 dev enp3s0
ip link set enp3s0 up
ip link set enp3s0 down
Routing
ip route add default via 192.168.1.1
ip route add 10.0.0.0/8 via 192.168.1.254
ip route del default via 192.168.1.1
Tutte le modifiche con ip sono temporanee — perse al riavvio!

4. Configurazione persistente
Networking in Linux — ITS Academy
Debian — /etc/network/interfaces
auto enp3s0
iface enp3s0 inet static
address 192.168.1.100
netmask 255.255.255.0
gateway 192.168.1.1
dns-nameservers 8.8.8.8
systemctl restart networking
Ubuntu — Netplan /etc/netplan/*.yaml
network:
version: 2
ethernets:
enp3s0:
addresses: [192.168.1.100/24]
routes:
- to: default
via: 192.168.1.1
netplan apply
Best practice: usare file dedicati nelle directory .d/ — non modificare i file di configurazione base (come per MariaDB)

5. Risoluzione dei nomi (DNS)
Networking in Linux — ITS Academy
Applicazione
(ping google.com) →
/etc/nsswitch.conf
ordine: files → dns →
/etc/hosts
mappature locali →
Server DNS
/etc/resolv.conf
/etc/hosts
127.0.0.1     localhost
192.168.1.10  server-web.lan
192.168.1.20  db.lan
/etc/resolv.conf
nameserver 8.8.8.8
nameserver 1.1.1.1
search lan
Con systemd-resolved: /etc/resolv.conf è un symlink gestito automaticamente — modificarlo direttamente potrebbe non avere effetto.

6. Diagnostica di rete — sequenza logica
Networking in Linux — ITS Academy
1 Interfaccia attiva? ip addr show
2 Raggiungo il gateway? ping -c 4 192.168.1.1
3 Internet raggiungibile (per IP)? ping -c 4 8.8.8.8
4 DNS funziona? dig google.com  /  nslookup google.com
Altri strumenti: traceroute / tracepath   |   ss -tuln / ss -tulnp   |   tcpdump -i enp3s0

7. Porte e servizi comuni
Networking in Linux — ITS Academy
ss -tulnp   # mostra porte in ascolto con nome del processo
Porta Protocollo Servizio
22 TCP SSH
25 TCP SMTP
53 TCP/UDP DNS
80 TCP HTTP
443 TCP HTTPS
3306 TCP MySQL / MariaDB
5432 TCP PostgreSQL

8. Esercizio pratico — Studio Fotografico Bianchi
Networking in Linux — ITS Academy
Scenario:
Il server Linux dello studio ha due interfacce: enp3s0 (LAN 192.168.10.0/24) e enp4s0 (Internet via DHCP)
Obiettivi:
• Assegnare a enp3s0 l'IP statico 192.168.10.1/24 in modo 
persistente
• Aggiungere in /etc/hosts le voci per i client della LAN
• Verificare la connettività con ping verso i client
• Verificare le porte in ascolto con ss -tulnp
• Usare traceroute per analizzare il percorso verso 8.8.8.8
Domande di riflessione:
• Perché è importante configurare l'IP in modo 
persistente?
• Cosa succede se il gateway predefinito non è 
configurato correttamente?
• Qual è la differenza pratica tra /etc/hosts e un 
server DNS?

Riepilogo
Visualizzare interfacce ip addr show
Configurare IP (temp.) ip addr add IP/MASK dev IF
Tabella di routing ip route show
Conf. persistente Debian /etc/network/interfaces
Conf. persistente Ubuntu /etc/netplan/*.yaml
Risoluzione locale /etc/hosts
Server DNS /etc/resolv.conf
Porte in ascolto ss -tuln / ss -tulnp
Cattura traffico tcpdump -i enp3s0
