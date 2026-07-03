# Teoria della visualizzazione

Fonte: `Teoria della visualizzazione.pptx`

### Slide 1

Teoria della Visualizzazione e Grammar of Graphics

---

### Slide 2

Teoria della Visualizzazione
e Grammar of Graphics

Perché i grafici comunicano meglio delle tabelle · Come scegliere il grafico giusto · Principi di design visivo · Accessibilità

Esempi tratti da: Our World in Data, The Economist, NYT Graphics

---

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

Pre-attentive

Il cervello processa forma e colore prima della lettura
Pattern visivi emergono in millisecondi

Carico cognitivo

Un grafico ben fatto riduce lo sforzo di interpretazione
La tabella richiede confronto mentale attivo

Memoria

Le immagini si ricordano meglio dei numeri (picture superiority effect)
Un'infografica dura nella memoria fino a 6 volte di più

---

### Slide 4

Grammar of Graphics: i canali visivi

Ogni dato può essere codificato su canali visivi diversi. La scelta del canale determina quanto è facile leggerlo.

Posizione

Il canale più accurato
Usato da bar chart, scatter plot, line chart
Percezione immediata delle differenze

Lunghezza

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

Forma

Solo per categorie (max 5-6)
Difficile distinguerne molte
Usata spesso in scatter plot

Saturazione / Intensità

Per valori quantitativi continui
Mappe di calore, choropleth
Sequential palette: da chiaro a scuro

Regola d'oro: usa posizione per il dato più importante. Aggiungi altri canali solo se necessario.

---

### Slide 5

Come scegliere il grafico giusto: il framework delle 4 domande

Confronto

Sto comparando valori tra categorie o nel tempo?
→ Bar chart, grouped bar, line chart
Esempio: vendite per regione, trend annuale

Distribuzione

Com'è distribuito un valore nella popolazione?
→ Histogram, box plot, violin plot
Esempio: distribuzione voti, età clienti

Relazione

C'è correlazione tra due variabili?
→ Scatter plot, bubble chart, heatmap
Esempio: reddito vs. istruzione

Composizione

Come si compone un totale in parti?
→ Stacked bar, treemap, waffle chart
Evita il pie chart se >3 categorie

Domanda pratica da porsi prima di ogni grafico:

"Cosa voglio che il lettore confronti, veda, o capisca in 5 secondi?"

---

### Slide 6

Errori comuni nella visualizzazione

Chartjunk

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

Difficile confrontare angoli non adiacenti
Con >4 categorie diventano illeggibili
Alternativa: bar chart orizzontale ordinato

Titoli assenti o generici

"Grafico 1" non è un titolo
Il titolo deve dichiarare il messaggio, non descrivere il grafico
Esempio: "Le vendite online crescono del 40% YoY"

Colori non accessibili

8% delle persone ha difficoltà a distinguere rosso/verde
Contrasto insufficiente per testo su sfondo colorato
Testa sempre con un simulatore di daltonismo

Data-ink ratio (Tufte): massimizza il rapporto ink utile / ink totale. Ogni tratto deve essere utile alla comunicazione.

---

### Slide 7

Teoria del colore per la visualizzazione

Palette Sequenziale

Per dati ordinali o continui (es. temperatura, reddito)

dal chiaro al scuro

Palette Divergente

Per dati con punto centrale significativo (es. ±variazione, approvazione)

centro neutro, due estremi

Palette Categorica

Per categorie nominali (es. paesi, prodotti, segmenti)

colori distinti, uguale luminosità

Strumenti consigliati: ColorBrewer2.org · Coolors.co · Viz Palette (accessibilità)

---

### Slide 8

Chiarezza visiva: titoli, etichette, annotazioni

Anatomia di un grafico chiaro

Titolo: messaggio principale (non descrizione)
Sottotitolo: fonte, unità di misura, periodo
Etichette assi: sempre presenti, concise
Legenda: vicina al dato, non isolata

Annotazioni efficaci

Annotazioni dirette > legenda separata
Evidenzia l'evento chiave (es. 'Lockdown Mar 2020')
Usa linee di riferimento per soglie importanti
Font size minimo 9pt per leggibilità

Tooltip e interattività

Per dashboard digitali: tooltip al passaggio del mouse
Non mettere nel tooltip dati già visibili nel grafico
Formato: Etichetta: valore (unità)

Esempio: titolo che informa vs titolo che descrive

✗  "Grafico delle vendite per trimestre"

Descrive il grafico, non dice nulla al lettore

✓  "Le vendite Q4 crescono del 23% nonostante l'inflazione"

Comunica il messaggio, il lettore sa cosa guardare

Gerarchia tipografica nel titolo:

Titolo 
Sottotitolo · Fonte  
Etichette assi

---

### Slide 9

Accessibilità nella visualizzazione

Progettare per tutti: daltonismo, bassa visione, stampa in B/N

8%

degli uomini ha daltonismo rosso-verde (deuteranopia/protanopia)

0.5%

delle donne ha daltonismo — meno diffuso ma non raro

4.5:1

rapporto di contrasto minimo WCAG AA per testo normale

Palette colorblind-safe

Evita rosso+verde insieme (il problema più comune)
Usa palette testate: Okabe-Ito, ColorBrewer, Viridis
Aggiungi sempre una variazione di forma o pattern
Testa con Coblis Color Blindness Simulator

Contrasto e leggibilità

Testo scuro su sfondo chiaro (o viceversa): ratio ≥ 4.5:1
Non usare solo il colore per trasmettere informazione critica
Etichette dirette sui dati > legenda separata per chi usa screen reader
Font min 10pt per grafici stampati

Palette Okabe-Ito (colorblind-safe):

Arancio

Cielo

Verde

Giallo

Blu

Rosso

Rosa

Nero

---

### Slide 10

Recap: i 4 concetti chiave

1. Perché i grafici

Il cervello processa pattern visivi più velocemente dei numeri
Usa grafici quando vuoi mostrare trend, confronti o relazioni
Una tabella è meglio quando il lettore cerca valori precisi

2. Grammar of Graphics

Ogni variabile va mappata su un canale visivo:posizione > lunghezza > colore > dimensione
Scegli il canale più accurato per il dato più importante
Il tipo di grafico discende dalla domanda analitica (confronto, distribuzione, relazione, composizione)

3. Chiarezza e design

Titolo informativo, etichette chiare, legenda vicina al dato
Elimina il chartjunk: ogni pixel deve essere giustificato
Parti sempre da zero sull'asse Y se stai mostrando lunghezze

4. Accessibilità

Usa palette colorblind-safe (Okabe-Ito, Viridis, ColorBrewer)
Garantisci contrasto WCAG 4.5:1 per il testo
Non affidarti solo al colore: aggiungi forma, pattern o etichette dirette