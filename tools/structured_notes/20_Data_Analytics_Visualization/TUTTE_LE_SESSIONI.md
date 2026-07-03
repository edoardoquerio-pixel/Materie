# 20 - Data Analytics e Visualization — Tutte le Sessioni


---

## Sessione 1: Testimonianza Francesco Ceriani


Testimonianaza Aziendale
Guest: Francesco Ceriani
Retail landscape
Data sources and architecture
Value chain, from raw data to decision
My personal journey
Laurea in Ingegneria Informatica
Marketing Analyst
CRM Analysis Manager
Private Data Strategy Consultant
Oggi vedremo un caso reale di un luxury fashion retailer globale per capire, dal punto di vista della data governance, che la qualità del dato
non è affatto scontata. I dati non sono “buoni” per definizione: diventano affidabili solo grazie a processi strutturati, regole chiare e
responsabilità definite. Attraverso questo caso analizzeremo come i dati nascono, come vengono gestiti e perché solo dati di qualità
permettono di prendere decisioni di business solide in un contesto competitivo come quello del luxury.
- Retail landscape -
Pipelines a diversi fusi
orari, diverse regole
fiscali, vincoli legali sui
Tassi cambio variano
ogni giorno. Come fare
report globale? E trend
Diversi idiomi, caratteri
speciali, tassonomia
Diverse strutture
scontrini, ambiguita
codici cliente/prodotti..
«La scalabilità di un sistema è la capacità di ampliarne le dimensioni senza aumentare la complessità»
• Transaction/receipt ID
• Till / POS ID
• product ID / SKU
• discount applied
• Total amount. taxes
• Sorgenti di traffico (eg
social media, paid ad,
• Durata sessione
• Velocità di caricamento
• Tasso di conversion
- Data sources and architecture -
• Store/Department
• CRM interactions
• Sale associate ID
• Interaction date/time
• Channel (in store,
Whtsapp, clientelling
app, email, sms..)
• Interaction type (follow
up, invitation,
campaign promotion..)
• Gestione inventario
• Stock availability
• Presenza di figli
• Livello istruzione
• Fascia di reddito
• Valore immobiliare
della’rea di residenza
• Capacità di spesa
- Value chain, from raw data to decision -
(Export, Transform, Load)
• Dati incompleti o mal
• Errori inserimento
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
Qui si forgia la qualità del
• Interactive dashboard e
• KPI standardizzati
• Monitoraggio qualità dati
• Single source of truth
• Pattern e trend detection
• Segmentazioni
• Analisi predittive
• Test e simulazioni

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 2: Alberi di decisione


### Slide 1
DOCENTE | Adriano Gaved
UNITA’ FORMATIVA | Data Analytics and Visualization
ARGOMENTO | Albero di decisione
### Slide 2
Classificare con una sequenza di domande Sì / No
Dataset: prestiti.xlsx
### Slide 3
Come funziona un albero di decisione
Un albero pone una serie di domande sui dati per arrivare a una classificazione
debiti_totali > 30.000?
reddito > 40.000?
### Slide 4
Concetti chiave dell'albero di decisione
La prima domanda — la variabile che divide meglio i dati. L'algoritmo la sceglie automaticamente in base all'indice di Gini o all'entropia.
Ogni domanda successiva su una variabile. Ogni nodo divide i dati in due (o più) rami finché non si raggiunge una foglia.
Il nodo terminale: contiene la classe predetta (es. Approvato / Rifiutato). Non ci sono più domande da porre.
Profondità (depth)
Numero di livelli dell'albero. Alberi profondi imparano bene i dati di training ma rischiano l'overfitting.
L'albero memorizza i dati di training anziché generalizzare. Si controlla limitando la profondità massima (max_depth).
Misura l'impurità di un nodo: 0 = perfettamente puro (una sola classe), 0.5 = massima mescolanza. L'algoritmo minimizza il Gini.
### Slide 5
Albero di decisione vs Regressione logistica
Due approcci diversi allo stesso problema di classificazione
Albero di decisione
Regressione logistica
Classe diretta (Sì/No)
Probabilità → soglia → Sì/No
Interpretabilità
Alta: si legge come flowchart
Media: coefficienti da interpretare
Non lineari, regole nette
Lineari nel log-odds
Rischio alto senza potatura
Variabili categ.
Gestite nativamente
Richiedono encoding
Spiegare decisioni a non tecnici
Quando serve una probabilità calibrata
### Slide 6
Esempio — classificare 5 clienti con l'albero
Regole dell'albero (semplificate):
SE debiti > 30.000  →  SE età > 50  →  Approvato  |  altrimenti Rifiutato
SE debiti ≤ 30.000  →  SE reddito > 40.000  →  Approvato  |  altrimenti Rifiutato
Regola applicata
debiti≤30k → reddito>40k → ✅
debiti>30k → età≤50 → ❌
debiti≤30k → reddito>40k → ✅
debiti≤30k → reddito≤40k → ❌
debiti>30k → età>50 → ✅
### Slide 7
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
6  Importanza variabili
import pandas as pd
model.feature_importances_,
index=X.columns

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 3: Analisi esplorativa


### Slide 1
Analisi Esplorativa dei Dati (EDA)
con Microsoft Excel
Dataset: immobiliare.xlsx
### Slide 2
Prima di analizzare, esplorare
Perché fare EDA?
"In God we trust. All others must bring data."  — W. E. Deming
Capire la struttura
Quante righe? Che tipi di variabili? Dati mancanti?
Trovare i problemi
Outlier, errori di inserimento, distribuzioni anomale
Generare ipotesi
Quali variabili sembrano correlate? Cosa vale approfondire?
### Slide 3
Il dataset: immobiliare.xlsx
Useremo lo stesso dataset per tutta la sessione. Ogni blocco risponde a una domanda diversa.
210.000, 340.000…
Centro, Periferia, Semi
anno_costruzione
1965, 2005, 1988…
### Slide 4
Statistiche descrittive
Cosa misura ogni indicatore?
Sensibile agli outlier
Valore centrale
Robusta agli outlier
Dispersione dei valori
Stessa unità della variabile
=QUARTILE(A:A; 1)
Suddivisione in 4 parti
=MIN()  /  =MAX()
Primo segnale di outlier
### Slide 5
Media vs Mediana – non è la stessa cosa
Dataset prezzi (€)
• 1.800.000 ← outlier
Cosa ci dice questo?
La media è trascinata in alto dall'appartamento a 1,8M€.
La mediana descrive meglio il caso tipico.
Con dati immobiliari (e redditi, stipendi…) la mediana è quasi sempre più informativa.
### Slide 6
Tabelle pivot – lo strumento più potente di Excel
Una tabella dinamica che aggrega i dati secondo criteri scelti da te.
Calcolare medie, conteggi, somme per gruppi. Es: prezzo medio per zona.
Inserisci → Tabella Pivot → scegli righe, colonne e valori.
Esempio: prezzo medio per zona
### Slide 7
Identificare valori anomali (outlier)
Calcola Q1 e Q3.
Outlier = valori fuori da
[Q1 − 1.5·IQR,  Q3 + 1.5·IQR]
Formula / strumento:
=QUARTILE(A:A;3)−QUARTILE(A:A;1)
Inserisci → Grafici → Box e baffi.
I punti fuori dai baffi sono outlier.
Formula / strumento:
Grafico nativo Excel
Filtro + ordinamento
Ordina per colonna e guarda i valori estremi manualmente.
Formula / strumento:
### Slide 8
Esercizio guidato  ·  immobiliare.xlsx
Apri il file e completa le seguenti attività:
Calcola media e mediana del prezzo. Sono molto diverse? Perché?
Crea una tabella pivot: prezzo medio per zona
Individua eventuali outlier sulla colonna prezzo_eur (usa il box plot)
Aggiungi la colonna  prezzo_al_mq = prezzo / superficie
### Slide 9
Riepilogo  ·  Cosa abbiamo imparato
Le statistiche descrittive danno una prima fotografia numerica del dataset
Media ≠ Mediana: scegliere l'indicatore giusto evita conclusioni errate
Le tabelle pivot permettono di esplorare distribuzioni per categoria in pochi clic
Gli outlier vanno identificati prima di qualsiasi analisi: cambiano tutto
➡  Prossimo passo: usare questi stessi dati per costruire una regressione lineare

---

## Sessione 4: Dashboard design


### Slide 1
Visualization to Inform: Dashboard Design
### Slide 2
Dashboard vs Report — Scopo e Audience
Monitoraggio in tempo reale o quasi-reale
Decisioni operative immediate
Audience: manager, executive
Lettura in 5–30 secondi
Aggiornamento automatico e continuo
KPI al centro, dati aggregati
Analisi storica e documentazione
Decisioni strategiche e audit
Audience: analisti, stakeholder, revisori
Lettura approfondita: minuti o ore
Prodotto periodicamente (mensile, trimestrale)
Dettaglio e contesto narrativo
La dashboard risponde a «Come stiamo andando ORA?» — il report a «Perché è successo?»
### Slide 3
Anatomia di una Dashboard Efficace
Executive — alto livello
Trend di periodo
Manager — media granularità
Breakdown per categoria
Confronti temporali
Filtraggio interattivo
Analisti — dettaglio transazionale
Alert e anomalie
Una dashboard non è un report: scegli il livello giusto prima di disegnare
### Slide 4
Strumenti per le Dashboard — Panoramica di Mercato
Microsoft Power BI
Enterprise / Self-service
✓  Integrazione nativa con Excel e Azure
✓  DAX per calcoli avanzati
✗  Curva di apprendimento su DAX
→  Aziende Microsoft-centric, analisti business
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
✓  Motore associativo: esplora senza query
✓  Potente per analisi ad hoc
✗  UI meno intuitiva di Power BI/Tableau
→  Grandi enterprise, dati molto relazionali
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
### Slide 5
Layout: Z-Pattern e Percorso di Lettura
Come leggiamo una schermata
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
### Slide 6
Gerarchia Visiva e Whitespace
I 4 strumenti della gerarchia visiva
1. Dimensione (Size)

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 5: Espressioni regolari - esercizio


### Slide 1
DOCENTE | Adriano Gaved
UNITA’ FORMATIVA | Data Analytics and Visualization
ARGOMENTO | TDD e espressioni regolari
### Slide 2
Espressioni Regolari & TDD(Test-Driven Development)
Scrivi i test prima. Poi scrivi la regex.
### Slide 3
Cos'è il Test-Driven Development?
Scrivi un test che fallisce
Scrivi il codice minimo per farlo passare
Migliora il codice senza rompere i test
Perché usarlo con le regex?Una regex sembra funzionare finché non incontra un caso che non avevi previsto. I test ti proteggono.
### Slide 4
Il tuo compito: scrivi una regex per ciascun tipo di dato
Es: 00100, 20121
Data gg/mm/aaaa
Es: 01/01/2024, 29/02/2000
Es: RSSMRA80A01H501U
Indirizzo email
Es: user+tag@sub.example.co.uk
Numero di telefono
Es: +39 333 1234567, 800 123456
### Slide 5
Passo 1 — Genera 50 casi di test con un motore AI
Prompt da usare con ChatGPT / Claude / Gemini
Genera 50 casi di test per validare [TIPO DI DATO] con una regex.
Per ogni caso fornisci: valore, risultato atteso (Match / Non match), nota esplicativa.
Includi casi validi, invalidi, edge case (emoji, newline, tab, spazi, Unicode).
Formato: CSV con colonne valore,risultato,note
Casi validi (≈20)
Valori corretti in tutte le varianti previste dal formato
Casi invalidi (≈20)
Valori errati, troppo corti, troppo lunghi, caratteri sbagliati
Edge case (≈10)
Emoji, \n, \t, spazi iniziali/finali, Unicode non-ASCII, sequenze ambigue
### Slide 6
Passo 2 — Costruisci il file Excel di verifica
Regex:  inserisci qui la tua espressione regolare  →  usata in tutta la colonna C
=REGEX.TEST(A3,$G$1)
=REGEX.TEST(A4,$G$1)
=REGEX.TEST(A5,$G$1)
=REGEX.TEST(A6,$G$1)
✅  Test superato
❌  Falso positivo / Falso negativo
⚠️  Cella di input regex
Formula in C3:  =REGEX.TEST(A3, $G$1)
La regex è in $G$1 (riferimento assoluto) — trascina la formula su tutta la colonna.
### Slide 7
Cosa fare, passo dopo passo
1.  Scegli un tipo di dato
2.  Chiedi all'AI 50 casi di test, verifica che coprano tutti I casi possibili
3.  Crea il file Excel per fare i test
4.  Scrivi la regex: parti semplice, poi aggiungi complessità fino a far passare tutti i test

---

## Sessione 6: Google Colab


### Slide 1
DOCENTE | Adriano Gaved
UNITA’ FORMATIVA | Data Analytics and Visualization
ARGOMENTO | Google Colab
### Slide 2
Scrivere ed eseguire Python nel browser, senza installare nulla
colab.research.google.com
### Slide 3
Cos'è Google Colab
Un ambiente di sviluppo Python gratuito che gira nel browser
🌐  Browser-based
Non installi nulla sul tuo computer. Funziona su qualsiasi PC, Mac o Chromebook con Chrome o Firefox.
☁️  Salvataggio su Drive
I notebook si salvano automaticamente su Google Drive. Puoi condividerli come un documento Google.
GPU e CPU gratuiti forniti da Google. Sufficienti per analisi dati e machine learning di base.
📓  Notebook interattivo
Misto di codice Python eseguibile e testo formattato. Ogni cella può essere eseguita separatamente.
📦  Librerie preinstallate
pandas, numpy, sklearn, matplotlib, seaborn sono già disponibili. Nessun pip install necessario per i casi comuni.
🔗  Collegato a Google
Accede direttamente a Google Drive, Google Sheets e altri servizi Google con una sola riga di codice.
### Slide 4
Anatomia di un notebook
Un notebook è composto da celle — ogni cella contiene codice o testo
▶  Cella di codice
import pandas as pd
df = pd.read_excel('prestiti.xlsx')
id   eta   reddito_annuo   debiti_totali   prestito_approvato
0   1    38      45000           12000              Sì
T  Cella di testo (Markdown)
## Analisi esplorativa
Questa sezione calcola le statistiche descrittive
del dataset **prestiti.xlsx**.
Interazioni principali
▶  Esegui cella
Runtime → Esegui tutto
Runtime → Interrompi
### Slide 5
Primo utilizzo — creare ed eseguire il primo notebook
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
Ctrl+S oppure File → Salva
Il file .ipynb è salvato su Google Drive
automaticamente ogni pochi minuti
### Slide 6
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
### Slide 7
Shortcut — tasti utili in Colab
Imparare 8-10 shortcut rende il lavoro nel notebook molto più veloce
Windows / Linux
(sostituisci Ctrl con ⌘ Cmd)

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 7: L4 - Regressione lineare


### Slide 1
DOCENTE | Adriano Gaved
UNITA’ FORMATIVA | Data Analytics and Visualization
ARGOMENTO | Regressione lineare
### Slide 2
Lineare e Multipla
Dalla retta semplice al modello con più variabili
Dataset: immobiliare.xlsx
### Slide 3
Cos'è la regressione lineare
Domanda: esiste una relazione tra superficie e prezzo?
L'idea di fondo
Cerchiamo una retta y = a + b·x che descriva al meglio la relazione tra due variabili numeriche.
La retta non passa per tutti i punti — minimizza la distanza da ciascuno.
Cosa sono x e y
x = variabile indipendente (es. superficie_mq)
y = variabile dipendente (es. prezzo_eur)
Stiamo chiedendo: al crescere di x, come cambia y?
• Descrivere la relazione tra due variabili
• Quantificare quanto x spiega y
• Fare previsioni su nuovi dati
### Slide 4
La formula della retta
y  =  a  +  b · x
Valore di y quando x = 0
Es: se superficie = 0 il prezzo base sarebbe €a (non sempre ha senso fisico)
Coefficiente angolare
Di quanto aumenta y per ogni unità in più di x
Es: b = 2.500 significa che ogni mq aggiuntivo vale circa €2.500
Coefficiente di determinazione
Quota della variabilità di y spiegata dal modello
R² = 0.82 → la superficie spiega l'82% della variazione dei prezzi
### Slide 5
La formula della retta
### Slide 6
Interpretare R²
R² misura quanto bene la retta si adatta ai dati
Relazione debole
La retta spiega poco
Relazione moderata
Ci sono altri fattori
Relazione buona
Relazione molto forte
Modello affidabile
⚠  Attenzione: R² alto non significa causalità
Un R² = 0.85 tra superficie e prezzo dice che la superficie è un buon predittore del prezzo.
Non dice che la superficie causa il prezzo — ci sono zone, finiture, anno di costruzione e altri fattori.
La regressione descrive, non spiega.
### Slide 7
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
Sostituisci con i tuoi valori reali
6  Verifica con REGR.LIN
=REGR.LIN(prezzo_eur; superficie_mq)
Restituisce {b; a} — confronta con il grafico
### Slide 8
Perché l'EDA viene prima della regressione
Gli outlier distorcono la retta — ricordate quelli trovati nel Blocco 1?
❌  Con gli outlier
• id 8: €1.850.000 in Periferia
• id 15: €38.000 in Centro
• id 56: 8 mq a €45.000
• id 68: €920.000 in Periferia
La retta viene tirata verso i valori estremi.
R² apparentemente alto ma fuorviante.

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 8: PowerQuery v3


### Slide 1
DOCENTE | Adriano Gaved
UNITA’ FORMATIVA | Data Analytics and Visualization
ARGOMENTO | Tidy Data e Power Query
### Slide 2
Ogni variabile deve formare una colonna distinta nel dataset.
Ogni singola osservazione deve formare una riga dedicata.
Ogni tipo di unità osservazionale deve formare una tabella.
Tidy data: Le 3 Regole d'Oro
### Slide 3
Tidy data: Le 3 Regole d'Oro – Regola 3
Esempio: Valori
studente_id | nome | corso_id | corso_nome
1 | Mario | C01 | Matematica
1 | Mario | C02 | Fisica
studente_id | nome
corso_id | corso_nome
C01 | Matematica
studente_id | corso_id
Ogni tipo di unità osservazionale (studenti, corsi, iscrizioni) ha la sua tabella dedicata.
### Slide 4
Efficienza Computazionale: Molti linguaggi (R, Python) sono ottimizzati per operazioni vettoriali su colonne.
Visualizzazione: Strumenti come ggplot2 o Seaborn richiedono dati in formato lungo (long format).
Integrità: Riduce drasticamente la probabilità di errori logici durante il filtraggio o l'aggregazione.
Standardizzazione: Permette di riutilizzare lo stesso codice su dataset diversi ma con la stessa struttura.
Perché la struttura conta?
### Slide 5
Messy (Compatto)
Colonna: Sesso_Età
Valori: "M_25", "F_30", "M_18"
Richiede parsing di stringhe ogni volta che si vuole filtrare per età.
Colonna A: Sesso (M, F)
Colonna B: Età (25, 30, 18)
Permette analisi statistiche dirette (es. età media per sesso).
Variabili Multiple in una Colonna
### Slide 6
Messy data: diritto da un film dell’orrore
### Slide 7
Pulizia dati strutturata e ripetibile
Dataset: 20260708_Risposte_Invito.xlsx
### Slide 8
Cosa succede se il file sorgente cambia il mese prossimo?
Come sapete quali operazioni avete fatto, e in che ordine?
Come collaborate con un collega sullo stesso processo di cleaning?
Cosa fate se vi accorgete di aver sbagliato un passo a metà lavoro?
Problemi del cleaning manuale in Excel
✗  Non ripetibile
✗  Non documentato
✗  Non reversibile
✗  Non collaborativo
### Slide 9
Interfaccia Power Query |  Demo
Come aprire Power Query
Scheda Dati → Recupera dati → Da file → Da cartella di lavoro
Seleziona il foglio 'Originale'
Clic su Trasforma dati (non Carica)
[ Screenshot: Dati → Recupera dati → Da file ]
Elementi chiave dell'interfaccia
Pannello Passaggi applicati
La lista di tutte le trasformazioni — il cuore di PQ
Mostra il risultato dopo ogni passo
Barra della formula
Codice M del passo selezionato
Lista di tutte le query nel file
### Slide 10
La reversibilità
Come funziona l'undo in Power Query
Intestazioni promosso
Tipo modificato
Duplicati rimossi
▲  Selezionato: anteprima mostra i dati a questo punto
Per eliminare un passo:
Clic destro sul passo nel pannello → Elimina
I passi successivi vengono ricalcolati automaticamente
Se i passi successivi dipendono da quello eliminato → errore segnalato chiaramente
[ Screenshot: Pannello Passaggi – clic destro Elimina ]
### Slide 11
Operazioni di cleaning
Dal cleaning manuale a Power Query
Operazione | Excel manuale | Power Query

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 9: Pulizia dei dati in Excel (1)


### Slide 1
DOCENTE | Adriano Gaved
UNITA’ FORMATIVA | Data Analytics and Visualization
ARGOMENTO | Data cleaning in Excel
### Slide 2
Pulizia dei dati in Excel
da ”I dieci metodi principali per la pulizia dei dati” su support.microsoft.com
### Slide 3
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
### Slide 4
2. Controllo ortografia
Il correttore ortografico può essere usato non solo per trovare parole con errori di ortografia, ma anche valori usati in modo incoerente, ad esempio nomi di prodotto o società, aggiungendo tali valori a un dizionario personalizzato.
### Slide 5
Funzioni base (sinistra, destra, trova)
Anteprima suggerita (flash fill)
Introduzione di Power Query
Funzioni regex native in cella
Evoluzione del testo in Excel
### Slide 6
Cosa sono le regex
Una espressione regolare è un modello che definisce una sequenza di caratteri. Permette di cercare, validare e trasformare testi complessi con estrema precisione.
Perché usarle in Excel
Rispetto alle funzioni tradizionali, le regex offrono una flessibilità senza precedenti per gestire dati non strutturati in modo nativo e veloce.
Definizione e vantaggi
### Slide 7
Funzione | Scopo principale | Esempio pratico
Regextest | Verifica se il testo corrisponde a uno schema. Restituisce vero o falso. | Validare se una cella contiene un codice fiscale nel formato corretto.
Regexextract | Estrae una porzione specifica di testo in base a un modello definito. | Recuperare solo il numero d'ordine da una stringa di testo mista.
Regexreplace | Sostituisce le parti di testo che corrispondono allo schema con un nuovo valore. | Rimuovere tutti i caratteri non numerici da una lista di contatti.
Le funzioni regex in Excel
### Slide 8
Iniziamo con un caso intuitivo: cercare una parola o una cifra.
✓ Corrisponde a:
"Ho una mela rossa"
✗ Non corrisponde a:
✓ Corrisponde a:
✗ Non corrisponde a:
UN ESEMPIO SEMPLICE
### Slide 9
Mentre i caratteri letterali matchano se stessi, i metacaratteri definiscono set o comportamenti logici.
. : Qualsiasi carattere singolo.
[abc] : Classe di caratteri (a, b o c).
[^abc] : Qualsiasi cosa tranne a, b o c.
\ : Carattere di escape.
LETTERALI E METACARATTERI
### Slide 10
Simbolo | Descrizione | Match Esempio | No Match
\d | Cifra decimale (0-9) | "8" | "k"
\w | Alfanumerico (a-z, 0-9, _) | "m" | "@"
\s | Spazio bianco | " " | "4"
\D | Qualsiasi NON cifra | "%" | "1"
CLASSI DI CARATTERI COMUNI
### Slide 11
{n} : Esattamente n volte.
{n,m} : Da n a m volte.
Esempio: \d{5} per un CAP.
Quantità Variabile
* : Zero o più volte.
+ : Una o più volte.
? : Zero o una volta.
I QUANTIFICATORI
### Slide 12
^ : Matcher dell'inizio della stringa.
$ : Matcher della fine della stringa.
\b : Word Boundary.
| : Operatore OR (Alternanza).
ANCORAGGI E CONFINI

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 10: Regressione logistica


### Slide 1
DOCENTE | Adriano Gaved
UNITA’ FORMATIVA | Data Analytics and Visualization
ARGOMENTO | Regressione logistica
### Slide 2
Prevedere un risultato Sì / No
Dataset: prestiti.xlsx
### Slide 3
Classificazione: quando l'output non è un numero
Finora abbiamo sempre previsto un valore numerico continuo.
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
### Slide 4
La curva a S — sigmoid
A differenza della retta, la logistica produce sempre un valore tra 0 e 1
Output sempre in [0, 1]
Non è mai negativa né superiore a 1 — è una probabilità.
Forma a S (sigmoid)
Sale lentamente, poi rapidamente al centro, poi si appiattisce di nuovo.
Soglia di decisione
P ≥ 0,5 → Sì. La soglia è modificabile in base al contesto.
Funziona come la multipla: ogni variabile ha il suo coefficiente.
### Slide 5
La formula logistica
z  =  a  +  b₁·reddito  +  b₂·debiti  +  b₃·età
P(Sì)  =  1 / (1 + e⁻ᶻ)
z è il punteggio lineare (come nella regressione multipla). La sigmoid lo trasforma in probabilità.
b₁ > 0: reddito più alto → z aumenta →P(Sì) aumenta
b₂ < 0: debiti più alti → z diminuisce →P(Sì) diminuisce
b₃ > 0: età maggiore → storico più lungo →P(Sì) aumenta lievemente
### Slide 6
Esempio numerico — dataset prestiti.xlsx
Supponiamo di aver ottenuto i seguenti coefficienti:
z = −2.5 + 0.00005·reddito − 0.00006·debiti + 0.02·età
### Slide 7
Valutare il modello — la matrice di confusione
Come capire se il modello funziona bene?
(VP + VN) / totale  = (38+47)/(38+47+6+9) = 85%
Quante previsioni sono corrette in totale
VP / (VP + FP)  =  38/(38+9) = 81%
Tra chi prevediamo Sì, quanti sono davvero Sì
VP / (VP + FN)  =  38/(38+6) = 86%
Tra chi è davvero Sì, quanti prevediamo Sì
### Slide 8
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
### Slide 9
Come funziona il train/test split
Il dataset viene diviso casualmente in due parti prima di fare qualsiasi cosa
Dataset completo — 100 clienti
Training set — 80 clienti (80%)
Il test set non si tocca
I dati di test devono restare nascosti fino alla valutazione finale. Usarli per scegliere i parametri del modello invalida i risultati.
Proporzione tipica: 80/20
80% training, 20% test è la proporzione più comune. Con dataset piccoli (< 100 righe) si può scendere a 70/30.
random_state — cos'è e perché serve

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 11: Teoria della visualizzazione


### Slide 1
Teoria della Visualizzazione e Grammar of Graphics
### Slide 2
Teoria della Visualizzazione
e Grammar of Graphics
Perché i grafici comunicano meglio delle tabelle · Come scegliere il grafico giusto · Principi di design visivo · Accessibilità
Esempi tratti da: Our World in Data, The Economist, NYT Graphics
### Slide 3
Perché i grafici? Il limite delle tabelle
Dati grezzi — cosa noti?
Anno | Paese A | Paese B
2018 | 12.4 | 8.1
2019 | 13.1 | 9.4
2020 | 10.2 | 11.2
2021 | 14.8 | 10.9
2022 | 16.3 | 11.5
2023 | 17.1 | 12.0
Stesso dato — trend immediato
Il cervello processa forma e colore prima della lettura
Pattern visivi emergono in millisecondi
Carico cognitivo
Un grafico ben fatto riduce lo sforzo di interpretazione
La tabella richiede confronto mentale attivo
Le immagini si ricordano meglio dei numeri (picture superiority effect)
Un'infografica dura nella memoria fino a 6 volte di più
### Slide 4
Grammar of Graphics: i canali visivi
Ogni dato può essere codificato su canali visivi diversi. La scelta del canale determina quanto è facile leggerlo.
Il canale più accurato
Usato da bar chart, scatter plot, line chart
Percezione immediata delle differenze
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
Solo per categorie (max 5-6)
Difficile distinguerne molte
Usata spesso in scatter plot
Saturazione / Intensità
Per valori quantitativi continui
Mappe di calore, choropleth
Sequential palette: da chiaro a scuro
Regola d'oro: usa posizione per il dato più importante. Aggiungi altri canali solo se necessario.
### Slide 5
Come scegliere il grafico giusto: il framework delle 4 domande
Sto comparando valori tra categorie o nel tempo?
→ Bar chart, grouped bar, line chart
Esempio: vendite per regione, trend annuale
Com'è distribuito un valore nella popolazione?
→ Histogram, box plot, violin plot
Esempio: distribuzione voti, età clienti
C'è correlazione tra due variabili?
→ Scatter plot, bubble chart, heatmap
Esempio: reddito vs. istruzione
Come si compone un totale in parti?
→ Stacked bar, treemap, waffle chart
Evita il pie chart se >3 categorie
Domanda pratica da porsi prima di ogni grafico:
"Cosa voglio che il lettore confronti, veda, o capisca in 5 secondi?"
### Slide 6
Errori comuni nella visualizzazione
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

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 12: Visualizzazione con Seaborn


### Slide 1
DOCENTE | Adriano Gaved
UNITA’ FORMATIVA | Data Analytics and Visualization
ARGOMENTO | <<TITLE>>
Introduzione a Seaborn
### Slide 2
Introduzione a Seaborn
Visualizzazione dati in Python per l'analisi esplorativa e la modellazione
Dataset: tips (seaborn built-in)
### Slide 3
Agenda della lezione
Seaborn vs Matplotlib
Quando usare cosa
La struttura dati che Seaborn si aspetta
set_theme, palette, contesto
I tre plot universali
relplot · displot · catplot
Small multiples & faceting
hue / col / row
Curve di regressione
lmplot e regplot integrati
### Slide 4
Seaborn vs Matplotlib — quando usare cosa
Libreria di base — controllo totale su ogni pixel
Richiede codice verboso per grafici semplici
Ideale per: annotazioni personalizzate, layout complessi, output finale per report
Curva di apprendimento più ripida
Costruito su Matplotlib — sintassi di alto livello
Grafici statistici in una riga di codice
Integrazione nativa con DataFrame Pandas (formato tidy)
Ideale per: EDA, visualizzare distribuzioni e relazioni
💡  In pratica: usa Seaborn per esplorare i dati; aggiungi chiamate Matplotlib solo dove serve personalizzazione.
### Slide 5
Il formato Tidy — la struttura dati che Seaborn si aspetta
La regola d'oro del formato Tidy:
Ogni colonna = una variabile
total_bill, tip, sex, smoker, day, time, size
Ogni riga = un'osservazione
Un pasto al ristorante
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
### Slide 6
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
### Slide 7
Temi e stili — set_theme, palette, contesto
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
deep · muted · bright · pastel · dark · colorblind (qualitative)

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 13: Visualizzazione e storytelling


### Slide 1
Visualizzazione per convincere: Storytelling
### Slide 2
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
❌ Titolo dashboard: "Attrition by Department"
✅ Titolo storia: "HR perde 1 dipendente su 3: il problema è sistemico"
### Slide 3
La struttura del data storytelling: Context → Insight → Action
Chi è l'audience?
Qual è la situazione di partenza?
Es.: L'azienda registra un tasso
di attrition del 23% — sopra
la media del settore (15%).
Cosa rivela davvero il dato?
Perché è sorprendente o rilevante?
Es.: Il problema non è uniforme:
HR ha un attrition del 36%,
quasi 3× rispetto a R&D (12%).
Cosa deve fare l'audience?
Quale decisione è facilitata?
Es.: Prioritizzare interventi
di retention nell'HR:
job satisfaction e retribuzione.
Ogni visual nella storia corrisponde a uno di questi tre momenti. Se non sai dove collocare un grafico, probabilmente non serve.
### Slide 4
Applicazione al dataset HR: identificare l'insight
I dati grezzi non parlano da soli. Serve una domanda.
Domanda esplorativa | Dato trovato | È un insight?
Quanti abbandonano l'azienda? | 16 dipendenti su 70 (23%) | Contesto — non basta
Il problema è uguale ovunque? | HR: 36% vs R&D: 12% | ✅ Sì — è sorprendente
Perché HR è diverso? | Job satisfaction e stipendio più bassi | ✅ Rafforza l'insight
Gli straordinari contano? | OT=Yes: 31% vs OT=No: 21% | Segnale — da approfondire
La storia scelta per l'esercizio:
CONTEXT: Attrition 23%
INSIGHT: HR al 36% —
3× rispetto a R&D
ACTION: Intervenire su
stipendio e soddisfazione
### Slide 5
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
### Slide 6
Codice Seaborn — Visual 1 (Context): Attrition rate complessivo
Visual 1 di 3 — CONTEXT: mostra la dimensione del problema
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 14: Visualizzazione per Big Data


### Slide 1
Visualizzazione e Big Data
### Slide 2
Visualizzazione e Big Data
Problemi di visualizzazione nei Big Data e soluzioni
Data Analytics e Visualization  |  Modulo 3.5
Dataset: bigdata_viz_datasets.xlsx  (5 fogli, ~58.000 righe)
### Slide 3
1. Quando la scala diventa un problema
Quanti punti riesce a distinguere il nostro occhio in un grafico?  Circa 300–500. Cosa succede con 50.000?
Migliaia di punti si sovrappongono nello stesso pixel. Il grafico mostra una massa opaca: non vediamo densità, outlier, né distribuzione reale.
Rendering limit
Browser e librerie hanno un limite pratico: oltre 100k–500k marker il rendering rallenta o fallisce. Con Seaborn su Colab: crash o attesa di minuti.
Aggregation loss
Se aggreghiamo male (es. media mensile su dati orari) perdiamo i picchi, la varianza e i pattern stagionali. L’informazione è distrutta, non solo nascosta.
Dataset usato: foglio '1_Overplotting_Scatter'  (5.000 righe età–salario)
### Slide 4
1. Overplotting — il problema visivo
scatter() standard  —  5.000 punti
Problema: non si capisce dove sono concentrati i dati
hexbin()  —  stessi dati, densità visibile
Soluzione: la densità emerge chiaramente
### Slide 5
2. Sampling vs Aggregation — due strategie diverse
Di fronte a 50 milioni di righe: estraggo un sottoinsieme (sampling) o riassumo tutto (aggregation)?
Seleziona un sottoinsieme casuale (es. 1% dei dati)
Esplorazione iniziale, scatter plot, verifica distribuzione
Mantiene la forma della distribuzione originale
Gli outlier rari possono sparire dal campione
Calcola statistiche su gruppi (media, conteggio, somma)
Dashboard, trend temporali, confronti per categoria
Scala a miliardi di righe, risultato sempre leggibile
Nasconde varianza e distribuzioni interne ai gruppi
### Slide 6
2. Aggregation loss — quando aggregare fa perdere informazione
Scenario: vendite giornaliere 3 anni (foglio '2_Aggregation_Sales', 1.095 righe). Cosa succede se aggreghiamo a livelli diversi?
Dati giornalieri (raw)
1.095 punti — troppo rumore per capire il trend
Aggregato mensile
36 punti — trend stagionale visibile, varianza nascosta
Aggregato annuale
3 punti — trend visibile ma tutto il dettaglio perso
Regola pratica: aggregare al livello più fine che permette ancora una lettura chiara. Poi offrire drill-down.
### Slide 7
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
### Slide 8
3. Heatmap — leggere la densità su due dimensioni
Divide entrambe le variabili in bin (intervalli discreti)
Conta quante osservazioni cadono in ogni cella
Mappa il conteggio su una scala di colore
Il risultato è leggibile anche con milioni di punti
import seaborn as sns, pandas as pd
df = pd.read_excel('bigdata_viz_datasets.xlsx',
sheet_name='3_Heatmap_Students')
pivot = df.groupby(['Ore_Studio_Sett',
'Voto_Esame']).size().unstack()
sns.heatmap(pivot, cmap='Blues')
Ore Studio (bin)
Dataset: '3_Heatmap_Students'  (2.000 studenti, ore_studio × voto_esame)
### Slide 9
3. KDE e Histogram binned — distribuzioni a scala
Kernel Density Estimate (KDE)
La KDE stima la funzione di densità di probabilità smussando l'istogramma. Con fill=True e hue puoi confrontare gruppi sovrapposti su milioni di osservazioni.
sns.kdeplot(data=df, x='Altezza_cm',
hue='Genere', fill=True,
palette=['steelblue','crimson'])
Histogram binned
L'istogramma binned conta le frequenze per intervallo. Il parametro bins controlla la risoluzione: troppo pochi → perde dettaglio; troppi → rumore.

*[Contenuto troncato — vedi file originale per dettagli completi]*


---
*Totale: 14 sessioni generate il 02/07/2026*