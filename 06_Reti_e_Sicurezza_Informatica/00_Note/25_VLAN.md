# VLAN

**File:** `VLAN.pdf`
**Tipo:** `.pdf`
**Dimensione:** 1059.7 KB
**Ultima modifica:** 02/07/2026 09:28

---

VLAN

2
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Obiettivi del modulo
Titolo del modulo: Protocolli e modelli
Obiettivo del modulo: Spiegare come i protocolli di rete consentono ai dispositivi di accedere alle 
risorse di rete locali e remote. 
Titolo argomento Obiettivo argomento
Panoramica sulle VLAN Spiegare lo scopo delle VLAN in una rete commutata.
VLAN in un ambiente multi-
switch
Spiegare come uno switch inoltra i frame basati sulla 
configurazione VLAN in un ambiente multi-switch.
Configurazione della VLAN Configurare una porta switch da assegnare a una VLAN in base ai 
requisiti.
Trunk VLAN Configurare una porta trunk su uno switch LAN.
Protocollo trunking dinamico Configurare il protocollo DTP (Dynamic Trunking Protocol).

3
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Panoramica sulle VLAN

4
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Panoramica sulle VLAN
Definizioni delle VLAN
Le VLAN sono connessioni logiche con altri 
dispositivi simili.
L'inserimento di dispositivi in varie VLAN ha le 
seguenti caratteristiche:
• Fornisce la segmentazione dei vari gruppi di 
dispositivi sugli stessi switch
• Fornire un'organizzazione più gestibile
• Broadcast, multicast e unicast sono isolati 
nella singola VLAN
• Ogni VLAN avrà una propria gamma unica 
di indirizzamento IP
• Domini di broadcast più piccoli


5
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Panoramica sulle VLAN
Vantaggi di una 
progettazione VLAN
I vantaggi dell'utilizzo delle VLAN 
sono i seguenti: 
Vantaggi Descrizione
Domini di broadcast
più piccoli
La divisione della LAN riduce il numero di domini broadcast
Maggiore sicurezza Solo gli utenti della stessa VLAN possono comunicare insieme
Maggiore efficienza IT Le VLAN possono raggruppare dispositivi con requisiti simili, ad esempio 
facoltà e studenti
Riduzione dei costi Uno switch può supportare più gruppi o VLAN
Prestazioni migliorate I domini broadcast di piccole dimensioni riducono il traffico, migliorando la 
larghezza di banda
Gestione semplificata Gruppi simili avranno bisogno di applicazioni simili e altre risorse di rete


6
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Panoramica sulle VLAN
Tipi di VLAN
VLAN predefinita
La VLAN 1 è la seguente: 
• La VLAN predefinita
• La VLAN nativa predefinita
• La VLAN di gestione 
predefinita
• Impossibile eliminare o 
rinominare
Nota: Sebbene non sia 
possibile eliminare VLAN1, 
Cisco consiglia di assegnare 
queste funzionalità predefinite 
ad altre VLAN


7
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Panoramica sulle VLAN
Tipi di VLAN (seguito) 
VLAN dati 
• Dedicata al traffico generato dall'utente (email e traffico web). 
• VLAN 1 è la VLAN dati predefinita perché tutte le interfacce sono assegnate a questa VLAN.
VLAN nativa
• Questa viene utilizzata solo per i collegamenti trunk. 
• Tutti i frame sono contrassegnati su un collegamento trunk 802.1Q tranne quelli sulla VLAN 
nativa. 
VLAN di gestione 
• Questa viene utilizzata per il traffico SSH/Telnet VTY e non deve essere trasportata con il 
traffico dell'utente finale.
• In genere, la VLAN che è SVI per lo switch Layer 2. 

8
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Panoramica sulle VLAN
Tipi di VLAN (seguito) 
VLAN voce  
• È necessaria una VLAN separata perché il 
traffico vocale richiede:
• Larghezza di banda garantita
• Priorità QoS alta
• Capacità di evitare la congestione
• Ritardo inferiore a 150 ms dall'origine alla 
destinazione
• L'intera rete deve essere progettata per 
supportare la voce.


9
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
VLAN in un ambiente 
multi-switch

10
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
VLAN in un ambiente multi-switch
Definizione di trunk VLAN
Un trunk è un collegamento point-to-
point tra due dispositivi di rete.
Funzioni del trunk Cisco:
• Consente più di una VLAN
• Estende la VLAN su tutta la rete
• Per impostazione predefinita, 
supporta tutte le VLAN
• Supporta trunking 802.1Q


