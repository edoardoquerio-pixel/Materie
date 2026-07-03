# 14 - Cloud Azure — Tutte le Sessioni


---

## Sessione 1: Lezione 1


### Slide 1
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
Introduzione (4 ore)
### Slide 2
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
### Slide 3
Oggi: introduzione (4 ore)
•  Perché questo corso esiste
•  IT e sostenibilità: il contesto normativo e tecnologico
•  Smart working, smart grid, sensori ambientali
•  Economia circolare e gestione RAEE
•  Dal data center al cloud: il collegamento
•  Cos'è il cloud, come funziona, chi lo offre
•  Primo sguardo ad Azure
### Slide 4
Perché un corso su Azure
•  Il cloud è l'infrastruttura standard per aziende di ogni dimensione
•  Le competenze cloud sono tra le più richieste nel mercato IT
•  Azure è la piattaforma cloud di Microsoft — la seconda per quota di mercato globale
•  Un Cloud Specialist deve saper progettare, distribuire e gestire servizi su Azure
•  100 ore: dall'architettura di base fino a DevOps e gestione dei costi
### Slide 5
IT e sostenibilità: il quadro
•  L'Unione Europea ha fissato obiettivi di riduzione delle emissioni al 2030 e 2050
•  Il settore IT è responsabile di circa il 2-4% delle emissioni globali di CO₂
•  Allo stesso tempo, l'IT è uno strumento per ridurre consumi ed emissioni in altri settori
•  La normativa europea (Green Deal, CSRD, tassonomia) impone obblighi di rendicontazione
•  Per un tecnico IT, capire questo contesto non è opzionale: è parte del lavoro
### Slide 6
Smart working: tecnologie e impatto
•  Lavorare da remoto richiede infrastruttura IT: VPN, strumenti di collaborazione, sicurezza degli endpoint
•  Riduce spostamenti, quindi emissioni da trasporto
•  Richiede connettività affidabile e gestione centralizzata dei dispositivi
•  Strumenti tipici: Microsoft 365, Teams, VDI (Virtual Desktop Infrastructure)
•  Lato IT: il perimetro di sicurezza si sposta dall'ufficio al singolo dispositivo
•  Il cloud abilita lo smart working perché i servizi sono raggiungibili ovunque
### Slide 7
Smart grid: la gestione IT delle reti energetiche
•  Una smart grid è una rete elettrica che usa sensori, comunicazione e software per gestire la distribuzione dell'energia
•  L'IT serve a raccogliere dati dai contatori, prevedere i consumi, bilanciare domanda e offerta
•  Tecnologie coinvolte: protocolli di comunicazione (MQTT, AMQP), piattaforme IoT, database time-series
•  Il cloud fornisce la capacità di calcolo e archiviazione necessaria per elaborare grandi volumi di dati in tempo reale
•  In Italia: il contatore elettronico di seconda generazione (2G) è un esempio concreto di smart metering
### Slide 8
Sensori in rete per il monitoraggio ambientale
•  Sensori distribuiti misurano qualità dell'aria, temperatura, umidità, livello delle acque, rumore
•  I dati vengono trasmessi via rete (LoRaWAN, NB-IoT, 4G/5G) a piattaforme centrali
•  Il ruolo dell'IT: raccolta, validazione, archiviazione, visualizzazione e alerting
•  Volumi di dati potenzialmente molto alti → servono soluzioni scalabili
•  Il cloud è la scelta naturale: si paga in base all'uso, si scala con la domanda
•  Servizi Azure coinvolti: IoT Hub, Stream Analytics, Azure Maps
### Slide 9
Economia circolare: principi fondamentali
•  Modello lineare: estrai → produci → usa → butta
•  Modello circolare: progetta per durare, ripara, riusa, ricicla
•  La normativa UE spinge verso la circolarità (Regolamento Ecodesign, Direttiva Right to Repair)
•  Per l'IT questo significa:
○  Progettare software che giri su hardware meno recente
○  Prolungare la vita utile dei dispositivi con aggiornamenti e manutenzione
○  Scegliere fornitori cloud che usino energia rinnovabile
○  Monitorare e ridurre il consumo delle risorse computazionali
### Slide 10
Estendere la vita utile di prodotti e componenti
•  Un server fisico ha una vita utile media di 4-5 anni; spesso viene dismesso prima del necessario
•  Il ricondizionamento (refurbishing) è una pratica consolidata per PC, monitor, smartphone
•  Lato software: supporto a lungo termine (LTS), compatibilità con hardware datato, aggiornamenti di sicurezza
•  La virtualizzazione ha già allungato la vita dei server: più carichi su meno macchine fisiche
•  Il cloud porta questo concetto oltre: il fornitore gestisce il ciclo di vita dell'hardware, il cliente usa solo il servizio

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 2: Lezione 10


### Slide 1
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
Compute su Azure: dischi, scalabilità e costo delle VM (4 ore)
### Slide 2
Compute su Azure
Dischi, scalabilità e costo delle VM
### Slide 3
Da dove proseguiamo
•  abbiamo già visto come si sceglie una VM: immagine, size, regione, disponibilità
•  adesso guardiamo che cosa cambia davvero prestazioni e costo nel tempo
•  i punti chiave sono dischi, ridimensionamento, scale set e scelte di spesa
•  la domanda è pratica: questa VM basta, costa il giusto, cresce bene?
### Slide 4
Perché il disco conta
•  il disco non è solo spazio
•  influenza velocità di avvio, risposta dell'app e costo della VM
•  un disco lento può frenare anche una VM ben dimensionata
•  per questo compute e storage si leggono insieme
### Slide 5
Tipi di disco in Azure
casi economici e poco intensi
uso base con latenza più stabile
VM applicative e workload più reattivi
casi molto esigenti su IOPS e throughput
•  non tutti i tipi servono in ogni scenario
### Slide 6
Standard, Premium, Ultra
•  Standard: costa meno, va bene per test o carichi leggeri
•  Premium: è il riferimento quando conta la reattività
•  Ultra: serve solo per workload molto spinti
•  la scelta va fatta sul bisogno reale, non sul livello più alto disponibile
### Slide 7
OS disk e data disk
•  il OS disk contiene sistema operativo e avvio della VM
•  i data disk ospitano dati, log o parti dell'applicazione
•  separarli aiuta a gestire meglio prestazioni e crescita
•  non tutto deve stare sul disco del sistema
### Slide 8
Caching: che cosa significa
•  il caching usa memoria locale dell'host per accelerare alcuni accessi al disco
•  può essere utile in lettura o in lettura/scrittura, secondo il caso
•  non è una spunta magica: va allineato al comportamento del carico
•  prima capisco l'uso del disco, poi scelgo il caching
### Slide 9
Encryption dei dischi
cifratura dei dati a riposo
chiavi gestite dalla piattaforma Azure
chiavi gestite dal cliente, di solito via Key Vault
•  il punto comune è proteggere i dati memorizzati sui dischi
### Slide 10
Ridimensionare una VM
•  una VM può cambiare size se la stima iniziale non era corretta
•  aumentare o ridurre la taglia è il primo passo di right-sizing
•  non sempre serve creare una nuova macchina
•  prima misuro il bisogno, poi cambio dimensione
### Slide 11
Scale up e scale out
dare più risorse a una VM
usare più istanze simili
•  lo scale up è più semplice
•  lo scale out richiede un'app più distribuita
•  entrambi impattano costo e disponibilità
### Slide 12
Virtual Machine Scale Set
•  uno Scale Set gestisce più VM simili come un gruppo
•  serve quando più istanze fanno lo stesso lavoro
•  può crescere o ridursi con regole di autoscaling
•  è il passaggio naturale quando una sola VM non basta più
### Slide 13
Costo compute: che cosa incide
•  la size della VM pesa molto sul costo orario
•  contano anche dischi, tempo di accensione e numero di istanze
•  una VM accesa ma poco usata resta comunque una spesa
•  ottimizzare vuol dire usare risorse proporzionate
### Slide 14
Right-sizing, RI e Savings Plans
•  Right-sizing: scegliere o correggere la taglia giusta
•  Reserved Instances: convenienza se il carico è stabile nel tempo

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 3: Lezione 11


