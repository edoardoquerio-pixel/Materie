# Cloud Specialist - BF 2025-27 - Learning by project - Progetto

Fonte: `Cloud Specialist - BF 2025-27 - Learning by project - Progetto.pdf`

DOCENTE 

Unità Formativa 

Argomento 

Luca ROBALDO 

Learning by project 

Progetto infrastruttura IT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Convergenza, integrazione e 
potenziamento servizi IT 
azienda TP Group srl 

Scenario di riferimento 

Descrizione dello scenario 

Thema Consulting 

Pro Studio srl 

Assessment 

Vincoli, requisiti ed obiettivi, budget 

Vincoli tecnologici 

Vincoli logistici 

Obiettivi per il futuro 
Budget di progetto 
Costi indicativi risorse 
Requisiti compilazione documento di offerta tecnico/economico 

Criteri di valutazione 

Versione del documento: 260603 

3 

3 

3 

3 

4 

6 

6 

6 

6 
6 
7 
8 

9 

2 

 
 
 
 
 
 
 
Scenario di riferimento 
Due aziende che operano nel campo della progettazione nel settore automotive / aerospace 
decidono di creare un’alleanza (associazione di imprese) per proporsi ad un mercato sempre più 
richiedente di soluzioni altamente tecnologiche. Dall’unione di Thema Consulting e Pro Studio 
nasce TP Group. 
Nella fase di integrazione / convergenza, sono pesantemente coinvolti tutti i sistemi informativi, 
oggetto del progetto richiesto. 

Descrizione dello scenario 
Thema Consulting srl nasce alla fine degli anni ‘90 dall’idea di tre ingegneri progettisti, attivi da un 
decennio nel settore della progettazione meccanica; si occupa prevalentemente di progettazione 
strutturale in ambito automotive. 
Pro Studio srl nasce nel 2023 come startup ed è composta da giovani ingegneri progettisti che 
lavorano in ambito aerospace. 

Thema Consulting 

● Sede di proprietà in un edificio storico situato nel centro di Torino 
● E’ dotata di un piccolo data center, efficiente, ma poco capiente: non è purtroppo possibile 

espanderlo, i due armadi rack sono saturi. 

● Conta 30 persone (tra dipendenti e collaboratori) 
● Gli uffici possono ospitare fino a 40 postazioni di lavoro 

○ La postazione di lavoro è composta da una scrivania dotata di connessione di rete 

LAN ed un monitor esterno a cui il dipendente può collegare il proprio laptop 

● Per mezzo del loro cluster di calcolo HPC (ad esclusivo utilizzo del personale interno), sono 
in grado di svolgere simulazioni (crash test) e di fornire al cliente finale un progetto 
completo di calcolo strutturale. 

● Dal 2015 erogano per una cerchia ristretta di loro clienti un servizio di ottimizzazione dei 
pesi dei materiali (Pondus), indicato per la scelta di componenti speciali in ambito 
automotive (auto sportive) ed aerospace 

Pro Studio srl 

● Sede di rappresentanza in affitto presso un condominio uffici che fornisce tutte le facilities 

necessarie (energia elettrica, riscaldamento / condizionamento e connettività) 

● Conta 20 dipendenti in Torino 
● Non possiede una infrastruttura IT interna, ma utilizza servizi in cloud 
Il calcolo strutturale è sottomesso sui sistemi dei loro clienti finali 
● 

3 

 
 
 
 
 
Assessment 

Datacenter 

Thema Consulting 

Pro Studio 

Sistemi di virtualizzazione 

Backup 

Firewall 

Cluster di calcolo 

UPS 

Condizionamento 

2 host con VMWare 
1 SAN NetApp (24 TB tot.) 
(on premise) 

Nessuno 

Salvataggi on premise su NAS 
QNAP dedicato (32 TB tot.) 

On GCP 

1 x Fortigate FG-60F 

8 nodi dedicati al calcolo HPC 
(fisici - con soluzioni hw 
proprietarie come schede 
Infiniband, on premise, Linux) 
1 Front-end (VM Linux) 

N/A 

N/A 

In grado di sopperire ad una 
interruzione di corrente 
massima di 10’ 

N/A 

Al limite per l’attuale struttura, 
difficilmente potenziabile 

N/A 

4 

 
 
 
 
 
Servizio / sistema 

Thema Consulting 

Pro Studio 

Posta / Calendario 

Zimbra (VM Linux) 

Google Workspace 

Office / Produttività 

MS365 / LibreOffice 

Google Workspace 

Videoconferenza / IM 

MS Teams 

Google Meet 

Autenticazione 

Active Directory su Samba4 
(VM Linux) 

Google authenticator 

File Server 

NextCloud (VM Linux) 

Google Drive 

Sviluppo e versioning 

GiTea 

Contabilità 

CRM 

Time Sheet 

Profis (on premise Server 
Windows) 

Sugar CRM 
(self hosted, VM Linux) 

Kimai 
(Self hosted, VM Linux) 

Bit Bucket (SaaS) 

Odoo (SaaS) 

Odoo (SaaS) 

Odoo (SaaS) 

