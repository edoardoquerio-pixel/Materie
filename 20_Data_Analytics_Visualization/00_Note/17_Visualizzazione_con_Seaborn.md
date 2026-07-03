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
