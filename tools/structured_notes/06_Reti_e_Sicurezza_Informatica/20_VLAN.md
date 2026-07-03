# VLAN

## Panoramica
Titolo del modulo: Protocolli e modelli

## Argomenti trattati
Reti, Configurazione, Sicurezza, API REST, Data Analytics

---
## Appunti

Obiettivi del modulo
Titolo del modulo: Protocolli e modelli
Obiettivo del modulo: Spiegare come i protocolli di rete consentono ai dispositivi di accedere alle
risorse di rete locali e remote.
Titolo argomento
Obiettivo argomento
Panoramica sulle VLAN
Spiegare lo scopo delle VLAN in una rete commutata.
VLAN in un ambiente multiswitch
Spiegare come uno switch inoltra i frame basati sulla
configurazione VLAN in un ambiente multi-switch.
Configurazione della VLAN
Configurare una porta switch da assegnare a una VLAN in base ai
Configurare una porta trunk su uno switch LAN.
Protocollo trunking dinamico Configurare il protocollo DTP (Dynamic Trunking Protocol).
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Panoramica sulle VLAN
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
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
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Panoramica sulle VLAN
Vantaggi di una
progettazione VLAN
I vantaggi dell'utilizzo delle VLAN
sono i seguenti:
Domini di broadcast
La divisione della LAN riduce il numero di domini broadcast
Maggiore sicurezza
Solo gli utenti della stessa VLAN possono comunicare insieme
Maggiore efficienza IT
Le VLAN possono raggruppare dispositivi con requisiti simili, ad esempio
facoltà e studenti
Riduzione dei costi
Uno switch può supportare più gruppi o VLAN
Prestazioni migliorate
I domini broadcast di piccole dimensioni riducono il traffico, migliorando la
larghezza di banda
Gestione semplificata
Gruppi simili avranno bisogno di applicazioni simili e altre risorse di rete
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Panoramica sulle VLAN
VLAN predefinita
La VLAN 1 è la seguente:
• La VLAN predefinita
• La VLAN nativa predefinita
• La VLAN di gestione
Impossibile eliminare o
Nota: Sebbene non sia
possibile eliminare VLAN1,
Cisco consiglia di assegnare
queste funzionalità predefinite
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Panoramica sulle VLAN
Tipi di VLAN (seguito)
• Dedicata al traffico generato dall'utente (email e traffico web).
• VLAN 1 è la VLAN dati predefinita perché tutte le interfacce sono assegnate a questa VLAN.
• Questa viene utilizzata solo per i collegamenti trunk.
• Tutti i frame sono contrassegnati su un collegamento trunk 802.1Q tranne quelli sulla VLAN
VLAN di gestione
• Questa viene utilizzata per il traffico SSH/Telnet VTY e non deve essere trasportata con il
traffico dell'utente finale.
• In genere, la VLAN che è SVI per lo switch Layer 2.

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_VLAN.md*
