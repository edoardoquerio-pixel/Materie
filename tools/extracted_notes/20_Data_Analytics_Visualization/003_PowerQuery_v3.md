# PowerQuery v3

Fonte: `PowerQuery v3.pptx`

### Slide 1

DOCENTE | Adriano Gaved

UNITA’ FORMATIVA | Data Analytics and Visualization

ARGOMENTO | Tidy Data e Power Query

---

### Slide 2

Variabili

Ogni variabile deve formare una colonna distinta nel dataset.

Osservazioni

Ogni singola osservazione deve formare una riga dedicata.

Valori

Ogni tipo di unità osservazionale deve formare una tabella.

Tidy data: Le 3 Regole d'Oro

---

### Slide 3

Tidy data: Le 3 Regole d'Oro – Regola 3

Esempio: Valori

❌  Messy

studente_id | nome | corso_id | corso_nome

1 | Mario | C01 | Matematica

1 | Mario | C02 | Fisica

✅  Tidy

Studenti

studente_id | nome

1 | Mario

Corsi

corso_id | corso_nome

C01 | Matematica

C02 | Fisica

Iscrizioni

studente_id | corso_id

1 | C01

1 | C02

→

Ogni tipo di unità osservazionale (studenti, corsi, iscrizioni) ha la sua tabella dedicata.

---

### Slide 4

Efficienza Computazionale: Molti linguaggi (R, Python) sono ottimizzati per operazioni vettoriali su colonne.

Visualizzazione: Strumenti come ggplot2 o Seaborn richiedono dati in formato lungo (long format).

Integrità: Riduce drasticamente la probabilità di errori logici durante il filtraggio o l'aggregazione.

Standardizzazione: Permette di riutilizzare lo stesso codice su dataset diversi ma con la stessa struttura.

Perché la struttura conta?

---

### Slide 5

Messy (Compatto)

Colonna: Sesso_Età

Valori: "M_25", "F_30", "M_18"

Richiede parsing di stringhe ogni volta che si vuole filtrare per età.

Tidy (Atomico)

Colonna A: Sesso (M, F)

Colonna B: Età (25, 30, 18)

Permette analisi statistiche dirette (es. età media per sesso).

Variabili Multiple in una Colonna

---

### Slide 6

Messy data: diritto da un film dell’orrore

---

### Slide 7

Power Query

Pulizia dati strutturata e ripetibile

Dataset: 20260708_Risposte_Invito.xlsx

---

### Slide 8

Il problema

Cosa succede se il file sorgente cambia il mese prossimo?
Come sapete quali operazioni avete fatto, e in che ordine?
Come collaborate con un collega sullo stesso processo di cleaning?
Cosa fate se vi accorgete di aver sbagliato un passo a metà lavoro?

Problemi del cleaning manuale in Excel

✗  Non ripetibile

✗  Non documentato

✗  Non reversibile

✗  Non collaborativo

---

### Slide 9

Interfaccia Power Query |  Demo

Come aprire Power Query

Scheda Dati → Recupera dati → Da file → Da cartella di lavoro
Seleziona il foglio 'Originale'
Clic su Trasforma dati (non Carica)

[ Screenshot: Dati → Recupera dati → Da file ]

Elementi chiave dell'interfaccia

Pannello Passaggi applicati

La lista di tutte le trasformazioni — il cuore di PQ

Anteprima dati

Mostra il risultato dopo ogni passo

Barra della formula

Codice M del passo selezionato

Pannello Query

Lista di tutte le query nel file

---

### Slide 10

La reversibilità

Come funziona l'undo in Power Query

Sorgente

Intestazioni promosso

Tipo modificato

Duplicati rimossi

Testo tagliato

▲  Selezionato: anteprima mostra i dati a questo punto

Per eliminare un passo:

Clic destro sul passo nel pannello → Elimina
I passi successivi vengono ricalcolati automaticamente
Se i passi successivi dipendono da quello eliminato → errore segnalato chiaramente

[ Screenshot: Pannello Passaggi – clic destro Elimina ]

---

### Slide 11

Operazioni di cleaning

Dal cleaning manuale a Power Query

Operazione | Excel manuale | Power Query

Testo maiuscolo/minuscolo | Funzione MAIUSC / MINUSC | Trasforma → Maiuscole/Minuscole

Spazi extra | Trova/Sostituisci + ANNULLA.SPAZI | Trasforma → Taglia

Elimina duplicati | Dati → Rimuovi duplicati | Home → Rimuovi righe → Duplicati

Filtra righe anomale | Filtro + cancella righe | Filtro colonna → deseleziona valori

Dividi colonna | Testo in colonne | Trasforma → Dividi colonna → Per delimitatore

Sostituisci valori | Trova/Sostituisci | Trasforma → Sostituisci valori

---

### Slide 12

Demo sul dataset – sequenza consigliata

1

Promuovi intestazioni

Home → Usa prima riga come intestazioni

2

Tipo dati colonne

Seleziona colonne → Trasforma → Rileva tipo dati

3

Togli gli spazi in eccesso in tutti i campi testo

Seleziona col. testo → Trasforma → Taglia

→ Risolve spazi in email e nomi

4

Proper case sui nomi

Colonna 'Nome e Cognome' → Trasforma → Proper Case.

→ Risolve: vincenzo, CARLA, clelia LORIGLIOLA

5

