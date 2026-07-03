# 9) Microsoft Azure - Compute su Azure - VM, immagini e dimensionamento

**File:** `9) Microsoft Azure - Compute su Azure - VM, immagini e dimensionamento.pptx`
**Tipo:** `.pptx`
**Dimensione:** 73.4 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Compute su Azure: VM, immagini e dimensionamento (4 ore)

---

Compute su Azure
Virtual Machine, immagini e dimensionamento

---

Da dove ripartiamo
•  abbiamo già letto una VM dal lato rete: NIC, Public IP, NSG, RDP
•  abbiamo già aperto il wizard di creazione fino a Review + create
•  oggi cambiamo domanda: non solo chi raggiunge la VM, ma quale VM stiamo scegliendo
•  il punto è leggere le scelte di compute prima ancora di creare

---

La VM come risorsa compute
•  una Virtual Machine è compute IaaS
•  scegli tu sistema operativo, dimensione, immagine e dischi
•  Azure ti fornisce infrastruttura fisica, rete, regioni e opzioni di disponibilità
•  rispetto a App Service o Functions hai più controllo, ma anche più gestione

---

Le scelte che pesano subito
Scelta
Cosa decide
Regione
dove gira la VM
Immagine
il punto di partenza del sistema
Size
vCPU e RAM disponibili
Dischi
prestazioni e costo di base
Disponibilità
continuità del servizio
•  la rete la conosciamo già: qui la rileggiamo come contesto della VM

---

Come leggere il nome di una size
Esempio
Lettura rapida
B2s
serie economica, 2 vCPU
D2s_v5
uso generale, 2 vCPU, generazione v5
E2s_v5
stessa taglia, ma più orientata alla memoria
•  la serie indica la famiglia della VM
•  il numero dà l'ordine di grandezza
•  s indica supporto a Premium SSD

---

Famiglie da ricordare
Famiglia
Quando la guardo
B
carichi leggeri o intermittenti
D
uso generale
E
applicazioni che chiedono più RAM
F
più CPU rispetto alla memoria
•  non serve imparare tutto il catalogo
•  servono pochi riferimenti per non scegliere a caso

---

vCPU e RAM: la domanda giusta
•  se il collo di bottiglia è l'elaborazione, guardo prima le vCPU
•  se l'app tiene molto in memoria, guardo prima la RAM
•  non esiste la VM migliore in assoluto
•  la scelta giusta dipende dal carico, non dal nome più grande

---

Immagine, OS disk e data disk
•  l'immagine è il modello iniziale della VM
•  decide sistema operativo e software di partenza
•  il OS disk nasce dall'immagine
•  i data disk si aggiungono dopo, per dati e applicazioni

---

Da dove arrivano le immagini
•  il Marketplace raccoglie immagini Microsoft e di terze parti
•  esempi tipici: Windows Server, Ubuntu, immagini con software già presente
•  un'immagine pronta accelera la partenza
•  più l'immagine è ricca, più va capita bene prima di usarla

---

Regione, vincoli e scelta reale
•  la regione non si sceglie solo per abitudine
•  contano policy, disponibilità del servizio e vicinanza
•  con sottoscrizioni limitate conviene verificare prima opzioni davvero disponibili
•  nel wizard la prima lettura utile è: Region, Image, Size

---

Availability Set e Availability Zone
Se voglio...
Guardo...
proteggermi dal guasto di host o rack
Availability Set
separazione fisica tra data center nella stessa regione
Availability Zone
•  la zona è una separazione fisica più forte
•  non tutte le regioni offrono le zone
•  una VM singola resta una VM singola: la continuità cresce con più istanze

---

La VM che abbiamo già
•  in Overview leggo nome, resource group, regione e stato
•  in Size leggo famiglia, vCPU, RAM e cambio taglia se serve
•  in Disks distinguo OS disk ed eventuali data disk
•  in Networking ritrovo NIC, IP e NSG, cioè il pezzo che conosciamo già
•  la stessa VM si legge da compute, storage e rete insieme

---

Nel wizard VM, cosa guardare davvero
•  Basics: subscription, resource group, nome, regione
•  Image e Size: sistema di partenza e potenza della macchina
•  Disks: tipo di OS disk e impostazioni principali
•  Networking: VNet, subnet, accesso pubblico o privato
•  Review + create: riepilogo finale delle scelte

---

Quando ha senso scegliere una VM
•  quando ti serve controllo sull'OS
•  quando devi installare software specifico
•  quando il caso non entra bene in un servizio PaaS
•  quando vuoi capire fino in fondo che cosa gira e dove gira

---

Chiusura del blocco
•  una VM non si sceglie dal nome più vistoso
•  contano insieme immagine, size, dischi, regione e disponibilità
•  la rete dice se la raggiungi; il compute dice che macchina stai usando
•  il passo successivo è leggere meglio dischi, prestazioni e scalabilità delle VM
