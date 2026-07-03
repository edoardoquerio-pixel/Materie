# ITS-ICT 2025-2027-CloudSpecialist Microservices intro

## Panoramica
UF: Containers-Microservices-Servlerless

## Argomenti trattati
Cloud, Git, Reti, Programmazione, API REST

---
## Appunti

2025-2027 Cloud specialist
UF: Containers-Microservices-Servlerless
Docente: Denis Maggiorotto
Denis Maggiorotto
Denis Maggiorotto
• Managing Director and shareholder @ Sunnyvale S.r.l.
20 years of experience in ICT consulting
Senior Software / Enterprise Architect @ Major companies in public
utility, telco, TV broadcasting and banking sector
• Oracle University Principal Instructor regarding Java technologies
(Micro Edition, Standard Edition and Enterprise Edition) and Oracle's
middleware products.
Independent IT professional trainer and public speaker
Denis Maggiorotto
denis.maggiorotto@its-ictpiemonte.it
https://www.linkedin.com/in/denismaggiorotto/
https://github.com/denismaggior8
L'architettura software a microservizi si riferisce ad una tecnica per
progettare applicazioni flessibili ed altamente scalabili,
scomponendo il software in servizi discreti che implementano
specifiche funzioni di business.
Questi servizi possono quindi essere sviluppati, distribuiti e scalati
in modo indipendente.
Ogni microservizio comunica con altri servizi tramite API
(Application Programming Interface) e protocolli standardizzati, e
possono essere scritti in linguaggi differenti o con tecnologie
Ciò differisce completamente dai sistemi costruiti con strutture
monolitiche, in cui i servizi erano inestricabilmente interconnessi, e
potevano essere scalati solo insieme.
Poiché ogni servizio ha una funzionalità ben precisa, è molto più
piccolo in termini di dimensioni e complessità.
Il termine microservizio deriva da questo progetto di funzionalità
discreta, non dalla sua dimensione fisica.
L’architettura a microservizi arriva per risolvere le problematiche di altre due
architettura molto utilizzate in precedenza (e in alcuni casi utilizzate ancora
SOA (Service Oriented Architecture)
Un po’ di storia
Architettura monolitica
L’architettura originale, dalla quale sono derivate le altre
Tutte le componenti software vengono eseguite in un singolo
Non vi è alcun tipo di distribuzione delle sue componenti
Tutte le classi, le librerie ed altre componenti del software
hanno un alto livello di dipendenza fra loro
Spesso ci si riferisce a questi tipi di software col termine «Silo»
Architettura monolitica
Architettura monolitica
Spesso questi software non espongono nessuna interfaccia per
essere utilizzati da altri software (API)
Architettura monolitica
Architettura monolitica
Processo di sviluppo waterfall
Il modello waterfall è una scomposizione delle attività di progetto in fasi
sequenziali e lineari, in cui ciascuna fase dipende dai risultati conseguiti
dalla precedente e costituisce il prerequisito per la fase successiva.
L'approccio è tipico del modello architetturale monolitico.
Nello sviluppo del software, tende ad essere tra gli approcci meno iterativi
e flessibili, poiché il progresso scorre in gran parte in una direzione ("verso il
basso" come una cascata) attraverso le fasi di ideazione, avvio, analisi,
progettazione, costruzione, test, implementazione e manutenzione .
Processo di sviluppo waterfall
Vantaggi architettura monolitica
Più facile da progettare (no rete, no latenza, no protocolli di
comunicazione, tutto in un singolo processo)
E’ più performante (no latenze di rete, no overhead per
serializzazione/deserializzazione oggetti, etc)
E’ più facile da gestire (file di log centralizzati, unico processo da
Service Oriented Architecture (SOA)
Il termine fu coniano nel 1998
Le applicazioni sono composte da processi che espongono servizi al
Ogni servizio «pubblicizza» le proprie funzionalità tramite file
contenenti metadati
E’ modello architetturale che si basa molto sugli standard XML, XML
Schema, XSLT, SOAP, WSDL, etc…
Spesso viene fatto uso di Enterprise Service Bus (ESB) per mediare tra
client e servizi o tra un servizio e l’altro (autenticazione, trasformazione,
adattamento di protocollo)
Service Oriented Architecture (SOA)
Service Oriented Architecture (SOA)
Vantaggi architettura SOA
Dati e funzionalità vengono condivisi in modalità standard

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 2025_ITS-ICT_2025-2027-CloudSpecialist_Microservices_intro.md*
