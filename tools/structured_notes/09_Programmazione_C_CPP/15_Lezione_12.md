# Lezione 12

## Panoramica
1. Ciclo for: sintassi e semantica

## Argomenti trattati
Generale

---
## Appunti

LEZIONE 12 - Ciclo for
PARTE TEORICA (2h)
1. Ciclo for: sintassi e semantica
Il ciclo for è il ciclo più utilizzato quando si conosce in anticipo il numero di iterazioni da
eseguire. È particolarmente utile per contatori e iterazioni su sequenze.
for (inizializzazione; condizione; aggiornamento) {
// corpo del ciclo
Componenti del for:
Inizializzazione: eseguita una sola volta all’inizio (es: i = 0)
Condizione: verificata prima di ogni iterazione (es: i < 10)
Aggiornamento: eseguito dopo ogni iterazione (es: i++)
Corpo: blocco di istruzioni da ripetere
Flowchart del for:
┌──────────────┐
│Inizializzazione│
└──────┬─────────┘
│ Condizione? │
└──────┬──────┘
│ VERO │ FALSO ──> Continua
#include <stdio.h>
// Stampa numeri da 1 a 10
for (int i = 1; i <= 10; i++) {
printf("%d ", i);
// Output: 1 2 3 4 5 6 7 8 9 10
Equivalenza con while:
for (int i = 0; i < 5; i++) {
printf("%d\n", i);
// Equivalente con while
// inizializzazione
while (i < 5) {
printf("%d\n", i);
// aggiornamento
2. Varianti del ciclo for
Contare all’indietro:
for (int i = 10; i >= 1; i--) {
printf("%d ", i);
printf("Partenza!\n");
// Output: 10 9 8 7 6 5 4 3 2 1 Partenza!
Incremento personalizzato:
// Numeri pari da 0 a 20
for (int i = 0; i <= 20; i += 2) {
printf("%d ", i);
// Output: 0 2 4 6 8 10 12 14 16 18 20
// Multipli di 5
for (int i = 5; i <= 50; i += 5) {
printf("%d ", i);
// Output: 5 10 15 20 25 30 35 40 45 50
For con espressioni complesse:
// Più variabili
for (int i = 0, j = 10; i < j; i++, j--) {
printf("i=%d, j=%d\n", i, j);
// Condizione complessa
for (int i = 1; i <= 100 && i*i <= 50; i++) {
printf("%d ", i);
For “infinito”:
// Tutte le parti sono opzionali
printf("Ciclo infinito\n");
// Serve un break per uscire!
// Equivalente a while(1)
3. Cicli annidati
I cicli annidati sono cicli dentro altri cicli. Il ciclo interno viene eseguito completamente
per ogni iterazione del ciclo esterno.
Struttura base:
for (int i = 0; i < righe; i++) {
// ciclo esterno
for (int j = 0; j < colonne; j++) { // ciclo interno
// eseguito righe × colonne volte
Esempio 1: Tabella di moltiplicazione
#include <stdio.h>
printf("TABELLA PITAGORICA\n");
// Intestazione
for (int i = 1; i <= 10; i++) {
printf("%4d", i);
for (int i = 0; i < 40; i++) printf("-");
// Righe della tabella
for (int i = 1; i <= 10; i++) {
printf("%2d |", i);
for (int j = 1; j <= 10; j++) {
printf("%4d", i * j);
Esempio 2: Pattern con asterischi

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 012_lezione_12_for.md*