11
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
VLAN in un ambiente multi-switch
Reti senza VLAN
Senza VLAN, tutti i dispositivi collegati agli switch riceveranno tutto il traffico unicast, 
multicast e broadcast.


12
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
VLAN in un ambiente multi-switch
Reti con VLAN
Con le VLAN, il traffico unicast, multicast e broadcast è limitato a una VLAN. Senza un 
dispositivo di Layer 3 per collegare le VLAN, i dispositivi in VLAN diverse non possono 
comunicare. 


13
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
VLAN in un ambiente multi-switch
Identificazione VLAN con un tag
• L'intestazione IEEE 802.1Q è 4 Byte
• Quando il tag viene creato, FCS deve essere 
ricalcolato.
• Quando viene inviato ai dispositivi finali, questo tag 
deve essere rimosso e il FCS ricalcolato nuovamente 
al suo numero originale.
Campo tag VLAN 802.1Q Funzione
Tipo • Campo a 2 byte con 0x8100 esadecimale
• Questo è indicato come Tag Protocol ID (TPID)
Priorità utente • Valore a 3 bit che supporta 
Canonical Format Identifier (CFI) • Valore a 1 bit che può supportare frame token ring su Ethernet
VLAN ID (VID) • Identificatore VLAN a 12 bit in grado di supportare fino a 4096 
VLAN


14
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
VLAN in un ambiente multi-switch
VLAN nativa e tag 802.1Q
Basi trunk 802.1Q:
• Il tagging viene in genere eseguito su tutte le 
VLAN.
• L'uso di una VLAN nativa è stato progettato 
per l'uso legacy, come l'hub nell'esempio.
• A meno che non sia cambiato, VLAN1 è la 
VLAN nativa.
• Entrambe le estremità di un collegamento 
trunk devono essere configurate con la 
stessa VLAN nativa.
• Ogni trunk è configurato separatamente, 
quindi è possibile avere una VLAN nativa 
diversa su trunk separati.


15
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
VLAN in un ambiente multi-switch
Tagging Voice VLAN
Il telefono VoIP è uno switch a tre porte:
• Lo switch utilizzerà CDP per informare il telefono della 
VLAN Voice.
• Il telefono contrassegnerà il proprio traffico (Voice) e può 
impostare Cost of Service (Cos). CoS è QoS per il Layer 
2.
• Il telefono potrebbe o non può etichettare i frame dal PC.
Traffico Funzione del tagging
Voice VLAN Taggato con un valore di priorità di classe di servizio (CoS) appropriato
Access VLAN Può anche essere taggata con un valore di priorità CoS di Layer 2
Access VLAN Non è contrassegnata (nessun valore di priorità CoS di Layer 2)


16
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
VLAN in un ambiente multi-switch
Esempio di verifica Voice VLAN
Il comando show interfaces fa0/18 switchport può mostrarci sia dati che VLAN vocali 
assegnati all'interfaccia.


17
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
VLAN in un ambiente multi-switch
Packet Tracer – Indagine su un'implementazione VLAN
In questa attività Packet Tracer, si potrà:
• Parte 1: Osservare il traffico broadcast in un'implementazione VLAN
• Parte 2: Osservare il traffico broadcast senza VLAN

18
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN

19
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Intervalli VLAN su switch Catalyst
Gli switch Catalyst 2960 e 3650 supportano 
oltre 4000 VLAN.
Intervallo normale VLAN 1 — 1005 Intervallo esteso VLAN 1006 - 4095
Utilizzato in piccole e medie imprese Usato da ⁪provider di servizi
1002 — 1005 sono riservati alle VLAN legacy Sono in Running-Config
1, 1002 - 1005 vengono creati 
automaticamente e non possono essere 
eliminati
Supporta meno funzioni VLAN
Memorizzati nel file vlan.dat in flash Richiede configurazioni VTP
VTP può sincronizzare tra gli switch


20
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Comandi di creazione VLAN
I dettagli VLAN vengono memorizzati nel file vlan.dat. È possibile creare VLAN in 
modalità di configurazione globale.
Attività Comando IOS
Accedere alla modalità di 
configurazione globale. Switch# configure terminal
Creare una VLAN con un numero ID 
valido. Switch(config)# vlan vlan-id
Specificare un nome univoco per 
identificare la VLAN. Switch(config-vlan)# name vlan-name
Ritornare alla modalità privileged EXEC. Switch(config-vlan)# end
Accedere alla modalità di 
configurazione globale. Switch# configure terminal

