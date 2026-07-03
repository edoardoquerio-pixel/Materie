# Parte 1

Fonte: `2) Microsoft Azure - Architettura e Strumenti di Accesso (Parte 1).pptx`

### Slide 1

DOCENTE

Federico Laurianti

UNITA' FORMATIVA

Microsoft Azure (100 ore)

ARGOMENTO

Architettura e strumenti di accesso - Parte 1 (4 ore)

---

### Slide 2

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

### Slide 3

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

### Slide 4

Come trovare tenant e subscription

•  Apriamo portal.azure.com
•  In alto a destra, icona utente → "Switch directory": ecco il nostro tenant (ITS ICT Piemonte)
•  Nella barra di ricerca cerchiamo "Subscriptions"
•  Troviamo Azure for Students: notiamo nome, ID, stato
•  Clicchiamo sulla subscription per vedere credito residuo e limiti
•  Cerchiamo "Free services" per vedere la lista dei servizi gratuiti inclusi

---

### Slide 5

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

### Slide 6

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

### Slide 7

Come creare un Resource Group

•  Cerchiamo "Resource groups" nella barra di ricerca del portale
•  Clicchiamo "+ Create"
•  Basics: subscription, nome rg-demo, regione Italy North
•  Notiamo i tab del wizard: Tags, poi Review + create - lo stesso pattern di sempre
•  Clicchiamo "Review + create" → controlliamo il riepilogo → "Create"
•  Apriamo il resource group: Overview (vuoto), Activity Log, Tags
•  Notiamo come la UI è identica a quella di qualsiasi altra risorsa

---

### Slide 8

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

### Slide 9

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

### Slide 10

Come esplorare regioni e zone nel wizard

•  Iniziamo a creare una Virtual Machine (non la completiamo)
•  Nella sezione "Region", apriamo il menu a tendina: scorriamo per vedere quante regioni esistono
•  Scegliamo Italy North
•  In "Availability options" selezioniamo "Availability zone": compaiono le 3 zone
•  Proviamo a cambiare regione e notiamo come alcune non offrono zone di disponibilità
•  Guardiamo i tab del wizard: Disks, Networking, Management... tutti con default
•  Arriviamo a "Review + create": vediamo il riepilogo, poi annulliamo

---

### Slide 11

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

### Slide 12

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

### Slide 13

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

### Slide 14

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

### Slide 15

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

### Slide 16

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