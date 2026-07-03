# Lezione 16

## Panoramica
## Funzioni: Parte 2 (Ricorsione, Prototipazione, Best Practices)

## Argomenti trattati
Data Analytics, API REST

---
## Appunti

# GUIDA DIDATTICA - LEZIONE 16
## Funzioni: Parte 2 (Ricorsione, Prototipazione, Best Practices)
### DURATA TOTALE: 4 ORE
## STRUTTURA DELLA LEZIONE
### Parte 1: RIPASSO (1 ora)
- Svolgimento esercizi di ripasso Lezione 15
- Correzione e discussione
### Parte 2: TEORIA LEZIONE 16 (1.5 ore)
- Funzioni ricorsive
- Prototipazione
- Funzioni void avanzate
- Variabili static
- Best practices
### Parte 3: PRATICA GUIDATA (1 ora)
- Esercizi svolti insieme
### Parte 4: ESERCIZI AUTONOMI (30 minuti)
- Esercizi individuali o a coppie
## PARTE 1: RIPASSO (60 minuti)
### Attività: Svolgimento Esercizi Ripasso
**Organizzazione:**
- I primi 3 esercizi: guidati insieme
- Esercizio 4: a coppie o individualmente
- Esercizio sfida: facoltativo per chi finisce prima
**Tempistiche:**
- Esercizio 1: 10 min
- Esercizio 2: 10 min
- Esercizio 3: 10 min
- Esercizio 4: 15 min
- Correzione e discussione: 15 min
**Punti chiave da ribadire durante la correzione:**
- L'importanza dei prototipi
- Il passaggio per valore delle variabili semplici
- Gli array vengono passati per riferimento (anticipazione!)
- La validazione dell'input nelle funzioni
## PARTE 2: TEORIA LEZIONE 16 (90 minuti)
### 2.1 FUNZIONI RICORSIVE (35 minuti)
**Introduzione (5 min):**
> "Una funzione ricorsiva è come le matrioske russe: ogni funzione contiene una versione più piccola di sé stessa!"
**Concetti fondamentali:**
1. **Caso base**: condizione di uscita (SEMPRE necessario!)
2. **Caso ricorsivo**: chiamata a sé stessa con parametri ridotti
**Esempio 1: Fattoriale (10 min)**
= 5 × 4 × 3 × 2!
= 5 × 4 × 3 × 2 × 1!
= 5 × 4 × 3 × 2 × 1
int fattoriale(int n) {
// Caso base: STOP!
if (n == 0 || n == 1) {
// Caso ricorsivo: chiama sé stessa
return n * fattoriale(n - 1);
**Visualizzazione dello stack (10 min):**
Stack per `fattoriale(5)`:
╔═══════════════╗
║ fattoriale(5) ║ → aspetta fattoriale(4)
╠═══════════════╣
║ fattoriale(4) ║ → aspetta fattoriale(3)
╠═══════════════╣
║ fattoriale(3) ║ → aspetta fattoriale(2)
╠═══════════════╣
║ fattoriale(2) ║ → aspetta fattoriale(1)
╠═══════════════╣
║ fattoriale(1) ║ → RITORNA 1 ✓
╚═══════════════╝
fattoriale(2) ritorna 2 × 1 = 2
fattoriale(3) ritorna 3 × 2 = 6
fattoriale(4) ritorna 4 × 6 = 24
fattoriale(5) ritorna 5 × 24 = 120
**⚠️ ATTENZIONE: Errori comuni (5 min)**
// ERRORE 1: Manca il caso base
int sbagliata(int n) {
return n * sbagliata(n - 1);  // Ricorsione infinita!
// ERRORE 2: Caso base irraggiungibile
int sbagliata2(int n) {
if (n == 0) return 0;
return n + sbagliata2(n + 1);  // n aumenta invece di diminuire!
**Esempio 2: Somma primi N numeri (5 min)**
int somma(int n) {
if (n == 0) return 0;         // Caso base
return n + somma(n - 1);      // Caso ricorsivo
// somma(5) = 5 + somma(4)

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 016_guida_didattica_lezione16.md*
