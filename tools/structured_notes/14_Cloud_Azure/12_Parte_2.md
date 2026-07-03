# Parte 2

## Panoramica
Architettura e strumenti di accesso - Parte 2 (4 ore)

## Argomenti trattati
Azure, Cloud, Data Analytics, Database, Installazione

---
## Appunti

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
*Fonte: 003_3_Microsoft_Azure_-_Architettura_e_Strumenti_di_Accesso_Parte_2_.md*