### Slide 1
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
Compute su Azure: App Service e Functions (4 ore)
### Slide 2
Compute su Azure
App Service e Functions
### Slide 3
Dalla VM al servizio gestito
•  con una VM gestisci sistema operativo, patch, runtime e applicazione
•  con App Service porti soprattutto codice e configurazione
•  con Functions porti funzioni che si attivano a evento
•  il cambio di logica è: meno server da gestire, più focus sull'applicazione
### Slide 4
App Service: idea base
•  App Service pubblica web app e API senza gestire una VM
•  Azure gestisce OS, runtime, patching e integrazione con la piattaforma
•  tu gestisci codice, configurazione, dominio, scaling e osservabilità
•  è una scelta tipica quando l'app è web o HTTP API
### Slide 5
App Service Plan
•  il piano decide dove gira l'app e quante risorse usa
•  più app possono condividere lo stesso piano
•  cambiare piano cambia capacità, costo e funzionalità disponibili
•  l'app è il sito; il piano è la capacità che lo ospita
### Slide 6
Web App e API App
sito web o backend HTTP
API consumata da app o servizi
•  nella pratica entrambe stanno dentro il modello App Service
•  la distinzione aiuta a ragionare sul tipo di applicazione
### Slide 7
Deployment slot
•  uno slot è un ambiente parallelo alla produzione
•  esempio: production e staging
•  puoi pubblicare una versione nuova nello slot di test
•  poi fai swap per portarla in produzione con meno rischio
### Slide 8
Scaling in App Service
•  Scale up: cambio piano o capacità del piano
•  Scale out: aumento il numero di istanze
•  l'autoscale può reagire a metriche come CPU o richieste
•  il costo segue il piano e le istanze usate
### Slide 9
Quando scegliere App Service
•  applicazioni web e API
•  deploy frequenti e gestione semplice
•  integrazione con domini, certificati, log e scaling
•  quando non serve controllare direttamente il sistema operativo
### Slide 10
Azure Functions: idea base
•  Azure Functions esegue codice in risposta a un evento
•  una funzione non è una web app intera
•  è un pezzo di logica che parte quando succede qualcosa
•  esempi: richiesta HTTP, messaggio in coda, timer, file caricato
### Slide 11
Trigger e binding
evento che avvia la funzione
dato letto dalla funzione
destinazione su cui la funzione scrive
•  la funzione dichiara collegamenti che Azure gestisce per lei
### Slide 12
API leggera o webhook
attività pianificata
elaborare messaggi
reagire a un file caricato
•  il trigger racconta perché il codice parte
### Slide 13
App Service o Functions?
Scelta naturale
tenere online un'app web o API
reagire a eventi separati
gestire OS e software specifico
•  non sono livelli migliori o peggiori: rispondono a problemi diversi
### Slide 14
Limiti pratici in aula
•  con Azure for Students alcune opzioni possono essere limitate
•  App Service e Functions sono più adatti a demo leggere rispetto ad AKS
•  se un piano o una regione non compare, si verifica prima subscription e disponibilità

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 4: Lezione 12


### Slide 1
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
Compute su Azure: container, AKS e ottimizzazione (4 ore)
### Slide 2
Compute su Azure
Container, AKS e ottimizzazione
### Slide 3
Perché arriviamo ai container
•  una VM porta con sé sistema operativo e gestione completa
•  App Service riduce la gestione del server
•  il container impacchetta applicazione e dipendenze in modo ripetibile
•  il problema diventa: dove faccio girare quel container?
### Slide 4
Container: idea base
•  un container contiene app, runtime e dipendenze
•  parte da un'immagine container
•  gira in modo più leggero di una VM completa
•  non sostituisce sempre la VM: risponde a un modello diverso di distribuzione
### Slide 5
Container Instances
•  Azure Container Instances esegue container singoli senza gestire server
•  è adatto a prove rapide, job semplici o processi isolati
•  parti da un'immagine e Azure avvia il container
•  è il modo più diretto per eseguire un container su Azure
### Slide 6
App Service for Containers
•  porta il modello App Service su applicazioni containerizzate
•  utile quando hai una web app dentro un container
•  mantieni funzionalità come dominio, scaling e gestione piattaforma
•  è un ponte tra PaaS web e mondo container
### Slide 7
Quando serve Kubernetes
•  quando i container diventano molti
•  quando servono replica, aggiornamenti controllati e self-healing
•  quando l'app è composta da più servizi
•  Kubernetes organizza container su un cluster di nodi
### Slide 8
AKS: Kubernetes gestito
•  AKS è Azure Kubernetes Service
•  Azure gestisce il piano di controllo Kubernetes
•  tu gestisci nodi, workload, networking e aggiornamenti applicativi
•  sotto ci sono VM, ma non le tratti come VM singole
### Slide 9
•  un node pool è un gruppo di nodi con caratteristiche simili
•  i nodi sono le macchine su cui girano i pod
•  puoi avere pool diversi per workload diversi
•  scegliere i nodi significa scegliere costo e capacità del cluster
### Slide 10
•  i pod devono comunicare tra loro
•  alcuni servizi devono essere raggiunti dall'esterno
•  entrano in gioco rete del cluster, servizi e ingress
•  qui tornano concetti già visti: subnet, IP, bilanciamento, sicurezza
### Slide 11
Aggiornamenti in AKS
•  un cluster va aggiornato nel tempo
•  si aggiornano Kubernetes, nodi e applicazioni
•  gli aggiornamenti vanno pianificati per ridurre interruzioni
•  AKS semplifica, ma non elimina la responsabilità operativa
### Slide 12
ACI, App Service for Containers, AKS
Scelta naturale
eseguire un container singolo
Container Instances
pubblicare una web app containerizzata
App Service for Containers
orchestrare molti container
•  la scelta dipende da complessità e responsabilità operativa
### Slide 13
Ottimizzazione compute
•  scegli il servizio più semplice che risolve il problema
•  spegni o riduci ciò che non serve
•  usa scaling quando il carico cambia
•  misura prima di aumentare risorse
•  collega sempre prestazioni, disponibilità e costo
### Slide 14
Riepilogo del blocco Compute
controllo completo dell'OS
web app o API gestita

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 5: Lezione 13


### Slide 1
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
Storage, Data & Integration - PT1: Storage account, servizi dati, sicurezza e accesso storage (4 ore)
### Slide 2
Storage account e servizi dati
•  Storage account: General Purpose v2 e Premium
•  Servizi disponibili: Blob, File, Queue, Table
•  Casi d'uso principali dei servizi dati e quando scegliere Azure Files
•  Criteri di scelta: prestazioni, latenza, costo e tipo di workload
•  Scelte iniziali: naming, regione e ridondanza del dato
### Slide 3
Perché partiamo dallo storage account
•  Lo storage account è il contenitore logico dei principali servizi dati di base su Azure.
•  Dentro uno storage account puoi trovare Blob, File, Queue e Table.
•  Le scelte fatte all'inizio influenzano costo, prestazioni e resilienza.
•  Prima di creare i dati, conviene capire che tipo di workload stiamo servendo.
•  Il punto non è solo salvare dati: è scegliere il servizio giusto.
### Slide 4
General Purpose v2 o Premium
Quando ha senso
General Purpose v2
scelta standard per la maggior parte dei workload
latenza più bassa e prestazioni più alte su scenari specifici
•  GPv2 è il punto di partenza naturale in quasi tutti i progetti.
•  Premium si usa quando il carico giustifica davvero il costo più alto.
•  La domanda giusta è: che prestazioni servono davvero?
### Slide 5
I quattro servizi da ricordare
oggetti, file applicativi, immagini, log, backup
file share gestite con accesso tipo file server
messaggi semplici tra componenti
dati NoSQL chiave-valore semplici
•  Lo stesso storage account può esporre più servizi.
•  Cambia il modello di accesso, non solo il nome.
### Slide 6
Quando scegliere ciascun servizio
•  Blob se devi salvare file o oggetti non strutturati.
•  Azure Files se ti serve una share condivisa come servizio gestito.
•  Queue se devi disaccoppiare producer e consumer con messaggi semplici.
•  Table se ti basta un archivio NoSQL leggero e poco complesso.
•  Se il dato è relazionale o molto strutturato, di solito serve un servizio diverso.
### Slide 7
Regione e ridondanza del dato
•  La regione conta per latenza, vicinanza agli utenti e conformità.
•  LRS tiene copie locali nello stesso datacenter.
•  ZRS distribuisce le copie su più zone della stessa regione.
•  GRS e varianti simili aggiungono replica geografica.
•  Più protezione significa spesso più costo e più complessità di scelta.
### Slide 8
Nel wizard, cosa guardare davvero
•  Performance: Standard o Premium.
•  Redundancy: LRS, ZRS o replica geografica.
•  Region: dove vivrà davvero il dato.
•  Naming: regole semplici e nomi coerenti.
•  Public access e rete: da decidere subito, non solo dopo.
### Slide 9
Sicurezza e accesso storage
•  Accesso ai dati: SAS, Shared Key e Managed Identity
•  Differenza tra credenziale applicativa e accesso operativo
•  Protezione rete con Firewall storage e regole VNET
•  Riduzione superficie esposta con accessi controllati e segmentazione
### Slide 10
Perché la sicurezza storage è delicata
•  Lo storage contiene spesso file applicativi, dati aziendali, log e backup.
•  Se l'accesso è troppo ampio, il rischio non è solo leggere i dati ma anche modificarli o cancellarli.
•  Bisogna distinguere l'accesso degli amministratori da quello delle applicazioni.
•  L'obiettivo è ridurre privilegi, superficie esposta e segreti in chiaro.
•  Qui la parte tecnica e quella operativa si toccano davvero.
### Slide 11
Tre modi comuni di dare accesso
accesso pieno basato sulla chiave dell'account
accesso limitato per tempo, permessi e risorsa
Managed Identity
accesso senza segreti nel codice
•  La chiave account è potente ma anche rischiosa.
•  La SAS restringe meglio il perimetro.
•  La Managed Identity è spesso la scelta più pulita per i workload Azure.
### Slide 12

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 6: Lezione 14


