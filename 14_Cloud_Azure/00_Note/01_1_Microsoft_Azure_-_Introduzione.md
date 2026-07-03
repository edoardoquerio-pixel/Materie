# 1) Microsoft Azure - Introduzione

**File:** `1) Microsoft Azure - Introduzione.pptx`
**Tipo:** `.pptx`
**Dimensione:** 81.6 KB
**Ultima modifica:** 02/07/2026 09:12

---

DOCENTE
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Introduzione (4 ore)

---

Microsoft Azure — Introduzione
Corso Cloud Specialist · ITS ICT
Cosa faremo in 100 ore
•  Sostenibilità e IT — smart working, smart grid, sensori, RAEE, economia circolare
•  Fondamenti di Azure — regioni, responsabilità condivisa, ARM, strumenti di accesso
•  Identity & Governance — Entra ID, MFA, RBAC, PIM, Azure Policy
•  Reti su Azure — VNet, NSG, VPN, ExpressRoute, Load Balancer, Firewall, Bastion
•  Compute & Container — VM, App Service, AKS, Functions, ottimizzazione costi
•  Storage, Data & Integration — Blob, File, database gestiti, Cosmos DB, Data Factory
•  Security & Business Continuity — Defender for Cloud, Key Vault, backup, DR
•  DevOps, IaC & Monitoraggio — ARM/Bicep, Terraform, CI/CD, Monitor, Cost Management

---

Oggi: introduzione (4 ore)
•  Perché questo corso esiste
•  IT e sostenibilità: il contesto normativo e tecnologico
•  Smart working, smart grid, sensori ambientali
•  Economia circolare e gestione RAEE
•  Dal data center al cloud: il collegamento
•  Cos'è il cloud, come funziona, chi lo offre
•  Primo sguardo ad Azure

---

Perché un corso su Azure
•  Il cloud è l'infrastruttura standard per aziende di ogni dimensione
•  Le competenze cloud sono tra le più richieste nel mercato IT
•  Azure è la piattaforma cloud di Microsoft — la seconda per quota di mercato globale
•  Un Cloud Specialist deve saper progettare, distribuire e gestire servizi su Azure
•  100 ore: dall'architettura di base fino a DevOps e gestione dei costi

---

IT e sostenibilità: il quadro
•  L'Unione Europea ha fissato obiettivi di riduzione delle emissioni al 2030 e 2050
•  Il settore IT è responsabile di circa il 2-4% delle emissioni globali di CO₂
•  Allo stesso tempo, l'IT è uno strumento per ridurre consumi ed emissioni in altri settori
•  La normativa europea (Green Deal, CSRD, tassonomia) impone obblighi di rendicontazione
•  Per un tecnico IT, capire questo contesto non è opzionale: è parte del lavoro

---

Smart working: tecnologie e impatto
•  Lavorare da remoto richiede infrastruttura IT: VPN, strumenti di collaborazione, sicurezza degli endpoint
•  Riduce spostamenti, quindi emissioni da trasporto
•  Richiede connettività affidabile e gestione centralizzata dei dispositivi
•  Strumenti tipici: Microsoft 365, Teams, VDI (Virtual Desktop Infrastructure)
•  Lato IT: il perimetro di sicurezza si sposta dall'ufficio al singolo dispositivo
•  Il cloud abilita lo smart working perché i servizi sono raggiungibili ovunque

---

Smart grid: la gestione IT delle reti energetiche
•  Una smart grid è una rete elettrica che usa sensori, comunicazione e software per gestire la distribuzione dell'energia
•  L'IT serve a raccogliere dati dai contatori, prevedere i consumi, bilanciare domanda e offerta
•  Tecnologie coinvolte: protocolli di comunicazione (MQTT, AMQP), piattaforme IoT, database time-series
•  Il cloud fornisce la capacità di calcolo e archiviazione necessaria per elaborare grandi volumi di dati in tempo reale
•  In Italia: il contatore elettronico di seconda generazione (2G) è un esempio concreto di smart metering

---

