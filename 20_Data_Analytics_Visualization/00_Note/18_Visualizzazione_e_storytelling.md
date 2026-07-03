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
