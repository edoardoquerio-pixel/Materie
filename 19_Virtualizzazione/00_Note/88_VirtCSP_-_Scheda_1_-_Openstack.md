# VirtCSP - Scheda 1 - Openstack

**File:** `VirtCSP - Scheda 1 - Openstack.pdf`
**Tipo:** `.pdf`
**Dimensione:** 259.4 KB
**Ultima modifica:** 02/07/2026 09:25

---

 
 
C2 General 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
 
DOCENTE Paolo Belloni 
Unità Formativa Sistemi di Virtualizzazione 
Argomento Scheda 1 – Openstack CPU, RAM e rete  

2 
 
L’obiettivo è comprendere il comportamento reale delle risorse di sistema 
all’interno di una VM.  
 
1. Accesso alla VM tramite Floating IP e SSH  
Quando una VM viene creata in OpenStack, riceve un indirizzo IP privato (es. 
10.0.0.x). Questo indirizzo è valido solo all’interno della rete virtuale e non è 
raggiungibile. Per accedere da remoto devi quindi assegnare un Floating IP.  
OBIETTIVO  
Collegarsi alla VM da remoto comprendendo la differenza tra rete privata e 
accesso pubblico.  
 Passo 1 — Creazione Floating IP:  
- Aprire Horizon  
- Andare in Project → Network → Floating IP  
- Cliccare ‘Allocate IP to Project’  
RISULTATO: viene assegnato un IP pubblico.  
 
Passo 2 — Associazione IP:  
- Cliccare ‘Associate’  
- Selezionare la VM e la porta  
RISULTATO: la VM ottiene un IP pubblico.  
 
Passo 3 — Verifica Security Group:  
- Abilitare porta TCP 22  
RISULTATO: SSH permesso.  
 
Passo 4 — Connessione:  
ssh ubuntu@IP-PUBBLICO -i mykey.pem  
mykey.pem viene generato quando si crea istanza: è fondamentale salvare 
la chiave in locale e posizionarsi nella cartella che contiene il file .pem 
quando si fa ssh. 

3 
 
RISULTATO: accesso alla shell Linux.  
INTERPRETAZIONE: senza Floating IP una VM cloud non è raggiungibile 
dall’esterno. 
 
2. Analisi della CPU  
Di seguito alcune considerazioni sulla gestione della CPU da parte di 
Openstack. Si ricorda che Openstack lavora ad un livello più alto rispetto 
l’hypervisor. 
Passo 1 — Identificare CPU:  
cat /proc/cpuinfo  
RISULTATO: numero di vCPU presenti.  
INTERPRETAZIONE: rappresentano le CPU virtuali disponibili.  
Esegui il comando cat /proc/cpuinfo. Questo file contiene informazioni 
dettagliate sulla CPU. Conta quante volte compare la voce 'processor': 
quella è la quantità di CPU virtuali assegnate alla macchina.  
 
Passo 2 — Monitoraggio:  
htop  
OSSERVARE: barre CPU e colori.  
INTERPRETAZIONE:  
- Verde: utilizzo da processi  
- Rosso: sistema  
- Giallo: attesa I/O  
Avvia htop per monitorare la CPU in tempo reale. Osserva le barre colorate: il 
verde indica lavoro eseguito dalle applicazioni, il rosso attività del sistema e il 
giallo eventuale attesa di risorse.  
 
Passo 3 — Generare carico:  
stress --cpu 4 &  
jobs  
RISULTATO: vengono creati processi CPU.  
 
Passo 4 — Osservazione:  
htop  

4 
 
RISULTATO: CPU al 100%.  
INTERPRETAZIONE: più processi competono per CPU.  
Genera carico con stress --cpu 4 &. Ora osserva di nuovo htop: vedrai le CPU 
completamente occupate. Questo significa che i processi stanno 
competendo per la CPU.  
 
Passo 5 — Load average:  
uptime  
RISULTATO: load > numero CPU.  
INTERPRETAZIONE: coda di processi in attesa.  
Usa uptime per leggere il valore 'load average'. Se il valore supera il numero 
di CPU disponibili, significa che il sistema è sovraccarico.  
 
3. Analisi della Memoria  
Esegui free -m per vedere lo stato della memoria. Osserva la quantità di RAM 
disponibile.  
Passo 1 — Stato memoria:  
free -m  
RISULTATO: memoria disponibile.  
 
Passo 2 — Stress memoria:  
stress --ram 1 --vm-bytes 1G  
RISULTATO: consumo RAM.  
Esegui stress --ram 1 --vm-bytes 1G per occupare memoria. Ripeti free -m e 
osserva la differenza.  
 
Passo 3 — Verifica:  
free -m  
RISULTATO: memoria libera diminuisce.  
INTERPRETAZIONE: memoria finita = sistema rallenta.  
Quando la memoria libera diminuisce, il sistema deve gestire le risorse in 
maniera più complessa. Se la memoria finisce, si verificano rallentamenti.  
 

5 
 
4. Analisi della Rete  
Passo 1 — ARP table:  
ip neigh  
RISULTATO: elenco IP e MAC noti. Esegui ip neigh per visualizzare la tabella 
ARP, che associa indirizzi IP a indirizzi MAC.  
 
Passo 2 — Pulizia:  
sudo ip neigh flush all  
RISULTATO: tabella vuota.  
Pulisci la tabella con sudo ip neigh flush all e verifica che sia vuota. La tabella 
resta vuota per pochi secondi, perche lamacchina subito contatta il 
gateway per verificare la connettivita: per vedere tabella arp vuota 
ocnviene dare insieme sudo … e ip neigh. 
 
Passo 3 — Ping esterno:  
ping 8.8.8.8  
RISULTATO: connessione Internet.  
Esegui ping 8.8.8.8 e poi ping verso un IP interno. Successivamente controlla 
nuovamente ip neigh.  
 
Passo 4 — Ping interno:  
ping 10.0.0.5  
RISULTATO: comunicazione rete privata.  
 
Passo 5 — Verifica ARP:  
ip neigh  
RISULTATO: nuove entry.  
INTERPRETAZIONE: ARP si popola solo dopo comunicazione.  
 
La tabella ARP si riempie nuovamente. Questo dimostra che il sistema 
apprende dinamicamente i dispositivi presenti sulla rete. Openstack e 
hypervisor lavorano a livello 2.  