### Slide 1
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
Storage, Data & Integration: protezione dati, file service e backup (4 ore)
### Slide 2
Storage, protezione dati e file service (4 ore)
•  Lifecycle, tiering e retention per governare costo e ciclo di vita del dato
•  Versioning, soft delete e immutabilita per protezione operativa e compliance
•  Azure Files con identita centralizzate e permessi a due livelli
•  Backup e recovery per continuita operativa verificabile
### Slide 3
Blob tiering: Hot, Cool, Archive
dati letti spesso
dati letti saltuariamente
dati rari, conservazione lunga
•  Il tier influenza costo di storage e costo/tempo di accesso
•  Non esiste tier migliore in assoluto: dipende dal comportamento del dato
•  La scelta corretta parte da frequenza reale di lettura
### Slide 4
Lifecycle management e retention
•  Le regole lifecycle automatizzano spostamento e cancellazione blob
•  Condizioni comuni: età del dato, prefisso, tipo di contenuto
•  Vantaggio: meno operazioni manuali e costo più stabile nel tempo
•  Retention va allineata a esigenze operative e vincoli normativi
•  Lifecycle è una policy continua, non una attività una tantum
### Slide 5
Versioning, soft delete e immutabilita
•  Versioning: mantiene storico delle modifiche ai blob
•  Soft delete: recupera cancellazioni accidentali in finestra definita
•  Immutabilita (WORM): blocca modifica/cancellazione per un periodo
•  Versioning e soft delete coprono errori operativi
•  WORM copre integrita forte, audit e requisiti di compliance
### Slide 6
Protezione e costo: combinare le leve
Leva principale
ridurre costo nel tempo
lifecycle + tiering
recuperare errori utente
versioning + soft delete
garantire integrita legale
immutabilita WORM
•  Non si attiva tutto per default: si sceglie in base al rischio
•  La soluzione giusta e una combinazione coerente di controlli
### Slide 7
Azure Files: quando usarlo
•  Azure Files fornisce file share SMB gestite nello Storage Account
•  Utile per workload che si aspettano condivisioni file classiche
•  Adatto a directory condivise, profili utente e applicazioni lift-and-shift
•  Se serve modello object/API, spesso e preferibile Blob Storage
•  La scelta dipende dal modo in cui l'app legge e scrive i dati
### Slide 8
Identita centralizzate per Azure Files
•  Accesso integrabile con identita directory (AD DS o Entra in scenari compatibili)
•  Si riducono account locali e credenziali statiche
•  Gruppi e ruoli semplificano concessione e revoca accessi
•  Il controllo accessi diventa uniforme e tracciabile nel tempo
•  Obiettivo: governance chiara tra utenti, gruppi e risorse
### Slide 9
Permessi: livello share e livello NTFS
•  Permessi share: definiscono chi puo accedere alla condivisione
•  Permessi NTFS: definiscono cosa puo fare dentro file e cartelle
•  Accesso effettivo = intersezione dei due livelli
•  Errore tipico: un livello corretto e l'altro errato
•  Verifica sempre entrambe le dimensioni prima del go-live
### Slide 10
Backup, recovery e continuita operativa
•  Recovery Services Vault centralizza policy e operazioni di restore
•  Backup senza test di restore non garantisce recupero reale
•  RPO: perdita dati accettabile, RTO: tempo massimo di ripristino
•  Policy e retention devono essere coerenti con criticita servizio
•  Continuita operativa = tecnologia + procedure verificate
### Slide 11
Scenario integrato: scelta guidata
dati poco letti ma da tenere
lifecycle verso Cool/Archive
rischio sovrascrittura/cancellazione
versioning + soft delete
requisito legale di integrita
immutabilita WORM

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 7: Lezione 15


