# Cloud Azure — Quaderno di Appunti

> **Materia:** 14_Cloud_Azure
> **Data generazione:** Febbraio 2026
> **Corso:** ITS ICT Cloud Specialist 2025-2027

---

## Indice delle Sessioni

1. [1 Microsoft Azure - Introduzione](#1-microsoft-azure---introduzione)
2. [10 Microsoft Azure -Compute su Azure - Dischi scalabilità e costo delle VM](#10-microsoft-azure--compute-su-azure---dischi-scalabilità-e-costo-delle-vm)
3. [11 Microsoft Azure - Compute su Azure - App Service e Functions](#11-microsoft-azure---compute-su-azure---app-service-e-functions)
4. [12 Microsoft Azure - Compute su Azure - Container AKS e ottimizzazione](#12-microsoft-azure---compute-su-azure---container-aks-e-ottimizzazione)
5. [13 Microsoft Azure - Storage Data Integration - Storage e Sicurezza](#13-microsoft-azure---storage-data-integration---storage-e-sicurezza)
6. [14 Microsoft Azure - Storage Data Integration - Protezione dati e file service](#14-microsoft-azure---storage-data-integration---protezione-dati-e-file-service)
7. [15 Microsoft Azure - AI su Azure - Foundry modelli e GitHub Copilot](#15-microsoft-azure---ai-su-azure---foundry-modelli-e-github-copilot)
8. [16 Microsoft Azure - Storage Data Integration - Database gestiti Cosmos DB e Dat](#16-microsoft-azure---storage-data-integration---database-gestiti-cosmos-db-e-dat)
9. [17 Microsoft Azure - Security Reliability e Business Continuity - PT1 - Defender](#17-microsoft-azure---security-reliability-e-business-continuity---pt1---defender)
10. [18 Microsoft Azure - Security Reliability e Business Continuity - PT2 - Backup D](#18-microsoft-azure---security-reliability-e-business-continuity---pt2---backup-d)
11. [2 Microsoft Azure - Architettura e Strumenti di Accesso Parte 1](#2-microsoft-azure---architettura-e-strumenti-di-accesso-parte-1)
12. [3 Microsoft Azure - Architettura e Strumenti di Accesso Parte 2](#3-microsoft-azure---architettura-e-strumenti-di-accesso-parte-2)
13. [4 Microsoft Azure - Identity e Governance Parte 1](#4-microsoft-azure---identity-e-governance-parte-1)
14. [5 Identity e Governance - Parte 2](#5-identity-e-governance---parte-2)
15. [6 Reti su Azure - Parte 1](#6-reti-su-azure---parte-1)
16. [7 Microsoft Azure - Reti su Azure - Parte 2](#7-microsoft-azure---reti-su-azure---parte-2)
17. [8 Microsoft Azure - Reti su Azure - Parte 3](#8-microsoft-azure---reti-su-azure---parte-3)
18. [9 Microsoft Azure - Compute su Azure - VM immagini e dimensionamento](#9-microsoft-azure---compute-su-azure---vm-immagini-e-dimensionamento)

---

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


---

# 10) Microsoft Azure -Compute su Azure - Dischi, scalabilità e costo delle VM

**File:** `10) Microsoft Azure -Compute su Azure - Dischi, scalabilità e costo delle VM.pptx`
**Tipo:** `.pptx`
**Dimensione:** 72.9 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Compute su Azure: dischi, scalabilità e costo delle VM (4 ore)

---

Compute su Azure
Dischi, scalabilità e costo delle VM

---

Da dove proseguiamo
•  abbiamo già visto come si sceglie una VM: immagine, size, regione, disponibilità
•  adesso guardiamo che cosa cambia davvero prestazioni e costo nel tempo
•  i punti chiave sono dischi, ridimensionamento, scale set e scelte di spesa
•  la domanda è pratica: questa VM basta, costa il giusto, cresce bene?

---

Perché il disco conta
•  il disco non è solo spazio
•  influenza velocità di avvio, risposta dell'app e costo della VM
•  un disco lento può frenare anche una VM ben dimensionata
•  per questo compute e storage si leggono insieme

---

Tipi di disco in Azure
Tipo
Uso tipico
Standard HDD
casi economici e poco intensi
Standard SSD
uso base con latenza più stabile
Premium SSD
VM applicative e workload più reattivi
Ultra Disk
casi molto esigenti su IOPS e throughput
•  non tutti i tipi servono in ogni scenario

---

Standard, Premium, Ultra
•  Standard: costa meno, va bene per test o carichi leggeri
•  Premium: è il riferimento quando conta la reattività
•  Ultra: serve solo per workload molto spinti
•  la scelta va fatta sul bisogno reale, non sul livello più alto disponibile

---

OS disk e data disk
•  il OS disk contiene sistema operativo e avvio della VM
•  i data disk ospitano dati, log o parti dell'applicazione
•  separarli aiuta a gestire meglio prestazioni e crescita
•  non tutto deve stare sul disco del sistema

---

Caching: che cosa significa
•  il caching usa memoria locale dell'host per accelerare alcuni accessi al disco
•  può essere utile in lettura o in lettura/scrittura, secondo il caso
•  non è una spunta magica: va allineato al comportamento del carico
•  prima capisco l'uso del disco, poi scelgo il caching

---

Encryption dei dischi
Opzione
Significato
SSE
cifratura dei dati a riposo
PMK
chiavi gestite dalla piattaforma Azure
CMK
chiavi gestite dal cliente, di solito via Key Vault
•  il punto comune è proteggere i dati memorizzati sui dischi

---

Ridimensionare una VM
•  una VM può cambiare size se la stima iniziale non era corretta
•  aumentare o ridurre la taglia è il primo passo di right-sizing
•  non sempre serve creare una nuova macchina
•  prima misuro il bisogno, poi cambio dimensione

---

Scale up e scale out
Se faccio...
Sto facendo...
dare più risorse a una VM
Scale up
usare più istanze simili
Scale out
•  lo scale up è più semplice
•  lo scale out richiede un'app più distribuita
•  entrambi impattano costo e disponibilità

---

Virtual Machine Scale Set
•  uno Scale Set gestisce più VM simili come un gruppo
•  serve quando più istanze fanno lo stesso lavoro
•  può crescere o ridursi con regole di autoscaling
•  è il passaggio naturale quando una sola VM non basta più

---

Costo compute: che cosa incide
•  la size della VM pesa molto sul costo orario
•  contano anche dischi, tempo di accensione e numero di istanze
•  una VM accesa ma poco usata resta comunque una spesa
•  ottimizzare vuol dire usare risorse proporzionate

---

Right-sizing, RI e Savings Plans
•  Right-sizing: scegliere o correggere la taglia giusta
•  Reserved Instances: convenienza se il carico è stabile nel tempo
•  Savings Plans: più flessibili quando l'uso cambia tra servizi compute
•  prima osservo i consumi, poi scelgo l'impegno di spesa

---

Dove guardare nel portale
•  Virtual machines -> VM -> Size: taglia e cambio dimensione
•  Virtual machines -> VM -> Disks: OS disk, data disk, tipo disco
•  Virtual machine scale sets: gruppi di VM simili
•  Cost Management + Billing: lettura dei costi complessivi
•  con account limitati alcune opzioni possono non essere disponibili

---

Chiusura del blocco
•  non basta scegliere una VM: bisogna leggere anche dischi, crescita e spesa
•  Standard, Premium e Ultra rispondono a bisogni diversi
•  Scale Set serve quando il carico chiede più istanze uguali
•  il passo successivo è passare dal compute IaaS al compute gestito


---

# 11) Microsoft Azure - Compute su Azure - App Service e Functions

**File:** `11) Microsoft Azure - Compute su Azure - App Service e Functions.pptx`
**Tipo:** `.pptx`
**Dimensione:** 72.9 KB
**Ultima modifica:** 02/07/2026 09:28

---

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Compute su Azure: App Service e Functions (4 ore)

---

Compute su Azure
App Service e Functions

---

Dalla VM al servizio gestito
•  con una VM gestisci sistema operativo, patch, runtime e applicazione
•  con App Service porti soprattutto codice e configurazione
•  con Functions porti funzioni che si attivano a evento
•  il cambio di logica è: meno server da gestire, più focus sull'applicazione

---

App Service: idea base
•  App Service pubblica web app e API senza gestire una VM
•  Azure gestisce OS, runtime, patching e integrazione con la piattaforma
•  tu gestisci codice, configurazione, dominio, scaling e osservabilità
•  è una scelta tipica quando l'app è web o HTTP API

---

App Service Plan
•  il piano decide dove gira l'app e quante risorse usa
•  più app possono condividere lo stesso piano
•  cambiare piano cambia capacità, costo e funzionalità disponibili
•  l'app è il sito; il piano è la capacità che lo ospita

---

Web App e API App
Caso
Servizio
sito web o backend HTTP
Web App
API consumata da app o servizi
API App
•  nella pratica entrambe stanno dentro il modello App Service
•  la distinzione aiuta a ragionare sul tipo di applicazione

---

Deployment slot
•  uno slot è un ambiente parallelo alla produzione
•  esempio: production e staging
•  puoi pubblicare una versione nuova nello slot di test
•  poi fai swap per portarla in produzione con meno rischio

---

Scaling in App Service
•  Scale up: cambio piano o capacità del piano
•  Scale out: aumento il numero di istanze
•  l'autoscale può reagire a metriche come CPU o richieste
•  il costo segue il piano e le istanze usate

---

Quando scegliere App Service
•  applicazioni web e API
•  deploy frequenti e gestione semplice
•  integrazione con domini, certificati, log e scaling
•  quando non serve controllare direttamente il sistema operativo

---

Azure Functions: idea base
•  Azure Functions esegue codice in risposta a un evento
•  una funzione non è una web app intera
•  è un pezzo di logica che parte quando succede qualcosa
•  esempi: richiesta HTTP, messaggio in coda, timer, file caricato

---

Trigger e binding
Concetto
Significato
Trigger
evento che avvia la funzione
Input binding
dato letto dalla funzione
Output binding
destinazione su cui la funzione scrive
•  la funzione dichiara collegamenti che Azure gestisce per lei

---

Trigger comuni
Trigger
Esempio
HTTP
API leggera o webhook
Timer
attività pianificata
Queue
elaborare messaggi
Blob
reagire a un file caricato
•  il trigger racconta perché il codice parte

---

App Service o Functions?
Se devo...
Scelta naturale
tenere online un'app web o API
App Service
reagire a eventi separati
Functions
gestire OS e software specifico
VM
•  non sono livelli migliori o peggiori: rispondono a problemi diversi

---

Limiti pratici in aula
•  con Azure for Students alcune opzioni possono essere limitate
•  App Service e Functions sono più adatti a demo leggere rispetto ad AKS
•  se un piano o una regione non compare, si verifica prima subscription e disponibilità
•  l'obiettivo è leggere il modello, non forzare ogni creazione

---

Dove guardare nel portale
•  App Services: web app, piani, deployment slot, scaling
•  App Service plans: capacità condivisa e costo del piano
•  Function App: funzioni, trigger, configurazione
•  Application Insights: log e metriche applicative
•  Cost Management + Billing: costo dei piani e delle risorse

---

Chiusura del blocco
•  App Service riduce la gestione del server per web app e API
•  Functions esegue codice a evento con trigger e binding
•  rispetto alle VM perdi controllo sull'OS, ma guadagni semplicità operativa
•  il passo successivo è capire dove entrano container e Kubernetes


---

# 12) Microsoft Azure - Compute su Azure - Container, AKS e ottimizzazione

**File:** `12) Microsoft Azure - Compute su Azure - Container, AKS e ottimizzazione.pptx`
**Tipo:** `.pptx`
**Dimensione:** 72.3 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Compute su Azure: container, AKS e ottimizzazione (4 ore)

---

Compute su Azure
Container, AKS e ottimizzazione

---

Perché arriviamo ai container
•  una VM porta con sé sistema operativo e gestione completa
•  App Service riduce la gestione del server
•  il container impacchetta applicazione e dipendenze in modo ripetibile
•  il problema diventa: dove faccio girare quel container?

---

Container: idea base
•  un container contiene app, runtime e dipendenze
•  parte da un'immagine container
•  gira in modo più leggero di una VM completa
•  non sostituisce sempre la VM: risponde a un modello diverso di distribuzione

---

Container Instances
•  Azure Container Instances esegue container singoli senza gestire server
•  è adatto a prove rapide, job semplici o processi isolati
•  parti da un'immagine e Azure avvia il container
•  è il modo più diretto per eseguire un container su Azure

---

App Service for Containers
•  porta il modello App Service su applicazioni containerizzate
•  utile quando hai una web app dentro un container
•  mantieni funzionalità come dominio, scaling e gestione piattaforma
•  è un ponte tra PaaS web e mondo container

---

Quando serve Kubernetes
•  quando i container diventano molti
•  quando servono replica, aggiornamenti controllati e self-healing
•  quando l'app è composta da più servizi
•  Kubernetes organizza container su un cluster di nodi

---

AKS: Kubernetes gestito
•  AKS è Azure Kubernetes Service
•  Azure gestisce il piano di controllo Kubernetes
•  tu gestisci nodi, workload, networking e aggiornamenti applicativi
•  sotto ci sono VM, ma non le tratti come VM singole

---

Node pool
•  un node pool è un gruppo di nodi con caratteristiche simili
•  i nodi sono le macchine su cui girano i pod
•  puoi avere pool diversi per workload diversi
•  scegliere i nodi significa scegliere costo e capacità del cluster

---

Network in AKS
•  i pod devono comunicare tra loro
•  alcuni servizi devono essere raggiunti dall'esterno
•  entrano in gioco rete del cluster, servizi e ingress
•  qui tornano concetti già visti: subnet, IP, bilanciamento, sicurezza

---

Aggiornamenti in AKS
•  un cluster va aggiornato nel tempo
•  si aggiornano Kubernetes, nodi e applicazioni
•  gli aggiornamenti vanno pianificati per ridurre interruzioni
•  AKS semplifica, ma non elimina la responsabilità operativa

---

ACI, App Service for Containers, AKS
Se devo...
Scelta naturale
eseguire un container singolo
Container Instances
pubblicare una web app containerizzata
App Service for Containers
orchestrare molti container
AKS
•  la scelta dipende da complessità e responsabilità operativa

---

Ottimizzazione compute
•  scegli il servizio più semplice che risolve il problema
•  spegni o riduci ciò che non serve
•  usa scaling quando il carico cambia
•  misura prima di aumentare risorse
•  collega sempre prestazioni, disponibilità e costo

---

Riepilogo del blocco Compute
Scenario
Servizio
controllo completo dell'OS
VM
web app o API gestita
App Service
codice a evento
Functions
container singolo
Container Instances
orchestrazione container
AKS

---

Dove guardare nel portale
•  Container instances: container singoli
•  App Services: web app anche containerizzate
•  Kubernetes services: cluster AKS, node pool e aggiornamenti
•  Container registries: immagini container private
•  Cost Management + Billing: costo di VM, piani, funzioni e cluster

---

Chiusura del blocco
•  il compute Azure va da VM a PaaS, serverless e container
•  più sali di livello, meno gestisci server direttamente
•  più lo scenario è complesso, più cresce il bisogno di architettura e controllo
•  da qui il lavoro pratico è scegliere il servizio minimo adatto al caso


---

# 13) Microsoft Azure - Storage, Data Integration - Storage e Sicurezza

**File:** `13) Microsoft Azure - Storage, Data Integration - Storage e Sicurezza.pptx`
**Tipo:** `.pptx`
**Dimensione:** 72.6 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Storage, Data & Integration - PT1: Storage account, servizi dati, sicurezza e accesso storage (4 ore)

---

Storage account e servizi dati
•  Storage account: General Purpose v2 e Premium
•  Servizi disponibili: Blob, File, Queue, Table
•  Casi d'uso principali dei servizi dati e quando scegliere Azure Files
•  Criteri di scelta: prestazioni, latenza, costo e tipo di workload
•  Scelte iniziali: naming, regione e ridondanza del dato

---

Perché partiamo dallo storage account
•  Lo storage account è il contenitore logico dei principali servizi dati di base su Azure.
•  Dentro uno storage account puoi trovare Blob, File, Queue e Table.
•  Le scelte fatte all'inizio influenzano costo, prestazioni e resilienza.
•  Prima di creare i dati, conviene capire che tipo di workload stiamo servendo.
•  Il punto non è solo salvare dati: è scegliere il servizio giusto.

---

General Purpose v2 o Premium
Modello
Quando ha senso
General Purpose v2
scelta standard per la maggior parte dei workload
Premium
latenza più bassa e prestazioni più alte su scenari specifici
•  GPv2 è il punto di partenza naturale in quasi tutti i progetti.
•  Premium si usa quando il carico giustifica davvero il costo più alto.
•  La domanda giusta è: che prestazioni servono davvero?

---

I quattro servizi da ricordare
Servizio
A cosa serve
Blob
oggetti, file applicativi, immagini, log, backup
File
file share gestite con accesso tipo file server
Queue
messaggi semplici tra componenti
Table
dati NoSQL chiave-valore semplici
•  Lo stesso storage account può esporre più servizi.
•  Cambia il modello di accesso, non solo il nome.

---

Quando scegliere ciascun servizio
•  Blob se devi salvare file o oggetti non strutturati.
•  Azure Files se ti serve una share condivisa come servizio gestito.
•  Queue se devi disaccoppiare producer e consumer con messaggi semplici.
•  Table se ti basta un archivio NoSQL leggero e poco complesso.
•  Se il dato è relazionale o molto strutturato, di solito serve un servizio diverso.

---

Regione e ridondanza del dato
•  La regione conta per latenza, vicinanza agli utenti e conformità.
•  LRS tiene copie locali nello stesso datacenter.
•  ZRS distribuisce le copie su più zone della stessa regione.
•  GRS e varianti simili aggiungono replica geografica.
•  Più protezione significa spesso più costo e più complessità di scelta.

---

Nel wizard, cosa guardare davvero
•  Performance: Standard o Premium.
•  Redundancy: LRS, ZRS o replica geografica.
•  Region: dove vivrà davvero il dato.
•  Naming: regole semplici e nomi coerenti.
•  Public access e rete: da decidere subito, non solo dopo.

---

Sicurezza e accesso storage
•  Accesso ai dati: SAS, Shared Key e Managed Identity
•  Differenza tra credenziale applicativa e accesso operativo
•  Protezione rete con Firewall storage e regole VNET
•  Riduzione superficie esposta con accessi controllati e segmentazione

---

Perché la sicurezza storage è delicata
•  Lo storage contiene spesso file applicativi, dati aziendali, log e backup.
•  Se l'accesso è troppo ampio, il rischio non è solo leggere i dati ma anche modificarli o cancellarli.
•  Bisogna distinguere l'accesso degli amministratori da quello delle applicazioni.
•  L'obiettivo è ridurre privilegi, superficie esposta e segreti in chiaro.
•  Qui la parte tecnica e quella operativa si toccano davvero.

---

Tre modi comuni di dare accesso
Metodo
Logica
Shared Key
accesso pieno basato sulla chiave dell'account
SAS
accesso limitato per tempo, permessi e risorsa
Managed Identity
accesso senza segreti nel codice
•  La chiave account è potente ma anche rischiosa.
•  La SAS restringe meglio il perimetro.
•  La Managed Identity è spesso la scelta più pulita per i workload Azure.

---

Credenziale applicativa vs accesso operativo
•  Un'app non dovrebbe usare le stesse credenziali di un amministratore.
•  L'accesso operativo serve a gestire, verificare e correggere.
•  L'accesso applicativo serve solo a fare il lavoro minimo richiesto.
•  RBAC e ruoli dati aiutano a separare questi due piani.
•  Quando questa separazione manca, la sicurezza peggiora subito.

---

Firewall storage e rete
•  Uno storage account può essere aperto pubblicamente, limitato o chiuso alla rete pubblica.
•  Il firewall permette di limitare IP e reti autorizzate.
•  Le regole VNet restringono l'accesso ai workload interni autorizzati.
•  Se serve isolamento più forte, si entra con Private Endpoint.
•  La sicurezza non dipende solo dalla credenziale, ma anche dal percorso di rete.

---

Ridurre la superficie esposta
•  Preferire Managed Identity quando l'app gira su servizi Azure.
•  Usare SAS brevi e mirate invece di accessi troppo larghi.
•  Limitare o disabilitare l'accesso pubblico quando non serve.
•  Separare storage diversi per sensibilità e responsabilità.
•  Attivare log e auditing per lasciare tracce leggibili.

---

Nel portale, dove guardare
•  Access keys per capire se esistono chiavi account attive.
•  Shared access signature per generare accessi delegati.
•  IAM per ruoli e autorizzazioni.
•  Networking per firewall, reti selezionate e endpoint.
•  Qui si legge quasi tutto il perimetro di sicurezza dello storage.


---

# 14) Microsoft Azure - Storage, Data Integration - Protezione dati e file service

**File:** `14) Microsoft Azure - Storage, Data Integration - Protezione dati e file service.pptx`
**Tipo:** `.pptx`
**Dimensione:** 69.4 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Storage, Data & Integration: protezione dati, file service e backup (4 ore)

---

Storage, protezione dati e file service (4 ore)
•  Lifecycle, tiering e retention per governare costo e ciclo di vita del dato
•  Versioning, soft delete e immutabilita per protezione operativa e compliance
•  Azure Files con identita centralizzate e permessi a due livelli
•  Backup e recovery per continuita operativa verificabile

---

Blob tiering: Hot, Cool, Archive
Tier
Uso tipico
Hot
dati letti spesso
Cool
dati letti saltuariamente
Archive
dati rari, conservazione lunga
•  Il tier influenza costo di storage e costo/tempo di accesso
•  Non esiste tier migliore in assoluto: dipende dal comportamento del dato
•  La scelta corretta parte da frequenza reale di lettura

---

Lifecycle management e retention
•  Le regole lifecycle automatizzano spostamento e cancellazione blob
•  Condizioni comuni: età del dato, prefisso, tipo di contenuto
•  Vantaggio: meno operazioni manuali e costo più stabile nel tempo
•  Retention va allineata a esigenze operative e vincoli normativi
•  Lifecycle è una policy continua, non una attività una tantum

---

Versioning, soft delete e immutabilita
•  Versioning: mantiene storico delle modifiche ai blob
•  Soft delete: recupera cancellazioni accidentali in finestra definita
•  Immutabilita (WORM): blocca modifica/cancellazione per un periodo
•  Versioning e soft delete coprono errori operativi
•  WORM copre integrita forte, audit e requisiti di compliance

---

Protezione e costo: combinare le leve
Esigenza
Leva principale
ridurre costo nel tempo
lifecycle + tiering
recuperare errori utente
versioning + soft delete
garantire integrita legale
immutabilita WORM
•  Non si attiva tutto per default: si sceglie in base al rischio
•  La soluzione giusta e una combinazione coerente di controlli

---

Azure Files: quando usarlo
•  Azure Files fornisce file share SMB gestite nello Storage Account
•  Utile per workload che si aspettano condivisioni file classiche
•  Adatto a directory condivise, profili utente e applicazioni lift-and-shift
•  Se serve modello object/API, spesso e preferibile Blob Storage
•  La scelta dipende dal modo in cui l'app legge e scrive i dati

---

Identita centralizzate per Azure Files
•  Accesso integrabile con identita directory (AD DS o Entra in scenari compatibili)
•  Si riducono account locali e credenziali statiche
•  Gruppi e ruoli semplificano concessione e revoca accessi
•  Il controllo accessi diventa uniforme e tracciabile nel tempo
•  Obiettivo: governance chiara tra utenti, gruppi e risorse

---

Permessi: livello share e livello NTFS
•  Permessi share: definiscono chi puo accedere alla condivisione
•  Permessi NTFS: definiscono cosa puo fare dentro file e cartelle
•  Accesso effettivo = intersezione dei due livelli
•  Errore tipico: un livello corretto e l'altro errato
•  Verifica sempre entrambe le dimensioni prima del go-live

---

Backup, recovery e continuita operativa
•  Recovery Services Vault centralizza policy e operazioni di restore
•  Backup senza test di restore non garantisce recupero reale
•  RPO: perdita dati accettabile, RTO: tempo massimo di ripristino
•  Policy e retention devono essere coerenti con criticita servizio
•  Continuita operativa = tecnologia + procedure verificate

---

Scenario integrato: scelta guidata
Domanda
Scelta tecnica
dati poco letti ma da tenere
lifecycle verso Cool/Archive
rischio sovrascrittura/cancellazione
versioning + soft delete
requisito legale di integrita
immutabilita WORM
app che richiede file share SMB
Azure Files
requisito di recupero servizio
backup con Vault + test restore
•  Una architettura robusta nasce da esigenze esplicite e priorita chiare

---

Traccia tecnica di lavoro
•  Definire un caso d'uso con requisiti storage, protezione e recupero
•  Progettare policy lifecycle e strategia di protezione del dato
•  Progettare file share con identita centralizzate e permessi a due livelli
•  Definire backup, retention e piano di test restore
•  Documentare evidenze operative e motivazioni architetturali

---

Criteri di qualita della soluzione
•  Scelta corretta tra blob policy e file share in base al contesto d'uso
•  Livelli coerenti di protezione: operativo, integrita, recovery
•  Motivazioni tecniche chiare e leggibili anche per interlocutori non tecnici
•  Decisioni architetturali validate con verifiche pratiche


---

# 15) Microsoft Azure - AI su Azure - Foundry, modelli e GitHub Copilot

**File:** `15) Microsoft Azure - AI su Azure - Foundry, modelli e GitHub Copilot.pptx`
**Tipo:** `.pptx`
**Dimensione:** 67.4 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
AI su Azure: Foundry, modelli e GitHub Copilot (in preparazione all'evento Microsoft Build //localhost Torino) (4 ore)

---

AI su Azure
Foundry, modelli e GitHub Copilot: cosa c'è sotto le demo del Microsoft Build //localhost Torino

---

Argomenti
•  Dove sta l'AI nel catalogo Azure (AI Services, Azure OpenAI, Foundry)
•  Azure AI Foundry: risorsa, progetto, hub — cosa sono davvero
•  Deployare un modello (gpt-4o-mini) e usarlo dal playground
•  Chiamare il modello via endpoint + key (il ponte verso il codice)
•  GitHub Copilot e i modelli di Foundry
•  Agenti: il loop "ragiona → usa strumento → risponde" (cenni)
•  Responsible AI e costi a token
•  Filo conduttore: è tutta infrastruttura Azure che già conoscete

---

Dove sta l'AI nel catalogo Azure
•  Azure AI Services — modelli pronti via API: Vision, Language, Speech, Translator
•  Azure OpenAI — i modelli GenAI (GPT, ecc.) ospitati su Azure, con endpoint e key
•  Azure AI Foundry — l'hub di lavoro sopra i modelli: deploy, playground, agenti, RAG
“Stessa logica di sempre: una risorsa dentro un resource group, in una regione, con identità e accesso che già sapete gestire. L'AI non è un mondo a parte.”

---

Azure AI Foundry: i pezzi
•  Risorsa di Foundry — l'account (tipo AIServices) che contiene tutto
•  Progetto — l'area di lavoro dentro la risorsa: modelli, agenti, dati, valutazioni
•  Hub (versione classica) — workspace condiviso, costruito sopra Machine Learning
“Due esperienze convivono: la "Nuova fonderia" (risorsa + progetto) e l'hub classico. Stesso obiettivo, organizzazione diversa.”

---

Deployare un modello e provarlo
•  Dal catalogo (oltre 100 modelli: OpenAI, Llama, Mistral, Cohere…) si sceglie e si fa deploy.
•  Il deployment è il "modello pubblicato": ha un nome e si chiama da playground e API.
•  Per la demo: `gpt-4o-mini` — economico, veloce, multimodale.
•  Nel playground / Chat si prova subito: prompt → risposta.
•  Concetti da mostrare lì: system prompt (istruzioni), temperature, token.

---

Dal playground al codice
•  Il playground è comodo, ma in produzione si chiama il modello via API.
•  Servono due cose: l'endpoint della risorsa e una key (oppure Managed Identity).
curl "$ENDPOINT/openai/deployments/gpt-4o-mini/chat/completions?api-version=2024-08-01-preview" \
  -H "api-key: $KEY" -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"Ciao!"}]}'
“Stesso modello, stessa risposta del playground: cambia solo che ora lo chiama il tuo codice.”

---

GitHub Copilot e i modelli di Foundry
•  GitHub Copilot = assistente AI dentro l'editor (scrive, spiega, refattorizza codice).
•  Non è "un altro modello": dietro usa modelli (OpenAI e altri) e oggi può collegarsi a modelli ospitati su Azure / Foundry.
•  Vantaggio per l'azienda: stessi modelli, governance, billing e dati sotto il proprio tenant Azure.
•  Due usi complementari:
      ○  Copilot → produttività dello sviluppatore
      ○  modello via API/Foundry → AI dentro l'applicazione che costruisci

---

Agenti: oltre la singola risposta
•  Un agente non si limita a rispondere: ragiona → usa uno strumento → risponde.
•  Strumenti tipici: Code Interpreter (esegue codice), ricerca su dati/RAG, funzioni custom.
•  Esempio: "somma dei primi 50 numeri primi" → l'agente scrive ed esegue codice e poi spiega.
•  Agenti, routine e workflow: dal singolo agente a più passi orchestrati (routine ricorrenti, workflow multi-step e multi-agente).
•  È il loop "agentico" che vedremo all'evento (Foundry Agents).
•  Nota reale: creare agenti richiede il ruolo dati Foundry User sulla risorsa (RBAC).

---

Responsible AI e costi
•  Allucinazioni: il modello può affermare cose false con tono sicuro → serve verifica umana.
•  Bias e content filter: Azure applica filtri sui contenuti; l'AI Act UE classifica per rischio.
•  Dati: con Azure i prompt restano nel tuo tenant (governance, compliance).
•  Costi a token: i modelli Standard/GlobalStandard sono pay-per-token → da fermi non costano.
      ○  eccezione: i deployment Provisioned (PTU) riservano capacità e si pagano a ore.

---

Da portare a casa (e all'evento)
•  L'AI su Azure è una risorsa + un modello deployato: ci parli con endpoint e key, come ogni servizio.
•  Foundry è lo studio di lavoro attorno ai modelli: deploy, playground, agenti, RAG.
•  GitHub Copilot porta gli stessi modelli nell'editor, sotto la governance del tuo tenant.
•  Gli agenti aggiungono il loop ragiona→strumento→risponde.
•  Tutto poggia su ciò che già sappiamo: resource group, identità, RBAC, costi.
“All'evento (Build //localhost Torino) vedrete Foundry e Copilot costruire applicazioni AI: ora sapete cosa c'è sotto.”


---

# 16) Microsoft Azure - Storage, Data Integration - Database gestiti, Cosmos DB e Data Integration

**File:** `16) Microsoft Azure - Storage, Data Integration - Database gestiti, Cosmos DB e Data Integration.pptx`
**Tipo:** `.pptx`
**Dimensione:** 73.7 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Storage, Data & Integration: database gestiti, Cosmos DB e Data Integration (4 ore)

---

Dal database al flusso del dato
Database gestiti, Cosmos DB e integrazione dati: dove nasce il dato e dove deve arrivare

---

Argomenti (4 ore)
•  Perché un database gestito (PaaS) e cosa cambia nel modello operativo
•  Relazionali gestiti: Azure SQL (single/MI), PostgreSQL/MySQL Flexible
•  Continuità del servizio: backup, replica, HA, RPO/RTO
•  Cosmos DB: partizionamento, throughput, consistency levels
•  Quando relazionale e quando NoSQL distribuito
•  Il dato non vive da solo: integrazione con Data Factory
•  Pipeline, trigger, orchestrazione e cenni su Synapse

---

Perché scegliere un database gestito
•  Un database gestito riduce il lavoro su patching, backup e manutenzione di base.
•  Il team si concentra più sul dato e meno sul server del database.
•  Non elimina le scelte architetturali: sposta il livello del lavoro.
•  Alta disponibilità, backup e monitoraggio entrano più facilmente nel servizio.
•  È uno dei vantaggi più evidenti del cloud PaaS.

---

Database relazionali gestiti
•  Azure SQL Database — il database relazionale come servizio (single database).
•  Managed Instance — più vicino allo SQL Server tradizionale (migrazioni lift-and-shift).
•  PostgreSQL e MySQL Flexible Server — motori open source gestiti.
•  La scelta dipende da compatibilità applicativa, controllo richiesto e percorso di migrazione.
•  Il tema non è solo il motore: è il modello operativo.

---

Continuità del servizio
•  In un database gestito il tema non è solo scrivere query, ma tenere vivo il servizio.
•  Backup automatici, replica e opzioni HA riducono i rischi operativi.
•  La continuità cambia da servizio a servizio.
•  Va sempre letta insieme a RPO (quanto dato posso perdere) e RTO (in quanto torno su) e ai costi.
•  Il cloud aiuta, ma non sostituisce il ragionamento progettuale.

---

Cosmos DB: idea base
•  Cosmos DB è il servizio NoSQL distribuito di Azure.
•  Supporta più API e modelli di accesso (SQL/Core, MongoDB, Cassandra…).
•  Si usa quando servono scala elevata, bassa latenza e distribuzione globale.
•  Non è un sostituto automatico di ogni database relazionale.

---

Cosmos DB: i tre concetti chiave
•  Partizionamento — la partition key distribuisce i dati: una buona chiave = scala uniforme.
•  Throughput — capacità misurata in RU/s (Request Units), provisioned o serverless.
•  Consistency levels — dal più forte al più disponibile: Strong, Bounded staleness, Session, Consistent prefix, Eventual.
•  Sono leve di costo/prestazioni/coerenza: si scelgono in base al requisito, non a caso.

---

Relazionale o NoSQL
Modello
Quando tende a servire
Relazionale
schema stabile, query strutturate, transazioni forti
NoSQL distribuito
scala ampia, flessibilità, accesso globale e veloce
•  La scelta non è di moda, ma di requisito.
•  Il modello dati influenza sviluppo, costo e integrazione futura.

---

Il dato non vive mai da solo
•  I database entrano in flussi con applicazioni, code, ETL e analytics.
•  Per questo il tema non è solo il motore, ma anche l'integrazione.
•  Un database operativo e una piattaforma analytics hanno scopi diversi.
•  Il progetto vero inizia quando i dati devono muoversi tra servizi diversi.
“Da qui in poi passiamo dal "dove sta il dato" al "come si muove il dato".”

---

Perché serve integrazione dati
•  I dati arrivano da applicazioni, file, database, API e sistemi esterni.
•  Il problema non è solo salvarli, ma spostarli e coordinarli bene.
•  L'integrazione evita passaggi manuali fragili e poco tracciabili.
•  Nel cloud questo significa pipeline, trigger e orchestrazione.
•  Qui inizia il livello più sistemico del dato.

---

Data Factory: idea base
•  Azure Data Factory serve a costruire pipeline di integrazione.
•  Coordina attività tra sorgenti e destinazioni diverse.
•  Concetti base: pipeline, activity, linked service, dataset.
•  Non è un database, ma un motore di orchestrazione del flusso.
•  Il valore è nel movimento controllato del dato.

---

Trigger e orchestrazione
•  Un trigger decide quando parte una pipeline.
•  Può essere orario, ricorrente o legato a un evento.
•  L'orchestrazione mette in ordine i passaggi e le dipendenze.
•  Se un flusso ha più step, non basta copiare dati: bisogna coordinarli.
•  È qui che l'integrazione diventa processo, non solo trasferimento.

---

Synapse: dove entra
•  Synapse entra quando il focus si sposta verso analytics e workspace integrati.
•  Aiuta a collegare ingestione, query e consumo analitico.
•  Non sostituisce Data Factory in tutto, ma può lavorare insieme.
•  Il punto è distinguere orchestrazione del dato da analisi del dato.
•  Quando il progetto cresce, questi ruoli vanno separati bene.

---

Flusso tipico da leggere
•  i dati entrano da app, file o database
•  una pipeline li sposta o li prepara
•  lo storage o il layer analitico li riceve
•  report, query o altri servizi li consumano
•  Il valore non è il singolo servizio, ma il flusso completo.
•  La domanda giusta è sempre: dove nasce il dato e dove deve arrivare?

---

Quando usare cosa
•  Database gestito → il dato operativo dell'applicazione (relazionale o Cosmos).
•  Data Factory → quando il problema è orchestrare passaggi e spostamenti.
•  Synapse → quando il problema è analizzare i dati a livello più ampio.
•  Spesso non si escludono: collaborano.
•  L'integrazione dati è il ponte tra operativo e analitico.


---

# 17) Microsoft Azure - Security, Reliability e Business Continuity - PT1 - Defender e Key Vault

**File:** `17) Microsoft Azure - Security, Reliability e Business Continuity - PT1 - Defender e Key Vault.pptx`
**Tipo:** `.pptx`
**Dimensione:** 72.6 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Security, Reliability e Business Continuity - PT1: Defender for Cloud e Key Vault (4 ore)

---

Vedere il rischio e proteggere i segreti
Defender for Cloud per la postura, Key Vault per chiavi e credenziali

---

Argomenti (4 ore)
•  Defender for Cloud: posture management, workload protection, recommendations
•  Priorità del rischio: cosa guardare prima (esposizione, identity, patching)
•  Guest Configuration e vulnerability assessment come controllo continuo
•  Ridurre la superficie esposta: WAF, segmentazione, log ed evidenze
•  Key Vault: centralizzare segreti, chiavi e certificati
•  Accesso applicativo con Managed Identity e permessi minimi
•  Rotazione, scadenza, HSM e fiducia tra servizi (TLS/mTLS)

---

Perché partire da Defender for Cloud
•  La sicurezza cloud non si legge solo dal firewall o da una singola VM.
•  Serve una vista trasversale su configurazioni, rischi e priorità operative.
•  Defender for Cloud legge lo stato di sicurezza di subscription e risorse.
•  Il valore: vedere i problemi ricorrenti prima che diventino incidente.
•  La sicurezza diventa controllo continuo, non verifica occasionale.

---

Posture management e workload protection
Livello
Cosa guarda
Posture management
configurazioni, policy, esposizioni e hardening
Workload protection
minacce, vulnerabilità e segnali operativi
•  Il primo livello misura quanto l'ambiente è impostato bene.
•  Il secondo guarda cosa sta succedendo ai workload reali.
•  Le due letture servono insieme, non una al posto dell'altra.

---

Recommendations e priorità
•  Le recommendations mostrano configurazioni deboli o mancanti.
•  Non tutte pesano uguale: alcune riducono il rischio molto più di altre.
•  Leggere prima: esposizione pubblica, identity, patching, crittografia.
•  Il punto non è chiudere ticket, ma abbassare il rischio reale.
•  Serve sempre un ordine di priorità, non una lista piatta.

---

Guest Configuration e vulnerability assessment
•  Guest Configuration verifica che le VM rispettino le impostazioni attese.
•  Il vulnerability assessment evidenzia software e componenti deboli.
•  Servono a ridurre deriva configurativa e superfici note.
•  La sicurezza del workload non finisce al bordo della subnet.
•  Anche dentro la macchina vanno letti stato e conformità tecnica.

---

Ridurre la superficie e raccogliere evidenze
•  Meno porte aperte e meno endpoint pubblici = meno rischio.
•  WAF, segmentazione e regole mirate filtrano il traffico utile.
•  Principio guida: esporre solo ciò che serve davvero.
•  Activity Log e log diagnostici raccontano cosa è successo e dove.
•  Senza evidenze un incidente resta un sospetto: la sicurezza è anche lettura dei segnali.

---

Dal vedere il rischio al proteggere i segreti
•  Defender ci dice dove siamo esposti; ora vediamo come custodire ciò che è sensibile.
•  Una delle esposizioni più comuni: credenziali e chiavi sparse nel codice o nei file.
•  Il passo naturale è centralizzarle in un servizio dedicato: Azure Key Vault.
“Stesso obiettivo (ridurre il rischio), ma ora a livello di segreti e crittografia.”

---

Perché centralizzare segreti e chiavi
•  Segreti e chiavi sparsi nel codice o nei config aumentano il rischio.
•  Un servizio centrale rende chiari controllo accessi, rotazione e audit.
•  Azure Key Vault nasce per togliere le credenziali dai punti sbagliati.
•  L'obiettivo non è solo custodire il valore, ma governarne il ciclo di vita.

---

Segreti, chiavi e certificati
Oggetto
Uso tipico
Secret
password, connection string, token
Key
crittografia, firma, protezione dati
Certificate
TLS, identità del servizio, trust
•  Hanno tutti valore sensibile, ma scopi diversi.
•  Separarli bene aiuta a scegliere permessi e processo corretti.

---

Come un'app accede al vault
•  Il modello migliore su Azure è spesso la Managed Identity.
•  Così l'app non porta con sé credenziali da salvare altrove.
•  I permessi devono essere minimi e mirati all'oggetto richiesto.
•  L'accesso degli amministratori va separato da quello applicativo.
•  Un vault sicuro dipende tanto dal permesso quanto dal contenuto.

---

Rotazione e scadenza
•  Un segreto statico per anni è un debito, non una soluzione.
•  Rotazione e scadenza obbligano a rinnovare i valori sensibili.
•  L'app va progettata per leggere credenziali aggiornate.
•  Se la rotazione rompe il servizio, il problema è anche architetturale.
•  Qui si vede se la sicurezza è stata pensata davvero.

---

HSM e fiducia tra servizi
•  Non tutte le chiavi richiedono lo stesso livello di protezione.
•  Gli scenari più sensibili possono richiedere HSM dedicati o gestiti.
•  L'HSM aumenta garanzie e isolamento del materiale crittografico (compliance, rischio alto).
•  I certificati proteggono le connessioni e dichiarano identità: entrano in TLS e basi di mTLS.
•  Anche qui conta la gestione: rinnovo, scadenza, revoca. Domanda finale: chi si fida di chi, e con quale prova?

---

Da portare a casa
•  Defender for Cloud = vedere il rischio in modo continuo e per priorità.
•  Posture (come sei impostato) e workload protection (cosa accade) vanno letti insieme.
•  Key Vault = togliere segreti e chiavi dai punti sbagliati e governarne il ciclo di vita.
•  Managed Identity + permessi minimi = accesso applicativo senza credenziali sparse.
•  Filo unico: prima vedo dove sono esposto, poi proteggo ciò che è sensibile.


---

# 18) Microsoft Azure - Security, Reliability e Business Continuity - PT2 - Backup, Disaster Recovery

**File:** `18) Microsoft Azure - Security, Reliability e Business Continuity - PT2 - Backup, Disaster Recovery.pptx`
**Tipo:** `.pptx`
**Dimensione:** 79.9 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Security, Reliability e Business Continuity - PT2: Backup, Disaster Recovery e Compliance (4 ore)

---

Backup, Disaster Recovery e Compliance
Far sopravvivere dato e servizio a un guasto, e saperlo dimostrare

---

Argomenti (4 ore)
•  Il backup non è solo una copia: progettare il recupero
•  La logica 3-2-1 applicata al cloud
•  Retention operativa e storica
•  Recovery Services Vault e separazione dei vault
•  Restore test e runbook: protezione reale vs dichiarata
•  Alta disponibilità vs Disaster Recovery
•  Availability Set / Zone / Region, RPO/RTO (Recovery Point/Time Objective), Azure Site Recovery
•  Il failover come sequenza, non solo replica
•  Compliance e audit: dimostrare la conformità e poter fare il postmortem
•  Sicurezza applicativa (API Management) e Private Link

---

Il backup non è solo una copia
•  Fare backup non significa automaticamente poter ripartire bene.
•  Conta cosa proteggi, con quale frequenza e quanto velocemente recuperi.
•  Backup e continuità del servizio vanno letti insieme.
•  Se non sai cosa vuoi recuperare prima, la policy resta astratta.
•  Il punto è progettare il recupero, non solo salvare dati.

---

La logica 3-2-1 nel cloud
•  La regola 3-2-1: più copie, su supporti/livelli diversi, con una separazione reale.
•  Nel cloud la separazione non è solo fisica: può essere logica, operativa, di accesso.
•  Serve a ridurre il rischio di perdita unica o compromissione comune.
•  Va adattata al workload, non applicata come slogan.

---

Retention operativa e storica
Tipo
Scopo
Operativa
recupero veloce dopo errore o incidente comune
Storica
conservazione lunga per audit, analisi o obblighi
•  Le due retention non coincidono quasi mai.
•  Confonderle porta a costi inutili o recuperi insufficienti.

---

Recovery Services Vault e separazione
•  Il Recovery Services Vault è il contenitore Azure per backup e punti di ripristino.
•  Tiene insieme policy di backup, retention e gli elementi protetti.
•  Vault separation: non tutto deve stare nello stesso contenitore operativo.
•  Separare ambienti/workload riduce il blast radius di errori o compromissioni.
•  Anche i permessi diventano più leggibili e meno pericolosi.

---

Restore test e runbook
•  Un backup non testato è solo una promessa.
•  I restore test verificano tempi, dipendenze e integrità del recupero.
•  I runbook evitano di improvvisare durante un incidente.
•  Quando il ripristino coinvolge più servizi, la procedura conta quanto il dato.
•  Qui si vede la differenza tra protezione dichiarata e protezione reale.

---

Dal backup alla continuità: HA vs DR
•  Alta disponibilità (HA) e Disaster Recovery (DR) non sono la stessa cosa.
•  HA: riduce interruzioni locali o limitate (un nodo, un guasto circoscritto).
•  DR: prepara il servizio a eventi gravi e meno frequenti (perdita di una region).
•  Se i due piani si confondono, anche il design resta ambiguo.
•  Distinguere continuità locale da recupero su scala ampia.

---

Availability Set, Zone e Region
Livello
Idea chiave
Availability Set
separazione da fault e update domain (stesso datacenter)
Availability Zone
distribuzione su zone distinte nella stessa region
Region
separazione geografica per eventi più ampi
•  Ogni livello aumenta resilienza, ma anche costo e complessità.
•  La scelta dipende da rischio atteso e criticità del servizio.

---

RPO e RTO
•  RPO (Recovery Point Objective): quanta perdita di dati puoi tollerare.
•  RTO (Recovery Time Objective): in quanto tempo devi tornare operativo.
•  Sono i due numeri guida per decidere architettura e investimento.
•  Senza questi riferimenti, parlare di DR (Disaster Recovery) resta troppo vago.
•  Prima si definisce il requisito, poi si sceglie la tecnologia.

---

Azure Site Recovery
•  Azure Site Recovery (ASR) supporta replica e failover controllato.
•  Porta i workload verso un sito secondario o una region alternativa.
•  Non basta attivarlo: va allineato a dipendenze applicative e dati.
•  È uno strumento, non il piano completo.
•  Il valore emerge quando entra in una strategia coerente.

---

Il failover è una sequenza
•  Un failover serio non sposta solo macchine: muove un servizio intero.
•  Vanno considerati ordine di avvio, dipendenze, DNS, dati e verifiche finali.
•  Se manca una dipendenza critica, il sito secondario non serve davvero.
•  Per questo il piano va scritto, provato e aggiornato.
•  La resilienza dipende dalla sequenza, non solo dalla replica.

---

Scegliere il livello giusto
•  Non ogni servizio richiede architetture multi-region complesse.
•  Per alcuni workload basta alta disponibilità locale ben progettata.
•  Per altri servono replica geografica e piani di ripartenza dettagliati.
•  Il design corretto nasce dall'impatto del fermo sul business.
•  Affidabilità e costo vanno bilanciati con lucidità.

---

Compliance: non basta la checklist
•  La compliance non è spuntare un elenco di controlli: è dimostrare che l'ambiente segue regole e vincoli.
•  In cloud conta la raccolta continua delle evidenze: se la prova manca, anche un buon controllo è difficile da sostenere.
•  È il punto dove governance e operatività si incontrano.

---

Regulatory Compliance in Azure
•  Regulatory Compliance (in Defender for Cloud / Azure Policy) legge requisiti e stato dei controlli.
•  Mostra dove sono i gap e quali evidenze sono disponibili, raggruppati per area (rete, identity, dati…).
•  Non sostituisce il lavoro del team: rende visibile il quadro.
•  Uno standard senza lettura operativa resta teorico.

---

Audit e tracciabilità
•  Audit = ricostruire chi ha fatto cosa e quando.
•  Activity Log e log diagnostici, raccolti in un workspace e interrogabili via Application Insights.
•  Servono quando qualcosa sfugge a design e postura: sono la base del postmortem.
•  Le evidenze vanno conservate in modo coerente e consultabile nel tempo.

---

Sicurezza applicativa: il punto centralizzato
•  La sicurezza è anche come pubblichi l'applicazione, non solo la piattaforma.
•  Un gateway centralizzato come API Management concentra più controlli:
      ○  autenticazione/autorizzazione di chi chiama (subscription key, token/JWT)
      ○  protezione dagli attacchi e rate limiting
      ○  TLS, cifratura e certificati gestiti sul gateway
•  WAF ed endpoint gestiti completano il perimetro: sicuro dentro ma esposto male fuori = fragile.

---

Private Link e pubblicazione controllata
•  Private Link riduce l'esposizione pubblica dei servizi critici (già visto nella lezione di rete).
•  Raggiungi alcune risorse via percorsi privati, senza passare da Internet.
•  Ha molto senso per dati e backend sensibili.
•  Principio: pubblicare meno, controllare meglio.

---

Da portare a casa
•  Il backup serve a ripartire: 3-2-1, retention operativa/storica, vault separation, restore test.
•  HA (alta disponibilità) ≠ DR (Disaster Recovery); RPO/RTO guidano architettura e spesa.
•  Il failover è una sequenza, abilitata da strumenti come ASR (Azure Site Recovery).
•  Compliance = dimostrare la conformità; audit/log = poter fare il postmortem.
•  Sicurezza applicativa con APIM e Private Link: pubblicare meno, controllare meglio.


---

# 2) Microsoft Azure - Architettura e Strumenti di Accesso (Parte 1)

**File:** `2) Microsoft Azure - Architettura e Strumenti di Accesso (Parte 1).pptx`
**Tipo:** `.pptx`
**Dimensione:** 77.6 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Architettura e strumenti di accesso - Parte 1 (4 ore)

---

Architettura e strumenti di accesso
Corso Cloud Specialist - ITS ICT
Agenda (4 ore)
•  Tenant, subscription e piano gratuito
•  Risorse, wizard di creazione, resource group
•  Regioni e zone di disponibilità
•  Azure Resource Manager (ARM)
•  Portale e Azure CLI
•  Marketplace, tipi di risorse, IaaS/PaaS/SaaS

---

Tenant, Subscription e piano gratuito
Livello
Cos'è
Nel nostro caso
Tenant
L'organizzazione su Azure
ITS ICT Piemonte
Subscription
Fatturazione e limiti
Azure for Students
Resource Group
Contenitore logico
Lo creiamo noi
Risorsa
Il servizio (VM, DB...)
Lo creiamo noi
Azure for Students
•  100 $ di credito e accesso a servizi gratuiti
•  Alcuni gratuiti per 12 mesi (VM, storage, database)
•  Altri always free con rinnovo mensile (App Service, Functions)
•  Controllate i costi nella sezione "Cost Management"

---

Come trovare tenant e subscription
•  Apriamo portal.azure.com
•  In alto a destra, icona utente → "Switch directory": ecco il nostro tenant (ITS ICT Piemonte)
•  Nella barra di ricerca cerchiamo "Subscriptions"
•  Troviamo Azure for Students: notiamo nome, ID, stato
•  Clicchiamo sulla subscription per vedere credito residuo e limiti
•  Cerchiamo "Free services" per vedere la lista dei servizi gratuiti inclusi

---

Risorse e UI uniforme
In Azure tutto è una risorsa: VM, database, storage, rete, resource group.
La UI del portale è sempre la stessa per ogni tipo di risorsa:
Azione
Come
Creare
Basics (nome, regione, RG) → Tab (default OK) → Review + Create
Elencare
Sezione dedicata o "All resources"
Dettaglio
Click sulla risorsa → Overview, Settings, ...
Cancellare
Pulsante Delete nella barra superiore

---

Resource Group
Il resource group è la risorsa più semplice ma anche la più fondamentale.
•  Contenitore logico che raggruppa risorse correlate
•  Ogni risorsa deve stare in esattamente un resource group
•  Ha un nome e una regione (dove Azure salva i metadati)
•  Le risorse al suo interno possono stare in regioni diverse
Convenzione di nome
Esempio
rg-progetto-ambiente
rg-webapp-prod
rg-progetto-dev
rg-webapp-dev
Cancellare un resource group = cancellare tutto ciò che contiene.

---

Come creare un Resource Group
•  Cerchiamo "Resource groups" nella barra di ricerca del portale
•  Clicchiamo "+ Create"
•  Basics: subscription, nome rg-demo, regione Italy North
•  Notiamo i tab del wizard: Tags, poi Review + create - lo stesso pattern di sempre
•  Clicchiamo "Review + create" → controlliamo il riepilogo → "Create"
•  Apriamo il resource group: Overview (vuoto), Activity Log, Tags
•  Notiamo come la UI è identica a quella di qualsiasi altra risorsa

---

Regioni Azure
Una regione è un'area geografica con uno o più data center.
Caratteristica
Dettaglio
Quante
Oltre 60 nel mondo
In Italia
Italy North (Milano)
Scelta
Vicinanza, conformità, costi
•  Recommended: la maggior parte dei servizi, zone di disponibilità (es. Italy North)
•  Alternate: gamma più limitata, per esigenze specifiche

---

Zone di disponibilità (Availability Zones)
Data center fisicamente separati dentro una stessa regione.
Regione
Zone disponibili
Con AZ (es. Italy North)
Zone 1, 2, 3
Senza AZ
Nessuna zona
•  Creando 3 VM in zone diverse si ottiene ridondanza
•  Nel wizard VM: "Availability options" per scegliere la zona

---

Come esplorare regioni e zone nel wizard
•  Iniziamo a creare una Virtual Machine (non la completiamo)
•  Nella sezione "Region", apriamo il menu a tendina: scorriamo per vedere quante regioni esistono
•  Scegliamo Italy North
•  In "Availability options" selezioniamo "Availability zone": compaiono le 3 zone
•  Proviamo a cambiare regione e notiamo come alcune non offrono zone di disponibilità
•  Guardiamo i tab del wizard: Disks, Networking, Management... tutti con default
•  Arriviamo a "Review + create": vediamo il riepilogo, poi annulliamo

---

Azure Resource Manager (ARM)
ARM è il livello di gestione centrale: ogni operazione passa da qui.
Strumento
Passa da ARM?
Portale Azure
Si
Azure CLI / PowerShell
Si
SDK / API REST
Si
In "Review + create" c'è "Download a template for automation": file JSON con tutti i parametri della risorsa, per ricrearla in modo programmatico.

---

Strumenti di accesso: portale e CLI
Portale Azure
•  Interfaccia web: portal.azure.com
•  Ideale per esplorare, imparare, operazioni manuali
•  Tutto si fa con click, no codice
Azure CLI (az)
•  Strumento a riga di comando, si usa in PowerShell o nel terminale
•  Comandi strutturati in modo gerarchico, si esplorano con --help:
Comando
Cosa mostra
az --help
Lista dei gruppi di comandi
az vm --help
Comandi per le VM
az vm create --help
Parametri per creare una VM

---

Come usare la CLI di Azure
•  Apriamo Cloud Shell nel portale (icona >_ in alto)
•  Scegliamo Bash
•  Proviamo i comandi di help:
az --help
az group --help
•  Creiamo un resource group da CLI:
az group create --name rg-demo-cli --location italynorth
•  Elenchiamo i resource group:
az group list --output table
•  Lo vediamo anche nel portale: stessa risorsa, creata da CLI anziché dalla UI

---

Marketplace e tipi di risorse
Marketplace
•  Catalogo di risorse e soluzioni: Microsoft e terze parti
•  "Create a resource" apre il Marketplace
Le tre macro-categorie
Categoria
Cosa fa
Esempi
Compute
Esegue codice
VM, App Service, Functions
Network
Connette risorse
Virtual Network, Load Balancer
Storage
Conserva dati
Blob Storage, File Share, Disk
Ogni soluzione cloud combina compute, network e storage.

---

IaaS, PaaS, SaaS
Tre modelli, diversi per livello di gestione:
Modello
Cosa gestisci tu
Esempio Azure
IaaS
OS, runtime, app, dati
Virtual Machine
PaaS
Solo app e dati
App Service, SQL Database
SaaS
Solo i dati
Microsoft 365, Outlook
•  PaaS è il modello più importante: non gestisci server, OS o aggiornamenti
•  Ti concentri su codice e dati: scaling, patching e HA sono automatici
•  Esempio: carichi il codice su App Service e il sito è online

---

Riepilogo
Concetto
Cosa ricordare
Tenant / Subscription
Organizzazione + fatturazione (100 $)
Risorse
Tutto è una risorsa, UI e wizard uniformi
Resource Group
Contenitore logico, cancellarlo cancella tutto
Regioni
60+, Italy North a Milano
Availability Zones
Fino a 3 zone per ridondanza fisica
ARM
Ogni operazione passa da qui, template JSON
Portale / CLI
Due modi, stesso risultato
Marketplace
Catalogo risorse Microsoft e terze parti
IaaS / PaaS / SaaS
PaaS = focus su codice e dati


---

# 3) Microsoft Azure - Architettura e Strumenti di Accesso (Parte 2)

**File:** `3) Microsoft Azure - Architettura e Strumenti di Accesso (Parte 2).pptx`
**Tipo:** `.pptx`
**Dimensione:** 78.9 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Architettura e strumenti di accesso - Parte 2 (4 ore)

---

Architettura e strumenti di accesso - Parte 2
Corso Cloud Specialist - ITS ICT
Agenda (4 ore)
•  Paired regions e edge locations
•  Modello di responsabilità condivisa e SLA
•  Best practice di separazione (resource group)
•  ARM: scope e idempotenza
•  Cloud Shell e Azure PowerShell
•  Blueprint vs template
•  Panoramica servizi core e PaaS

---

Paired Regions
Ogni regione Azure ha una regione associata (paired) nello stesso continente.
Regione
Paired Region
West Europe (Paesi Bassi)
North Europe (Irlanda)
France Central (Parigi)
France South (Marsiglia)
East US
West US
•  Italy North (Milano) non ha una paired region locale
•  Disaster recovery: se una regione cade, la paired prende il carico
•  Aggiornamenti sequenziali: Azure aggiorna una regione alla volta

---

Edge Locations
Punti di presenza vicini agli utenti finali, fuori dai data center principali.
Concetto
Cosa fa
Azure CDN
Cache di contenuti statici vicino all'utente
Azure Front Door
Routing globale, accelerazione, WAF
Azure Edge Zones
Compute a bassa latenza in prossimità
•  Bassa latenza: gaming, streaming, IoT
•  Distribuzione globale: immagini, video, file statici

---

Modello di responsabilità condivisa
Chi gestisce cosa dipende dal modello di servizio scelto.
Livello
IaaS
PaaS
SaaS
Dati e accessi
Tu
Tu
Tu
Applicazione
Tu
Tu
Provider
Runtime / OS
Tu
Provider
Provider
Infrastruttura fisica
Provider
Provider
Provider
•  Da IaaS a SaaS: la responsabilità si sposta verso il provider
•  Sempre tua: dati, account, identità, dispositivi

---

SLA e disponibilità
Lo SLA (Service Level Agreement) è la garanzia di uptime di un servizio.
SLA
Downtime annuo
Esempio servizio
99.9%
~8.7 ore
App Service, SQL Database
99.95%
~4.4 ore
VM singola (Premium SSD)
99.99%
~52 minuti
VM in Availability Zones
Come si calcola lo SLA composto?
•  Due servizi in sequenza: SLA1 x SLA2 (es. 99.9% x 99.9% = 99.8%)
•  Per aumentare lo SLA: ridondanza, zone, paired regions
•  Nessun SLA per i servizi del tier gratuito

---

Best practice: separazione dei Resource Group
Non mettere tutto in un unico RG. Separare per scopo e ciclo di vita.
Criterio
Esempio
Per ambiente
rg-app-dev, rg-app-prod
Per applicazione
rg-webapp, rg-api, rg-database
Per ciclo di vita
Risorse temporanee in un RG a parte
•  Risorse che si creano e cancellano insieme nello stesso RG
•  Ambienti diversi in RG diversi (mai dev e prod insieme)
•  I permessi (RBAC) si assegnano a livello di RG

---

ARM: scope e idempotenza
Ogni operazione ARM avviene a un livello (scope) preciso:
Scope
Cosa contiene
Management Group
Raggruppa subscription
Subscription
Fatturazione e limiti
Resource Group
Contenitore logico di risorse
Risorsa
Il singolo servizio (VM, DB, ...)
Idempotenza: stesso template eseguito 2 volte = stesso risultato. Se la risorsa esiste, ARM la aggiorna (non la duplica). Template come fonte di verità (IaC).

---

Cloud Shell
Terminale nel browser, integrato nel portale Azure (icona >_).
Caratteristica
Dettaglio
Accesso
Dal portale, zero installazione
Linguaggi
Bash o PowerShell
Preinstallato
Azure CLI, PowerShell, Git, Terraform
Storage
File persistenti su File Share (5 GB)
•  Non vuoi installare nulla sul tuo PC
•  Sei su un PC non tuo (laboratorio, aula)

---

Azure PowerShell
Modulo Az per PowerShell: stesse operazioni della CLI, sintassi PowerShell.
Azure CLI
Azure PowerShell
az group create --name rg
New-AzResourceGroup -Name rg
az vm list --output table
Get-AzVM
az group delete --name rg
Remove-AzResourceGroup -Name rg
•  CLI (az): sintassi breve, cross-platform, popolare tra dev
•  PowerShell (Az): pipeline e oggetti, familiare a sysadmin
•  Entrambi passano da ARM: stesso risultato

---

Blueprint vs Template ARM
Template ARM
Azure Blueprint
Cos'è
File JSON per creare risorse
Pacchetto di governance completo
Contiene
Risorse e parametri
Template + policy + RBAC + RG
Scope
Resource group o subscription
Subscription
Scopo
Deploy ripetibile
Ambiente compliant "chiavi in mano"
•  Template: "crea queste risorse con questi parametri"
•  Blueprint: "prepara un ambiente con risorse, regole e permessi"

---

Servizi core: Compute
Risorse che eseguono codice.
Servizio
Tipo
Quando usarlo
Virtual Machine
IaaS
Controllo totale su OS e software
App Service
PaaS
Web app senza gestire server
Functions
PaaS serverless
Codice a evento, pay-per-execution
Container Instances
PaaS
Container singoli, avvio rapido
AKS
PaaS
Orchestrazione Kubernetes
Da VM a Functions: meno controllo, meno gestione, più automazione.

---

Servizi core: Storage
Risorse che conservano dati.
Servizio
Cosa memorizza
Esempio d'uso
Blob Storage
File non strutturati
Immagini, video, backup
File Share
File condivisi (SMB/NFS)
Cartelle di rete in cloud
Queue Storage
Messaggi in coda
Comunicazione tra servizi
Table Storage
Dati NoSQL chiave-valore
Log, dati semplici
Disk
Dischi per VM
OS disk, data disk
•  Tutto dentro uno Storage Account (nome unico globale)
•  Livelli di accesso: Hot, Cool, Archive (costo vs velocità)

---

Servizi core: Network
Risorse che connettono e proteggono.
Servizio
Cosa fa
Virtual Network (VNet)
Rete privata in cloud
Subnet
Segmento dentro una VNet
NSG
Firewall a livello di subnet/NIC
Load Balancer
Distribuisce traffico tra VM
VPN Gateway
Connette rete on-premise ad Azure
Application Gateway
Load balancer HTTP con WAF
•  Ogni VM si collega a una VNet tramite una NIC
•  Le NSG filtrano il traffico con regole allow/deny

---

Servizi PaaS in dettaglio
PaaS: tu scrivi il codice, Azure gestisce tutto il resto.
Servizio PaaS
Cosa risolve
App Service
Hosting web/API (deploy da Git o ZIP)
Azure SQL Database
DB relazionale gestito
Cosmos DB
DB NoSQL distribuito globalmente
Functions
Codice a evento (serverless)
Cache for Redis
Cache in memoria per performance
•  Zero patching OS, scaling automatico
•  Deploy più veloce, focus su business logic

---

Riepilogo Parte 2
Concetto
Cosa ricordare
Paired Regions
Disaster recovery, aggiornamenti sequenziali
Edge
CDN e Front Door per bassa latenza
Responsabilità condivisa
IaaS: gestisci di più, SaaS: gestisci meno
SLA
% uptime garantita, composto = prodotto
Separazione RG
Per ambiente, app o ciclo di vita
ARM Scope
Management Group > Sub > RG > Risorsa
Idempotenza
Stesso template, stesso risultato
Cloud Shell / PowerShell
Strumenti alternativi alla CLI
Blueprint
Ambiente compliant chiavi in mano
Compute / Storage / Network
I tre pilastri di ogni soluzione cloud


---

# 4) Microsoft Azure - Identity e Governance (Parte 1)

**File:** `4) Microsoft Azure - Identity e Governance (Parte 1).pptx`
**Tipo:** `.pptx`
**Dimensione:** 75.7 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Identity e Governance - Parte 1 (2 ore)

---

Identity e Governance
Come Azure gestisce chi sei, cosa puoi fare e quali regole valgono

---

Argomenti di oggi
•  Microsoft Entra ID: cos'è, il tenant, il dominio .onmicrosoft.com
•  Utenti e gruppi: interni vs esterni, creazione, associazione
•  App Registration: identità per le applicazioni
•  Azure Policy: assegnazioni e restrizioni (es. region consentite)
•  RBAC: cos'è, ruoli, scope, assegnazioni
•  IAM nel portale: Check Access, Add Role Assignment
•  MFA: perché è obbligatorio
Nelle prossime lezioni approfondiremo ogni tema e ne aggiungeremo altri.

---

Microsoft Entra ID (ex Azure AD)
Microsoft Entra ID è il servizio di identità e accesso di Azure. Gestisce:
•  Chi sei: utenti, gruppi, applicazioni
•  Come ti autentichi: password, MFA, Authenticator
•  Cosa puoi fare: ruoli, permessi, policy
Ogni organizzazione Azure ha almeno un tenant Entra ID: è il "contenitore" di tutte le identità.
“Pensatelo come l'elenco telefonico dell'organizzazione: contiene tutti gli utenti, i gruppi e le app registrate.”

---

Il tenant e il dominio .onmicrosoft.com
Quando un'organizzazione crea un tenant Entra ID, riceve un dominio di default:
nomeorganizzazione.onmicrosoft.com
•  È l'indirizzo univoco del tenant su Azure
•  Nel vostro caso: itsictpiemonte.onmicrosoft.com
•  Il vostro account istituzionale è collegato a quel tenant
Con la sottoscrizione per studenti, l'accesso a Entra ID è bloccato, ma il tenant esiste. La sottoscrizione normale permette di gestire utenti, gruppi e app.

---

Utenti: interni ed esterni
In Entra ID ci sono due tipi di utenti:
Member (interno)
Guest (esterno)
Chi è
Appartiene all'organizzazione
Invitato da fuori
Account
Nel tenant (es. mario.rossi@...onmicrosoft.com)
Il suo esistente (Gmail, altro tenant)
Accesso
Completo (in base ai permessi)
Limitato a ciò che gli è condiviso
Quando crei un utente, puoi assegnargli subito uno o più gruppi esistenti.

---

Gruppi
I gruppi servono a organizzare gli utenti e semplificare la gestione dei permessi.
•  Crei un gruppo (es. "Team Sviluppo", "Docenti", "Studenti Anno 1")
•  Associ uno o più utenti al gruppo
•  Assegni i permessi al gruppo invece che ai singoli utenti
Vantaggio: se entra un nuovo membro nel team, lo aggiungi al gruppo e ha subito tutti i permessi necessari. Non devi configurare nulla risorsa per risorsa.
“È lo stesso principio dei gruppi di Active Directory in azienda, ma su cloud.”

---

App Registration: identità per le applicazioni
Anche le applicazioni hanno bisogno di un'identità per interagire con Azure.
App Registration crea un'identità nel tenant Entra ID. Esempio: Terraform.
•  Si registra come app nel tenant
•  Riceve credenziali (client ID + secret) per autenticarsi
•  Gli si assegnano i permessi necessari (es. creare VM, gestire rete)
Stessa cosa per: pipeline CI/CD, script di automazione, applicazioni web.
“In Enterprise Applications trovi le app già registrate e i relativi permessi.”

---

Azure Policy
Azure Policy impone regole sull'intera sottoscrizione (o su un ambito più ristretto).
Quello che abbiamo visto: Authoring > Assignments > Allowed resource deployment regions - solo 5 region consentite. Se crei una VM in una region non in lista, Azure la blocca.
Le policy servono a:
•  Impedire errori: nessuno crea risorse dove non dovrebbe
•  Garantire conformità: regole aziendali applicate automaticamente
•  Controllare i costi: es. limitare i tipi di VM consentiti
“La policy non è un permesso: è una regola imposta dall'alto che vale per tutti, indipendentemente dal ruolo.”

---

RBAC: Role-Based Access Control
RBAC è il modello con cui Azure gestisce i permessi. Tre domande:
•  Chi? - un utente, un gruppo, un'app (il principal)
•  Cosa può fare? - un insieme di azioni (il ruolo)
•  Dove? - a quale livello si applica (lo scope)
Esempio: "Mario (chi) ha il ruolo Contributor (cosa) sul Resource Group Lab-01 (dove)."
Lo scope è gerarchico (i permessi si ereditano dall'alto verso il basso):
Management Group > Subscription > Resource Group > Resource
Reader sulla Subscription = Reader su tutti i Resource Group e risorse al suo interno.

---

Ruoli principali di Azure
Alcuni ruoli predefiniti (built-in) che incontrate spesso:
Ruolo
Cosa può fare
Owner
Tutto, compreso assegnare ruoli ad altri
Contributor
Tutto tranne assegnare ruoli
Reader
Solo leggere, non può modificare nulla
User Access Administrator
Gestisce solo chi ha accesso a cosa
Esistono anche ruoli specifici per servizio (es. "Virtual Machine Contributor", "Storage Blob Data Reader").
“Un permesso (role assignment) può avere una data di scadenza: dopo quella data, l'accesso viene rimosso automaticamente.”

---

IAM nel portale: Check Access e Add Role Assignment
Su qualsiasi risorsa o Resource Group, c'è il pannello Access control (IAM).
Check Access: cerchi una persona e vedi che ruolo ha (anche permessi ereditati).
Add role assignment richiede 3 cose:
•  Role: Owner, Contributor, Reader, ecc.
•  Members: User/group/service principal oppure Managed identity
•  Confermi e il permesso è attivo
“Cliccando su un utente o gruppo nel pannello IAM, puoi vederne info e metadati.”

---

Service Principal vs Managed Identity
Nell'Add Role Assignment avete visto due tipi di identità non-umane:
Service Principal
Managed Identity
Chi la crea
Tu (App Registration)
Azure
Credenziali
Tu le gestisci (secret)
Azure le gestisce
Uso tipico
Servizi esterni (Terraform, GitHub)
Servizi Azure (VM, App)
Rischio
Secret può essere esposto
Nessun secret da esporre
In breve: se il servizio gira dentro Azure, usa Managed Identity. Se è esterno, serve un Service Principal.

---

MFA: Multi-Factor Authentication
MFA aggiunge un secondo fattore di verifica oltre alla password.
•  Qualcosa che sai: la password
•  Qualcosa che hai: il telefono con Microsoft Authenticator
Microsoft lo richiede su tutti i tenant (potete posticipare X volte, poi è obbligatorio). Nel vostro caso: login > notifica su Authenticator > approvate.
“Una password rubata non basta più per entrare. L'MFA è il singolo intervento più efficace contro accessi non autorizzati.”

---

Riepilogo: i pezzi del puzzle
Livello
Servizio
Domanda
Identità
Entra ID: utenti, gruppi, app, MFA
Chi sei?
Permessi
RBAC: ruolo + scope = accesso
Cosa puoi fare?
Regole
Azure Policy: vincoli dall'alto
Cosa è consentito fare?
•  Entra ID gestisce le identità
•  RBAC assegna i permessi
•  Policy impone le regole

---

Prossime lezioni
Quello che abbiamo visto oggi è una panoramica. Nelle prossime 8 ore approfondiremo:
•  Conditional Access: regole che decidono quando e come puoi accedere
•  Identity Protection: rilevamento automatico di accessi sospetti
•  PIM: attivare ruoli privilegiati solo quando servono
•  Management Groups: organizzare più sottoscrizioni
•  Policy e iniziative: creare e gestire set di regole
•  Tagging, naming convention, locks: governance pratica delle risorse
•  B2B e B2C: gestire identità esterne in scenari reali


---

# 5) Identity e Governance - Parte 2

**File:** `5) Identity e Governance - Parte 2.pptx`
**Tipo:** `.pptx`
**Dimensione:** 71.7 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Identity e Governance - Parte 2 (4 ore)

---

Identity e Governance - Parte 2
Conditional Access, Identity Protection, PIM e governance pratica

---

Argomenti di oggi
•  Conditional Access: regole di accesso basate su utente, rischio e dispositivo
•  Identity Protection: segnali di rischio e protezione degli account
•  PIM: ruoli privilegiati attivi solo quando servono
•  Management Groups: organizzare più subscription in modo coerente
•  Azure Policy e iniziative: applicare regole di conformità in modo centralizzato
•  Naming, tagging e locks: governance pratica delle risorse
•  B2B ed External ID: identità esterne per partner e applicazioni

---

Conditional Access
Conditional Access è il motore Zero Trust di Microsoft Entra. Funziona con regole if-then:
“Se un utente vuole accedere a una risorsa, allora deve soddisfare una condizione.”
Esempio: "Se un utente accede da fuori rete aziendale, allora deve fare MFA."
Le policy si creano in Entra ID > Conditional Access > Policies e si applicano dopo l'autenticazione iniziale (primo fattore).
Richiedono licenza Entra ID P1 (inclusa in Microsoft 365 Business Premium).

---

Conditional Access: segnali e decisioni
Segnali (input della policy):
•  Utente o gruppo: a chi si applica la policy
•  Indirizzo IP: posizione geografica, rete aziendale o meno
•  Dispositivo: conforme, ibrido, piattaforma (Windows, iOS...)
•  Applicazione: a quale app si sta accedendo
•  Livello di rischio: segnale da Identity Protection
Decisioni (output della policy):
•  Blocca accesso
•  Consenti con condizioni: richiedi MFA, dispositivo conforme, cambio password

---

Identity Protection
Identity Protection rileva automaticamente comportamenti sospetti sugli accessi:
•  Login da IP anonimi (es. VPN/Tor)
•  Password spray: tentativi di indovinare password su molti account
•  Credenziali compromesse: trovate in database di leak
•  Viaggio impossibile: login da Roma e da Tokyo a 5 minuti di distanza
Genera tre report: risky users, risky sign-ins, risk detections.
Può integrarsi con Conditional Access: se il rischio è alto, blocca l'accesso o forza il cambio password. Richiede licenza Entra ID P2.

---

PIM: Privileged Identity Management
PIM elimina i permessi privilegiati permanenti. Principio: nessuno dovrebbe essere Owner o Global Admin 24/7.
Come funziona:
•  L'admin assegna un ruolo come eligible (idoneo), non active
•  Quando serve, l'utente attiva il ruolo dal portale PIM
•  L'attivazione richiede: MFA, una giustificazione, eventuale approvazione
•  Il ruolo resta attivo per un tempo limitato (es. 8 ore), poi scade
“È il principio del just-in-time access: i permessi esistono solo quando servono.”
Richiede licenza Entra ID P2 o Entra ID Governance.

---

Management Groups
I Management Groups sono il livello sopra le subscription:
Management Group > Subscription > Resource Group > Resource
Servono per applicare in modo coerente policy e RBAC a più sottoscrizioni insieme.
•  Ogni directory ha un Root Management Group
•  Le assegnazioni fatte a un MG si ereditano verso il basso
•  Sono utili per separare ambienti, business unit o aree geografiche
“Esempio: il MG "Europa" può imporre policy comuni a tutte le subscription europee.”

---

Azure Policy e iniziative
Azure Policy controlla se le risorse rispettano regole organizzative.
•  Esempi: consentire solo regioni approvate, imporre tag obbligatori, vietare SKU non autorizzate
•  Effetti tipici: audit, deny, append, deployIfNotExists
•  Si assegna a Management Group, subscription o Resource Group
Iniziativa = raccolta di più policy gestite come un unico set.
•  Utile per standard di sicurezza, compliance o cost management
•  Rende più semplice applicare e tracciare regole comuni
“I Management Groups danno la gerarchia, Azure Policy applica le regole.”

---

Governance pratica: naming, tagging e locks
Strumento
A cosa serve
Naming convention
Dare nomi coerenti e leggibili alle risorse
Tag
Aggiungere metadati come Environment, Owner, CostCenter
Lock
Proteggere da modifiche o cancellazioni accidentali
•  I tag aiutano costi e filtri, ma non si ereditano automaticamente
•  I lock nel portale sono Delete e Read-only; in CLI/API sono CanNotDelete e ReadOnly

---

B2B ed External ID
B2B collaboration: collaborazione con partner esterni nel tenant workforce.
•  Inviti un utente esterno come Guest nello stesso tenant dei dipendenti
•  Usa spesso le sue credenziali originali
•  Accede solo a ciò che gli condividi
External ID in external tenant: CIAM per clienti o business customer.
•  Tenant separato in configurazione external
•  Registrazione self-service e login anche con provider esterni
•  Scenario tipico: portali clienti, app SaaS o aree riservate per utenti esterni

---

Riepilogo
•  Accesso: Conditional Access e Identity Protection
•  Privilegi: PIM per ridurre i permessi permanenti
•  Governance: Management Groups, Policy, tag e locks
•  Identità esterne: B2B per partner, External ID per utenti finali
Questi strumenti si combinano per decidere chi entra, con quali permessi e su quali risorse.

---

Dove lo vedi: Entra admin center
Se sei in Portal settings > Directories + subscriptions, non e' questa la schermata giusta.
Nel menu sinistro torna su Entra ID e usa anche Search menu se una voce non e' visibile.
•  Vai in Entra ID > Conditional Access, poi apri Policies
•  Apri Identity Protection e usa i report Risky users, Risky sign-ins, Risk detections
•  Apri Privileged Identity Management per ruoli eligible e attivazioni
•  Vai in Entra ID > Users > New user > Invite external user
•  Vai in Entra ID > External Identities > Cross-tenant access settings

---

Dove lo vedi: Azure portal
Apri portal.azure.com e poi:
•  Cerca Management Groups per vedere la gerarchia sopra le subscription
•  Cerca Policy per Definitions, Assignments, Compliance
•  Apri una subscription, Resource Group o risorsa e vai in Tags
•  Per i lock: sulla subscription la voce e' Resource locks; su Resource Group o risorsa la voce e' Locks
La naming convention non ha una schermata dedicata: si definisce come standard e spesso si fa rispettare con Azure Policy.


---

# 6) Reti su Azure - Parte 1

**File:** `6) Reti su Azure - Parte 1.pptx`
**Tipo:** `.pptx`
**Dimensione:** 67.5 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Reti su Azure - Parte 1 (2 ore)

---

Reti su Azure - Parte 1
VNet, subnet, NSG e accesso RDP come caso guida

---

Argomenti
•  Perche' la rete conta in Azure
•  VNet e Subnet: i blocchi base
•  NSG: regole allow/deny sul traffico
•  RDP su una VM Windows: cosa deve esserci per collegarsi
•  Caso guida: relazione tra regola TCP 3389 e accesso alla VM
•  Segmentazione, troubleshooting e casi piu' realistici

---

Dove siamo nel percorso
•  Dopo identita', permessi e governance, passiamo al livello rete
•  La rete decide chi raggiunge cosa e su quale porta
•  Qui iniziamo dalla parte piu' concreta: una VM gia' esistente e il suo NSG
•  Una VM gia' esistente con il suo NSG e' un buon caso iniziale per leggere l'effetto delle regole

---

I pezzi minimi della rete in Azure
Oggetto
A cosa serve
VNet
La rete privata nel cloud
Subnet
Una porzione della VNet
NIC
La scheda di rete della VM
Public IP
L'indirizzo pubblico per accesso da Internet
NSG
Le regole che permettono o bloccano traffico
•  Per il caso RDP bastano soprattutto VM + Public IP + NSG

---

VNet e Subnet
•  Una VNet e' la tua rete privata in Azure
•  Una Subnet divide la rete in zone piu' piccole
•  Le subnet servono per separare carichi di lavoro e applicare regole diverse
•  Piu' avanti useremo questa logica per distinguere frontend, backend e management

---

NSG: concetti chiave
•  Un Network Security Group contiene regole Allow o Deny
•  Le regole valgono su traffico inbound o outbound
•  Un NSG si puo' associare a una subnet o a una NIC
•  Le regole hanno una priority: numero piu' basso = precedenza piu' alta
•  Le regole di default esistono gia', ma le regole custom possono prevalere

---

RDP: condizioni minime di accesso
•  Una VM Windows accesa
•  Un Public IP sulla VM, se il collegamento e' diretto da Internet
•  Una regola inbound TCP 3389 che consenta il traffico verso la VM
•  Credenziali valide della macchina virtuale
“Se la porta 3389 non e' consentita, la connessione RDP non parte.”

---

Dove lo vedi nel portale
•  Apri la Virtual machine
•  Nel menu vai su Networking > Network settings
•  Controlla se c'e' una regola che consente TCP 3389
•  Apri il Network security group associato
•  In Inbound security rules leggi, modifichi o elimini la regola

---

Caso guida: RDP e regola 3389
•  Se esiste una regola inbound TCP 3389 che consente il traffico, la VM puo' accettare nuove connessioni RDP
•  Se la regola manca oppure viene negata, la connessione RDP fallisce
•  L'esito dipende anche da priority, source, protocol e scope
•  Il punto non e' memorizzare clic, ma leggere il legame tra regola di rete e accessibilita' della VM
La rete non e' sfondo: decide concretamente se un accesso e' possibile oppure no.

---

Attenzione: cosa osservare davvero
•  Gli NSG sono stateful: una sessione gia' aperta puo' restare attiva
•  Se togli la regola, di solito falliscono le nuove connessioni RDP
•  La stessa porta puo' avere esiti diversi in base a priority, source e scope
•  Una regola con source My IP e' piu' sicura di una con source Any

---

Sviluppi del tema
•  Subnet e segmentazione della rete
•  Differenza tra NSG su subnet e su NIC
•  Effective security rules e verifica del risultato finale
•  Altri casi: HTTP, HTTPS, regole troppo larghe, regole troppo strette
Il punto chiave e' che una regola di rete cambia davvero il comportamento della VM.


---

# 7) Microsoft Azure - Reti su Azure - Parte 2

**File:** `7) Microsoft Azure - Reti su Azure - Parte 2.pptx`
**Tipo:** `.pptx`
**Dimensione:** 72.5 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Reti su Azure - Parte 2 (3 ore)

---

Reti su Azure - Parte 2
NSG su subnet e NIC, effective rules, HTTP/HTTPS e troubleshooting

---

Argomenti
•  Ripresa dei concetti chiave della Parte 1
•  Differenza tra NSG su subnet e NSG su NIC
•  Effective security rules: dove leggere il risultato finale
•  Casi tipici: HTTP e HTTPS su una VM
•  Metodo di troubleshooting quando un accesso non funziona
•  Verifica dal portale e da Cloud Shell

---

Ripartenza dalla Parte 1
•  Nella prima parte abbiamo visto VNet, subnet, NSG e caso RDP 3389
•  Il punto chiave era semplice: una regola di rete cambia davvero il comportamento della VM
•  Ora facciamo un passo in piu': capire dove applicare la regola e come leggere l'effetto complessivo
•  Non basta vedere un NSG nel portale: bisogna capire se e' quello che decide davvero il traffico

---

Subnet e NIC: due livelli diversi
Livello
Cosa protegge
Quando e' utile
Subnet
Un insieme di risorse nella stessa porzione di rete
Per regole comuni a piu' VM
NIC
Una singola interfaccia di rete
Per eccezioni o casi specifici
•  Azure permette di usare NSG su entrambi i livelli
•  Il punto non e' aggiungere regole ovunque, ma capire quale livello ha senso usare

---

Quando ha senso lavorare sulla subnet
•  Quando piu' VM dello stesso livello applicativo devono seguire le stesse regole
•  Quando vuoi separare bene frontend, backend e zone amministrative
•  Quando vuoi una vista piu' ordinata della segmentazione
•  Quando la regola descrive il comportamento atteso di tutta una porzione di rete
La subnet e' il posto naturale per la policy comune.

---

Quando ha senso lavorare sulla NIC
•  Quando una singola VM ha bisogno di un'eccezione temporanea o mirata
•  Quando vuoi differenziare una macchina senza cambiare tutta la subnet
•  Quando stai facendo verifica o isolamento di un nodo specifico
•  Se usi troppe eccezioni a livello NIC, pero', la lettura della rete diventa meno chiara
Una regola sulla NIC e' potente, ma va usata con criterio.

---

Cosa conta davvero nel risultato finale
•  Il traffico reale dipende dalla combinazione delle regole visibili sulla subnet e sulla NIC
•  Guardare una sola regola spesso porta a conclusioni sbagliate
•  Se un livello blocca il traffico necessario, l'accesso fallisce anche se altrove vedi un allow
•  Per questo Azure offre una vista di sintesi: le effective security rules
Il problema non e' trovare una regola, ma capire l'effetto finale.

---

Effective security rules
•  Sono la vista che aiuta a leggere il comportamento effettivo della VM
•  Riassumono regole default e regole custom che incidono sul traffico
•  Sono utili quando una VM non risponde e vuoi evitare di controllare oggetti a caso
•  Non sostituiscono il ragionamento, ma evitano errori di lettura del contesto
Se devi capire perche' una VM non e' raggiungibile, questa e' una verifica centrale.

---

Caso tipico: pubblicare HTTP
Per raggiungere una pagina web su una VM servono almeno questi elementi:
•  Una Public IP associata al percorso corretto
•  Una regola inbound TCP 80 coerente con il livello scelto
•  Un servizio nella VM che ascolta davvero sulla porta 80
•  Nessun blocco effettivo che annulli quel traffico
La rete da sola non basta: deve esserci anche qualcosa che risponde dentro la VM.

---

Caso tipico: pubblicare HTTPS
•  Dal punto di vista della rete, HTTPS significa soprattutto porta 443
•  Il certificato non risolve una regola mancante: se 443 non passa, il servizio resta irraggiungibile
•  In alcuni casi si lascia aperta anche la 80 per reindirizzare verso 443
•  In altri casi si espone solo 443 per ridurre la superficie visibile
La regola di rete decide il passaggio, il servizio applicativo decide la risposta corretta.

---

Regole troppo larghe e regole troppo strette
Situazione
Rischio
Source = Any su porta sensibile
Espone troppo la VM
Priority non ragionata
Una regola inattesa puo' prevalere
Apertura su subnet intera senza motivo
Allarga la superficie di attacco
Regola troppo specifica o nel punto sbagliato
Il traffico legittimo non passa
•  La sicurezza non e' solo aprire o chiudere: e' aprire bene, nel punto giusto

---

Metodo di troubleshooting
•  Verifica se esiste un Public IP o un percorso di accesso coerente
•  Controlla la porta corretta: 3389, 80, 443 o altra porta prevista
•  Leggi NSG su subnet e su NIC
•  Controlla le effective security rules
•  Verifica che il servizio nella VM stia davvero ascoltando
•  Solo dopo passa ai dettagli piu' fini
Il troubleshooting efficace parte da una sequenza chiara, non da clic casuali.

---

Dove lo verifichi da Cloud Shell
az network nsg rule list --resource-group <rg> --nsg-name <nsg-name> --output table
az network nic list-effective-nsg --resource-group <rg> --name <nic-name>
az vm list-ip-addresses --resource-group <rg> --name <vm-name>
•  Il primo comando elenca le regole dell'NSG
•  Il secondo aiuta a leggere l'effetto effettivo sulla NIC
•  Il terzo mostra gli indirizzi associati alla VM

---

Chiusura del blocco
•  Con VNet, Subnet, NSG ed effective rules hai il minimo per leggere molti problemi reali
•  La rete in Azure non e' solo configurazione: e' controllo dell'accesso e riduzione del rischio
•  Il passo successivo puo' essere ampliare il quadro con routing, peering e accessi piu' strutturati
Prima di creare nuove risorse, conviene saper leggere bene il comportamento della rete.


---

# 8) Microsoft Azure - Reti su Azure - Parte 3

**File:** `8) Microsoft Azure - Reti su Azure - Parte 3.pptx`
**Tipo:** `.pptx`
**Dimensione:** 73.0 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Reti su Azure - Parte 3 (4 ore)

---

Reti su Azure - Parte 3
Routing, peering, pubblicazione e accessi

---

Cosa chiudiamo oggi
•  completiamo il quadro rispetto alla Parte 2 con routing, peering e accessi più strutturati
•  colleghiamo ogni esigenza al servizio giusto: cambiare percorso, collegare reti, pubblicare, tenere privato, amministrare
•  distinguiamo i ruoli principali dei servizi di rete Azure
•  l'obiettivo è leggere una topologia e scegliere il servizio adatto

---

La rete in tre domande
•  Dove sta la risorsa? In una Virtual network, dentro una Subnet
•  Ha un indirizzo solo interno o anche pubblico? Qui entra il Public IP address
•  Chi può raggiungerla? Lo decidono le regole del Network Security Group
•  Se devo ragionare su gruppi di VM, uso un Application Security Group
•  Il senso è semplice: posizione, indirizzo, regole

---

Se il traffico deve cambiare strada
•  Una regola può dire "puoi passare", ma serve anche sapere dove vai
•  In Azure la risorsa si chiama Route table
•  Dentro ci metti le route personalizzate, cioè le UDR
•  Esempio: una subnet deve uscire solo passando da Azure Firewall
•  Quindi: NSG decide se passi, Route table decide il percorso

---

Se devo collegare due reti Azure
•  Il nome da ricordare è VNet peering
•  Serve quando due Virtual network devono parlarsi direttamente
•  Non stai pubblicando su Internet
•  Non stai ancora collegando una sede esterna: stai collegando Azure con Azure
•  Domanda pratica: devo unire due reti cloud o portare dentro una rete da fuori?

---

Collegare una sede o una persona
•  Se invece la rete arriva da fuori Azure, entra in gioco Virtual network gateway
•  Site-to-Site: collega Azure a una sede o a un data center
•  Point-to-Site: collega un singolo computer ad Azure
•  Local network gateway serve a descrivere la rete esterna
•  Qui chiudiamo l'idea di accessi più strutturati: peering tra reti Azure, gateway verso l'esterno

---

Quando la rete cresce
•  ExpressRoute collega Azure a reti aziendali con una connessione dedicata
•  Azure Virtual WAN organizza connettività tra sedi, utenti remoti e reti cloud
•  entrano in gioco quando aumentano sedi, percorsi e punti di accesso
•  completano il quadro della connettività ibrida e multi-sede

---

Pubblicare un servizio
Se devo...
Uso...
distribuire traffico tra VM
Azure Load Balancer
pubblicare un sito o una web app
Azure Application Gateway
•  Load Balancer ragiona da rete
•  Application Gateway ragiona da applicazione web
•  Esempio: due VM dietro Load Balancer, portale studenti con Application Gateway

---

Se gli utenti sono distribuiti
•  Azure Front Door gestisce ingressi globali vicini agli utenti
•  lavora bene quando il traffico arriva da aree geografiche diverse
•  Load Balancer e Application Gateway coprono invece ingressi regionali o applicativi
•  la scelta dipende da dove stanno gli utenti e da come entra il traffico

---

I nomi contano quanto gli IP
•  Se il nome punta male, sembra che la rete non funzioni
•  distinguiamo DNS zones pubbliche e Private DNS zones
•  quando usi servizi privati, anche il DNS entra nella soluzione
•  risoluzione dei nomi e indirizzi IP lavorano insieme

---

Portare un servizio dentro la rete
•  la domanda pratica è: il servizio resta pubblico o entra davvero nella rete?
•  Private Endpoint porta il servizio dentro la rete privata
•  Service Endpoints mantengono il servizio pubblico, ma ne limitano l'accesso alla rete autorizzata
•  qui distinguiamo accesso privato e servizio pubblico filtrato

---

Proteggere i servizi esposti
•  un Network Security Group regola il traffico su subnet e schede di rete
•  Azure Firewall filtra il traffico in modo centralizzato
•  Azure DDoS Protection difende i servizi pubblici da attacchi volumetrici
•  qui distinguiamo filtraggio locale, filtraggio centrale e protezione dell'esposizione pubblica

---

Entrare in una VM senza esporla
•  Lasciare RDP o SSH aperti su Internet è comodo, ma rischioso
•  Azure Bastion ti fa entrare dal portale senza pubblicare 3389 o 22
•  Just-in-time VM access aggiunge un'apertura temporanea quando serve
•  Il principio da ricordare è semplice: amministrazione sì, esposizione no

---

Percorso nel portale Azure
•  Virtual networks: VNet, subnet e peering
•  Route tables e Network security groups: percorso e regole
•  Virtual machines: test di connettività e amministrazione
•  Load balancers o Application gateways: pubblicazione del servizio
•  Storage accounts, Private endpoints e Private DNS zones: accesso privato
•  gateway, Firewall, Front Door, DDoS e Virtual WAN: ruolo nel disegno complessivo

---

Chiusura del blocco
•  rispetto alla Parte 2 il quadro ora include routing, peering e accessi più strutturati
•  ogni servizio occupa un punto preciso nel disegno della rete
•  i nomi aiutano a leggere il portale e l'architettura
•  con questa parte si chiude Reti su Azure (IaaS & edge)
•  da qui in poi il lavoro è applicare questi servizi negli scenari


---

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

