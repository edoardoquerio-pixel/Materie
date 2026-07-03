# Lezione 13

## Panoramica
Storage, Data & Integration - PT1: Storage account, servizi dati, sicurezza e accesso storage (4 ore)

## Argomenti trattati
Azure, Sicurezza, Data Analytics, API REST, Reti

---
## Appunti

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
*Fonte: 013_13_Microsoft_Azure_-_Storage_Data_Integration_-_Storage_e_Sicurezza.md*
