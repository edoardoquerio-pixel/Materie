# InterVLAN Routing

Fonte: `InterVLAN Routing.pdf`

Routing inter-VLAN

Obiettivi del modulo

Titolo del modulo: Routing inter-VLAN

Obiettivo del modulo: Risolvere i problemi di routing inter-VLAN sui dispositivi di Layer 3

Titolo argomento

Obiettivo argomento

Funzionamento del routing interVLAN

Descrivere le opzioni per la configurazione del routing 
tra VLAN.

Routing inter-VLAN router-on-a-stick Configurare il router-on-a-stick inter-VLAN routing.

Routing inter-VLAN utilizzando 
switch Layer 3

Configurare il routing inter-VLAN utilizzando lo 
switching Layer 3

Risoluzione dei problemi relativi al 
routing inter-VLAN

Risolvere i problemi comuni di configurazione tra 
VLAN.

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

2

Funzionamento del routing
inter-VLAN

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

3

Funzionamento del routing inter-VLAN
Cos'è il routing inter-VLAN?

Le VLAN vengono utilizzate per segmentare le reti Layer 2 commutate per una serie di motivi. 
Indipendentemente dal motivo, gli host in una VLAN non possono comunicare con gli host in un'altra 
VLAN a meno che non sia presente un router o uno switch Layer 3 per fornire servizi di routing.

Il routing inter-VLAN è il processo di inoltro del traffico di rete da una VLAN a un'altra VLAN.

Esistono tre opzioni di routing inter-VLAN:

• Routing inter-VLAN legacy - Questa è una soluzione legacy. Ha una scalabilità minima.

• Router-on-a-stick - Questa è una soluzione accettabile per una rete di piccole e medie 

dimensioni.

• Switch di livello 3 utilizzando interfacce virtuali commutate (SVI) - Questa è la soluzione più 

scalabile per organizzazioni di medie e grandi dimensioni. 

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

4

Funzionamento del routing inter-VLAN
Routing legacy inter-VLAN

•

•

•

La prima soluzione di routing inter-VLAN si basava sull'utilizzo di un router con più interfacce 
Ethernet. Ogni interfaccia router è stata collegata a una porta switch in diverse VLAN. Le 
interfacce del router fungono da gateway predefiniti per gli host locali nella subnet VLAN.
Il routing inter-VLAN legacy utilizzando interfacce fisiche funziona, ma ha una limitazione 
significativa. Non è ragionevolmente scalabile perché i router hanno un numero limitato di 
interfacce fisiche. La richiesta di un'interfaccia router fisica per VLAN esaurisce rapidamente la 
capacità dell'interfaccia fisica di un router.
Nota: Questo metodo di routing inter-VLAN non è più implementato nelle reti commutate ed è 
incluso solo a scopo esplicativo.

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

5

Funzionamento del routing inter-VLAN
Routing router-on-a-stick inter-VLAN

Il metodo di routing inter-VLAN "router-on-a-stick" supera la limitazione del metodo di routing inter-VLAN 
legacy. Richiede solo un'interfaccia Ethernet fisica per instradare il traffico tra più VLAN su una rete.
• Un'interfaccia Ethernet router Cisco IOS è configurata come un trunk 802.1Q e collegata a una porta 

•

trunk su uno switch Layer 2. In particolare, l'interfaccia del router è configurata utilizzando subinterfacce 
per identificare VLAN instradabili.
Le subinterfacce configurate sono interfacce virtuali basate su software. Ciascuna è associata a 
un'unica interfaccia Ethernet fisica. Le subinterfacce sono configurate nel software su un router. Ogni 
sottointerfaccia è configurata in modo indipendente con un indirizzo IP e un'assegnazione VLAN. Le 
subinterfacce sono configurate per subnet diverse che corrispondono alla loro assegnazione VLAN. 
Questo facilita il routing logico.

