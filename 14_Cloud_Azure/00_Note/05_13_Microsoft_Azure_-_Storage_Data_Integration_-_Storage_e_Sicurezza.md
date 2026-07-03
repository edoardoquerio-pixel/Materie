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