### Slide 1
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
AI su Azure: Foundry, modelli e GitHub Copilot (in preparazione all'evento Microsoft Build //localhost Torino) (4 ore)
### Slide 2
Foundry, modelli e GitHub Copilot: cosa c'è sotto le demo del Microsoft Build //localhost Torino
### Slide 3
•  Dove sta l'AI nel catalogo Azure (AI Services, Azure OpenAI, Foundry)
•  Azure AI Foundry: risorsa, progetto, hub — cosa sono davvero
•  Deployare un modello (gpt-4o-mini) e usarlo dal playground
•  Chiamare il modello via endpoint + key (il ponte verso il codice)
•  GitHub Copilot e i modelli di Foundry
•  Agenti: il loop "ragiona → usa strumento → risponde" (cenni)
•  Responsible AI e costi a token
•  Filo conduttore: è tutta infrastruttura Azure che già conoscete
### Slide 4
Dove sta l'AI nel catalogo Azure
•  Azure AI Services — modelli pronti via API: Vision, Language, Speech, Translator
•  Azure OpenAI — i modelli GenAI (GPT, ecc.) ospitati su Azure, con endpoint e key
•  Azure AI Foundry — l'hub di lavoro sopra i modelli: deploy, playground, agenti, RAG
“Stessa logica di sempre: una risorsa dentro un resource group, in una regione, con identità e accesso che già sapete gestire. L'AI non è un mondo a parte.”
### Slide 5
Azure AI Foundry: i pezzi
•  Risorsa di Foundry — l'account (tipo AIServices) che contiene tutto
•  Progetto — l'area di lavoro dentro la risorsa: modelli, agenti, dati, valutazioni
•  Hub (versione classica) — workspace condiviso, costruito sopra Machine Learning
“Due esperienze convivono: la "Nuova fonderia" (risorsa + progetto) e l'hub classico. Stesso obiettivo, organizzazione diversa.”
### Slide 6
Deployare un modello e provarlo
•  Dal catalogo (oltre 100 modelli: OpenAI, Llama, Mistral, Cohere…) si sceglie e si fa deploy.
•  Il deployment è il "modello pubblicato": ha un nome e si chiama da playground e API.
•  Per la demo: `gpt-4o-mini` — economico, veloce, multimodale.
•  Nel playground / Chat si prova subito: prompt → risposta.
•  Concetti da mostrare lì: system prompt (istruzioni), temperature, token.
### Slide 7
Dal playground al codice
•  Il playground è comodo, ma in produzione si chiama il modello via API.
•  Servono due cose: l'endpoint della risorsa e una key (oppure Managed Identity).
curl "$ENDPOINT/openai/deployments/gpt-4o-mini/chat/completions?api-version=2024-08-01-preview" \
-H "api-key: $KEY" -H "Content-Type: application/json" \
-d '{"messages":[{"role":"user","content":"Ciao!"}]}'
“Stesso modello, stessa risposta del playground: cambia solo che ora lo chiama il tuo codice.”
### Slide 8
GitHub Copilot e i modelli di Foundry
•  GitHub Copilot = assistente AI dentro l'editor (scrive, spiega, refattorizza codice).
•  Non è "un altro modello": dietro usa modelli (OpenAI e altri) e oggi può collegarsi a modelli ospitati su Azure / Foundry.
•  Vantaggio per l'azienda: stessi modelli, governance, billing e dati sotto il proprio tenant Azure.
•  Due usi complementari:
○  Copilot → produttività dello sviluppatore
○  modello via API/Foundry → AI dentro l'applicazione che costruisci
### Slide 9
Agenti: oltre la singola risposta
•  Un agente non si limita a rispondere: ragiona → usa uno strumento → risponde.
•  Strumenti tipici: Code Interpreter (esegue codice), ricerca su dati/RAG, funzioni custom.
•  Esempio: "somma dei primi 50 numeri primi" → l'agente scrive ed esegue codice e poi spiega.
•  Agenti, routine e workflow: dal singolo agente a più passi orchestrati (routine ricorrenti, workflow multi-step e multi-agente).
•  È il loop "agentico" che vedremo all'evento (Foundry Agents).
•  Nota reale: creare agenti richiede il ruolo dati Foundry User sulla risorsa (RBAC).
### Slide 10
Responsible AI e costi
•  Allucinazioni: il modello può affermare cose false con tono sicuro → serve verifica umana.
•  Bias e content filter: Azure applica filtri sui contenuti; l'AI Act UE classifica per rischio.
•  Dati: con Azure i prompt restano nel tuo tenant (governance, compliance).
•  Costi a token: i modelli Standard/GlobalStandard sono pay-per-token → da fermi non costano.
○  eccezione: i deployment Provisioned (PTU) riservano capacità e si pagano a ore.
### Slide 11
Da portare a casa (e all'evento)
•  L'AI su Azure è una risorsa + un modello deployato: ci parli con endpoint e key, come ogni servizio.
•  Foundry è lo studio di lavoro attorno ai modelli: deploy, playground, agenti, RAG.
•  GitHub Copilot porta gli stessi modelli nell'editor, sotto la governance del tuo tenant.
•  Gli agenti aggiungono il loop ragiona→strumento→risponde.
•  Tutto poggia su ciò che già sappiamo: resource group, identità, RBAC, costi.
“All'evento (Build //localhost Torino) vedrete Foundry e Copilot costruire applicazioni AI: ora sapete cosa c'è sotto.”

---

## Sessione 8: Lezione 16


### Slide 1
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
Storage, Data & Integration: database gestiti, Cosmos DB e Data Integration (4 ore)
### Slide 2
Dal database al flusso del dato
Database gestiti, Cosmos DB e integrazione dati: dove nasce il dato e dove deve arrivare
### Slide 3
Argomenti (4 ore)
•  Perché un database gestito (PaaS) e cosa cambia nel modello operativo
•  Relazionali gestiti: Azure SQL (single/MI), PostgreSQL/MySQL Flexible
•  Continuità del servizio: backup, replica, HA, RPO/RTO
•  Cosmos DB: partizionamento, throughput, consistency levels
•  Quando relazionale e quando NoSQL distribuito
•  Il dato non vive da solo: integrazione con Data Factory
•  Pipeline, trigger, orchestrazione e cenni su Synapse
### Slide 4
Perché scegliere un database gestito
•  Un database gestito riduce il lavoro su patching, backup e manutenzione di base.
•  Il team si concentra più sul dato e meno sul server del database.
•  Non elimina le scelte architetturali: sposta il livello del lavoro.
•  Alta disponibilità, backup e monitoraggio entrano più facilmente nel servizio.
•  È uno dei vantaggi più evidenti del cloud PaaS.
### Slide 5
Database relazionali gestiti
•  Azure SQL Database — il database relazionale come servizio (single database).
•  Managed Instance — più vicino allo SQL Server tradizionale (migrazioni lift-and-shift).
•  PostgreSQL e MySQL Flexible Server — motori open source gestiti.
•  La scelta dipende da compatibilità applicativa, controllo richiesto e percorso di migrazione.
•  Il tema non è solo il motore: è il modello operativo.
### Slide 6
Continuità del servizio
•  In un database gestito il tema non è solo scrivere query, ma tenere vivo il servizio.
•  Backup automatici, replica e opzioni HA riducono i rischi operativi.
•  La continuità cambia da servizio a servizio.
•  Va sempre letta insieme a RPO (quanto dato posso perdere) e RTO (in quanto torno su) e ai costi.
•  Il cloud aiuta, ma non sostituisce il ragionamento progettuale.
### Slide 7
Cosmos DB: idea base
•  Cosmos DB è il servizio NoSQL distribuito di Azure.
•  Supporta più API e modelli di accesso (SQL/Core, MongoDB, Cassandra…).
•  Si usa quando servono scala elevata, bassa latenza e distribuzione globale.
•  Non è un sostituto automatico di ogni database relazionale.
### Slide 8
Cosmos DB: i tre concetti chiave
•  Partizionamento — la partition key distribuisce i dati: una buona chiave = scala uniforme.
•  Throughput — capacità misurata in RU/s (Request Units), provisioned o serverless.
•  Consistency levels — dal più forte al più disponibile: Strong, Bounded staleness, Session, Consistent prefix, Eventual.
•  Sono leve di costo/prestazioni/coerenza: si scelgono in base al requisito, non a caso.
### Slide 9
Relazionale o NoSQL
Quando tende a servire
schema stabile, query strutturate, transazioni forti
NoSQL distribuito
scala ampia, flessibilità, accesso globale e veloce
•  La scelta non è di moda, ma di requisito.
•  Il modello dati influenza sviluppo, costo e integrazione futura.
### Slide 10
Il dato non vive mai da solo
•  I database entrano in flussi con applicazioni, code, ETL e analytics.
•  Per questo il tema non è solo il motore, ma anche l'integrazione.
•  Un database operativo e una piattaforma analytics hanno scopi diversi.
•  Il progetto vero inizia quando i dati devono muoversi tra servizi diversi.
“Da qui in poi passiamo dal "dove sta il dato" al "come si muove il dato".”
### Slide 11
Perché serve integrazione dati
•  I dati arrivano da applicazioni, file, database, API e sistemi esterni.
•  Il problema non è solo salvarli, ma spostarli e coordinarli bene.
•  L'integrazione evita passaggi manuali fragili e poco tracciabili.
•  Nel cloud questo significa pipeline, trigger e orchestrazione.
•  Qui inizia il livello più sistemico del dato.
### Slide 12
Data Factory: idea base
•  Azure Data Factory serve a costruire pipeline di integrazione.
•  Coordina attività tra sorgenti e destinazioni diverse.
•  Concetti base: pipeline, activity, linked service, dataset.
•  Non è un database, ma un motore di orchestrazione del flusso.
•  Il valore è nel movimento controllato del dato.
### Slide 13

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 9: Lezione 17


### Slide 1
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
Security, Reliability e Business Continuity - PT1: Defender for Cloud e Key Vault (4 ore)
### Slide 2
Vedere il rischio e proteggere i segreti
Defender for Cloud per la postura, Key Vault per chiavi e credenziali
### Slide 3
Argomenti (4 ore)
•  Defender for Cloud: posture management, workload protection, recommendations
•  Priorità del rischio: cosa guardare prima (esposizione, identity, patching)
•  Guest Configuration e vulnerability assessment come controllo continuo
•  Ridurre la superficie esposta: WAF, segmentazione, log ed evidenze
•  Key Vault: centralizzare segreti, chiavi e certificati
•  Accesso applicativo con Managed Identity e permessi minimi
•  Rotazione, scadenza, HSM e fiducia tra servizi (TLS/mTLS)
### Slide 4
Perché partire da Defender for Cloud
•  La sicurezza cloud non si legge solo dal firewall o da una singola VM.
•  Serve una vista trasversale su configurazioni, rischi e priorità operative.
•  Defender for Cloud legge lo stato di sicurezza di subscription e risorse.
•  Il valore: vedere i problemi ricorrenti prima che diventino incidente.
•  La sicurezza diventa controllo continuo, non verifica occasionale.
### Slide 5
Posture management e workload protection
Posture management
configurazioni, policy, esposizioni e hardening
Workload protection
minacce, vulnerabilità e segnali operativi
•  Il primo livello misura quanto l'ambiente è impostato bene.
•  Il secondo guarda cosa sta succedendo ai workload reali.
•  Le due letture servono insieme, non una al posto dell'altra.
### Slide 6
Recommendations e priorità
•  Le recommendations mostrano configurazioni deboli o mancanti.
•  Non tutte pesano uguale: alcune riducono il rischio molto più di altre.
•  Leggere prima: esposizione pubblica, identity, patching, crittografia.
•  Il punto non è chiudere ticket, ma abbassare il rischio reale.
•  Serve sempre un ordine di priorità, non una lista piatta.
### Slide 7
Guest Configuration e vulnerability assessment
•  Guest Configuration verifica che le VM rispettino le impostazioni attese.
•  Il vulnerability assessment evidenzia software e componenti deboli.
•  Servono a ridurre deriva configurativa e superfici note.
•  La sicurezza del workload non finisce al bordo della subnet.
•  Anche dentro la macchina vanno letti stato e conformità tecnica.
### Slide 8
Ridurre la superficie e raccogliere evidenze
•  Meno porte aperte e meno endpoint pubblici = meno rischio.
•  WAF, segmentazione e regole mirate filtrano il traffico utile.
•  Principio guida: esporre solo ciò che serve davvero.
•  Activity Log e log diagnostici raccontano cosa è successo e dove.
•  Senza evidenze un incidente resta un sospetto: la sicurezza è anche lettura dei segnali.
### Slide 9
Dal vedere il rischio al proteggere i segreti
•  Defender ci dice dove siamo esposti; ora vediamo come custodire ciò che è sensibile.
•  Una delle esposizioni più comuni: credenziali e chiavi sparse nel codice o nei file.
•  Il passo naturale è centralizzarle in un servizio dedicato: Azure Key Vault.
“Stesso obiettivo (ridurre il rischio), ma ora a livello di segreti e crittografia.”
### Slide 10
Perché centralizzare segreti e chiavi
•  Segreti e chiavi sparsi nel codice o nei config aumentano il rischio.
•  Un servizio centrale rende chiari controllo accessi, rotazione e audit.
•  Azure Key Vault nasce per togliere le credenziali dai punti sbagliati.
•  L'obiettivo non è solo custodire il valore, ma governarne il ciclo di vita.
### Slide 11
Segreti, chiavi e certificati
password, connection string, token
crittografia, firma, protezione dati
TLS, identità del servizio, trust
•  Hanno tutti valore sensibile, ma scopi diversi.
•  Separarli bene aiuta a scegliere permessi e processo corretti.
### Slide 12
Come un'app accede al vault
•  Il modello migliore su Azure è spesso la Managed Identity.
•  Così l'app non porta con sé credenziali da salvare altrove.
•  I permessi devono essere minimi e mirati all'oggetto richiesto.
•  L'accesso degli amministratori va separato da quello applicativo.
•  Un vault sicuro dipende tanto dal permesso quanto dal contenuto.

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 10: Lezione 18


### Slide 1
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
Security, Reliability e Business Continuity - PT2: Backup, Disaster Recovery e Compliance (4 ore)
### Slide 2
Backup, Disaster Recovery e Compliance
Far sopravvivere dato e servizio a un guasto, e saperlo dimostrare
### Slide 3
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
### Slide 4
Il backup non è solo una copia
•  Fare backup non significa automaticamente poter ripartire bene.
•  Conta cosa proteggi, con quale frequenza e quanto velocemente recuperi.
•  Backup e continuità del servizio vanno letti insieme.
•  Se non sai cosa vuoi recuperare prima, la policy resta astratta.
•  Il punto è progettare il recupero, non solo salvare dati.
### Slide 5
La logica 3-2-1 nel cloud
•  La regola 3-2-1: più copie, su supporti/livelli diversi, con una separazione reale.
•  Nel cloud la separazione non è solo fisica: può essere logica, operativa, di accesso.
•  Serve a ridurre il rischio di perdita unica o compromissione comune.
•  Va adattata al workload, non applicata come slogan.
### Slide 6
Retention operativa e storica
recupero veloce dopo errore o incidente comune
conservazione lunga per audit, analisi o obblighi
•  Le due retention non coincidono quasi mai.
•  Confonderle porta a costi inutili o recuperi insufficienti.
### Slide 7
Recovery Services Vault e separazione
•  Il Recovery Services Vault è il contenitore Azure per backup e punti di ripristino.
•  Tiene insieme policy di backup, retention e gli elementi protetti.
•  Vault separation: non tutto deve stare nello stesso contenitore operativo.
•  Separare ambienti/workload riduce il blast radius di errori o compromissioni.
•  Anche i permessi diventano più leggibili e meno pericolosi.
### Slide 8
Restore test e runbook
•  Un backup non testato è solo una promessa.
•  I restore test verificano tempi, dipendenze e integrità del recupero.
•  I runbook evitano di improvvisare durante un incidente.
•  Quando il ripristino coinvolge più servizi, la procedura conta quanto il dato.
•  Qui si vede la differenza tra protezione dichiarata e protezione reale.
### Slide 9
Dal backup alla continuità: HA vs DR
•  Alta disponibilità (HA) e Disaster Recovery (DR) non sono la stessa cosa.
•  HA: riduce interruzioni locali o limitate (un nodo, un guasto circoscritto).
•  DR: prepara il servizio a eventi gravi e meno frequenti (perdita di una region).
•  Se i due piani si confondono, anche il design resta ambiguo.
•  Distinguere continuità locale da recupero su scala ampia.
### Slide 10
Availability Set, Zone e Region
Availability Set
separazione da fault e update domain (stesso datacenter)
Availability Zone
distribuzione su zone distinte nella stessa region
separazione geografica per eventi più ampi
•  Ogni livello aumenta resilienza, ma anche costo e complessità.
•  La scelta dipende da rischio atteso e criticità del servizio.
### Slide 11
•  RPO (Recovery Point Objective): quanta perdita di dati puoi tollerare.
•  RTO (Recovery Time Objective): in quanto tempo devi tornare operativo.
•  Sono i due numeri guida per decidere architettura e investimento.
•  Senza questi riferimenti, parlare di DR (Disaster Recovery) resta troppo vago.
•  Prima si definisce il requisito, poi si sceglie la tecnologia.
### Slide 12
Azure Site Recovery
•  Azure Site Recovery (ASR) supporta replica e failover controllato.
•  Porta i workload verso un sito secondario o una region alternativa.
•  Non basta attivarlo: va allineato a dipendenze applicative e dati.

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 11: Parte 1


### Slide 1
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
Architettura e strumenti di accesso - Parte 1 (4 ore)
### Slide 2
Architettura e strumenti di accesso
Corso Cloud Specialist - ITS ICT
•  Tenant, subscription e piano gratuito
•  Risorse, wizard di creazione, resource group
•  Regioni e zone di disponibilità
•  Azure Resource Manager (ARM)
•  Portale e Azure CLI
•  Marketplace, tipi di risorse, IaaS/PaaS/SaaS
### Slide 3
Tenant, Subscription e piano gratuito
Nel nostro caso
L'organizzazione su Azure
ITS ICT Piemonte
Fatturazione e limiti
Azure for Students
Contenitore logico
Il servizio (VM, DB...)
Azure for Students
•  100 $ di credito e accesso a servizi gratuiti
•  Alcuni gratuiti per 12 mesi (VM, storage, database)
•  Altri always free con rinnovo mensile (App Service, Functions)
•  Controllate i costi nella sezione "Cost Management"
### Slide 4
Come trovare tenant e subscription
•  Apriamo portal.azure.com
•  In alto a destra, icona utente → "Switch directory": ecco il nostro tenant (ITS ICT Piemonte)
•  Nella barra di ricerca cerchiamo "Subscriptions"
•  Troviamo Azure for Students: notiamo nome, ID, stato
•  Clicchiamo sulla subscription per vedere credito residuo e limiti
•  Cerchiamo "Free services" per vedere la lista dei servizi gratuiti inclusi
### Slide 5
Risorse e UI uniforme
In Azure tutto è una risorsa: VM, database, storage, rete, resource group.
La UI del portale è sempre la stessa per ogni tipo di risorsa:
Basics (nome, regione, RG) → Tab (default OK) → Review + Create
Sezione dedicata o "All resources"
Click sulla risorsa → Overview, Settings, ...
Pulsante Delete nella barra superiore
### Slide 6
Il resource group è la risorsa più semplice ma anche la più fondamentale.
•  Contenitore logico che raggruppa risorse correlate
•  Ogni risorsa deve stare in esattamente un resource group
•  Ha un nome e una regione (dove Azure salva i metadati)
•  Le risorse al suo interno possono stare in regioni diverse
Convenzione di nome
rg-progetto-ambiente
rg-progetto-dev
Cancellare un resource group = cancellare tutto ciò che contiene.
### Slide 7
Come creare un Resource Group
•  Cerchiamo "Resource groups" nella barra di ricerca del portale
•  Clicchiamo "+ Create"
•  Basics: subscription, nome rg-demo, regione Italy North
•  Notiamo i tab del wizard: Tags, poi Review + create - lo stesso pattern di sempre
•  Clicchiamo "Review + create" → controlliamo il riepilogo → "Create"
•  Apriamo il resource group: Overview (vuoto), Activity Log, Tags
•  Notiamo come la UI è identica a quella di qualsiasi altra risorsa
### Slide 8
Una regione è un'area geografica con uno o più data center.
Oltre 60 nel mondo
Italy North (Milano)
Vicinanza, conformità, costi
•  Recommended: la maggior parte dei servizi, zone di disponibilità (es. Italy North)
•  Alternate: gamma più limitata, per esigenze specifiche
### Slide 9
Zone di disponibilità (Availability Zones)
Data center fisicamente separati dentro una stessa regione.
Zone disponibili
Con AZ (es. Italy North)
•  Creando 3 VM in zone diverse si ottiene ridondanza
•  Nel wizard VM: "Availability options" per scegliere la zona
### Slide 10
Come esplorare regioni e zone nel wizard
•  Iniziamo a creare una Virtual Machine (non la completiamo)

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 12: Parte 2


### Slide 1
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
Architettura e strumenti di accesso - Parte 2 (4 ore)
### Slide 2
Architettura e strumenti di accesso - Parte 2
Corso Cloud Specialist - ITS ICT
•  Paired regions e edge locations
•  Modello di responsabilità condivisa e SLA
•  Best practice di separazione (resource group)
•  ARM: scope e idempotenza
•  Cloud Shell e Azure PowerShell
•  Blueprint vs template
•  Panoramica servizi core e PaaS
### Slide 3
Ogni regione Azure ha una regione associata (paired) nello stesso continente.
West Europe (Paesi Bassi)
North Europe (Irlanda)
France Central (Parigi)
France South (Marsiglia)
•  Italy North (Milano) non ha una paired region locale
•  Disaster recovery: se una regione cade, la paired prende il carico
•  Aggiornamenti sequenziali: Azure aggiorna una regione alla volta
### Slide 4
Punti di presenza vicini agli utenti finali, fuori dai data center principali.
Cache di contenuti statici vicino all'utente
Azure Front Door
Routing globale, accelerazione, WAF
Azure Edge Zones
Compute a bassa latenza in prossimità
•  Bassa latenza: gaming, streaming, IoT
•  Distribuzione globale: immagini, video, file statici
### Slide 5
Modello di responsabilità condivisa
Chi gestisce cosa dipende dal modello di servizio scelto.
Infrastruttura fisica
•  Da IaaS a SaaS: la responsabilità si sposta verso il provider
•  Sempre tua: dati, account, identità, dispositivi
### Slide 6
SLA e disponibilità
Lo SLA (Service Level Agreement) è la garanzia di uptime di un servizio.
Esempio servizio
App Service, SQL Database
VM singola (Premium SSD)
VM in Availability Zones
Come si calcola lo SLA composto?
•  Due servizi in sequenza: SLA1 x SLA2 (es. 99.9% x 99.9% = 99.8%)
•  Per aumentare lo SLA: ridondanza, zone, paired regions
•  Nessun SLA per i servizi del tier gratuito
### Slide 7
Best practice: separazione dei Resource Group
Non mettere tutto in un unico RG. Separare per scopo e ciclo di vita.
rg-app-dev, rg-app-prod
Per applicazione
rg-webapp, rg-api, rg-database
Per ciclo di vita
Risorse temporanee in un RG a parte
•  Risorse che si creano e cancellano insieme nello stesso RG
•  Ambienti diversi in RG diversi (mai dev e prod insieme)
•  I permessi (RBAC) si assegnano a livello di RG
### Slide 8
ARM: scope e idempotenza
Ogni operazione ARM avviene a un livello (scope) preciso:
Management Group
Raggruppa subscription
Fatturazione e limiti
Contenitore logico di risorse
Il singolo servizio (VM, DB, ...)
Idempotenza: stesso template eseguito 2 volte = stesso risultato. Se la risorsa esiste, ARM la aggiorna (non la duplica). Template come fonte di verità (IaC).
### Slide 9
Terminale nel browser, integrato nel portale Azure (icona >_).
Dal portale, zero installazione
Bash o PowerShell
Azure CLI, PowerShell, Git, Terraform
File persistenti su File Share (5 GB)
•  Non vuoi installare nulla sul tuo PC
•  Sei su un PC non tuo (laboratorio, aula)
### Slide 10
Azure PowerShell

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 13: Parte 1


### Slide 1
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
Identity e Governance - Parte 1 (2 ore)
### Slide 2
Identity e Governance
Come Azure gestisce chi sei, cosa puoi fare e quali regole valgono
### Slide 3
Argomenti di oggi
•  Microsoft Entra ID: cos'è, il tenant, il dominio .onmicrosoft.com
•  Utenti e gruppi: interni vs esterni, creazione, associazione
•  App Registration: identità per le applicazioni
•  Azure Policy: assegnazioni e restrizioni (es. region consentite)
•  RBAC: cos'è, ruoli, scope, assegnazioni
•  IAM nel portale: Check Access, Add Role Assignment
•  MFA: perché è obbligatorio
Nelle prossime lezioni approfondiremo ogni tema e ne aggiungeremo altri.
### Slide 4
Microsoft Entra ID (ex Azure AD)
Microsoft Entra ID è il servizio di identità e accesso di Azure. Gestisce:
•  Chi sei: utenti, gruppi, applicazioni
•  Come ti autentichi: password, MFA, Authenticator
•  Cosa puoi fare: ruoli, permessi, policy
Ogni organizzazione Azure ha almeno un tenant Entra ID: è il "contenitore" di tutte le identità.
“Pensatelo come l'elenco telefonico dell'organizzazione: contiene tutti gli utenti, i gruppi e le app registrate.”
### Slide 5
Il tenant e il dominio .onmicrosoft.com
Quando un'organizzazione crea un tenant Entra ID, riceve un dominio di default:
nomeorganizzazione.onmicrosoft.com
•  È l'indirizzo univoco del tenant su Azure
•  Nel vostro caso: itsictpiemonte.onmicrosoft.com
•  Il vostro account istituzionale è collegato a quel tenant
Con la sottoscrizione per studenti, l'accesso a Entra ID è bloccato, ma il tenant esiste. La sottoscrizione normale permette di gestire utenti, gruppi e app.
### Slide 6
Utenti: interni ed esterni
In Entra ID ci sono due tipi di utenti:
Member (interno)
Guest (esterno)
Appartiene all'organizzazione
Invitato da fuori
Nel tenant (es. mario.rossi@...onmicrosoft.com)
Il suo esistente (Gmail, altro tenant)
Completo (in base ai permessi)
Limitato a ciò che gli è condiviso
Quando crei un utente, puoi assegnargli subito uno o più gruppi esistenti.
### Slide 7
I gruppi servono a organizzare gli utenti e semplificare la gestione dei permessi.
•  Crei un gruppo (es. "Team Sviluppo", "Docenti", "Studenti Anno 1")
•  Associ uno o più utenti al gruppo
•  Assegni i permessi al gruppo invece che ai singoli utenti
Vantaggio: se entra un nuovo membro nel team, lo aggiungi al gruppo e ha subito tutti i permessi necessari. Non devi configurare nulla risorsa per risorsa.
“È lo stesso principio dei gruppi di Active Directory in azienda, ma su cloud.”
### Slide 8
App Registration: identità per le applicazioni
Anche le applicazioni hanno bisogno di un'identità per interagire con Azure.
App Registration crea un'identità nel tenant Entra ID. Esempio: Terraform.
•  Si registra come app nel tenant
•  Riceve credenziali (client ID + secret) per autenticarsi
•  Gli si assegnano i permessi necessari (es. creare VM, gestire rete)
Stessa cosa per: pipeline CI/CD, script di automazione, applicazioni web.
“In Enterprise Applications trovi le app già registrate e i relativi permessi.”
### Slide 9
Azure Policy impone regole sull'intera sottoscrizione (o su un ambito più ristretto).
Quello che abbiamo visto: Authoring > Assignments > Allowed resource deployment regions - solo 5 region consentite. Se crei una VM in una region non in lista, Azure la blocca.
Le policy servono a:
•  Impedire errori: nessuno crea risorse dove non dovrebbe
•  Garantire conformità: regole aziendali applicate automaticamente
•  Controllare i costi: es. limitare i tipi di VM consentiti
“La policy non è un permesso: è una regola imposta dall'alto che vale per tutti, indipendentemente dal ruolo.”
### Slide 10
RBAC: Role-Based Access Control
RBAC è il modello con cui Azure gestisce i permessi. Tre domande:
•  Chi? - un utente, un gruppo, un'app (il principal)
•  Cosa può fare? - un insieme di azioni (il ruolo)
•  Dove? - a quale livello si applica (lo scope)
Esempio: "Mario (chi) ha il ruolo Contributor (cosa) sul Resource Group Lab-01 (dove)."
Lo scope è gerarchico (i permessi si ereditano dall'alto verso il basso):
Management Group > Subscription > Resource Group > Resource
Reader sulla Subscription = Reader su tutti i Resource Group e risorse al suo interno.

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 14: Parte 2


### Slide 1
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
Identity e Governance - Parte 2 (4 ore)
### Slide 2
Identity e Governance - Parte 2
Conditional Access, Identity Protection, PIM e governance pratica
### Slide 3
Argomenti di oggi
•  Conditional Access: regole di accesso basate su utente, rischio e dispositivo
•  Identity Protection: segnali di rischio e protezione degli account
•  PIM: ruoli privilegiati attivi solo quando servono
•  Management Groups: organizzare più subscription in modo coerente
•  Azure Policy e iniziative: applicare regole di conformità in modo centralizzato
•  Naming, tagging e locks: governance pratica delle risorse
•  B2B ed External ID: identità esterne per partner e applicazioni
### Slide 4
Conditional Access
Conditional Access è il motore Zero Trust di Microsoft Entra. Funziona con regole if-then:
“Se un utente vuole accedere a una risorsa, allora deve soddisfare una condizione.”
Esempio: "Se un utente accede da fuori rete aziendale, allora deve fare MFA."
Le policy si creano in Entra ID > Conditional Access > Policies e si applicano dopo l'autenticazione iniziale (primo fattore).
Richiedono licenza Entra ID P1 (inclusa in Microsoft 365 Business Premium).
### Slide 5
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
### Slide 6
Identity Protection
Identity Protection rileva automaticamente comportamenti sospetti sugli accessi:
•  Login da IP anonimi (es. VPN/Tor)
•  Password spray: tentativi di indovinare password su molti account
•  Credenziali compromesse: trovate in database di leak
•  Viaggio impossibile: login da Roma e da Tokyo a 5 minuti di distanza
Genera tre report: risky users, risky sign-ins, risk detections.
Può integrarsi con Conditional Access: se il rischio è alto, blocca l'accesso o forza il cambio password. Richiede licenza Entra ID P2.
### Slide 7
PIM: Privileged Identity Management
PIM elimina i permessi privilegiati permanenti. Principio: nessuno dovrebbe essere Owner o Global Admin 24/7.
•  L'admin assegna un ruolo come eligible (idoneo), non active
•  Quando serve, l'utente attiva il ruolo dal portale PIM
•  L'attivazione richiede: MFA, una giustificazione, eventuale approvazione
•  Il ruolo resta attivo per un tempo limitato (es. 8 ore), poi scade
“È il principio del just-in-time access: i permessi esistono solo quando servono.”
Richiede licenza Entra ID P2 o Entra ID Governance.
### Slide 8
Management Groups
I Management Groups sono il livello sopra le subscription:
Management Group > Subscription > Resource Group > Resource
Servono per applicare in modo coerente policy e RBAC a più sottoscrizioni insieme.
•  Ogni directory ha un Root Management Group
•  Le assegnazioni fatte a un MG si ereditano verso il basso
•  Sono utili per separare ambienti, business unit o aree geografiche
“Esempio: il MG "Europa" può imporre policy comuni a tutte le subscription europee.”
### Slide 9
Azure Policy e iniziative
Azure Policy controlla se le risorse rispettano regole organizzative.
•  Esempi: consentire solo regioni approvate, imporre tag obbligatori, vietare SKU non autorizzate
•  Effetti tipici: audit, deny, append, deployIfNotExists
•  Si assegna a Management Group, subscription o Resource Group
Iniziativa = raccolta di più policy gestite come un unico set.
•  Utile per standard di sicurezza, compliance o cost management
•  Rende più semplice applicare e tracciare regole comuni
“I Management Groups danno la gerarchia, Azure Policy applica le regole.”
### Slide 10
Governance pratica: naming, tagging e locks
Naming convention
Dare nomi coerenti e leggibili alle risorse
Aggiungere metadati come Environment, Owner, CostCenter
Proteggere da modifiche o cancellazioni accidentali
•  I tag aiutano costi e filtri, ma non si ereditano automaticamente
•  I lock nel portale sono Delete e Read-only; in CLI/API sono CanNotDelete e ReadOnly

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 15: Parte 1


### Slide 1
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
Reti su Azure - Parte 1 (2 ore)
### Slide 2
Reti su Azure - Parte 1
VNet, subnet, NSG e accesso RDP come caso guida
### Slide 3
•  Perche' la rete conta in Azure
•  VNet e Subnet: i blocchi base
•  NSG: regole allow/deny sul traffico
•  RDP su una VM Windows: cosa deve esserci per collegarsi
•  Caso guida: relazione tra regola TCP 3389 e accesso alla VM
•  Segmentazione, troubleshooting e casi piu' realistici
### Slide 4
Dove siamo nel percorso
•  Dopo identita', permessi e governance, passiamo al livello rete
•  La rete decide chi raggiunge cosa e su quale porta
•  Qui iniziamo dalla parte piu' concreta: una VM gia' esistente e il suo NSG
•  Una VM gia' esistente con il suo NSG e' un buon caso iniziale per leggere l'effetto delle regole
### Slide 5
I pezzi minimi della rete in Azure
La rete privata nel cloud
Una porzione della VNet
La scheda di rete della VM
L'indirizzo pubblico per accesso da Internet
Le regole che permettono o bloccano traffico
•  Per il caso RDP bastano soprattutto VM + Public IP + NSG
### Slide 6
•  Una VNet e' la tua rete privata in Azure
•  Una Subnet divide la rete in zone piu' piccole
•  Le subnet servono per separare carichi di lavoro e applicare regole diverse
•  Piu' avanti useremo questa logica per distinguere frontend, backend e management
### Slide 7
NSG: concetti chiave
•  Un Network Security Group contiene regole Allow o Deny
•  Le regole valgono su traffico inbound o outbound
•  Un NSG si puo' associare a una subnet o a una NIC
•  Le regole hanno una priority: numero piu' basso = precedenza piu' alta
•  Le regole di default esistono gia', ma le regole custom possono prevalere
### Slide 8
RDP: condizioni minime di accesso
•  Una VM Windows accesa
•  Un Public IP sulla VM, se il collegamento e' diretto da Internet
•  Una regola inbound TCP 3389 che consenta il traffico verso la VM
•  Credenziali valide della macchina virtuale
“Se la porta 3389 non e' consentita, la connessione RDP non parte.”
### Slide 9
Dove lo vedi nel portale
•  Apri la Virtual machine
•  Nel menu vai su Networking > Network settings
•  Controlla se c'e' una regola che consente TCP 3389
•  Apri il Network security group associato
•  In Inbound security rules leggi, modifichi o elimini la regola
### Slide 10
Caso guida: RDP e regola 3389
•  Se esiste una regola inbound TCP 3389 che consente il traffico, la VM puo' accettare nuove connessioni RDP
•  Se la regola manca oppure viene negata, la connessione RDP fallisce
•  L'esito dipende anche da priority, source, protocol e scope
•  Il punto non e' memorizzare clic, ma leggere il legame tra regola di rete e accessibilita' della VM
La rete non e' sfondo: decide concretamente se un accesso e' possibile oppure no.
### Slide 11
Attenzione: cosa osservare davvero
•  Gli NSG sono stateful: una sessione gia' aperta puo' restare attiva
•  Se togli la regola, di solito falliscono le nuove connessioni RDP
•  La stessa porta puo' avere esiti diversi in base a priority, source e scope
•  Una regola con source My IP e' piu' sicura di una con source Any
### Slide 12
Sviluppi del tema
•  Subnet e segmentazione della rete
•  Differenza tra NSG su subnet e su NIC
•  Effective security rules e verifica del risultato finale
•  Altri casi: HTTP, HTTPS, regole troppo larghe, regole troppo strette
Il punto chiave e' che una regola di rete cambia davvero il comportamento della VM.

---

## Sessione 16: Parte 2


### Slide 1
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
Reti su Azure - Parte 2 (3 ore)
### Slide 2
Reti su Azure - Parte 2
NSG su subnet e NIC, effective rules, HTTP/HTTPS e troubleshooting
### Slide 3
•  Ripresa dei concetti chiave della Parte 1
•  Differenza tra NSG su subnet e NSG su NIC
•  Effective security rules: dove leggere il risultato finale
•  Casi tipici: HTTP e HTTPS su una VM
•  Metodo di troubleshooting quando un accesso non funziona
•  Verifica dal portale e da Cloud Shell
### Slide 4
Ripartenza dalla Parte 1
•  Nella prima parte abbiamo visto VNet, subnet, NSG e caso RDP 3389
•  Il punto chiave era semplice: una regola di rete cambia davvero il comportamento della VM
•  Ora facciamo un passo in piu': capire dove applicare la regola e come leggere l'effetto complessivo
•  Non basta vedere un NSG nel portale: bisogna capire se e' quello che decide davvero il traffico
### Slide 5
Subnet e NIC: due livelli diversi
Quando e' utile
Un insieme di risorse nella stessa porzione di rete
Per regole comuni a piu' VM
Una singola interfaccia di rete
Per eccezioni o casi specifici
•  Azure permette di usare NSG su entrambi i livelli
•  Il punto non e' aggiungere regole ovunque, ma capire quale livello ha senso usare
### Slide 6
Quando ha senso lavorare sulla subnet
•  Quando piu' VM dello stesso livello applicativo devono seguire le stesse regole
•  Quando vuoi separare bene frontend, backend e zone amministrative
•  Quando vuoi una vista piu' ordinata della segmentazione
•  Quando la regola descrive il comportamento atteso di tutta una porzione di rete
La subnet e' il posto naturale per la policy comune.
### Slide 7
Quando ha senso lavorare sulla NIC
•  Quando una singola VM ha bisogno di un'eccezione temporanea o mirata
•  Quando vuoi differenziare una macchina senza cambiare tutta la subnet
•  Quando stai facendo verifica o isolamento di un nodo specifico
•  Se usi troppe eccezioni a livello NIC, pero', la lettura della rete diventa meno chiara
Una regola sulla NIC e' potente, ma va usata con criterio.
### Slide 8
Cosa conta davvero nel risultato finale
•  Il traffico reale dipende dalla combinazione delle regole visibili sulla subnet e sulla NIC
•  Guardare una sola regola spesso porta a conclusioni sbagliate
•  Se un livello blocca il traffico necessario, l'accesso fallisce anche se altrove vedi un allow
•  Per questo Azure offre una vista di sintesi: le effective security rules
Il problema non e' trovare una regola, ma capire l'effetto finale.
### Slide 9
Effective security rules
•  Sono la vista che aiuta a leggere il comportamento effettivo della VM
•  Riassumono regole default e regole custom che incidono sul traffico
•  Sono utili quando una VM non risponde e vuoi evitare di controllare oggetti a caso
•  Non sostituiscono il ragionamento, ma evitano errori di lettura del contesto
Se devi capire perche' una VM non e' raggiungibile, questa e' una verifica centrale.
### Slide 10
Caso tipico: pubblicare HTTP
Per raggiungere una pagina web su una VM servono almeno questi elementi:
•  Una Public IP associata al percorso corretto
•  Una regola inbound TCP 80 coerente con il livello scelto
•  Un servizio nella VM che ascolta davvero sulla porta 80
•  Nessun blocco effettivo che annulli quel traffico
La rete da sola non basta: deve esserci anche qualcosa che risponde dentro la VM.
### Slide 11
Caso tipico: pubblicare HTTPS
•  Dal punto di vista della rete, HTTPS significa soprattutto porta 443
•  Il certificato non risolve una regola mancante: se 443 non passa, il servizio resta irraggiungibile
•  In alcuni casi si lascia aperta anche la 80 per reindirizzare verso 443
•  In altri casi si espone solo 443 per ridurre la superficie visibile
La regola di rete decide il passaggio, il servizio applicativo decide la risposta corretta.
### Slide 12
Regole troppo larghe e regole troppo strette
Source = Any su porta sensibile
Espone troppo la VM
Priority non ragionata
Una regola inattesa puo' prevalere
Apertura su subnet intera senza motivo

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 17: Parte 3


### Slide 1
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
Reti su Azure - Parte 3 (4 ore)
### Slide 2
Reti su Azure - Parte 3
Routing, peering, pubblicazione e accessi
### Slide 3
Cosa chiudiamo oggi
•  completiamo il quadro rispetto alla Parte 2 con routing, peering e accessi più strutturati
•  colleghiamo ogni esigenza al servizio giusto: cambiare percorso, collegare reti, pubblicare, tenere privato, amministrare
•  distinguiamo i ruoli principali dei servizi di rete Azure
•  l'obiettivo è leggere una topologia e scegliere il servizio adatto
### Slide 4
La rete in tre domande
•  Dove sta la risorsa? In una Virtual network, dentro una Subnet
•  Ha un indirizzo solo interno o anche pubblico? Qui entra il Public IP address
•  Chi può raggiungerla? Lo decidono le regole del Network Security Group
•  Se devo ragionare su gruppi di VM, uso un Application Security Group
•  Il senso è semplice: posizione, indirizzo, regole
### Slide 5
Se il traffico deve cambiare strada
•  Una regola può dire "puoi passare", ma serve anche sapere dove vai
•  In Azure la risorsa si chiama Route table
•  Dentro ci metti le route personalizzate, cioè le UDR
•  Esempio: una subnet deve uscire solo passando da Azure Firewall
•  Quindi: NSG decide se passi, Route table decide il percorso
### Slide 6
Se devo collegare due reti Azure
•  Il nome da ricordare è VNet peering
•  Serve quando due Virtual network devono parlarsi direttamente
•  Non stai pubblicando su Internet
•  Non stai ancora collegando una sede esterna: stai collegando Azure con Azure
•  Domanda pratica: devo unire due reti cloud o portare dentro una rete da fuori?
### Slide 7
Collegare una sede o una persona
•  Se invece la rete arriva da fuori Azure, entra in gioco Virtual network gateway
•  Site-to-Site: collega Azure a una sede o a un data center
•  Point-to-Site: collega un singolo computer ad Azure
•  Local network gateway serve a descrivere la rete esterna
•  Qui chiudiamo l'idea di accessi più strutturati: peering tra reti Azure, gateway verso l'esterno
### Slide 8
Quando la rete cresce
•  ExpressRoute collega Azure a reti aziendali con una connessione dedicata
•  Azure Virtual WAN organizza connettività tra sedi, utenti remoti e reti cloud
•  entrano in gioco quando aumentano sedi, percorsi e punti di accesso
•  completano il quadro della connettività ibrida e multi-sede
### Slide 9
Pubblicare un servizio
distribuire traffico tra VM
Azure Load Balancer
pubblicare un sito o una web app
Azure Application Gateway
•  Load Balancer ragiona da rete
•  Application Gateway ragiona da applicazione web
•  Esempio: due VM dietro Load Balancer, portale studenti con Application Gateway
### Slide 10
Se gli utenti sono distribuiti
•  Azure Front Door gestisce ingressi globali vicini agli utenti
•  lavora bene quando il traffico arriva da aree geografiche diverse
•  Load Balancer e Application Gateway coprono invece ingressi regionali o applicativi
•  la scelta dipende da dove stanno gli utenti e da come entra il traffico
### Slide 11
I nomi contano quanto gli IP
•  Se il nome punta male, sembra che la rete non funzioni
•  distinguiamo DNS zones pubbliche e Private DNS zones
•  quando usi servizi privati, anche il DNS entra nella soluzione
•  risoluzione dei nomi e indirizzi IP lavorano insieme
### Slide 12
Portare un servizio dentro la rete
•  la domanda pratica è: il servizio resta pubblico o entra davvero nella rete?
•  Private Endpoint porta il servizio dentro la rete privata
•  Service Endpoints mantengono il servizio pubblico, ma ne limitano l'accesso alla rete autorizzata
•  qui distinguiamo accesso privato e servizio pubblico filtrato
### Slide 13
Proteggere i servizi esposti
•  un Network Security Group regola il traffico su subnet e schede di rete
•  Azure Firewall filtra il traffico in modo centralizzato
•  Azure DDoS Protection difende i servizi pubblici da attacchi volumetrici

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 18: Lezione 9


### Slide 1
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
Compute su Azure: VM, immagini e dimensionamento (4 ore)
### Slide 2
Compute su Azure
Virtual Machine, immagini e dimensionamento
### Slide 3
Da dove ripartiamo
•  abbiamo già letto una VM dal lato rete: NIC, Public IP, NSG, RDP
•  abbiamo già aperto il wizard di creazione fino a Review + create
•  oggi cambiamo domanda: non solo chi raggiunge la VM, ma quale VM stiamo scegliendo
•  il punto è leggere le scelte di compute prima ancora di creare
### Slide 4
La VM come risorsa compute
•  una Virtual Machine è compute IaaS
•  scegli tu sistema operativo, dimensione, immagine e dischi
•  Azure ti fornisce infrastruttura fisica, rete, regioni e opzioni di disponibilità
•  rispetto a App Service o Functions hai più controllo, ma anche più gestione
### Slide 5
Le scelte che pesano subito
dove gira la VM
il punto di partenza del sistema
vCPU e RAM disponibili
prestazioni e costo di base
continuità del servizio
•  la rete la conosciamo già: qui la rileggiamo come contesto della VM
### Slide 6
Come leggere il nome di una size
serie economica, 2 vCPU
uso generale, 2 vCPU, generazione v5
stessa taglia, ma più orientata alla memoria
•  la serie indica la famiglia della VM
•  il numero dà l'ordine di grandezza
•  s indica supporto a Premium SSD
### Slide 7
Famiglie da ricordare
Quando la guardo
carichi leggeri o intermittenti
applicazioni che chiedono più RAM
più CPU rispetto alla memoria
•  non serve imparare tutto il catalogo
•  servono pochi riferimenti per non scegliere a caso
### Slide 8
vCPU e RAM: la domanda giusta
•  se il collo di bottiglia è l'elaborazione, guardo prima le vCPU
•  se l'app tiene molto in memoria, guardo prima la RAM
•  non esiste la VM migliore in assoluto
•  la scelta giusta dipende dal carico, non dal nome più grande
### Slide 9
Immagine, OS disk e data disk
•  l'immagine è il modello iniziale della VM
•  decide sistema operativo e software di partenza
•  il OS disk nasce dall'immagine
•  i data disk si aggiungono dopo, per dati e applicazioni
### Slide 10
Da dove arrivano le immagini
•  il Marketplace raccoglie immagini Microsoft e di terze parti
•  esempi tipici: Windows Server, Ubuntu, immagini con software già presente
•  un'immagine pronta accelera la partenza
•  più l'immagine è ricca, più va capita bene prima di usarla
### Slide 11
Regione, vincoli e scelta reale
•  la regione non si sceglie solo per abitudine
•  contano policy, disponibilità del servizio e vicinanza
•  con sottoscrizioni limitate conviene verificare prima opzioni davvero disponibili
•  nel wizard la prima lettura utile è: Region, Image, Size
### Slide 12
Availability Set e Availability Zone
proteggermi dal guasto di host o rack
Availability Set
separazione fisica tra data center nella stessa regione
Availability Zone
•  la zona è una separazione fisica più forte
•  non tutte le regioni offrono le zone
•  una VM singola resta una VM singola: la continuità cresce con più istanze
### Slide 13
La VM che abbiamo già
•  in Overview leggo nome, resource group, regione e stato

*[Contenuto troncato — vedi file originale per dettagli completi]*


---
*Totale: 18 sessioni generate il 02/07/2026*