21
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Esempio di creazione VLAN
• Se Student PC sarà nella VLAN 20, 
creeremo prima la VLAN e poi la 
denomineremo.
• Se non gli viene assegnato un nome, 
Cisco IOS gli assegnerà un nome 
predefinito di vlan e il numero a quattro 
cifre della VLAN. Ad esempio vlan0020 
per VLAN 20.
Prompt Comando
S1# Configure terminal
S1(config)# vlan 20
S1(config-vlan)# name student
S1(config-vlan)# end


22
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Comandi di assegnazione porta VLAN
Una volta creata la VLAN, possiamo quindi assegnarla alle interfacce corrette.
Attività Comando
Accedere alla modalità di configurazione globale. Switch# configure terminal
Accedere alla modalità di configurazione 
dell’interfaccia. Switch(config)# interface interface-id
Impostare la porta in modalità di accesso. Switch(config-if)# switchport mode access
Assegnare la porta a una VLAN. Switch(config-if)# switchport access vlan vlan-id
Ritornare alla modalità privileged EXEC. Switch(config-if)# end

23
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Esempio di assegnazione porta VLAN
Possiamo assegnare la VLAN 
all'interfaccia porta.
• Una volta assegnata al dispositivo la 
VLAN, il dispositivo finale avrà 
bisogno delle informazioni 
sull'indirizzo IP per tale VLAN
• Qui, Student PC riceve 172.17.20.22
Prompt Comando
S1# Configure terminal
S1(config)# Interface fa0/18
S1(config-if)# Switchport mode access
S1(config-if)# Switchport access vlan 20
S1(config-if)# end


24
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
VLAN Data e Voice
Una porta di accesso può essere 
assegnata solo a una VLAN dati. 
Tuttavia, può anche essere 
assegnato a una VLAN Voice per 
quando un telefono e un dispositivo 
finale sono spenti dalla stessa porta 
di switch.


25
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Esempio di VLAN Data e Voice
• Vogliamo creare e denominare sia VLAN 
Voice che Data.
• Oltre ad assegnare la VLAN Data, 
assegneremo anche la VLAN Voice e 
accenderemo QoS per il traffico vocale 
all'interfaccia.
• Lo switch catalyst più recente creerà 
automaticamente la VLAN, se non esiste già, 
quando viene assegnata a un'interfaccia.
Nota: QoS non viene affrontato in questo 
corso. Qui mostriamo l'uso del comando mls 
qos trust [cos | device cisco-phone | dscp | 
ip-precedence] .


26
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Verifica informazioni 
VLAN
Usare il comando show vlan. La 
sintassi completa è la seguente: 
show vlan [brief | id vlan-id | name
vlan-name | summary]
Attività Opzione di comando
Visualizzare il nome VLAN, lo stato e le relative porte una VLAN per 
riga. brief
Visualizzare le informazioni sul numero ID VLAN identificato. id vlan-id
Visualizzare le informazioni sul nome VLAN identificato. Il vlan name
è una stringa ASCII da 1 a 32 caratteri. name vlan-name
Visualizzare le informazioni di riepilogo della VLAN. Riepilogo


27
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Modificare l'appartenenza alla 
porta VLAN
Esistono diversi modi per cambiare 
l'appartenenza alla VLAN:
• Reinserire il comando switchport access 
vlan vlan-id 
• Utilizzare no switchport access vlan per 
riposizionare l'interfaccia in VLAN 1
Utilizzare brief show vlan o i comandi show 
interface fa0/18 switchport per verificare la 
corretta associazione VLAN.


28
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Eliminare VLAN
Eliminare le VLAN con il comando no vlan vlan-id
Attenzione: Prima di eliminare una VLAN, riassegnare tutte le porte membro a una VLAN 
diversa. 
• Eliminare tutte le VLAN con i comandi delete flash:vlan.dat o delete vlan.dat .
• Ricaricare lo switch quando si eliminano tutte le VLAN.
Nota: Per ripristinare l'impostazione predefinita di fabbrica: scollegare tutti i cavi dati, 
cancellare la configurazione di avvio ed eliminare il file vlan.dat, quindi ricaricare il 
dispositivo.

29
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Packet Tracer — Configurazione VLAN
In questo Packet Tracer, verranno raggiunti i seguenti obiettivi:
• Verificare la configurazione VLAN predefinita
• Configurare VLAN
• Assegnare VLAN alle porte

30
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Trunk VLAN

