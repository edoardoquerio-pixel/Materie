# Visualizzazione per Big Data

## Panoramica
Problemi di visualizzazione nei Big Data e soluzioni

## Argomenti trattati
Data Analytics

---
## Appunti

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
*Fonte: 999_Visualizzazione_per_Big_Data.md*
