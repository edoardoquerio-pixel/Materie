# Espressioni regolari - esercizio

**File:** `Espressioni regolari - esercizio.pptx`
**Tipo:** `.pptx`
**Dimensione:** 108.3 KB
**Ultima modifica:** 02/07/2026 09:24

---

Espressioni Regolari & TDD(Test-Driven Development)
Scrivi i test prima. Poi scrivi la regex.

---

Cos'è il Test-Driven Development?
Il ciclo TDD
🔴  RED
Scrivi un test che fallisce

🟢  GREEN
Scrivi il codice minimo per farlo passare

🔵  REFACTOR
Migliora il codice senza rompere i test
RED
Fai fallire
il test
GREEN
Fai passare
il test
REFACTOR
Migliorare
la soluzione
Perché usarlo con le regex?Una regex sembra funzionare finché non incontra un caso che non avevi previsto. I test ti proteggono.

---

Il tuo compito: scrivi una regex per ciascun tipo di dato
01
CAP italiano
Es: 00100, 20121
02
Data gg/mm/aaaa
Es: 01/01/2024, 29/02/2000
03
Codice fiscale
Es: RSSMRA80A01H501U
04
Targa italiana
Es: AB123CD
05
Indirizzo email
Es: user+tag@sub.example.co.uk
06
Numero di telefono
Es: +39 333 1234567, 800 123456

---

Passo 1 — Genera 50 casi di test con un motore AI
Prompt da usare con ChatGPT / Claude / Gemini
Genera 50 casi di test per validare [TIPO DI DATO] con una regex.
Per ogni caso fornisci: valore, risultato atteso (Match / Non match), nota esplicativa.
Includi casi validi, invalidi, edge case (emoji, newline, tab, spazi, Unicode).
Formato: CSV con colonne valore,risultato,note
Casi validi (≈20)
📋
Valori corretti in tutte le varianti previste dal formato
Casi invalidi (≈20)
❌
Valori errati, troppo corti, troppo lunghi, caratteri sbagliati
Edge case (≈10)
⚠️
Emoji, \n, \t, spazi iniziali/finali, Unicode non-ASCII, sequenze ambigue

---

Passo 2 — Costruisci il file Excel di verifica
A
Valore
B
Atteso
C
Risultato
REGEX.TEST
D
Esito
Regex:  inserisci qui la tua espressione regolare  →  usata in tutta la colonna C
AB123CD
Match
=REGEX.TEST(A3,$G$1)
✅ OK
ab123cd
Non match
=REGEX.TEST(A4,$G$1)
✅ OK
AB12CD
Non match
=REGEX.TEST(A5,$G$1)
❌ Falso pos.
😀B123CD
Non match
=REGEX.TEST(A6,$G$1)
✅ OK
✅  Test superato
❌  Falso positivo / Falso negativo
⚠️  Cella di input regex
Formula in C3:  =REGEX.TEST(A3, $G$1)
La regex è in $G$1 (riferimento assoluto) — trascina la formula su tutta la colonna.

---

Cosa fare, passo dopo passo
1.  Scegli un tipo di dato
2.  Chiedi all'AI 50 casi di test, verifica che coprano tutti I casi possibili
3.  Crea il file Excel per fare i test
4.  Scrivi la regex: parti semplice, poi aggiungi complessità fino a far passare tutti i test
