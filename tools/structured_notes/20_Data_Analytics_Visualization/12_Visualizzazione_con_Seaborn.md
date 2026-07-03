# Visualizzazione con Seaborn

## Panoramica
UNITA’ FORMATIVA | Data Analytics and Visualization

## Argomenti trattati
Data Analytics, API REST

---
## Appunti

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
*Fonte: 999_Visualizzazione_con_Seaborn.md*
