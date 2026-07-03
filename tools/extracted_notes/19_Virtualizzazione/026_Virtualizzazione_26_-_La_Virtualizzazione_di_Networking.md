# Virtualizzazione 26 - La Virtualizzazione di Networking

Fonte: `Virtualizzazione 26 - La Virtualizzazione di Networking.pdf`

DOCENTE

Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]

Unità Formativa

Elementi di Virtualizzazione

Argomento

La Virtualizzazione della Rete (Networking)

Il Modello ISO OSI

P. Belloni | 

2

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

➢Viceversa,

l’instradamento del traffico è necessario quando comunicano due nodi

appartenenti a due reti virtuali diverse, anche se attestati alla stessa rete fisica.

➢Segrega il traffico di gestione (incluso il network broadcast) all’interno della singola rete

virtuale, evitando che si propaghi in altre reti.

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P. Belloni | 

3

La Virtualizzazione delle Rete 2/4

Rete Fisica

• Composta da:

▪ adattatori di rete;
▪ switch;
▪ router;
▪ bridge;
▪ ripetitori e hub.

• Fornisce connettività tra:

▪ server fisici che ospitano hypervisor;
▪ server fisici e client;
▪ server fisici e sistemi di storage.

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P. Belloni | 

4

La Virtualizzazione delle Rete 3/4

Rete di VM
• Si trova all’interno dei serve fisici.
• È composta da switch logici chiamati
switch virtuali, con funzione simile
agli switch fisici.

• Fornisce

connettività

tra

all’interno di un server fisico.
al

connettività

• Fornisce

dell’hypervisor.

VM

kernel

• Connette alla rete fisica.

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P. Belloni | 

5

La Virtualizzazione delle Rete 4/4

• La rete di VM e la rete fisica sono virtualizzate per creare delle reti virtuali (p. es. Virtual Local

Area Network VLAN o Virtual Storage Area Network VSAN)

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P. Belloni | 

6

Virtual Networking della VM 1/4

P. Belloni | 

7

Virtual Networking della VM 2/4

• Creare sottoreti virtuali mediante switch di rete virtuali interni ed

esterni.

• Una rete virtuale è una rete privata definita dal software in un

ambiente virtuale.

• Uno switch di rete virtuale esterno consente di instradare il traffico

verso la rete esterna.

• Uno switch di rete virtuale interno non gestisce il traffico verso la
rete esterna. Viene usato per la costituzione di sottoreti virtuali.

•

•

•

•

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

•

senza una connessione a una scheda di rete fisica, la VM3 non può
essere vista, tanto meno attaccata, da una fonte esterna.

• VM1 funge da firewall e, con pratiche di sicurezza appropriate,

protegge i dati contenuti nell'altra VM.

P. Belloni | 

8

Virtual Networking della VM 3/4

• Rispetto alla slide precedente, aggiunto un
ulteriore switch virtuale per separare due
reti.

• Possono essere diverse organizzazioni
aziendali che richiedono spazi di
rete
separati in cui lavorare (es: la produzione è
separata dal test e dallo sviluppo).

• Questa architettura migliora inoltre le
prestazioni riducendo il traffico su ogni
segmento e migliora la sicurezza limitando
l'accesso a ciascuna area.

• Una terza macchina virtuale viene aggiunta
all'host e può comunicare solo con il nuovo
switch virtuale esterno.

P. Belloni | 

9

Virtual Networking della VM 4/4

• Nel caso il traffico dati dello storage viaggi
su una rete, è necessario allocare una
larghezza di banda adeguata per evitare
problemi di prestazioni.

• Ad esempio dedicando schede di rete
fisiche per il traffico dello storage, come
mostrato in figura.

P. Belloni | 

10

Le Metodologie per la Virtualizzazione della Rete

1. Basata sul SO dello switch fisico.

• Il SO deve avere una specifica funzionalità per la virtualizzazione della rete.

2. Basata sull’hypervisor.

▪ Una opzione è che l’hypervisor disponga di funzionalità integrate di networking e

virtualizzazione della rete.

❖Per creare switch virtuali e per configurare su quelli delle reti virtuali.

▪ In alternativa, l’hypevisor utilizza software di una terza parte, al fine di fornire

funzionalità di networking e virtualizzazione della rete.

❖Il software della terza parte viene installato sopra l’hypervisor.
❖Questo software rimpiazza le funzionalità di networking native dell’hypervisor.

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P. Belloni | 

11

I Benefici della Virtualizzazione di Rete

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P. Belloni | 

12

Infrastruttura di rete in un VDC

• L’infrastruttura di rete di un Virtual Data Center (VDC) include componenti di rete sia fisica che
virtuale. Questi componenti sono connessi gli uni agli altri, per abilitare il flusso di traffico di
rete.

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P. Belloni | 

