# Teoria della visualizzazione

## Panoramica
Teoria della Visualizzazione e Grammar of Graphics

## Argomenti trattati
Data Analytics, Git

---
## Appunti

### Slide 1
Teoria della Visualizzazione e Grammar of Graphics
### Slide 2
Teoria della Visualizzazione
e Grammar of Graphics
Perché i grafici comunicano meglio delle tabelle · Come scegliere il grafico giusto · Principi di design visivo · Accessibilità
Esempi tratti da: Our World in Data, The Economist, NYT Graphics
### Slide 3
Perché i grafici? Il limite delle tabelle
Dati grezzi — cosa noti?
Anno | Paese A | Paese B
2018 | 12.4 | 8.1
2019 | 13.1 | 9.4
2020 | 10.2 | 11.2
2021 | 14.8 | 10.9
2022 | 16.3 | 11.5
2023 | 17.1 | 12.0
Stesso dato — trend immediato
Il cervello processa forma e colore prima della lettura
Pattern visivi emergono in millisecondi
Carico cognitivo
Un grafico ben fatto riduce lo sforzo di interpretazione
La tabella richiede confronto mentale attivo
Le immagini si ricordano meglio dei numeri (picture superiority effect)
Un'infografica dura nella memoria fino a 6 volte di più
### Slide 4
Grammar of Graphics: i canali visivi
Ogni dato può essere codificato su canali visivi diversi. La scelta del canale determina quanto è facile leggerlo.
Il canale più accurato
Usato da bar chart, scatter plot, line chart
Percezione immediata delle differenze
Secondo canale per accuratezza
Bar chart orizzontali e verticali
Funziona solo con baseline comune (zero)
Colore (tonalità)
Ottimo per categorie (max 6-8)
Scarso per valori ordinali o continui
Attenzione a daltonismo e stampa B/N
Dimensione (area)
Bubble chart, treemap
Meno accurato di posizione e lunghezza
Le aree circolari sono spesso sottostimate
Solo per categorie (max 5-6)
Difficile distinguerne molte
Usata spesso in scatter plot
Saturazione / Intensità
Per valori quantitativi continui
Mappe di calore, choropleth
Sequential palette: da chiaro a scuro
Regola d'oro: usa posizione per il dato più importante. Aggiungi altri canali solo se necessario.
### Slide 5
Come scegliere il grafico giusto: il framework delle 4 domande
Sto comparando valori tra categorie o nel tempo?
→ Bar chart, grouped bar, line chart
Esempio: vendite per regione, trend annuale
Com'è distribuito un valore nella popolazione?
→ Histogram, box plot, violin plot
Esempio: distribuzione voti, età clienti
C'è correlazione tra due variabili?
→ Scatter plot, bubble chart, heatmap
Esempio: reddito vs. istruzione
Come si compone un totale in parti?
→ Stacked bar, treemap, waffle chart
Evita il pie chart se >3 categorie
Domanda pratica da porsi prima di ogni grafico:
"Cosa voglio che il lettore confronti, veda, o capisca in 5 secondi?"
### Slide 6
Errori comuni nella visualizzazione
Effetti 3D, ombre, griglie inutili, clipart decorativi
Ogni pixel deve servire al dato(data-ink ratio, Tufte)
Rimuovi tutto ciò che non aggiunge informazione
Assi ingannevoli
Asse Y che non parte da zero altera la percezione
Scala logaritmica non dichiarata
Dual-axis con scale diverse = correlazioni false
Visual overloading
Troppi colori, troppi dataset nello stesso grafico
Il lettore non sa dove guardare
Regola: max 4-5 serie nello stesso grafico
Pie chart abusati

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_Teoria_della_visualizzazione.md*
