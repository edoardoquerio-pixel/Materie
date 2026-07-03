# Lezione 15

## Panoramica
1. Concetto di Funzione e Modularità

## Argomenti trattati
Programmazione, API REST

---
## Appunti

LEZIONE 15 - Funzioni: Parte 1
PARTE TEORICA (2h)
1. Concetto di Funzione e Modularità
Una funzione è un blocco di codice riutilizzabile che esegue un compito specifico. Le
funzioni sono il fondamento della programmazione modulare.
Vantaggi delle funzioni: - Riutilizzabilità: scrivi una volta, usa molte volte - Modularità:
divide programmi complessi in parti gestibili - Manutenibilità: più facile trovare e
correggere errori - Leggibilità: codice più chiaro e organizzato - Testing: puoi testare
singole funzioni - Collaborazione: diversi programmatori su funzioni diverse
Analogia della vita reale:
Preparare una pizza:
├─ Preparare l'impasto()
├─ Stendere la pasta()
├─ Aggiungere ingredienti()
└─ Cuocere in forno()
Ogni fase è una "funzione" con un compito specifico!
Esempio senza funzioni (codice duplicato):
// Calcolo area rettangolo 1
int base1 = 5, altezza1 = 3;
int area1 = base1 * altezza1;
printf("Area 1: %d\n", area1);
// Calcolo area rettangolo 2
int base2 = 8, altezza2 = 4;
int area2 = base2 * altezza2;
printf("Area 2: %d\n", area2);
// Calcolo area rettangolo 3
int base3 = 10, altezza3 = 6;
int area3 = base3 * altezza3;
printf("Area 3: %d\n", area3);
Esempio con funzioni (codice riutilizzabile):
int calcolaArea(int base, int altezza) {
return base * altezza;
printf("Area 1: %d\n", calcolaArea(5, 3));
printf("Area 2: %d\n", calcolaArea(8, 4));
printf("Area 3: %d\n", calcolaArea(10, 6));
2. Definizione e Dichiarazione
Struttura di una funzione:
tipoRitorno nomeFunzione(parametro1, parametro2, ...) {
// corpo della funzione
return valore; // se tipoRitorno != void
Componenti: 1. Tipo di ritorno: tipo del valore restituito (int, float, void, ecc.) 2. Nome
della funzione: identificatore univoco (convenzioni camelCase o snake_case) 3.
Parametri: input della funzione (opzionali) 4. Corpo: blocco di codice tra {} 5. Return:
restituisce un valore (obbligatorio se tipo != void)
// Funzione che calcola la somma di due numeri
int somma(int a, int b) {
int risultato = a + b;
return risultato;
// Funzione che stampa un saluto (nessun ritorno)
void saluta(char nome[]) {
printf("Ciao, %s!\n", nome);
// Non serve return
// Funzione senza parametri
int getNumeroFisso() {
// Funzione che verifica se un numero è pari
int isPari(int n) {
return (n % 2 == 0); // Ritorna 1 (vero) o 0 (falso)
Dichiarazione vs Definizione:
// DICHIARAZIONE (prototipo): dice al compilatore che la funzione esiste
int somma(int a, int b);
// DEFINIZIONE: implementa la funzione
int somma(int a, int b) {
// Esempio completo
#include <stdio.h>
// Dichiarazioni (in alto)
int somma(int a, int b);
int prodotto(int a, int b);
printf("%d\n", somma(5, 3)); // 8
printf("%d\n", prodotto(5, 3)); // 15
// Definizioni (dopo main)
int somma(int a, int b) {
int prodotto(int a, int b) {
3. Parametri Formali e Attuali
Parametri formali: variabili nella definizione della funzione Parametri attuali (o
argomenti): valori passati quando si chiama la funzione
// a e b sono PARAMETRI FORMALI
int somma(int a, int b) {
int x = 10, y = 20;
// x e y sono PARAMETRI ATTUALI (argomenti)
int risultato = somma(x, y);

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 015_lezione_15_funzioni1.md*
