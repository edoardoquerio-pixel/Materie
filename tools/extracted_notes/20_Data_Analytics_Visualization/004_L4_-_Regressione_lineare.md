# L4 - Regressione lineare

Fonte: `L4 - Regressione lineare.pptx`

### Slide 1

DOCENTE | Adriano Gaved

UNITA’ FORMATIVA | Data Analytics and Visualization

ARGOMENTO | Regressione lineare

---

### Slide 2

Regressione
Lineare e Multipla

Dalla retta semplice al modello con più variabili

Dataset: immobiliare.xlsx

---

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

A cosa serve

• Descrivere la relazione tra due variabili
• Quantificare quanto x spiega y
• Fare previsioni su nuovi dati

---

### Slide 4

La formula della retta

y  =  a  +  b · x

a

Intercetta

Valore di y quando x = 0

Es: se superficie = 0 il prezzo base sarebbe €a (non sempre ha senso fisico)

b

Coefficiente angolare

Di quanto aumenta y per ogni unità in più di x

Es: b = 2.500 significa che ogni mq aggiuntivo vale circa €2.500

R²

Coefficiente di determinazione

Quota della variabilità di y spiegata dal modello

R² = 0.82 → la superficie spiega l'82% della variazione dei prezzi

---

### Slide 5

La formula della retta

---

### Slide 6

Interpretare R²

R² misura quanto bene la retta si adatta ai dati

R² < 0.3

Relazione debole
La retta spiega poco

0.3 – 0.6

Relazione moderata
Ci sono altri fattori

0.6 – 0.8

Relazione buona
Modello utile

R² > 0.8

Relazione molto forte
Modello affidabile

⚠  Attenzione: R² alto non significa causalità

Un R² = 0.85 tra superficie e prezzo dice che la superficie è un buon predittore del prezzo.
Non dice che la superficie causa il prezzo — ci sono zone, finiture, anno di costruzione e altri fattori.
La regressione descrive, non spiega.

---

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
=2480*C2+45000
Sostituisci con i tuoi valori reali

6  Verifica con REGR.LIN

=REGR.LIN(prezzo_eur; superficie_mq)
Restituisce {b; a} — confronta con il grafico

---

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
Le previsioni su appartamenti normali saranno sbagliate.

✅  Senza gli outlier

Filtra le righe anomale prima di creare il grafico:

Dati → Filtro automatico
Escludi id 8, 15, 56, 68

La retta descrive meglio il mercato normale.
R² più basso ma più onesto.
Le previsioni sono più affidabili.

---

### Slide 9

Blocco 2  ·  Usare la retta per fare previsioni

Supponiamo di aver ottenuto:  y = 2.480x + 47.000   (R² = 0,76)

Superficie (mq)

Formula applicata

Prezzo stimato €

60 mq

=2.480×60 + 47.000

€ 195.800

90 mq

=2.480×90 + 47.000

€ 270.200

120 mq

=2.480×120 + 47.000

€ 344.600

150 mq

=2.480×150 + 47.000

€ 419.000

⚠  La previsione è valida nel range dei dati osservati (es. 40–180 mq). Estrapolare fuori da questo range (es. 500 mq) produce stime non affidabili — la retta non sa cosa succede dove non ha visto dati.

---

### Slide 10

Blocco 2  ·  Prerequisito: attivare il componente Analisi dati

La regressione multipla richiede il componente aggiuntivo Analysis ToolPak

1

Apri le Opzioni di Excel

File → Opzioni

2

Vai a Componenti aggiuntivi

Nel menu laterale: Componenti aggiuntivi

3

Gestisci componenti

In fondo: Gestisci → Componenti aggiuntivi di Excel → Vai

4

Attiva Analysis ToolPak

Spunta ☑ Strumenti di analisi → OK

5

Verifica

Scheda Dati → in fondo a destra compare il pulsante Analisi dati

⚠  Operazione da fare una sola volta per installazione di Excel. Su Mac il percorso è: Strumenti → Componenti aggiuntivi di Excel.

---

### Slide 11

Regressione multipla: superficie + anno di costruzione

E se il prezzo dipendesse da più variabili insieme?

prezzo  =  a  +  b₁ · superficie_mq  +  b₂ · anno_costruzione

b₁

superficie_mq

Es: b₁ = 2.200
Ogni mq aggiuntivo
vale ~€2.200

b₂

anno_costruzione

Es: b₂ = 380
Ogni anno più recente
vale ~€380

R²

del modello

Es: R² = 0,81
Le due variabili
spiegano l'81%

---

### Slide 12

Blocco 2  ·  Regressione multipla in Excel – passo dopo passo

1  Prepara i dati (senza outlier)

Filtra o copia i dati escludendo id 8, 15, 56, 68.
Le colonne devono essere adiacenti oppure selezionabili con Ctrl+clic.

2  Apri Analisi dati

Scheda Dati → Analisi dati → Regressione → OK

3  Imposta le variabili

Intervallo Y: colonna prezzo_eur
Intervallo X: colonne superficie_mq e anno_costruzione (selezionale insieme)

4  Scegli l'output

Seleziona un foglio nuovo o una cella vuota come destinazione → OK

5  Leggi i risultati

Nella tabella Coefficienti:
• Intercept = a
• superficie_mq = b₁
• anno_costruzione = b₂
R² è in cima al report

6  Confronta con la regressione semplice

R² è aumentato rispetto al modello con sola superficie?
Di quanto? Valeva aggiungere anno_costruzione?

---

### Slide 13

Esercizio guidato  ·  immobiliare.xlsx

Apri il file e segui i passi:

1

Crea uno scatter plot superficie_mq vs prezzo_eur. Aggiungi trendline lineare con R². Annota i valori.

2

Identifica visivamente i punti anomali. Filtra i dati escludendo gli outlier. Come cambia R²?

3

Con l'equazione pulita, stima il prezzo di un appartamento da 75 mq e uno da 110 mq

4

Attiva Analisi dati ed esegui la regressione multipla: Y = prezzo_eur, X = superficie_mq + anno_costruzione

5

Confronta R² del modello semplice vs multiplo. Quanto aggiunge anno_costruzione? Qual è il coefficiente b₂?

---

### Slide 14

Riepilogo  ·  Regressione lineare e multipla

📈

La regressione lineare trova la retta y = a + b·x che minimizza gli errori sui dati

📐

b dice quanto vale ogni unità di x — ogni mq aggiuntivo, ogni anno più recente

🎯

R² misura la bontà del fit: la regressione multipla lo aumenta aggiungendo variabili esplicative

⚠️

Gli outlier distorcono la retta e R² può risultare fuorviante: l'EDA viene sempre prima