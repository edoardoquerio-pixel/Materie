# Parte 1

## Panoramica
Architettura e strumenti di accesso - Parte 1 (4 ore)

## Argomenti trattati
Azure, Cloud, Database, Data Analytics, Reti

---
## Appunti

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
*Fonte: 002_2_Microsoft_Azure_-_Architettura_e_Strumenti_di_Accesso_Parte_1_.md*