• Quando il traffico con tag VLAN entra nell'interfaccia del router, viene inoltrato alla sottointerfaccia 

VLAN. Dopo che una decisione di routing è stata presa in base all'indirizzo di rete IP di destinazione, il 
router determina l'interfaccia di uscita per il traffico. Se l'interfaccia di uscita è configurata come 
sottointerfaccia 802.1q, i frame di dati vengono contrassegnati da VLAN con la nuova VLAN e inviati 
nuovamente l'interfaccia fisica.

Nota: Il metodo router-on-a-stick del routing inter-VLAN non supera 50 VLAN.

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

6

Funzionamento del routing inter-VLAN
Routing inter-VLAN su uno switch di Layer 3

Il metodo moderno per eseguire il routing inter-VLAN consiste nell'utilizzare gli switch di Layer 3 e le 
interfacce virtuali commutate (SVI). Un SVI è un'interfaccia virtuale configurata su uno switch Layer 3, 
come mostrato nella figura.

Nota: Uno switch Layer 3 è anche chiamato interruttore multilayer in quanto opera al Layer 2 e al Layer 
3. Tuttavia, in questo corso usiamo il termine switch Layer 3.

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

7

Funzionamento del routing inter-VLAN
Routing inter-VLAN su uno switch di Layer 3 (seguito)

Gli SVI inter-VLAN vengono creati nello stesso modo in cui viene configurata l'interfaccia VLAN di 
gestione. L'SVI viene creato per una VLAN esistente sullo switch. Anche se virtuale, l'SVI svolge le 
stesse funzioni per la VLAN come farebbe un'interfaccia router. In particolare, fornisce l'elaborazione 
Layer 3 per i pacchetti inviati a o da tutte le porte switch associate a tale VLAN.

Di seguito sono riportati i vantaggi dell'utilizzo di switch Layer 3 per il routing inter-VLAN:

•

•

•

•

•

•

Sono molto più veloci del router-on-a-stick perché tutto è hardware commutato e instradato.

Non è necessario alcun collegamento esterno dallo switch al router per il routing.

Essi non sono limitati a un collegamento perché Layer 2 EtherChannels può essere utilizzato 
come collegamenti trunk tra gli switch per aumentare la larghezza di banda.

La latenza è molto inferiore perché i dati non devono lasciare lo switch per essere instradati a una 
rete diversa.

Sono più comunemente distribuiti in una LAN del campus rispetto ai router.
L'unico svantaggio è che gli interruttori Layer 3 sono più costosi.

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

8

Routing inter-VLAN routeron-a-stick

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

9

Routing inter-VLAN router-on-a-stick
Scenario di router-on-a-stick

•

•

•

•

Nella figura, l'interfaccia R1 GigabitEthernet 0/0/1 è 
collegata alla porta S1 FastEthernet 0/5. La porta S1 
FastEthernet 0/1 è collegata alla porta S2 FastEthernet 0/1. 
Si tratta di collegamenti trunk necessari per inoltrare il 
traffico all'interno e tra le VLAN.
Per instradare VLAN, l'interfaccia R1 GigabitEthernet 0/0/1 è 
logicamente suddivisa in tre subinterfacce, come mostrato 
nella tabella. La tabella mostra anche le tre VLAN che 
verranno configurate sugli switch.
Si supponga che R1, S1 e S2 hanno configurazioni di base 
iniziali. Attualmente PC1 e PC2 non possono eseguire il 
ping a vicenda perché si trovano su reti separate. Solo S1 e 
S2 possono eseguire il ping a vicenda, ma sono 
irraggiungibili da PC1 o PC2 perché sono anche su reti 
diverse.
Per consentire ai dispositivi di eseguire il ping reciproco, gli 
switch devono essere configurati con VLAN e trunking e il 
router deve essere configurato per il routing inter-VLAN.

Sottointerfacc
ia

VLAN Indirizzo IP

G0/0/1.10

