# Virtualizzazione 26 - La Virtualizzazione

Fonte: `Virtualizzazione 26 - La Virtualizzazione.pdf`

DOCENTE

Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]

Unità Formativa

Sistemi di Virtualizzazione

Argomento

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
SSD da 250 GB.

▪ Flex FC 5022 è adattatore SAN

montato sul server.

Virtualizzazione | 

2

Esempio | I Server Virtuali

▪ Le macchine virtuali costituiscono tre ambienti:

➢ Produzione
➢ Test/Perf
➢ Development/Acceptance

▪ La potenza richiesta per le macchine (virtuali) è

stata stimata in un esercizio di sizing.

▪ La capacità complessiva del

fisico è
superiore alla somma delle macchine virtuali
configurate (33 core/cpu).

server

▪ È possibile osservare che la potenza delle
macchine di Acceptance/Dev e Test/Perf è simile o
uguale a quella dell’ambiente di Produzione.

▪ Questo perché la virtualizzazione consente di
presentare al richiedente, cioè la VM, la potenza
necessaria quando questa è necessaria.

▪ Nel caso di un ambiente fisico tutta la potenza
dovrebbe essere stata resa SEMPRE disponibile.

Virtualizzazione | 

3

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

4

Data Center

▪ Un data center è una struttura utilizzata per ospitare sistemi

informatici e

componenti associati, come sistemi di telecomunicazione e archiviazione.

