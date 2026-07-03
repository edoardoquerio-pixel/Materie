# Analisi esplorativa

## Panoramica
Analisi Esplorativa dei Dati (EDA)

## Argomenti trattati
Data Analytics

---
## Appunti

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
*Fonte: 999_Analisi_esplorativa.md*
