# Lezione 9

## Panoramica
LEZIONE 9 - Costrutto di Selezione: if-else

## Argomenti trattati
API REST, Data Analytics, Sicurezza

---
## Appunti

LEZIONE 9 - Costrutto di Selezione: if-else
Durata: 4 ore | Teoria: 2h | Esercizi: 2h
PARTE TEORICA (2 ore)
9.1 Introduzione alla Selezione (10 min)
Cos’è la Selezione?
La selezione (o alternativa) permette al programma di scegliere quale blocco di codice
eseguire in base a una condizione.
Analogia vita reale:
SE piove ALLORA
prendi ombrello
lascia ombrello a casa
Flusso di Controllo
Senza selezione (sequenziale):
Tutte le istruzioni vengono sempre eseguite.
SE condizione ALLORA
Istruzione 2 ← Eseguita solo se vera
Istruzione 3 ← Eseguita solo se falsa
Flow Chart: Selezione
┌────┴────┐ ┌┴────────┐
│Istruzione│ │Istruzione│
└────┬────┘ └┬────────┘
9.2 Istruzione if Semplice (15 min)
if (condizione) {
// Codice eseguito SE condizione è vera
Componenti: - if: parola chiave - condizione: espressione booleana (vera/falsa) - { }:
blocco di codice (facoltativo se una sola istruzione)
Esempio 1: Controllo età
if (eta >= 18) {
printf("Sei maggiorenne\n");
Esempio 2: Numero positivo
printf("Il numero è positivo\n");
Esempio 3: Verifica divisibilità
if (n % 2 == 0) {
printf("%d è pari\n", n);
Blocco Singola vs Multipla Istruzione
Una istruzione (parentesi opzionali):
printf("Positivo\n");
// Equivalente a:
printf("Positivo\n");
Più istruzioni (parentesi OBBLIGATORIE):
printf("Il numero è positivo\n");
printf("Raddoppiato: %d\n", x);
ERRORE comune (senza parentesi):
printf("Positivo\n");
x = x * 2; // SEMPRE eseguito! Non fa parte dell'if
printf("Positivo\n");
x = x * 2; // Ora fa parte dell'if
Best Practice: Usa SEMPRE le parentesi graffe, anche per singola istruzione!
Condizioni Complesse
AND logico (&&):
char patente = 'S';
if (eta >= 18 && patente == 'S') {
printf("Puoi guidare\n");
OR logico (||):
int giorno = 7;
if (giorno == 6 || giorno == 7) {
printf("È weekend!\n");
NOT logico (!):
int piove = 0; // 0 = no, 1 = sì
printf("Non serve ombrello\n");
Condizioni nidificate:
if (voto >= 18) {
if (voto >= 27) {
printf("Ottimo!\n");
Valori di Verità
In C, 0 è falso, tutto il resto è vero.
if (x) { // Vero perché x = 5 (≠ 0)
printf("x è vero\n");
if (y) { // Falso perché y = 0
printf("Non stampato\n");
if (!y) { // Vero perché NOT di 0
printf("y è falso\n");
9.3 Istruzione if-else (20 min)
if (condizione) {
// Codice SE condizione è vera
// Codice SE condizione è falsa
Caratteristiche: - Esattamente UN blocco viene eseguito - Se condizione vera → esegue
primo blocco - Se condizione falsa → esegue secondo blocco
Flow Chart: if-else
┌────┴────┐ ┌─┴─────┐

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 009_lezione9_if_selezione.md*
