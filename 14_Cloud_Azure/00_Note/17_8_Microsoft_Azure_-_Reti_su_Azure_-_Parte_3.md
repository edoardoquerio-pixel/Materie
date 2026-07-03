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
