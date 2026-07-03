# Lab - Identifying IPv4 Addresses

Fonte: `Lab - Identifying IPv4 Addresses.pdf`

Laboratorio: Individuazione degli indirizzi IPv4 

Obiettivi 

Sezione 1: Individuare gli indirizzi IPv4 

Sezione 2: Classificare gli indirizzi IPv4 

Introduzione e scenario 

In questa attività di laboratorio si esaminerà la struttura degli indirizzi del protocollo Internet versione 4 (IPv4). 
Si identificheranno i diversi tipi di indirizzi IPv4 e i componenti che formano l'indirizzo, come la porzione rete e 
dell'host, nonché la subnet mask. I tipi di indirizzi analizzati includono quelli pubblici, privati, unicast e 
multicast. 

Risorse necessarie 

• Dispositivo con accesso a Internet 
• Facoltativo: calcolatore degli indirizzi IPv4 

Sezione 1: 

Individuare gli indirizzi IPv4 

Nella Sezione 1 vengono forniti alcuni esempi di indirizzi IPv4 e si completeranno le tabelle con le 
informazioni appropriate. 

Fase 1: Analizzare la tabella riportata di seguito e identificare la porzione rete e dell'host degli 

indirizzi IPv4 forniti. 

Le prime due righe mostrano alcuni esempi di come completare la tabella. 

Sigle della tabella: 
N = tutti gli 8 bit di un ottetto sono nella porzione rete dell'indirizzo 
n = un bit nella porzione rete dell'indirizzo 
H = tutti gli 8 bit di un ottetto sono nella porzione dell'host dell'indirizzo 
h = un bit nella porzione dell'host dell'indirizzo 

Indirizzo 
IP/prefisso 

Rete/host 

N, n = rete, H, h = host 

Subnet mask 

Indirizzo di rete 

192.168.10.10/24 

N.N.N.H 

255.255.255.0 

192.168.10.0 

10.101.99.17/23 

N.N.nnnnnnnh.H 

255.255.254.0 

10.101.98.0 

209.165.200.227/27 

172.31.45.252/24 

10.1.8.200/26 

172.16.117.77/20 

10.1.1.101/25 

209.165.202.140/27 

192.168.28.45/28 

© 2017 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Questo documento contiene informazioni pubbliche di Cisco. 

Pagina 1 di 3 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Laboratorio: Individuazione degli indirizzi IPv4 

Fase 2: Analizzare la tabella seguente ed elencare l'intervallo degli indirizzi host e di broadcast 

sulla base di una coppia rete/maschera del prefisso. 

Le prima riga mostra un esempio di come completare la tabella. 

Indirizzo 
IP/prefisso 

Indirizzo del primo 
host 

Indirizzo dell'ultimo 
host 

Indirizzo di broadcast 

192.168.10.10/24 

192.168.10.1 

192.168.10.254 

192.168.10.255 

10.101.99.17/23 

209.165.200.227/27 

172.31.45.252/24 

10.1.8.200/26 

172.16.117.77/20 

10.1.1.101/25 

209.165.202.140/27 

192.168.28.45/28 

Sezione 2: Classificare gli indirizzi IPv4 

Nella Sezione 2 si identificheranno e classificheranno diversi esempi di indirizzi IPv4. 

Fase 1: Analizzare la tabella riportata di seguito e identificare il tipo di indirizzo (rete, host, 

multicast o indirizzo di broadcast). 

Le prima riga mostra un esempio di come completare la tabella. 

Indirizzo IP 

Subnet mask 

Tipo di indirizzo 

10.1.1.1 

255.255.255.252 

host 

192.168.33.63 

255.255.255.192 

239.192.1.100 

255.252.0.0 

172.25.12.52 

255.255.255.0 

10.255.0.0 

255.0.0.0 

172.16.128.48 

255.255.255.240 

209.165.202.159 

255.255.255.224 

172.16.0.255 

255.255.0.0 

224.10.1.11 

255.255.255.0 

© 2017 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Questo documento contiene informazioni pubbliche di Cisco. 

Pagina 2 di 3 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Laboratorio: Individuazione degli indirizzi IPv4 

Fase 2: Analizzare la tabella riportata di seguito e identificare l'indirizzo come pubblico o 

privato. 

Indirizzo IP/prefisso 

Pubblico o privato 

209.165.201.30/27 

192.168.255.253/24 

10.100.11.103/16 

172.30.1.100/28 

192.31.7.11/24 

172.20.18.150/22 

128.107.10.1/16 

192.135.250.10/24 

64.104.0.11/16 

Fase 3: Analizzare la tabella riportata di seguito e identificare se la coppia indirizzo/prefisso è 

un indirizzo dell'host valido. 

Indirizzo 
IP/prefisso 

Indirizzo dell'host 
valido? 

Motivo 

127.1.0.10/24 

172.16.255.0/16 

241.19.10.100/24 

192.168.0.254/24 

192.31.7.255/24 

64.102.255.255/14 

224.0.0.5/16 

10.0.255.255/8 

198.133.219.8/24 

Approfondimento 

Perché dovremmo continuare a studiare l'indirizzamento IPv4 se lo spazio degli indirizzi IPv4 disponibile è 
vuoto? 

_____________________________________________________________________________________ 

_____________________________________________________________________________________ 

© 2017 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Questo documento contiene informazioni pubbliche di Cisco. 

Pagina 3 di 3