# Pulizia dei dati in Excel (1)

Fonte: `Pulizia dei dati in Excel (1).pptx`

### Slide 1

DOCENTE | Adriano Gaved

UNITA’ FORMATIVA | Data Analytics and Visualization

ARGOMENTO | Data cleaning in Excel

---

### Slide 2

Pulizia dei dati in Excel

da ”I dieci metodi principali per la pulizia dei dati” su support.microsoft.com

---

### Slide 3

Informazioni di base

Importare i dati da un'origine dati esterna.
Creare una copia di backup dei dati originali in una cartella di lavoro separata.
Verificare che i dati nelle righe e nelle colonne siano in formato tabulare con:
dati simili in ogni colonna,
tutte le colonne e le righe visibili
nessuna riga vuota all'interno dell'intervallo
Eseguire prima le attività che non richiedono la modifica della colonna, ad esempio il controllo ortografico o le operazioni con Trova e sostituisci.
Successivamente, eseguire le attività che richiedono la modifica della colonna. I passaggi generali per la modifica di una colonna sono:
Inserire una nuova colonna (B) accanto alla colonna originale (A) da pulire.
Aggiungere una formula che trasformerà i dati nella parte superiore della nuova colonna (B).
Inserire la formula nella nuova colonna (B). In una tabella di Excel una colonna calcolata viene creata automaticamente con i valori inseriti.
Selezionare la nuova colonna (B), copiarla e incollarla come valori nella nuova colonna (B).
Rimuovere la colonna originale (A), che converte la nuova colonna da B ad A.

---

### Slide 4

2. Controllo ortografia

Il correttore ortografico può essere usato non solo per trovare parole con errori di ortografia, ma anche valori usati in modo incoerente, ad esempio nomi di prodotto o società, aggiungendo tali valori a un dizionario personalizzato.

---

### Slide 5

1985

Funzioni base (sinistra, destra, trova)

2013

Anteprima suggerita (flash fill)

2016

Introduzione di Power Query

2024

Funzioni regex native in cella

Evoluzione del testo in Excel

---

### Slide 6

Cosa sono le regex

Una espressione regolare è un modello che definisce una sequenza di caratteri. Permette di cercare, validare e trasformare testi complessi con estrema precisione.

Perché usarle in Excel

Rispetto alle funzioni tradizionali, le regex offrono una flessibilità senza precedenti per gestire dati non strutturati in modo nativo e veloce.

Definizione e vantaggi

---

### Slide 7

Funzione | Scopo principale | Esempio pratico

Regextest | Verifica se il testo corrisponde a uno schema. Restituisce vero o falso. | Validare se una cella contiene un codice fiscale nel formato corretto.

Regexextract | Estrae una porzione specifica di testo in base a un modello definito. | Recuperare solo il numero d'ordine da una stringa di testo mista.

Regexreplace | Sostituisce le parti di testo che corrispondono allo schema con un nuovo valore. | Rimuovere tutti i caratteri non numerici da una lista di contatti.

Le funzioni regex in Excel

---

### Slide 8

Iniziamo con un caso intuitivo: cercare una parola o una cifra.

Pattern: mela

✓ Corrisponde a:

"Ho una mela rossa"

✗ Non corrisponde a:

"Ho una pera"

Pattern: \d

✓ Corrisponde a:

"Viale Roma 5"

✗ Non corrisponde a:

"Viale Roma"

UN ESEMPIO SEMPLICE

---

### Slide 9

Mentre i caratteri letterali matchano se stessi, i metacaratteri definiscono set o comportamenti logici.

•

. : Qualsiasi carattere singolo.

•

[abc] : Classe di caratteri (a, b o c).

•

[^abc] : Qualsiasi cosa tranne a, b o c.

•

\ : Carattere di escape.

LETTERALI E METACARATTERI

---

### Slide 10

Simbolo | Descrizione | Match Esempio | No Match

\d | Cifra decimale (0-9) | "8" | "k"

\w | Alfanumerico (a-z, 0-9, _) | "m" | "@"

\s | Spazio bianco | " " | "4"

\D | Qualsiasi NON cifra | "%" | "1"

CLASSI DI CARATTERI COMUNI

---

### Slide 11

Quantità Fissa

{n} : Esattamente n volte.

{n,m} : Da n a m volte.

Esempio: \d{5} per un CAP.

Quantità Variabile

* : Zero o più volte.

+ : Una o più volte.

? : Zero o una volta.

I QUANTIFICATORI

---

### Slide 12

^ : Matcher dell'inizio della stringa.

$ : Matcher della fine della stringa.

\b : Word Boundary.

| : Operatore OR (Alternanza).

ANCORAGGI E CONFINI

---

### Slide 13

Le parentesi ( ) permettono di raggruppare parti del pattern per estrarle separatamente o applicare quantificatori.

Logica di Gruppo

Ogni gruppo riceve un indice numerico (1, 2, 3...) in base all'ordine di apertura delle parentesi.

Esempio: (\w+)\s(\d+)

Esempio Estrazione

Testo: "Mele 50"

Gruppo 1: Mele

Gruppo 2: 50

I GRUPPI DI CATTURA

