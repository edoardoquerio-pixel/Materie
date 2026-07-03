# InterVLAN Routing

## Panoramica
Titolo del modulo: Routing inter-VLAN

## Argomenti trattati
Configurazione, Reti, Data Analytics

---
## Appunti

Routing inter-VLAN
Obiettivi del modulo
Titolo del modulo: Routing inter-VLAN
Obiettivo del modulo: Risolvere i problemi di routing inter-VLAN sui dispositivi di Layer 3
Titolo argomento
Obiettivo argomento
Funzionamento del routing interVLAN
Descrivere le opzioni per la configurazione del routing
Routing inter-VLAN router-on-a-stick Configurare il router-on-a-stick inter-VLAN routing.
Routing inter-VLAN utilizzando
Configurare il routing inter-VLAN utilizzando lo
switching Layer 3
Risoluzione dei problemi relativi al
routing inter-VLAN
Risolvere i problemi comuni di configurazione tra
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Funzionamento del routing
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Funzionamento del routing inter-VLAN
Cos'è il routing inter-VLAN?
Le VLAN vengono utilizzate per segmentare le reti Layer 2 commutate per una serie di motivi.
Indipendentemente dal motivo, gli host in una VLAN non possono comunicare con gli host in un'altra
VLAN a meno che non sia presente un router o uno switch Layer 3 per fornire servizi di routing.
Il routing inter-VLAN è il processo di inoltro del traffico di rete da una VLAN a un'altra VLAN.
Esistono tre opzioni di routing inter-VLAN:
• Routing inter-VLAN legacy - Questa è una soluzione legacy. Ha una scalabilità minima.
• Router-on-a-stick - Questa è una soluzione accettabile per una rete di piccole e medie
• Switch di livello 3 utilizzando interfacce virtuali commutate (SVI) - Questa è la soluzione più
scalabile per organizzazioni di medie e grandi dimensioni.
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Funzionamento del routing inter-VLAN
Routing legacy inter-VLAN
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
Funzionamento del routing inter-VLAN
Routing router-on-a-stick inter-VLAN
Il metodo di routing inter-VLAN "router-on-a-stick" supera la limitazione del metodo di routing inter-VLAN
legacy. Richiede solo un'interfaccia Ethernet fisica per instradare il traffico tra più VLAN su una rete.
• Un'interfaccia Ethernet router Cisco IOS è configurata come un trunk 802.1Q e collegata a una porta
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
Funzionamento del routing inter-VLAN
Routing inter-VLAN su uno switch di Layer 3
Il metodo moderno per eseguire il routing inter-VLAN consiste nell'utilizzare gli switch di Layer 3 e le
interfacce virtuali commutate (SVI). Un SVI è un'interfaccia virtuale configurata su uno switch Layer 3,
come mostrato nella figura.
Nota: Uno switch Layer 3 è anche chiamato interruttore multilayer in quanto opera al Layer 2 e al Layer
3. Tuttavia, in questo corso usiamo il termine switch Layer 3.
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Funzionamento del routing inter-VLAN
Routing inter-VLAN su uno switch di Layer 3 (seguito)
Gli SVI inter-VLAN vengono creati nello stesso modo in cui viene configurata l'interfaccia VLAN di
gestione. L'SVI viene creato per una VLAN esistente sullo switch. Anche se virtuale, l'SVI svolge le
stesse funzioni per la VLAN come farebbe un'interfaccia router. In particolare, fornisce l'elaborazione

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_InterVLAN_Routing.md*