Sensori in rete per il monitoraggio ambientale
•  Sensori distribuiti misurano qualità dell'aria, temperatura, umidità, livello delle acque, rumore
•  I dati vengono trasmessi via rete (LoRaWAN, NB-IoT, 4G/5G) a piattaforme centrali
•  Il ruolo dell'IT: raccolta, validazione, archiviazione, visualizzazione e alerting
•  Volumi di dati potenzialmente molto alti → servono soluzioni scalabili
•  Il cloud è la scelta naturale: si paga in base all'uso, si scala con la domanda
•  Servizi Azure coinvolti: IoT Hub, Stream Analytics, Azure Maps

---

Economia circolare: principi fondamentali
•  Modello lineare: estrai → produci → usa → butta
•  Modello circolare: progetta per durare, ripara, riusa, ricicla
•  La normativa UE spinge verso la circolarità (Regolamento Ecodesign, Direttiva Right to Repair)
•  Per l'IT questo significa:
      ○  Progettare software che giri su hardware meno recente
      ○  Prolungare la vita utile dei dispositivi con aggiornamenti e manutenzione
      ○  Scegliere fornitori cloud che usino energia rinnovabile
      ○  Monitorare e ridurre il consumo delle risorse computazionali

---

Estendere la vita utile di prodotti e componenti
•  Un server fisico ha una vita utile media di 4-5 anni; spesso viene dismesso prima del necessario
•  Il ricondizionamento (refurbishing) è una pratica consolidata per PC, monitor, smartphone
•  Lato software: supporto a lungo termine (LTS), compatibilità con hardware datato, aggiornamenti di sicurezza
•  La virtualizzazione ha già allungato la vita dei server: più carichi su meno macchine fisiche
•  Il cloud porta questo concetto oltre: il fornitore gestisce il ciclo di vita dell'hardware, il cliente usa solo il servizio
•  Microsoft ha programmi di riuso e riciclo per l'hardware dei propri data center (Circular Centers)

---

RAEE: gestione dei rifiuti elettronici
•  RAEE = Rifiuti di Apparecchiature Elettriche ed Elettroniche
•  In Italia la normativa di riferimento è il D.Lgs. 49/2014, che recepisce la Direttiva 2012/19/UE
•  I produttori hanno l'obbligo di finanziare raccolta e smaltimento (responsabilità estesa del produttore)
•  I rifiuti IT contengono materiali preziosi (oro, rame, terre rare) ma anche sostanze pericolose (piombo, mercurio)
•  Lo smaltimento corretto richiede centri autorizzati e tracciabilità
•  Per chi lavora nell'IT: ogni dismissione di hardware deve seguire queste regole
•  Il passaggio al cloud riduce la quantità di hardware da gestire localmente, ma non elimina il problema

---

Dal data center al cloud
•  Tradizionalmente ogni azienda gestiva i propri server in un locale tecnico o in un data center
•  Questo significa: acquisto hardware, alimentazione, raffreddamento, manutenzione, personale dedicato
•  Problemi: costi fissi alti, capacità spesso sovradimensionata, tempi lunghi per scalare
•  Il cloud computing sposta tutto questo presso un fornitore esterno
•  Il cliente usa i servizi via rete e paga in base al consumo
•  Il fornitore gestisce hardware, alimentazione, rete, sicurezza fisica, aggiornamenti
•  Non è una novità: il modello esiste dagli anni 2000, ma è diventato dominante nell'ultimo decennio

---

Cos'è il cloud in pratica
•  Un insieme di data center distribuiti nel mondo, gestiti da un fornitore
•  Il cliente accede a risorse (server, storage, database, reti) tramite Internet o connessioni dedicate
•  Le risorse si creano e si eliminano in minuti, non in settimane
•  Si paga a consumo (pay-as-you-go) oppure con impegni a 1-3 anni per risparmiare
•  Cinque caratteristiche essenziali (definizione NIST):
      ○  Self-service on demand
      ○  Accesso via rete
      ○  Pool di risorse condivise
      ○  Elasticità rapida
      ○  Servizio misurabile

---

