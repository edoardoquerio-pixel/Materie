# networking linux doc

## Panoramica
Lezione — Linux Server | ITS Academy

## Argomenti trattati
Linux, Configurazione, Reti, Docker, API REST

---
## Appunti

Networking in Linux
Lezione — Linux Server | ITS Academy
1. Introduzione
La configurazione di rete è una competenza fondamentale per chi amministra un server
Linux. In questa lezione vedremo come funziona lo stack di rete, come configurare
interfacce, routing e risoluzione dei nomi, e come diagnosticare problemi di connettività.
2. Concetti fondamentali
Interfacce di rete
Un'interfaccia di rete è il punto di contatto tra il sistema operativo e la rete fisica (o virtuale).
In Linux le interfacce seguono una nomenclatura predittiva (introdotta con systemd/udev):
eth0, enp3s0, ens33
virbr0, docker0
Ethernet fisica
Loopback (127.0.0.1)
Bridge virtuali
Il loopback è un'interfaccia speciale: tutto il traffico inviato a 127.0.0.1 rimane all'interno della
macchina stessa. È usato da servizi che comunicano localmente (es. PHP → MySQL).
Il modello TCP/IP a strati
HTTP, FTP, SSH, DNS
TCP (affidabile), UDP (veloce)
IP, ICMP, routing
Ethernet, ARP, MAC address
3. Comandi essenziali
Networking in Linux — ITS Academy
Comando ip — visualizzare le interfacce
Il comando ip sostituisce il vecchio ifconfig ed è lo strumento principale per la gestione della
rete in Linux moderno.
ip addr show # mostra tutte le interfacce
ip addr show enp3s0 # mostra solo una interfaccia
ip addr add 192.168.1.100/24 dev enp3s0 # assegna IP temporaneo
ip addr del 192.168.1.100/24 dev enp3s0 # rimuove un IP
ip link set enp3s0 up # attiva interfaccia
ip link set enp3s0 down # disattiva interfaccia
Il routing determina come i pacchetti raggiungono la destinazione. La tabella di routing dice
al kernel quale gateway usare per raggiungere una determinata rete.
ip route show # mostra la tabella di routing
ip route add default via 192.168.1.1 # default gateway
ip route add 10.0.0.0/8 via 192.168.1.254 # rotta statica
ip route del default via 192.168.1.1 # elimina rotta
Tutte le modifiche con ip sono temporanee: vengono perse al riavvio del sistema.
4. Configurazione persistente
Debian — /etc/network/interfaces
iface enp3s0 inet static
address 192.168.1.100
netmask 255.255.255.0
gateway 192.168.1.1
dns-nameservers 8.8.8.8 1.1.1.1
systemctl restart networking
Ubuntu moderno — Netplan (/etc/netplan/*.yaml)
addresses: [192.168.1.100/24]
via: 192.168.1.1
addresses: [8.8.8.8, 1.1.1.1]
Best practice: come per MariaDB, preferire i file dedicati nelle directory .d/ invece di
modificare i file di configurazione base.
Networking in Linux — ITS Academy
5. Risoluzione dei nomi (DNS)
Quando si esegue ping google.com il sistema deve tradurre il nome in un indirizzo IP.
Questo processo si chiama risoluzione DNS.
Ordine di risoluzione — /etc/nsswitch.conf
hosts: files dns
Il sistema controlla prima /etc/hosts, poi interroga il server DNS configurato.
/etc/hosts — mappature statiche
127.0.0.1 localhost
192.168.1.10 server-web.lan server-web
192.168.1.20 db.lan
Utile in laboratorio per simulare un DNS senza installarne uno.
/etc/resolv.conf — server DNS
nameserver 8.8.8.8
nameserver 1.1.1.1
Attenzione: su sistemi con systemd-resolved, questo file è un symlink gestito
automaticamente.
6. Diagnostica di rete
La sequenza logica per diagnosticare un problema di connettività parte sempre dal livello più
• Passo 1 — L'interfaccia è attiva?
ip addr show # verificare la presenza di UP e di un indirizzo IP
• Passo 2 — Raggiungo il gateway?
ping -c 4 192.168.1.1
• Passo 3 — Raggiungo Internet per IP?
ping -c 4 8.8.8.8
• Passo 4 — Il DNS funziona?

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_networking_linux_doc.md*