G0/0/1.20

10

20

192.168.10.1/24

192.168.20.1/24

G0/0/1.30

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

192.168.99.1/24

99

10

Routing inter-VLAN router-on-a-stick
Configurazione VLAN e Trunking S1

Per configurare S1 con VLAN e trunking, completare i passaggi seguenti:
• Passo 1. Creare e assegnare un nome alle VLAN. 
• Passo 2. Creare l'interfaccia di gestione.
• Passo 3. Configurare le porte di accesso.
• Passo 4. Configurare le porte trunking. 

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

11

Routing inter-VLAN router-on-a-stick
Configurazione VLAN e Trunking S2

La configurazione per S2 
è simile a S1.

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

12

Routing inter-VLAN router-on-a-stick
Configurazione sottointerfaccia R1

Il metodo router-on-a-stick richiede di creare una sottointerfaccia per ogni VLAN da instradare. 
Viene creata una sottointerfaccia utilizzando il comando interfaceinterface_id subinterface_id in 
modalità di configurazione globale. La sintassi dell'interfaccia secondaria è l'interfaccia fisica 
seguita da un punto e un numero di sottointerfaccia. Anche se non richiesto, è consuetudine 
abbinare il numero di sottointerfaccia con il numero VLAN.
Ogni sottointerfaccia viene quindi configurata con i seguenti due comandi:

•

•

encapsulation dot1q vlan_id [native] - Questo comando configura la sottointerfaccia per 
rispondere al traffico incapsulato 802.1Q dal file specificato vlan-id. L'opzione parola 
chiave native viene aggiunta solo per impostare la VLAN nativa su qualcosa di diverso da 
VLAN 1.

ip addressip-address subnet-mask - Questo comando configura l'indirizzo IPv4 della 
sottointerfaccia. Questo indirizzo in genere funge da gateway predefinito per la VLAN 
identificata.

Ripetere il processo per ogni VLAN da instradare. A ogni sottointerfaccia del router deve essere 
assegnato un indirizzo IP su una subnet univoca affinché si verifichi il routing. Quando tutte le 
subinterfacce sono state create, abilitare l'interfaccia fisica utilizzando il comando di 
configurazione dell'interfaccia no shutdown. Se l'interfaccia fisica è disabilitata, tutte le 
sottointerfacce sono disabilitate.

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

13

Routing inter-VLAN router-on-a-stick
Configurazione sottointerfaccia R1 (seguito)

Nella configurazione, le 
subinterfacce R1 G0/0/1 sono 
configurate per VLAN 10, 20 e 
99.

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

14

Router-on-a-stick Inter-VLAN Routing
Verifica della connettività tra PC1 e PC2

La configurazione del router-on-a-stick è 
completa dopo che il trunk switch e le 
subinterfacce del router sono state configurate. 
La configurazione può essere verificata da 
host, router e switch.

Da un host, verificare la connettività a un host 
in un'altra VLAN utilizzando il comando ping. È 
una buona idea verificare prima la 
configurazione IP dell'host corrente utilizzando 
il comando host di Windows ipconfig.

Quindi, utilizzare ping per verificare la 
connettività con PC2 e S1, come mostrato 
nella figura. L'output ping conferma con 
successo il routing inter-VLAN in funzione.

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

15

Routing inter-VLAN router-on-a-stick
Verifica del routing inter-VLAN di router-on-a-stick

Oltre all'utilizzo del ping tra dispositivi, è possibile utilizzare i seguenti comandi 
show per verificare e risolvere i problemi della configurazione del router-on-astick.
•
•
•
•

show ip route
show ip interface brief
show interfaces
show interfaces trunk

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

16

Routing inter-VLAN 
utilizzando Switch Layer 3

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

17

Routing inter-VLAN utilizzando Layer 3 Switch
Switch Layer 3 di routing inter-VLAN

