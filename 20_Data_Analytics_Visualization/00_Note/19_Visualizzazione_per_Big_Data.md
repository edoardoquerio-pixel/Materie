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
