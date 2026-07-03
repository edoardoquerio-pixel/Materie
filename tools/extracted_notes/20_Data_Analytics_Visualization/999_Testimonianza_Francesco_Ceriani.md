# Testimonianza Francesco Ceriani

Fonte: `Testimonianza Francesco Ceriani.pdf`

Testimonianaza Aziendale

Guest: Francesco Ceriani

30/04/2026

Intro

Retail landscape

Data sources and architecture

Value chain, from raw data to decision

- Intro -

My personal journey

Laurea in Ingegneria Informatica

Marketing Analyst

CRM Analysis Manager

Private Data Strategy Consultant

Head of Data

Case study

Oggi vedremo un caso reale di un luxury fashion retailer globale per capire, dal punto di vista della data governance, che la qualità del dato 

non è affatto scontata. I dati non sono “buoni” per definizione: diventano affidabili solo grazie a processi strutturati, regole chiare e 

responsabilità definite. Attraverso questo caso analizzeremo come i dati nascono, come vengono gestiti e perché solo dati di qualità 

permettono di prendere decisioni di business solide in un contesto competitivo come quello del luxury.

- Retail landscape -

38

12

Stores

Countries

8

Currencies

10

Languages

Pipelines a diversi fusi 
orari, diverse regole 
fiscali, vincoli legali sui 
dati (GDPR)

Tassi cambio variano 
ogni giorno. Come fare 
report globale? E trend 
anno su anno?

Diversi idiomi, caratteri 
speciali, tassonomia 
globale

3

Till systems

Diverse strutture 
scontrini, ambiguita 
codici cliente/prodotti..

«La scalabilità di un sistema è la capacità di ampliarne le dimensioni senza aumentare la complessità»

Sales

• Transaction/receipt ID
• Date & time
• Store ID
• Till / POS ID
• Cashier ID
• Line items:

• product ID / SKU
• Quantity
• unit price
• discount applied
• Total amount. taxes

Website

• Utenti unici
• Sorgenti di traffico (eg
social media, paid ad, 
search engine)
• Durata sessione
• Velocità di caricamento
• Device
• Tasso di conversion

- Data sources and architecture -

HR

• Staff ID
• Name
• Store/Department
• Start Date
• End Date
• Discount

Marketing

• CRM interactions
• Events
• Sale associate ID
• Interaction date/time
• Channel (in store, 

Whtsapp, clientelling
app, email, sms..)

• Interaction type (follow 

up, invitation, 
campaign promotion..)

Products

• Gestione inventario
• Product ID
• Colour
• Size
• Category
• Stock availability

3rd party

• Età stimata
• Presenza di figli
• Livello istruzione
• Professione
• Fascia di reddito
• Valore immobiliare

della’rea di residenza

• Capacità di spesa
• …

- Value chain, from raw data to decision -

Creazione del 
dato

ETL 
(Export, Transform, Load)

Visualization

Analysis

Decision

• Dati incompleti o mal 

formattati

• Errori inserimento

manuale

• Standard diversi tra sistemi
• Misparsing (eg indirizzo)

Il dato nasce sporco per 
natura: è il processo che 
deve renderlo affidabile

• Pipelines automation
• Normalizzazione
• Deduplicazione
• Arricchimento
• Data quality rules
• Creation of a cured data 

layer 

Qui si forgia la qualità del 
dato

• Interactive dashboard e 

report

• KPI standardizzati
• Storytelling
• Monitoraggio qualità dati
• Single source of truth

• Pattern e trend detection
• Segmentazioni
• Analisi predittive
• Test e simulazioni
• Return of investment

Qui il dato diventa semantica

Qui si risponde a specifiche 
domande di business 

(AWS, Azure, Databricks)

(PowerBI, Tableau, Looker..)

(Python, SQL, Excel) 

Data engineer

Data engineer

Data Analyst

Data Scientist
Data Analyst

• Decisioni strategiche
• Ottimizzazione processi
• Prioritizzazine investimenti

Good decisions don’t start 
from dashboards, but from 
clean and governed data

Management

- QA -