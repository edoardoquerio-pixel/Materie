# Lezione 11

## Panoramica
LEZIONE 11 - Cicli: while e do-while

## Argomenti trattati
Generale

---
## Appunti

LEZIONE 11 - Cicli: while e do-while
PARTE TEORICA (2h)
1. Concetto di Iterazione
L’iterazione (o ciclo/loop) è un costrutto fondamentale che permette di ripetere un
blocco di istruzioni finché una determinata condizione rimane vera.
Perché sono importanti i cicli?
Evitano la ripetizione di codice
Permettono di processare grandi quantità di dati
Consentono di eseguire operazioni fino al raggiungimento di un obiettivo
Elementi chiave di un ciclo:
Inizializzazione: preparare le variabili prima del ciclo
Condizione: espressione booleana che controlla se continuare
Corpo: blocco di istruzioni da ripetere
Aggiornamento: modifica delle variabili per avvicinarsi alla fine
Il ciclo while ripete un blocco di codice finché la condizione è vera. La condizione viene
verificata prima di ogni iterazione.
while (condizione) {
// corpo del ciclo
// istruzioni da ripetere
Flowchart del while:
Esempio 1: Contare da 1 a 5
#include <stdio.h>
int i = 1; // Inizializzazione
while (i <= 5) { // Condizione
printf("%d\n", i);
i++; // Aggiornamento
Esempio 2: Somma di numeri inseriti dall’utente
#include <stdio.h>
printf("Inserisci numeri (0 per terminare):\n");
scanf("%d", &numero);
while (numero != 0) {
somma += numero;
printf("Somma parziale: %d\n", somma);
scanf("%d", &numero);
printf("Somma totale: %d\n", somma);
3. Ciclo do-while
Il ciclo do-while esegue il corpo almeno una volta, poi controlla la condizione. La
verifica avviene dopo ogni iterazione.
// corpo del ciclo
// istruzioni da ripetere
} while (condizione); // NOTA: il punto e virgola è obbligatorio!
Flowchart del do-while:
Esempio: Menu con validazione
#include <stdio.h>
printf("\n=== MENU ===\n");
printf("1. Opzione A\n");
printf("2. Opzione B\n");
printf("3. Esci\n");
printf("Scelta: ");
scanf("%d", &scelta);
switch(scelta) {
printf("Hai scelto A\n");
printf("Hai scelto B\n");
printf("Arrivederci!\n");
printf("Scelta non valida!\n");
} while (scelta != 3);
4. Differenze tra while e do-while
Prima del corpo
Esecuzioni minime
0 (può non eseguire mai)
1 (esegue sempre almeno una
Quando non si sa se
Quando serve almeno
Esempio comparativo:
// while - potrebbe non stampare nulla
while (x < 5) {
printf("Questo non viene mai stampato\n");
// do-while - stampa almeno una volta
printf("Questo viene stampato una volta: %d\n", y);
} while (y < 5);
Quando usare do-while:
Menu interattivi
Validazione input (richiedi finché non è valido)
Quando serve almeno un’iterazione garantita
5. Cicli Infiniti e Condizioni di Uscita
Ciclo infinito (da evitare accidentalmente!):
// ERRORE: condizione sempre vera
while (i > 0) {
printf("Loop infinito!\n");
// Manca i++ o una condizione di uscita

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 011_lezione_11_cicli.md*