Il routing inter-VLAN che utilizza il metodo router-on-a-stick è semplice da implementare per 
un'organizzazione di piccole e medie dimensioni. Tuttavia, una grande azienda richiede un 
metodo più veloce e molto più scalabile per fornire il routing inter-VLAN.

Le LAN del campus aziendale utilizzano switch Layer 3 per fornire il routing inter-VLAN. Gli 
switch Layer 3 utilizzano la commutazione basata su hardware per ottenere velocità di 
elaborazione dei pacchetti superiori rispetto ai router. Gli switch Layer 3 sono comunemente 
implementati anche negli armadi di cablaggio a livello di distribuzione aziendale.

Le funzionalità di uno switch Layer 3 includono la possibilità di eseguire le seguenti operazioni:

•

•

•

Instradare da una VLAN all'altra utilizzando più interfacce virtuali commutate (SVIS).

Convertire un switchport Layer 2 in un'interfaccia Layer 3 (cioè una porta instradata). Una 
porta instradata è simile a un'interfaccia fisica su un router Cisco IOS.

Per fornire il routing inter-VLAN, gli switch Layer 3 utilizzano gli SVI. Gli SVI sono 
configurati utilizzando lo stesso comando interface vlan vlan-id utilizzato per creare l'SVI 
di gestione su uno switch Layer 2. È necessario creare un SVI Layer 3 per ciascuna delle 
VLAN instradabili.

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

18

Routing inter-VLAN utilizzando Layer 3 Switch
Scenario di switch Layer 3

Nella figura, lo switch Layer 
3, D1, è collegato a due host 
su diverse VLAN. PC1 è in 
VLAN 10 e PC2 è in VLAN 
20, come mostrato. Lo switch 
Layer 3 fornirà servizi di 
routing inter-VLAN ai due 
host.

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

19

Routing inter-VLAN utilizzando Layer 3 Switch
Configurazione di switch Layer 3

Per configurare S1 con VLAN e trunking, completare i 
passaggi seguenti:
•

Passo 1. Creare le VLAN. Nell'esempio vengono 
utilizzati VLAN 10 e 20. 
Passo 2. Creare le interfacce VLAN SVI. L'indirizzo IP 
configurato fungerà da gateway predefinito per gli host 
nella rispettiva VLAN. 
Passo 3. Configurare le porte di accesso. Assegnare la 
porta appropriata alla VLAN richiesta. 

•

•

•

Passo 4. Abilitare il routing IP. Eseguire il comando di 
configurazione globale routing ip per consentire lo 
scambio di traffico tra VLAN 10 e 20. Questo comando 
deve essere configurato per abilitare il routing inter-VLAN 
su uno switch Layer 3 per IPv4.

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

20

Routing inter-VLAN utilizzando Layer 3 Switch
Verifica di switch Layer 3 di routing inter-VLAN

Il routing inter-VLAN utilizzando uno switch Layer 3 è più semplice da configurare rispetto 
al metodo router-on-a-stick. Al termine della configurazione, la configurazione può essere 
verificata verificando la connettività tra gli host.
• Da un host, verificare la connettività a un host in un'altra VLAN utilizzando il comando 

ping. È una buona idea verificare prima la configurazione IP dell'host corrente 
utilizzando il comando host di Windows ipconfig.
Successivamente, verificare la connettività con PC2 utilizzando il comando host di 
Windows ping. L'uscita ping riuscita conferma che il routing inter-VLAN è operativo.

•

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

21

Routing inter-VLAN utilizzando Layer 3 Switch
Routing su switch Layer 3

Se le VLAN devono essere raggiungibili da altri dispositivi di Layer 3, devono essere 
pubblicizzate utilizzando routing statico o dinamico. Per abilitare il routing su uno switch di 
Layer 3, è necessario configurare una porta instradata.

