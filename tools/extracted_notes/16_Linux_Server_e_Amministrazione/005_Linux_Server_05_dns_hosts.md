# Linux Server 05 dns hosts

Fonte: `Linux Server 05 dns hosts.pdf`

DOCENTE 

UNITA’ 
FORMATIVA 

Wolfgang Cecchin 

Linux Server 

ARGOMENTO 

DNS, file hosts 

 
 
 
 
 
 
 
 
 
Lo scopo di assegnare dei nomi agli indirizzi IP è quello di rendere più facile la 
memorizzazione per le persone. In verità, un indirizzo IP identifica un'interfaccia di rete 
associata con un dispositivo come una scheda di rete. Poiché ogni macchina può avere più 
schede e più interfacce per ogni scheda, un singolo computer può avere più nomi nel 
sistema dei nomi di dominio. 

https://debian-handbook.info/browse/it-IT/stable/sect.hostname-name-service.html 

Il servizio DNS 

https://it.wikipedia.org/wiki/Nome_di_dominio 

https://it.wikipedia.org/wiki/Domain_Name_System 

Interrogare il DNS 

$ dig google.com 

The most important section is the ANSWER section: 

• The first column lists the name of the server that was queried 
• The second column is the Time to Live, a set timeframe after which the record is 

refreshed 

• The third column shows the class of query – in this case, “IN” stands for Internet 
• The fourth column displays the type of query – in this case, “A” stands for an A 

(address) record 
 The final column displays the IP address associated with the domain name 

• 

Tipi di record DNS - Wikipedia 

2 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Ricordarsi: 

A NAME = Address Name 
CNAME = Canonical Name 
MX = Mail Server 

3 

 
 
 
 
Associare un nome a un IP 

E’ possibile associare il nome di un dominio a un server (o meglio a un IP) attraverso il 
servizio DNS. 

E’ possibile tuttavia informare la macchina locale dell’associazione di un nome dominio e 
IP attraverso il file “hosts”. 

Posizione su Linux / Mac: 
/etc/hosts 

Nota bene: molti file di configurazione importanti in Linux si trovano nella directory /etc 

Posizione su Windows: 
c:\Windows\System32\Drivers\etc\hosts 

Sintassi del file hosts: 
127.0.0.1 localhost 
192.168.0.1 mioSito.example.com mioSito 
127.0.1.1 mercoledi.local 

4