▪ Generalmente include alimentatori ridondanti o di backup, connessioni di
comunicazione dati ridondati, controlli ambientali (ad esempio, condizionamento
dell'aria, sistemi antincendio) e vari dispositivi di sicurezza.

▪ I grandi data center sono edifici su scala industriale che utilizzano tanta elettricità

quanto una piccola città.

Virtualizzazione | 

5

Data Center – Un Sistema complesso

Virtualizzazione | 

6

Data Center – Non solo Computing

Virtualizzazione | 

7

Data Center - Condizionamento

Virtualizzazione | 

8

Osservatorio Data Center del POLIMI

ll settore dei data center in Italia sta vivendo una fase di crescita senza
precedenti, come evidenziato dai dati dell’Osservatorio Data Center del
Politecnico di Milano. Nel 2024, la potenza energetica totale dei data
center italiani ha raggiunto i 513 MW IT, segnando un incremento del
17% rispetto all’anno precedente. Questo sviluppo è stato alimentato da
investimenti massicci: nel biennio 2023-2024 sono stati spesi 5 miliardi
di euro per la costruzione e l’allestimento di nuove infrastrutture,
mentre per il biennio 2025-2026 sono previsti ulteriori 10,1 miliardi di
investimenti.

Virtualizzazione | 

9

Data Center Classico (CDC)

▪ Un Data Center Classico (Classic DC CDC) contiene risorse fisiche di Information

Technology che includono la risorse computazionali, la rete e lo storage.

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

Virtualizzazione | 

10

Applicazioni

Business applications
▪ E-mail, Enterprise Resource Planning (ERP), Decision Support System (DSS),

Data Warehouse (DW).
Management applications
▪ Resource management, performance tuning.
Data protection applications
▪ Backup, replication.
Security applications
▪ Autenticazione, antivirus.
➢Caratterisitche principali di I/O per una applicazione

✓Read intensive vs. write intensive
✓Sequential vs. random

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

Virtualizzazione | 

11

Database Management System

• Un database è un modo strutturato per memorizzare i dati in

tabelle logicamente organizzate e collegate tra loro.

➢ Un database aiuta a ottimizzare l’archiviazione e il recupero dei dati.
• Un Sistema di Gestione di Database (DBMS) è un insieme di
programmi che controllano la creazione, la manutenzione e l’uso
di un database.

➢ Il DBMS elabora la richiesta di dati di un’applicazione e istruisce il

sistema operativo per accedere ai dati appropriati.

➢ Il DBMS gestisce i dati in arrivo, li organizza e facilita la modifica o

l’estrazione dei dati da parte degli utenti o di altri programmi.

• Alcune soluzioni DBMS popolari sono MySQL, Oracle, SQL Server,

etc.

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

Virtualizzazione | 

12

Compute

Una risorsa che esegue le applicazioni con il supporto delle componenti
computazionali sottostanti.
▪ Consiste in componenti fisici (dispositivi hardware) che comunicano

tra loro utilizzando componenti logici (software e protocolli).

▪ Tre componenti fisici chiave: Unità di Elaborazione Centrale (CPU),

Memoria e dispositivi di Input/Output (I/O).

➢La memoria viene utilizzata per memorizzare i dati, sia in modo persistente

che temporaneo.

➢I dispositivi I/O consentono di inviare e ricevere dati da e verso un sistema di

calcolo. Questa comunicazione può essere di uno dei seguenti tipi:

✓ Comunicazioni utente-compute: gestite da dispositivi I/O di base, come la tastiera, il
mouse e il monitor. Questi dispositivi consentono agli utenti di inserire dati e visualizzare
i risultati delle operazioni.

✓ Comunicazioni

o
dall'adattatore host (host adapter) che collega un sistema di calcolo a un altro sistema di
calcolo/dispositivo di archiviazione.

compute-compute/archiviazione:

controller

gestite

host

dal

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

Virtualizzazione | 

13

HW | Esempi di Compute

• Laptop/desktop, blade server, complessi cluster di server, computer

mainframe, ecc.

• La tecnologia di blade server è comunemente utilizzata per

implementare il computer nei cDC.

• Sono stati sviluppati

in risposta alla crescente necessità di una

potenza di calcolo che non occupi molto spazio.

• Riducendo i costi e la complessità nel datacenter,

i blade server
consolidano le funzioni di alimentazione e di sistema in un unico
chassis integrato e consentono l'aggiunta di server come componenti
hot-pluggable.

• La tecnologia dei blade server aumenta notevolmente la densità dei
server, riduce i costi di alimentazione e raffreddamento, facilita
l'espansione dei server e semplifica la gestione del datacenter.

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

Virtualizzazione | 

14

HW | Esempi di Compute | Blade Server

Features and specifications
• Processors

✓ Up to two Intel Xeon 2.8 or 3.6 GHz / 800 MHz
✓ 1MB L2 Cache

• Memory

✓ Up to 8 GB PC2-3200
✓ Four slots
• Hard drives

Frequenza di clock = 
velocità cui il processore
esegue le istruzioni

✓ Up to Two 36.4 GB 10,000 rpm
✓ Ultra320 SCSI

• Networking

✓ Dual 10/100/1000 Ethernet

Broadcom 5704S

controller

/

• Video
✓ATI RadeonTM 7000M

Bus di Sistema = velocità
alla quale I dati vengono
trasferiti tra processore e 
RAM 

Virtualizzazione | 

15

Blade server IBM HS20

HW | Esempi di Compute | Blade Server

Virtualizzazione | 

16

HW | Server Clustering

• È il metodo di raggruppare due o più server (noti anche come nodi) e

farli lavorare insieme come un unico sistema.

• Questo garantisce che le applicazioni e le risorse mission-critical siano
altamente disponibili: più nodi vengono riuniti in un cluster per migliorare
la disponibilità e le prestazioni.

• Quando si verifica un guasto su un nodo in un cluster, le risorse vengono
reindirizzate e il carico di lavoro viene riassegnato a un altro nodo nel cluster.
• Il clustering si implementa con software che collega i nodi nel cluster
e fornisce una vista del sistema unico ai client che utilizzano il cluster
stesso.

• Questi nodi comunicano tra loro tramite una rete privata. La
comunicazione tra i nodi di un cluster tramite heartbeat consente al
servizio di clustering di rilevare i guasti dei nodi e i cambiamenti di
stato, e gestisce il cluster come un'unica entità.

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

Virtualizzazione | 

17

Storage

▪ È una risorsa che permette di

persistente, per un uso successivo.

immagazzinare i dati

in modalità

➢I dati creati da individui o aziende devono essere memorizzati in modo che siano

facilmente accessibili per ulteriori elaborazioni.

• I dispositivi progettati per memorizzare i dati sono chiamati dispositivi di

archiviazione o semplicemente storage.

• Il tipo di archiviazione utilizzato varia in base al tipo di dati ed alla velocità

con cui vengono creati e utilizzati.

➢Dispositivi come la memoria in un telefono cellulare o una fotocamera digitale, DVD,
CD-ROM e unità disco nei computer personali sono esempi di dispositivi di
archiviazione.

• Un dispositivo di archiviazione utilizza supporti magnetici, ottici o a stato

solido.

➢I dischi, i nastri e i dischetti utilizzano supporti magnetici.
➢I CD/DVD utilizzano supporti ottici per l'archiviazione.
➢La memoria flash rimovibile o le unità flash sono esempi di supporti a stato solido.

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

Virtualizzazione | 

18

Tipi di Storage

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

Virtualizzazione | 

19

Network | Il Modello ISO OSI

Virtualizzazione | 

20

Virtualizzazione

• T = Hardware reale (Target)
• V = Virtual, Software eseguibile su HW

H, detto Host

• S = SW originariamente sviluppato per

T

➢Non si vuole cambiare S.
➢HW T non è più disponibile.
➢V è meno costoso di T.
➢V è più flessibile di T.
➢V rende il sistema che esegue S più

sicuro.

Virtualizzazione | 

21

Virtualizzazione

• Livello alto di astrazione di un sistema
dettagli

che
dell’implementazione sottostante.

nasconde

i

• Astrazione di risorse computazionali:

❑si presenta all’utilizzatore una
vista logica diversa da quella
fisica.

• Come? Disaccoppiando l’architettura
ed il comportamento delle risorse hw
e sw percepiti dall’utente dalla loro
realizzazione fisica.

Vista Logica (sistema virtuale)

Tecnologie di Virtualizzazione

Sistema Reale
--- risorse HW e SW ---

Vista Fisica
(sistema reale)

Virtualizzazione | 

22

Virtualizzazione di Risorse

• Virtualizzazione

di

Risorse

computazionali di Sistema (hw + sw)

• Macchina Virtuale (VM), container

• Virtualizzazione di Storage

• Storage Area Network (SAN)

• Virtualizzazione di Rete

• Virtual LAN (VLAN), Virtual Private

Network (VPN)

• Virtualizzazione di Data Center

Virtualizzazione | 

23

Il Cloud

• La virtualizzazione è il primo
passo verso la creazione di
un'infrastruttura Cloud.

• Trasformare un Data Center
in un Data
(C-DC)
classico
(V-DC)
virtualizzato
Center
richiede la virtualizzazione degli
elementi principali del Data
Center.

graduale

alla
approccio
virtualizzazione
di
un'infrastruttura consente una
transizione agevole da C-DC a VDC.

• Un

Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

Virtualizzazione | 

24

Macchina Virtuale

• Una macchina virtuale (VM, Virtual
Machine, in contrapposizione ad una
macchina fisica o reale) permette di
rappresentare le risorse hw/sw di una
macchina diversamente dalla loro
realtà.

❖ Ad es.: risorse hw della VM (CPU, scheda di
rete, …) diverse dalle risorse fisiche della
macchina reale.

❖ Ad es.: risorse sw (sistema operativo, …)
diverse dalle risorse sw della macchina
reale.

• Una singola macchina fisica può
essere usata come differenti ambienti
di elaborazione.

❖ Molteplici VM su una singola macchina

fisica.

VM1

VM2

VMX

Layer di Virtualizzazione

Hardware

Virtualizzazione | 

25

Cenni Storici sulla Virtualizzazione 1/2

• Il concetto di VM è un’idea “vecchia”, essendo stato definito a metà degli anni ’60

in un contesto centralizzato.

➢Ideato per consentire al software legacy (esistente) di essere eseguito su
mainframe molto costosi e condividere in modo trasparente le (scarse) risorse
fisiche.

➢Fu uso per la prima volta sul mainframe IBM System/360-67, basato su un
emulatore che i programmatori usavano per sviluppare un sistema operativo
(simile nel principio ma molto diverso nella realizzazione dall’attuale
virtualizzazione).

• Negli anni ’80, con il passaggio ai PC, il problema della condivisione trasparente

delle risorse di calcolo viene risolto dai SO multitasking.

➢L’interesse per la virtualizzazione svanisce.

Virtualizzazione | 

26

3

6

5

2

1

4

IBM System/360-67

Virtualizzazione | 

27

Cenni Storici sulla Virtualizzazione 2/2

• Alla fine degli anni

'90,

l’interesse rinasce per rendere meno onerosa la

programmazione hw special-purpose.

✓VMware fondata nel 1998.

• Si acuisce il problema dei costi di gestione e di sottoutilizzo di piattaforme hw e

sw eterogenee.

✓L’hw cambia più velocemente del sw (middleware e applicazioni).
✓Aumenta il costo di gestione e diminuisce la portabilità.

• Diventa nuovamente importante la condivisione dell’hw e delle capacità di

calcolo non usate, per ridurre i costi dell’infrastruttura.

✓È una delle tecnologie abilitanti del Cloud Computing.

Virtualizzazione | 

28

I Vantaggi della Virtualizzazione 1/3

• Facilita la compatibilità, portabilità, interoperabilità e migrazione di applicazioni

ed ambienti.

▪ Indipendenza dall’hw.
▪ Create Once, Run Anywhere.
▪ VM legacy: eseguire vecchi SO o vecchie applicazioni su nuove piattaforme.

Programma

Interfaccia A

Hardware/software Sistema A

Programma

Interfaccia A

Implementazione della
mimica A su B

Interfaccia B

Hardware/software Sistema B

Virtualizzazione | 

29

I Vantaggi della Virtualizzazione 2/3

• Permette il consolidamento dei server (servers consolidation) in un data center,

con vantaggi economici, gestionali ed energetici.

✓Multiplexing di molteplici VM sullo stesso server.
✓Obiettivo: ridurre il numero totale di server usati, utilizzandoli in modo più

efficiente.
✓Vantaggi:

❑Riduzione di costi, consumi energetici e spazio occupato.
❑Semplificazione nella gestione, manutenzione ed upgrade dei server.
❑Riduzione dei tempi di downtime, tramite live migration di VM.

Virtualizzazione | 

30

Il Consolidamento dei Server

SALES

Windows

Application

OS

Hardware

Utilizzo

Server

CRM

Linux

HW

37%

ERP

Solaris

Strato di 
Virtualizzazione
o Hypervisor

Virtualizzazione | 

31

I Vantaggi della Virtualizzazione 3/3

• Permette di isolare componenti malfunzionanti o soggetti ad attacchi di sicurezza,

incrementando affidabilità e sicurezza delle applicazioni.

▪ Macchine virtuali di differenti applicazioni non possono avere accesso alle

rispettive risorse.

▪ Bug del software, crash, virus in una VM non possono danneggiare altre VM

in esecuzione sulla stessa macchina fisica.

• Permette di isolare le prestazioni di diverse VM.

▪ Tramite lo scheduling delle risorse fisiche che sono condivise tra molteplici

VM in esecuzione sulla stessa macchina fisica.

• Permette di bilanciare il carico sui server.

▪ Tramite la migrazione della VM da un server ad un altro.

Virtualizzazione | 

32

Uso di ambienti di esecuzione virtualizzati

• In ambito personale e didattico.

▪ Per eseguire simultaneamente diversi SO sulla stessa macchina.
▪ Per semplificare l’installazione di sw.

• In ambito professionale.

▪ Per debugging, testing e sviluppo di applicazioni.

• In ambito aziendale.

▪ Per consolidare l’infrastruttura del data center.
▪ Per garantire business continuity: incapsulando interi sistemi in singoli file
(system image) che possono essere replicati, migrati o reinstallati su qualsiasi
server.

Virtualizzazione | 

33

L’Hypervisor

• Un Hypervisor è un software di virtualizzazione che
SO
eseguire
permette
contemporaneamente sulla stessa macchina fisica,
interagendo direttamente con le risorse fisiche del
server.

diversi

di

• Un Hypervisor è un software che si trova tra il
sistema operativo e le risorse hw specializzate del
server.

• Quando è presente, è l’hypervisor, piuttosto che il
SO, che gestisce le connessioni tra i driver e le
risorse del server.

• L’hypervisor presenta una connessione virtuale alle

risorse del server per il SO di una VM.
In particolare, l’hypervisor lo fa per molte VM in
esecuzione sullo stesso server, anche se queste VM
hanno tutte SO diversi e applicazioni non correlate
tra loro.

•

•

•

Il termine hypervisor è una variante di supervisor
(solitamente riferito al kernel di un SO): essendo
l’hypervisor il supervisor di supervisor,
il prefisso
hyper è una variante più forte di super.
Il termine è stato usato per la prima volta attorno al
1970: IBM lo ha coniato per la macchina 360/65 e
successive.

CPU

Memory

NIC

DISK

SERVER

Virtualizzazione | 

34

VM1

VM2

VM3

Application

Application

Application

OS1

OS2

OS3

Hypervisor

Driver

Driver

Driver

Driver