13

Connessione di Rete e Flusso di Traffico: Esempio 1

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P. Belloni | 

14

Connessione di Rete e Flusso di Traffico: Esempio 2

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P. Belloni | 

15

Connessione di Rete e Flusso di Traffico: Esempio 3

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P. Belloni | 

16

I componenti della Rete Virtuale: Virtual NIC 

• Collega le VM al virtual switch.

▪ Il guest OS invia il traffico di I/O al VNIC utilizzando un driver, esattamente

come avviene per un NIC fisico.

• Il VNIC invia il traffico di I/O, in forma di pacchetti Ethernet, al virtual switch.
• Ha un unico MAC address e IP address. L’hypervisor genera il MAC address del

VNIC al momento della creazione della VM.

• Supporta lo standard Ethernet come un NIC fisico.

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P. Belloni | 

17

[I componenti della Rete Virtuale: Virtual HBA] 

• Abilita l’acceso di una VM al disco FC RDM/LUN assegnato alla VM stessa.
• Viene configurato usando la tecnologia N_Port ID Virtualization (NPIV).

▪ Un singolo FC HBA fisico o una porta CAN (N_Port) funziona come N porte
virtuali multiple, ognuna con il proprio world wide name (WWN, un indirizzo
univoco a 64-bit).

• Il kernel dell’hypervisor utilizza NPIV per instanziare N_porte virtuali, assegnadole

alle VM.

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P. Belloni | 

18

I componenti della Rete Virtuale: Virtual Switch 1/4 

• È uno switch logico che lavora al livello 2 della pila OSI e supporta il protocollo

Ethernet.

• Si trova all’interno di un server fisico.
• Viene creato e configurato usando l’hypervisor.
• Conserva una tabella con gli indirizzi MAC al fine di forwardare i pacchetti.

▪ MAC address table: MAC address + porta.

• Indirizza il traffico di rete verso/dalle VM e il kernel di hypervisor.

▪ VM verso VM internamente al server fisico.
▪ VM verso rete fisica.
▪ Hypervisor kernel: IP storage, VM migration e traffico di gestione.

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P. Belloni | 

19

I componenti della Rete Virtuale: Virtual Switch 2/4 

• Un virtual switch può essere connesso a diversi NIC fisici.

▪ La connessione a NIC diversi abilita il load balancing ed il failover del traffico

outbound.

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P. Belloni | 

20

I componenti della Rete Virtuale: Virtual Switch 3/4 

• Un virtual switch può non essere connesso ad alcun NIC fisico.

▪ In questo caso, indirizza il traffico di VM all’interno del server fisico (es.

firewall).

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P. Belloni | 

21

I componenti della Rete Virtuale: Virtual Switch 4/4 

• Non c’è mai connessione diretta tra virtual switch (peculiarità di Vmware; in altre
parole, VMware implementa un “single-tier networking”. Come conseguenza il
protocollo di spanning Tree per prevenire loop non serve) .

• Tuttavia il traffico può essere trasferito tra virtual switch attraverso le VM a questi

attestate.

• I NIC fisici permettono ai virtual switch di collegarsi alla rete fisica, per questo

motivo un NIC fisico non è condiviso tra diversi virtual switch.

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P. Belloni | 

22

Virtual Switch: porte e gruppi di porte

• Tipi di porte del virtual switch:

❑Hypervisor kernel port: garantiscono connettività al kernel di hypervisor;
❑VM port: forniscono connettività ai virtual NIC;
❑Uplink port: garantiscono connettività al NIC fisico. Un virtual switch è in grado di trasferire

dati ad una rete fisica solo se uno o più NIC fisici sono conessi alle sue uplink port.

• VM port group: raggruppare le porte delle VM è un meccanismo per applicare le stesse politiche

di rete (policy) a tutte le VM del Gruppo, invece di configurarle singolarmente su ogni porta.
▪ Esempi di politiche: sicurezza, load balancing, failover tra PNIC, limitazioni di banda.

• Le VM collegate ad un VM port group condividono la stessa configurazione.
▪ Evita di configurare le policy individualmente su ogni porta di VM.

VM port

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P. Belloni | 

23

Virtual Switch Distribuito

• È possible aggregare più virtual switch istanziati su diversi server fisici: questo
crea uno switch virtuale distribuito, che funziona come un singolo virtual switch.
• Solitamente, gli switch virtuali distribuiti permettono 1. di gestire in modo
centralizzato la rete di VM e 2. di mantenere le stesse politiche di rete in caso di
migrazione di VM tra server fisici.

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P. Belloni | 

24