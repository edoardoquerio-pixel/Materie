# Espressioni regolari - esercizio

## Panoramica
UNITA’ FORMATIVA | Data Analytics and Visualization

## Argomenti trattati
Data Analytics

---
## Appunti

### Slide 1
DOCENTE | Adriano Gaved
UNITA’ FORMATIVA | Data Analytics and Visualization
ARGOMENTO | TDD e espressioni regolari
### Slide 2
Espressioni Regolari & TDD(Test-Driven Development)
Scrivi i test prima. Poi scrivi la regex.
### Slide 3
Cos'è il Test-Driven Development?
Scrivi un test che fallisce
Scrivi il codice minimo per farlo passare
Migliora il codice senza rompere i test
Perché usarlo con le regex?Una regex sembra funzionare finché non incontra un caso che non avevi previsto. I test ti proteggono.
### Slide 4
Il tuo compito: scrivi una regex per ciascun tipo di dato
Es: 00100, 20121
Data gg/mm/aaaa
Es: 01/01/2024, 29/02/2000
Es: RSSMRA80A01H501U
Indirizzo email
Es: user+tag@sub.example.co.uk
Numero di telefono
Es: +39 333 1234567, 800 123456
### Slide 5
Passo 1 — Genera 50 casi di test con un motore AI
Prompt da usare con ChatGPT / Claude / Gemini
Genera 50 casi di test per validare [TIPO DI DATO] con una regex.
Per ogni caso fornisci: valore, risultato atteso (Match / Non match), nota esplicativa.
Includi casi validi, invalidi, edge case (emoji, newline, tab, spazi, Unicode).
Formato: CSV con colonne valore,risultato,note
Casi validi (≈20)
Valori corretti in tutte le varianti previste dal formato
Casi invalidi (≈20)
Valori errati, troppo corti, troppo lunghi, caratteri sbagliati
Edge case (≈10)
Emoji, \n, \t, spazi iniziali/finali, Unicode non-ASCII, sequenze ambigue
### Slide 6
Passo 2 — Costruisci il file Excel di verifica
Regex:  inserisci qui la tua espressione regolare  →  usata in tutta la colonna C
=REGEX.TEST(A3,$G$1)
=REGEX.TEST(A4,$G$1)
=REGEX.TEST(A5,$G$1)
=REGEX.TEST(A6,$G$1)
✅  Test superato
❌  Falso positivo / Falso negativo
⚠️  Cella di input regex
Formula in C3:  =REGEX.TEST(A3, $G$1)
La regex è in $G$1 (riferimento assoluto) — trascina la formula su tutta la colonna.
### Slide 7
Cosa fare, passo dopo passo
1.  Scegli un tipo di dato
2.  Chiedi all'AI 50 casi di test, verifica che coprano tutti I casi possibili
3.  Crea il file Excel per fare i test
4.  Scrivi la regex: parti semplice, poi aggiungi complessità fino a far passare tutti i test

---
*Fonte: 999_Espressioni_regolari_-_esercizio.md*
