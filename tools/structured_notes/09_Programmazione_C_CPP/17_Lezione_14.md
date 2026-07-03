# Lezione 14

## Panoramica
LEZIONE 14 - Array Multidimensionali e

## Argomenti trattati
API REST, Sicurezza, Git, Data Analytics

---
## Appunti

LEZIONE 14 - Array Multidimensionali e
PARTE TEORICA (2h)
1. Array Bidimensionali (Matrici)
Un array bidimensionale (o matrice) è un array di array: una struttura che organizza i
dati in righe e colonne.
Rappresentazione concettuale:
Array bidimensionale: int matrice[3][4]
Colonna: 0 1 2 3
┌────┬────┬────┬────┐
Riga 0 │ 1 │ 2 │ 3 │ 4 │
├────┼────┼────┼────┤
Riga 1 │ 5 │ 6 │ 7 │ 8 │
├────┼────┼────┼────┤
Riga 2 │ 9 │ 10 │ 11 │ 12 │
└────┴────┴────┴────┘
matrice[0][0] = 1 matrice[0][1] = 2
matrice[1][2] = 7 matrice[2][3] = 12
Utilizzi comuni: - Tabelle di dati (es: vendite per mese/prodotto) - Immagini bitmap -
Giochi da tavolo (scacchiera, tris) - Matrici matematiche - Griglie geografiche
2. Dichiarazione e Inizializzazione delle Matrici
tipo nomeMatrice[righe][colonne];
Esempi di dichiarazione:
int matrice[3][4]; // 3 righe, 4 colonne (12 elementi totali)
float temperature[12][7]; // 12 mesi, 7 giorni/settimana
char scacchiera[8][8]; // Scacchiera 8×8
Inizializzazione:
// Metodo 1: Inizializzazione completa
int matrice[3][4] = {
{1, 2, 3, 4}, // Riga 0
{5, 6, 7, 8}, // Riga 1
{9, 10, 11, 12} // Riga 2
// Metodo 2: Inizializzazione lineare (stesso risultato)
int matrice[3][4] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
// Metodo 3: Inizializzazione parziale
int matrice[3][4] = {
{1, 2}, // Riga 0: {1, 2, 0, 0}
{5}, // Riga 1: {5, 0, 0, 0}
{} // Riga 2: {0, 0, 0, 0}
// Metodo 4: Inizializzazione a zero
int matrice[3][4] = {0}; // Tutti gli elementi a 0
// Metodo 5: Prima dimensione automatica
int matrice[][4] = {
{9, 10, 11, 12}
}; // Il compilatore deduce 3 righe
Esempio completo:
#include <stdio.h>
// Matrice 3×3 (identità)
int identita[3][3] = {
// Matrice non inizializzata
float valori[2][3];
// Inizializzazione manuale
valori[0][0] = 1.5;
valori[0][1] = 2.3;
valori[0][2] = 3.7;
valori[1][0] = 4.2;
valori[1][1] = 5.8;
valori[1][2] = 6.1;
3. Accesso agli Elementi
nomeMatrice[indiceRiga][indiceColonna]
Accesso in lettura e scrittura:
int matrice[3][4] = {
{9, 10, 11, 12}
int valore = matrice[1][2]; // valore = 7
matrice[0][0] = 100; // Primo elemento = 100
matrice[2][3] = 200; // Ultimo elemento = 200
// Uso in espressioni
int somma = matrice[0][1] + matrice[1][1]; // 2 + 6 = 8
matrice[1][0] = matrice[0][0] * 2; // matrice[1][0] = 200
Iterazione con cicli annidati:
int matrice[3][4];
int righe = 3, colonne = 4;
for (int i = 0; i < righe; i++) {
for (int j = 0; j < colonne; j++) {
matrice[i][j] = i * colonne + j + 1;
printf("Matrice:\n");
for (int i = 0; i < righe; i++) {
for (int j = 0; j < colonne; j++) {
printf("%3d ", matrice[i][j]);
4. Operazioni su Matrici
Input da utente:

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 014_lezione_14_matrici.md*
