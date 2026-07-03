# Data Analytics & Visualization — Appunti Strutturati per Sessione

> **Corso:** ITS ICT Cloud Specialist 2025-2027  
> **Materia:** 20_Data_Analytics_Visualization

---

## Indice delle Sessioni

1. [Analisi Esplorativa](#analisi-esplorativa)
2. [Data Cleaning e Power Query](#data-cleaning-e-power-query)
3. [Dashboard Design](#dashboard-design)
4. [Visualizzazione e Storytelling](#visualizzazione-e-storytelling)
5. [Regressione e ML](#regressione-e-ml)
6. [Excel e Grafici](#excel-e-grafici)
7. [Regex e Google Colab](#regex-e-google-colab)
8. [Testimonianza](#testimonianza)

---

## Analisi Esplorativa

### Materiali

- [`02_Analisi_esplorativa.md`](00_Note/02_Analisi_esplorativa.md)
- [`15_Teoria_della_visualizzazione.md`](00_Note/15_Teoria_della_visualizzazione.md)

### Contenuti

Analisi Esplorativa dei Dati (EDA)
con Microsoft Excel
Dataset: immobiliare.xlsx

---

Prima di analizzare, esplorare
Perché fare EDA?
"In God we trust. All others must bring data."  — W. E. Deming
Capire la struttura
Quante righe? Che tipi di variabili? Dati mancanti?
Trovare i problemi
Outlier, errori di inserimento, distribuzioni anomale
Generare ipotesi
Quali variabili sembrano correlate? Cosa

*[Contenuto troncato — vedi file completo]*

---

Teoria della Visualizzazione e Grammar of Graphics

---

Teoria della Visualizzazione
e Grammar of Graphics
Perché i grafici comunicano meglio delle tabelle · Come scegliere il grafico giusto · Principi di design visivo · Accessibilità
Esempi tratti da: Our World in Data, The Economist, NYT Graphics

---

Perché i grafici? Il limite delle tabelle
Dati grezzi — cosa noti?
Stesso dato — trend immed

*[Contenuto troncato — vedi file completo]*

---


## Data Cleaning e Power Query

### Materiali

- [`13_Pulizia_dei_dati_in_Excel_1.md`](00_Note/13_Pulizia_dei_dati_in_Excel_1.md)
- [`11_PowerQuery_v3.md`](00_Note/11_PowerQuery_v3.md)
- [`05_Esercizio_di_Data_cleaning.md`](00_Note/05_Esercizio_di_Data_cleaning.md)
- [`04_Data_Set_per_esercizio_Power_Query.md`](00_Note/04_Data_Set_per_esercizio_Power_Query.md)

### Contenuti

Pulizia dei dati in Excel
da ”I dieci metodi principali per la pulizia dei dati” su support.microsoft.com

---

Informazioni di base
Importare i dati da un'origine dati esterna.
Creare una copia di backup dei dati originali in una cartella di lavoro separata.
Verificare che i dati nelle righe e nelle colonne siano in formato tabulare con:
dati simili in ogni colonna,
tutte le colonne e le righe vi

*[Contenuto troncato — vedi file completo]*

---

Variabili
Ogni variabile deve formare una colonna distinta nel dataset.
Osservazioni
Ogni singola osservazione deve formare una riga dedicata.
Valori
Ogni tipo di unità osservazionale deve formare una tabella.
Tidy data: Le 3 Regole d'Oro

---

Tidy data: Le 3 Regole d'Oro – Regola 3
Esempio: Valori
❌  Messy
✅  Tidy
Studenti
Corsi
Iscrizioni
→
Ogni tipo di unità osservazionale (studenti, corsi, is

*[Contenuto troncato — vedi file completo]*

---

## Sheet: Originale

Nome e Cognome | Email | Indirizzo | Numero di cellulare | Con quante altre persone parteciperai? | Data di conferma
Debora Nizzola | debora_nizzola@gmail.com | C.so Enrico Gamba 36, Bolzano, RM | 3389962593 | 2 | 2023-10-21 12:16:40 PM
Silvio Contardi | scontardi8@gmail.com | C/da Calatubo 161, Alcamo, VE | 3932245433 | 2 | 2023-10-24 07:27:10 PM
Monica Limongi | monica_limon

*[Contenuto troncato — vedi file completo]*

---

## Sheet: Sporco

ID Ordine | Nome e Cognome | Prodotto | Quantità | Prezzo unitario (€) | Stato | Data ordine
ORD-1042 | ALICE moretti | Penna stilografica | 8 | 24.5 | Annullato | 2024-02-02
ORD-1035 |   ALICE LOMBARDI | Penna stilografica | 9 | 24.5 | Consegnato | 2024-05-22
ORD-1075 | DAVIDE GALLO | Graffette | 6 | 1.5 | Consegnato | 2024-02-09
ORD-1059 | Andrea Bianchi | Penna stilografica | 

*[Contenuto troncato — vedi file completo]*

---


## Dashboard Design

### Materiali

- [`03_Dashboard_design.md`](00_Note/03_Dashboard_design.md)

### Contenuti

Visualization to Inform: Dashboard Design

---

Dashboard vs Report — Scopo e Audience
DASHBOARD
Monitoraggio in tempo reale o quasi-reale
Decisioni operative immediate
Audience: manager, executive
Lettura in 5–30 secondi
Aggiornamento automatico e continuo
KPI al centro, dati aggregati
REPORT
Analisi storica e documentazione
Decisioni strategiche e audit
Audience: analisti, stakeholder, revisori


*[Contenuto troncato — vedi file completo]*

---


## Visualizzazione e Storytelling

### Materiali

- [`18_Visualizzazione_e_storytelling.md`](00_Note/18_Visualizzazione_e_storytelling.md)
- [`17_Visualizzazione_con_Seaborn.md`](00_Note/17_Visualizzazione_con_Seaborn.md)
- [`19_Visualizzazione_per_Big_Data.md`](00_Note/19_Visualizzazione_per_Big_Data.md)

### Contenuti

Visualizzazione per convincere: Storytelling

---

Dashboard vs Storia: perché non basta mostrare i dati
 La dashboard risponde a domande
Mostra tutto simultaneamente
L'utente esplora liberamente
Nessuna direzione imposta
Utile per monitorare, non per convincere
 La storia guida verso una conclusione
Seleziona e ordina le informazioni
Ha un protagonista e un punto di arrivo
Elimina il rumore visiv

*[Contenuto troncato — vedi file completo]*

---

Introduzione a Seaborn

---

Introduzione a Seaborn
Visualizzazione dati in Python per l'analisi esplorativa e la modellazione
Dataset: tips (seaborn built-in)

---

Agenda della lezione
1
Seaborn vs Matplotlib
Quando usare cosa
2
Formato Tidy
La struttura dati che Seaborn si aspetta
3
Temi e stili
set_theme, palette, contesto
4
I tre plot universali
relplot · displot · catplot
5
Small multiples &

*[Contenuto troncato — vedi file completo]*

---

Visualizzazione e Big Data

---

Visualizzazione e Big Data
Problemi di visualizzazione nei Big Data e soluzioni
Data Analytics e Visualization  |  Modulo 3.5
Dataset: bigdata_viz_datasets.xlsx  (5 fogli, ~58.000 righe)

---

1. Quando la scala diventa un problema
Quanti punti riesce a distinguere il nostro occhio in un grafico?  Circa 300–500. Cosa succede con 50.000?
Overplotting
Migliaia di pun

*[Contenuto troncato — vedi file completo]*

---


## Regressione e ML

### Materiali

- [`14_Regressione_logistica.md`](00_Note/14_Regressione_logistica.md)
- [`10_L4_-_Regressione_lineare.md`](00_Note/10_L4_-_Regressione_lineare.md)
- [`01_Alberi_di_decisione.md`](00_Note/01_Alberi_di_decisione.md)

### Contenuti

Regressione
Logistica
Prevedere un risultato Sì / No
Dataset: prestiti.xlsx

---

Classificazione: quando l'output non è un numero
Finora abbiamo sempre previsto un valore numerico continuo.
Output
Esempio
Regressione lineare
Numero continuo
Prezzo di un appartamento: €245.000
Regressione logaritmica
Numero continuo
Prezzo al mq dato l'anno: €3.200
Regressione logistica
Sì / No  (0 o 1)
Il prestit

*[Contenuto troncato — vedi file completo]*

---

Regressione
Lineare e Multipla
Dalla retta semplice al modello con più variabili
Dataset: immobiliare.xlsx

---

Cos'è la regressione lineare
Domanda: esiste una relazione tra superficie e prezzo?
L'idea di fondo
Cerchiamo una retta y = a + b·x che descriva al meglio la relazione tra due variabili numeriche.

La retta non passa per tutti i punti — minimizza la distanza da ciascuno.
Cosa sono x e y

*[Contenuto troncato — vedi file completo]*

---

Albero di
Decisione
Classificare con una sequenza di domande Sì / No
Dataset: prestiti.xlsx

---

Come funziona un albero di decisione
Un albero pone una serie di domande sui dati per arrivare a una classificazione
debiti_totali > 30.000?
reddito > 40.000?
età > 50?
No
Sì
✅ Approvato
Sì
❌ Rifiutato
No
✅ Approvato
Sì
❌ Rifiutato
No
Nodo radice
Nodo interno
Foglie

---

Concetti chiave dell'albero d

*[Contenuto troncato — vedi file completo]*

---


## Excel e Grafici

### Materiali

- [`08_Grafici_in_Excel.md`](00_Note/08_Grafici_in_Excel.md)
- [`15_Teoria_della_visualizzazione.md`](00_Note/15_Teoria_della_visualizzazione.md)
- [`17_Visualizzazione_con_Seaborn.md`](00_Note/17_Visualizzazione_con_Seaborn.md)
- [`18_Visualizzazione_e_storytelling.md`](00_Note/18_Visualizzazione_e_storytelling.md)
- [`19_Visualizzazione_per_Big_Data.md`](00_Note/19_Visualizzazione_per_Big_Data.md)
- [`20_Visualizzazione.md`](00_Note/20_Visualizzazione.md)
- [`12_Prestiti_-_Regressione_Logaritmica.md`](00_Note/12_Prestiti_-_Regressione_Logaritmica.md)

### Contenuti

## Sheet: Ricchezza e vita 2017

Country | Life expectancy at birth | GDP per capita | Population
Qatar | 80.72 | 154669 | 2711764
Norway | 82.62 | 84056 | 5277396
United Arab Emirates | 79.5 | 76644 | 9068297
Singapore | 83.22 | 67331 | 5764489
Kuwait | 79.78 | 66010 | 4124904
Ireland | 81.92 | 60544 | 4771860
Switzerland | 83.41 | 60171 | 8451688
Luxembourg | 81.73 | 56780 | 596290
United States

*[Contenuto troncato — vedi file completo]*

---

Teoria della Visualizzazione e Grammar of Graphics

---

Teoria della Visualizzazione
e Grammar of Graphics
Perché i grafici comunicano meglio delle tabelle · Come scegliere il grafico giusto · Principi di design visivo · Accessibilità
Esempi tratti da: Our World in Data, The Economist, NYT Graphics

---

Perché i grafici? Il limite delle tabelle
Dati grezzi — cosa noti?
Stesso dato — trend immed

*[Contenuto troncato — vedi file completo]*

---

Introduzione a Seaborn

---

Introduzione a Seaborn
Visualizzazione dati in Python per l'analisi esplorativa e la modellazione
Dataset: tips (seaborn built-in)

---

Agenda della lezione
1
Seaborn vs Matplotlib
Quando usare cosa
2
Formato Tidy
La struttura dati che Seaborn si aspetta
3
Temi e stili
set_theme, palette, contesto
4
I tre plot universali
relplot · displot · catplot
5
Small multiples &

*[Contenuto troncato — vedi file completo]*

---

Visualizzazione per convincere: Storytelling

---

Dashboard vs Storia: perché non basta mostrare i dati
 La dashboard risponde a domande
Mostra tutto simultaneamente
L'utente esplora liberamente
Nessuna direzione imposta
Utile per monitorare, non per convincere
 La storia guida verso una conclusione
Seleziona e ordina le informazioni
Ha un protagonista e un punto di arrivo
Elimina il rumore visiv

*[Contenuto troncato — vedi file completo]*

---

Visualizzazione e Big Data

---

Visualizzazione e Big Data
Problemi di visualizzazione nei Big Data e soluzioni
Data Analytics e Visualization  |  Modulo 3.5
Dataset: bigdata_viz_datasets.xlsx  (5 fogli, ~58.000 righe)

---

1. Quando la scala diventa un problema
Quanti punti riesce a distinguere il nostro occhio in un grafico?  Circa 300–500. Cosa succede con 50.000?
Overplotting
Migliaia di pun

*[Contenuto troncato — vedi file completo]*

---

## Sheet: Dati_Grezzi

EmployeeID | Age | Gender | Department | JobRole | MonthlyIncome | OverTime | YearsAtCompany | YearsWithCurrManager | JobSatisfaction | EnvironmentSatisfaction | WorkLifeBalance | Attrition | AttritionNum
1001 | 23 | Female | Human Resources | Human Resources | 5526 | Yes | 17 | 1 | 4 | 1 | 1 | Yes | 1
1002 | 23 | Male | Sales | Manager | 6821 | No | 17 | 6 | 2 | 4 | 3 | No 

*[Contenuto troncato — vedi file completo]*

---

## Sheet: Dati

id | eta | reddito_annuo | debiti_totali | prestito_approvato
1 | 38 | 56110 | 44909 | No
2 | 33 | 48219 | 43659 | No
3 | 36 | 42559 | 8533 | Sì
4 | 35 | 56621 | 1964 | Sì
5 | 65 | 92000 | 58000 | No
6 | 27 | 52399 | 54156 | No
7 | 49 | 36285 | 52020 | No
8 | 44 | 48674 | 31901 | No
9 | 57 | 91942 | 28152 | Sì
10 | 49 | 59125 | 42942 | Sì
11 | 60 | 52457 | 45280 | No
12 | 61 | 1900

*[Contenuto troncato — vedi file completo]*

---


## Regex e Google Colab

### Materiali

- [`06_Espressioni_regolari_-_esercizio.md`](00_Note/06_Espressioni_regolari_-_esercizio.md)
- [`07_Google_Colab.md`](00_Note/07_Google_Colab.md)

### Contenuti

Espressioni Regolari & TDD(Test-Driven Development)
Scrivi i test prima. Poi scrivi la regex.

---

Cos'è il Test-Driven Development?
Il ciclo TDD
🔴  RED
Scrivi un test che fallisce

🟢  GREEN
Scrivi il codice minimo per farlo passare

🔵  REFACTOR
Migliora il codice senza rompere i test
RED
Fai fallire
il test
GREEN
Fai passare
il test
REFACTOR
Migliorare
la soluzione
Perché usarlo con le regex?U

*[Contenuto troncato — vedi file completo]*

---

Google Colab
Scrivere ed eseguire Python nel browser, senza installare nulla
colab.research.google.com

---

Cos'è Google Colab
Un ambiente di sviluppo Python gratuito che gira nel browser
🌐  Browser-based
Non installi nulla sul tuo computer. Funziona su qualsiasi PC, Mac o Chromebook con Chrome o Firefox.
☁️  Salvataggio su Drive
I notebook si salvano automaticamente su Google Drive. Puoi condivi

*[Contenuto troncato — vedi file completo]*

---


## Testimonianza

### Materiali

- [`16_Testimonianza_Francesco_Ceriani.md`](00_Note/16_Testimonianza_Francesco_Ceriani.md)

### Contenuti

30/04/2026
Testimonianaza Aziendale
Guest: Francesco Ceriani

Intro
Retail landscape
Data sources and architecture
Value chain, from raw data to decision


- Intro -
Laurea in Ingegneria Informatica
Marketing Analyst
CRM Analysis Manager
Private Data Strategy Consultant
Head of Data
My personal journey
Oggi vedremo un caso reale di un luxury fashion retailer globale per capire, dal punto di vista 

*[Contenuto troncato — vedi file completo]*

---


