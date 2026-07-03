# Lezione 9

## Panoramica
Compute su Azure: VM, immagini e dimensionamento (4 ore)

## Argomenti trattati
Azure, Reti, API REST, Data Analytics

---
## Appunti

### Slide 1
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
Compute su Azure: VM, immagini e dimensionamento (4 ore)
### Slide 2
Compute su Azure
Virtual Machine, immagini e dimensionamento
### Slide 3
Da dove ripartiamo
•  abbiamo già letto una VM dal lato rete: NIC, Public IP, NSG, RDP
•  abbiamo già aperto il wizard di creazione fino a Review + create
•  oggi cambiamo domanda: non solo chi raggiunge la VM, ma quale VM stiamo scegliendo
•  il punto è leggere le scelte di compute prima ancora di creare
### Slide 4
La VM come risorsa compute
•  una Virtual Machine è compute IaaS
•  scegli tu sistema operativo, dimensione, immagine e dischi
•  Azure ti fornisce infrastruttura fisica, rete, regioni e opzioni di disponibilità
•  rispetto a App Service o Functions hai più controllo, ma anche più gestione
### Slide 5
Le scelte che pesano subito
dove gira la VM
il punto di partenza del sistema
vCPU e RAM disponibili
prestazioni e costo di base
continuità del servizio
•  la rete la conosciamo già: qui la rileggiamo come contesto della VM
### Slide 6
Come leggere il nome di una size
serie economica, 2 vCPU
uso generale, 2 vCPU, generazione v5
stessa taglia, ma più orientata alla memoria
•  la serie indica la famiglia della VM
•  il numero dà l'ordine di grandezza
•  s indica supporto a Premium SSD
### Slide 7
Famiglie da ricordare
Quando la guardo
carichi leggeri o intermittenti
applicazioni che chiedono più RAM
più CPU rispetto alla memoria
•  non serve imparare tutto il catalogo
•  servono pochi riferimenti per non scegliere a caso
### Slide 8
vCPU e RAM: la domanda giusta
•  se il collo di bottiglia è l'elaborazione, guardo prima le vCPU
•  se l'app tiene molto in memoria, guardo prima la RAM
•  non esiste la VM migliore in assoluto
•  la scelta giusta dipende dal carico, non dal nome più grande
### Slide 9
Immagine, OS disk e data disk
•  l'immagine è il modello iniziale della VM
•  decide sistema operativo e software di partenza
•  il OS disk nasce dall'immagine
•  i data disk si aggiungono dopo, per dati e applicazioni
### Slide 10
Da dove arrivano le immagini
•  il Marketplace raccoglie immagini Microsoft e di terze parti
•  esempi tipici: Windows Server, Ubuntu, immagini con software già presente
•  un'immagine pronta accelera la partenza
•  più l'immagine è ricca, più va capita bene prima di usarla
### Slide 11
Regione, vincoli e scelta reale
•  la regione non si sceglie solo per abitudine
•  contano policy, disponibilità del servizio e vicinanza
•  con sottoscrizioni limitate conviene verificare prima opzioni davvero disponibili
•  nel wizard la prima lettura utile è: Region, Image, Size
### Slide 12
Availability Set e Availability Zone
proteggermi dal guasto di host o rack
Availability Set
separazione fisica tra data center nella stessa regione
Availability Zone
•  la zona è una separazione fisica più forte
•  non tutte le regioni offrono le zone
•  una VM singola resta una VM singola: la continuità cresce con più istanze
### Slide 13
La VM che abbiamo già
•  in Overview leggo nome, resource group, regione e stato

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 009_9_Microsoft_Azure_-_Compute_su_Azure_-_VM_immagini_e_dimensionamento.md*