Una porta instradata viene creata su uno switch di Layer 3 disabilitando la funzione 
switchport su una porta di Layer 2 collegata a un altro dispositivo di Layer 3. In 
particolare, la configurazione del comando di configurazione dell'interfaccia no 
switchport su una porta di Layer 2 lo converte in un'interfaccia di Layer 3. Quindi 
l'interfaccia può essere configurata con una configurazione IPv4 per connettersi a un 
router o a un altro switch Layer 3.

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

22

Routing inter-VLAN utilizzando Layer 3 Switch
Scenario di routing su switch Layer 3

Nella figura, lo switch D1 Layer 3 configurato in 
precedenza è ora collegato a R1. R1 e D1 sono 
entrambi in un dominio del protocollo di routing 
OSPF (Open Shortest Path First). Supponiamo 
che Inter-VLAN sia stato implementato con 
successo su D1. Anche l'interfaccia G0/0/1 di R1 
è stata configurata e abilitata. Inoltre, R1 utilizza 
OSPF per pubblicizzare le sue due reti, 
10.10.10.0/24 e 10.20.20.0/24.

Nota: La configurazione di routing OSPF è 
trattata in un altro corso. In questo modulo, i 
comandi di configurazione OSPF saranno forniti a 
voi in tutte le attività e valutazioni. Non è 
necessario comprendere la configurazione per 
abilitare il routing OSPF sullo switch Layer 3.

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

23

Routing inter-VLAN utilizzando Layer 3 Switch
Configurazione routing su switch Layer 3

Completare i passaggi seguenti per configurare D1 per l'instradamento con R1:
•

Passo 1. Configurare la porta instradata. Utilizzare il comando no switchport per convertire la 
porta in una porta instradata, quindi assegnare un indirizzo IP e una subnet mask. Attivare la porta.
Passo 2. Abilitare il routing. Utilizzare il comando di configurazione globale ip routing per abilitare 
il routing.
Passo 3. Configurare il routing. Utilizzare un metodo di routing appropriato. In questo esempio, è 
configurato Single-Area OSPFv2
Passo 4. Verificare il routing. Usare il comando show ip route .
Passo 5. Verificare la connettività. Utilizzare il comando ping per verificare la raggiungibilità.

•

•

•
•

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

24

Risoluzione dei problemi 
relativi al routing inter-VLAN

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

25

Risoluzione dei problemi relativi al routing inter-VLAN
Problemi comuni in inter-VLAN

Ci sono una serie di motivi per cui una configurazione inter-VLAN potrebbe non funzionare. Tutti sono 
legati a problemi di connettività. Innanzitutto, controllare il layer fisico per risolvere eventuali problemi in 
cui un cavo potrebbe essere collegato alla porta errata. Se le connessioni sono corrette, utilizzare 
l'elenco nella tabella per altri motivi comuni per cui la connettività tra VLAN potrebbe non riuscire.

Tipo di problema

Come risolvere il problema

Come verificare

VLAN mancanti

•Creare (o ricreare) la VLAN se non esiste.
•Assicurarsi che la porta host sia assegnata alla VLAN 
corretta.

show vlan [brief]
show interfaces switchport
ping

Cambiare i problemi della 
porta del trunk

•Assicurarsi che i trunk siano configurati correttamente.
•Assicurarsi che la porta sia una porta trunk e abilitata.

show interface trunk
show running-config

Cambiare i problemi della 
porta di accesso

Problemi di configurazione 
del router

•Assegnare VLAN corretta alla porta di accesso.
•Assicurarsi che la porta sia una porta di accesso e 
abilitata.
•Host non è configurato correttamente nella subnet 
errata.

•L'indirizzo IPv4 della sottointerfaccia del router è 
configurato in modo errato.
•La sottointerfaccia del router viene assegnata all'ID 
VLAN.

show interfaces switchport
show running-config interface
ipconfig

show ip interface brief
show interfaces

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

26

Risoluzione dei problemi relativi al routing inter-VLAN
Scenario di risoluzione dei problemi relativi al routing interVLAN