Rimuovi duplicati

Seleziona tutte le colonne → Home → Rimuovi righe → Duplicati

→ Silvio Contardi appare 2 volte, Monica Limongi 3 volte

6

Filtra valori non corretti

Filtro colonna partecipanti → “Non contiene ‘-’”

→ Benedetta Contardi (-2), Simona Lucenti (0)

---

### Slide 13

Demo: Split Nome e Cognome

Obiettivo: da 'Debora Nizzola' → Nome: 'Debora'  |  Cognome: 'Nizzola'

1

Seleziona colonna 'Nome e Cognome'

2

Trasforma → Dividi colonna → In base al delimitatore

3

Delimitatore: Spazio  |  Dove: All'occorrenza più a sinistra

4

Rinomina: colonna.1 → Nome,  colonna.2 → Cognome

5

Trasforma → Ogni parola in maiuscolo (su entrambe le nuove colonne)

⚠  Caso speciale: 'laura iolanda teresa Minotti' → 3 spazi → gestire manuale o con logica aggiuntiva

[ Screenshot: Finestra Split colonna per spazio ]

---

### Slide 14

Split Indirizzo → Via / Città / Provincia

Obiettivo: da 'Via Accursio Di Leo 6, Rescaldina, RM'  →  3 colonne

Passaggi in Power Query

Seleziona colonna Indirizzo
Dividi per delimitatore: virgola → ogni occorrenza
Ottieni 3 colonne (nel caso base)
Taglia tutte e 3 (rimuovi spazi)
Rinomina: Via, Città, Provincia

Casi problematici nel dataset

Emanuela Longari

5 segmenti (indirizzo con CAP incluso)

Roberta Pettiti

Solo 2 segmenti – provincia mancante

Monica MORELLI

Solo provincia, indirizzo incompleto

Valeria Costanzi

Terzo campo è un comune, non provincia

---

### Slide 15

Blocco 3  [avanzato]  Normalizzazione numero di telefono

Obiettivo: tutti nel formato  +39 XXX XXXXXXX

Formati presenti nel dataset

3389962593

cellulare senza prefisso (10 cifre)

+393480413086

con prefisso internazionale (12 cifre)

+393342237895

con spazi iniziali

+39 335 457510

già formattato con spazi

Logica corretta (colonna personalizzata)

⚠  '3932798650' inizia con 39 ma NON è il prefisso! È un cellulare 393... con 10 cifre.

Regola: lunghezza 10 cifre = senza prefisso  |  12 cifre = con prefisso 39

let
  pulito = Text.Remove([Telefono], {" ", "+", "-"}),
  norm = if Text.Length(pulito) = 12
         and Text.StartsWith(pulito, "39")
         then "+" & Text.Insert(pulito, 2, " ")
         else "+39 " & pulito
in norm

---

### Slide 16

Esercizio pratico |  Hands-on

Consegna agli studenti

File: 20260708_Risposte_Invito.xlsx  •  Foglio: Originale  •  Target: foglio Desiderata

Base

Importa il foglio Originale in Power Query
Taglia tutti i campi testo (rimuovi spazi)
Proper case sulla colonna Nome e Cognome
Dividi Nome e Cognome in due colonne
Rimuovi i duplicati
Filtra righe con partecipanti negativi o zero

Avanzato

Dividi la colonna Indirizzo in Via / Città / Provincia
Normalizza il numero di telefono (colonna personalizzata)
Separa Data di conferma in Conversion Day e Conversion Time

---

### Slide 17

La ripetibilità

Scenario: arriva il file aggiornato del mese prossimo

1

Duplica il file sorgente

Simula l'arrivo di nuovi dati

2

Home → Impostazioni origine dati

Cambia il percorso al nuovo file

3

Home → Aggiorna tutto

La pipeline si riesegue automaticamente

4

Verifica il risultato

Stesso output pulito, nuovi dati

[ Screenshot: Demo aggiornamento sorgente dati + Aggiorna tutto ]

---

### Slide 18

Riepilogo

🔁

Ripetibile

La stessa pipeline funziona ogni mese senza lavoro manuale

📋

Documentato

Il pannello Passaggi è un log automatico di tutte le operazioni

↩

Reversibile

Ogni passo può essere eliminato o modificato in qualsiasi momento

🤝

Condivisibile

La query può essere esportata e riusata da altri

---

### Slide 19

Esercizio  Pulisci il file ordini.xlsx

File SPORCO  (foglio: Sporco)

ID Ordine

es. ORD-1001

Nome e Cognome

es. '  MARCO rossi ', 'giulia FERRARI'

Prodotto

es. 'Notebook ' (spazio finale)

Quantità

es. -3, 0 (valori anomali)

Prezzo unitario (€)

es. 12.90

Stato

es. 'consegnato', 'IN TRANSITO'

Data ordine

es. 2024-03-15

→

File PULITO  (foglio: Desiderata)

ID Ordine

invariato

Nome

da split + Proper case

Cognome

da split + Proper case

Prodotto

trim applicato

Quantità

solo valori > 0

Prezzo unitario (€)

invariato

Stato

Consegnato / In transito / Annullato

Data ordine

invariato

Operazioni da usare:  Trim  •  Proper case  •  Rimuovi duplicati  •  Filtra righe (Quantità ≤ 0 e righe vuote)  •  Split colonna  •  Sostituisci valori (Stato)