I tre modelli di servizio
IaaS — Infrastructure as a Service
•  Il fornitore offre macchine virtuali, rete, storage
•  Il cliente gestisce sistema operativo, applicazioni, dati
•  Massima flessibilità, massima responsabilità
PaaS — Platform as a Service
•  Il fornitore gestisce anche il sistema operativo e il runtime
•  Il cliente distribuisce il proprio codice o le proprie configurazioni
•  Meno controllo, meno lavoro di gestione
SaaS — Software as a Service
•  Il fornitore offre l'applicazione pronta all'uso
•  Il cliente la usa e basta (es. Microsoft 365, Gmail)

---

Cloud pubblico, privato, ibrido
Cloud pubblico
•  Risorse condivise tra più clienti, gestite dal fornitore
•  Nessun investimento iniziale in hardware
•  Adatto alla maggior parte dei carichi di lavoro
Cloud privato
•  Infrastruttura dedicata a un singolo cliente
•  Può essere on-premises o ospitata presso un fornitore
•  Richiesto quando ci sono vincoli normativi o di sicurezza stringenti
Cloud ibrido
•  Combinazione di cloud pubblico e privato
•  I carichi si spostano tra i due ambienti in base alle esigenze
•  È il modello più diffuso nelle grandi organizzazioni

---

Responsabilità condivisa
•  Nel cloud la sicurezza e la gestione sono divise tra fornitore e cliente
•  Il fornitore si occupa di: hardware, rete fisica, data center, hypervisor
•  Il cliente si occupa di: dati, identità, configurazione dei servizi, accessi
Livello
IaaS
PaaS
SaaS
Dati e accessi
Cliente
Cliente
Cliente
Applicazione
Cliente
Cliente
Fornitore
Sistema operativo
Cliente
Fornitore
Fornitore
Rete e infrastruttura
Fornitore
Fornitore
Fornitore
Data center fisico
Fornitore
Fornitore
Fornitore
•  Regola pratica: più il servizio è gestito, meno responsabilità ha il cliente — ma meno controllo

---

Perché Azure
•  Seconda piattaforma cloud per quota di mercato globale (dopo AWS)
•  Integrazione nativa con l'ecosistema Microsoft: Active Directory, Windows Server, SQL Server, Microsoft 365
•  Presente in oltre 60 regioni nel mondo, con data center anche in Italia (Milano, dal 2020)
•  Offre oltre 200 servizi: compute, storage, database, AI, IoT, DevOps, sicurezza
•  Modello di licenza flessibile: pay-as-you-go, Reserved Instances, Savings Plans
•  Certificazioni di conformità: ISO 27001, SOC 1/2/3, GDPR, AgID (per la PA italiana)
•  Strumenti di gestione: portale web, CLI, PowerShell, SDK in tutti i linguaggi principali

---

L'ecosistema Azure: una mappa (1/2)
Infrastruttura
•  Regioni, Availability Zones, resource group, subscription, tenant
Identità e sicurezza
•  Microsoft Entra ID, RBAC, Conditional Access, Key Vault, Defender for Cloud
Rete
•  Virtual Network, NSG, VPN Gateway, ExpressRoute, Load Balancer, Firewall

---

L'ecosistema Azure: una mappa (2/2)
Compute
•  Virtual Machines, App Service, Azure Functions, Container Instances, AKS
Dati
•  Storage Account (Blob, File, Queue, Table), Azure SQL, PostgreSQL, Cosmos DB
Gestione e automazione
•  Azure Monitor, Log Analytics, ARM/Bicep, Terraform, Azure DevOps, Cost Management

---

Riepilogo
•  L'IT ha un ruolo attivo nella sostenibilità: smart working, smart grid, monitoraggio ambientale, gestione RAEE
•  L'economia circolare si applica anche ai prodotti IT
•  Il cloud computing sostituisce l'infrastruttura locale con servizi on-demand
•  Tre modelli di servizio: IaaS, PaaS, SaaS — ognuno con un diverso livello di responsabilità
•  Cloud pubblico, privato o ibrido in base alle esigenze
•  Azure è la piattaforma su cui lavoreremo per le restanti 96 ore
•  Nelle prossime lezioni: architettura Azure, identity, reti, compute, storage, sicurezza, DevOps
