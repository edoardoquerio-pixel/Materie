# Lezione 10

## Panoramica
LEZIONE 10 - Costrutto di Selezione:

## Argomenti trattati
Reti, Data Analytics, Programmazione

---
## Appunti

LEZIONE 10 - Costrutto di Selezione:
Durata: 4 ore | Teoria: 2h | Esercizi: 2h
PARTE TEORICA (2 ore)
10.1 Introduzione allo switch (15 min)
Cos’è lo switch?
Lo switch è un costrutto di selezione multipla che permette di scegliere tra diverse
alternative in base al valore di una singola espressione.
Analogia: Come un centralino telefonico che smista le chiamate verso estensioni diverse.
Quando usare switch?
✓✓ USA switch quando: - Confronti una variabile con molte costanti - Hai 4+
alternative discrete - I valori sono interi o caratteri - Vuoi codice più leggibile e
✗✗ USA if-else quando: - Condizioni complesse (range, AND, OR) - Confronti con float
- Poche alternative (2-3) - Condizioni non costanti
Confronto if-else vs switch
Con if-else (verboso):
int scelta = 2;
if (scelta == 1) {
printf("Opzione 1\n");
} else if (scelta == 2) {
printf("Opzione 2\n");
} else if (scelta == 3) {
printf("Opzione 3\n");
} else if (scelta == 4) {
printf("Opzione 4\n");
printf("Opzione non valida\n");
Con switch (più chiaro):
int scelta = 2;
switch (scelta) {
printf("Opzione 1\n");
printf("Opzione 2\n");
printf("Opzione 3\n");
printf("Opzione 4\n");
printf("Opzione non valida\n");
10.2 Sintassi dello switch (20 min)
switch (espressione) {
case costante1:
// Istruzioni per costante1
case costante2:
// Istruzioni per costante2
case costante3:
// Istruzioni per costante3
// Istruzioni se nessun case corrisponde
break; // Opzionale nell'ultimo caso
1. switch (espressione) - espressione: valutata UNA sola volta - Deve essere intero o
carattere - Non può essere float, double, stringa
2. case costante: - costante: deve essere letterale o costante nota a compile-time -
Non può essere variabile - Ogni case deve essere unico
3. break: - Esce dallo switch - Senza break, l’esecuzione continua al caso successivo
4. default: - Caso opzionale - Eseguito se nessun case corrisponde - Può essere in
qualsiasi posizione (convenzionalmente alla fine)
Flow Chart: switch
┌────────┼────────┬────────┐
case 1? case 2? case 3? default
┌────┐ ┌────┐ ┌────┐ ┌────┐
│Code│ │Code│ │Code│ │Code│
└─┬──┘ └─┬──┘ └─┬──┘ └─┬──┘
break? break? break? │
└───────┴───────┴───────┘
Esempio 1: Menu semplice
printf("Scegli (1-3): ");
scanf("%d", &opzione);
switch (opzione) {
printf("Hai scelto opzione 1\n");
printf("Hai scelto opzione 2\n");
printf("Hai scelto opzione 3\n");
printf("Opzione non valida\n");
Esempio 2: Giorni della settimana
printf("Numero giorno (1-7): ");
scanf("%d", &giorno);
switch (giorno) {
printf("Lunedì\n");
printf("Martedì\n");
printf("Mercoledì\n");
printf("Giovedì\n");
printf("Venerdì\n");
printf("Sabato\n");
printf("Domenica\n");
printf("Giorno non valido\n");
Esempio 3: Caratteri
printf("Voto letterale (A-F): ");

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 010_lezione10_switch.md*
