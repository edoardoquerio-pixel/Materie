# networking linux doc

**File:** `networking linux doc.pdf`
**Tipo:** `.pdf`
**Dimensione:** 3934.6 KB
**Ultima modifica:** 02/07/2026 09:22

---

Networking in Linux — ITS Academy 
 
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
 
Nome Tipo 
eth0, enp3s0, ens33 Ethernet fisica 
wlan0, wlp2s0 Wireless 
lo Loopback (127.0.0.1) 
virbr0, docker0 Bridge virtuali 
 
Il loopback è un'interfaccia speciale: tutto il traffico inviato a 127.0.0.1 rimane all'interno della 
macchina stessa. È usato da servizi che comunicano localmente (es. PHP → MySQL). 
Il modello TCP/IP a strati 
Strato Protocolli 
Applicazione HTTP, FTP, SSH, DNS 
Trasporto TCP (affidabile), UDP (veloce) 
Rete IP, ICMP, routing 
Collegamento Ethernet, ARP, MAC address 
 
3. Comandi essenziali 

Networking in Linux — ITS Academy 
Comando ip — visualizzare le interfacce 
Il comando ip sostituisce il vecchio ifconfig ed è lo strumento principale per la gestione della 
rete in Linux moderno. 
ip addr show           # mostra tutte le interfacce 
ip addr show enp3s0    # mostra solo una interfaccia 
ip addr add 192.168.1.100/24 dev enp3s0   # assegna IP temporaneo  
ip addr del 192.168.1.100/24 dev enp3s0   # rimuove un IP 
ip link set enp3s0 up  # attiva interfaccia 
ip link set enp3s0 down  # disattiva interfaccia 
Routing 
Il routing determina come i pacchetti raggiungono la destinazione. La tabella di routing dice 
al kernel quale gateway usare per raggiungere una determinata rete. 
ip route show           # mostra la tabella di routing 
ip route add default via 192.168.1.1        # default gateway  
ip route add 10.0.0.0/8 via 192.168.1.254  # rotta statica 
ip route del default via 192.168.1.1        # elimina rotta 
     Tutte le modifiche con ip sono temporanee: vengono perse al riavvio del sistema. 
4. Configurazione persistente 
Debian — /etc/network/interfaces 
auto enp3s0 
iface enp3s0 inet static 
    address 192.168.1.100 
    netmask 255.255.255.0 
    gateway 192.168.1.1 
    dns-nameservers 8.8.8.8 1.1.1.1 
Per applicare: 
systemctl restart networking 
Ubuntu moderno — Netplan (/etc/netplan/*.yaml) 
network: 
  version: 2 
  ethernets: 
    enp3s0: 
      addresses: [192.168.1.100/24] 
      routes: 
        - to: default 
          via: 192.168.1.1 
      nameservers: 
        addresses: [8.8.8.8, 1.1.1.1] 
Per applicare: 
netplan apply 
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
127.0.0.1    localhost 
192.168.1.10 server-web.lan server-web 
192.168.1.20 db.lan 
Utile in laboratorio per simulare un DNS senza installarne uno. 
/etc/resolv.conf — server DNS 
nameserver 8.8.8.8 
nameserver 1.1.1.1 
search lan 
Attenzione: su sistemi con systemd-resolved, questo file è un symlink gestito 
automaticamente. 
6. Diagnostica di rete 
La sequenza logica per diagnosticare un problema di connettività parte sempre dal livello più 
basso: 
• Passo 1 — L'interfaccia è attiva? 
ip addr show    # verificare la presenza di UP e di un indirizzo IP  
• Passo 2 — Raggiungo il gateway? 
ping -c 4 192.168.1.1 
• Passo 3 — Raggiungo Internet per IP? 
ping -c 4 8.8.8.8 
• Passo 4 — Il DNS funziona? 
ping -c 4 google.com 
nslookup google.com 
dig google.com 
Altri strumenti 
Comando Utilizzo 
traceroute google.com Traccia il percorso dei pacchetti 
ss -tuln Connessioni attive e porte in ascolto 
ss -tulnp Come sopra + nome del processo 
tcpdump -i enp3s0 Cattura traffico su un'interfaccia 
tcpdump -i enp3s0 port 80 Cattura solo traffico sulla porta 80 
 

Networking in Linux — ITS Academy 
7. Porte e servizi 
Ogni servizio di rete ascolta su una porta. Le porte fino a 1023 sono privilegiate e richiedono 
i permessi di root. 
Porta Protocollo Servizio 
22 TCP SSH 
25 TCP SMTP 
53 TCP/UDP DNS 
80 TCP HTTP 
443 TCP HTTPS 
3306 TCP MySQL/MariaDB 
5432 TCP PostgreSQL 
 
ss -tulnp    # mostra porte in ascolto con nome del processo 
8. Esercizio pratico — Studio Fotografico Bianchi 
Il server Linux dello studio ha due interfacce di rete: 
• enp3s0 — collegata alla LAN interna (192.168.10.0/24) 
• enp4s0 — collegata al provider Internet (IP via DHCP) 
 
Obiettivi: 
• Assegnare a enp3s0 l'IP statico 192.168.10.1/24 in modo persistente 
• Aggiungere in /etc/hosts le voci per i client della LAN 
• Verificare la connettività verso i client con ping 
• Verificare le porte in ascolto con ss -tulnp 
• Usare traceroute per analizzare il percorso verso 8.8.8.8 
 
Domande di riflessione: 
• Perché è importante configurare l'IP in modo persistente? 
• Cosa succede se il gateway predefinito non è configurato correttamente? 
• Qual è la differenza pratica tra /etc/hosts e un server DNS? 
9. Riepilogo 
Concetto Comando / File chiave 
Visualizzare interfacce ip addr show 
Configurare IP (temporaneo) ip addr add IP/MASK dev IF 
Visualizzare routing ip route show 
Configurazione persistente /etc/network/interfaces o Netplan 
Risoluzione locale /etc/hosts 

Networking in Linux — ITS Academy 
Server DNS /etc/resolv.conf 
Diagnostica connettività ping, traceroute, ss 
Cattura traffico tcpdump 
 
