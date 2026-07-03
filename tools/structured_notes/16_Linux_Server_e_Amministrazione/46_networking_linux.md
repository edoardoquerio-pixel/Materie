# networking linux

## Panoramica
Configurazione, diagnostica e gestione della rete

## Argomenti trattati
Linux, Configurazione, Reti, Docker, API REST

---
## Appunti

Wolfgang Cecchin
UNITA’ FORMATIVA
Configurazione, diagnostica e gestione della rete
Linux Server | ITS Academy
1. Concetti fondamentali — stack TCP/IP e interfacce
2. Il comando ip — visualizzare e configurare
3. Routing e tabella di instradamento
4. Configurazione persistente — interfaces e Netplan
5. Risoluzione dei nomi — DNS, /etc/hosts, /etc/resolv.conf
6. Diagnostica — ping, traceroute, ss, tcpdump
7. Porte e servizi comuni
8. Esercizio pratico — Studio Fotografico Bianchi
Networking in Linux — ITS Academy
2. Concetti fondamentali — Stack TCP/IP
HTTP · FTP · SSH · DNS
TCP (affidabile) · UDP (veloce)
IP · ICMP · Routing
Ethernet · ARP · MAC
Networking in Linux — ITS Academy
Interfacce di rete — nomenclatura predittiva
Ethernet fisica
virbr0 / docker0
Loopback — 127.0.0.1 (locale)
Bridge virtuale
⚑ Il loopback è usato da servizi che comunicano localmente — es. PHP → MySQL (127.0.0.1:3306)
Networking in Linux — ITS Academy
3. Il comando ip — operazioni principali
Sostituisce il vecchio ifconfig — strumento principale in Linux moderno
Modificare (temporaneo)
ip addr add 192.168.1.10/24 dev enp3s0
ip addr del 192.168.1.10/24 dev enp3s0
ip link set enp3s0 up
ip link set enp3s0 down
ip addr show enp3s0
ip route add default via 192.168.1.1
ip route add 10.0.0.0/8 via 192.168.1.254
ip route del default via 192.168.1.1
Tutte le modifiche con ip sono temporanee — perse al riavvio!
Networking in Linux — ITS Academy
4. Configurazione persistente
Debian — /etc/network/interfaces
Ubuntu — Netplan /etc/netplan/*.yaml
iface enp3s0 inet static
address 192.168.1.100
netmask 255.255.255.0
gateway 192.168.1.1
dns-nameservers 8.8.8.8
addresses: [192.168.1.100/24]
via: 192.168.1.1
systemctl restart networking
Best practice: usare file dedicati nelle directory .d/ — non modificare i file di configurazione base (come per MariaDB)
Networking in Linux — ITS Academy
5. Risoluzione dei nomi (DNS)
(ping google.com)
/etc/nsswitch.conf
ordine: files → dns
mappature locali
/etc/resolv.conf
/etc/resolv.conf
127.0.0.1 localhost
192.168.1.10 server-web.lan
192.168.1.20 db.lan
nameserver 8.8.8.8
nameserver 1.1.1.1
Con systemd-resolved: /etc/resolv.conf è un symlink gestito automaticamente — modificarlo direttamente potrebbe non avere effetto.
Networking in Linux — ITS Academy
6. Diagnostica di rete — sequenza logica
Interfaccia attiva?
Raggiungo il gateway?
ping -c 4 192.168.1.1
Internet raggiungibile (per IP)?
ping -c 4 8.8.8.8
dig google.com / nslookup google.com
Altri strumenti:
traceroute / tracepath | ss -tuln / ss -tulnp | tcpdump -i enp3s0
Networking in Linux — ITS Academy
7. Porte e servizi comuni
ss -tulnp # mostra porte in ascolto con nome del processo
MySQL / MariaDB
Networking in Linux — ITS Academy

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_networking_linux.md*