31
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Trunk VLAN
Comandi di configurazione del trunk
Configurare e verificare i trunk VLAN. I trunk sono layer 2 e trasportano il traffico per tutte le 
VLAN.
Attività Comando IOS
Enter global configuration mode. Switch# configure terminal
Accedere alla modalità di configurazione 
dell’interfaccia. Switch(config)# interface interface-id
Impostare la porta sulla modalità trunking 
permanente. Switch(config-if)# switchport mode trunk
Impostare la VLAN nativa su qualcosa di 
diverso dalla VLAN 1.
Switch(config-if)# switchport trunk native vlan 
vlan-id
Specificare l'elenco delle VLAN da 
autorizzare sul collegamento trunk.
Switch(config-if)# switchport trunk allowed 
vlan vlan-list
Ritornare alla modalità privileged EXEC. Switch(config-if)# end

32
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Trunk VLAN
Esempio di configurazione del 
trunk
Le subnet associate a ogni VLAN sono:
• VLAN 10 - Faculty/Staff - 172.17.10.0/24
• VLAN 20 - Student - 172.17.20.0/24
• VLAN 30 - Guest - 172.17.30.0/24
• VLAN 99 - Native - 172.17.99.0/24
La porta F0/1 su S1 è 
configurata come porta trunk.
Nota: Questo presuppone uno 
switch 2960 che utilizza il tag 
802.1q. Gli switch di Layer 3 
richiedono che l'incapsulamento 
sia configurato prima della 
modalità trunk. 
Prompt Comando
S1(config)# Interface fa0/1
S1(config-if)# Switchport mode trunk
S1(config-if)# Switchport trunk native vlan 99
S1(config-if)# Switchport trunk allowed vlan 10,20,30,99
S1(config-if)# terminare


33
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Trunk VLAN
Verifica della configurazione 
trunk
Impostare la modalità trunk e vlan nativo.
Notare sh int fa0/1 switchport :
• È impostato su trunk amministrativo
• È impostato come trunk operativamente 
(funzionante)
• L'incapsulamento è dot1q
• VLAN nativa impostata su VLAN 99 
• Tutte le VLAN create sullo switch 
passeranno il traffico su questo trunk


34
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Trunk VLAN
Ripristinare il trunk allo stato predefinito
• Ripristina le impostazioni predefinite 
del trunk con il comando no.
• Tutte le VLAN hanno consentito di 
passare il traffico
• VLAN nativa = VLAN 1
• Verificare le impostazioni predefinite 
con un comando sh int fa0/1 
switchport .


35
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Trunk VLAN
Ripristinare il trunk allo stato predefinito (seguito)
Ripristinare il trunk in una modalità di accesso 
con il comando switchport mode access :
• È impostato su un'interfaccia di accesso 
amministrativo
• È impostato come interfaccia di accesso 
operativamente (funzionante)


36
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Trunk VLAN
Packet Tracer — Configurazione trunk
In questo Packet Tracer, verranno raggiunti i seguenti obiettivi:
• Verificare VLAN
• Configurare trunk

37
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Trunk VLAN
Laboratorio — Configurare VLAN e trunks
In questa attività di laboratorio si seguiranno i seguenti passi:
• Implementare la rete e configurare le impostazione di base del dispositivo
• Creare VLAN e assegnare porte switch
• Gestire le assegnazioni delle porte VLAN e il database VLAN
• Configurare un trunk 802.1Q tra gli switch
• Eliminare il database VLAN

38
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Dynamic Trunking Protocol

39
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Dynamic Trunking Protocol
Introduzione a DTP
Dynamic Trunking Protocol (DTP) è un protocollo proprietario di Cisco.
Le caratteristiche DTP sono le seguenti:
• Attivo per impostazione predefinita su Catalyst 2960 e 2950 switch
• Dynamic-auto è predefinito sugli switch 2960 e 2950
• Può essere disattivato con il comando nonegotiate
• Può essere riattivato impostando l'interfaccia su dynamic-auto
• L'impostazione di uno switch su un trunk statico o un accesso statico eviterà problemi di 
negoziazione con il trunk in modalità switchport o i comandi di accesso in modalità 
switchport.


40
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Dynamic Trunking Protocol
Modalità di negoziazione interfaccia
Il comando switchport mode prevede opzioni aggiuntive.
Utilizzare il comando di configurazione dell'interfaccia switchport nonegotiate per 
interrompere la negoziazione DTP.
Opzione Descrizione
access Modalità di accesso permanente e negozia per convertire il 
collegamento adiacente in un collegamento di accesso
dynamic auto Diventa un'interfaccia trunk se l'interfaccia adiacente è impostata sulla 
modalità trunk o desiderable
dynamic desirable Cerca attivamente di diventare un trunk negoziando con altre interfacce 
auto o desirable
trunk Modalità di trunking permanente e negozia per convertire il 
collegamento adiacente in un collegamento trunk

