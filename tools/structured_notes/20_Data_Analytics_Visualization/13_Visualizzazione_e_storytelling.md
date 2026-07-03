# Visualizzazione e storytelling

## Panoramica
Visualizzazione per convincere: Storytelling

## Argomenti trattati
Data Analytics, Reti, API REST

---
## Appunti

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
*Fonte: 999_Visualizzazione_e_storytelling.md*
