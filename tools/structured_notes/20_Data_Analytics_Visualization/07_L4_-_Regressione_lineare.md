# L4 - Regressione lineare

## Panoramica
UNITA’ FORMATIVA | Data Analytics and Visualization

## Argomenti trattati
Data Analytics, API REST, Installazione

---
## Appunti

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
*Fonte: 004_L4_-_Regressione_lineare.md*
