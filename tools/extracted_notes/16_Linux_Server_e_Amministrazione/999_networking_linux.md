# networking linux

Fonte: `networking linux.pdf`

DOCENTE

Wolfgang Cecchin

UNITA’ FORMATIVA

ARGOMENTO

Linux Server

Networking

Networking
in Linux

Configurazione, diagnostica e gestione della rete

Linux Server | ITS Academy

Agenda

•
•
•
•
•
•
•
•

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

Applicazione

HTTP · FTP · SSH · DNS

Trasporto

TCP (affidabile) · UDP (veloce)

Rete

IP · ICMP · Routing

Collegamento

Ethernet · ARP · MAC

Networking in Linux — ITS Academy

Interfacce di rete — nomenclatura predittiva

eth0 / enp3s0

wlan0 / wlp2s0

Ethernet fisica

Wireless

lo

virbr0 / docker0

Loopback — 127.0.0.1 (locale)

Bridge virtuale

⚑ Il loopback è usato da servizi che comunicano localmente — es. PHP → MySQL (127.0.0.1:3306)

Networking in Linux — ITS Academy

3. Il comando ip — operazioni principali

Sostituisce il vecchio ifconfig — strumento principale in Linux moderno

Visualizzare

Modificare (temporaneo)

ip addr add 192.168.1.10/24 dev enp3s0
ip addr del 192.168.1.10/24 dev enp3s0
ip link set enp3s0 up
ip link set enp3s0 down

ip addr show
ip addr show enp3s0
ip route show
ip link show

Routing

ip route add default via 192.168.1.1
ip route add 10.0.0.0/8 via 192.168.1.254
ip route del default via 192.168.1.1

Tutte le modifiche con ip sono temporanee — perse al riavvio!

Networking in Linux — ITS Academy

4. Configurazione persistente

Debian — /etc/network/interfaces

Ubuntu — Netplan /etc/netplan/*.yaml

auto enp3s0
iface enp3s0 inet static

address 192.168.1.100
netmask 255.255.255.0
gateway 192.168.1.1
dns-nameservers 8.8.8.8

network:

version: 2
ethernets:
enp3s0:

addresses: [192.168.1.100/24]
routes:

- to: default

via: 192.168.1.1

systemctl restart networking

netplan apply

Best practice: usare file dedicati nelle directory .d/ — non modificare i file di configurazione base (come per MariaDB)

Networking in Linux — ITS Academy

5. Risoluzione dei nomi (DNS)

Applicazione
(ping google.com)

→

/etc/nsswitch.conf
ordine: files → dns

→

/etc/hosts
mappature locali

→

Server DNS
/etc/resolv.conf

/etc/hosts

/etc/resolv.conf

127.0.0.1 localhost
192.168.1.10 server-web.lan
192.168.1.20 db.lan

nameserver 8.8.8.8
nameserver 1.1.1.1
search lan

Con systemd-resolved: /etc/resolv.conf è un symlink gestito automaticamente — modificarlo direttamente potrebbe non avere effetto.

Networking in Linux — ITS Academy

6. Diagnostica di rete — sequenza logica

1

2

3

4

Interfaccia attiva?

ip addr show

Raggiungo il gateway?

ping -c 4 192.168.1.1

Internet raggiungibile (per IP)?

ping -c 4 8.8.8.8

DNS funziona?

dig google.com / nslookup google.com

Altri strumenti:

traceroute / tracepath | ss -tuln / ss -tulnp | tcpdump -i enp3s0

Networking in Linux — ITS Academy

7. Porte e servizi comuni

ss -tulnp # mostra porte in ascolto con nome del processo

Porta

Protocollo

Servizio

22

25

53

80

443

3306

5432

TCP

TCP

TCP/UDP

TCP

TCP

TCP

TCP

SSH

SMTP

DNS

HTTP

HTTPS

MySQL / MariaDB

PostgreSQL

Networking in Linux — ITS Academy

8. Esercizio pratico — Studio Fotografico Bianchi

Scenario:

Il server Linux dello studio ha due interfacce: enp3s0 (LAN 192.168.10.0/24) e enp4s0 (Internet via DHCP)

Obiettivi:

Domande di riflessione:

•

•
•
•
•

Assegnare a enp3s0 l'IP statico 192.168.10.1/24 in modo 
persistente
Aggiungere in /etc/hosts le voci per i client della LAN
Verificare la connettività con ping verso i client
Verificare le porte in ascolto con ss -tulnp
Usare traceroute per analizzare il percorso verso 8.8.8.8

•

•

•

Perché è importante configurare l'IP in modo 
persistente?
Cosa succede se il gateway predefinito non è 
configurato correttamente?
Qual è la differenza pratica tra /etc/hosts e un 
server DNS?

Networking in Linux — ITS Academy

Riepilogo

Visualizzare interfacce

Configurare IP (temp.)

Tabella di routing

ip addr show

ip addr add IP/MASK dev IF

ip route show

Conf. persistente Debian

/etc/network/interfaces

Conf. persistente Ubuntu

/etc/netplan/*.yaml

Risoluzione locale

Server DNS

Porte in ascolto

Cattura traffico

/etc/hosts

/etc/resolv.conf

ss -tuln / ss -tulnp

tcpdump -i enp3s0