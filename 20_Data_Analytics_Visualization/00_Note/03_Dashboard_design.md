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
