# Analisi esplorativa

Fonte: `Analisi esplorativa.pptx`

### Slide 1

Analisi Esplorativa dei Dati (EDA)

con Microsoft Excel

Dataset: immobiliare.xlsx

---

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

---

### Slide 3

Il dataset: immobiliare.xlsx

Useremo lo stesso dataset per tutta la sessione. Ogni blocco risponde a una domanda diversa.

Colonna

Tipo

Esempio valori

superficie_mq

numerico

85, 120, 60…

prezzo_eur

numerico

210.000, 340.000…

zona

categorico

Centro, Periferia, Semi

anno_costruzione

numerico

1965, 2005, 1988…

piano

numerico

0, 1, 2, 3…

ascensore

booleano

Sì / No

---

### Slide 4

Statistiche descrittive

Cosa misura ogni indicatore?

Indicatore

Formula Excel

Misura

Nota

Media

=MEDIA(A:A)

Valore tipico

Sensibile agli outlier

Mediana

=MEDIANA(A:A)

Valore centrale

Robusta agli outlier

Dev. Standard

=DEV.ST(A:A)

Dispersione dei valori

Stessa unità della variabile

Quartili

=QUARTILE(A:A; 1)

Suddivisione in 4 parti

Q2 = mediana

Min / Max

=MIN()  /  =MAX()

Valori estremi

Primo segnale di outlier

---

### Slide 5

Media vs Mediana – non è la stessa cosa

Dataset prezzi (€)

• 180.000

• 210.000

• 225.000

• 240.000

• 260.000

• 280.000

• 1.800.000 ← outlier

Media:

€ 456.429

Mediana:

€ 240.000

Cosa ci dice questo?

La media è trascinata in alto dall'appartamento a 1,8M€.

La mediana descrive meglio il caso tipico.

Con dati immobiliari (e redditi, stipendi…) la mediana è quasi sempre più informativa.

---

### Slide 6

Tabelle pivot – lo strumento più potente di Excel

Cos'è

Una tabella dinamica che aggrega i dati secondo criteri scelti da te.

A cosa serve

Calcolare medie, conteggi, somme per gruppi. Es: prezzo medio per zona.

Come si crea

Inserisci → Tabella Pivot → scegli righe, colonne e valori.

Esempio: prezzo medio per zona

Zona

Prezzo medio €

N.

Centro

€ 385.000

47

Semi-centro

€ 240.000

63

Periferia

€ 175.000

89

---

### Slide 7

Identificare valori anomali (outlier)

Regola 1.5×IQR

Rigoroso

Calcola Q1 e Q3.
Outlier = valori fuori da
[Q1 − 1.5·IQR,  Q3 + 1.5·IQR]

Formula / strumento:

=QUARTILE(A:A;3)−QUARTILE(A:A;1)

Box plot

Visuale

Inserisci → Grafici → Box e baffi.
I punti fuori dai baffi sono outlier.

Formula / strumento:

Grafico nativo Excel

Filtro + ordinamento

Rapido

Ordina per colonna e guarda i valori estremi manualmente.

Formula / strumento:

Dati → Ordina

---

### Slide 8

Esercizio guidato  ·  immobiliare.xlsx

Apri il file e completa le seguenti attività:

1

Calcola media e mediana del prezzo. Sono molto diverse? Perché?

2

Crea una tabella pivot: prezzo medio per zona

3

Individua eventuali outlier sulla colonna prezzo_eur (usa il box plot)

4

Aggiungi la colonna  prezzo_al_mq = prezzo / superficie

---

### Slide 9

Riepilogo  ·  Cosa abbiamo imparato

📊

Le statistiche descrittive danno una prima fotografia numerica del dataset

⚖️

Media ≠ Mediana: scegliere l'indicatore giusto evita conclusioni errate

🔄

Le tabelle pivot permettono di esplorare distribuzioni per categoria in pochi clic

🎯

Gli outlier vanno identificati prima di qualsiasi analisi: cambiano tutto

➡  Prossimo passo: usare questi stessi dati per costruire una regressione lineare