=SOSTITUISCI.REGEX(A2; "(\d{+})"; ”più di $1")

---

### Slide 14

3. Rimozione di righe duplicate

---

### Slide 15

4. Ricerca e sostituzione di testo

È possibile rimuovere una stringa iniziale comune, ad esempio un'etichetta seguita da due punti e spazio o un suffisso, ad esempio una frase tra parentesi alla fine della stringa obsoleta o non necessaria. A questo scopo, è possibile trovare istanze del testo e quindi sostituirlo senza testo o altro testo.

---

### Slide 16

Funzione | Scopo principale | Esempio pratico

Testo.precedente (textbefore)
 | Restituisce il testo che compare prima di un carattere o di una stringa di delimitazione specificata.
Sostituisce le vecchie combinazioni complesse di funzioni come SINISTRA e TROVA. | Esempio: =TESTO.PRECEDENTE(A1; " ")estrae il nome da una cella contenente"Nome Cognome".

Testo.successivo (textafter) | Restituisce il testo che compare dopo un determinato delimitatore.
Molto utile per isolare estensioni di file, domini email o parti finali di codici complessi. | Esempio: =TESTO.SUCCESSIVO(A1; "@")
estrae il dominio da un indirizzo email.

Testo.dividi (textsplit) | Suddivide una stringa di testo in più celle (colonne o righe) utilizzando i delimitatori scelti. | Esempio: =TESTO.DIVIDI(A1; ";")

Le nuove funzioni di testo in Excel

---

### Slide 17

4. Ricerca e sostituzione di testo

Esercizio: con che formula si può verificare se una cella contiene un certo carattere?


=SE(VAL.NUMERO(RICERCA(“x”,A1),”SI”,”NO”)						// Case insensitive

=SE(VAL.NUMERO(TROVA(“x”,A1),”SI”,”NO”)						// Case sensitive

---

### Slide 18

5. Modifica delle lettere maiuscole e minuscole del testo

INFERIORE(“Lorem Ipsum”) 		=> 		“lorem ipsum”

SUPERIORE(“Lorem Ipsum”)		=> 		“LOREM IPSUM”

MAIUSC.INIZ(“LOrEm ipSUm”)	=> 		“Lorem Ipsum”

---

### Slide 19

6. Rimozione degli spazi

Seccatura COLOSSALE!

ANNULLA.SPAZI() toglie spazi in eccesso all’inizio, fine e in mezzo ad un testo.

---

### Slide 20

7. Correzione di numeri

Il caso classico è quello di avere numeri salvati come testo.

Altro caso tipico è il caso di “numeri” che non sono in realtà numeri(non ha senso sommarli, sottrarli, etc..), come i NUMERI DI TELEFONO.

In questo caso spesso si deve ricondurli a uno stesso standard,
p.es 011 123 567 (e non (11) 123-456).

Colossale seccatura è la trasformazione del formato dei numeri:

1,234.56 => 1.234,56

---

### Slide 21

9. Unione e divisione di colonne

Un'attività comune dopo l'importazione di dati da un'origine dati esterna consiste nell'unione di due o più colonne in una sola o nella divisione di una colonna in due o più colonne. 
Si vuole, ad esempio, dividere una colonna che contiene un nome completo in nome e cognome. Oppure dividere una colonna che contiene un campo di indirizzo in colonne separate con via e numero civico, città, area geografica e codice postale.

Altri valori comuni che possono richiedere l'unione in un'unica colonna o la divisione in più colonne sono: codici di prodotto, percorsi di file e indirizzi IP (Internet Protocol).

---

### Slide 22

8. Correzione di date e ore

Il vero incubo… che raddoppia dovendo spostare i dati da e verso Google Sheet.

Primo grande problema: date salvate come testo.

Secondo problema: qual è il formato delle date?

Per le ore: che differenza c’è tra 12.15 e 12:15?

---

### Slide 23

9. Unione e divisione di colonne

Operatori e funzioni rilevanti:
&
CONCATENA()
DESTRA(), SINISTRA(), LUNGHEZZA()

---

### Slide 24

10. Trasformazione e ridisposizione di colonne e righe

La maggior parte delle caratteristiche di analisi e formattazione in Office Excel presuppongono la presenza dei dati in un'unica tabella normale bidimensionale.

A volte si potrebbe voler trasformare le righe in colonne e le colonne in righe. In altri casi, i dati non sono neanche strutturati in formato tabulare e potrebbe essere necessario convertirli da un formato non tabulare a uno tabulare.

---

### Slide 25

10. Diritto da un film dell’orrore

---

### Slide 26

Variabili

Ogni variabile deve formare una colonna distinta nel dataset.

Osservazioni

Ogni singola osservazione deve formare una riga dedicata.

Valori

Ogni tipo di unità osservazionale deve formare una tabella.

Tidy data: Le 3 Regole d'Oro

---

### Slide 27

Efficienza Computazionale: Molti linguaggi (R, Python) sono ottimizzati per operazioni vettoriali su colonne.

Visualizzazione: Strumenti come ggplot2 o Seaborn richiedono dati in formato lungo (long format).

Integrità: Riduce drasticamente la probabilità di errori logici durante il filtraggio o l'aggregazione.

Standardizzazione: Permette di riutilizzare lo stesso codice su dataset diversi ma con la stessa struttura.

Perché la struttura conta?

Ordinamento, filtri, funzioni: in Excel non funzionano o funzionano male su dati ‘messy’