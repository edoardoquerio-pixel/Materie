# Data Analytics & Visualization — Quaderno di Appunti

> **Materia:** 20_Data_Analytics_Visualization
> **Data generazione:** Febbraio 2026
> **Corso:** ITS ICT Cloud Specialist 2025-2027

---

## Indice delle Sessioni

1. [Alberi di decisione](#alberi-di-decisione)
2. [Analisi esplorativa](#analisi-esplorativa)
3. [Dashboard design](#dashboard-design)
4. [Data Set per esercizio Power Query](#data-set-per-esercizio-power-query)
5. [Esercizio di Data cleaning](#esercizio-di-data-cleaning)
6. [Espressioni regolari - esercizio](#espressioni-regolari---esercizio)
7. [Google Colab](#google-colab)
8. [Grafici in Excel](#grafici-in-excel)
9. [L4 - 1 immobiliare](#l4---1-immobiliare)
10. [L4 - Regressione lineare](#l4---regressione-lineare)
11. [PowerQuery v3](#powerquery-v3)
12. [Prestiti - Regressione Logaritmica](#prestiti---regressione-logaritmica)
13. [Pulizia dei dati in Excel 1](#pulizia-dei-dati-in-excel-1)
14. [Regressione logistica](#regressione-logistica)
15. [Teoria della visualizzazione](#teoria-della-visualizzazione)
16. [Testimonianza Francesco Ceriani](#testimonianza-francesco-ceriani)
17. [Visualizzazione con Seaborn](#visualizzazione-con-seaborn)
18. [Visualizzazione e storytelling](#visualizzazione-e-storytelling)
19. [Visualizzazione per Big Data](#visualizzazione-per-big-data)
20. [Visualizzazione](#visualizzazione)
21. [Voti giornata 37](#voti-giornata-37)

---

# Alberi di decisione

**File:** `Alberi di decisione.pptx`
**Tipo:** `.pptx`
**Dimensione:** 96.9 KB
**Ultima modifica:** 02/07/2026 09:24

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

Concetti chiave dell'albero di decisione
Nodo radice
La prima domanda — la variabile che divide meglio i dati. L'algoritmo la sceglie automaticamente in base all'indice di Gini o all'entropia.
Nodi interni
Ogni domanda successiva su una variabile. Ogni nodo divide i dati in due (o più) rami finché non si raggiunge una foglia.
Foglie
Il nodo terminale: contiene la classe predetta (es. Approvato / Rifiutato). Non ci sono più domande da porre.
Profondità (depth)
Numero di livelli dell'albero. Alberi profondi imparano bene i dati di training ma rischiano l'overfitting.
Overfitting
L'albero memorizza i dati di training anziché generalizzare. Si controlla limitando la profondità massima (max_depth).
Indice di Gini
Misura l'impurità di un nodo: 0 = perfettamente puro (una sola classe), 0.5 = massima mescolanza. L'algoritmo minimizza il Gini.

---

Albero di decisione vs Regressione logistica
Due approcci diversi allo stesso problema di classificazione
Albero di decisione
Regressione logistica
Output
Classe diretta (Sì/No)
Probabilità → soglia → Sì/No
Interpretabilità
Alta: si legge come flowchart
Media: coefficienti da interpretare
Relazioni
Non lineari, regole nette
Lineari nel log-odds
Overfitting
Rischio alto senza potatura
Rischio basso
Variabili categ.
Gestite nativamente
Richiedono encoding
Quando usarlo
Spiegare decisioni a non tecnici
Quando serve una probabilità calibrata

---

Esempio — classificare 5 clienti con l'albero
Regole dell'albero (semplificate):
SE debiti > 30.000  →  SE età > 50  →  Approvato  |  altrimenti Rifiutato
SE debiti ≤ 30.000  →  SE reddito > 40.000  →  Approvato  |  altrimenti Rifiutato
Cliente
Reddito
Debiti
Età
Regola applicata
Previsione
A
€65.000
€8.000
45
debiti≤30k → reddito>40k → ✅
✅ Approvato
B
€28.000
€42.000
31
debiti>30k → età≤50 → ❌
❌ Rifiutato
C
€45.000
€15.000
38
debiti≤30k → reddito>40k → ✅
✅ Approvato
D
€22.000
€5.000
55
debiti≤30k → reddito≤40k → ❌
❌ Rifiutato
E
€50.000
€48.000
55
debiti>30k → età>50 → ✅
✅ Approvato

---

Albero di decisione in Python — Google Colab
1  Carica e prepara
import pandas as pd
df = pd.read_excel('prestiti.xlsx')
X = df[['eta','reddito_annuo','debiti_totali']]
y = (df['prestito_approvato']=='Sì').astype(int)
2  Split train / test
from sklearn.model_selection import train_test_split
X_tr,X_te,y_tr,y_te = train_test_split(
  X, y, test_size=0.2, random_state=42)
3  Allena l'albero
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(
  max_depth=3, random_state=42)
model.fit(X_tr, y_tr)
4  Valuta
from sklearn.metrics import (
  accuracy_score, confusion_matrix)
print(accuracy_score(y_te, model.predict(X_te)))
print(confusion_matrix(y_te, model.predict(X_te)))
5  Visualizza l'albero
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
fig,ax = plt.subplots(figsize=(12,5))
plot_tree(model, feature_names=X.columns,
  class_names=['No','Sì'], filled=True, ax=ax)
plt.show()
6  Importanza variabili
import pandas as pd
pd.Series(
  model.feature_importances_,
  index=X.columns
).sort_values().plot.barh()
plt.title('Importanza variabili')

---

Il rischio principale — overfitting
Un albero troppo profondo impara a memoria i dati di training, ma sbaglia sui nuovi dati
max_depth = 1
Accuratezza training:
65%
Accuratezza test:
63%
Underfitting: troppo semplice. Una sola domanda non basta per separare le classi.
max_depth = 3
Accuratezza training:
84%
Accuratezza test:
82%
Bilanciato: buona generalizzazione. L'albero cattura le relazioni principali senza memorizzare.
max_depth = None
Accuratezza training:
100%
Accuratezza test:
71%
Overfitting: perfetto sul training, pessimo sul test. L'albero ha memorizzato ogni esempio.
💡  Regola pratica: inizia con max_depth=3, poi aumenta di 1 finché l'accuratezza sul test smette di migliorare.

---

Importanza delle variabili — cosa conta di più?
L'albero di decisione calcola automaticamente quanto ogni variabile contribuisce alle previsioni
debiti_totali
52%
reddito_annuo
34%
eta
14%
debiti_totali (52%) — La variabile più discriminante: livello di indebitamento è il fattore principale nella decisione.
reddito_annuo (34%) — Secondo fattore: il reddito determina la capacità di rimborso.
età (14%) — Contributo minore: l'età agisce come fattore di contesto, non determinante.

---

Esercizio  ·  prestiti.xlsx
Usa il dataset già noto: 100 clienti, 3 variabili, esito approvazione.
1
Su Colab: carica prestiti.xlsx, prepara X e y, esegui il train/test split (80/20, random_state=42)
2
Allena un DecisionTreeClassifier con max_depth=3. Qual è l'accuratezza sul test set?
3
Visualizza l'albero con plot_tree. Quale variabile è alla radice? Corrisponde a quella con importanza più alta?
4
Allena un secondo albero senza limitare la profondità. Confronta l'accuratezza su training e test. Cosa osservi?
5
Stampa la matrice di confusione per entrambi gli alberi. Quale ha meno falsi negativi?

---

Riepilogo — albero di decisione
🌳
L'albero classifica ponendo domande sequenziali sulle variabili: ogni nodo divide i dati in rami
👁️
È il classificatore più interpretabile: la logica di ogni previsione è leggibile come un diagramma di flusso
⚠️
Senza limitare la profondità (max_depth) l'albero memorizza il training set — verifica sempre l'accuratezza sul test
📊
feature_importances_ mostra quanto conta ogni variabile: utile per capire cosa guida le decisioni
Logistica: probabilità  ·  Albero: regole leggibili  ·  Entrambi: matrice di confusione per valutare


---

# Analisi esplorativa

**File:** `Analisi esplorativa.pptx`
**Tipo:** `.pptx`
**Dimensione:** 41.6 KB
**Ultima modifica:** 02/07/2026 09:24

---

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
Quali variabili sembrano correlate? Cosa vale approfondire?

---

Il dataset: immobiliare.xlsx
Useremo lo stesso dataset per tutta la sessione. Ogni blocco risponde a una domanda diversa.
Colonna
Tipo
Esempio valori
superficie_mq
numerico
85, 120, 60…
prezzo_eur
numerico
210.000, 340.000…
zona
categorico
Centro, Periferia, Semi
anno_costruzione
numerico
1965, 2005, 1988…
piano
numerico
0, 1, 2, 3…
ascensore
booleano
Sì / No

---

Statistiche descrittive
Cosa misura ogni indicatore?
Indicatore
Formula Excel
Misura
Nota
Media
=MEDIA(A:A)
Valore tipico
Sensibile agli outlier
Mediana
=MEDIANA(A:A)
Valore centrale
Robusta agli outlier
Dev. Standard
=DEV.ST(A:A)
Dispersione dei valori
Stessa unità della variabile
Quartili
=QUARTILE(A:A; 1)
Suddivisione in 4 parti
Q2 = mediana
Min / Max
=MIN()  /  =MAX()
Valori estremi
Primo segnale di outlier

---

Media vs Mediana – non è la stessa cosa
Dataset prezzi (€)
• 180.000
• 210.000
• 225.000
• 240.000
• 260.000
• 280.000
• 1.800.000 ← outlier
Media:
€ 456.429
Mediana:
€ 240.000
Cosa ci dice questo?
La media è trascinata in alto dall'appartamento a 1,8M€.

La mediana descrive meglio il caso tipico.

Con dati immobiliari (e redditi, stipendi…) la mediana è quasi sempre più informativa.

---

Tabelle pivot – lo strumento più potente di Excel
Cos'è
Una tabella dinamica che aggrega i dati secondo criteri scelti da te.
A cosa serve
Calcolare medie, conteggi, somme per gruppi. Es: prezzo medio per zona.
Come si crea
Inserisci → Tabella Pivot → scegli righe, colonne e valori.
Esempio: prezzo medio per zona
Zona
Prezzo medio €
N.
Centro
€ 385.000
47
Semi-centro
€ 240.000
63
Periferia
€ 175.000
89

---

Identificare valori anomali (outlier)
Regola 1.5×IQR
Rigoroso
Calcola Q1 e Q3.
Outlier = valori fuori da
[Q1 − 1.5·IQR,  Q3 + 1.5·IQR]
Formula / strumento:
=QUARTILE(A:A;3)−QUARTILE(A:A;1)
Box plot
Visuale
Inserisci → Grafici → Box e baffi.
I punti fuori dai baffi sono outlier.
Formula / strumento:
Grafico nativo Excel
Filtro + ordinamento
Rapido
Ordina per colonna e guarda i valori estremi manualmente.
Formula / strumento:
Dati → Ordina

---

Esercizio guidato  ·  immobiliare.xlsx
Apri il file e completa le seguenti attività:
1
Calcola media e mediana del prezzo. Sono molto diverse? Perché?
2
Crea una tabella pivot: prezzo medio per zona
3
Individua eventuali outlier sulla colonna prezzo_eur (usa il box plot)
4
Aggiungi la colonna  prezzo_al_mq = prezzo / superficie

---

Riepilogo  ·  Cosa abbiamo imparato
📊
Le statistiche descrittive danno una prima fotografia numerica del dataset
⚖️
Media ≠ Mediana: scegliere l'indicatore giusto evita conclusioni errate
🔄
Le tabelle pivot permettono di esplorare distribuzioni per categoria in pochi clic
🎯
Gli outlier vanno identificati prima di qualsiasi analisi: cambiano tutto
➡  Prossimo passo: usare questi stessi dati per costruire una regressione lineare


---

# Dashboard design

**File:** `Dashboard design.pptx`
**Tipo:** `.pptx`
**Dimensione:** 113.6 KB
**Ultima modifica:** 02/07/2026 09:24

---

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
Lettura approfondita: minuti o ore
Prodotto periodicamente (mensile, trimestrale)
Dettaglio e contesto narrativo
La dashboard risponde a «Come stiamo andando ORA?» — il report a «Perché è successo?»

---

Anatomia di una Dashboard Efficace
STRATEGICA
Executive — alto livello
3–5 KPI chiave
Trend di periodo
Semafori
ANALITICA
Manager — media granularità
Breakdown per categoria
Confronti temporali
Filtraggio interattivo
OPERATIVA
Analisti — dettaglio transazionale
Dati granulari
Drill-down
Alert e anomalie
Una dashboard non è un report: scegli il livello giusto prima di disegnare

---

Strumenti per le Dashboard — Panoramica di Mercato
Microsoft Power BI
Enterprise / Self-service
✓  Integrazione nativa con Excel e Azure
✓  DAX per calcoli avanzati
✗  Curva di apprendimento su DAX
→  Aziende Microsoft-centric, analisti business
Tableau
Enterprise / Visuale
✓  Miglior UX per la visualizzazione
✓  Calcoli visuali intuitivi
✗  Costoso (licenze per utente)
→  Analisti dati, team BI dedicati
Looker / Looker Studio
Enterprise / Free
✓  Looker Studio gratuito con Google Data
✓  Connettori Google nativi
✗  Looker enterprise molto costoso
→  Aziende Google Cloud, team tecnici
Qlik Sense
Enterprise
✓  Motore associativo: esplora senza query
✓  Potente per analisi ad hoc
✗  UI meno intuitiva di Power BI/Tableau
→  Grandi enterprise, dati molto relazionali
Grafana
Open Source / DevOps
✓  Gratuito e open source
✓  Eccellente per metriche temporali
✗  Non adatto a business analytics classico
→  Team IT, DevOps, monitoring sistemi
Microsoft Excel
Starter / Universale
✓  Già installato ovunque
✓  Sparklines e conditional formatting nativi
✗  Non scala su dati grandi (>1M righe)
→  PMI, utenti business, primo approccio
Per iniziare: Excel o Looker Studio (gratuiti) — Per crescere: Power BI o Tableau

---

Layout: Z-Pattern e Percorso di Lettura
Come leggiamo una schermata
1
KPI
Principale
2
KPI
3
KPI
5
Grafico
Principale
6
Tabella
7
Filtri
Percorso Z
Principi di Layout
Top-left = priorità massima
L'occhio parte dall'angolo in alto a sinistra. Il KPI più importante va lì.
Scansione orizzontale → diagonale → basso
Progetta seguendo questo percorso naturale: header, poi centro, poi footer.
Whitespace è contenuto
Lo spazio vuoto riduce il carico cognitivo. Non riempire ogni pixel.
Max 3 livelli di gerarchia visiva
Titolo, KPI, dettaglio. Più livelli confondono.
Design = guidare l'attenzione, non riempire lo spazio

---

Gerarchia Visiva e Whitespace
I 4 strumenti della gerarchia visiva
1. Dimensione (Size)
Numero grande → importanza alta
KPI: 48–72pt; etichette: 10–12pt
La differenza di size crea focus immediato
2. Colore (Color)
Usa il colore con intento, non decorazione
Un solo colore accent per le azioni chiave
Rosso/giallo/verde per i semafori
3. Posizione (Position)
Top > bottom, left > right in cultura occidentale
Elementi correlati vicini (legge di prossimità)
Allineamento su griglia invisibile
4. Spazio bianco (Whitespace)
Margini ≥ 16px tra elementi
Raggruppa con spazio, non solo con bordi
Meno è più: ogni elemento deve guadagnarsi il posto
Gerarchia visiva = mappa cognitiva per l'utente

---

KPI Cards — Struttura, Best Practice e Status
Anatomia di una KPI Card
① Etichetta
Attrition Rate
② Valore
16.1%
↑ +2.3pp
③ Target
Target: ≤ 10%
Best Practice
✓  Un solo numero principale per card
✓  Sempre il trend (Δ vs periodo precedente)
✓  Target o soglia espliciti
✗  Evita più di 6 KPI card per pagina
✗  Non usare il rosso per «normale»
✗  Disambigua: ↑ attrition è NEGATIVO
RAG Status — Red / Amber / Green
RED
KPI fuori soglia — azione immediata richiesta.   Es. Attrition > 15%
AMBER
KPI in zona di attenzione — monitorare.   Es. Attrition 8–15%
GREEN
KPI entro target — situazione normale.   Es. Attrition < 8%
RAG = semaforo visivo per prioritizzare l'attenzione — verde non richiede azione, rosso sì

---

Sparklines e Micro-Chart
Definizione di Edward Tufte (1983)
"A sparkline is a small, intense, simple, word-sized graphic."
Line Sparkline
Trend temporale
Andamento mensile di un KPI
Variazione nel tempo
Rilevamento di stagionalità
Column Sparkline
Comparazione periodica
Confronto mese su mese
Distribuzione per categoria
Varianza da target
Win/Loss
Esito binario
Sì/No, Sopra/Sotto soglia
Streak di performance
Anomalie binarie
Le sparkline mostrano il trend senza interrompere il flusso di lettura — ideali nelle tabelle KPI

---

Conditional Formatting nelle Dashboard
Tre pattern fondamentali
RAG Status
Attrition < 8% → verde  |  8–12% → ambra  |  > 12% → rosso
Data Bar
Lunghezza proporzionale al valore — confronto immediato senza grafico separato
Color Scale (gradiente)
Da freddo (basso) a caldo (alto) — ideale per heatmap dipartimentali
Esempio: tabella HR con CF
Dipartimento
Attrition %
Δ YoY
Status
Sales
22.4%
+4.1pp
●
HR
14.6%
+1.2pp
●
R&D
 8.3%
−0.8pp
●
Finance
 6.1%
−1.5pp
●
IT
 5.2%
−2.0pp
●
Marketing
18.9%
+3.7pp
●
Il conditional formatting trasforma una tabella in una heat map visuale — meno lettura, più percezione

---

Contesto di Business: Attrition e HR Analytics
Cos'è l'Attrition?
Attrition = tasso con cui i dipendenti lasciano l'azienda in un dato periodo, per qualsiasi motivo (dimissioni, licenziamento, pensionamento).
Formula:
Attrition Rate = Dipendenti usciti/Organico medio × 100
Benchmark di settore
< 10%
Normale / buono
10–15%
Da monitorare (AMBER)
> 15%
Critico — azione richiesta
Obiettivi di business dell'analisi HR
1
Identificare i fattori di rischio
Quali variabili (reparto, stipendio, overtime, soddisfazione) correlano con l'uscita? Permette di intervenire in anticipo.
2
Quantificare il costo dell'attrition
Sostituire un dipendente costa 50–200% del suo stipendio annuo (recruiting, onboarding, perdita di produttività).
3
Supportare decisioni HR con i dati
Passare da decisioni intuitive a decisioni basate su evidenza: quali reparti hanno priorità? Dove intervenire prima?
4
Monitorare l'efficacia degli interventi
La dashboard permette di verificare nel tempo se le azioni correttive (aumenti, flessibilità, formazione) hanno effetto.
IBM HR Analytics: 1.470 dipendenti, 35 variabili, attrition reale al 16.1% — sopra la soglia critica

---

Il Dataset: IBM HR Analytics Employee Attrition
Caratteristiche del dataset
1.470
righe (dipendenti)
35
colonne (attributi)
16.1%
tasso di attrition
0
valori mancanti
Variabili principali per la dashboard
Attrition (target: Sì/No)
Age, Gender, Department
JobRole, JobLevel
MonthlyIncome, OverTime
YearsAtCompany, YearsWithCurrManager
JobSatisfaction (1–4)
Come caricarlo in Google Colab
from google.colab import files
uploaded = files.upload()  # carica il CSV
import io
df = pd.read_csv(io.BytesIO(
  uploaded[‘HR-Employee-Attrition.csv']))

print(df.shape)      # (1470, 35)
df['Attrition'].value_counts(normalize=True)
Dataset pubblico, pulito, ricco di variabili — ideale per dashboard HR executive

---

Design Workflow: dal Dato alla Dashboard
1
Definisci l'audience
Chi la legge? Ogni quanto? Cosa decide?
2
Scegli i KPI
Max 5–7 metriche. Ogni KPI deve scatenare  un'azione.
3
Sketch su carta
Disegna a mano prima di aprire Python/Excel.
4
Prototipa con dati reali
Pandas + Excel.Verifica con l'audience.
5
Itera e misura
Time-to-insight: quanto impiega a trovare la risposta?
Errori comuni da evitare
Dashboard Spaghetti: troppi grafici, nessuna gerarchia
KPI Graveyard: metriche senza owner né azione conseguente
Chart Junk: 3D pie, effetti ombra, sfondi decorativi
Data Ink Ratio basso: più inchiostro decorativo che dati (Tufte)
Disegna prima, codifica dopo — il design parte dall'audience, non dal dataset

---

Esercizio — Executive HR Dashboard
Obiettivo: costruire una dashboard executive HR in una singola pagina Excel
1
Prepara i KPI (15 min)
Calcola: Attrition Rate totale, per Department, per Gender
Calcola: Average Monthly Income, Average Age, % Overtime workers
Aggiungi una colonna AttritionNum (1/0) per facilitare i calcoli
In Excel: usa COUNTIF/AVERAGEIF; in Python: groupby + agg
2
Costruisci i grafici (15 min)
Bar chart: Attrition % per Department (evidenzia sopra il 15%)
KPI card: Attrition Rate complessiva con colore RAG
Sparkline mensile: trend attrition ultimi 12 mesi (dati simulati)
Tabella top-5 JobRole per attrition con conditional formatting
3
Assembla la dashboard (15 min)
Disponi seguendo lo Z-pattern: KPI in alto, grafici al centro
Usa whitespace: non accostare elementi senza margine
Aggiungi titolo, data di aggiornamento, fonte dati
Test: mostra a un collega — trova il KPI critico in < 10 sec?

---

Recap — Cosa Portare a Casa
4 takeaway fondamentali
1
Dashboard ≠ Report
Scopo diverso, audience diversa, design diverso. La dashboard è per decisioni rapide e operative; il report per analisi profonde.
2
Z-pattern + gerarchia visiva
Metti i KPI più importanti in alto a sinistra. Usa size, colore, posizione e whitespace per guidare l'occhio, non decorare.
3
KPI cards, Semafori e sparklines
Ogni KPI card: valore, trend e target. RAG = semaforo visivo (verde/ambra/rosso). Le sparklines comprimono il trend in spazio minimo.
4
Design workflow: audience first
Prima definisci chi legge e cosa deve decidere. Poi scegli i KPI. Poi sketch. Poi codifica. Mai al contrario.
Dashboard = risposta rapida + design intenzionale + audience al centro


---

# Data Set per esercizio Power Query

**File:** `Data Set per esercizio Power Query.xlsx`
**Tipo:** `.xlsx`
**Dimensione:** 10.1 KB
**Ultima modifica:** 02/07/2026 09:24

---

## Sheet: Sporco

ID Ordine | Nome e Cognome | Prodotto | Quantità | Prezzo unitario (€) | Stato | Data ordine
ORD-1042 | ALICE moretti | Penna stilografica | 8 | 24.5 | Annullato | 2024-02-02
ORD-1035 |   ALICE LOMBARDI | Penna stilografica | 9 | 24.5 | Consegnato | 2024-05-22
ORD-1075 | DAVIDE GALLO | Graffette | 6 | 1.5 | Consegnato | 2024-02-09
ORD-1059 | Andrea Bianchi | Penna stilografica | 9 | 24.5 | Consegnato | 2024-05-10
ORD-1045 | MARCO GALLO | Evidenziatore | 8 | 1.8 | in transito | 2024-07-23
ORD-1058 | Marco Costa | Graffette | 5 | 1.5 | Annullato | 2024-02-05
ORD-1034 | Sara Rossi | Penna stilografica | -1 | 24.5 | Consegnato | 2024-02-02
ORD-1023 | Andrea Gallo | Agenda | 0 | 8.5 | Consegnato | 2024-12-24
ORD-1062 | Matteo De Luca | Evidenziatore | 1 | 1.8 | Consegnato | 2024-06-25
ORD-1018 | Matteo Moretti | Biro | 7 | 0.9 | in transito | 2024-04-05
ORD-1068 | Giulia Lombardi | Graffette | -7 | 1.5 | Annullato | 2024-12-05
ORD-1048 | Marco Rossi | Biro | 8 | 0.9 | Annullato | 2024-09-06
ORD-1053 | Valentina Lombardi | Post-it | 5 | 3.2 | In transito | 2024-03-22
ORD-1008 | Alice Costa | Biro | 6 | 0.9 | Annullato | 2024-04-23
ORD-1015 | ANDREA BIANCHI | Post-it | 10 | 3.2 | Annullato | 2024-06-07
ORD-1013 | Elena Gallo | Evidenziatore | 9 | 1.8 | CONSEGNATO | 2024-11-11
ORD-1020 | LUCA MANCINI | Raccoglitore | 10 | 6.9 | Consegnato | 2024-07-13
ORD-1078 | Matteo Moretti | Biro | 4 | 0.9 | IN TRANSITO | 2024-01-23
ORD-1028 |   Sara Moretti | Biro | 2 | 0.9 | Consegnato | 2024-12-16
ORD-1043 | Simone Marino | Notebook | 2 | 12.9 | Consegnato | 2024-03-14
ORD-1044 | Elena Greco | Post-it  | 7 | 3.2 | Consegnato | 2024-03-13
ORD-1033 | Giulia Lombardi | Notebook  | 10 | 12.9 | Annullato | 2024-04-19
ORD-1003 | Davide Conti | Graffette | 7 | 1.5 | Consegnato | 2024-08-19
ORD-1007 | ELENA marino | Penna stilografica | 7 | 24.5 | Consegnato | 2024-09-10
ORD-1017 | SARA gentile | Graffette | -9 | 1.5 | In transito | 2024-12-19
ORD-1032 | CHIARA greco | Graffette | 8 | 1.5 | Consegnato | 2024-04-08
ORD-1042 | ALICE moretti | Penna stilografica | 8 | 24.5 | Annullato | 2024-02-02
ORD-1055 | FRANCESCA BRUNO | Penna stilografica  | 2 | 24.5 | Annullato | 2024-04-17
ORD-1079 | Matteo Rossi | Graffette | 9 | 1.5 | Annullato | 2024-12-24
ORD-1011 | chiara lombardi | Post-it  | 5 | 3.2 | Annullato | 2024-11-21
ORD-1070 |   LUCA GENTILE | Cartelline | 7 | 4.6 | Annullato | 2024-12-26
ORD-1064 | Valentina Gallo | Graffette | 1 | 1.5 | Consegnato | 2024-02-23
ORD-1006 | giulia lombardi | Cartelline | 10 | 4.6 | In transito | 2024-01-24
ORD-1074 | Matteo Lombardi | Evidenziatore | 2 | 1.8 | In transito | 2024-06-21
ORD-1057 | LUCA greco | Graffette | 5 | 1.5 | Annullato | 2024-11-17
ORD-1047 | SARA rossi | Biro | 9 | 0.9 | Consegnato | 2024-12-11
ORD-1025 | ALICE COSTA | Graffette | 10 | 1.5 | Consegnato | 2024-03-12
ORD-1031 | paolo marino | Post-it | 5 | 3.2 | In transito | 2024-11-21
ORD-1038 | Simone Gallo | Cartelline | 7 | 4.6 | In transito | 2024-08-28
ORD-1060 | FRANCESCA CONTI | Cartelline | 4 | 4.6 | Annullato | 2024-11-28
ORD-1039 | Valentina Rossi | Penna stilografica | 1 | 24.5 | IN TRANSITO | 2024-12-11
ORD-1071 | sara ricci | Agenda | 2 | 8.5 | In transito | 2024-01-28
ORD-1029 | Alice Bianchi | Graffette | 3 | 1.5 | Consegnato | 2024-11-16
ORD-1004 | Andrea Mancini | Notebook | 3 | 12.9 | Annullato | 2024-07-11
ORD-1030 | DAVIDE FERRARI | Evidenziatore | 9 | 1.8 | Annullato | 2024-07-07

## Sheet: Desiderata

ID Ordine | Nome | Cognome | Prodotto | Quantità | Prezzo unitario (€) | Stato | Data ordine
ORD-1001 | Marco | Rossi | Notebook | 3 | 12.9 | Consegnato | 2024-03-15
ORD-1002 | Giulia | Ferrari | Post-it | 5 | 3.2 | In transito | 2024-07-22
ORD-1003 | Luca | Bianchi | Biro | 10 | 0.9 | Annullato | 2024-01-08
↑ Queste sono 3 righe di esempio. Il foglio Sporco ne contiene ~100. |  |  |  |  |  |  | 


---

# Esercizio di Data cleaning

**File:** `Esercizio di Data cleaning.xlsx`
**Tipo:** `.xlsx`
**Dimensione:** 18.4 KB
**Ultima modifica:** 02/07/2026 09:27

---

## Sheet: Originale

Nome e Cognome | Email | Indirizzo | Numero di cellulare | Con quante altre persone parteciperai? | Data di conferma
Debora Nizzola | debora_nizzola@gmail.com | C.so Enrico Gamba 36, Bolzano, RM | 3389962593 | 2 | 2023-10-21 12:16:40 PM
Silvio Contardi | scontardi8@gmail.com | C/da Calatubo 161, Alcamo, VE | 3932245433 | 2 | 2023-10-24 07:27:10 PM
Monica Limongi | monica_limongi@gmail.com | Contrada Timponelli sn, Alcamo, TO | 3662747429 | 1 | 2023-10-23 09:48:54 PM
Alice Andreotti | alice_andreotti@gmail.com | Corso Montegrappa 28, Palermo, RG  | 3286465881 | 1 | 2023-10-18 02:44:28 PM
Elda Brusca | elda_brusca@me.com | Corso Romini 63, Trescore Balneario, TO | 3357105734 |  | 2023-10-20 07:00:20 PM
vincenzo Adami | vadami4@gmail.com | Corso Trieste 63, Borgoricco, RM | 3898084425 |  | 2023-10-24 08:04:29 AM
Emanuela Longari | emanuelalongari  | Scuola dell'Infanza S. Giovanni XXIII, via Somalia 8, cap 20032, Mestre, MB | 3925839137 | 2 | 2023-10-24 10:10:02 AM
Stefania Consolandi | sconsolandi3@gmail.com | Strada Chieri 19, Torino, TO | 3394071208 | 2 | 2023-10-21 12:18:31 PM
Anna Nardelli | anardelli3@gmail.com | Strada Comunale da S. Vito a Revigliasco, 32, Torino, TO | 3381679250 | 4 | 2023-10-21 10:52:43 AM
Valter Ossola | valterossola@me.com | Strada del Lauro 39, Alcamo, PA | 3462143336 | 1 | 2023-10-22 09:07:01 PM
Tania TANEGGI | taniataneggi@gmail.com | Strada Lanzo 160/E, Bolzano, TO | 3312355307 | 3 | 2023-10-19 08:29:52 PM
Laura Ducoli | lauraducoli@virgilio.it | Strada San Vito Revigliasco 32, Palermo, TP | 3662749130 | 3 | 2023-10-23 10:43:50 PM
Helene Suarez | hsuarez7@gmail.com | Strada San Vito Revigliasco 32, Roma, TP | 3478225042 | 4 | 2023-10-23 03:47:28 PM
Debora Tasca | deboratasca@gmail.com | Via Accursio Di Leo 6, Rescaldina, RM | 3391463428 | 1 | 2023-10-21 12:18:23 PM
Luigi Coppola | luigicoppola@tiscali.it | Via Achille Grandi, Bolzano, MB | 3355938138 | 3 | 2023-10-20 12:30:51 PM
Valeria Costanzi | vcostanzi10@gmail.com | Via Allegrezza 6/1, Cassano Magnago, Cormano | 3356619708 | 1 | 2023-10-20 03:00:29 PM
CARLA Clementi | cclementi9@hotmail.it  | Via Appia 24, Alcamo, TO |  +393480413086 | 12 | 2023-10-25 10:37:56 AM
Benedetta Contardi | bcontardi3@gmail.com | Via Bernini 50, Palermo, TO | 3285648871 |  -2 | 2023-10-18 09:43:08 AM
Roberta Pettiti | robertapettiti@gmail.com | Via C. S. Garrisi 136/A, Roma | 3289336948 | 1 | 2023-10-18 09:04:53 PM
Monica Limongi | mlimongi8@gmail.com | Via Canneti 5, Aprilia, MI | 3662431990 | 1 | 2023-10-23 09:46:03 PM
Massimo Protti | massimoprotti@gmail.com | Via Cappellini 11, Milano, RM | 3358103440 | 1 | 2023-10-20 11:10:51 PM
Stefano bartolo | stefanobartolo@gmail.com | Via Colombera 16, Abbiategrasso, PD | 3406560283 | 2 | 2023-10-22 03:52:57 PM
MICAELA Catti | micaelacatti@progettomirasole.it  | Via Copernico 28, Torino, TO |  +393355638437 |  | 2023-10-25 09:22:24 AM
Cristina giussani | cristina_giussani@fgcl.it | Via Croce Sant'Amato 2, Roma, PC | 3278511373 | 15 | 2023-10-17 12:33:51 PM
Federica Soriani | federicasoriani@gmail.com | Via De Amicis 18, Carate Brianza, TO | 3403060456 |  | 2023-10-21 02:14:51 PM
Massimo Ducoli | massimo_ducoli@virgilio.it  | Via dei Larici 1/A, Palermo, BZ |  +39335457510 | 3 | 2023-10-24 09:14:39 PM
Guido CATALDI |  guidocataldi@tonarini.com | Via Delle Badesse 12, Cesena |  +393931113877 | 2 | 2023-10-25 07:05:38 PM
Lorenzo Ceccarelli |  lceccarelli8@gmail.com | Via delle Rosine 8, Nepi, LT |  | 4 | 2023-10-25 08:27:01 PM
Rosi Spagnuolo | rosispagnuolo@gmail.com | Via Delle Vignasse 26, Paderno Dugnano, MI | 3478225042 |  | 2023-10-23 03:20:53 PM
Silvio Contardi | scontardi8@gmail.com  | Via Fogazzaro 42, Alcamo, RM | 3932245433 | 2 | 2023-10-24 07:27:10 PM
Massimo Formenti | massimoformenti@tricol.it | Via Forte Marghera 151, Bari, MB | 3351211808 |  | 2023-10-20 10:26:52 AM
Simona lucenti | slucenti10@gmail.com | Via Francesco Ercole, Macerata, BG | 3405394873 | 0 | 2023-10-21 08:43:43 PM
Elisabetta Pilone | epilone8@gmail.com | Via G. Donizetti 52, Carmagnola, RM | 3406655602 | 1 | 2023-10-22 06:03:58 PM
Paolo Pettiti | paolo_pettiti@gmail.com | Via Giovanni XXIII 7, Torino, TO | 3406407664 | 1 | 2023-10-21 09:18:52 PM
Tiziana rossi |  tizianarossi@libero.it | Via Gozzi 48, Torino, VA |  |  | 2023-10-25 08:04:23 PM
Lorena calapaj | lcalapaj10@yahoo.it | Via Gregorio Speciale 4, Pecetto, TP | 3289336948 | 1 | 2023-10-19 11:22:02 AM
Marco Nurzia | marconurzia@progettoarca.org | Via Heloise 42, Roma, VA | 3490848254 | 1 | 2023-10-23 07:28:40 PM
Rossana Oggioni | rossanaoggioni@gmail.com | Via J. F. Kennedy 102, Roma, TN | 3389912020 | 1 | 2023-10-21 12:04:52 PM
Francesco Roitero | froitero6@gmail.com  | Via Macchie 8, Cormano, FC | 3929149658 | 14 | 2023-10-24 12:27:09 PM
Maria Andreata | maria_andreata@gmail.com | Via Martin Luther King 25, Bolzano Vicentino, MC | 3409313044 | 1 | 2023-10-22 08:55:40 PM
Cristina bertè | cristina_bert@hotmail.it | Via Ninni Cassara' 21, Palermo | 3381679250 |  | 2023-10-21 11:40:06 AM
Monica MORELLI | monicamorelli@libero.it  | Via P. Montana 2, VI | 3932245433 | 0 | 2023-10-24 02:18:08 PM
laura iolanda teresa Minotti | laura iolanda teresa_minotti@gmail.com | Via Piave 50/5, Alcamo, MI | 3355246315 | 4 | 2023-10-20 10:52:17 AM
Tania Pinoli | tpinoli7@gmail.com | Via Pinin Pacot 29, Alcamo, PA | 3313049364 | 1 | 2023-10-19 08:48:18 PM
franco Frisardi | franco_frisardi@yahoo.it | Via Polistena 43, Palermo, RM | 3351021597 | 2 | 2023-10-19 11:17:41 PM
Lorella Minonzio | lminonzio5@gmail.com | Via Salvotti, 41, Galliate Lombardo, PD | 3466362838 | 1 | 2023-10-23 10:36:53 AM
Marco La Torre | marco_la torre@gmail.com | Via San Vittore 47, Mori, Trento | 3483416310 | 4 | 2023-10-23 03:53:45 PM
Cristina Rivolta | cristinarivolta@gmail.com | Via Sciadonna 28, Palermo, PV | 3280158923 | 1 | 2023-10-18 09:27:58 AM
clelia LORIGLIOLA | clorigliola5@gmail.com | Via Soldato Toti 5, Torino, RM | 3334954519 | 1 | 2023-10-19 10:07:41 PM

## Sheet: Desiderata

Nome | Cognome | Email | Indirizzo | Città | Provincia | Numero di cellulare | Con quante altre persone parteciperai? | Conversion Day | Conversion Time | 
Silvio | Contardi | scontardi8@gmail.com | Via Fogazzaro 42 | Alcamo | RM | +39 393 2245 433 | 2 | 2023-10-24 00:00:00 | 19:27:00 | 

## Sheet: Da riesaminare

Nome e Cognome | Email | Indirizzo | Numero di cellulare | Con quante altre persone parteciperai? | Data di conferma


---

# Espressioni regolari - esercizio

**File:** `Espressioni regolari - esercizio.pptx`
**Tipo:** `.pptx`
**Dimensione:** 108.3 KB
**Ultima modifica:** 02/07/2026 09:24

---

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
Perché usarlo con le regex?Una regex sembra funzionare finché non incontra un caso che non avevi previsto. I test ti proteggono.

---

Il tuo compito: scrivi una regex per ciascun tipo di dato
01
CAP italiano
Es: 00100, 20121
02
Data gg/mm/aaaa
Es: 01/01/2024, 29/02/2000
03
Codice fiscale
Es: RSSMRA80A01H501U
04
Targa italiana
Es: AB123CD
05
Indirizzo email
Es: user+tag@sub.example.co.uk
06
Numero di telefono
Es: +39 333 1234567, 800 123456

---

Passo 1 — Genera 50 casi di test con un motore AI
Prompt da usare con ChatGPT / Claude / Gemini
Genera 50 casi di test per validare [TIPO DI DATO] con una regex.
Per ogni caso fornisci: valore, risultato atteso (Match / Non match), nota esplicativa.
Includi casi validi, invalidi, edge case (emoji, newline, tab, spazi, Unicode).
Formato: CSV con colonne valore,risultato,note
Casi validi (≈20)
📋
Valori corretti in tutte le varianti previste dal formato
Casi invalidi (≈20)
❌
Valori errati, troppo corti, troppo lunghi, caratteri sbagliati
Edge case (≈10)
⚠️
Emoji, \n, \t, spazi iniziali/finali, Unicode non-ASCII, sequenze ambigue

---

Passo 2 — Costruisci il file Excel di verifica
A
Valore
B
Atteso
C
Risultato
REGEX.TEST
D
Esito
Regex:  inserisci qui la tua espressione regolare  →  usata in tutta la colonna C
AB123CD
Match
=REGEX.TEST(A3,$G$1)
✅ OK
ab123cd
Non match
=REGEX.TEST(A4,$G$1)
✅ OK
AB12CD
Non match
=REGEX.TEST(A5,$G$1)
❌ Falso pos.
😀B123CD
Non match
=REGEX.TEST(A6,$G$1)
✅ OK
✅  Test superato
❌  Falso positivo / Falso negativo
⚠️  Cella di input regex
Formula in C3:  =REGEX.TEST(A3, $G$1)
La regex è in $G$1 (riferimento assoluto) — trascina la formula su tutta la colonna.

---

Cosa fare, passo dopo passo
1.  Scegli un tipo di dato
2.  Chiedi all'AI 50 casi di test, verifica che coprano tutti I casi possibili
3.  Crea il file Excel per fare i test
4.  Scrivi la regex: parti semplice, poi aggiungi complessità fino a far passare tutti i test


---

# Google Colab

**File:** `Google Colab.pptx`
**Tipo:** `.pptx`
**Dimensione:** 97.6 KB
**Ultima modifica:** 02/07/2026 09:24

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
I notebook si salvano automaticamente su Google Drive. Puoi condividerli come un documento Google.
🆓  Gratuito
GPU e CPU gratuiti forniti da Google. Sufficienti per analisi dati e machine learning di base.
📓  Notebook interattivo
Misto di codice Python eseguibile e testo formattato. Ogni cella può essere eseguita separatamente.
📦  Librerie preinstallate
pandas, numpy, sklearn, matplotlib, seaborn sono già disponibili. Nessun pip install necessario per i casi comuni.
🔗  Collegato a Google
Accede direttamente a Google Drive, Google Sheets e altri servizi Google con una sola riga di codice.

---

Anatomia di un notebook
Un notebook è composto da celle — ogni cella contiene codice o testo
▶  Cella di codice
import pandas as pd
df = pd.read_excel('prestiti.xlsx')
df.head()
Output:
   id   eta   reddito_annuo   debiti_totali   prestito_approvato
0   1    38      45000           12000              Sì
T  Cella di testo (Markdown)
## Analisi esplorativa
Questa sezione calcola le statistiche descrittive
del dataset **prestiti.xlsx**.
Interazioni principali
▶  Esegui cella
Shift + Enter
+ Cella codice
Ctrl + M  B
+ Cella testo
Ctrl + M  M
Elimina cella
Ctrl + M  D
Esegui tutto
Runtime → Esegui tutto
Interrompi
Runtime → Interrompi

---

Primo utilizzo — creare ed eseguire il primo notebook
1  Apri Colab
Vai su colab.research.google.com
Accedi con il tuo account Google
2  Nuovo notebook
File → Nuovo notebook
Appare un foglio vuoto con una cella di codice
3  Rinomina il file
Clic su 'Untitled0.ipynb' in alto
Scrivi un nome es. 'Analisi_Prestiti'
4  Scrivi il primo codice
Clic sulla cella → scrivi:
print('Ciao Colab!')
5  Esegui la cella
Premi Shift+Enter
L'output appare sotto la cella
Il numero [1] indica l'ordine di esecuzione
6  Salvataggio
Ctrl+S oppure File → Salva
Il file .ipynb è salvato su Google Drive
automaticamente ogni pochi minuti

---

Esempio — le prime righe di ogni analisi dati
Queste 4 celle sono il punto di partenza standard per qualsiasi dataset:
1  Importa le librerie
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
2  Carica il dataset
df = pd.read_excel('prestiti.xlsx')
print(df.shape)       # (100, 5)
df.head()             # prime 5 righe
3  Statistiche di base
df.describe()         # media, std, min, max
df['prestito_approvato'].value_counts()
4  Primo grafico
df.plot.scatter(x='reddito_annuo', y='debiti_totali',
  c=df['prestito_approvato'].map({'Sì':1,'No':0}),
  colormap='RdYlGn')
plt.show()

---

Shortcut — tasti utili in Colab
Imparare 8-10 shortcut rende il lavoro nel notebook molto più veloce
Windows / Linux
Mac
(sostituisci Ctrl con ⌘ Cmd)
Shift + Enter
Esegui cella e passa alla successiva
Ctrl + Enter
Esegui cella, resta sulla stessa
Alt + Enter
Esegui cella e inserisci una nuova sotto
Ctrl + M  B
Inserisci cella di codice sotto
Ctrl + M  A
Inserisci cella di codice sopra
Ctrl + M  D
Elimina cella selezionata
Ctrl + M  M
Converti cella in testo (Markdown)
Ctrl + M  Y
Converti cella in codice
Ctrl + S
Salva il notebook
Ctrl + Z
Annulla ultima modifica
Ctrl + /
Commenta/decommenta riga selezionata
Tab
Autocompleta il codice
Shift + Tab
Mostra la documentazione della funzione
Ctrl + F
Cerca nel notebook
Ctrl + M  H
Mostra tutti gli shortcut disponibili
Ctrl + M  .
Interrompi l'esecuzione

---

Gestione file — caricare dati su Colab
Colab non ha accesso al tuo PC. I file devono essere caricati esplicitamente.
A  Upload manuale (più semplice)
Dal pannello 📁 a sinistra → icona upload → seleziona il file.
Il file è disponibile finché la sessione è attiva.
import pandas as pd
df = pd.read_excel('prestiti.xlsx')
df.head()
⚠  Il file si cancella alla chiusura della sessione
B  Da codice (files.upload)
Fa apparire un pulsante di upload direttamente nell'output della cella.
from google.colab import files
uploaded = files.upload()
import io
df =pd.read_excel(io.BytesIO(uploaded['prestiti.xlsx']))
⚠  Richiede interazione manuale ogni volta
C  Da Google Drive (soluzione stabile)
Monta il Drive e accedi ai file come se fossero in una cartella locale.
from google.colab import drive
drive.mount('/content/drive')
df = pd.read_excel('/content/drive/MyDrive/prestiti.xlsx')
✅  Il file rimane disponibile tra sessioni diverse

---

Connessione a Google Drive — flusso di lavoro consigliato
Organizza i tuoi progetti con una cartella dedicata su Drive
1  Monta il Drive
from google.colab import drive
drive.mount('/content/drive')
💡  Appare un link: clicca, accedi con Google, copia il codice di autorizzazione e incollalo nella cella.
2  Naviga nella cartella
import os
os.chdir('/content/drive/MyDrive/AnalisiDati')
os.listdir()  # elenca i file nella cartella
💡  Crea su Drive una cartella  AnalisiDati  e mettici i tuoi file .xlsx prima di iniziare.
3  Carica il dataset
import pandas as pd
df = pd.read_excel('prestiti.xlsx')
print(f'{len(df)} righe caricate')
💡  Da questo punto il percorso relativo funziona direttamente. I file rimangono tra sessioni.
4  Salva i risultati
# Salva un DataFrame come Excel su Drive
df_risultati.to_excel('risultati.xlsx', index=False)
print('Salvato su Drive')
💡  Il file appare subito nella cartella Drive e può essere aperto in Excel.

---

Esercizio — primo notebook su Colab
Crea un nuovo notebook e completa i seguenti passi:
1
Vai su colab.research.google.com, crea un nuovo notebook e rinominalo con il tuo nome
2
Crea una cella di testo con un titolo ## e una breve descrizione di cosa farai
3
Carica il file prestiti.xlsx (upload manuale o da Drive) e visualizza le prime 5 righe con df.head()
4
In una nuova cella, calcola df.describe() e df['prestito_approvato'].value_counts()
5
Crea un grafico scatter: reddito_annuo sull'asse x, debiti_totali sull'asse y, colorato per esito
6
Salva il notebook su Drive e condividi il link con il docente (File → Condividi)

---

Riepilogo — Google Colab
🌐
Colab è un ambiente Python nel browser: zero installazioni, accessibile da qualsiasi computer
📓
Il notebook è fatto di celle di codice e testo — esegui ogni cella con Shift+Enter
📁
I file si caricano via upload, da codice, o montando Google Drive (soluzione più stabile)
⌨️
10 shortcut base (Shift+Enter, Ctrl+M B, Ctrl+/, Tab…) rendono il lavoro molto più veloce
colab.research.google.com  —  accedi con il tuo account Google, è gratuito


---

# Grafici in Excel

**File:** `Grafici in Excel.xlsx`
**Tipo:** `.xlsx`
**Dimensione:** 322.8 KB
**Ultima modifica:** 02/07/2026 09:11

---

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
United States | 78.82 | 54008 | 329791232
Saudi Arabia | 77.16 | 50002 | 34193120
Hong Kong | 84.9 | 49919 | 7461508
Australia | 83 | 49266 | 24590336
Netherlands | 81.73 | 46651 | 17207204
Germany | 80.94 | 45620 | 82624368
Denmark | 81.11 | 45456 | 5737286
Sweden | 82.44 | 45193 | 10058191
Canada | 82.02 | 44592 | 36554344
Taiwan | 80.13 | 43504 | 23665028
Iceland | 82.54 | 42978 | 343641
Austria | 81.64 | 42177 | 8797497
Bahrain | 79.69 | 40696 | 1456844
Belgium | 81.36 | 39352 | 11384491
Japan | 84.2 | 38415 | 126662464
Finland | 81.5 | 38367 | 5508146
France | 82.47 | 37895 | 64144092
United Kingdom | 81.17 | 37783 | 66064808
Oman | 77.92 | 37102 | 4541853
South Korea | 83.29 | 37093 | 51511640
Puerto Rico | 79.26 | 35439 | 3366407
New Zealand | 82.22 | 34876 | 4746253
Italy | 82.73 | 34027 | 60004024
Israel | 82.72 | 32339 | 8309256
Equatorial Guinea | 60.82 | 31048 | 1450703
Spain | 83.03 | 30908 | 46584168
Malta | 83.59 | 30902 | 479507
Czechia | 78.96 | 29998 | 10531315
Czechoslovakia |  | 28773 | 
Trinidad and Tobago | 74.23 | 28557 | 1478616
Slovenia | 81.07 | 28190 | 2098396
Seychelles | 73.8 | 27574 | 101828
Cyprus | 81.33 | 26445 | 1208527
Portugal | 81.5 | 26299 | 10307528
Estonia | 77.98 | 26254 | 1317550
Lithuania | 75.44 | 26157 | 2904452
Slovakia | 77.22 | 26096 | 5439418
Poland | 77.72 | 26061 | 38532816
Turkmenistan | 68.92 | 25070 | 5968388
Kazakhstan | 71.4 | 24557 | 18314822
Hungary | 76.01 | 24350 | 9788940

## Sheet: Dow Jones

Data | Chiusura | Volume
2022-12-30 00:00:00 | 33147.25 | 295500000
2022-12-29 00:00:00 | 33220.8 | 243060000
2022-12-28 00:00:00 | 32875.71 | 252260000
2022-12-27 00:00:00 | 33241.56 | 246010000
2022-12-23 00:00:00 | 33203.93 | 221050000
2022-12-22 00:00:00 | 33027.49 | 340640000
2022-12-21 00:00:00 | 33376.48 | 328020000
2022-12-20 00:00:00 | 32849.74 | 303970000
2022-12-19 00:00:00 | 32757.54 | 326430000
2022-12-16 00:00:00 | 32920.46 | 756310000
2022-12-15 00:00:00 | 33202.22 | 394290000
2022-12-14 00:00:00 | 33966.35 | 339090000
2022-12-13 00:00:00 | 34108.64 | 442650000
2022-12-12 00:00:00 | 34005.04 | 313440000
2022-12-09 00:00:00 | 33476.46 | 287630000
2022-12-08 00:00:00 | 33781.48 | 271830000
2022-12-07 00:00:00 | 33597.92 | 359980000
2022-12-06 00:00:00 | 33596.34 | 306220000
2022-12-05 00:00:00 | 33947.1 | 312960000
2022-12-02 00:00:00 | 34429.88 | 290580000
2022-12-01 00:00:00 | 34395.01 | 348720000
2022-11-30 00:00:00 | 34589.77 | 524440000
2022-11-29 00:00:00 | 33852.53 | 279750000
2022-11-28 00:00:00 | 33849.46 | 300330000
2022-11-25 00:00:00 | 34347.03 | 131660000
2022-11-23 00:00:00 | 34194.06 | 236820000
2022-11-22 00:00:00 | 34098.1 | 277070000
2022-11-21 00:00:00 | 33700.28 | 352960000
2022-11-18 00:00:00 | 33745.69 | 312950000
2022-11-17 00:00:00 | 33546.32 | 319210000
2022-11-16 00:00:00 | 33553.83 | 301560000
2022-11-15 00:00:00 | 33592.92 | 390610000
2022-11-14 00:00:00 | 33536.7 | 354340000
2022-11-11 00:00:00 | 33747.86 | 427790000
2022-11-10 00:00:00 | 33715.37 | 480130000
2022-11-09 00:00:00 | 32513.94 | 355200000
2022-11-08 00:00:00 | 33160.83 | 335340000
2022-11-07 00:00:00 | 32827 | 336300000
2022-11-04 00:00:00 | 32403.22 | 422370000
2022-11-03 00:00:00 | 32001.25 | 354440000
2022-11-02 00:00:00 | 32147.76 | 398430000
2022-11-01 00:00:00 | 32653.2 | 323210000
2022-10-31 00:00:00 | 32732.95 | 390890000
2022-10-28 00:00:00 | 32861.8 | 495830000
2022-10-27 00:00:00 | 32033.28 | 375720000
2022-10-26 00:00:00 | 31839.11 | 430400000
2022-10-25 00:00:00 | 31836.74 | 336930000
2022-10-24 00:00:00 | 31499.62 | 345040000
2022-10-21 00:00:00 | 31082.56 | 418190000

## Sheet: Vittime WW2 in Europa

Paese | Civili | Militari | Ebrei
Danimarca | 0 | 0 | 1500
Lussemburgo | 0 | 0 | 3000
Norvegia | 0 | 10000 | 1500
Bulgaria | 0 | 10000 | 7000
Finlandia | 0 | 90000 | 
Stati Uniti | 8000 | 170000 | 0
Romania | 40000 | 200000 | 425000
Austria | 40000 | 230000 | 40000
Belgio | 50000 | 10000 | 40000
Gran Bretagna | 60000 | 330000 | 0
Cecoslovacchia | 70000 | 20000 | 260000
Grecia | 80000 | 20000 | 60000
Ungheria | 80000 | 120000 | 200000
Paesi Bassi | 100000 | 10000 | 90000
Lettonia | 120000 | 0 | 0
Italia | 138000 | 319000 | 15000
Estonia | 140000 | 0 | 0
Lituania | 170000 | 0 | 0
Francia | 270000 | 250000 | 90000
Jugoslavia | 1300000 | 300000 | 55000
Polonia | 2500000 | 120000 | 2800000
Germania | 3640000 | 3250000 | 170000
Unione Sovietica | 16900000 | 8600000 | 1720000

## Sheet: Fasce d'età Italia 2022

Fascia d'Età | Maschi | Femmine
0-4 | 1101059 | 1041775
05-09 | 1297135 | 1226182
10-14 | 1453792 | 1369852
15-19 | 1482037 | 1384080
20-24 | 1532384 | 1390957
25-29 | 1550618 | 1450727
30-34 | 1631425 | 1580224
35-39 | 1717489 | 1695383
40-44 | 1935510 | 1932574
45-49 | 2293863 | 2316007
50-54 | 2375261 | 2431976
55-59 | 2324641 | 2410494
60-64 | 1960517 | 2092767
65-69 | 1683212 | 1844230
70-74 | 1577285 | 1791634
75-79 | 1191693 | 1457824
80-84 | 95939 | 1324533
85-89 | 519985 | 881267
90-94 | 192933 | 447406
95-99 | 3544 | 124858
100+ | 3287 | 16427
Fascia d'Età | Maschi | Femmine
0-4 | 1101059 | -1041775
05-09 | 1297135 | -1226182
10-14 | 1453792 | -1369852
15-19 | 1482037 | -1384080
20-24 | 1532384 | -1390957
25-29 | 1550618 | -1450727
30-34 | 1631425 | -1580224
35-39 | 1717489 | -1695383
40-44 | 1935510 | -1932574
45-49 | 2293863 | -2316007
50-54 | 2375261 | -2431976
55-59 | 2324641 | -2410494
60-64 | 1960517 | -2092767
65-69 | 1683212 | -1844230
70-74 | 1577285 | -1791634
75-79 | 1191693 | -1457824
80-84 | 95939 | -1324533
85-89 | 519985 | -881267
90-94 | 192933 | -447406
95-99 | 3544 | -124858
100+ | 3287 | -16427

## Sheet: Residenti per regione

Regione | Residenti
Lombardia | 9950742
Lazio | 5707112
Campania | 5592175
Veneto | 4838253
Sicilia | 4802016
Emilia-Romagna | 4426929
Piemonte | 4240736
Puglia | 3900852
Toscana | 3651152
Calabria | 1841300
Sardegna | 1575028
Liguria | 1502624
Marche | 1480839
Abruzzo | 1269860
Friuli Venezia Giulia | 1192191
Trentino-Alto Adige | 1075317
Umbria | 854137
Basilicata | 536659
Molise | 28984
Valle d'Aosta | 122955

## Sheet: Italiani residenti allestero

Continente di residenza | Iscritti
Europa | 3187011
Africa | 70171
Asia | 73887
America | 2311871
Oceania | 163054
Antartide | 74

## Sheet: Omicidi e possesso di armi

Location | Intentional homicide victims per 100,000 inhabitants				 | Estimate of firearms in civilian possession pe 100 inhabitants
United States | 6.8 | 120.5
Yemen | 6.3 | 52.8
New Caledonia | 3.1 | 42.5
Montenegro | 2.4 | 39.1
Serbia | 1.1 | 39.1
Canada | 2.1 | 34.7
Uruguay | 8.9 | 34.7
Cyprus | 1.3 | 34
Finland | 1.6 | 32.4
Lebanon | 2.3 | 31.9
Iceland | 0.5 | 31.7
Bosnia and Herzegovina | 1 | 31.2
Austria | 0.7 | 30
North Macedonia | 1.1 | 29.8
Liechtenstein | 5.1 | 28.8
Norway | 0.5 | 28.8
Malta | 0.4 | 28.3
Switzerland | 0.5 | 27.6
New Zealand | 2.6 | 26.3
Kosovo | 2 | 23.8
Sweden | 1.1 | 23.1
Greenland | 5.4 | 22.3
Pakistan | 4 | 22.3
Portugal | 0.8 | 21.3
France | 1.1 | 19.6
French Guiana | 13.3 | 19.6
Germany | 0.8 | 19.6
Iraq | 9.4 | 19.6
Monaco | 0 | 19.6
Réunion | 1.7 | 19.6
Luxembourg | 0.6 | 18.9
Bahamas | 29.2 | 18.8
Jordan | 1 | 18.7
Venezuela | 19.3 | 18.5
Greece | 0.9 | 17.6
Kuwait | 0.3 | 16.7
Oman | 0.2 | 16.7
Paraguay | 7.8 | 16.7
Qatar | 0.3 | 16.7
Saudi Arabia | 0.8 | 16.7
United Arab Emirates | 0.5 | 16.7
U.S. Virgin Islands | 49.6 | 16.6
Turkey | 2.5 | 16.5
Suriname | 5.7 | 15.9
Guyana | 16.3 | 15.8
Slovenia | 0.4 | 15.6
Namibia | 12.4 | 15.4
Thailand | 4.8 | 15.1
Australia | 0.7 | 14.5

## Sheet: Giocatori NBA

PLAYER | 2P% | 3P% | FT% | Punti/min | Rimb/min | AST+Rubate+Stoppate-Perse/min
LeBron James | 0.553715933401544 | 0.344 | 0.735 | 0.7144914690892976 | 0.1972634611123421 | 0.16114557943718147
Kareem Abdul-Jabbar | 0.5597935593340168 | 0.055999999999999994 | 0.721 | 0.668227552832225 | 0.30358945792570413 | 0.13024405528670405
Karl Malone | 0.519034749034749 | 0.27399999999999997 | 0.742 | 0.6732297819587253 | 0.27287974914314883 | 0.07208488295777729
Michael Jordan | 0.510171800166967 | 0.327 | 0.835 | 0.7874177029992685 | 0.16269202633504024 | 0.1491343574737869
Dirk Nowitzki | 0.4959511984452602 | 0.38 | 0.879 | 0.6144022426849923 | 0.22366499892927366 | 0.07101835808982421
Shaquille O'Neal | 0.5829174170311294 | 0.045 | 0.527 | 0.6822053104945488 | 0.31249850895817927 | 0.07603120452322447
Carmelo Anthony | 0.4720315137872819 | 0.355 | 0.8140000000000001 | 0.6501275480890768 | 0.17944062693907567 | 0.051409923471146556
Moses Malone | 0.492400104465918 | 0.1 | 0.769 | 0.6081293958421158 | 0.3596991413547514 | 0.018060393601206984
 |  |  |  | 0.879 |  | 

## Sheet: Fantavoti 2021-22 tutti

Codice Giocatore | Giornata | Fantavoto |  |  | 
1015976 | 4 | 5.5 |  |  | 
1015976 | 8 | 5.85 |  |  | 
1015976 | 6 | 5.85 |  |  | 
1015976 | 5 | 6.5 |  |  | 
1015976 | 1 | 6.5 |  |  | 
1015976 | 7 | 6.85 |  |  | 
1015976 | 3 | 6.85 |  |  | 
1015976 | 2 | 6.85 |  |  | 
1015994 | 8 | 5 |  |  | 
1015994 | 7 | 5.2 |  |  | 
1015994 | 6 | 5.7 |  |  | 
1015994 | 4 | 5.7 |  |  | 
1015994 | 12 | 5.75 |  |  | 
1015994 | 10 | 5.75 |  |  | 
1015994 | 1 | 5.75 |  |  | 
1015994 | 9 | 6 |  |  | 
1015994 | 3 | 6 |  |  | 
1015994 | 2 | 6.35 |  |  | 
1015994 | 11 | 7.5 |  |  | 
1015994 | 13 | 6.75 |  |  | 
1015994 | 14 | 7.25 |  |  | 
1015994 | 15 | 10.5 |  |  | 
1015994 | 17 | 6.25 |  |  | 
1015994 | 18 | 6 |  |  | 
1015994 | 19 | 6 |  |  | 
1016003 | 1 | 5.35 |  |  | 
1016005 | 10 | 5.25 |  |  | 
1016005 | 2 | 5.35 |  |  | 
1016005 | 11 | 5 |  |  | 
1016005 | 13 | 5.75 |  |  | 
1016005 | 12 | 5.75 |  |  | 
1016005 | 8 | 5.85 |  |  | 
1016005 | 6 | 5.85 |  |  | 
1016005 | 1 | 5.85 |  |  | 
1016005 | 9 | 6 |  |  | 
1016005 | 5 | 5.5 |  |  | 
1016005 | 3 | 9.35 |  |  | 
1016005 | 4 | 10 |  |  | 
1016005 | 14 | 5.25 |  |  | 
1016005 | 15 | 9.75 |  |  | 
1016005 | 16 | 5.5 |  |  | 
1016005 | 17 | 9.75 |  |  | 
1016005 | 18 | 11.5 |  |  | 
1016005 | 19 | 5.75 |  |  | 
1016029 | 13 | 5.25 |  |  | 
1016029 | 4 | 5.5 |  |  | 
1016029 | 11 | 6 |  |  | 
1016029 | 5 | 6.2 |  |  | 
1016029 | 6 | 6.35 |  |  | 

## Sheet: Processo di vendita

Fase | Anno 2023 | 
Primo contatto | 998 | 
Richiesta di preventivo | 220 | 
Preventivo inviato | 204 | 
Preventivo accettato | 149 | 
Ordine eseguito | 142 | 
Fattura pagata | 106 | 

## Sheet: Fantavoti 2021-22 Comparazione

Giornata | Gerard Deulofeu | Pedro | Pereyra | Pobega | Politano |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
1 | 9.85 | 6.5 | 9.5 |  | 6.25 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
2 | 10 | 8.2 | 6 |  | 7 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
3 | 6.5 | 5.35 | 6.2 | 9.5 | 9.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
4 | 5.5 | 6.2 | 5.5 | 6.35 | 6.85 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
5 | 6.2 | 5.7 | 5.35 | 6.2 | 6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
6 | 6.35 | 10 | 5.7 | 5.85 | 6.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
7 | 7.5 | 5 | 9.2 | 6 | 6.35 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
8 | 6 | 6.2 | 3.5 | 5.35 | 5.35 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
9 |  | 5.25 |  | 9.25 | 6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
10 |  | 10 | 6 | 5 | 6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
11 | 6 | 9.75 | 5 | 7 | 6.25 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
12 | 10 | 12 | 7.75 |  | 5.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
13 | 5.25 | 5.25 | 5 | 7.25 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
14 | 6 | 5.25 | 5.5 | 5.75 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
15 | 7.5 | 9.75 |  | 9.75 | 4.75 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
16 | 9.5 | 6.25 |  | 5.25 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
17 | 5.25 | 6.75 |  | 6.25 | 6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
18 | 13 | 10 |  | 10 | 5.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
19 | 5 | 9.25 |  | 5.75 | 5.75 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
20 |  | 4.75 |  |  | 7.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
21 | 5.5 | 5.25 |  |  | 6.25 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
22 | 5.75 | 7.5 |  |  | 5.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
23 | 4.75 |  |  | 4.75 | 6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
24 |  | 5.5 |  | 5.25 | 7.25 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
25 | 5.75 | 6.25 |  | 5.25 | 5.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
26 | 9.75 | 6 | 6 | 5.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
27 | 6 | 9.75 | 7.5 | 4.5 | 6.75 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
28 | 9.25 | 5.5 | 6.5 | 5.25 | 5.75 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
29 | 5.25 | 6 | 6 | 7 | 7.25 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
30 | 9.5 | 5 | 7.25 | 4.5 | 6.25 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
31 |  |  | 7 |  | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
32 | 10.5 | 8 |  | 4.75 | 5.25 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
33 | 11.5 |  | 6.25 | 6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
34 | 7 |  |  |  | 5.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
35 | 6.25 |  | 5 | 6.25 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
36 | 6.5 |  | 6 | 6 | 6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
37 | 7.25 | 5.5 | 5 | 5.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
38 | 10 | 9.75 | 5.5 | 5.75 | 9.25 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

## Sheet: Conto Economico

Voci del conto economico | Valori
Vendite | 3869000
Costi di vendita | -580350
Costi di marketing | -812490
Costi di produzione | -464280
Costi di amministrazione | -193450
Margine Operativo Lordo | 1818430
Rendite finanziarie | 116070
Interessi passivi | -270830
Ammortamenti | -309520
Imposte | -193450
Utile | 1160700


---

# L4 - 1 immobiliare

**File:** `L4 - 1 immobiliare.xlsx`
**Tipo:** `.xlsx`
**Dimensione:** 9.5 KB
**Ultima modifica:** 02/07/2026 09:24

---

## Sheet: Dati

id | superficie_mq | prezzo_eur | zona | anno_costruzione | piano | ascensore
1 | 46 | 65000 | Periferia | 1985 | 3 | Sì
2 | 179 | 221000 | Periferia | 1961 | 6 | Sì
3 | 99 | 490000 | Centro | 2014 | 0 | No
4 | 147 | 252000 | Periferia | 1978 | 7 | Sì
5 | 41 | 61000 | Periferia | 1970 | 6 | Sì
6 | 126 | 498000 | Centro | 1963 | 1 | Sì
7 | 107 | 284000 | Semi-centro | 1955 | 7 | Sì
8 | 62 | 1850000 | Periferia | 1960 | 8 | Sì
9 | 132 | 186000 | Periferia | 1974 | 1 | Sì
10 | 60 | 156000 | Semi-centro | 1979 | 1 | Sì
11 | 81 | 115000 | Periferia | 1997 | 5 | Sì
12 | 58 | 171000 | Semi-centro | 1971 | 8 | Sì
13 | 137 | 511000 | Centro | 1984 | 8 | Sì
14 | 54 | 137000 | Semi-centro | 1979 | 0 | No
15 | 95 | 38000 | Centro | 1977 | 7 | Sì
16 | 157 | 209000 | Periferia | 1968 | 4 | Sì
17 | 177 | 350000 | Periferia | 1983 | 6 | Sì
18 | 96 | 253000 | Semi-centro | 1967 | 8 | Sì
19 | 68 | 106000 | Periferia | 1969 | 2 | No
20 | 137 | 533000 | Centro | 2009 | 8 | Sì
21 | 42 | 124000 | Semi-centro | 1964 | 8 | Sì
22 | 127 | 199000 | Periferia | 1964 | 7 | No
23 | 107 | 237000 | Semi-centro | 2014 | 2 | No
24 | 169 | 230000 | Periferia | 1975 | 2 | Sì
25 | 175 | 278000 | Periferia | 1950 | 5 | Sì
26 | 132 | 448000 | Centro | 1989 | 3 | Sì
27 | 60 | 112000 | Periferia | 1960 | 7 | Sì
28 | 176 | 350000 | Periferia | 1966 | 2 | No
29 | 175 | 940000 | Centro | 2004 | 3 | Sì
30 | 91 | 188000 | Periferia | 1989 | 6 | Sì
31 | 152 | 210000 | Periferia | 2016 | 7 | Sì
32 | 126 | 283000 | Semi-centro | 1952 | 8 | Sì
33 | 58 | 119000 | Semi-centro | 1957 | 3 | Sì
34 | 124 | 456000 | Centro | 1959 | 6 | No
35 | 94 | 191000 | Periferia | 2019 | 2 | No
36 | 102 | 237000 | Semi-centro | 2010 | 6 | Sì
37 | 150 | 629000 | Centro | 1995 | 6 | Sì
38 | 53 | 78000 | Periferia | 1962 | 0 | No
39 | 103 | 171000 | Periferia | 1974 | 3 | Sì
40 | 86 | 327000 | Centro | 1985 | 7 | Sì
41 | 153 | 327000 | Periferia | 2020 | 1 | Sì
42 | 63 | 102000 | Periferia | 1980 | 2 | No
43 | 55 | 67000 | Periferia | 1971 | 6 | Sì
44 | 156 | 461000 | Semi-centro | 1986 | 6 | Sì
45 | 164 | 240000 | Periferia | 1901 | 3 | Sì
46 | 178 | 223000 | Periferia | 1957 | 5 | Sì
47 | 168 | 467000 | Semi-centro | 2017 | 2 | Sì
48 | 57 | 87000 | Periferia | 1958 | 3 | Sì
49 | 103 | 172000 | Periferia | 1955 | 1 | No

## Sheet: Dizionario

Colonna | Tipo | Descrizione | Valori possibili
id | numerico intero | Identificatore univoco dell'annuncio | 1–100
superficie_mq | numerico intero | Superficie lorda in metri quadrati | es. 40–180
prezzo_eur | numerico intero | Prezzo di vendita in euro | es. 80.000–900.000
zona | categorico | Zona della città | Centro / Semi-centro / Periferia
anno_costruzione | numerico intero | Anno di costruzione dell'edificio | es. 1950–2022
piano | numerico intero | Piano dell'appartamento | 0 = piano terra
ascensore | categorico | Presenza dell'ascensore nell'edificio | Sì / No


---

# L4 - Regressione lineare

**File:** `L4 - Regressione lineare.pptx`
**Tipo:** `.pptx`
**Dimensione:** 109.9 KB
**Ultima modifica:** 02/07/2026 09:24

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
x = variabile indipendente (es. superficie_mq)
y = variabile dipendente (es. prezzo_eur)

Stiamo chiedendo: al crescere di x, come cambia y?
A cosa serve
• Descrivere la relazione tra due variabili
• Quantificare quanto x spiega y
• Fare previsioni su nuovi dati

---

La formula della retta
y  =  a  +  b · x
a
Intercetta
Valore di y quando x = 0
Es: se superficie = 0 il prezzo base sarebbe €a (non sempre ha senso fisico)
b
Coefficiente angolare
Di quanto aumenta y per ogni unità in più di x
Es: b = 2.500 significa che ogni mq aggiuntivo vale circa €2.500
R²
Coefficiente di determinazione
Quota della variabilità di y spiegata dal modello
R² = 0.82 → la superficie spiega l'82% della variazione dei prezzi

---

La formula della retta

---

Interpretare R²
R² misura quanto bene la retta si adatta ai dati
R² < 0.3
Relazione debole
La retta spiega poco
0.3 – 0.6
Relazione moderata
Ci sono altri fattori
0.6 – 0.8
Relazione buona
Modello utile
R² > 0.8
Relazione molto forte
Modello affidabile
⚠  Attenzione: R² alto non significa causalità
Un R² = 0.85 tra superficie e prezzo dice che la superficie è un buon predittore del prezzo.
Non dice che la superficie causa il prezzo — ci sono zone, finiture, anno di costruzione e altri fattori.
La regressione descrive, non spiega.

---

Regressione in Excel – passo dopo passo
1  Crea lo scatter plot
Seleziona le colonne superficie_mq e prezzo_eur
Inserisci → Grafici → Dispersione
2  Aggiungi la trendline
Clic destro sui punti → Aggiungi linea di tendenza
Seleziona: Lineare
3  Mostra equazione e R²
Nel pannello trendline:
Visualizza equazione nel grafico
Visualizza R² nel grafico
4  Leggi i risultati
Il grafico mostra: y = bx + a
Annota b (pendenza) e R²
Es: y = 2480x + 45.000, R² = 0,78
5  Fai una previsione
Scrivi in una cella:
=2480*C2+45000
Sostituisci con i tuoi valori reali
6  Verifica con REGR.LIN
=REGR.LIN(prezzo_eur; superficie_mq)
Restituisce {b; a} — confronta con il grafico

---

Perché l'EDA viene prima della regressione
Gli outlier distorcono la retta — ricordate quelli trovati nel Blocco 1?
❌  Con gli outlier
• id 8: €1.850.000 in Periferia
• id 15: €38.000 in Centro
• id 56: 8 mq a €45.000
• id 68: €920.000 in Periferia

La retta viene tirata verso i valori estremi.
R² apparentemente alto ma fuorviante.
Le previsioni su appartamenti normali saranno sbagliate.
✅  Senza gli outlier
Filtra le righe anomale prima di creare il grafico:

Dati → Filtro automatico
Escludi id 8, 15, 56, 68

La retta descrive meglio il mercato normale.
R² più basso ma più onesto.
Le previsioni sono più affidabili.

---

Blocco 2  ·  Usare la retta per fare previsioni
Supponiamo di aver ottenuto:  y = 2.480x + 47.000   (R² = 0,76)
Superficie (mq)
Formula applicata
Prezzo stimato €
60 mq
=2.480×60 + 47.000
€ 195.800
90 mq
=2.480×90 + 47.000
€ 270.200
120 mq
=2.480×120 + 47.000
€ 344.600
150 mq
=2.480×150 + 47.000
€ 419.000
⚠  La previsione è valida nel range dei dati osservati (es. 40–180 mq). Estrapolare fuori da questo range (es. 500 mq) produce stime non affidabili — la retta non sa cosa succede dove non ha visto dati.

---

Blocco 2  ·  Prerequisito: attivare il componente Analisi dati
La regressione multipla richiede il componente aggiuntivo Analysis ToolPak
1
Apri le Opzioni di Excel
File → Opzioni
2
Vai a Componenti aggiuntivi
Nel menu laterale: Componenti aggiuntivi
3
Gestisci componenti
In fondo: Gestisci → Componenti aggiuntivi di Excel → Vai
4
Attiva Analysis ToolPak
Spunta ☑ Strumenti di analisi → OK
5
Verifica
Scheda Dati → in fondo a destra compare il pulsante Analisi dati
⚠  Operazione da fare una sola volta per installazione di Excel. Su Mac il percorso è: Strumenti → Componenti aggiuntivi di Excel.

---

Regressione multipla: superficie + anno di costruzione
E se il prezzo dipendesse da più variabili insieme?
prezzo  =  a  +  b₁ · superficie_mq  +  b₂ · anno_costruzione
b₁
superficie_mq
Es: b₁ = 2.200
Ogni mq aggiuntivo
vale ~€2.200
b₂
anno_costruzione
Es: b₂ = 380
Ogni anno più recente
vale ~€380
R²
del modello
Es: R² = 0,81
Le due variabili
spiegano l'81%

---

Blocco 2  ·  Regressione multipla in Excel – passo dopo passo
1  Prepara i dati (senza outlier)
Filtra o copia i dati escludendo id 8, 15, 56, 68.
Le colonne devono essere adiacenti oppure selezionabili con Ctrl+clic.
2  Apri Analisi dati
Scheda Dati → Analisi dati → Regressione → OK
3  Imposta le variabili
Intervallo Y: colonna prezzo_eur
Intervallo X: colonne superficie_mq e anno_costruzione (selezionale insieme)
4  Scegli l'output
Seleziona un foglio nuovo o una cella vuota come destinazione → OK
5  Leggi i risultati
Nella tabella Coefficienti:
• Intercept = a
• superficie_mq = b₁
• anno_costruzione = b₂
R² è in cima al report
6  Confronta con la regressione semplice
R² è aumentato rispetto al modello con sola superficie?
Di quanto? Valeva aggiungere anno_costruzione?

---

Esercizio guidato  ·  immobiliare.xlsx
Apri il file e segui i passi:
1
Crea uno scatter plot superficie_mq vs prezzo_eur. Aggiungi trendline lineare con R². Annota i valori.
2
Identifica visivamente i punti anomali. Filtra i dati escludendo gli outlier. Come cambia R²?
3
Con l'equazione pulita, stima il prezzo di un appartamento da 75 mq e uno da 110 mq
4
Attiva Analisi dati ed esegui la regressione multipla: Y = prezzo_eur, X = superficie_mq + anno_costruzione
5
Confronta R² del modello semplice vs multiplo. Quanto aggiunge anno_costruzione? Qual è il coefficiente b₂?

---

Riepilogo  ·  Regressione lineare e multipla
📈
La regressione lineare trova la retta y = a + b·x che minimizza gli errori sui dati
📐
b dice quanto vale ogni unità di x — ogni mq aggiuntivo, ogni anno più recente
🎯
R² misura la bontà del fit: la regressione multipla lo aumenta aggiungendo variabili esplicative
⚠️
Gli outlier distorcono la retta e R² può risultare fuorviante: l'EDA viene sempre prima


---

# PowerQuery v3

**File:** `PowerQuery v3.pptx`
**Tipo:** `.pptx`
**Dimensione:** 896.4 KB
**Ultima modifica:** 02/07/2026 09:24

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
Ogni tipo di unità osservazionale (studenti, corsi, iscrizioni) ha la sua tabella dedicata.

---

Efficienza Computazionale: Molti linguaggi (R, Python) sono ottimizzati per operazioni vettoriali su colonne.
Visualizzazione: Strumenti come ggplot2 o Seaborn richiedono dati in formato lungo (long format).
Integrità: Riduce drasticamente la probabilità di errori logici durante il filtraggio o l'aggregazione.
Standardizzazione: Permette di riutilizzare lo stesso codice su dataset diversi ma con la stessa struttura.
Perché la struttura conta?

---

Messy (Compatto)
Colonna: Sesso_Età
Valori: "M_25", "F_30", "M_18"
Richiede parsing di stringhe ogni volta che si vuole filtrare per età.
Tidy (Atomico)
Colonna A: Sesso (M, F)
Colonna B: Età (25, 30, 18)
Permette analisi statistiche dirette (es. età media per sesso).
Variabili Multiple in una Colonna

---

Messy data: diritto da un film dell’orrore

---

Power Query
Pulizia dati strutturata e ripetibile
Dataset: 20260708_Risposte_Invito.xlsx

---

Il problema
Cosa succede se il file sorgente cambia il mese prossimo?
Come sapete quali operazioni avete fatto, e in che ordine?
Come collaborate con un collega sullo stesso processo di cleaning?
Cosa fate se vi accorgete di aver sbagliato un passo a metà lavoro?
Problemi del cleaning manuale in Excel
✗  Non ripetibile
✗  Non documentato
✗  Non reversibile
✗  Non collaborativo

---

Interfaccia Power Query |  Demo
Come aprire Power Query
Scheda Dati → Recupera dati → Da file → Da cartella di lavoro
Seleziona il foglio 'Originale'
Clic su Trasforma dati (non Carica)
[ Screenshot: Dati → Recupera dati → Da file ]
Elementi chiave dell'interfaccia
Pannello Passaggi applicati
La lista di tutte le trasformazioni — il cuore di PQ
Anteprima dati
Mostra il risultato dopo ogni passo
Barra della formula
Codice M del passo selezionato
Pannello Query
Lista di tutte le query nel file

---

La reversibilità
Come funziona l'undo in Power Query
Sorgente
Intestazioni promosso
Tipo modificato
Duplicati rimossi
Testo tagliato
▲  Selezionato: anteprima mostra i dati a questo punto
Per eliminare un passo:
Clic destro sul passo nel pannello → Elimina
I passi successivi vengono ricalcolati automaticamente
Se i passi successivi dipendono da quello eliminato → errore segnalato chiaramente
[ Screenshot: Pannello Passaggi – clic destro Elimina ]

---

Operazioni di cleaning
Dal cleaning manuale a Power Query

---

Demo sul dataset – sequenza consigliata
1
Promuovi intestazioni
Home → Usa prima riga come intestazioni
2
Tipo dati colonne
Seleziona colonne → Trasforma → Rileva tipo dati
3
Togli gli spazi in eccesso in tutti i campi testo
Seleziona col. testo → Trasforma → Taglia
→ Risolve spazi in email e nomi
4
Proper case sui nomi
Colonna 'Nome e Cognome' → Trasforma → Proper Case.
→ Risolve: vincenzo, CARLA, clelia LORIGLIOLA
5
Rimuovi duplicati
Seleziona tutte le colonne → Home → Rimuovi righe → Duplicati
→ Silvio Contardi appare 2 volte, Monica Limongi 3 volte
6
Filtra valori non corretti
Filtro colonna partecipanti → “Non contiene ‘-’”
→ Benedetta Contardi (-2), Simona Lucenti (0)

---

Demo: Split Nome e Cognome
Obiettivo: da 'Debora Nizzola' → Nome: 'Debora'  |  Cognome: 'Nizzola'
1
Seleziona colonna 'Nome e Cognome'
2
Trasforma → Dividi colonna → In base al delimitatore
3
Delimitatore: Spazio  |  Dove: All'occorrenza più a sinistra
4
Rinomina: colonna.1 → Nome,  colonna.2 → Cognome
5
Trasforma → Ogni parola in maiuscolo (su entrambe le nuove colonne)
⚠  Caso speciale: 'laura iolanda teresa Minotti' → 3 spazi → gestire manuale o con logica aggiuntiva
[ Screenshot: Finestra Split colonna per spazio ]

---

Split Indirizzo → Via / Città / Provincia
Obiettivo: da 'Via Accursio Di Leo 6, Rescaldina, RM'  →  3 colonne
Passaggi in Power Query
Seleziona colonna Indirizzo
Dividi per delimitatore: virgola → ogni occorrenza
Ottieni 3 colonne (nel caso base)
Taglia tutte e 3 (rimuovi spazi)
Rinomina: Via, Città, Provincia
Casi problematici nel dataset
Emanuela Longari
5 segmenti (indirizzo con CAP incluso)
Roberta Pettiti
Solo 2 segmenti – provincia mancante
Monica MORELLI
Solo provincia, indirizzo incompleto
Valeria Costanzi
Terzo campo è un comune, non provincia

---

Blocco 3  [avanzato]  Normalizzazione numero di telefono
Obiettivo: tutti nel formato  +39 XXX XXXXXXX
Formati presenti nel dataset
3389962593
cellulare senza prefisso (10 cifre)
+393480413086
con prefisso internazionale (12 cifre)
 +393342237895
con spazi iniziali
+39 335 457510
già formattato con spazi
Logica corretta (colonna personalizzata)
⚠  '3932798650' inizia con 39 ma NON è il prefisso! È un cellulare 393... con 10 cifre.
Regola: lunghezza 10 cifre = senza prefisso  |  12 cifre = con prefisso 39
let
  pulito = Text.Remove([Telefono], {" ", "+", "-"}),
  norm = if Text.Length(pulito) = 12
         and Text.StartsWith(pulito, "39")
         then "+" & Text.Insert(pulito, 2, " ")
         else "+39 " & pulito
in norm

---

Esercizio pratico |  Hands-on
Consegna agli studenti
File: 20260708_Risposte_Invito.xlsx  •  Foglio: Originale  •  Target: foglio Desiderata
Base
Importa il foglio Originale in Power Query
Taglia tutti i campi testo (rimuovi spazi)
Proper case sulla colonna Nome e Cognome
Dividi Nome e Cognome in due colonne
Rimuovi i duplicati
Filtra righe con partecipanti negativi o zero
Avanzato
Dividi la colonna Indirizzo in Via / Città / Provincia
Normalizza il numero di telefono (colonna personalizzata)
Separa Data di conferma in Conversion Day e Conversion Time

---

La ripetibilità
Scenario: arriva il file aggiornato del mese prossimo
1
Duplica il file sorgente
Simula l'arrivo di nuovi dati
2
Home → Impostazioni origine dati
Cambia il percorso al nuovo file
3
Home → Aggiorna tutto
La pipeline si riesegue automaticamente
4
Verifica il risultato
Stesso output pulito, nuovi dati
[ Screenshot: Demo aggiornamento sorgente dati + Aggiorna tutto ]

---

Riepilogo
🔁
Ripetibile
La stessa pipeline funziona ogni mese senza lavoro manuale
📋
Documentato
Il pannello Passaggi è un log automatico di tutte le operazioni
↩
Reversibile
Ogni passo può essere eliminato o modificato in qualsiasi momento
🤝
Condivisibile
La query può essere esportata e riusata da altri

---

Esercizio  Pulisci il file ordini.xlsx
File SPORCO  (foglio: Sporco)
ID Ordine
es. ORD-1001
Nome e Cognome
es. '  MARCO rossi ', 'giulia FERRARI'
Prodotto
es. 'Notebook ' (spazio finale)
Quantità
es. -3, 0 (valori anomali)
Prezzo unitario (€)
es. 12.90
Stato
es. 'consegnato', 'IN TRANSITO'
Data ordine
es. 2024-03-15
→
File PULITO  (foglio: Desiderata)
ID Ordine
invariato
Nome
da split + Proper case
Cognome
da split + Proper case
Prodotto
trim applicato
Quantità
solo valori > 0
Prezzo unitario (€)
invariato
Stato
Consegnato / In transito / Annullato
Data ordine
invariato
Operazioni da usare:  Trim  •  Proper case  •  Rimuovi duplicati  •  Filtra righe (Quantità ≤ 0 e righe vuote)  •  Split colonna  •  Sostituisci valori (Stato)


---

# Prestiti - Regressione Logaritmica

**File:** `Prestiti - Regressione Logaritmica.xlsx`
**Tipo:** `.xlsx`
**Dimensione:** 8.7 KB
**Ultima modifica:** 02/07/2026 09:24

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
12 | 61 | 19000 | 0 | Sì
13 | 50 | 88251 | 11575 | Sì
14 | 33 | 86510 | 23347 | Sì
15 | 51 | 52309 | 39681 | No
16 | 30 | 93655 | 32168 | Sì
17 | 58 | 48890 | 58105 | No
18 | 45 | 35183 | 4802 | Sì
19 | 62 | 78771 | 25538 | Sì
20 | 49 | 23663 | 14739 | Sì
21 | 50 | 51252 | 10469 | No
22 | 38 | 63952 | 13307 | No
23 | 24 | 45000 | 55000 | No
24 | 30 | 49150 | 47363 | No
25 | 61 | 23578 | 38068 | No
26 | 24 | 65100 | 38209 | No
27 | 43 | 41874 | 19354 | Sì
28 | 65 | 90783 | 7357 | Sì
29 | 32 | 27062 | 28124 | No
30 | 57 | 89213 | 45557 | Sì
31 | 50 | 62965 | 42276 | Sì
32 | 22 | 34578 | 20354 | Sì
33 | 41 | 53251 | 37030 | No
34 | 26 | 79589 | 34211 | Sì
35 | 24 | 18749 | 20950 | No
36 | 53 | 91368 | 34915 | Sì
37 | 52 | 47235 | 43876 | No
38 | 63 | 21000 | 500 | Sì
39 | 32 | 37184 | 16928 | No
40 | 35 | 51888 | 27843 | No
41 | 44 | 50015 | 38803 | No
42 | 35 | 63982 | 27880 | Sì
43 | 47 | 78381 | 5685 | Sì
44 | 24 | 18536 | 42817 | No
45 | 34 | 76917 | 31505 | No
46 | 46 | 61629 | 4017 | Sì
47 | 49 | 35955 | 9723 | No
48 | 29 | 66307 | 53969 | No
49 | 41 | 57761 | 39533 | No

## Sheet: Dizionario

Colonna | Tipo | Descrizione
id | intero | Identificatore univoco del cliente
eta | intero | Età del richiedente in anni
reddito_annuo | intero | Reddito annuo lordo in euro
debiti_totali | intero | Totale debiti in corso in euro (mutui, prestiti, carte)
prestito_approvato | categorico | Esito della richiesta: Sì = approvato, No = rifiutato


---

# Pulizia dei dati in Excel (1)

**File:** `Pulizia dei dati in Excel (1).pptx`
**Tipo:** `.pptx`
**Dimensione:** 2366.4 KB
**Ultima modifica:** 02/07/2026 09:24

---

Pulizia dei dati in Excel
da ”I dieci metodi principali per la pulizia dei dati” su support.microsoft.com

---

Informazioni di base
Importare i dati da un'origine dati esterna.
Creare una copia di backup dei dati originali in una cartella di lavoro separata.
Verificare che i dati nelle righe e nelle colonne siano in formato tabulare con:
dati simili in ogni colonna,
tutte le colonne e le righe visibili
nessuna riga vuota all'interno dell'intervallo
Eseguire prima le attività che non richiedono la modifica della colonna, ad esempio il controllo ortografico o le operazioni con Trova e sostituisci.
Successivamente, eseguire le attività che richiedono la modifica della colonna. I passaggi generali per la modifica di una colonna sono:
Inserire una nuova colonna (B) accanto alla colonna originale (A) da pulire.
Aggiungere una formula che trasformerà i dati nella parte superiore della nuova colonna (B).
Inserire la formula nella nuova colonna (B). In una tabella di Excel una colonna calcolata viene creata automaticamente con i valori inseriti.
Selezionare la nuova colonna (B), copiarla e incollarla come valori nella nuova colonna (B).
Rimuovere la colonna originale (A), che converte la nuova colonna da B ad A.


---

2. Controllo ortografia
Il correttore ortografico può essere usato non solo per trovare parole con errori di ortografia, ma anche valori usati in modo incoerente, ad esempio nomi di prodotto o società, aggiungendo tali valori a un dizionario personalizzato.


---

1985
Funzioni base (sinistra, destra, trova)
2013
Anteprima suggerita (flash fill)
2016
Introduzione di Power Query
2024
Funzioni regex native in cella
Evoluzione del testo in Excel

---

Cosa sono le regex
Una espressione regolare è un modello che definisce una sequenza di caratteri. Permette di cercare, validare e trasformare testi complessi con estrema precisione.
Perché usarle in Excel
Rispetto alle funzioni tradizionali, le regex offrono una flessibilità senza precedenti per gestire dati non strutturati in modo nativo e veloce.
Definizione e vantaggi

---

Le funzioni regex in Excel

---

Iniziamo con un caso intuitivo: cercare una parola o una cifra.
Pattern: mela
✓ Corrisponde a:
"Ho una mela rossa"
✗ Non corrisponde a:
"Ho una pera"
Pattern: \d
✓ Corrisponde a:
"Viale Roma 5"
✗ Non corrisponde a:
"Viale Roma"
UN ESEMPIO SEMPLICE

---

Mentre i caratteri letterali matchano se stessi, i metacaratteri definiscono set o comportamenti logici.
•
. : Qualsiasi carattere singolo.
•
[abc] : Classe di caratteri (a, b o c).
•
[^abc] : Qualsiasi cosa tranne a, b o c.
•
\ : Carattere di escape.
LETTERALI E METACARATTERI

---

CLASSI DI CARATTERI COMUNI

---

Quantità Fissa
{n} : Esattamente n volte.
{n,m} : Da n a m volte.
Esempio: \d{5} per un CAP.
Quantità Variabile
* : Zero o più volte.
+ : Una o più volte.
? : Zero o una volta.
I QUANTIFICATORI

---

^ : Matcher dell'inizio della stringa.
$ : Matcher della fine della stringa.
\b : Word Boundary.
| : Operatore OR (Alternanza).
ANCORAGGI E CONFINI

---

Le parentesi ( ) permettono di raggruppare parti del pattern per estrarle separatamente o applicare quantificatori.
Logica di Gruppo
Ogni gruppo riceve un indice numerico (1, 2, 3...) in base all'ordine di apertura delle parentesi.
Esempio: (\w+)\s(\d+)
Esempio Estrazione
Testo: "Mele 50"
Gruppo 1: Mele
Gruppo 2: 50
I GRUPPI DI CATTURA
=SOSTITUISCI.REGEX(A2; "(\d{+})"; ”più di $1")

---

3. Rimozione di righe duplicate

---

4. Ricerca e sostituzione di testo
È possibile rimuovere una stringa iniziale comune, ad esempio un'etichetta seguita da due punti e spazio o un suffisso, ad esempio una frase tra parentesi alla fine della stringa obsoleta o non necessaria. A questo scopo, è possibile trovare istanze del testo e quindi sostituirlo senza testo o altro testo.

---

Le nuove funzioni di testo in Excel

---

4. Ricerca e sostituzione di testo
Esercizio: con che formula si può verificare se una cella contiene un certo carattere?


=SE(VAL.NUMERO(RICERCA(“x”,A1),”SI”,”NO”)						// Case insensitive

=SE(VAL.NUMERO(TROVA(“x”,A1),”SI”,”NO”)						// Case sensitive

---

5. Modifica delle lettere maiuscole e minuscole del testo
INFERIORE(“Lorem Ipsum”) 		=> 		“lorem ipsum”

SUPERIORE(“Lorem Ipsum”)		=> 		“LOREM IPSUM”

MAIUSC.INIZ(“LOrEm ipSUm”)	=> 		“Lorem Ipsum”



---

6. Rimozione degli spazi
Seccatura COLOSSALE!

ANNULLA.SPAZI() toglie spazi in eccesso all’inizio, fine e in mezzo ad un testo.

---

7. Correzione di numeri
Il caso classico è quello di avere numeri salvati come testo.

Altro caso tipico è il caso di “numeri” che non sono in realtà numeri(non ha senso sommarli, sottrarli, etc..), come i NUMERI DI TELEFONO.

In questo caso spesso si deve ricondurli a uno stesso standard,
p.es 011 123 567 (e non (11) 123-456).

Colossale seccatura è la trasformazione del formato dei numeri:

1,234.56 => 1.234,56

---

9. Unione e divisione di colonne
Un'attività comune dopo l'importazione di dati da un'origine dati esterna consiste nell'unione di due o più colonne in una sola o nella divisione di una colonna in due o più colonne. 
Si vuole, ad esempio, dividere una colonna che contiene un nome completo in nome e cognome. Oppure dividere una colonna che contiene un campo di indirizzo in colonne separate con via e numero civico, città, area geografica e codice postale.

Altri valori comuni che possono richiedere l'unione in un'unica colonna o la divisione in più colonne sono: codici di prodotto, percorsi di file e indirizzi IP (Internet Protocol).

---

8. Correzione di date e ore
Il vero incubo… che raddoppia dovendo spostare i dati da e verso Google Sheet.

Primo grande problema: date salvate come testo.

Secondo problema: qual è il formato delle date?

Per le ore: che differenza c’è tra 12.15 e 12:15?


---

9. Unione e divisione di colonne
Operatori e funzioni rilevanti:
&
CONCATENA()
DESTRA(), SINISTRA(), LUNGHEZZA()

---

10. Trasformazione e ridisposizione di colonne e righe
La maggior parte delle caratteristiche di analisi e formattazione in Office Excel presuppongono la presenza dei dati in un'unica tabella normale bidimensionale.

A volte si potrebbe voler trasformare le righe in colonne e le colonne in righe. In altri casi, i dati non sono neanche strutturati in formato tabulare e potrebbe essere necessario convertirli da un formato non tabulare a uno tabulare.


---

10. Diritto da un film dell’orrore

---

Variabili
Ogni variabile deve formare una colonna distinta nel dataset.
Osservazioni
Ogni singola osservazione deve formare una riga dedicata.
Valori
Ogni tipo di unità osservazionale deve formare una tabella.
Tidy data: Le 3 Regole d'Oro

---

Efficienza Computazionale: Molti linguaggi (R, Python) sono ottimizzati per operazioni vettoriali su colonne.
Visualizzazione: Strumenti come ggplot2 o Seaborn richiedono dati in formato lungo (long format).
Integrità: Riduce drasticamente la probabilità di errori logici durante il filtraggio o l'aggregazione.
Standardizzazione: Permette di riutilizzare lo stesso codice su dataset diversi ma con la stessa struttura.
Perché la struttura conta?
Ordinamento, filtri, funzioni: in Excel non funzionano o funzionano male su dati ‘messy’


---

# Regressione logistica

**File:** `Regressione logistica.pptx`
**Tipo:** `.pptx`
**Dimensione:** 100.5 KB
**Ultima modifica:** 02/07/2026 09:24

---

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
Il prestito viene approvato?
💡  L'idea chiave
La regressione logistica non prevede direttamente Sì o No. Calcola la probabilità (tra 0 e 1) che l'evento accada.
Es: P(approvato) = 0,82 → molto probabile che venga approvato. Sopra una soglia (es. 0,5) → Sì.

---

La curva a S — sigmoid
A differenza della retta, la logistica produce sempre un valore tra 0 e 1
soglia 0,5
P(Sì)
1,0
0,0
Reddito →
❌  Rifiutato
✅  Approvato
Output sempre in [0, 1]
Non è mai negativa né superiore a 1 — è una probabilità.
Forma a S (sigmoid)
Sale lentamente, poi rapidamente al centro, poi si appiattisce di nuovo.
Soglia di decisione
P ≥ 0,5 → Sì. La soglia è modificabile in base al contesto.
Più variabili
Funziona come la multipla: ogni variabile ha il suo coefficiente.

---

La formula logistica
z  =  a  +  b₁·reddito  +  b₂·debiti  +  b₃·età
P(Sì)  =  1 / (1 + e⁻ᶻ)
z è il punteggio lineare (come nella regressione multipla). La sigmoid lo trasforma in probabilità.
b₁
reddito
b₁ > 0: reddito più alto → z aumenta →P(Sì) aumenta
b₂
debiti
b₂ < 0: debiti più alti → z diminuisce →P(Sì) diminuisce
b₃
età
b₃ > 0: età maggiore → storico più lungo →P(Sì) aumenta lievemente

---

Esempio numerico — dataset prestiti.xlsx
Supponiamo di aver ottenuto i seguenti coefficienti:
z = −2.5 + 0.00005·reddito − 0.00006·debiti + 0.02·età
Cliente
Reddito
Debiti
Età
z
P(Sì)
Decisione
A
€65.000
€8.000
45
1.32
0.79
✅ Approvato
B
€28.000
€42.000
31
−1.08
0.25
❌ Rifiutato
C
€45.000
€15.000
38
0.51
0.62
✅ Approvato
D
€22.000
€5.000
55
0.20
0.55
✅ Approvato
E
€50.000
€48.000
29
−0.70
0.33
❌ Rifiutato

---

Valutare il modello — la matrice di confusione
Come capire se il modello funziona bene?
Previsto: Sì
Previsto: No
Reale: Sì
Reale: No
38
Vero Positivo
(VP)
6
Falso Negativo
(FN)
9
Falso Positivo
(FP)
47
Vero Negativo
(VN)
Accuratezza
(VP + VN) / totale  = (38+47)/(38+47+6+9) = 85%
Quante previsioni sono corrette in totale
Precisione
VP / (VP + FP)  =  38/(38+9) = 81%
Tra chi prevediamo Sì, quanti sono davvero Sì
Recall
VP / (VP + FN)  =  38/(38+6) = 86%
Tra chi è davvero Sì, quanti prevediamo Sì

---

Perché dividere i dati in training e test?
Non basta che il modello funzioni bene sui dati che ha già visto
📚  Analogia: l'esame scolastico
Uno studente che memorizza le domande dell'anno scorso può risponderle tutte. Ma sa davvero la materia? Solo un esame con domande nuove lo rivela.
❌  Senza split — valutazione ingannevole
Il modello viene allenato su tutti i 100 clienti.
Viene valutato sugli stessi 100 clienti.

Risultato: accuratezza 95%

Ma il modello ha già visto ogni esempio durante il training. Non sappiamo se generalizza a nuovi clienti reali.

È come interrogare uno studente sulle stesse domande che ha studiato.
✅  Con split — valutazione onesta
80 clienti → training (il modello impara)
20 clienti → test (il modello non li ha mai visti)

Risultato: accuratezza 85% sul test

Questo 85% è una stima realistica di come il modello si comporterà su nuovi clienti in produzione.

È come un esame con domande nuove.

---

Come funziona il train/test split
Il dataset viene diviso casualmente in due parti prima di fare qualsiasi cosa
Dataset completo — 100 clienti
split casuale
Training set — 80 clienti (80%)
Test 20%
Il test set non si tocca
I dati di test devono restare nascosti fino alla valutazione finale. Usarli per scegliere i parametri del modello invalida i risultati.
Proporzione tipica: 80/20
80% training, 20% test è la proporzione più comune. Con dataset piccoli (< 100 righe) si può scendere a 70/30.
random_state — cos'è e perché serve
Lo split è casuale: ogni esecuzione sceglie 20 clienti diversi per il test.

random_state=42 blocca il generatore casuale su un valore fisso → il risultato è sempre lo stesso per tutti.

Il valore 42 non ha significato speciale: qualsiasi intero funziona. È una convenzione della comunità Python.

---

Regressione logistica in Python — Google Colab
1  Carica il dataset
import pandas as pd
df = pd.read_excel('prestiti.xlsx')
df.head()
2  Prepara le variabili
X = df[['eta','reddito_annuo',
        'debiti_totali']]
y = (df['prestito_approvato']=='Sì')
    .astype(int)
3  Split train / test
from sklearn.model_selection import
  train_test_split
X_tr,X_te,y_tr,y_te = train_test_split(
  X, y, test_size=0.2,
  random_state=42)
4  Allena il modello
from sklearn.linear_model import
  LogisticRegression
model = LogisticRegression()
model.fit(X_tr, y_tr)
5  Valuta le performance
from sklearn.metrics import
  accuracy_score, confusion_matrix
print(accuracy_score(y_te, model.predict(X_te)))
print(confusion_matrix(y_te, model.predict(X_te)))
6  Fai una previsione
nuovo = pd.DataFrame([[38, 45000, 15000]], columns=['eta', 'reddito_annuo', 'debiti_totali’])

prob = model.predict_proba(nuovo)[0][1]
print(f'P(approvato) = {prob:.2f}')

---

Esercizio  ·  prestiti.xlsx
100 clienti: età, reddito annuo, debiti totali, esito della richiesta di prestito.
1
Esplora il dataset: quanti prestiti sono stati approvati? Qual è il reddito medio degli approvati vs rifiutati?
2
Su Google Colab: carica il file, prepara X e y, esegui il train/test split (80/20)
3
Allena un modello LogisticRegression. Qual è l'accuratezza sul test set?
4
Stampa la matrice di confusione. Quanti falsi positivi e falsi negativi ci sono?
5
Stima la probabilità di approvazione per un cliente di 40 anni, reddito €50.000, debiti €12.000

---

Riepilogo — regressione logistica
🎯
La regressione logistica prevede la probabilità di un evento binario (Sì/No, 0/1)
📐
z è calcolato come nella regressione multipla; la sigmoid trasforma z in una probabilità tra 0 e 1
⚖️
La soglia di decisione (es. 0,5) converte la probabilità in una classe: sopra → Sì, sotto → No
📊
La matrice di confusione mostra VP, VN, FP, FN — accuratezza da sola non basta
Lineare: prevede un numero  ·  Logaritmica: relazione curva  ·  Multipla: più variabili  ·  Logistica: prevede Sì/No


---

# Teoria della visualizzazione

**File:** `Teoria della visualizzazione.pptx`
**Tipo:** `.pptx`
**Dimensione:** 115.6 KB
**Ultima modifica:** 02/07/2026 09:24

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
Stesso dato — trend immediato
 Pre-attentive
Il cervello processa forma e colore prima della lettura
Pattern visivi emergono in millisecondi
Carico cognitivo
Un grafico ben fatto riduce lo sforzo di interpretazione
La tabella richiede confronto mentale attivo
Memoria
Le immagini si ricordano meglio dei numeri (picture superiority effect)
Un'infografica dura nella memoria fino a 6 volte di più

---

Grammar of Graphics: i canali visivi
Ogni dato può essere codificato su canali visivi diversi. La scelta del canale determina quanto è facile leggerlo.
Posizione
Il canale più accurato
Usato da bar chart, scatter plot, line chart
Percezione immediata delle differenze
Lunghezza
Secondo canale per accuratezza
Bar chart orizzontali e verticali
Funziona solo con baseline comune (zero)
Colore (tonalità)
Ottimo per categorie (max 6-8)
Scarso per valori ordinali o continui
Attenzione a daltonismo e stampa B/N
Dimensione (area)
Bubble chart, treemap
Meno accurato di posizione e lunghezza
Le aree circolari sono spesso sottostimate
Forma
Solo per categorie (max 5-6)
Difficile distinguerne molte
Usata spesso in scatter plot
Saturazione / Intensità
Per valori quantitativi continui
Mappe di calore, choropleth
Sequential palette: da chiaro a scuro
Regola d'oro: usa posizione per il dato più importante. Aggiungi altri canali solo se necessario.

---

Come scegliere il grafico giusto: il framework delle 4 domande
Confronto
Sto comparando valori tra categorie o nel tempo?
→ Bar chart, grouped bar, line chart
Esempio: vendite per regione, trend annuale
Distribuzione
Com'è distribuito un valore nella popolazione?
→ Histogram, box plot, violin plot
Esempio: distribuzione voti, età clienti
Relazione
C'è correlazione tra due variabili?
→ Scatter plot, bubble chart, heatmap
Esempio: reddito vs. istruzione
Composizione
Come si compone un totale in parti?
→ Stacked bar, treemap, waffle chart
Evita il pie chart se >3 categorie
Domanda pratica da porsi prima di ogni grafico:
"Cosa voglio che il lettore confronti, veda, o capisca in 5 secondi?"

---

Errori comuni nella visualizzazione
Chartjunk
Effetti 3D, ombre, griglie inutili, clipart decorativi
Ogni pixel deve servire al dato(data-ink ratio, Tufte)
Rimuovi tutto ciò che non aggiunge informazione
Assi ingannevoli
Asse Y che non parte da zero altera la percezione
Scala logaritmica non dichiarata
Dual-axis con scale diverse = correlazioni false
Visual overloading
Troppi colori, troppi dataset nello stesso grafico
Il lettore non sa dove guardare
Regola: max 4-5 serie nello stesso grafico
Pie chart abusati
Difficile confrontare angoli non adiacenti
Con >4 categorie diventano illeggibili
Alternativa: bar chart orizzontale ordinato
Titoli assenti o generici
"Grafico 1" non è un titolo
Il titolo deve dichiarare il messaggio, non descrivere il grafico
Esempio: "Le vendite online crescono del 40% YoY"
Colori non accessibili
8% delle persone ha difficoltà a distinguere rosso/verde
Contrasto insufficiente per testo su sfondo colorato
Testa sempre con un simulatore di daltonismo
Data-ink ratio (Tufte): massimizza il rapporto ink utile / ink totale. Ogni tratto deve essere utile alla comunicazione.

---

Teoria del colore per la visualizzazione
Palette Sequenziale
Per dati ordinali o continui (es. temperatura, reddito)
dal chiaro al scuro
Palette Divergente
Per dati con punto centrale significativo (es. ±variazione, approvazione)
centro neutro, due estremi
Palette Categorica
Per categorie nominali (es. paesi, prodotti, segmenti)
colori distinti, uguale luminosità
Strumenti consigliati: ColorBrewer2.org · Coolors.co · Viz Palette (accessibilità)

---

Chiarezza visiva: titoli, etichette, annotazioni
Anatomia di un grafico chiaro
Titolo: messaggio principale (non descrizione)
Sottotitolo: fonte, unità di misura, periodo
Etichette assi: sempre presenti, concise
Legenda: vicina al dato, non isolata
Annotazioni efficaci
Annotazioni dirette > legenda separata
Evidenzia l'evento chiave (es. 'Lockdown Mar 2020')
Usa linee di riferimento per soglie importanti
Font size minimo 9pt per leggibilità
Tooltip e interattività
Per dashboard digitali: tooltip al passaggio del mouse
Non mettere nel tooltip dati già visibili nel grafico
Formato: Etichetta: valore (unità)
Esempio: titolo che informa vs titolo che descrive
✗  "Grafico delle vendite per trimestre"
Descrive il grafico, non dice nulla al lettore
✓  "Le vendite Q4 crescono del 23% nonostante l'inflazione"
Comunica il messaggio, il lettore sa cosa guardare
Gerarchia tipografica nel titolo:
Titolo 
Sottotitolo · Fonte  
Etichette assi  

---

Accessibilità nella visualizzazione
Progettare per tutti: daltonismo, bassa visione, stampa in B/N
8%
degli uomini ha daltonismo rosso-verde (deuteranopia/protanopia)
0.5%
delle donne ha daltonismo — meno diffuso ma non raro
4.5:1
rapporto di contrasto minimo WCAG AA per testo normale
Palette colorblind-safe
Evita rosso+verde insieme (il problema più comune)
Usa palette testate: Okabe-Ito, ColorBrewer, Viridis
Aggiungi sempre una variazione di forma o pattern
Testa con Coblis Color Blindness Simulator
Contrasto e leggibilità
Testo scuro su sfondo chiaro (o viceversa): ratio ≥ 4.5:1
Non usare solo il colore per trasmettere informazione critica
Etichette dirette sui dati > legenda separata per chi usa screen reader
Font min 10pt per grafici stampati
Palette Okabe-Ito (colorblind-safe):
Arancio
Cielo
Verde
Giallo
Blu
Rosso
Rosa
Nero

---

Recap: i 4 concetti chiave
1. Perché i grafici
Il cervello processa pattern visivi più velocemente dei numeri
Usa grafici quando vuoi mostrare trend, confronti o relazioni
Una tabella è meglio quando il lettore cerca valori precisi
2. Grammar of Graphics
Ogni variabile va mappata su un canale visivo:posizione > lunghezza > colore > dimensione
Scegli il canale più accurato per il dato più importante
Il tipo di grafico discende dalla domanda analitica (confronto, distribuzione, relazione, composizione)
3. Chiarezza e design
Titolo informativo, etichette chiare, legenda vicina al dato
Elimina il chartjunk: ogni pixel deve essere giustificato
Parti sempre da zero sull'asse Y se stai mostrando lunghezze
4. Accessibilità
Usa palette colorblind-safe (Okabe-Ito, Viridis, ColorBrewer)
Garantisci contrasto WCAG 4.5:1 per il testo
Non affidarti solo al colore: aggiungi forma, pattern o etichette dirette


---

# Testimonianza Francesco Ceriani

**File:** `Testimonianza Francesco Ceriani.pdf`
**Tipo:** `.pdf`
**Dimensione:** 562.7 KB
**Ultima modifica:** 02/07/2026 09:24

---

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
Oggi vedremo un caso reale di un luxury fashion retailer globale per capire, dal punto di vista della data governance, che la qualità del dato 
non è affatto scontata. I dati non sono “buoni” per definizione: diventano affidabili solo grazie a processi strutturati, regole chiare e 
responsabilità definite. Attraverso questo caso analizzeremo come i dati nascono, come vengono gestiti e perché solo dati di qualità 
permettono di prendere decisioni di business solide in un contesto competitivo come quello del luxury.
Case study


- Retail landscape -
Currencies8
Languages10
Till systems3
Countries12
Stores38
Diversi idiomi, caratteri 
speciali, tassonomia 
globale
Pipelines a diversi fusi 
orari, diverse regole 
fiscali, vincoli legali sui 
dati (GDPR)
Tassi cambio variano 
ogni giorno. Come fare 
report globale? E trend 
anno su anno?
Diverse strutture 
scontrini, ambiguita 
codici cliente/prodotti..
«La scalabilità di un sistema è la capacità di ampliarne le dimensioni senza aumentare la complessità»


- Data sources and architecture -
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
Sales
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
Marketing
• Gestione inventario
• Product ID
• Colour
• Size
• Category
• Stock availability
Products
• Utenti unici
• Sorgenti di traffico (eg
social media, paid ad, 
search engine)
• Durata sessione
• Velocità di caricamento
• Device
• Tasso di conversion
Website
• Staff ID
• Name
• Store/Department
• Start Date
• End Date
• Discount
HR • Età stimata
• Presenza di figli
• Livello istruzione
• Professione
• Fascia di reddito
• Valore immobiliare
della’rea di residenza
• Capacità di spesa
• …
3rd party

- Value chain, from raw data to decision -
• Dati incompleti o mal 
formattati
• Errori inserimento
manuale
• Standard diversi tra sistemi
• Misparsing (eg indirizzo)
Creazione del 
dato
• Interactive dashboard e 
report
• KPI standardizzati
• Storytelling
• Monitoraggio qualità dati
• Single source of truth
Visualization
• Decisioni strategiche
• Ottimizzazione processi
• Prioritizzazine investimenti
Decision
• Pipelines automation
• Normalizzazione
• Deduplicazione
• Arricchimento
• Data quality rules
• Creation of a cured data 
layer 
ETL 
• Pattern e trend detection
• Segmentazioni
• Analisi predittive
• Test e simulazioni
• Return of investment
Analysis
Data engineer
 Data engineer
 Data Analyst
 Data Scientist
Data Analyst
Management
Il dato nasce sporco per 
natura: è il processo che 
deve renderlo affidabile
Qui si forgia la qualità del 
dato
Good decisions don’t start 
from dashboards, but from 
clean and governed data
Qui il dato diventa semantica Qui si risponde a specifiche 
domande di business 
(PowerBI, Tableau, Looker..)(AWS, Azure, Databricks) (Python, SQL, Excel) 
(Export, Transform, Load)


- QA -



---

# Visualizzazione con Seaborn

**File:** `Visualizzazione con Seaborn.pptx`
**Tipo:** `.pptx`
**Dimensione:** 109.5 KB
**Ultima modifica:** 02/07/2026 09:24

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
Small multiples & faceting
hue / col / row
6
Curve di regressione
lmplot e regplot integrati

---

Seaborn vs Matplotlib — quando usare cosa
Matplotlib
Libreria di base — controllo totale su ogni pixel
Richiede codice verboso per grafici semplici
Ideale per: annotazioni personalizzate, layout complessi, output finale per report
Curva di apprendimento più ripida
Seaborn
Costruito su Matplotlib — sintassi di alto livello
Grafici statistici in una riga di codice
Integrazione nativa con DataFrame Pandas (formato tidy)
Ideale per: EDA, visualizzare distribuzioni e relazioni
💡  In pratica: usa Seaborn per esplorare i dati; aggiungi chiamate Matplotlib solo dove serve personalizzazione.

---

Il formato Tidy — la struttura dati che Seaborn si aspetta
La regola d'oro del formato Tidy:
1
Ogni colonna = una variabile
total_bill, tip, sex, smoker, day, time, size
2
Ogni riga = un'osservazione
Un pasto al ristorante
3
Ogni cella = un valore
No celle con elenchi, no colonne replicate
Perché è importante: se i dati non sono tidy, hue / col / row non funzionano.
# ❌ Formato WIDE (da Excel)
#  mancia_uomo  mancia_donna
#     2.50         3.00
#     1.75         4.50
# ✅ Formato TIDY
#  sex    tip
#  Male   2.50
#  Female 3.00
Per convertire wide → tidy in Pandas: usa pd.melt().  Esempio: pd.melt(df, id_vars=['day'], value_vars=['tip_m','tip_f'], var_name='sex', value_name='tip')

---

▶ Colab — Carica e ispeziona il dataset tips
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# ── 1. Caricare il dataset ────────────────────────────────────────
tips = sns.load_dataset('tips')

# ── 2. Struttura ─────────────────────────────────────────────────
print(tips.shape)           # (244, 7) → 244 pasti, 7 variabili
print(tips.dtypes)          # tipi: float64, category, object
print(tips.head())

# ── 3. Statistica descrittiva ────────────────────────────────────
tips.describe()

# ── 4. Conteggi per variabile categorica ─────────────────────────
print(tips['day'].value_counts())
print(tips['sex'].value_counts())

---

Temi e stili — set_theme, palette, contesto
Stile (sfondo)
whitegrid — griglia su sfondo bianco (default EDA)
darkgrid — griglia su sfondo scuro
white — sfondo bianco pulito
dark — sfondo scuro
ticks — solo tacche sugli assi
Contesto (scala)
paper — dimensioni ridotte
notebook — dimensioni standard (default)
talk — dimensioni medie per presentazioni
poster — dimensioni grandi
Palette colori
deep · muted · bright · pastel · dark · colorblind (qualitative)
Blues · Greens · Reds (sequenziale)
RdBu · coolwarm (divergente)
sns.color_palette('tab10', n_colors=5)
# Imposta tema globale — metti questa cella all'inizio del notebook
sns.set_theme(style='whitegrid', context='notebook', palette='deep')

# Per un singolo grafico con stile diverso:
with sns.axes_style('dark'):
    sns.histplot(tips['total_bill'])
Regola pratica: usa 'whitegrid' + 'notebook' per EDA, 'white' + 'talk' quando prepari grafici da inserire in presentazioni.

---

I tre plot universali — relplot · displot · catplot
Seaborn organizza i grafici in tre famiglie. Ogni funzione di alto livello accetta hue / col / row per i small multiples.
relplot
Relazioni tra variabili numeriche
scatter (default) — scatter plot
line — linee con banda di confidenza
sns.relplot(data=tips, x='total_bill', y='tip', kind='scatter', hue='sex')
displot
Distribuzioni di una o due variabili
hist — istogramma
kde — densità di kernel
ecdf — distribuzione cumulativa
sns.displot(data=tips, x='total_bill', kind='hist', hue='smoker', kde=True)
catplot
Variabili categoriche
strip · swarm — punti
box · violin · boxen — distribuzioni
bar · count · point — stime
sns.catplot(data=tips, x='day', y='tip', kind='box', hue='sex')

---

▶ Colab — Esercizio guidato: i tre plot universali
sns.set_theme(style='whitegrid', context='notebook', palette='deep')

# ── relplot: scatter total_bill vs tip ───────────────────────────
sns.relplot(data=tips, x='total_bill', y='tip',
            kind='scatter', hue='sex', col='time')
plt.show()

# ── displot: distribuzione total_bill ────────────────────────────
sns.displot(data=tips, x='total_bill', kind='hist',
            hue='smoker', kde=True, bins=20)
plt.show()

# ── catplot: tip per giorno della settimana ───────────────────────
sns.catplot(data=tips, x='day', y='tip',
            kind='box', hue='sex',
            order=['Thur','Fri','Sat','Sun'])
plt.show()

# Domanda: cosa noti confrontando pranzo (Lunch) e cena (Dinner)?

---

Small multiples e faceting — hue / col / row
Seaborn crea automaticamente griglie di grafici con tre parametri:
hue=
Colore diverso per ogni categoria — sullo stesso grafico
hue=
col=
Una colonna per ogni categoria — grafici affiancati in orizzontale
col=
row=
row=
Una riga per ogni categoria — grafici impilati in verticale
# hue soltanto → un grafico con colori diversi per fumatori/non fumatori
sns.relplot(data=tips, x='total_bill', y='tip', hue='smoker')

# col → due grafici affiancati (Lunch | Dinner)
sns.relplot(data=tips, x='total_bill', y='tip', hue='sex', col='time')

# col + row → griglia 2×2  (time × smoker)
sns.relplot(data=tips, x='total_bill', y='tip',
            hue='sex', col='time', row='smoker')
⚠  col_wrap=N limita il numero di colonne quando una variabile ha molti livelli. Esempio: col='day', col_wrap=2  → 2 colonne invece di 4.
sns.relplot(data=tips, x='total_bill', y='tip', hue='sex', col='day', col_wrap=2)

---

pairplot — matrice di scatter per l'analisi esplorativa
sns.pairplot() produce una griglia N×N: scatter tra ogni coppia di variabili numeriche, distribuzione sulla diagonale.
Diagonale
Distribuzione di ogni variabile(istogramma o KDE)
Triangolo inferiore
Scatter tra ogni coppia di variabili
hue=
Colora i punti per categoria —mostra cluster e separazione
# Base — tutte le variabili numeriche
sns.pairplot(tips)

# Con colore per categoria
sns.pairplot(tips, hue='sex')

# Solo triangolo inferiore (meno ridondante)
sns.pairplot(tips, hue='sex', corner=True)
# Seleziona variabili specifiche + KDE sulla diagonale
sns.pairplot(tips, vars=['total_bill', 'tip', 'size'], diag_kind='kde', hue='smoker')
⚠  Su dataset con molte colonne pairplot diventa lento e illeggibile. Seleziona le variabili rilevanti con vars=['col1','col2',...]

---

Curve di regressione — lmplot e regplot
Seaborn calcola e disegna la retta di regressione (con banda di confidenza al 95%) in automatico:
regplot
Grafico singolo — restituisce un asse Matplotlib.
Adatto quando vuoi aggiungere elementi con Matplotlib.
sns.regplot(data=tips, x='total_bill', y='tip',
           scatter_kws={'alpha': 0.4},
           line_kws={'color': 'red'})
lmplot
Figure-level — supporta hue / col / row.
Crea una figura autonoma (FacetGrid).
sns.lmplot(data=tips, x='total_bill', y='tip',
          hue='smoker', col='time')
# Regressione polinomiale di grado 2 (order=2)
sns.regplot(data=tips, x='total_bill', y='tip', order=2)
# Lowess (non parametrica, nessuna assunzione lineare)
sns.regplot(data=tips, x='total_bill', y='tip', lowess=True)
La banda grigia attorno alla retta è l'intervallo di confidenza al 95% stimato. Più è larga, meno dati ci sono in quella zona.Disabilita con ci=None per velocizzare la visualizzazione su dataset grandi.
sns.lmplot(data=tips, x='total_bill', y='tip', hue='smoker', col='time', ci=95)

---

▶ Colab — Esercizio: regressione e small multiples
# ── 1. lmplot con hue + col ──────────────────────────────────────
sns.lmplot(data=tips, x='total_bill', y='tip',
           hue='smoker', col='time',
           height=4, aspect=0.9)
plt.suptitle('Mancia vs Conto: fumatori vs non fumatori (pranzo|cena)',
             y=1.02)
plt.show()

# ── 2. catplot violin: distribuzione mancia per giorno ──────────
sns.catplot(data=tips, x='day', y='tip',
            kind='violin', hue='sex', split=True,
            order=['Thur','Fri','Sat','Sun'],
            height=4, aspect=1.5)
plt.show()

# ── 3. displot KDE: distribuzione conto per giorno ──────────────
sns.displot(data=tips, x='total_bill',
            kind='kde', hue='day',
            fill=True, alpha=0.4)
plt.show()

# → Quale giorno ha la distribuzione più asimmetrica?

---

Esercizio — Analisi esplorativa del dataset tips
1. Carica e ispeziona
Carica tips. Quante righe e colonne ci sono? Quali variabili sono categoriche? Usa .dtypes e .describe().
2. Distribuzione delle mance
Crea un displot (kind='hist', kde=True) della colonna tip. Poi separa per smoker con hue='smoker'. La distribuzione cambia?
3. Small multiples
Con relplot, visualizza total_bill vs tip usando hue='sex' e col='time'. Commenta: la relazione cambia tra pranzo e cena?
4. Regressione
Usa lmplot per aggiungere la retta di regressione al grafico precedente. Aggiungi col='smoker' per creare una griglia 2×2.

---

Recap — 4 concetti chiave da ricordare
1
Seaborn = Matplotlib semplificato
Grafici statistici in una riga. Per personalizzazioni avanzate, usa direttamente le API Matplotlib sull'Axes restituito.
2
I tuoi dati devono essere Tidy
Una riga = un'osservazione, una colonna = una variabile. Senza formato tidy, hue/col/row non funzionano.
3
Tre famiglie coprono quasi tutto
relplot → relazioni numerichedisplot → distribuzionicatplot → categoricheOgni famiglia supporta small multiples.
4
hue / col / row = small multiples
Tre parametri per confrontare sottogruppi senza scrivere loop. col_wrap limita le colonne per variabili con molti livelli.
Seaborn: sns.relplot · sns.displot · sns.catplot · sns.lmplot — dataset tips


---

# Visualizzazione e storytelling

**File:** `Visualizzazione e storytelling.pptx`
**Tipo:** `.pptx`
**Dimensione:** 95.2 KB
**Ultima modifica:** 02/07/2026 09:24

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
Elimina il rumore visivo
Progettata per suscitare una reazione
La stessa dashboard HR che avete costruito può diventare una storia.
La differenza non è nei dati — è nelle scelte editoriali: cosa metti in primo piano, cosa elimini, quale titolo usi.
VS
❌ Titolo dashboard: "Attrition by Department"
✅ Titolo storia: "HR perde 1 dipendente su 3: il problema è sistemico"

---

La struttura del data storytelling: Context → Insight → Action
01  CONTEXT
Dove siamo?
Chi è l'audience?
Qual è la situazione di partenza?

Es.: L'azienda registra un tasso
di attrition del 23% — sopra
la media del settore (15%).
▶
02  INSIGHT
Cosa rivela davvero il dato?
Perché è sorprendente o rilevante?

Es.: Il problema non è uniforme:
HR ha un attrition del 36%,
quasi 3× rispetto a R&D (12%).
▶
03  ACTION
Cosa deve fare l'audience?
Quale decisione è facilitata?

Es.: Prioritizzare interventi
di retention nell'HR:
job satisfaction e retribuzione.
Ogni visual nella storia corrisponde a uno di questi tre momenti. Se non sai dove collocare un grafico, probabilmente non serve.

---

Applicazione al dataset HR: identificare l'insight
I dati grezzi non parlano da soli. Serve una domanda.
La storia scelta per l'esercizio:
CONTEXT: Attrition 23%
nel complesso
INSIGHT: HR al 36% —
3× rispetto a R&D
ACTION: Intervenire su
stipendio e soddisfazione

---

Cosa mostrare e cosa nascondere: tecniche di focus visivo
Riduci il rumore
Elimina le variabili non rilevanti per l'insight
Rimuovi la legenda se c'è un solo colore per la storia
Accorcia i titoli degli assi (o toglili se sono ovvi)
Non mostrare ogni categoria — aggrega o filtra
Evidenzia il punto chiave
Usa un solo colore accentato su sfondo grigio
Annota direttamente sul grafico (evita la legenda)
Usa il titolo come claim, non come etichetta
Aggiungi una linea di riferimento (media, target)
Il titolo come claim: la regola più importante
❌ Titolo descrittivo:
"Attrition rate per dipartimento"
→ Descrive il grafico, non dice nulla
✅ Titolo come claim:
"HR perde 1 dipendente su 3: il triplo di R&D"
→ Dice già la conclusione
In Seaborn: usa ax.set_title() per il claim, ax.axhline() per la linea di riferimento, ax.annotate() per le note.
ax.set_title('HR perde 1 dipendente su 3: il triplo di R&D', fontsize=13, fontweight='bold', color='#C0392B')
ax.axhline(y=attrition_media, color='gray', linestyle='--', linewidth=1, label=f'Media: {attrition_media:.0%}')
ax.annotate('HR', xy=(0, 35.7), xytext=(0.3, 38), fontsize=10, color='#C0392B', fontweight='bold')

---

Codice Seaborn — Visual 1 (Context): Attrition rate complessivo
Visual 1 di 3 — CONTEXT: mostra la dimensione del problema
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Carica il dataset (carica HR_Analytics_Dashboard.xlsx su Colab prima)
df = pd.read_excel('HR_Analytics_Dashboard.xlsx', sheet_name='Dati_Grezzi')

# Prepara i dati
attrition_counts = df['Attrition'].value_counts()
total = len(df)
rate = (attrition_counts['Yes'] / total) * 100

fig, ax = plt.subplots(figsize=(7, 4))
colors = ['#C0392B' if v == 'Yes' else '#BDD7EE' for v in attrition_counts.index]
sns.barplot(x=attrition_counts.index, y=attrition_counts.values, palette=colors, ax=ax)

# Titolo come claim
ax.set_title(f'Il 23% dei dipendenti ha lasciato l\'azienda — sopra la media di settore',
             fontsize=12, fontweight='bold', color='#1A1A2E', pad=12)
ax.set_xlabel(''); ax.set_ylabel('N. dipendenti')
ax.annotate(f'{rate:.0f}%', xy=(0, attrition_counts['Yes']),
            xytext=(0, attrition_counts['Yes'] + 0.5),
            fontsize=14, fontweight='bold', color='#C0392B', ha='center')
sns.despine(); plt.tight_layout(); plt.show()

---

Codice Seaborn — Visual 2 (Insight): Attrition per dipartimento
Visual 2 di 3 — INSIGHT: il problema non è uniforme — HR è anomalo
# Calcola attrition rate per dipartimento
dept = df.groupby('Department')['AttritionNum'].agg(['sum','count']).reset_index()
dept['rate'] = dept['sum'] / dept['count'] * 100
media_globale = df['AttritionNum'].mean() * 100

# Ordina per rate decrescente
dept = dept.sort_values('rate', ascending=False)

# Colore: rosso per HR (anomalia), grigio per gli altri
colors = ['#C0392B' if d == 'Human Resources' else '#BDD7EE' for d in dept['Department']]

fig, ax = plt.subplots(figsize=(7, 4))
sns.barplot(data=dept, x='Department', y='rate', palette=colors, ax=ax)

# Linea media + annotazione
ax.axhline(y=media_globale, color='#595959', linestyle='--', linewidth=1.2)
ax.text(2.35, media_globale + 0.8, f'Media: {media_globale:.0f}%', fontsize=9, color='#595959')

# Titolo come claim + etichette valori
ax.set_title('HR perde 1 dipendente su 3: il triplo di R&D', fontsize=12,
             fontweight='bold', color='#C0392B', pad=12)
for p in ax.patches:
    ax.annotate(f'{p.get_height():.0f}%', (p.get_x() + p.get_width()/2, p.get_height()),
                ha='center', va='bottom', fontsize=11, fontweight='bold')
ax.set_xlabel(''); ax.set_ylabel('Attrition rate (%)'); sns.despine()
plt.tight_layout(); plt.show()

---

Codice Seaborn — Visual 3 (Action): Soddisfazione e stipendio in HR
Visual 3 di 3 — ACTION: le leve su cui intervenire in HR
# Filtra solo HR e confronta chi è rimasto vs chi se ne è andato
hr = df[df['Department'] == 'Human Resources'].copy()

# Calcola medie di JobSatisfaction e MonthlyIncome per gruppo Attrition
hr_agg = hr.groupby('Attrition')[['JobSatisfaction', 'MonthlyIncome']].mean().reset_index()

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Grafico 1: Job Satisfaction
colors_att = ['#1E8449' if a == 'No' else '#C0392B' for a in hr_agg['Attrition']]
sns.barplot(data=hr_agg, x='Attrition', y='JobSatisfaction',
            palette=colors_att, ax=axes[0])
axes[0].set_title('Job Satisfaction\n(rimasti vs usciti)', fontsize=11, fontweight='bold')
axes[0].set_ylim(0, 4); axes[0].set_xlabel(''); axes[0].set_ylabel('Soddisfazione (1-4)')
sns.despine(ax=axes[0])

# Grafico 2: Monthly Income
sns.barplot(data=hr_agg, x='Attrition', y='MonthlyIncome',
            palette=colors_att, ax=axes[1])
axes[1].set_title('Stipendio mensile medio\n(rimasti vs usciti)', fontsize=11, fontweight='bold')
axes[1].set_xlabel(''); axes[1].set_ylabel('Stipendio (€)')
sns.despine(ax=axes[1])

fig.suptitle('In HR chi se ne va guadagna meno ed è meno soddisfatto',
             fontsize=12, fontweight='bold', color='#1B5F8C', y=1.02)
plt.tight_layout(); plt.show()

---

Esercizio: costruisci la tua storia in 3 visual
⏱  15 minuti — lavoro individuale, poi presentazione al partner (5 min)
01
Scegli il tuo insight
Usa il dataset HR_Analytics_Dashboard.xlsx
Trova UNA domanda che produce una risposta sorprendente
Non usare l'esempio HR/attrition già mostrato
Esempi: overtime vs attrition, età vs soddisfazione, anzianità vs income
02
Costruisci i 3 visual con Seaborn
Visual 1 — Context: mostra il dato di partenza
Visual 2 — Insight: evidenzia l'anomalia o il pattern
Visual 3 — Action: mostra la leva su cui agire
Usa titoli come claim, annota i punti chiave
03
Presenta al partner (5 min ciascuno)
Racconta la storia in sequenza: context → insight → action
Il partner deve capire il messaggio senza guardare il codice
Feedback: il titolo dice già la conclusione?
Cosa toglieresti per rendere il messaggio più chiaro?
Dataset: HR_Analytics_Dashboard.xlsx  |  Strumento: Google Colab + Seaborn

---

Recap: quello che conta davvero nel data storytelling
Una storia non è una dashboard
La dashboard esplora, la storia convince.
Seleziona, ordina, elimina il rumore.
Context → Insight → Action
Ogni visual ha un posto nella sequenza.
Se non sai dove collocarlo, probabilmente non serve.
Il titolo è il messaggio
Non descrivere il grafico: dì già la conclusione.
"HR perde 1 su 3" vale più di "Attrition by Department".
Meno è più
Un colore accentato, una linea di riferimento, zero legende inutili.
Seaborn: set_title, axhline, annotate, despine.
Storytelling = scegliere cosa dire, a chi, e in quale ordine  |  Dataset: HR Analytics


---

# Visualizzazione per Big Data

**File:** `Visualizzazione per Big Data.pptx`
**Tipo:** `.pptx`
**Dimensione:** 155.8 KB
**Ultima modifica:** 02/07/2026 09:24

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
Migliaia di punti si sovrappongono nello stesso pixel. Il grafico mostra una massa opaca: non vediamo densità, outlier, né distribuzione reale.
Rendering limit
Browser e librerie hanno un limite pratico: oltre 100k–500k marker il rendering rallenta o fallisce. Con Seaborn su Colab: crash o attesa di minuti.
Aggregation loss
Se aggreghiamo male (es. media mensile su dati orari) perdiamo i picchi, la varianza e i pattern stagionali. L’informazione è distrutta, non solo nascosta.
Dataset usato: foglio '1_Overplotting_Scatter'  (5.000 righe età–salario)

---

1. Overplotting — il problema visivo
scatter() standard  —  5.000 punti
Età (anni)
Problema: non si capisce dove sono concentrati i dati
hexbin()  —  stessi dati, densità visibile
bassa densità
alta densità
Soluzione: la densità emerge chiaramente

---

2. Sampling vs Aggregation — due strategie diverse
Di fronte a 50 milioni di righe: estraggo un sottoinsieme (sampling) o riassumo tutto (aggregation)?
SAMPLING
Cosa fa: 
Seleziona un sottoinsieme casuale (es. 1% dei dati)
Quando usarlo: 
Esplorazione iniziale, scatter plot, verifica distribuzione
Vantaggio: 
Mantiene la forma della distribuzione originale
Rischio: 
Gli outlier rari possono sparire dal campione
AGGREGATION
Cosa fa: 
Calcola statistiche su gruppi (media, conteggio, somma)
Quando usarlo: 
Dashboard, trend temporali, confronti per categoria
Vantaggio: 
Scala a miliardi di righe, risultato sempre leggibile
Rischio: 
Nasconde varianza e distribuzioni interne ai gruppi

---

2. Aggregation loss — quando aggregare fa perdere informazione
Scenario: vendite giornaliere 3 anni (foglio '2_Aggregation_Sales', 1.095 righe). Cosa succede se aggreghiamo a livelli diversi?
Dati giornalieri (raw)
1.095 punti — troppo rumore per capire il trend
Difficile
Aggregato mensile
36 punti — trend stagionale visibile, varianza nascosta
Buono
Aggregato annuale
3 punti — trend visibile ma tutto il dettaglio perso
Troppo poco
Regola pratica: aggregare al livello più fine che permette ancora una lettura chiara. Poi offrire drill-down.

---

3. Chart types per grandi dataset — panoramica
Heatmap  —  Correlazioni e pattern 2D
Quando: due variabili categoriali o binned. Es: voto vs ore_studio per corso.
sns.heatmap(pivot_df, annot=True, cmap='Blues')
Hexbin / Jointplot  —  Scatter ad alta densità
Quando: due variabili continue, milioni di punti. Sostituisce scatter.
sns.jointplot(data=df, x='age', y='salary', kind='hex')
KDE — Density Plot  —  Distribuzione continua stimata
Quando: capire la forma della distribuzione su grandi campioni.
sns.kdeplot(data=df, x='weight', hue='gender', fill=True)
Histogram binned  —  Frequenze per intervallo
Quando: distribuzione di una variabile continua. Scegliere bins con cura.
sns.histplot(data=df, x='age', bins=30, kde=True)

---

3. Heatmap — leggere la densità su due dimensioni
Come funziona
1
Divide entrambe le variabili in bin (intervalli discreti)
2
Conta quante osservazioni cadono in ogni cella
3
Mappa il conteggio su una scala di colore
4
Il risultato è leggibile anche con milioni di punti
import seaborn as sns, pandas as pd
df = pd.read_excel('bigdata_viz_datasets.xlsx',
                   sheet_name='3_Heatmap_Students')
pivot = df.groupby(['Ore_Studio_Sett',
         'Voto_Esame']).size().unstack()
sns.heatmap(pivot, cmap='Blues')
Ore Studio (bin)
0-5
5-10
10-15
15-20
20-25
25-30
18-20
20-22
22-24
24-26
26-28
28-30
Voto Esame
pochi studenti
molti studenti
Dataset: '3_Heatmap_Students'  (2.000 studenti, ore_studio × voto_esame)

---

3. KDE e Histogram binned — distribuzioni a scala
Kernel Density Estimate (KDE)
Maschi
Femmine
Altezza (cm)
La KDE stima la funzione di densità di probabilità smussando l'istogramma. Con fill=True e hue puoi confrontare gruppi sovrapposti su milioni di osservazioni.
sns.kdeplot(data=df, x='Altezza_cm',
            hue='Genere', fill=True,
            palette=['steelblue','crimson'])
Histogram binned
Salario (€)
L'istogramma binned conta le frequenze per intervallo. Il parametro bins controlla la risoluzione: troppo pochi → perde dettaglio; troppi → rumore.
sns.histplot(data=df, x='Salario (€)',
             bins=40, kde=True,
             color='steelblue')
Dataset: '1_Overplotting_Scatter' e '4_Sampling_Demo'

---

4. Datashader — visualizzare miliardi di punti
Seaborn/Matplotlib disegnano ogni punto — con 100M punti crollano. Datashader li rasterizza prima di renderizzare.
1
Rasterizza
Divide il canvas in una griglia di pixel. Per ogni punto calcola in quale pixel cade.
→
2
Aggrega
Conta (o calcola media/somma) dei punti per pixel. Operazione vettorizzata: scala a miliardi.
→
3
Colora
Applica una colormap alla griglia aggregata. Produce un'immagine PNG — non punti vettoriali.
import datashader as ds
import datashader.transfer_functions as tf

canvas = ds.Canvas(plot_width=800, plot_height=600)
agg    = canvas.points(df, 'Età', 'Salario (€)')
img    = tf.shade(agg, cmap=['lightblue','darkblue'])
img    # display in notebook
Note per questo corso
pip install datashader  necessario su Colab
API diversa da Seaborn
Per esplorazione: hexbin è sufficiente

---

5. Progressive disclosure — aggregati + drill-down
Principio UX: mostrare prima il riassunto, poi permettere all'utente di approfondire il dettaglio che gli interessa.
Livello 1 — KPI globale
Totale vendite annuali: 1 numero
▼
Livello 2 — Trend mensile
Line chart aggregato: 12–36 punti visibili
▼
Livello 3 — Dettaglio per area
Heatmap per regione × mese: pattern locali
▼
Livello 4 — Dati grezzi (drill)
Tabella filtrata: singole transazioni su richiesta
Collegamento con il Modulo 3.3 (Dashboard): ogni livello corrisponde a un componente della dashboard — KPI card, line chart, heatmap, data table con filtro.

---

Esercizio  —  Da scatter a hexbin su Google Colab
Dataset: '1_Overplotting_Scatter'  (5.000 righe — Età, Salario, Settore)
1
Crea lo scatter standard
Plotta Età (asse X) vs Salario (asse Y) con sns.scatterplot(). Osserva l'overplotting.
sns.scatterplot(data=df, x='Età', y='Salario (€)', alpha=0.3)
2
Campiona e riprova
Prendi un campione casuale di 500 righe (df.sample(500)). Il grafico migliora? Perdi informazione?
df_s = df.sample(500, random_state=42)
sns.scatterplot(data=df_s, x='Età', y='Salario (€)')
3
Hexbin plot
Usa sns.jointplot(kind='hex') sull'intero dataset. Dove si concentrano i dati?
sns.jointplot(data=df, x='Età', y='Salario (€)', kind='hex', cmap='Blues')
4
KDE per settore
Usa sns.kdeplot() per confrontare la distribuzione del salario nei 5 settori.
sns.kdeplot(data=df, x='Salario (€)', hue='Settore', fill=True)

---

Recap  —  4 concetti chiave
1
I grafici standard non gestiscono troppi dati
Overplotting, rendering limit e aggregation loss rendono i chart classici inutili oltre i 50–100k punti. Il problema non è estetico: è informativo.
2
Sampling e aggregation hanno trade-off diversi
Il sampling preserva la forma ma perde outlier rari. L'aggregation scala a miliardi ma nasconde varianza. Scegliere in base all'obiettivo.
3
Hexbin, KDE e heatmap sono gli strumenti giusti
Sostituiscono scatter e bar chart quando i punti sono troppi. Tutti disponibili in Seaborn con un parametro kind o una funzione dedicata.
4
Progressive disclosure = aggregati + drill-down
Mostrare KPI → trend → dettaglio → dati grezzi. Tecnica chiave per dashboard e storytelling su grandi dati. Per dati estremi: Datashader.
Big Data Viz: scegli il chart type giusto → scala → preserva l'informazione → guida il lettore dal KPI al dettaglio


---

# Visualizzazione

**File:** `Visualizzazione.xlsx`
**Tipo:** `.xlsx`
**Dimensione:** 19.0 KB
**Ultima modifica:** 02/07/2026 09:24

---

## Sheet: Dati_Grezzi

EmployeeID | Age | Gender | Department | JobRole | MonthlyIncome | OverTime | YearsAtCompany | YearsWithCurrManager | JobSatisfaction | EnvironmentSatisfaction | WorkLifeBalance | Attrition | AttritionNum
1001 | 23 | Female | Human Resources | Human Resources | 5526 | Yes | 17 | 1 | 4 | 1 | 1 | Yes | 1
1002 | 23 | Male | Sales | Manager | 6821 | No | 17 | 6 | 2 | 4 | 3 | No | 0
1003 | 49 | Female | Sales | Sales Executive | 5818 | No | 3 | 1 | 4 | 1 | 3 | No | 0
1004 | 24 | Female | Human Resources | Manager | 6528 | No | 12 | 1 | 3 | 3 | 2 | No | 0
1005 | 36 | Female | Sales | Manager | 8936 | No | 12 | 4 | 4 | 3 | 2 | No | 0
1006 | 39 | Male | Sales | Manager | 5726 | No | 5 | 5 | 2 | 2 | 4 | No | 0
1007 | 42 | Male | Human Resources | Human Resources | 5550 | No | 8 | 1 | 2 | 3 | 2 | No | 0
1008 | 31 | Female | Research & Development | Manufacturing Director | 6879 | Yes | 17 | 8 | 3 | 4 | 4 | No | 0
1009 | 53 | Male | Sales | Manager | 6108 | Yes | 5 | 5 | 4 | 1 | 4 | No | 0
1010 | 57 | Male | Research & Development | Healthcare Representative | 3521 | No | 3 | 3 | 3 | 3 | 1 | No | 0
1011 | 22 | Female | Sales | Sales Representative | 8501 | No | 3 | 3 | 3 | 2 | 2 | No | 0
1012 | 55 | Male | Sales | Manager | 5553 | No | 15 | 0 | 1 | 3 | 3 | Yes | 1
1013 | 27 | Male | Sales | Manager | 5686 | No | 17 | 12 | 2 | 2 | 4 | No | 0
1014 | 55 | Female | Sales | Sales Representative | 3257 | No | 17 | 12 | 2 | 3 | 4 | No | 0
1015 | 50 | Female | Human Resources | Manager | 6275 | No | 18 | 8 | 2 | 2 | 1 | Yes | 1
1016 | 36 | Male | Human Resources | Human Resources | 6237 | No | 10 | 1 | 2 | 3 | 4 | Yes | 1
1017 | 58 | Female | Sales | Manager | 6074 | No | 3 | 1 | 4 | 3 | 4 | No | 0
1018 | 28 | Male | Human Resources | Human Resources | 7196 | No | 10 | 10 | 1 | 2 | 2 | Yes | 1
1019 | 49 | Male | Research & Development | Laboratory Technician | 6297 | No | 14 | 12 | 1 | 1 | 1 | No | 0
1020 | 48 | Female | Sales | Sales Executive | 7119 | No | 12 | 0 | 2 | 4 | 1 | No | 0
1021 | 40 | Female | Research & Development | Manufacturing Director | 5700 | No | 15 | 2 | 2 | 3 | 2 | No | 0
1022 | 42 | Male | Human Resources | Human Resources | 3206 | Yes | 15 | 8 | 2 | 1 | 1 | No | 0
1023 | 26 | Male | Sales | Manager | 3058 | No | 18 | 9 | 1 | 1 | 4 | No | 0
1024 | 38 | Male | Human Resources | Manager | 7532 | No | 10 | 3 | 3 | 4 | 2 | No | 0
1025 | 42 | Male | Research & Development | Manufacturing Director | 8586 | No | 3 | 1 | 2 | 3 | 2 | No | 0
1026 | 45 | Female | Sales | Sales Executive | 6122 | Yes | 17 | 11 | 3 | 1 | 3 | No | 0
1027 | 38 | Male | Sales | Sales Executive | 7900 | Yes | 9 | 9 | 2 | 3 | 2 | No | 0
1028 | 38 | Male | Research & Development | Manufacturing Director | 4921 | Yes | 13 | 4 | 1 | 1 | 3 | No | 0
1029 | 32 | Female | Human Resources | Manager | 3998 | Yes | 2 | 2 | 2 | 1 | 3 | No | 0
1030 | 30 | Male | Sales | Sales Representative | 5494 | No | 1 | 1 | 2 | 2 | 1 | No | 0
1031 | 31 | Male | Human Resources | Manager | 8204 | No | 13 | 0 | 2 | 3 | 4 | No | 0
1032 | 39 | Male | Human Resources | Human Resources | 2500 | No | 3 | 3 | 1 | 4 | 2 | Yes | 1
1033 | 41 | Male | Research & Development | Healthcare Representative | 6873 | No | 8 | 1 | 3 | 3 | 4 | No | 0
1034 | 23 | Male | Human Resources | Manager | 7671 | No | 8 | 2 | 3 | 1 | 1 | No | 0
1035 | 49 | Male | Research & Development | Healthcare Representative | 5023 | Yes | 13 | 0 | 2 | 3 | 4 | Yes | 1
1036 | 42 | Male | Human Resources | Manager | 6798 | No | 9 | 8 | 3 | 4 | 3 | No | 0
1037 | 34 | Female | Research & Development | Laboratory Technician | 5753 | No | 5 | 5 | 3 | 4 | 1 | No | 0
1038 | 42 | Female | Sales | Sales Representative | 4739 | No | 6 | 6 | 4 | 2 | 1 | No | 0
1039 | 27 | Male | Human Resources | Manager | 5001 | Yes | 0 | 0 | 2 | 4 | 1 | Yes | 1
1040 | 46 | Female | Human Resources | Human Resources | 4553 | No | 4 | 4 | 1 | 1 | 4 | Yes | 1
1041 | 25 | Male | Human Resources | Manager | 6162 | Yes | 14 | 10 | 3 | 4 | 4 | No | 0
1042 | 32 | Female | Human Resources | Manager | 5121 | No | 7 | 7 | 3 | 4 | 2 | No | 0
1043 | 40 | Male | Sales | Manager | 5820 | No | 4 | 2 | 2 | 4 | 2 | No | 0
1044 | 48 | Female | Sales | Sales Representative | 7304 | No | 13 | 0 | 2 | 4 | 4 | No | 0
1045 | 58 | Female | Human Resources | Human Resources | 2500 | No | 12 | 6 | 2 | 4 | 2 | Yes | 1
1046 | 46 | Female | Research & Development | Research Scientist | 7017 | No | 12 | 11 | 2 | 4 | 2 | No | 0
1047 | 47 | Male | Human Resources | Human Resources | 6871 | No | 5 | 0 | 3 | 4 | 3 | No | 0
1048 | 46 | Female | Research & Development | Healthcare Representative | 7298 | No | 13 | 4 | 1 | 4 | 1 | No | 0
1049 | 36 | Male | Sales | Sales Representative | 6424 | No | 7 | 3 | 1 | 2 | 2 | Yes | 1

## Sheet: KPI_Summary

METRICHE GLOBALI |  |  | 
Totale dipendenti | 70 |  | 
Di cui con Attrition=Yes | 16 |  | 
Attrition Rate | 0.228571428571429 |  | 
Età media | 40.2 |  | 
Stipendio mensile medio | 6018.85714285714 |  | 
% dipendenti con Overtime | 0.185714285714286 |  | 
Anni medi in azienda | 10.3285714285714 |  | 
Job Satisfaction media | 2.4 |  | 
ATTRITION PER DIPARTIMENTO |  |  | 
Dipartimento | Totale | Attriti | Attrition %
Sales | 26 | 4 | 0.153846153846154
Research & Development | 16 | 2 | 0.125
Human Resources | 28 | 10 | 0.357142857142857
ATTRITION PER GENERE |  |  | 
Genere | Totale | Attriti | Attrition %
Male | 43 | 10 | 0.232558139534884
Female | 27 | 6 | 0.222222222222222
TREND ATTRITION MENSILE (dati simulati) |  |  | 
Mese | Attrition % |  | 
Gen | 0.124 |  | 
Feb | 0.131 |  | 
Mar | 0.138 |  | 
Apr | 0.142 |  | 
Mag | 0.149 |  | 
Giu | 0.155 |  | 
Lug | 0.152 |  | 
Ago | 0.158 |  | 
Set | 0.161 |  | 
Ott | 0.163 |  | 
Nov | 0.159 |  | 
Dic | 0.161 |  | 

## Sheet: Top_JobRole

ATTRITION PER JOB ROLE |  |  | 
Job Role | Totale | Attriti | Attrition %
Human Resources | 11 | 6 | 0.545454545454545
Sales Representative | 8 | 3 | 0.375
Healthcare Representative | 4 | 1 | 0.25
Research Scientist | 4 | 1 | 0.25
Manager | 30 | 5 | 0.166666666666667
Sales Executive | 5 | 0 | 0
Manufacturing Director | 5 | 0 | 0
Laboratory Technician | 3 | 0 | 0

## Sheet: Istruzioni_Esercizio

ESERCIZIO — Executive HR Dashboard |  |  |  | 
Dataset: IBM HR Analytics  |  Tempo: 45 minuti |  |  |  | 
1 | Esplora i Dati Grezzi (foglio Dati_Grezzi) |  |  | 
 |   •  Quanti dipendenti totali? Quanti con Attrition=Yes? |  |  | 
 |   •  Nota le colonne disponibili: età, stipendio, dipartimento, soddisfazione |  |  | 
 |   •  Osserva il conditional formatting già applicato su AttritionNum |  |  | 
2 | Analizza i KPI (foglio KPI_Summary) |  |  | 
 |   •  Esamina le formule nelle celle colorate: COUNTIF, COUNTIFS, AVERAGEIF |  |  | 
 |   •  Osserva il conditional formatting RAG sull'Attrition % per dipartimento |  |  | 
 |   •  Identifica il dipartimento con attrition più alta e più bassa |  |  | 
 |   •  Guarda il trend mensile: c'è un pattern stagionale? |  |  | 
3 | Costruisci la Dashboard (nuovo foglio) |  |  | 
 |   •  Crea un nuovo foglio chiamato 'Dashboard' |  |  | 
 |   •  Aggiungi almeno 3 KPI card: Attrition Rate totale, Stipendio medio, % Overtime |  |  | 
 |   •  Inserisci un grafico a barre: Attrition % per Department |  |  | 
 |   •  Inserisci la tabella Top JobRole con conditional formatting RAG |  |  | 
 |   •  Disponi seguendo lo Z-pattern: KPI in alto, grafici al centro |  |  | 
 |   •  Aggiungi titolo, data di aggiornamento (usa =OGGI()), fonte dati |  |  | 
4 | Test finale (5 min) |  |  | 
 |   •  Mostra la dashboard a un collega — trova l'attrition totale in < 5 sec? |  |  | 
 |   •  Qual è il dipartimento più critico? Si vede immediatamente? |  |  | 
 |   •  Il titolo dice a chi è destinata e quando è aggiornata? |  |  | 
💡 SUGGERIMENTO: usa i fogli KPI_Summary e Top_JobRole come sorgenti dati per i grafici della dashboard |  |  |  | 


---

# Voti giornata 37

**File:** `Voti giornata 37.xlsx`
**Tipo:** `.xlsx`
**Dimensione:** 57.1 KB
**Ultima modifica:** 02/07/2026 09:28

---

## Sheet: Fantacalcio

Voti Fantacalcio 37ª giornata di campionato |  |  |  |  |  |  |  |  |  |  |  | 
Solo su www.fantacalcio.it i voti ufficiali per la tua lega |  |  |  |  |  |  |  |  |  |  |  | 
QUESTO FILE NON PUO' ESSERE RIPRODOTTO NE' PUBBLICATO SU ALTRI SITI INTERNET |  |  |  |  |  |  |  |  |  |  |  | 
E' DA CONSIDERARSI AD USO PERSONALE ESCLUSIVO DEGLI ISCRITTI DI FANTACALCIO.IT |  |  |  |  |  |  |  |  |  |  |  | 
Atalanta |  |  |  |  |  |  |  |  |  |  |  | 
Cod. | Ruolo | Nome | Voto | Gf | Gs | Rp | Rs | Rf | Au | Amm | Esp | Ass
4431 | P | Carnesecchi | 6.5 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0
554 | D | Zappacosta | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
787 | D | Djimsiti | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
2640 | D | Kolasinac | 6* | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5067 | D | Bakker | 6* | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5526 | D | Scalvini | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6916 | D | Ahanor | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
22 | C | De Roon | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
2077 | C | Pasalic | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0
5295 | C | Musah | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5422 | C | Zalewski | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5792 | C | Ederson D.S. | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
4371 | A | Raspadori | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5918 | A | Sulemana K. | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5995 | A | De Ketelaere | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6435 | A | Krstovic | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
1909 | ALL | Palladino | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
Bologna |  |  |  |  |  |  |  |  |  |  |  | 
Cod. | Ruolo | Nome | Voto | Gf | Gs | Rp | Rs | Rf | Au | Amm | Esp | Ass
133 | P | Skorupski | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
4734 | D | Miranda J. | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
7175 | D | Joao Mario | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
7212 | D | Heggem | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
7326 | D | Helland | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
184 | C | Bernardeschi | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
788 | C | Freuler | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
2167 | C | Orsolini | 7 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5298 | C | Pobega | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0
5858 | C | Ferguson | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6054 | C | Moro N. | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6844 | C | Rowe | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1
6572 | A | Castro S. | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6643 | A | Dallinga | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6895 | A | Dominguez B. | 6* | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
4993 | ALL | Italiano | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
Cagliari |  |  |  |  |  |  |  |  |  |  |  | 
Cod. | Ruolo | Nome | Voto | Gf | Gs | Rp | Rs | Rf | Au | Amm | Esp | Ass
4360 | P | Caprile | 6.5 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0
4210 | D | Mina | 7 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
4461 | D | Zappa | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5701 | D | Obert | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6230 | D | Dossena | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6832 | D | Palestra | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
7268 | D | Rodriguez Ju. | 6* | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0

## Sheet: Statistico

Voti Statistici 37ª giornata di campionato |  |  |  |  |  |  |  |  |  |  |  | 
Solo su www.fantacalcio.it i voti ufficiali per la tua lega |  |  |  |  |  |  |  |  |  |  |  | 
QUESTO FILE NON PUO' ESSERE RIPRODOTTO NE' PUBBLICATO SU ALTRI SITI INTERNET |  |  |  |  |  |  |  |  |  |  |  | 
E' DA CONSIDERARSI AD USO PERSONALE ESCLUSIVO DEGLI ISCRITTI DI FANTACALCIO.IT |  |  |  |  |  |  |  |  |  |  |  | 
Atalanta |  |  |  |  |  |  |  |  |  |  |  | 
Cod. | Ruolo | Nome | Voto | Gf | Gs | Rp | Rs | Rf | Au | Amm | Esp | Ass
4431 | P | Carnesecchi | 6.5 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0
554 | D | Zappacosta | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
787 | D | Djimsiti | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
2640 | D | Kolasinac | 6* | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5067 | D | Bakker | 6* | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5526 | D | Scalvini | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6916 | D | Ahanor | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
22 | C | De Roon | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
2077 | C | Pasalic | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0
5295 | C | Musah | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5422 | C | Zalewski | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5792 | C | Ederson D.S. | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
4371 | A | Raspadori | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5918 | A | Sulemana K. | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5995 | A | De Ketelaere | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6435 | A | Krstovic | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
1909 | ALL | Palladino | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
Bologna |  |  |  |  |  |  |  |  |  |  |  | 
Cod. | Ruolo | Nome | Voto | Gf | Gs | Rp | Rs | Rf | Au | Amm | Esp | Ass
133 | P | Skorupski | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
4734 | D | Miranda J. | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
7175 | D | Joao Mario | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
7212 | D | Heggem | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
7326 | D | Helland | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
184 | C | Bernardeschi | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
788 | C | Freuler | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
2167 | C | Orsolini | 7 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5298 | C | Pobega | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0
5858 | C | Ferguson | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6054 | C | Moro N. | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6844 | C | Rowe | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1
6572 | A | Castro S. | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6643 | A | Dallinga | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6895 | A | Dominguez B. | 6* | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
4993 | ALL | Italiano | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
Cagliari |  |  |  |  |  |  |  |  |  |  |  | 
Cod. | Ruolo | Nome | Voto | Gf | Gs | Rp | Rs | Rf | Au | Amm | Esp | Ass
4360 | P | Caprile | 6.5 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0
4210 | D | Mina | 7.5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
4461 | D | Zappa | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5701 | D | Obert | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6230 | D | Dossena | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6832 | D | Palestra | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
7268 | D | Rodriguez Ju. | 6* | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0

## Sheet: Italia

Voti Italia 37ª giornata di campionato |  |  |  |  |  |  |  |  |  |  |  | 
Solo su www.fantacalcio.it i voti ufficiali per la tua lega |  |  |  |  |  |  |  |  |  |  |  | 
QUESTO FILE NON PUO' ESSERE RIPRODOTTO NE' PUBBLICATO SU ALTRI SITI INTERNET |  |  |  |  |  |  |  |  |  |  |  | 
E' DA CONSIDERARSI AD USO PERSONALE ESCLUSIVO DEGLI ISCRITTI DI FANTACALCIO.IT |  |  |  |  |  |  |  |  |  |  |  | 
Atalanta |  |  |  |  |  |  |  |  |  |  |  | 
Cod. | Ruolo | Nome | Voto | Gf | Gs | Rp | Rs | Rf | Au | Amm | Esp | Ass
4431 | P | Carnesecchi | 6.5 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0
554 | D | Zappacosta | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
787 | D | Djimsiti | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
2640 | D | Kolasinac | 6* | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5067 | D | Bakker | 6* | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5526 | D | Scalvini | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6916 | D | Ahanor | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
22 | C | De Roon | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
2077 | C | Pasalic | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0
5295 | C | Musah | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5422 | C | Zalewski | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5792 | C | Ederson D.S. | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
4371 | A | Raspadori | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5918 | A | Sulemana K. | 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5995 | A | De Ketelaere | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6435 | A | Krstovic | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
1909 | ALL | Palladino | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
Bologna |  |  |  |  |  |  |  |  |  |  |  | 
Cod. | Ruolo | Nome | Voto | Gf | Gs | Rp | Rs | Rf | Au | Amm | Esp | Ass
133 | P | Skorupski | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
4734 | D | Miranda J. | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
7175 | D | Joao Mario | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
7212 | D | Heggem | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
7326 | D | Helland | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
184 | C | Bernardeschi | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
788 | C | Freuler | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
2167 | C | Orsolini | 7 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5298 | C | Pobega | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0
5858 | C | Ferguson | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6054 | C | Moro N. | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6844 | C | Rowe | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1
6572 | A | Castro S. | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6643 | A | Dallinga | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6895 | A | Dominguez B. | 6* | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
4993 | ALL | Italiano | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
Cagliari |  |  |  |  |  |  |  |  |  |  |  | 
Cod. | Ruolo | Nome | Voto | Gf | Gs | Rp | Rs | Rf | Au | Amm | Esp | Ass
4360 | P | Caprile | 6.5 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0
4210 | D | Mina | 7 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
4461 | D | Zappa | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
5701 | D | Obert | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6230 | D | Dossena | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
6832 | D | Palestra | 6.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
7268 | D | Rodriguez Ju. | 6* | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0

