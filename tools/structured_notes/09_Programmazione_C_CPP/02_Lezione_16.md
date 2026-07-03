# Lezione 16

## Panoramica
### TEMPO STIMATO: 3 ore (15 esercizi + bonus)

## Argomenti trattati
API REST, Programmazione

---
## Appunti

# ESERCIZI - PUNTATORI IN C
### TEMPO STIMATO: 3 ore (15 esercizi + bonus)
**DISTRIBUZIONE CONSIGLIATA:**
- Esercizi 1-5: Basi puntatori (50 min)
- Esercizi 6-10: Aritmetica e array (60 min)
- Esercizi 11-15: Stringhe e avanzati (70 min)
## PARTE 1: BASI DEI PUNTATORI
## Esercizio 1: Primo Contatto con i Puntatori (15 min)
Scrivi un programma che:
1. Dichiara una variabile `int x = 42`
2. Dichiara un puntatore `int* p` che punta a `x`
- Valore di `x`
- Indirizzo di `x` (`&x`)
- Valore di `p` (dovrebbe essere uguale a `&x`)
- Valore puntato da `p` (`*p`)
- Indirizzo di `p` (`&p`)
4. Modifica il valore di `x` attraverso il puntatore: `*p = 100`
5. Ristampa `x` e `*p`
<summary><b>💡 SOLUZIONE</b></summary>
#include <stdio.h>
p = &x;  // p ora punta a x
printf("=== INFORMAZIONI INIZIALI ===\n");
printf("Valore di x: %d\n", x);
printf("Indirizzo di x (&x): %p\n", &x);
printf("Valore di p: %p\n", p);
printf("Valore puntato da p (*p): %d\n", *p);
printf("Indirizzo di p (&p): %p\n", &p);
// Verifica che p contenga l'indirizzo di x
printf("✓ Il puntatore p punta correttamente a x\n\n");
// Modifica attraverso il puntatore
printf("=== MODIFICA ATTRAVERSO PUNTATORE ===\n");
printf("Eseguo: *p = 100\n\n");
printf("Valore di x: %d\n", x);
printf("Valore puntato da p (*p): %d\n", *p);
=== INFORMAZIONI INIZIALI ===
Valore di x: 42
Indirizzo di x (&x): 0x7fff5fbff73c
Valore di p: 0x7fff5fbff73c
Valore puntato da p (*p): 42
Indirizzo di p (&p): 0x7fff5fbff740
✓ Il puntatore p punta correttamente a x
=== MODIFICA ATTRAVERSO PUNTATORE ===
Eseguo: *p = 100
Valore di x: 100
Valore puntato da p (*p): 100
## Esercizio 2: Swap con Puntatori (15 min)
Implementa due versioni della funzione swap:
1. **swapSbagliato(int a, int b)** — passaggio per valore (non funziona)
2. **swap(int* a, int* b)** — passaggio per riferimento (funziona)
Testa entrambe e spiega perché solo la seconda funziona.
<summary><b>💡 SOLUZIONE</b></summary>
#include <stdio.h>
// Versione SBAGLIATA: passaggio per valore
void swapSbagliato(int a, int b) {
printf("  Dentro swapSbagliato: a=%d, b=%d\n", a, b);
// Versione CORRETTA: passaggio per riferimento
void swap(int* a, int* b) {
printf("  Dentro swap: *a=%d, *b=%d\n", *a, *b);
int x = 10, y = 20;
printf("=== TEST SWAP SBAGLIATO ===\n");
printf("Prima: x=%d, y=%d\n", x, y);
swapSbagliato(x, y);
printf("Dopo:  x=%d, y=%d\n", x, y);
printf("❌ Non funziona! x e y non sono cambiati\n\n");
printf("=== TEST SWAP CORRETTO ===\n");
printf("Prima: x=%d, y=%d\n", x, y);
printf("Dopo:  x=%d, y=%d\n", x, y);
printf("✓ Funziona! x e y sono scambiati\n");
=== TEST SWAP SBAGLIATO ===
Prima: x=10, y=20
Dentro swapSbagliato: a=20, b=10
Dopo:  x=10, y=20
❌ Non funziona! x e y non sono cambiati
=== TEST SWAP CORRETTO ===
Prima: x=10, y=20
Dentro swap: *a=20, *b=10
Dopo:  x=20, y=10
✓ Funziona! x e y sono scambiati
**Spiegazione:**
- `swapSbagliato` riceve COPIE dei valori → scambia le copie, non gli originali

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 016_16_esercizi_puntatori.md*