Esempi di alcuni di questi problemi di routing 
inter-VLAN saranno ora trattati in modo più 
dettagliato. Questa topologia verrà utilizzata 
per tutti questi problemi.

Router R1 Sottointerfacce

Sottointerfac
cia

VLAN Indirizzo IP

G0/0/0.10

G0/0/0.20

G0/0/0.30

10

20

99

192.168.10.1/24

192.168.20.1/24

192.168.99.1/24

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

27

Risoluzione dei problemi relativi al routing inter-VLAN
VLAN mancanti

Un problema di connettività tra VLAN potrebbe 
essere causato da una VLAN mancante. La 
VLAN potrebbe mancare se non è stata creata, 
è stata cancellata accidentalmente o non è 
consentita sul collegamento trunk.

Quando una VLAN viene eliminata, tutte le 
porte assegnate a tale VLAN diventano inattive. 
Rimangono associati alla VLAN (e quindi 
inattivi) finché non vengono assegnate a una 
nuova VLAN o ricreate la VLAN mancante. 
Ricreare la VLAN mancante riassegnerà 
automaticamente gli host.

Utilizzare il comando show interface interfaceid switchport per verificare l'appartenenza 
VLAN della porta.

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

28

Risoluzione dei problemi relativi al routing inter-VLAN
Problemi switch porte trunk

Un altro problema per il routing tra VLAN include le porte switch configurate in modo errato. 
In una soluzione inter-VLAN legacy, questo potrebbe essere causato quando la porta del 
router di connessione non viene assegnata alla VLAN corretta.
Tuttavia, con una soluzione router-on-a-stick, la causa più comune è una porta trunk 
configurata in modo errato.
•

Verificare che la porta che si connette al router sia configurata correttamente come 
collegamento trunk utilizzando il comando show interface trunk.
Se tale porta è mancante dall'output, esaminare la configurazione della porta con il 
comando show running-config interface X per vedere come è configurata la porta.

•

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

29

Risoluzione dei problemi relativi al routing inter-VLAN
Problemi di accesso alle porte switch

Quando si sospetta un problema con una 
configurazione della porta di accesso switch, 
utilizzare i comandi di verifica per esaminare la 
configurazione e identificare il problema.

Un indicatore comune di questo problema è il 
PC con la configurazione corretta dell'indirizzo 
(indirizzo IP, subnet mask, gateway 
predefinito), ma non è in grado di eseguire il 
ping del gateway predefinito.
•

Utilizzare il comando show vlan brief, 
show interface X switchport o show 
running-config interface interface X per 
verificare l'assegnazione dell'interfaccia 
VLAN.

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

30

Risolvere i problemi comuni di configurazione tra VLAN
Problemi di configurazione router

I problemi di configurazione del router-on-a-stick sono solitamente correlati a 
configurazioni errate della subinterfaccia.
•

Verificare lo stato dell'interfaccia secondaria utilizzando il comando show ip interface 
brief. 
Verificare quali VLAN ciascuna delle sottointerfacce è presente. Per fare ciò, il 
comando show interfaces è utile ma genera una grande quantità di output non 
richiesto aggiuntivo. L'output dei comandi può essere ridotto utilizzando i filtri dei 
comandi IOS. In questo esempio, utilizzare la parola chiave include per identificare 
che solo le righe contenenti le lettere "Gig" o "802.1Q"

•

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

31

4.5 Quiz e pratica

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

32

Quiz e pratica
Cosa ho appreso in questo modulo? 

Il routing inter-VLAN è il processo di inoltro del traffico di rete da una VLAN a un'altra VLAN. 

•
• Tre opzioni includono legacy, router-on-a-stick e Layer 3 switch utilizzando SVI. 
• Per configurare uno switch con VLAN e trunking, completare la procedura seguente: creare e assegnare 

•