41
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Dynamic Trunking Protocol
Risultati di una configurazione DTP
Le opzioni di configurazione DTP sono le seguenti:
Dynamic Auto Dynamic 
Desirable Trunk Access
Dynamic Auto Access Trunk Trunk Access
Dynamic 
Desirable Trunk Trunk Trunk Access
Trunk Trunk Trunk Trunk Connettività 
limitata
Access Access Access Connettività 
limitata Access

42
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Dynamic Trunking Protocol
Verifica della modalità DTP
La configurazione DTP predefinita dipende 
dalla versione e dalla piattaforma Cisco 
IOS.
▪ Utilizzare il comando show dtp 
interface per determinare la modalità 
DTP corrente.
▪ La best practice consiglia di impostare le 
interfacce per l'accesso o il trunk e per 
disattivare DTP


43
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Quiz e pratica 

44
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Quiz e pratica
Packet Tracer – Implementare VLAN e Trunking
In questo Packet Tracer, verranno raggiunti i seguenti obiettivi:
• Configurare VLAN
• Assegnare porte alle VLAN
• Configurare trunking statico
• Configurare trunking dinamico

45
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Quiz e pratica
Laboratorio — Implementare VLAN e Trunking
In questa attività di laboratorio si seguiranno i seguenti passi:
• Implementare la rete e configurare le impostazione di base del dispositivo
• Creare VLAN e assegnare porte switch
• Configurare un trunk 802.1Q tra gli switch

46
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Quiz e pratica
Che cosa ho appreso in questo modulo?
• Le VLAN si basano su connessioni logiche anziché fisiche.
• Le VLAN possono segmentare le reti in base alla funzione, al team o 
all'applicazione.
• Ogni VLAN è considerata una rete logica separata.
• Un trunk è un collegamento point-to-point che porta più di una VLAN. 
• I campi dei tag VLAN includono tipo, priorità utente, CFI e VID.
• Per supportare VoIP è necessaria una VLAN vocale separata.
• Le configurazioni VLAN a intervallo normale vengono memorizzate nel file 
vlan.dat in flash.
• Una porta di accesso può appartenere a una VLAN dati alla volta, ma può anche 
avere una VLAN vocale.

47
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Quiz e pratica
Cosa ho appreso in questo modulo? (seguito)
• Un trunk è un collegamento di Layer 2 tra due switch che trasporta il traffico per 
tutte le VLAN.
• Il tunk avrà bisogno di tagging per le varie VLAN, in genere 802.1q.
• Il tag IEEE 802.1q consente di eseguire il provisioning di una VLAN nativa che 
rimarrà senza tag.
• Un'interfaccia può essere impostata su trunking o non trunking.
• La negoziazione del trunk è gestita dal Dynamic Trunking Protocol (DTP).
• DTP è un protocollo proprietario Cisco che gestisce la negoziazione trunk

48
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Pratica del modulo e Quiz
Nuovi Termini e Comandi
• VLAN
• Dominio di broadcast logico
• VLAN dati
• VLAN predefinita
• VLAN nativa
• VLAN di gestione
• show vlan brief
• VLAN voce
• Trunk VLAN
• Segmentazione VLAN
• Rete
• Tagging VLAN
• Canonical Format Identifier (CFI)
• Priorità utente
• ID VLAN
• Tipo
• show interfaces int switchport

49
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Quiz e pratica
Nuovi termini e comandi
• VLAN a intervallo normale
• VLAN a gamma estesa
• vlan vlan-id
• name vlan-name
• switchport mode access
• switchport access vlan 
vlan-id
• Intervallo interfaccia
• no switchport access vlan 
vlan-id
• vlan vlan-id
• delete flash:vlan.dat
• delete vlan.dat
• show vlan
• show interfaces
• show vlan summary
• show interfaces vlan 
vlan_id
• switchport mode trunk
• switchport trunk allowed 
vlan vlan_list
• switchport trunk native 
vlan vlan_id
• no switchport trunk 
allowed vlan
• no switchport trunk native 
vlan
• show interfaces 
switchport
• no switchport access vlan 
vlan_id
• show interfaces trunk
• show interfaces int_id 
trunk