Documentazione 

Media Wiki 
(Self hosted, VM Linux) 

Media Wiki 
(Self hosted on GCP) 

Applicazione proprietarie 

N/A 

Pondus 
Web application realizzata in 
C#, erogata da: 

● Web server (MS IIS) 
● DB server (MS SQL) 
Caratteristiche di entrambi i 
server (on premise su hw 
fisico): 1 CPU Xeon Silver 
4110, 64 GB RAM, 1,2 TB 
HDD 

● Ogni singolo dipendente ha un laptop aziendale assegnato 
● Non si richiedono soluzioni VDI per i dipendenti / collaboratori 

5 

 
 
 
 
 
 
 
 
 
 
 
 
 
Vincoli, requisiti ed obiettivi, budget 

Vincoli tecnologici 

Al fine di presentarsi ad un mercato sempre più richiedente in termini di certificazioni, il nuovo 
gruppo (TP group) ha deciso di ottemperare a quanto richiesto dalla normativa ISO/IEC 27001, 
con una particolare attenzione ai seguenti requisiti: 

● Business continuity 
○ Ridondanza 

■ dei sistemi più strategici 
■ delle connettività 

● Disaster recovery, applicato a: 

○ Delocalizzazione dei salvataggi dei dati 
○ Fruibilità dei servizi dedicati ai clienti 

● Sicurezza degli accessi ai dati 

○ Cifratura di tutti i sistemi di memorizzazione dei dati 
○ Utilizzo di applicazioni di rete che fanno uso di protocolli sicuri 
○ Accessi via VPN 

■ LAN to LAN 
■ Client To LAN 
■ Hybrid cloud 

Vincoli logistici 

Con la fusione delle due aziende non si intende rinnovare il contratto di locazione della Pro Studio: 
i dipendenti saranno trasferiti presso la sede della Thema Consulting. 

Obiettivi per il futuro 

● Potenziamento dell’applicazione Pondus e distribuzione della stessa ad un’utenza più 

ampia 

● Potenziamento del cluster di calcolo con l'incremento di altri 8 nodi entro 2 anni 

(mantenendone l’utilizzo riservato alle risorse interne) 

○ Per garantire le massime prestazioni nell’elaborazione, si sconsigliano sia la 

○ 

soluzione Virtual Machine sia la soluzione Container. 
I compute node del cluster devono essere connessi sia da una rete Ethernet, sia da 
una rete Infiniband (100 o 200 Gbps) 

○ Si predilige una soluzione con 2 processori, => 24 core, con un clock rate elevato e 

8 GB di RAM per ogni core 

○ Non servono GPU a bordo dei server di calcolo 
○ Sistema operativo richiesto: Linux 
○ Capacità richiesta per lo scratch sul singolo compute note: 1,6 TB 

Budget di progetto 

● Soluzione di calcolo On Premise/Hosting (acquisto proprietà nodi di calcolo): 580k + IVA 
● Soluzione di calcolo On-Cloud (noleggio): 525k + IVA 

6 

 
 
Costi indicativi risorse 

● Tecnico sistemista con almeno 5 anni di esperienza: €500/giorno 
● Project manager: €650/giorno 

7 

 
Requisiti 
tecnico/economico 

compilazione documento di offerta 

Si richiede da parte dell’ente proponente redazione di documento di offerta, tecnica ed economica, 
contenente i seguenti minimi requisiti: 

Indice 

● Pagina introduttiva 
● 
● Presentazione azienda (team) proponente (chi siete; principali servizi erogati; storicità) 
● 
● Assunzioni (assunzioni eventuali in ordine alla corretta erogazione delle fasi progettuali: es. 
si assume nel caso di erogazione di servizi da remoto la necessità di poter accedere ai 
sistemi aziendali mediante connessione sicura) 

Introduzione: cosa prevede la vs. offerta 

● Descrizione fornitura hardware (se presente) 
○ Descrizione materiale hw in fornitura 
○ Esclusioni 
○ Note 

● Attività richieste (attività tecnico-operative previste dal progetto) 

Installazione Hardware (es.) 
Installazione Software (es.) 

○ 
○ 
○ Test funzionali (es.) 
○ Esclusioni 
○ Note 

● Documentazione 
● Termini e condizioni (se presenti) 
● Quotazione economica 

Nice to have: 

● Gantt di progetto 
● Rasci table 

8 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Criteri di valutazione 
Per la redazione del progetto si richiede di considerare i seguenti criteri di valutazione: 

Erogazione del servizio 

Tipologie di server 

Sistema operativo 

Soluzioni scelte 

Beni del parco IT 

Gestione del parco IT 

Pricing 

● On premise (supporto manutentivo minimo 3 anni) 
● 
● Hosting co-location (contratto di hosting per minimo 3 anni) 

In cloud (minimo 3 anni) 

● Fisico 
● Virtuale 
● Container 

● MS Windows server 
● Linux server 

● Open source 
● Commerciali 

● A noleggio 
● Di proprietà 

● Con personale interno 
● 

In outsourcing 

In outsourcing 

● 
● Con personale interno 

9