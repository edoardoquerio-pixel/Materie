# Pulizia dei dati in Excel (1)

## Panoramica
UNITA’ FORMATIVA | Data Analytics and Visualization

## Argomenti trattati
Data Analytics, API REST

---
## Appunti

### Slide 1
DOCENTE | Adriano Gaved
UNITA’ FORMATIVA | Data Analytics and Visualization
ARGOMENTO | Data cleaning in Excel
### Slide 2
Pulizia dei dati in Excel
da ”I dieci metodi principali per la pulizia dei dati” su support.microsoft.com
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
### Slide 4
2. Controllo ortografia
Il correttore ortografico può essere usato non solo per trovare parole con errori di ortografia, ma anche valori usati in modo incoerente, ad esempio nomi di prodotto o società, aggiungendo tali valori a un dizionario personalizzato.
### Slide 5
Funzioni base (sinistra, destra, trova)
Anteprima suggerita (flash fill)
Introduzione di Power Query
Funzioni regex native in cella
Evoluzione del testo in Excel
### Slide 6
Cosa sono le regex
Una espressione regolare è un modello che definisce una sequenza di caratteri. Permette di cercare, validare e trasformare testi complessi con estrema precisione.
Perché usarle in Excel
Rispetto alle funzioni tradizionali, le regex offrono una flessibilità senza precedenti per gestire dati non strutturati in modo nativo e veloce.
Definizione e vantaggi
### Slide 7
Funzione | Scopo principale | Esempio pratico
Regextest | Verifica se il testo corrisponde a uno schema. Restituisce vero o falso. | Validare se una cella contiene un codice fiscale nel formato corretto.
Regexextract | Estrae una porzione specifica di testo in base a un modello definito. | Recuperare solo il numero d'ordine da una stringa di testo mista.
Regexreplace | Sostituisce le parti di testo che corrispondono allo schema con un nuovo valore. | Rimuovere tutti i caratteri non numerici da una lista di contatti.
Le funzioni regex in Excel
### Slide 8
Iniziamo con un caso intuitivo: cercare una parola o una cifra.
✓ Corrisponde a:
"Ho una mela rossa"
✗ Non corrisponde a:
✓ Corrisponde a:
✗ Non corrisponde a:
UN ESEMPIO SEMPLICE
### Slide 9
Mentre i caratteri letterali matchano se stessi, i metacaratteri definiscono set o comportamenti logici.
. : Qualsiasi carattere singolo.
[abc] : Classe di caratteri (a, b o c).
[^abc] : Qualsiasi cosa tranne a, b o c.
\ : Carattere di escape.
LETTERALI E METACARATTERI
### Slide 10
Simbolo | Descrizione | Match Esempio | No Match
\d | Cifra decimale (0-9) | "8" | "k"
\w | Alfanumerico (a-z, 0-9, _) | "m" | "@"
\s | Spazio bianco | " " | "4"
\D | Qualsiasi NON cifra | "%" | "1"
CLASSI DI CARATTERI COMUNI
### Slide 11
{n} : Esattamente n volte.
{n,m} : Da n a m volte.
Esempio: \d{5} per un CAP.
Quantità Variabile
* : Zero o più volte.
+ : Una o più volte.
? : Zero o una volta.
I QUANTIFICATORI
### Slide 12
^ : Matcher dell'inizio della stringa.
$ : Matcher della fine della stringa.
\b : Word Boundary.
| : Operatore OR (Alternanza).
ANCORAGGI E CONFINI

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 001_Pulizia_dei_dati_in_Excel_1_.md*
