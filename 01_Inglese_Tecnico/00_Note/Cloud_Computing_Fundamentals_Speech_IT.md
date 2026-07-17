# Cloud Computing Fundamentals — Discorso (20 min)

## 1. Introduzione

Buongiorno a tutti. Oggi parliamo di Cloud Computing — una delle tecnologie più trasformative degli ultimi vent'anni. Non è solo un argomento tecnico: è un cambio di paradigma nel modo in cui pensiamo, costruiamo e utilizziamo le risorse informatiche. Partiamo dalle basi e saliremo gradualmente fino ai concetti più avanzati come Serverless e Cloud-Native.

---

## 2. Cos'è il Cloud Computing e come funziona?

Partiamo dalla definizione. Il Cloud Computing è un modello che permette l'accesso on-demand, tramite rete, a un pool condiviso di risorse informatiche configurabili — server, storage, database, rete, software, analisi — che possono essere fornite e rilasciate con minimo sforzo di gestione o interazione con il fornitore.

Tradotto: invece di possedere fisicamente i tuoi computer e server, li noleggi da qualcun altro, li usi attraverso Internet, e paghi solo per quello che consumi.

Come funziona nel concreto? Ci sono tre attori principali: il **fornitore di cloud** (AWS, Azure, Google Cloud), il **cliente** (un'azienda o uno sviluppatore), e l'**utente finale**. Il fornitore possiede e gestisce data center enormi sparsi in tutto il mondo. Il cliente ci gira sopra applicazioni e dati senza doversi preoccupare dell'hardware sottostante. L'utente finale interagisce con queste applicazioni senza sapere — e senza dover sapere — dove risiedono fisicamente i dati.

La magia sta in tre caratteristiche fondamentali. Primo: **il self-service on-demand**. Puoi ottenere risorse in pochi clic o con una chiamata API, senza parlare con un venditore. Secondo: **l'accesso ampio alla rete**. Le risorse sono accessibili da qualsiasi dispositivo connesso a Internet. Terzo: **il pooling delle risorse**. Il fornitore serve molti clienti con le stesse infrastrutture fisiche, ottenendo economie di scala che si traducono in costi più bassi per tutti.

A questo si aggiungono due caratteristiche che definiscono l'esperienza cloud: la **rapida elasticità** — se la tua applicazione ha un picco di traffico, il cloud aggiunge automaticamente più risorse; se il traffico cala, le rilascia — e il **servizio misurato**, cioè paghi a consumo come per la luce o il gas. Niente bollette fisse, niente capacità inutilizzata.

---

## 3. L'evoluzione dai data center tradizionali al cloud

Per capire perché il cloud è così rivoluzionario, guardiamo da dove veniamo.

Fino ai primi anni 2000, se un'azienda voleva un'applicazione web, comprava server fisici. Doveva trovare spazio in un data center — spesso un locale appositamente costruito con raffreddamento, gruppi di continuità, sicurezza fisica. Doveva configurare rete, storage, backup. Doveva prevedere il carico futuro e comprare hardware con mesi di anticipo. Se il picco era più alto del previsto? L'applicazione crashava. Se era più basso? I server restavano spenti, soldi buttati.

Poi è arrivata la **virtualizzazione**. Un server fisico poteva ospitare più macchine virtuali, ognuna con il suo sistema operativo. Questo ha migliorato l'utilizzo delle risorse, ma il salto vero è stato il **cloud pubblico**. Nel 2006 Amazon lancia AWS con servizi come S3 per lo storage e EC2 per il calcolo. Nasce l'idea che l'infrastruttura non sia più un bene da possedere, ma un servizio da consumare.

Oggi siamo alla terza o quarta generazione: l'infrastruttura è programmabile via API, gestita con codice (Infrastructure as Code), e orchestrata da Kubernetes. Il data center non è più un luogo: è un'astrazione.

---

## 4. Modelli di servizio: IaaS, PaaS e SaaS

Il cloud si divide in tre modelli di servizio principali, che rappresentano diversi livelli di astrazione e responsabilità.

**IaaS — Infrastructure as a Service.** È il modello più vicino all'hardware tradizionale. Il fornitore ti dà macchine virtuali, storage, rete, e tu ci installi sopra sistema operativo, middleware, applicazioni. Hai massimo controllo, ma anche massima responsabilità di gestione. Esempi: AWS EC2, Google Compute Engine, Azure Virtual Machines. Chi lo usa? Amministratori di sistema, aziende che migrano carichi di lavoro esistenti senza modificarli.

**PaaS — Platform as a Service.** Qui il fornitore gestisce anche il sistema operativo, i runtime, il middleware. Tu porti solo il codice e i dati. Fai il deploy di un'applicazione senza preoccuparti di patch di sicurezza, aggiornamenti del sistema, scaling dell'infrastruttura. Esempi: Google App Engine, Heroku, Azure App Services. Chi lo usa? Sviluppatori che vogliono concentrarsi sul codice, non sull'infrastruttura.

**SaaS — Software as a Service.** Il prodotto finale, pronto all'uso. Il fornitore gestisce tutto: hardware, piattaforma, applicazione, dati. Tu apri un browser e usi il software. Non installi nulla, non gestisci nulla. Esempi: Gmail, Microsoft 365, Salesforce, Dropbox. Chi lo usa? Tutti — ogni utente finale.

C'è anche una metafora utile: IaaS è come comprare terreni e materiali da costruzione. PaaS è come affittare una casa già costruita ma vuota. SaaS è come affittare una casa già arredata con le utenze attive. Ognuno sceglie il modello che bilancia meglio controllo e convenienza per le proprie esigenze.

---

## 5. Pubblico, Privato, Ibrido e Multi-Cloud

Non tutto il cloud è uguale. Esistono diversi modelli di deployment.

**Cloud Pubblico.** L'infrastruttura è di proprietà del fornitore, situata nei suoi data center, e condivisa tra più clienti. Vantaggi: nessun costo di capitale iniziale, elasticità massima, paghi solo l'uso. Svantaggi: controllo ridotto, potenziali problemi di conformità normativa per dati sensibili.

**Cloud Privato.** L'infrastruttura è dedicata a una singola organizzazione. Può essere on-premise o gestita da un fornitore terzo. Vantaggi: controllo totale, sicurezza, conformità. Svantaggi: costi iniziali elevati, manutenzione interna, elasticità limitata dalle risorse fisiche a disposizione.

**Cloud Ibrido.** Combina cloud pubblico e privato, con orchestrazione tra i due. I dati e le applicazioni possono muoversi tra ambienti. L'esempio classico: un'applicazione bancaria gira su cloud privato per i dati sensibili, ma scala su cloud pubblico durante i picchi di traffico senza esporre dati critici. Vantaggi: flessibilità, sicurezza, ottimizzazione dei costi. Svantaggi: complessità operativa maggiore.

**Multi-Cloud.** Usi più fornitori di cloud pubblico contemporaneamente — AWS per il calcolo, Azure per Active Directory, Google Cloud per machine learning. Vantaggi: eviti il vendor lock-in, scegli il servizio migliore per ogni esigenza. Svantaggi: complessità gestionale significativa, necessità di competenze su più piattaforme sempre aggiornate.

La tendenza oggi? Secondo i report di settore, oltre l'80% delle aziende adotta già un approccio multi-cloud o ibrido. Il cloud puro e semplice non basta più — serve una strategia.

---

## 6. Vantaggi e svantaggi

Vediamo in modo equilibrato pro e contro.

**Vantaggi.** Il primo è economico: niente CapEx iniziale. Invece di milioni in hardware, paghi OpEx mensile. Secondo: elasticità. Se la tua startup cresce del 1000% in una settimana, il cloud non ti ferma. Se cala, non paghi risorse inutilizzate. Terzo: time-to-market. Un team di sviluppo può lanciare un'infrastruttura di produzione in minuti invece di settimane. Quarto: sicurezza. I grandi fornitori investono miliardi in sicurezza fisica e logica — cifre che nessuna azienda media può eguagliare. Quinto: disaster recovery. I dati sono replicati in più regioni geografiche. Un incendio in un data center? I servizi continuano da un'altra parte.

**Svantaggi.** Primo: costi imprevedibili. Se non monitori, a fine mese la bolletta può sorprenderti. Secondo: dipendenza dalla connettività. Senza Internet, non lavori. Terzo: vendor lock-in. Una volta che costruisci la tua architettura sui servizi proprietari di AWS, migrare altrove diventa complesso e costoso. Quarto: controllo ridotto. Se AWS ha un outage, il tuo servizio è giù — e non puoi farci nulla. Quinto: conformità. Certi settori — sanità, finanza, pubblica amministrazione — hanno vincoli normativi severi su dove e come i dati possono risiedere. Non tutto può andare sul cloud.

La chiave? Valutare caso per caso. Non esiste una risposta universale: ogni carico di lavoro ha il suo ambiente ideale.

---

## 7. Edge Computing vs Cloud Computing

Fin qui abbiamo parlato di dati che viaggiano verso data center centralizzati. Ma c'è un problema: la latenza.

Pensa a un'auto a guida autonoma. Se deve fermarsi per un ostacolo, non può aspettare che i dati vadano a un cloud regionale e tornino indietro. Servono millisecondi, non centinaia di millisecondi. Entra in gioco l'**Edge Computing**: l'elaborazione avviene vicino alla fonte dei dati — sul dispositivo stesso, su un gateway locale, su un server edge in un punto di presenza della rete.

Il cloud computing è centralizzato, potente, ideale per elaborazioni pesanti e dati storici. L'edge computing è distribuito, veloce, ideale per applicazioni real-time come IoT, veicoli autonomi, realtà aumentata, smart manufacturing.

Non sono in competizione: sono complementari. L'architettura moderna è spesso un continuum: i dispositivi edge raccolgono dati e eseguono decisioni rapide, i nodi intermedi aggregano, il cloud centrale fa analisi complesse e machine learning. L'esempio tipico: un termostato smart regola la temperatura localmente, ma invia i dati di utilizzo al cloud per migliorare gli algoritmi di previsione.

La crescita dell'IoT e del 5G sta accelerando l'edge computing. Gartner prevede che entro il 2028 il 75% dei dati aziendali sarà elaborato al di fuori dei data center centralizzati.

---

## 8. Serverless Computing

Un altro passo avanti nell'astrazione: il **Serverless Computing**. Il nome è fuorviante — server ci sono eccome — ma lo sviluppatore non li vede, non li gestisce, non li configura. Scrive solo funzioni, le carica sul cloud, e dice "esegui questa funzione quando succede X".

Immagina di voler ridimensionare un'immagine ogni volta che viene caricata. Con un approccio tradizionale, tieni un server in esecuzione in attesa di richieste. Con serverless, scrivi una funzione di poche righe, la colleghi a un evento di upload, e il cloud esegue la funzione solo quando serve. Se arrivano zero richieste, non paghi nulla. Se arrivano un milione, il cloud scala automaticamente.

I fornitori principali: AWS Lambda, Azure Functions, Google Cloud Functions.

Vantaggi: nessuna gestione di server, scaling automatico, paghi solo per il tempo di esecuzione — anche al millisecondo. Perfetto per carichi di lavoro intermittenti, microservizi, webhook, backend di applicazioni mobile.

Svantaggi: cold start — se una funzione non viene chiamata per un po', il successivo avvio impiega centinaia di millisecondi extra. Limiti di tempo di esecuzione — le funzioni Lambda muoiono dopo 15 minuti. Difficile debug locale. Complessità nel test.

Il serverless non sostituisce tutto, ma per certe categorie di problemi è difficilmente battibile in termini di efficienza e costo.

---

## 9. Applicazioni Cloud-Native

Ultimo tema: le **applicazioni Cloud-Native**. Non basta girare su cloud per essere cloud-native. Un'applicazione tradizionale semplicemente migrata su una macchina virtuale non sfrutta il cloud — ci vive dentro, ma non ne usa le potenzialità.

Un'applicazione cloud-native è progettata fin dall'inizio per il cloud. Si basa su quattro pilastri.

Primo: **microservizi**. L'applicazione è scomposta in tanti piccoli servizi indipendenti, ognuno con la propria responsabilità. Non un unico blocco monolitico, ma decine o centinaia di componenti che comunicano via API.

Secondo: **container**. Ogni microservizio gira in un container — leggero, isolato, riproducibile. Docker è lo standard, Kubernetes l'orchestratore di fatto.

Terzo: **DevOps e Continuous Delivery**. I deployment sono frequenti, automatizzati, ripetibili. L'infrastruttura è codice. I test e la sicurezza sono integrati nella pipeline di sviluppo.

Quarto: **resilienza e osservabilità**. L'applicazione assume che i componenti falliranno — e si progetta di conseguenza con retry, circuit breaker, graceful degradation. E deve essere osservabile: logging centralizzato, metriche, tracing distribuito.

Esempi di architetture cloud-native: Netflix, Spotify, Uber. Non potrebbero esistere senza cloud — la loro scala e velocità di innovazione richiedono queste tecnologie.

---

## 10. Conclusione

Per chiudere: il cloud computing non è solo una tecnologia, è un nuovo modo di pensare l'IT. È passare dal possesso all'accesso, dalla capacità fissa all'elasticità, dall'hardware al software.

Abbiamo visto le fondamenta: cos'è e come funziona. L'evoluzione storica dai data center tradizionali. I tre modelli di servizio — IaaS, PaaS, SaaS. I modelli di deployment — pubblico, privato, ibrido, multi-cloud. Vantaggi e svantaggi. E poi i frontier: edge computing, serverless, cloud-native.

Il messaggio finale è questo: il cloud non è una destinazione, è un viaggio. Le aziende non "finiscono" di migrare al cloud — evolvono continuamente il loro modo di usarlo. E chi capisce questi fondamenti ha gli strumenti per partecipare a questa evoluzione.

Grazie.
