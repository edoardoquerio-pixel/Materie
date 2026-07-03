# Lezione 15

## Panoramica
# ESERCIZI DI RIPASSO - LEZIONE 15

## Argomenti trattati
Generale

---
## Appunti

# ESERCIZI DI RIPASSO - LEZIONE 15
## Funzioni: Parte 1
### TEMPO STIMATO: 1 ora
## Esercizio 1: Funzioni Base (15 minuti)
Crea un programma con le seguenti funzioni:
1. `int cubo(int n)` - ritorna il cubo di un numero
2. `float mediaAritmetica(float a, float b, float c)` - ritorna la media di tre numeri
3. `int massimo2(int a, int b)` - ritorna il massimo tra due numeri
4. `void stampaBordo(int lunghezza)` - stampa una linea di asterischi della lunghezza specificata
**Test nel main:**
// cubo(4) → 64
// mediaAritmetica(8.0, 6.0, 10.0) → 8.0
// massimo2(15, 23) → 23
// stampaBordo(30) → ******************************
<summary><b>💡 SOLUZIONE</b></summary>
#include <stdio.h>
int cubo(int n);
float mediaAritmetica(float a, float b, float c);
int massimo2(int a, int b);
void stampaBordo(int lunghezza);
printf("=== TEST FUNZIONI BASE ===\n\n");
printf("Cubo di 4: %d\n", cubo(4));
printf("Cubo di -3: %d\n", cubo(-3));
printf("Cubo di 10: %d\n\n", cubo(10));
printf("Media di 8.0, 6.0, 10.0: %.2f\n", mediaAritmetica(8.0, 6.0, 10.0));
printf("Media di 5.5, 7.2, 9.3: %.2f\n\n", mediaAritmetica(5.5, 7.2, 9.3));
// Test massimo
printf("Massimo tra 15 e 23: %d\n", massimo2(15, 23));
printf("Massimo tra 100 e 50: %d\n", massimo2(100, 50));
printf("Massimo tra -5 e -10: %d\n\n", massimo2(-5, -10));
printf("Bordo di 30 caratteri:\n");
stampaBordo(30);
printf("\nBordo di 50 caratteri:\n");
stampaBordo(50);
int cubo(int n) {
return n * n * n;
float mediaAritmetica(float a, float b, float c) {
return (a + b + c) / 3.0;
int massimo2(int a, int b) {
// Alternativa più compatta:
// return (a > b) ? a : b;
void stampaBordo(int lunghezza) {
for (int i = 0; i < lunghezza; i++) {
**Output atteso:**
=== TEST FUNZIONI BASE ===
Cubo di -3: -27
Cubo di 10: 1000
Media di 8.0, 6.0, 10.0: 8.00
Media di 5.5, 7.2, 9.3: 7.33
Massimo tra 15 e 23: 23
Massimo tra 100 e 50: 100
Massimo tra -5 e -10: -5
Bordo di 30 caratteri:
Bordo di 50 caratteri:
## Esercizio 2: Validazione (15 minuti)
Crea funzioni di validazione che ritornano 1 (vero) o 0 (falso):
1. `int isMultiplo(int numero, int divisore)` - verifica se numero è multiplo di divisore
2. `int isCompreso(int n, int min, int max)` - verifica se n è compreso tra min e max (inclusi)
3. `int isVocale(char c)` - verifica se c è una vocale (a,e,i,o,u maiuscole o minuscole)
4. `int isBisestile(int anno)` - verifica se l'anno è bisestile
**Regola anno bisestile:**
- Divisibile per 4 E non per 100, OPPURE divisibile per 400
**Test nel main:**
// isMultiplo(15, 3) → 1 (vero)
// isMultiplo(15, 4) → 0 (falso)
// isCompreso(50, 1, 100) → 1
// isVocale('a') → 1
// isVocale('b') → 0
// isBisestile(2024) → 1
// isBisestile(1900) → 0
<summary><b>💡 SOLUZIONE</b></summary>
#include <stdio.h>
int isMultiplo(int numero, int divisore);
int isCompreso(int n, int min, int max);
int isVocale(char c);
int isBisestile(int anno);
printf("=== TEST FUNZIONI DI VALIDAZIONE ===\n\n");
// Test multiplo
printf("15 è multiplo di 3? %s\n", isMultiplo(15, 3) ? "SI" : "NO");
printf("15 è multiplo di 4? %s\n", isMultiplo(15, 4) ? "SI" : "NO");

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 015_esercizi_ripasso_lezione15.md*