un nome alle VLAN, creare l'interfaccia di gestione, configurare le porte di accesso e configurare le porte di 
trunking. 
Il metodo router-on-a-stick richiede la creazione di una sottointerfaccia per ogni VLAN da instradare. Una 
sottointerfaccia viene creata utilizzando il comando di modalità di configurazione globale interface_id 
subinterface_id . 

• A ogni sottointerfaccia del router deve essere assegnato un indirizzo IP su una subnet univoca affinché si 
verifichi il routing. Quando tutte le subinterfacce sono state create, l'interfaccia fisica deve essere abilitata 
utilizzando il comando di configurazione dell'interfaccia no shutdown. 

• Le LAN del campus aziendale utilizzano switch Layer 3 per fornire il routing inter-VLAN. Gli switch Layer 3 

utilizzano la commutazione basata su hardware per ottenere velocità di elaborazione dei pacchetti 
superiori rispetto ai router. 

• Le funzionalità di uno switch Layer 3 includono il routing da una VLAN all'altra utilizzando più interfacce 
virtuali commutate (SVI) e la conversione di una commutazione Layer 2 in un'interfaccia Layer 3 (ad 
esempio, una porta instradata). 

• Per fornire il routing inter-VLAN, gli switch Layer 3 utilizzano gli SVI. Gli SVI sono configurati utilizzando lo 

stesso comando interface vlan vlan-id utilizzato per creare la gestione SVI su uno switch Layer 2. 

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

33

Quiz e pratica
Cosa ho appreso in questo modulo? (seguito)

• Per configurare uno switch con VLANS e trunking, completare la procedura seguente: creare il VLANS, 

creare le interfacce VLAN SVI, configurare le porte di accesso e abilitare il routing IP. 

• Per abilitare il routing su uno switch di Layer 3, è necessario configurare una porta instradata. Una porta 

instradata viene creata su uno switch di Layer 3 disabilitando la funzione switchport su una porta di Layer 2 
collegata a un altro dispositivo di Layer 3. L'interfaccia può essere configurata con una configurazione IPv4 
per connettersi a un router o a un altro switch Layer 3. 

• Per configurare uno switch di Layer 3 per l'instradamento con un router, attenersi alla seguente procedura: 
configurare la porta instradata, abilitare il routing, configurare il routing, verificare il routing e verificare la 
connettività.

• Ci sono una serie di motivi per cui una configurazione inter-VLAN potrebbe non funzionare. Tutti sono 

correlati a problemi di connettività come VLAN mancanti, problemi di porta trunk switch, problemi di porta 
di accesso switch e problemi di configurazione del router. 

• Una VLAN potrebbe mancare se non è stata creata, è stata eliminata accidentalmente o non è consentita 

sul collegamento trunk. 

• Un altro problema per il routing tra VLAN include le porte switch configurate in modo errato. 
•

In una soluzione inter-VLAN legacy, una porta switch configurata in modo errato potrebbe essere causata 
quando la porta del router di connessione non è assegnata alla VLAN corretta. 

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

34

Quiz e pratica
Cosa ho appreso in questo modulo? (seguito)

• Con una soluzione router-on-a-stick, la causa più comune è una porta trunk configurata in modo errato. 
• Quando si sospetta un problema con una configurazione della porta di accesso switch, utilizzare ping e 

•

show interfaces interface-id switchport per identificare il problema. 
I problemi di configurazione del router con configurazioni router-on-a-stick sono solitamente correlati a 
configurazioni errate della subinterfaccia. Verificare lo stato dell'interfaccia secondaria utilizzando il 
comando show ip interface brief.

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

35

Modulo 4: Configurazione di base del dispositivo
Nuovi termini e comandi

▪ Routing inter-VLAN

▪ Router-on-a-stick

▪ encapsulation dot1q X [ native ]

▪ no switchport

▪ router ospf

▪ ip routing

© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento 
riservato Cisco

36