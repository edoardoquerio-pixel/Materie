# Parte 3

## Panoramica
Reti su Azure - Parte 3 (4 ore)

## Argomenti trattati
Azure, Reti, Cloud, Data Analytics, API REST

---
## Appunti

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
*Fonte: 008_8_Microsoft_Azure_-_Reti_su_Azure_-_Parte_3.md*
