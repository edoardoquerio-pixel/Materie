# 19 - Virtualizzazione — Tutte le Sessioni


---

## Sessione 1: VirtCSP - Scheda 1 - Openstack


Unità Formativa
Sistemi di Virtualizzazione
Scheda 1 – Openstack CPU, RAM e rete
L’obiettivo è comprendere il comportamento reale delle risorse di sistema
all’interno di una VM.
1. Accesso alla VM tramite Floating IP e SSH
Quando una VM viene creata in OpenStack, riceve un indirizzo IP privato (es.
10.0.0.x). Questo indirizzo è valido solo all’interno della rete virtuale e non è
raggiungibile. Per accedere da remoto devi quindi assegnare un Floating IP.
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
RISULTATO: accesso alla shell Linux.
INTERPRETAZIONE: senza Floating IP una VM cloud non è raggiungibile
2. Analisi della CPU
Di seguito alcune considerazioni sulla gestione della CPU da parte di
Openstack. Si ricorda che Openstack lavora ad un livello più alto rispetto
Passo 1 — Identificare CPU:
cat /proc/cpuinfo
RISULTATO: numero di vCPU presenti.
INTERPRETAZIONE: rappresentano le CPU virtuali disponibili.
Esegui il comando cat /proc/cpuinfo. Questo file contiene informazioni
dettagliate sulla CPU. Conta quante volte compare la voce 'processor':
quella è la quantità di CPU virtuali assegnate alla macchina.
Passo 2 — Monitoraggio:
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
RISULTATO: vengono creati processi CPU.
Passo 4 — Osservazione:
RISULTATO: CPU al 100%.
INTERPRETAZIONE: più processi competono per CPU.
Genera carico con stress --cpu 4 &. Ora osserva di nuovo htop: vedrai le CPU
completamente occupate. Questo significa che i processi stanno
competendo per la CPU.
Passo 5 — Load average:
RISULTATO: load > numero CPU.
INTERPRETAZIONE: coda di processi in attesa.
Usa uptime per leggere il valore 'load average'. Se il valore supera il numero
di CPU disponibili, significa che il sistema è sovraccarico.
3. Analisi della Memoria
Esegui free -m per vedere lo stato della memoria. Osserva la quantità di RAM
Passo 1 — Stato memoria:
RISULTATO: memoria disponibile.
Passo 2 — Stress memoria:
stress --ram 1 --vm-bytes 1G
RISULTATO: consumo RAM.
Esegui stress --ram 1 --vm-bytes 1G per occupare memoria. Ripeti free -m e
osserva la differenza.
Passo 3 — Verifica:
RISULTATO: memoria libera diminuisce.
INTERPRETAZIONE: memoria finita = sistema rallenta.
Quando la memoria libera diminuisce, il sistema deve gestire le risorse in
maniera più complessa. Se la memoria finisce, si verificano rallentamenti.
4. Analisi della Rete
Passo 1 — ARP table:
RISULTATO: elenco IP e MAC noti. Esegui ip neigh per visualizzare la tabella

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 2: Virtualizzazione 26 - Infrastruttura virtuale


Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]
Unità Formativa
Sistemi di Virtualizzazione
Infrastruttura Virtuale
Infrastruttura Virtuale
Componenti software (softwarizzate, astratte) che abilitano l’esecuzione di
applicazioni senza disporre di una macchina fisica
• Macchine Virtuali
• Cloud Service Provider
I livelli di Virtualizzazione 1/4
A che livello eseguire la virtualizzazione?
componenti del sistema.
▪ Interfaccia tra HW e SW (user ISA: istruzioni
macchina non privilegiate, invocabili da ogni
▪ Interfaccia tra HW e SW (system ISA: istruzioni
Sistema: Application Binary
▪ Chiamate di libreria: Application Programming
• Obiettivo della virtualizzazione
▪ Imitare il comportamento di queste interfacce
I livelli di Virtualizzazione 2/4
Cinque livelli di virtualizzazione
• Livello ISA (Instruction Set Architecture).
▪ Si implementa emulando l’ISA, attraverso una traduzione di ogni singola istruzione oppure
attraverso dynamic binary translation (converte in blocchi piuttosto che istruzione per
• Livello Hardware (aka HW Abstraction Layer HAL oppure system VM) .
▪ Bastato su hypervisor.
• Livello Sistema Operativo (aka containers).
• Livello Run-time Library.
• Livello applicazione utente (aka process VM).
I livelli di Virtualizzazione 3/4
I livelli di Virtualizzazione 4/4
VM – Virtualizzazione a livello HW
La Virtualizzazione a livello HW (System Level VM)
• La virtualizzazione a livello HW o system level VM si ottiene attraverso un hypervisor.
• Un Hypervisor è un software di virtualizzazione che permette di eseguire diversi SO
interagendo direttamente con le
contemporaneamente sulla stessa macchina fisica,
risorse fisiche del server. L’hypervisor ha due componenti:
▪ un Kernel – un SO per sistemi operativi;
▪ un Virtual Machine Monitor (VMM), che astrae l’HW per apparire come una
macchina fisica (con CPU, memoria e I/O propri). A volte VMM sinonimo di
• Host – piattaforma base sulla quale sono eseguite le varie VM.
▪ Composta da macchina fisica, opzionalmente SO host, hypervisor.
• Guest – tutto quanto si trova all’interno di una VM.
▪ SO guest e applicazioni eseguite dentro la VM.
La Virtualiz. a livello HW e l’Allocazione delle Risorse
Classificazione della Virtualizzazione a livello HW
Esistono diversi tipi di virtualizzazione a livello HW (o system level virtualization),
distinti in base a:
❖Dove si istanza l’hypervisor:
▪ System hypervisor, o di sistema, chiamato anche type-1, native or bare-metal
▪ Hosted hypervisor, o ospitato, chiamato anche type-2 hypervisor.
❖Come si virtualizzano le istruzioni sensibili e non virtualizzabili.
▪ Full virtualization:
▪ Software-assisted;
▪ Hardware-assisted.
▪ Para-virtualization.
Classificazione della Virtualizzazione a livello HW
Hypervisor di Sistema vs Ospitato 1/2
In quale livello dell’architettura di sistema si colloca l’hypervisor?
➢Direttamente sull’hardware: hypervisor di sistema
➢Sopra il SO host: hypervisor ospitato
Hypervisor di sistema
Hypervisor ospitato
Hypervisor di Sistema vs Ospitato 2/2
• Hypervisor di sistema (type-1): eseguito direttamente sull’hw, offre funzionalità di
virtualizzazione integrate in un SO semplificato (è, di fatto, un SO).
▪ L’hypervisor può avere un’architettura a micro-kernel (solo funzioni di base, no
device driver) o monolitica.
▪ Richiede HW certificato.
▪ Esempi: Xen, KVM (non univocamente riconosciuto), VMware ESX, Hyper-V.
• Hypervisor ospitato (type-2): eseguito sul SO host, accede alle risorse hw tramite le
chiamate di sistema del SO host.
▪ Interagisce con il SO host tramite l’ABI ed emula l’ISA di hw virtuale per i SO guest.
▪ Vantaggio: può usare il SO host per gestire le periferiche ed utilizzare servizi di basso
livello (es. scheduling delle risorse).
▪ Vantaggio: non occorre modificare il SO guest.
▪ Svantaggio: degrado delle prestazioni rispetto a hypervisor di sistema
▪ Esempi: Bochs, Parallels Desktop, VirtualBox.
Full-Virtualization vs Para-Virtualization

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 3: Virtualizzazione 26 - La Virtualizzazione di Mem


Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]
Unità Formativa
Elementi di Virtualizzazione
La virtualizzazione della memoria
Richiami sulla memoria 1/4
• La memoria principale può agire come “cache” per la memoria di massa (dischi,
• Si parla in questo caso di memoria virtuale:
▪ I programmi sono compilati rispetto ad uno spazio di indirizzamento virtuale, diverso
da quello fisico;
▪ Il sistema di memoria virtuale traduce gli indirizzi virtuali in indirizzi fisici.
▪ illusione di avere una maggiore memoria fisica;
▪ meccanismi di protezione (gli spazi virtuali di programmi diversi mappati su spazi
fisici differrenti).
Elementi di Virtualizzazione |
Richiami sulla memoria 2/4
• La memoria e organizzata in modo
gerarchico (a livelli):
• Liv. 1: memoria più veloce(costosa).
• Liv. N: memoria più lenta (economica).
• Il processore indirizza tutta la memoria
di Liv. N, ma accede direttamente solo
• La pagine cercate si trovano al livello 1
con maggiore probabilità.
Elementi di Virtualizzazione |
Richiami sulla memoria 3/4
• Ad ogni istante solo una parte delle pagine di memoria “virtuale” è presente nella
memoria fisica.
• Quando la pagina cercata non è in memoria e deve essere letta da disco, si parla di page
• Il costo dei page fault è estremamente elevato (milioni di cicli), e questo influenza molte
scelte (dimensioni della pagina 4, 16, 32, 64 KB, gestione software).
• L’indirizzo virtuale si suddivide in Virtual Page Address + offset.
• Il Virtual Page Address indirizza le entry di una tabella, detta Page Table, che contiene
informazioni sulla presenza / validità delle pagine in memoria.
• In un sistema di memoria virtuale, ogni accesso alla memoria richiede due accessi: prima
alla Page Table e quindi alla memoria fisica.
• Per ridurre questo overhead si sfrutta un meccanismo detto TLB (Translation Lookaside
Buffer), una sorta di cache della Page Table. La TLB contiene copia delle entry della Page
Table riferite recentemente, e, come la cache, può sfruttare l’associatività per ridurre i
Elementi di Virtualizzazione |
Richiami sulla memoria 4/4
Elementi di Virtualizzazione |
La virtualizzazione della memoria 1/2
• In un ambiente non-virtualizzato:
▪ Utilizzando le page table, si passa dalla memoria virtuale alla memoria fisica.
▪ Si parla di one-level mapping.
• In un ambiente virtualizzato:
▪ Tutte le VM condividono la stessa memoria fisica e hypervisor deve ripartirla tra le
▪ Si parla di two-level mapping: dalla memoria virtuale guest alla memoria fisica guest
alla memoria fisica host.
• Terminologia:
➢Guest virtual memory: memoria visibile alle applicazioni; spazio di indirizzamento
virtuale continuo presentato dal guest OS alle applicazioni.
➢Guest physical memory: memoria visibile al guest OS.
➢Host physical memory: memoria hw reale visibile ad hypervisor.
Elementi di Virtualizzazione |
La virtualizzazione della memoria 2/2
• Two-level memory mapping:
• Per passare dalla guest virtual memory alla host physical memory serve un mapping
Guest VA (virtual address) → guest PA (physical address) → host MA (machine
• Guest physical address ≠ host machine address.
Elementi di Virtualizzazione |
Shadow Page-Table SPT 1/2
• Per evitare la riduzione delle prestazioni derivanti da extra memory mapping,
l’hypervisor utilizza delle shadow page-table (SPT) al fine di accelerare il mapping.
▪ Mapping diretto guest virtual su host physical memory address.
• SPT mappa direttamente l’indirizzo della guest virtual
memory nell’indirizzo della host physical memory.
▪ Il guest OS conserva la sua PT per memoria virtuale nello
spazio di guest physical memory assegnato.
▪ Per ogni dato in guest physical memory,
dovrebbe mapparne l’indirizzo nel dato corrispondente
di host physical memory.
▪ SPT mappa direttamente l’indirizzo della guest virtual
memory nell’indirizzo della host physical memory.
▪ L’hypervisor deve mantenere aggiornata la SPT ad ogni
cambio che il guest OS attua sulle sue PT.
Elementi di Virtualizzazione |
Shadow Page-Table SPT 2/2
• L’hypervisor utilizza l’hw di Translation Lookaside Buffer (TLB) per eseguire il
mapping diretto della memoria virtuale nella memoria di macchina fisica,

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 4: Virtualizzazione 26 - La Virtualizzazione di Networking


Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]
Unità Formativa
Elementi di Virtualizzazione
La Virtualizzazione della Rete (Networking)
Il Modello ISO OSI
La Virtualizzazione delle Rete 1/4
Network Virtualization
È il processo di segmentazione logica o raggruppamento di reti fisiche che porta alla
creazione di entità logiche single o multiple ma indipendenti, chiamate reti virtuali.
➢Una rete virtuale appare come una rete fisica ai nodi a questa connessi.
➢Il processo di virtualizzazione delle reti abilita la condivisione delle risorse di rete.
➢La virtualizzazione abilita il raggruppamento funzionale di nodi con gli stessi requisiti in
una unica rete virtuale, indipendentemente dalla loro localizzazione geografica.
➢Permette la comunicazione diretta tra nodi appartenenti alla stessa rete virtuale, senza
necessità di instradare i pacchetti, anche se attestati a reti fisiche diverse.
l’instradamento del traffico è necessario quando comunicano due nodi
appartenenti a due reti virtuali diverse, anche se attestati alla stessa rete fisica.
➢Segrega il traffico di gestione (incluso il network broadcast) all’interno della singola rete
virtuale, evitando che si propaghi in altre reti.
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
La Virtualizzazione delle Rete 2/4
▪ adattatori di rete;
▪ ripetitori e hub.
• Fornisce connettività tra:
▪ server fisici che ospitano hypervisor;
▪ server fisici e client;
▪ server fisici e sistemi di storage.
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
La Virtualizzazione delle Rete 3/4
• Si trova all’interno dei serve fisici.
• È composta da switch logici chiamati
switch virtuali, con funzione simile
agli switch fisici.
all’interno di un server fisico.
dell’hypervisor.
• Connette alla rete fisica.
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
La Virtualizzazione delle Rete 4/4
• La rete di VM e la rete fisica sono virtualizzate per creare delle reti virtuali (p. es. Virtual Local
Area Network VLAN o Virtual Storage Area Network VSAN)
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
Virtual Networking della VM 1/4
Virtual Networking della VM 2/4
• Creare sottoreti virtuali mediante switch di rete virtuali interni ed
• Una rete virtuale è una rete privata definita dal software in un
ambiente virtuale.
• Uno switch di rete virtuale esterno consente di instradare il traffico
verso la rete esterna.
• Uno switch di rete virtuale interno non gestisce il traffico verso la
rete esterna. Viene usato per la costituzione di sottoreti virtuali.
VM1: due NIC virtuali VNIC1 e VNIC2, ognuna connessa ad uno switch
virtuale e quindi a ciascuna delle reti virtuali.
Le richieste che provengono da VNIC3 verranno trasmesse alla rete
fisica e al mondo esterno. Le risposte a tale richiesta seguono il
percorso al contrario, attraverso la NIC fisica, attraverso lo switch
virtuale esterno e di nuovo alla NIC virtuale della VM.
Le richieste da VNIC2 saranno inoltrare allo switch virtuale interno per
la comunicazione con altre macchine virtuali.
La VM3 può effettuare richieste solo tramite lo switch virtuale interno.
Questa è una strategia comune in un ambiente virtuale per proteggere
applicazioni e server da attacchi indesiderati:
senza una connessione a una scheda di rete fisica, la VM3 non può
essere vista, tanto meno attaccata, da una fonte esterna.
• VM1 funge da firewall e, con pratiche di sicurezza appropriate,
protegge i dati contenuti nell'altra VM.
Virtual Networking della VM 3/4
• Rispetto alla slide precedente, aggiunto un
ulteriore switch virtuale per separare due
• Possono essere diverse organizzazioni
aziendali che richiedono spazi di
separati in cui lavorare (es: la produzione è
separata dal test e dallo sviluppo).
• Questa architettura migliora inoltre le
prestazioni riducendo il traffico su ogni
segmento e migliora la sicurezza limitando
l'accesso a ciascuna area.
• Una terza macchina virtuale viene aggiunta
all'host e può comunicare solo con il nuovo
switch virtuale esterno.
Virtual Networking della VM 4/4

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 5: Virtualizzazione 26 - La Virtualizzazione


Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]
Unità Formativa
Sistemi di Virtualizzazione
Lez. 01 - Virtualizzazione
Esempio | La Macchina Host o Server Fisico
▪ Ciascuno dei due server IBM Flex
x440 è equipaggiato come segue:
➢24 core x86 a 2,7 GHz;
➢192 GB di RAM;
➢1 Fiber Channel HBA (Host Bus
Adapter) 16 Gbps;
➢8 porte Ethernet da 1 Gbps.
▪ La SAN si basa su SAN Brocade e
su un'unità IBM StorWize V7000
con 20 dischi SAS da 300 GB e 4
▪ Flex FC 5022 è adattatore SAN
montato sul server.
Virtualizzazione |
Esempio | I Server Virtuali
▪ Le macchine virtuali costituiscono tre ambienti:
➢ Development/Acceptance
▪ La potenza richiesta per le macchine (virtuali) è
stata stimata in un esercizio di sizing.
▪ La capacità complessiva del
superiore alla somma delle macchine virtuali
configurate (33 core/cpu).
▪ È possibile osservare che la potenza delle
macchine di Acceptance/Dev e Test/Perf è simile o
uguale a quella dell’ambiente di Produzione.
▪ Questo perché la virtualizzazione consente di
presentare al richiedente, cioè la VM, la potenza
necessaria quando questa è necessaria.
▪ Nel caso di un ambiente fisico tutta la potenza
dovrebbe essere stata resa SEMPRE disponibile.
Virtualizzazione |
Cloud Computing
▪ Definizione secondo U.S. National Institute of Standards and Technology (NIST).
“Cloud è un modello di accesso via rete da qualsiasi luogo, comodo e on-demand,
ad un insieme di risorse condivise – reti, server, dispositive di memorizzazione,
applicazioni e servizi – che possono essere forniti e rilasciati rapidamente, con
minimo costo di gestione o interazione con il fornitore del Servizio”.
▪ Caratteristiche dell’elaborazione in Cloud:
✓On demand (variazione di risorse "agile").
✓Shared resource pooling (risorse condivise).
✓Rapid elasticity (variazione di risorse "immediata").
✓Measured service (misura uso risorse / fatturaz. a consumo).
✓Broad network access.
✓High availability, disaster recovery (SLA).
Virtualizzazione |
▪ Un data center è una struttura utilizzata per ospitare sistemi
componenti associati, come sistemi di telecomunicazione e archiviazione.
▪ Generalmente include alimentatori ridondanti o di backup, connessioni di
comunicazione dati ridondati, controlli ambientali (ad esempio, condizionamento
dell'aria, sistemi antincendio) e vari dispositivi di sicurezza.
▪ I grandi data center sono edifici su scala industriale che utilizzano tanta elettricità
quanto una piccola città.
Virtualizzazione |
Data Center – Un Sistema complesso
Virtualizzazione |
Data Center – Non solo Computing
Virtualizzazione |
Data Center - Condizionamento
Virtualizzazione |
Osservatorio Data Center del POLIMI
ll settore dei data center in Italia sta vivendo una fase di crescita senza
precedenti, come evidenziato dai dati dell’Osservatorio Data Center del
Politecnico di Milano. Nel 2024, la potenza energetica totale dei data
center italiani ha raggiunto i 513 MW IT, segnando un incremento del
17% rispetto all’anno precedente. Questo sviluppo è stato alimentato da
investimenti massicci: nel biennio 2023-2024 sono stati spesi 5 miliardi
di euro per la costruzione e l’allestimento di nuove infrastrutture,
mentre per il biennio 2025-2026 sono previsti ulteriori 10,1 miliardi di
Virtualizzazione |
Data Center Classico (CDC)
▪ Un Data Center Classico (Classic DC CDC) contiene risorse fisiche di Information
Technology che includono la risorse computazionali, la rete e lo storage.
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
Virtualizzazione |
Business applications
▪ E-mail, Enterprise Resource Planning (ERP), Decision Support System (DSS),

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 6: Virtualizzazione 26 - VM e Openstack


Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]
Unità Formativa
Sistemi di Virtualizzazione
Macchina Virtuale e Openstack
Infrastruttura Virtuale
Componenti software (softwarizzate, astratte) che abilitano l’esecuzione di
applicazioni senza disporre di una macchina fisica
• Macchine Virtuali
• Cloud Service Provider
Come si realizza il Cloud Computing?
▪ Attraverso software non troppo diverso da hypervisor, ma creato per
gestire il cloud.
▪ Orchestratore di macchina virtuali.
▪ Openstack: piattaforma software per il management di un cloud.
▪ Progetto iniziato nel 2010 dalla collaborazione tra Rackspace e la
Come si realizza il Cloud Computing? (1)
▪ Si avvale delle sue
funzionalità per creare
un cloud di macchine
Come si realizza il Cloud Computing? (2)
Libvirt per gestire eterogeneità
▪ Si avvale di libvirt:
▪ Permette di interagire con
Gestione delle Risorse in Pool
La Gestione delle Risorse (Resource Management)
Resource Management
Un processo per allocare, a favore delle macchine virtuali (VM), le risorse di una
macchina fisica o di un cluster di macchine fisiche, al fine di ottimizzare l’utilizzo
complessivo delle risorse.
• A cosa serve la gestione delle risorse?
▪ Controlla l’uso delle risorse.
▪ Impedisce che una singola VM monopolizzi le risorse.
▪ Alloca le risorse opportunamente, in base alle priorità assegnate alle varie VM.
• Le risorse devono essere messe in pool (Resource Pooling), allo scopo di gestirle
“centralmente”.
• Risorse = CPU, memoria, rete e storage.
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
Il Resource Pooling
Resource Pooling
È una astrazione logica delle risorse fisiche aggregate, che ne abilita la gestione
• Un pool è creato a partire da una macchina fisica o da un insieme di machine fisiche (cluster).
▪ Questo resource pool di partenza è definito parent resource pool.
• A partire dal parent resource pool (iniziale), gli Amministratori di sistema possono allocare le
risorse ad una applicazione o a delle VM.
▪ Le risorse allocate, a partire dal parent pool, per una specifica applicazione o alla singola VM si definiscono
child resource pool.
• Tre indicatori vengono usati per controllare le risorse consumate dai diversi pool o dalle VM.
• Si parla di Key Performance Indicator (KPI). Questi sono:
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
Il Resource Pooling: un esempio
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
Share, Limit e Reservation
• Share Limit e Reservation sono dei parametri (variabili) che controllano le risorse allocate
ed utilizzate da un child resource pool o da una VM.
▪ Quantità di CPU o memoria che una VM o un child pool può avere, rispetto al totale delle
risorse (di CPU o memoria) del parent pool.
▪ Individua la priorità di una VM o child pool.
▪ Massima quantità di CPU o memoria che una VM o un child pool può consumare.
▪ Configurato alla creazione della VM, si può modificare solo a VM spenta.
▪ Quantità di CPU o memoria riservata per una VM o per un child pool.
▪ Una VM non viene attivata, se la quanità di risorse definite dalla reservation non sono
▪ Se la VM non utilizza tutte le risorse riservate, quelle libere vengono allocate ad altre
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
L’ottimizzazione delle risorse di CPU
• Allocare le risorse di una CPU in modo efficiente e appropriato è fondamentale.
• Le moderne CPU sono equipaggiate con core multipli e con hyper-threading.
▪ I processori multi-core hanno,
in una singola CPU (circuito integrato o socket),
diverse unità di processamento (processing unit, a.k.a. core).
▪ L’hyper-threading fa apparire una CPU fisica come due o più CPU logiche.
• L’hypervisor definisce e alloca le CPU virtuali sulla CPU fisiche (analogamente a
come un SO assegna ai diversi processi – o thread – il tempo di CPU).
• L’hypervisor supporta le funzionalità di multi-core, hyper-threading e CPU load-
balancing (bilanciamento del carico) per ottimizzare le risorse della CPU.
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
CPU: pCPU, L-CPU, vCPU
I processori Multi-Core
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
L’hyper-threading
Un thread o thread di esecuzione, in informatica, è una

*[Contenuto troncato — vedi file originale per dettagli completi]*


---
*Totale: 6 sessioni generate il 02/07/2026*