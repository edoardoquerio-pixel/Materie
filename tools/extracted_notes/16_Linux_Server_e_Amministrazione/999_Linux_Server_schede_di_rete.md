# Linux Server schede di rete

Fonte: `Linux Server schede di rete.pdf`

DOCENTE 

Wolfgang Cecchin 

UNITA’ FORMATIVA 

Linux Server 

ARGOMENTO 

Impostazione schede di rete 

 
 
 
 
 
 
Eventualmente fare uno snapshot della macchina virtuale. 

La macchina dovrebbe avere già una scheda di rete NAT. 

Impostare una seconda scheda di rete “solo host”. 

Fare una copia del file interfaces: 

$ sudo /etc/network/interfaces /etc/network/interfaces.bk 

Modificate il file interfaces: 

$ sudo nano /etc/network/interfaces 

Cambiare il file in modo che contenga queste righe 
(non modificare l’interfaccia di loopback, cioè lo, 
queste righe vanno aggiunte in fondo): 

# The primary network interface 
allow-hotplug enp0s3 
iface enp0s3 inet dhcp 
# This is an autoconfigured IPv6 interface 
iface enp0s3 inet6 auto 

Spiegazioni: 

• 

• 

allow-hotplug enp0s3: abilita l'interfaccia se detectata (es. USB, PCI hotplug) o all'avvio. Se 
non c'è auto, non parte automaticamente al boot.manpages.debian+1 

iface enp0s3 inet dhcp: IPv4 via DHCP (chiede IP/gateway/DNS al server DHCP, es. 
VirtualBox NAT assegna 10.0.2.15). 

• 

iface enp0s3 inet6 auto: IPv6 automatico (SLAAC/RA, senza indirizzo statico). 

$ sudo ifdown enp0s3 
$ sudo ifup enp0s3