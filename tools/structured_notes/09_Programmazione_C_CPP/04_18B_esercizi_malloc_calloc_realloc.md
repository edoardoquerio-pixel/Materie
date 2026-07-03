# 18B esercizi malloc calloc realloc

## Panoramica
# ESERCIZI - MALLOC, CALLOC E REALLOC

## Argomenti trattati
Generale

---
## Appunti

# ESERCIZI - MALLOC, CALLOC E REALLOC
### TEMPO STIMATO: 2 ore (15 esercizi)
**DISTRIBUZIONE CONSIGLIATA:**
- Esercizi 1-5: malloc base (40 min)
- Esercizi 6-10: calloc e array paralleli (50 min)
- Esercizi 11-15: realloc e ridimensionamento (30 min)
## PARTE 1: ESERCIZI MALLOC
## Esercizio 1: Array Dinamico di Interi (10 min)
Scrivi un programma che:
1. Chiede all'utente quanti numeri vuole inserire
2. Alloca un array dinamico con `malloc`
3. Legge i numeri da tastiera
4. Stampa l'array, la somma e la media
5. Libera la memoria
<summary><b>💡 SOLUZIONE</b></summary>
#include <stdio.h>
#include <stdlib.h>
printf("Quanti numeri vuoi inserire? ");
scanf("%d", &n);
// Alloca array dinamicamente
int* arr = (int*) malloc(n * sizeof(int));
if (arr == NULL) {
printf("ERRORE: Allocazione fallita!\n");
printf("Inserisci %d numeri:\n", n);
for (int i = 0; i < n; i++) {
printf("  arr[%d] = ", i);
scanf("%d", &arr[i]);
printf("\nArray: [ ");
for (int i = 0; i < n; i++) {
printf("%d ", arr[i]);
// Somma e media
for (int i = 0; i < n; i++) {
somma += arr[i];
float media = (float) somma / n;
printf("Somma:  %d\n", somma);
printf("Media:  %.2f\n", media);
// Libera la memoria
**Esempio di esecuzione:**
Quanti numeri vuoi inserire? 5
Inserisci 5 numeri:
Array: [ 10 30 20 50 40 ]
## Esercizio 2: Temperature della Settimana (10 min)
Alloca dinamicamente un array per 7 temperature (una per giorno), calcola:
- Media settimanale
- Giorno più caldo
- Giorno più freddo
<summary><b>💡 SOLUZIONE</b></summary>
## Esercizio 3: Filtra Numeri Positivi (10 min)
1. Leggi n numeri in un array dinamico#include <stdio.h>
#include <stdlib.h>
char* giorni[] = {"Lunedì", "Martedì", "Mercoledì", "Giovedì",
"Venerdì", "Sabato", "Domenica"};
float* temp = (float*) malloc(n * sizeof(float));
if (temp == NULL) {
printf("Errore allocazione!\n");
printf("=== TEMPERATURE SETTIMANALI ===\n\n");
for (int i = 0; i < n; i++) {
printf("  %s: ", giorni[i]);
scanf("%f", &temp[i]);
float somma = 0;
for (int i = 0; i < n; i++) somma += temp[i];
float media = somma / n;
float max = temp[0], min = temp[0];
int giornoMax = 0, giornoMin = 0;
for (int i = 1; i < n; i++) {
if (temp[i] > max) {
if (temp[i] < min) {
printf("\n=== RISULTATI ===\n");
printf("Media:         %.2f°C\n", media);
printf("Giorno più caldo:  %s (%.2f°C)\n", giorni[giornoMax], max);
printf("Giorno più freddo: %s (%.2f°C)\n", giorni[giornoMin], min);
2. Conta quanti sono positivi
3. Alloca un secondo array esattamente della dimensione necessaria
4. Copia solo i numeri positivi nel secondo array
5. Stampa entrambi e libera
<summary><b>💡 SOLUZIONE</b></summary>
#include <stdio.h>
#include <stdlib.h>
printf("Quanti numeri? ");
scanf("%d", &n);

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 018_18B_esercizi_malloc_calloc_realloc.md*
