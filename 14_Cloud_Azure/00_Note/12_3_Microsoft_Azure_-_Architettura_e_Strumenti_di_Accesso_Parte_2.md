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
