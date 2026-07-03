# Programmazione C/C++ — Quaderno di Appunti

> **Materia:** 09_Programmazione_C_CPP
> **Data generazione:** Febbraio 2026
> **Corso:** ITS ICT Cloud Specialist 2025-2027

---

## Indice delle Sessioni

1. [16 esercizi puntatori](#16-esercizi-puntatori)
2. [16 guida didattica puntatori](#16-guida-didattica-puntatori)
3. [18B esercizi malloc calloc realloc](#18b-esercizi-malloc-calloc-realloc)
4. [18B guida didattica array dinamici](#18b-guida-didattica-array-dinamici)
5. [19 pila coda studente completo](#19-pila-coda-studente-completo)
6. [20 lezione ordinamento studente completo](#20-lezione-ordinamento-studente-completo)
7. [21 lezione stringhe studente completo](#21-lezione-stringhe-studente-completo)
8. [22 lezione struct studente completo](#22-lezione-struct-studente-completo)
9. [23 lezione strutture oggetti faber studente completo](#23-lezione-strutture-oggetti-faber-studente-completo)
10. [24 lezione strutture file studente completo](#24-lezione-strutture-file-studente-completo)
11. [esercizi ripasso lezione15](#esercizi-ripasso-lezione15)
12. [guida didattica lezione16](#guida-didattica-lezione16)
13. [lezione 11 cicli](#lezione-11-cicli)
14. [lezione 12 for](#lezione-12-for)
15. [lezione 13 array](#lezione-13-array)
16. [lezione 14 matrici](#lezione-14-matrici)
17. [lezione 15 funzioni1](#lezione-15-funzioni1)
18. [lezione1 programmazione](#lezione1-programmazione)
19. [lezione10 switch](#lezione10-switch)
20. [lezione2 flowchart](#lezione2-flowchart)
21. [lezione3 binario](#lezione3-binario)
22. [lezione4 decimali char](#lezione4-decimali-char)
23. [lezione6 primo c](#lezione6-primo-c)
24. [lezione7 variabili input](#lezione7-variabili-input)
25. [lezione8 operatori](#lezione8-operatori)
26. [lezione9 if selezione](#lezione9-if-selezione)
27. [SVILUPPO SOSTENIBILE 25-27](#sviluppo-sostenibile-25-27)

---

# 16 esercizi puntatori

**File:** `16 esercizi puntatori.md`
**Tipo:** `.md`
**Dimensione:** 18.9 KB
**Ultima modifica:** 02/07/2026 09:24

---

# ESERCIZI - PUNTATORI IN C

### TEMPO STIMATO: 3 ore (15 esercizi + bonus)

---

**DISTRIBUZIONE CONSIGLIATA:**
- Esercizi 1-5: Basi puntatori (50 min)
- Esercizi 6-10: Aritmetica e array (60 min)
- Esercizi 11-15: Stringhe e avanzati (70 min)

---

## PARTE 1: BASI DEI PUNTATORI

## Esercizio 1: Primo Contatto con i Puntatori (15 min)

Scrivi un programma che:
1. Dichiara una variabile `int x = 42`
2. Dichiara un puntatore `int* p` che punta a `x`
3. Stampa:
   - Valore di `x`
   - Indirizzo di `x` (`&x`)
   - Valore di `p` (dovrebbe essere uguale a `&x`)
   - Valore puntato da `p` (`*p`)
   - Indirizzo di `p` (`&p`)
4. Modifica il valore di `x` attraverso il puntatore: `*p = 100`
5. Ristampa `x` e `*p`

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

int main() {
    int x = 42;
    int* p;
    
    p = &x;  // p ora punta a x
    
    printf("=== INFORMAZIONI INIZIALI ===\n");
    printf("Valore di x: %d\n", x);
    printf("Indirizzo di x (&x): %p\n", &x);
    printf("\n");
    printf("Valore di p: %p\n", p);
    printf("Valore puntato da p (*p): %d\n", *p);
    printf("Indirizzo di p (&p): %p\n", &p);
    printf("\n");
    
    // Verifica che p contenga l'indirizzo di x
    if (p == &x) {
        printf("✓ Il puntatore p punta correttamente a x\n\n");
    }
    
    // Modifica attraverso il puntatore
    printf("=== MODIFICA ATTRAVERSO PUNTATORE ===\n");
    printf("Eseguo: *p = 100\n\n");
    *p = 100;
    
    printf("Valore di x: %d\n", x);
    printf("Valore puntato da p (*p): %d\n", *p);
    
    return 0;
}
```

**Output:**
```
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
```

</details>

---

## Esercizio 2: Swap con Puntatori (15 min)

Implementa due versioni della funzione swap:
1. **swapSbagliato(int a, int b)** — passaggio per valore (non funziona)
2. **swap(int* a, int* b)** — passaggio per riferimento (funziona)

Testa entrambe e spiega perché solo la seconda funziona.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

// Versione SBAGLIATA: passaggio per valore
void swapSbagliato(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    printf("  Dentro swapSbagliato: a=%d, b=%d\n", a, b);
}

// Versione CORRETTA: passaggio per riferimento
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
    printf("  Dentro swap: *a=%d, *b=%d\n", *a, *b);
}

int main() {
    int x = 10, y = 20;
    
    printf("=== TEST SWAP SBAGLIATO ===\n");
    printf("Prima: x=%d, y=%d\n", x, y);
    swapSbagliato(x, y);
    printf("Dopo:  x=%d, y=%d\n", x, y);
    printf("❌ Non funziona! x e y non sono cambiati\n\n");
    
    printf("=== TEST SWAP CORRETTO ===\n");
    printf("Prima: x=%d, y=%d\n", x, y);
    swap(&x, &y);
    printf("Dopo:  x=%d, y=%d\n", x, y);
    printf("✓ Funziona! x e y sono scambiati\n");
    
    return 0;
}
```

**Output:**
```
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
```

**Spiegazione:**
- `swapSbagliato` riceve COPIE dei valori → scambia le copie, non gli originali
- `swap` riceve gli INDIRIZZI → può modificare direttamente gli originali

</details>

---

## Esercizio 3: Multipli Valori di Ritorno (20 min)

Implementa `void statistiche(int arr[], int dim, int* somma, float* media, int* max, int* min)` che calcola tutte le statistiche di un array usando puntatori per "tornare" i valori.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

void statistiche(int arr[], int dim, int* somma, float* media, int* max, int* min) {
    *somma = 0;
    *max = arr[0];
    *min = arr[0];
    
    for (int i = 0; i < dim; i++) {
        *somma += arr[i];
        if (arr[i] > *max) *max = arr[i];
        if (arr[i] < *min) *min = arr[i];
    }
    
    *media = (float)(*somma) / dim;
}

int main() {
    int array[] = {12, 45, 7, 23, 89, 34, 16};
    int dim = 7;
    
    int somma, max, min;
    float media;
    
    statistiche(array, dim, &somma, &media, &max, &min);
    
    printf("=== STATISTICHE ARRAY ===\n");
    printf("Array: ");
    for (int i = 0; i < dim; i++) {
        printf("%d ", array[i]);
    }
    printf("\n\n");
    
    printf("Somma:   %d\n", somma);
    printf("Media:   %.2f\n", media);
    printf("Massimo: %d\n", max);
    printf("Minimo:  %d\n", min);
    
    return 0;
}
```

**Output:**
```
=== STATISTICHE ARRAY ===
Array: 12 45 7 23 89 34 16 

Somma:   226
Media:   32.29
Massimo: 89
Minimo:  7
```

</details>

---

## Esercizio 4: Incrementa e Triplo (15 min)

Scrivi due funzioni:
- `void incrementa(int* x)` — incrementa il valore puntato
- `void triplo(int* x)` — moltiplica per 3 il valore puntato

Testa con una variabile che parte da 5.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

void incrementa(int* x) {
    (*x)++;
}

void triplo(int* x) {
    *x = *x * 3;
}

int main() {
    int num = 5;
    
    printf("Valore iniziale: %d\n", num);
    
    incrementa(&num);
    printf("Dopo incrementa: %d\n", num);
    
    incrementa(&num);
    printf("Dopo 2° incrementa: %d\n", num);
    
    triplo(&num);
    printf("Dopo triplo: %d\n", num);
    
    return 0;
}
```

**Output:**
```
Valore iniziale: 5
Dopo incrementa: 6
Dopo 2° incrementa: 7
Dopo triplo: 21
```

</details>

---

## Esercizio 5: Divisione Completa (15 min)

Implementa `void divisioneCompleta(int dividendo, int divisore, int* quoziente, int* resto)` che calcola sia quoziente che resto.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

void divisioneCompleta(int dividendo, int divisore, int* quoziente, int* resto) {
    if (divisore == 0) {
        *quoziente = 0;
        *resto = 0;
        printf("ERRORE: Divisione per zero!\n");
        return;
    }
    
    *quoziente = dividendo / divisore;
    *resto = dividendo % divisore;
}

int main() {
    int q, r;
    
    printf("=== DIVISIONI COMPLETE ===\n\n");
    
    divisioneCompleta(17, 5, &q, &r);
    printf("17 / 5 = %d con resto %d\n\n", q, r);
    
    divisioneCompleta(100, 7, &q, &r);
    printf("100 / 7 = %d con resto %d\n\n", q, r);
    
    divisioneCompleta(50, 10, &q, &r);
    printf("50 / 10 = %d con resto %d\n\n", q, r);
    
    return 0;
}
```

**Output:**
```
=== DIVISIONI COMPLETE ===

17 / 5 = 3 con resto 2

100 / 7 = 14 con resto 2

50 / 10 = 5 con resto 0
```

</details>

---

## PARTE 2: ARITMETICA DEI PUNTATORI E ARRAY

## Esercizio 6: Stampa Array con Puntatori (15 min)

Implementa `void stampaArrayConPuntatori(int* arr, int dim)` che itera l'array usando l'aritmetica dei puntatori (senza indici).

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

void stampaArrayConPuntatori(int* arr, int dim) {
    int* p = arr;
    int* fine = arr + dim;
    
    printf("[ ");
    while (p < fine) {
        printf("%d ", *p);
        p++;
    }
    printf("]\n");
}

int main() {
    int numeri[] = {10, 20, 30, 40, 50, 60, 70};
    int dim = 7;
    
    printf("=== STAMPA CON PUNTATORI ===\n");
    stampaArrayConPuntatori(numeri, dim);
    
    return 0;
}
```

**Output:**
```
=== STAMPA CON PUNTATORI ===
[ 10 20 30 40 50 60 70 ]
```

</details>

---

## Esercizio 7: Somma Array con Puntatori (15 min)

Implementa `int sommaConPuntatori(int* arr, int dim)` usando solo puntatori.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

int sommaConPuntatori(int* arr, int dim) {
    int somma = 0;
    int* p = arr;
    int* fine = arr + dim;
    
    while (p < fine) {
        somma += *p;
        p++;
    }
    
    return somma;
}

int main() {
    int numeri[] = {5, 10, 15, 20, 25};
    int dim = 5;
    
    printf("Array: ");
    for (int i = 0; i < dim; i++) {
        printf("%d ", numeri[i]);
    }
    printf("\n");
    
    int somma = sommaConPuntatori(numeri, dim);
    printf("Somma: %d\n", somma);
    
    return 0;
}
```

**Output:**
```
Array: 5 10 15 20 25 
Somma: 75
```

</details>

---

## Esercizio 8: Trova Massimo con Puntatori (20 min)

Implementa `int* trovaMax(int* arr, int dim)` che ritorna un **puntatore** all'elemento massimo.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

int* trovaMax(int* arr, int dim) {
    int* maxPtr = arr;
    int* p = arr + 1;
    int* fine = arr + dim;
    
    while (p < fine) {
        if (*p > *maxPtr) {
            maxPtr = p;
        }
        p++;
    }
    
    return maxPtr;
}

int main() {
    int numeri[] = {15, 42, 8, 23, 67, 34, 12};
    int dim = 7;
    
    printf("Array: ");
    for (int i = 0; i < dim; i++) {
        printf("%d ", numeri[i]);
    }
    printf("\n");
    
    int* maxPtr = trovaMax(numeri, dim);
    
    printf("Elemento massimo: %d\n", *maxPtr);
    printf("Posizione: %ld\n", maxPtr - numeri);
    
    // Modifico il massimo
    *maxPtr = 100;
    
    printf("\nDopo modifica del massimo a 100:\n");
    printf("Array: ");
    for (int i = 0; i < dim; i++) {
        printf("%d ", numeri[i]);
    }
    printf("\n");
    
    return 0;
}
```

**Output:**
```
Array: 15 42 8 23 67 34 12 
Elemento massimo: 67
Posizione: 4

Dopo modifica del massimo a 100:
Array: 15 42 8 23 100 34 12 
```

</details>

---

## Esercizio 9: Inversione Array con Puntatori (20 min)

Implementa `void invertiConPuntatori(int* arr, int dim)` usando due puntatori (uno all'inizio, uno alla fine).

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

void invertiConPuntatori(int* arr, int dim) {
    int* inizio = arr;
    int* fine = arr + dim - 1;
    
    while (inizio < fine) {
        // Swap
        int temp = *inizio;
        *inizio = *fine;
        *fine = temp;
        
        inizio++;
        fine--;
    }
}

void stampaArray(int* arr, int dim) {
    printf("[ ");
    for (int i = 0; i < dim; i++) {
        printf("%d ", arr[i]);
    }
    printf("]\n");
}

int main() {
    int numeri[] = {10, 20, 30, 40, 50, 60, 70};
    int dim = 7;
    
    printf("Array originale:\n");
    stampaArray(numeri, dim);
    
    invertiConPuntatori(numeri, dim);
    
    printf("Array invertito:\n");
    stampaArray(numeri, dim);
    
    return 0;
}
```

**Output:**
```
Array originale:
[ 10 20 30 40 50 60 70 ]
Array invertito:
[ 70 60 50 40 30 20 10 ]
```

</details>

---

## Esercizio 10: Conta Elementi Maggiori di X (20 min)

Implementa `int contaMaggiori(int* arr, int dim, int soglia)` che conta quanti elementi sono > soglia, usando puntatori.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

int contaMaggiori(int* arr, int dim, int soglia) {
    int conta = 0;
    int* p = arr;
    int* fine = arr + dim;
    
    while (p < fine) {
        if (*p > soglia) {
            conta++;
        }
        p++;
    }
    
    return conta;
}

int main() {
    int numeri[] = {5, 12, 8, 20, 15, 3, 25, 7};
    int dim = 8;
    
    printf("Array: ");
    for (int i = 0; i < dim; i++) {
        printf("%d ", numeri[i]);
    }
    printf("\n\n");
    
    int soglie[] = {10, 15, 20};
    
    for (int i = 0; i < 3; i++) {
        int conta = contaMaggiori(numeri, dim, soglie[i]);
        printf("Elementi > %d: %d\n", soglie[i], conta);
    }
    
    return 0;
}
```

**Output:**
```
Array: 5 12 8 20 15 3 25 7 

Elementi > 10: 4
Elementi > 15: 2
Elementi > 20: 1
```

</details>

---

## PARTE 3: PUNTATORI E STRINGHE

## Esercizio 11: Lunghezza Stringa con Puntatori (15 min)

Implementa `int lunghezza(char* str)` che calcola la lunghezza senza usare `strlen()`.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

int lunghezza(char* str) {
    int len = 0;
    while (*str != '\0') {
        len++;
        str++;
    }
    return len;
}

int main() {
    char* stringhe[] = {
        "Ciao",
        "Programmazione",
        "C",
        "Hello World!"
    };
    
    printf("=== CALCOLO LUNGHEZZE ===\n\n");
    
    for (int i = 0; i < 4; i++) {
        printf("'%s' → lunghezza: %d\n", stringhe[i], lunghezza(stringhe[i]));
    }
    
    return 0;
}
```

**Output:**
```
=== CALCOLO LUNGHEZZE ===

'Ciao' → lunghezza: 4
'Programmazione' → lunghezza: 14
'C' → lunghezza: 1
'Hello World!' → lunghezza: 12
```

</details>

---

## Esercizio 12: Copia Stringa con Puntatori (20 min)

Implementa `void copiaStringa(char* dest, char* src)` senza usare `strcpy()`.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

void copiaStringa(char* dest, char* src) {
    while (*src != '\0') {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';  // Terminatore
}

// Versione compatta
void copiaStringaCompatta(char* dest, char* src) {
    while ((*dest++ = *src++) != '\0');
}

int main() {
    char originale[] = "Programmazione in C";
    char copia1[100];
    char copia2[100];
    
    copiaStringa(copia1, originale);
    copiaStringaCompatta(copia2, originale);
    
    printf("Originale: '%s'\n", originale);
    printf("Copia 1:   '%s'\n", copia1);
    printf("Copia 2:   '%s'\n", copia2);
    
    return 0;
}
```

**Output:**
```
Originale: 'Programmazione in C'
Copia 1:   'Programmazione in C'
Copia 2:   'Programmazione in C'
```

</details>

---

## Esercizio 13: Confronta Stringhe con Puntatori (20 min)

Implementa `int confrontaStringhe(char* str1, char* str2)` che ritorna:
- 0 se uguali
- valore < 0 se str1 < str2
- valore > 0 se str1 > str2

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

int confrontaStringhe(char* str1, char* str2) {
    while (*str1 != '\0' && *str2 != '\0') {
        if (*str1 != *str2) {
            return *str1 - *str2;
        }
        str1++;
        str2++;
    }
    return *str1 - *str2;
}

int main() {
    char* coppie[][2] = {
        {"Ciao", "Ciao"},
        {"Anna", "Antonio"},
        {"Zebra", "Alpaca"},
        {"ABC", "ABCD"}
    };
    
    printf("=== CONFRONTO STRINGHE ===\n\n");
    
    for (int i = 0; i < 4; i++) {
        int risultato = confrontaStringhe(coppie[i][0], coppie[i][1]);
        
        printf("'%s' vs '%s' → ", coppie[i][0], coppie[i][1]);
        
        if (risultato == 0) {
            printf("UGUALI\n");
        } else if (risultato < 0) {
            printf("'%s' viene PRIMA\n", coppie[i][0]);
        } else {
            printf("'%s' viene DOPO\n", coppie[i][0]);
        }
    }
    
    return 0;
}
```

**Output:**
```
=== CONFRONTO STRINGHE ===

'Ciao' vs 'Ciao' → UGUALI
'Anna' vs 'Antonio' → 'Anna' viene PRIMA
'Zebra' vs 'Alpaca' → 'Zebra' viene DOPO
'ABC' vs 'ABCD' → 'ABC' viene PRIMA
```

</details>

---

## Esercizio 14: Conta Vocali con Puntatori (20 min)

Implementa `int contaVocali(char* str)` che conta le vocali (a, e, i, o, u, maiuscole e minuscole).

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

int contaVocali(char* str) {
    int contatore = 0;
    
    while (*str != '\0') {
        char c = *str;
        
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            contatore++;
        }
        
        str++;
    }
    
    return contatore;
}

int main() {
    char* frasi[] = {
        "Ciao mondo",
        "Programmazione in C",
        "AEIOU",
        "xyz"
    };
    
    printf("=== CONTA VOCALI ===\n\n");
    
    for (int i = 0; i < 4; i++) {
        int vocali = contaVocali(frasi[i]);
        printf("'%s' → %d vocali\n", frasi[i], vocali);
    }
    
    return 0;
}
```

**Output:**
```
=== CONTA VOCALI ===

'Ciao mondo' → 4 vocali
'Programmazione in C' → 8 vocali
'AEIOU' → 5 vocali
'xyz' → 0 vocali
```

</details>

---

## Esercizio 15: Maiuscolo/Minuscolo con Puntatori (25 min)

Implementa due funzioni:
- `void maiuscolo(char* str)` — converte in maiuscolo
- `void minuscolo(char* str)` — converte in minuscolo

**Hint:** Le lettere minuscole hanno valori ASCII maggiori di 32 rispetto alle maiuscole.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

void maiuscolo(char* str) {
    while (*str != '\0') {
        if (*str >= 'a' && *str <= 'z') {
            *str = *str - 32;  // Converti in maiuscolo
        }
        str++;
    }
}

void minuscolo(char* str) {
    while (*str != '\0') {
        if (*str >= 'A' && *str <= 'Z') {
            *str = *str + 32;  // Converti in minuscolo
        }
        str++;
    }
}

int main() {
    char str1[] = "Ciao Mondo!";
    char str2[] = "Programmazione IN C";
    char str3[] = "HeLLo WoRLd 123";
    
    printf("=== CONVERSIONI ===\n\n");
    
    // Test maiuscolo
    printf("Originale: '%s'\n", str1);
    maiuscolo(str1);
    printf("Maiuscolo: '%s'\n\n", str1);
    
    // Test minuscolo
    printf("Originale: '%s'\n", str2);
    minuscolo(str2);
    printf("Minuscolo: '%s'\n\n", str2);
    
    // Test combinato
    printf("Originale: '%s'\n", str3);
    maiuscolo(str3);
    printf("Maiuscolo: '%s'\n", str3);
    minuscolo(str3);
    printf("Minuscolo: '%s'\n", str3);
    
    return 0;
}
```

**Output:**
```
=== CONVERSIONI ===

Originale: 'Ciao Mondo!'
Maiuscolo: 'CIAO MONDO!'

Originale: 'Programmazione IN C'
Minuscolo: 'programmazione in c'

Originale: 'HeLLo WoRLd 123'
Maiuscolo: 'HELLO WORLD 123'
Minuscolo: 'hello world 123'
```

</details>

---

## ESERCIZI BONUS

### Bonus 1: Concatena Stringhe (20 min)
Implementa `void concatena(char* dest, char* src)` che aggiunge `src` alla fine di `dest`.

### Bonus 2: Cerca Carattere (15 min)
Implementa `char* cercaCarattere(char* str, char c)` che ritorna un puntatore alla prima occorrenza di `c` in `str`, o `NULL` se non trovato.

### Bonus 3: Inverti Stringa (20 min)
Implementa `void invertiStringa(char* str)` che inverte la stringa in place usando due puntatori.

### Bonus 4: Sostituisci Carattere (20 min)
Implementa `int sostituisci(char* str, char vecchio, char nuovo)` che sostituisce tutte le occorrenze e ritorna il numero di sostituzioni.

### Bonus 5: Filtra Array (25 min)
Implementa `int filtraPari(int* src, int* dest, int dim)` che copia solo gli elementi pari da `src` a `dest` e ritorna quanti ne ha copiati.

---

## Domande di Verifica

1. **Cosa restituisce l'operatore `&`?**
2. **Cosa fa l'operatore `*`?**
3. **Perché `arr[2]` è equivalente a `*(arr+2)`?**
4. **Come si passa una variabile per riferimento?**
5. **Qual è la differenza tra `char str[]` e `char* str`?**

<details>
<summary><b>📝 RISPOSTE</b></summary>

1. L'**indirizzo di memoria** di una variabile
2. **Dereferenzia** un puntatore (accede al valore puntato)
3. Il compilatore traduce `arr[i]` in `*(arr + i)` automaticamente
4. Si passa l'**indirizzo** con `&` e la funzione riceve un **puntatore**
5. `char str[]` è modificabile (stack), `char* str` punta a memoria read-only

</details>

---

**Complimenti! Hai completato tutti gli esercizi sui puntatori! 🎉**



---

# 16 guida didattica puntatori

**File:** `16 guida didattica puntatori.md`
**Tipo:** `.md`
**Dimensione:** 24.6 KB
**Ultima modifica:** 02/07/2026 09:24

---

# GUIDA DIDATTICA - LEZIONE 19
## Puntatori in C

### DURATA TOTALE: 4 ORE

---

## STRUTTURA DELLA LEZIONE

### Parte 1: INTRODUZIONE E CONCETTO (30 minuti)
- Cos'è un puntatore
- Analogia della memoria
- Perché sono importanti

### Parte 2: SINTASSI E OPERATORI (60 minuti)
- Operatori & e *
- Dichiarazione e inizializzazione
- Puntatori e costanti
- Errori comuni

### Parte 3: PUNTATORI E ARRAY (60 minuti)
- Relazione array-puntatori
- Aritmetica dei puntatori
- Notazione equivalente
- Iterazione con puntatori

### Parte 4: PASSAGGIO PER RIFERIMENTO (45 minuti)
- Problema del passaggio per valore
- Soluzione con puntatori
- Funzioni che modificano variabili
- Restituzione multipli valori

### Parte 5: PUNTATORI E STRINGHE (45 minuti)
- Stringhe come puntatori
- Funzioni con stringhe
- Array di stringhe

---

## PARTE 1: INTRODUZIONE E CONCETTO (30 minuti)

### 1.1 Motivazione (5 min)

**Problema con le funzioni normali:**

```c
void incrementa(int x) {
    x++;
    printf("Dentro funzione: x = %d\n", x);
}

int main() {
    int numero = 10;
    incrementa(numero);
    printf("Fuori funzione: numero = %d\n", numero);
    return 0;
}
```

**Output:**
```
Dentro funzione: x = 11
Fuori funzione: numero = 10  ← Non è cambiato!
```

> "La funzione riceve una COPIA del valore, non può modificare l'originale. I puntatori risolvono questo problema!"

---

### 1.2 Cos'è un Puntatore? (10 min)

**Definizione:**
> Un **puntatore** è una variabile che contiene l'**indirizzo di memoria** di un'altra variabile.

**Analogia dell'edificio:**

```
La memoria è come un EDIFICIO con appartamenti:

┌─────────────┐
│  0x1000     │ ← Appartamento 1000
│  [int x=42] │    Contiene il valore 42
├─────────────┤
│  0x1004     │ ← Appartamento 1004
│  [int y=10] │    Contiene il valore 10
├─────────────┤
│  0x1008     │ ← Appartamento 1008
│  [int* p]   │    Contiene l'indirizzo 0x1000
│  =0x1000    │    (punta ad x!)
└─────────────┘

Un puntatore è come un POST-IT che dice:
"Il valore che cerchi è nell'appartamento 1000"
```

**In sintesi:**
- Una variabile **normale** contiene un **valore**
- Un **puntatore** contiene un **indirizzo**

---

### 1.3 Perché Sono Importanti? (10 min)

**I puntatori permettono di:**

1. **Modificare variabili nelle funzioni** (passaggio per riferimento)
   ```c
   void modifica(int* p) {
       *p = 100;  // Cambia l'originale!
   }
   ```

2. **Gestire array in modo efficiente**
   ```c
   void stampaArray(int* arr, int dim) {
       for (int i = 0; i < dim; i++) {
           printf("%d ", arr[i]);
       }
   }
   ```

3. **Manipolare stringhe**
   ```c
   char* str = "Ciao";
   while (*str != '\0') {
       printf("%c", *str);
       str++;
   }
   ```

4. **Creare strutture dati dinamiche** (liste, alberi, grafi)
   - Vedremo in seguito con `malloc` e allocazione dinamica

5. **Evitare copie di grandi struct**
   ```c
   void stampaStudente(Studente* s) {  // Passa solo l'indirizzo!
       printf("%s\n", s->nome);
   }
   ```

---

### 1.4 Visualizzazione Iniziale (5 min)

Scrivi alla lavagna questo schema:

```
VARIABILE vs PUNTATORE

┌──────────────────┐
│ Variabile int x  │
├──────────────────┤
│ Indirizzo: 0x1000│
│ Valore:    42    │
└──────────────────┘

┌──────────────────┐
│ Puntatore int* p │
├──────────────────┤
│ Indirizzo: 0x1008│
│ Valore:    0x1000│ ← Contiene l'indirizzo di x!
└──────────────────┘

p "punta" a x:
  p      → contiene 0x1000
  *p     → vale 42 (il valore di x)
  &x     → vale 0x1000 (l'indirizzo di x)
```

## PARTE 2: SINTASSI E OPERATORI (60 minuti)

### 2.1 Operatore & (address-of) — 10 min

**Significato:** Ottiene l'**indirizzo** di una variabile.

```c
int x = 42;
printf("Valore di x: %d\n", x);         // 42
printf("Indirizzo di x: %p\n", &x);     // 0x7fff... (esempio)
```

**Sintassi:**
```c
&variabile  → restituisce l'indirizzo
```

**Analogia:**
> "`&x` è come dire: 'Qual è l'indirizzo di casa di x?'"

**Visualizzazione:**

```
int x = 42;

x      → valore 42
&x     → indirizzo 0x1000

┌─────────────┐
│ x           │
│ indirizzo:  │ ← &x restituisce questo
│   0x1000    │
│ valore:     │
│   42        │ ← x restituisce questo
└─────────────┘
```

**⚠️ NOTA:** L'indirizzo `%p` viene stampato in esadecimale.

---

### 2.2 Operatore * (dereference) — 15 min

**Significato:** Accede al **valore** puntato da un puntatore.

```c
int x = 42;
int* p = &x;  // p contiene l'indirizzo di x

printf("Valore di p: %p\n", p);        // 0x1000 (indirizzo di x)
printf("Valore puntato: %d\n", *p);    // 42 (valore di x)
```

**Sintassi:**
```c
*puntatore  → restituisce il valore puntato
```

**Analogia:**
> "`*p` è come dire: 'Vai all'indirizzo scritto su p e leggimi il valore che c'è dentro'"

---

**Visualizzazione completa:**

```c
int numero = 42;
int* puntatore = &numero;
```

```
┌─────────────────┐        ┌─────────────────┐
│ numero          │◄───────│ puntatore       │
│ ind:   0x1000   │        │ ind:   0x1008   │
│ valore: 42      │        │ valore: 0x1000  │
└─────────────────┘        └─────────────────┘

numero          → 42
&numero         → 0x1000
puntatore       → 0x1000
*puntatore      → 42  (stesso di numero!)
&puntatore      → 0x1008
```

**Modifica attraverso puntatore:**

```c
*puntatore = 100;  // Modifica il valore di numero!

printf("numero = %d\n", numero);      // 100
printf("*puntatore = %d\n", *puntatore);  // 100
```

Ora:
```
┌─────────────────┐        ┌─────────────────┐
│ numero          │◄───────│ puntatore       │
│ ind:   0x1000   │        │ ind:   0x1008   │
│ valore: 100     │ ← Modificato!
└─────────────────┘        └─────────────────┘
```


### 2.3 Dichiarazione di Puntatori — 10 min

**Sintassi:**
```c
tipo* nomePuntatore;
```

**Esempi:**

```c
int* p1;       // Puntatore a int
float* p2;     // Puntatore a float
char* p3;      // Puntatore a char (stringa)
double* p4;    // Puntatore a double
```

**⚠️ ATTENZIONE — Dichiarazioni multiple:**

```c
// SBAGLIATO (solo p è puntatore, q è int normale):
int* p, q;

// CORRETTO (entrambi puntatori):
int *p, *q;     // Stile 1
int* p;         // Stile 2 (più chiaro)
int* q;
```

**Stile consigliato:**
```c
int* p;  // Asterisco vicino al tipo
int* q;  // Una dichiarazione per riga → più chiaro
```

---

### 2.4 Inizializzazione di Puntatori — 15 min

**Buone pratiche:**

```c
// 1. Inizializzazione a NULL (sicuro)
int* p = NULL;  // Puntatore nullo (non punta a nulla)

if (p == NULL) {
    printf("Puntatore non valido\n");
}

// 2. Inizializzazione con indirizzo
int x = 10;
int* p = &x;    // p punta a x

printf("%d\n", *p);  // 10

// 3. Assegnamento successivo
int y = 20;
int* q;
q = &y;         // OK
printf("%d\n", *q);  // 20
```

---

**⚠️ ERRORI COMUNI — Leggili ad alta voce!**

```c
// ERRORE 1: Puntatore non inizializzato
int* p;
*p = 42;  // ❌ CRASH! p contiene un indirizzo casuale (garbage)

// ERRORE 2: Dereferenziare NULL
int* p = NULL;
*p = 42;  // ❌ CRASH! Segmentation fault

// ERRORE 3: Confondere valore e indirizzo
int x = 10;
int* p = x;  // ❌ ERRORE! p deve contenere un indirizzo, non un valore
// Corretto: int* p = &x;

// ERRORE 4: Assegnare valore invece di indirizzo
int* p;
int x = 10;
p = x;  // ❌ ERRORE! Assegna valore a puntatore
// Corretto: p = &x;
```

**Regola d'oro:**
> "Un puntatore deve sempre contenere un **indirizzo**, mai un valore diretto."

---

### 2.5 Puntatori e Costanti — 10 min

**Tre casi da distinguere:**

**1. Puntatore a costante** (il valore non può essere modificato):
```c
int x = 10, y = 20;
const int* p1 = &x;

// *p1 = 15;  // ❌ ERRORE! Non si può modificare *p1
p1 = &y;      // ✅ OK, il puntatore può cambiare
```

**2. Puntatore costante** (il puntatore non può cambiare):
```c
int x = 10, y = 20;
int* const p2 = &x;

*p2 = 15;     // ✅ OK, si può modificare il valore
// p2 = &y;   // ❌ ERRORE! Il puntatore è fisso
```

**3. Puntatore costante a costante** (nulla può cambiare):
```c
int x = 10, y = 20;
const int* const p3 = &x;

// *p3 = 15;  // ❌ ERRORE!
// p3 = &y;   // ❌ ERRORE!
```

**Mnemonic:**
- `const` prima di `*` → il **valore** è costante
- `const` dopo `*` → il **puntatore** è costante

```
const int* p;       → valore costante
int* const p;       → puntatore costante
const int* const p; → entrambi costanti
```


---

## PARTE 3: PUNTATORI E ARRAY (60 minuti)

### 3.1 Array e Puntatori — Relazione Fondamentale (15 min)

**Fatto importante:**
> In C, il **nome di un array** è un **puntatore costante** al primo elemento.

```c
int arr[] = {10, 20, 30, 40, 50};

// arr è equivalente a &arr[0]
printf("%p\n", arr);        // Indirizzo del primo elemento
printf("%p\n", &arr[0]);    // Stesso indirizzo!
```

**Quindi:**
```c
int* p = arr;  // ✅ OK (senza &)

// È equivalente a:
int* p = &arr[0];
```

---

**Visualizzazione in memoria:**

```
Array: int arr[] = {10, 20, 30, 40, 50};

Indirizzo  Valore  Notazione
─────────────────────────────
0x1000     10      arr[0]  = *arr       = *(arr+0)
0x1004     20      arr[1]  = *(arr+1)
0x1008     30      arr[2]  = *(arr+2)
0x100C     40      arr[3]  = *(arr+3)
0x1010     50      arr[4]  = *(arr+4)
 ↑
arr (punta qui)
```

**Accesso equivalente:**

```c
arr[2]  ==  *(arr + 2)  ==  *(2 + arr)  ==  2[arr]

// Tutti accedono al terzo elemento (30)!
```

> "Il compilatore traduce `arr[i]` in `*(arr + i)` automaticamente."

---

### 3.2 Aritmetica dei Puntatori (20 min)

**Operazioni valide:**
- `p + n` : sposta il puntatore avanti di **n elementi**
- `p - n` : sposta il puntatore indietro di **n elementi**
- `p++` : sposta al **prossimo** elemento
- `p--` : sposta all'elemento **precedente**
- `p1 - p2` : **distanza** tra due puntatori (in elementi)

---

**IMPORTANTE — Il salto dipende dal tipo:**

```c
int arr[] = {10, 20, 30, 40, 50};
int* p = arr;

printf("Indirizzo p:     %p\n", p);
printf("Indirizzo p+1:   %p\n", p+1);
printf("Indirizzo p+2:   %p\n", p+2);
```

**Output:**
```
Indirizzo p:     0x1000
Indirizzo p+1:   0x1004  ← +4 byte (sizeof(int))
Indirizzo p+2:   0x1008  ← +8 byte totali
```

> "`p+1` NON è `indirizzo+1`, ma `indirizzo + sizeof(tipo)`"

---

**Esempio pratico:**

```c
int numeri[] = {10, 20, 30, 40, 50};
int* p = numeri;

printf("%d\n", *p);       // 10 (primo elemento)
printf("%d\n", *(p+1));   // 20 (secondo elemento)
printf("%d\n", *(p+2));   // 30 (terzo elemento)

p++;  // Sposta al prossimo elemento
printf("%d\n", *p);       // 20

p += 2;  // Sposta di 2 posizioni
printf("%d\n", *p);       // 40
```

---

**Differenza tra puntatori:**

```c
int arr[] = {10, 20, 30, 40, 50};
int* p1 = &arr[0];
int* p2 = &arr[4];

int distanza = p2 - p1;
printf("Distanza: %d elementi\n", distanza);  // 4
```

---

### 3.3 Iterazione con Puntatori (15 min)

**Tre modi per iterare su un array:**

**Metodo 1: Indice classico**
```c
int arr[] = {10, 20, 30, 40, 50};
for (int i = 0; i < 5; i++) {
    printf("%d ", arr[i]);
}
```

**Metodo 2: Aritmetica dei puntatori**
```c
int arr[] = {10, 20, 30, 40, 50};
for (int i = 0; i < 5; i++) {
    printf("%d ", *(arr + i));
}
```

**Metodo 3: Incremento del puntatore**
```c
int arr[] = {10, 20, 30, 40, 50};
int* p = arr;
int* fine = arr + 5;

while (p < fine) {
    printf("%d ", *p);
    p++;
}
```

**Metodo 4: Stile compatto**
```c
int arr[] = {10, 20, 30, 40, 50};
int* p = arr;

for (int i = 0; i < 5; i++) {
    printf("%d ", *p++);  // Stampa e poi incrementa
}
```

---

### 3.4 Array vs Puntatore — Differenze Importanti (10 min)

**Somiglianze:**
```c
int arr[5];
int* p = arr;

arr[2] == p[2] == *(arr+2) == *(p+2)  // ✅ Tutti uguali
```

**Differenze:**

| | Array | Puntatore |
|---|---|---|
| **Modifica** | ❌ `arr++` errore | ✅ `p++` ok |
| **sizeof** | Dimensione totale | Dimensione puntatore |
| **Tipo** | Puntatore costante | Variabile |

```c
int arr[5] = {1, 2, 3, 4, 5};
int* p = arr;

// arr è COSTANTE, p è VARIABILE
p++;       // ✅ OK: p ora punta al secondo elemento
// arr++;  // ❌ ERRORE! Non si può modificare arr

// sizeof comportamento diverso
printf("%lu\n", sizeof(arr));  // 20 (5 * 4 byte)
printf("%lu\n", sizeof(p));    // 8 (dimensione puntatore su 64-bit)
```

---

## PARTE 4: PASSAGGIO PER RIFERIMENTO (45 minuti)

### 4.1 Problema del Passaggio per Valore (10 min)

**Situazione:**

```c
void incrementa(int x) {
    x++;
    printf("Dentro funzione: x = %d\n", x);
}

int main() {
    int numero = 10;
    incrementa(numero);
    printf("Fuori funzione: numero = %d\n", numero);
    return 0;
}
```

**Output:**
```
Dentro funzione: x = 11
Fuori funzione: numero = 10  ← NON è cambiato!
```

**Perché?**
> La funzione riceve una **copia** del valore. Modificare `x` dentro la funzione non modifica `numero` nel `main()`.

**Visualizzazione:**

```
main():                  incrementa():
┌──────────┐            ┌──────────┐
│ numero   │            │ x        │
│ = 10     │ ─copia─→   │ = 10     │
└──────────┘            └──────────┘
                             ↓ x++
                        ┌──────────┐
                        │ x        │
                        │ = 11     │
                        └──────────┘
                        
numero rimane 10 (la copia è sparita)
```

---

### 4.2 Soluzione: Passaggio per Riferimento (15 min)

**Strategia:** Passa l'**indirizzo** invece del valore.

```c
void incrementa(int* x) {
    (*x)++;  // Modifica il valore puntato
    printf("Dentro funzione: *x = %d\n", *x);
}

int main() {
    int numero = 10;
    incrementa(&numero);  // Passa l'indirizzo
    printf("Fuori funzione: numero = %d\n", numero);
    return 0;
}
```

**Output:**
```
Dentro funzione: *x = 11
Fuori funzione: numero = 11  ← È cambiato! ✓
```

**Visualizzazione:**

```
main():                  incrementa():
┌──────────┐            ┌──────────┐
│ numero   │◄───────────│ x        │
│ = 10     │   punta    │ = &numero│
│ @0x1000  │            └──────────┘
└──────────┘                  ↓ (*x)++
┌──────────┐
│ numero   │ ← Modificato direttamente!
│ = 11     │
│ @0x1000  │
└──────────┘
```

**Sintassi:**
```c
// Dichiarazione
void funzione(int* parametro);

// Chiamata
funzione(&variabile);

// Uso interno
*parametro = nuovoValore;
```

---

### 4.3 Esempio: Swap di Due Variabili (10 min)

**Implementazione SBAGLIATA (per valore):**

```c
void swapSbagliato(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    // Scambia solo le copie locali!
}
```

**Implementazione CORRETTA (per riferimento):**

```c
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 10, y = 20;
    printf("Prima: x=%d, y=%d\n", x, y);
    
    swap(&x, &y);  // Passa gli indirizzi
    
    printf("Dopo: x=%d, y=%d\n", x, y);
    return 0;
}
```

**Output:**
```
Prima: x=10, y=20
Dopo: x=20, y=10  ← Scambiati! ✓
```

---

### 4.4 Restituzione di Multipli Valori (10 min)

**Problema:** In C una funzione può tornare **UN SOLO** valore.

**Soluzione:** Usa puntatori per "tornare" più valori.

**Esempio: Divisione con quoziente e resto**

```c
void divisioneCompleta(int dividendo, int divisore,
                        int* quoziente, int* resto) {
    *quoziente = dividendo / divisore;
    *resto = dividendo % divisore;
}

int main() {
    int q, r;
    divisioneCompleta(17, 5, &q, &r);
    
    printf("17 / 5 = %d con resto %d\n", q, r);
    // Output: 17 / 5 = 3 con resto 2
    
    return 0;
}
```

**Come funziona:**

```
main():
┌────┐  ┌────┐
│ q  │  │ r  │
└────┘  └────┘
  ↑       ↑
  │       │
divisioneCompleta(..., &q, &r)
  │       │
  │       └─ scrive il resto in r
  └───────── scrive il quoziente in q
```


---

## PARTE 5: PUNTATORI E STRINGHE (45 minuti)

### 5.1 Stringhe come Puntatori (10 min)

**Fatto:**
> In C, le stringhe sono **array di char**, quindi **puntatori a char**.

**Due modi di dichiarare stringhe:**

```c
// Modo 1: Array di caratteri (modificabile)
char str1[] = "Ciao";
str1[0] = 'c';  // ✅ OK: posso modificare

// Modo 2: Puntatore a stringa letterale (NON modificabile)
char* str2 = "Ciao";
// str2[0] = 'c';  // ❌ ERRORE: stringa in memoria read-only
```

**Differenza:**

| | `char str[]` | `char* str` |
|---|---|---|
| **Memoria** | Stack | Read-only (costante) |
| **Modificabile** | ✅ Sì | ❌ No |
| **Uso** | Buffers, manipolazione | Stringhe costanti |

---

### 5.2 Iterare su Stringhe con Puntatori (15 min)

**Metodo 1: Indice**
```c
char stringa[] = "Hello";
for (int i = 0; i < strlen(stringa); i++) {
    printf("%c ", stringa[i]);
}
```

**Metodo 2: Puntatore**
```c
char stringa[] = "Hello";
char* p = stringa;

while (*p != '\0') {  // Finché non raggiungi il terminatore
    printf("%c ", *p);
    p++;
}
```

**Output entrambi:**
```
H e l l o
```

---

**Esempio: Calcola lunghezza stringa**

```c
int lunghezza(char* str) {
    int len = 0;
    while (*str != '\0') {
        len++;
        str++;
    }
    return len;
}

int main() {
    char testo[] = "Programmazione";
    printf("Lunghezza: %d\n", lunghezza(testo));  // 14
    return 0;
}
```

---

### 5.3 Funzioni con Stringhe (10 min)

**Copia stringa:**

```c
void copiaStringa(char* dest, char* src) {
    while (*src != '\0') {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';  // Aggiungi terminatore
}

// Versione compatta
void copiaStringa2(char* dest, char* src) {
    while ((*dest++ = *src++) != '\0');
}
```

**Confronta stringhe:**

```c
int confrontaStringhe(char* str1, char* str2) {
    while (*str1 != '\0' && *str2 != '\0') {
        if (*str1 != *str2) {
            return *str1 - *str2;
        }
        str1++;
        str2++;
    }
    return *str1 - *str2;
}
```

---

### 5.4 Array di Stringhe (10 min)

**Un array di stringhe è un array di puntatori:**

```c
char* giorni[] = {
    "Lunedì",
    "Martedì",
    "Mercoledì",
    "Giovedì",
    "Venerdì",
    "Sabato",
    "Domenica"
};

for (int i = 0; i < 7; i++) {
    printf("%s\n", giorni[i]);
}
```

**Visualizzazione:**

```
giorni è un array di puntatori:

┌──────┐
│ ptr  │──→ "Lunedì"
├──────┤
│ ptr  │──→ "Martedì"
├──────┤
│ ptr  │──→ "Mercoledì"
├──────┤
...

giorni[0] punta a "Lunedì"
giorni[1] punta a "Martedì"
```

---

## RIEPILOGO E CHIUSURA (10 minuti)

### Concetti Chiave

**✓ Puntatori:**
- Contengono **indirizzi** di memoria
- `&` → ottiene l'indirizzo
- `*` → dereferenzia (accede al valore)

**✓ Array e Puntatori:**
- Il nome dell'array è un puntatore al primo elemento
- `arr[i]` è equivalente a `*(arr + i)`
- Aritmetica: `p+n` salta `n * sizeof(tipo)` byte

**✓ Passaggio per Riferimento:**
- Passa `&variabile` alla funzione
- Dentro la funzione: `*puntatore = valore`
- Permette di modificare variabili e tornare multipli valori

**✓ Stringhe:**
- Sono `char*` (puntatori a caratteri)
- Iterazione: `while (*p != '\0')`
- Array di stringhe: `char* arr[]`

---

### Errori Comuni da Evitare

```c
// ❌ Puntatore non inizializzato
int* p;
*p = 42;  // CRASH

// ❌ Dereferenziare NULL
int* p = NULL;
*p = 42;  // CRASH

// ❌ Confondere valore e indirizzo
int x = 10;
int* p = x;  // ERRORE
// Corretto: int* p = &x;

// ❌ Dimenticare le parentesi
int* p;
*p++;    // Incrementa p, poi dereferenzia (sbagliato)
(*p)++;  // Incrementa il valore puntato (corretto)
```

---

### Domande di Verifica

1. **"Cosa restituisce l'operatore `&`?"**
2. **"Cosa fa l'operatore `*`?"**
3. **"Perché `arr[2]` è equivalente a `*(arr+2)`?"**
4. **"Come si passa una variabile per riferimento?"**
5. **"Qual è la differenza tra `char str[]` e `char* str`?"**

---

<details>
<summary><b>📝 RISPOSTE PER IL DOCENTE</b></summary>

### 1. Operatore &

**Risposta:** Restituisce l'**indirizzo di memoria** di una variabile.

```c
int x = 42;
printf("%p\n", &x);  // Stampa l'indirizzo (es. 0x7fff...)
```

L'operatore `&` (address-of) è come chiedere: "Dove si trova questa variabile in memoria?"

---

### 2. Operatore *

**Risposta:** **Dereferenzia** un puntatore, cioè accede al valore nella posizione di memoria puntata.

```c
int x = 42;
int* p = &x;
printf("%d\n", *p);  // 42 (valore di x)
```

`*p` significa: "Vai all'indirizzo contenuto in `p` e leggimi il valore che c'è."

**Inoltre, `*` si usa anche per dichiarare puntatori:**
```c
int* p;  // Dichiarazione: p è un puntatore a int
```

---

### 3. Equivalenza arr[2] e *(arr+2)

**Risposta:** Il compilatore C traduce `arr[i]` in `*(arr + i)` automaticamente.

**Spiegazione:**

```c
int arr[] = {10, 20, 30, 40, 50};

arr[2]       // Notazione con indice
*(arr + 2)   // Notazione con puntatore

Entrambi accedono al terzo elemento (30).
```

**Perché?**
1. `arr` è un puntatore al primo elemento
2. `arr + 2` sposta il puntatore di 2 posizioni
3. `*(arr + 2)` dereferenzia → legge il valore

**In generale:**
```
arr[i]  ≡  *(arr + i)  ≡  *(i + arr)  ≡  i[arr]
```

Tutte queste notazioni sono **equivalenti** (anche se `i[arr]` è bizzarro!).

---

### 4. Passaggio per riferimento

**Risposta:** Si passa l'**indirizzo** della variabile usando `&`, e la funzione riceve un **puntatore**.

**Passaggi:**

1. **Dichiarazione:** funzione riceve puntatore
   ```c
   void modifica(int* p);
   ```

2. **Chiamata:** passa l'indirizzo con `&`
   ```c
   int x = 10;
   modifica(&x);
   ```

3. **Uso interno:** dereferenzia con `*`
   ```c
   void modifica(int* p) {
       *p = 100;  // Modifica x nel main
   }
   ```

**Perché funziona?**
La funzione riceve l'indirizzo di `x`, quindi può modificare direttamente il valore originale (non una copia).

---

### 5. Differenza char str[] vs char* str

**Risposta:**

**`char str[] = "Ciao"`** (array):
- Allocato nello **stack**
- **Modificabile**
- Copia la stringa in memoria locale
```c
char str1[] = "Ciao";
str1[0] = 'c';  // ✅ OK
```

**`char* str = "Ciao"`** (puntatore a letterale):
- Punta a memoria **read-only** (segmento costanti)
- **NON modificabile**
- Più efficiente (non fa copia)
```c
char* str2 = "Ciao";
str2[0] = 'c';  // ❌ CRASH: segmentation fault
```

**Quando usare quale:**
- `char str[]` → quando devi **modificare** la stringa
- `char* str` → stringhe **costanti** (es. menu, messaggi)

**Best practice per stringhe costanti:**
```c
const char* str = "Ciao";  // Rendi esplicito che è costante
```

</details>

---

## NOTE PER IL DOCENTE

### ⚠️ Punti critici da monitorare:

1. **Confusione tra `&` e `*`** — studenti invertono gli operatori
2. **Dereferenziare puntatori non inizializzati** — causa crash
3. **Dimenticare le parentesi in `(*p)++`** — precedenza operatori
4. **Modificare stringhe letterali** — comportamento indefinito
5. **Confondere array e puntatori** — `sizeof` comportamento diverso

### 💡 Suggerimenti didattici:

- Usa **diagrammi di memoria** alla lavagna per ogni esempio
- Fai **disegnare** agli studenti dove puntano i puntatori
- **Simula passo-passo** il passaggio per riferimento con frecce
- Usa **analogie concrete** (POST-IT, edificio con appartamenti)
- **Esegui codice live** mostrando gli indirizzi con `printf("%p")`

### 📊 Valutazione comprensione:

- ✅ Lo studente distingue `&` da `*`
- ✅ Lo studente inizializza correttamente i puntatori
- ✅ Lo studente itera su array con puntatori
- ✅ Lo studente passa variabili per riferimento
- ✅ Lo studente manipola stringhe con puntatori

### 🎯 Obiettivi minimi per questa lezione:

Lo studente è pronto se:
- Dichiara e inizializza puntatori senza errori
- Usa `&` per ottenere indirizzi e `*` per dereferenziare
- Passa variabili per riferimento a funzioni
- Itera su array usando puntatori
- Evita gli errori comuni (NULL, non inizializzato)

---

**Buona lezione! 🚀**



---

# 18B esercizi malloc calloc realloc

**File:** `18B esercizi malloc calloc realloc.md`
**Tipo:** `.md`
**Dimensione:** 23.2 KB
**Ultima modifica:** 02/07/2026 09:24

---

# ESERCIZI - MALLOC, CALLOC E REALLOC

### TEMPO STIMATO: 2 ore (15 esercizi)

---

**DISTRIBUZIONE CONSIGLIATA:**
- Esercizi 1-5: malloc base (40 min)
- Esercizi 6-10: calloc e array paralleli (50 min)
- Esercizi 11-15: realloc e ridimensionamento (30 min)

---

## PARTE 1: ESERCIZI MALLOC

## Esercizio 1: Array Dinamico di Interi (10 min)

Scrivi un programma che:
1. Chiede all'utente quanti numeri vuole inserire
2. Alloca un array dinamico con `malloc`
3. Legge i numeri da tastiera
4. Stampa l'array, la somma e la media
5. Libera la memoria

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;

    printf("Quanti numeri vuoi inserire? ");
    scanf("%d", &n);

    // Alloca array dinamicamente
    int* arr = (int*) malloc(n * sizeof(int));

    if (arr == NULL) {
        printf("ERRORE: Allocazione fallita!\n");
        return 1;
    }

    // Inserimento
    printf("Inserisci %d numeri:\n", n);
    for (int i = 0; i < n; i++) {
        printf("  arr[%d] = ", i);
        scanf("%d", &arr[i]);
    }

    // Stampa
    printf("\nArray: [ ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("]\n");

    // Somma e media
    int somma = 0;
    for (int i = 0; i < n; i++) {
        somma += arr[i];
    }
    float media = (float) somma / n;

    printf("Somma:  %d\n", somma);
    printf("Media:  %.2f\n", media);

    // Libera la memoria
    free(arr);
    arr = NULL;

    return 0;
}
```

**Esempio di esecuzione:**
```
Quanti numeri vuoi inserire? 5
Inserisci 5 numeri:
  arr[0] = 10
  arr[1] = 30
  arr[2] = 20
  arr[3] = 50
  arr[4] = 40

Array: [ 10 30 20 50 40 ]
Somma:  150
Media:  30.00
```

</details>

---

## Esercizio 2: Temperature della Settimana (10 min)

Alloca dinamicamente un array per 7 temperature (una per giorno), calcola:
- Media settimanale
- Giorno più caldo
- Giorno più freddo

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c

```

</details>

---

## Esercizio 3: Filtra Numeri Positivi (10 min)

1. Leggi n numeri in un array dinamico#include <stdio.h>
#include <stdlib.h>

int main() {
    int n = 7;
    char* giorni[] = {"Lunedì", "Martedì", "Mercoledì", "Giovedì", 
                      "Venerdì", "Sabato", "Domenica"};

    float* temp = (float*) malloc(n * sizeof(float));
    if (temp == NULL) {
        printf("Errore allocazione!\n");
        return 1;
    }

    printf("=== TEMPERATURE SETTIMANALI ===\n\n");
    for (int i = 0; i < n; i++) {
        printf("  %s: ", giorni[i]);
        scanf("%f", &temp[i]);
    }

    // Media
    float somma = 0;
    for (int i = 0; i < n; i++) somma += temp[i];
    float media = somma / n;

    // Max e min
    float max = temp[0], min = temp[0];
    int giornoMax = 0, giornoMin = 0;
    
    for (int i = 1; i < n; i++) {
        if (temp[i] > max) {
            max = temp[i];
            giornoMax = i;
        }
        if (temp[i] < min) {
            min = temp[i];
            giornoMin = i;
        }
    }

    printf("\n=== RISULTATI ===\n");
    printf("Media:         %.2f°C\n", media);
    printf("Giorno più caldo:  %s (%.2f°C)\n", giorni[giornoMax], max);
    printf("Giorno più freddo: %s (%.2f°C)\n", giorni[giornoMin], min);

    free(temp);
    temp = NULL;

    return 0;
}
2. Conta quanti sono positivi
3. Alloca un secondo array esattamente della dimensione necessaria
4. Copia solo i numeri positivi nel secondo array
5. Stampa entrambi e libera

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;

    printf("Quanti numeri? ");
    scanf("%d", &n);

    // Array originale
    int* arr = (int*) malloc(n * sizeof(int));
    if (arr == NULL) {
        printf("Errore allocazione!\n");
        return 1;
    }

    printf("Inserisci %d numeri:\n", n);
    for (int i = 0; i < n; i++) {
        printf("  arr[%d] = ", i);
        scanf("%d", &arr[i]);
    }

    // Conta i positivi
    int conta = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] > 0) conta++;
    }

    printf("\nNumeri positivi: %d\n\n", conta);

    // Alloca array per i positivi
    int* positivi = (int*) malloc(conta * sizeof(int));
    if (positivi == NULL) {
        free(arr);
        return 1;
    }

    // Copia solo i positivi
    int idx = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] > 0) {
            positivi[idx++] = arr[i];
        }
    }

    // Stampa
    printf("Array originale:  [ ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("]\n");

    printf("Array positivi:   [ ");
    for (int i = 0; i < conta; i++) printf("%d ", positivi[i]);
    printf("]\n");

    free(arr);
    arr = NULL;
    free(positivi);
    positivi = NULL;

    return 0;
}
```

**Esempio:**
```
Quanti numeri? 6
Inserisci 6 numeri:
  arr[0] = -5
  arr[1] = 12
  arr[2] = -3
  arr[3] = 8
  arr[4] = 0
  arr[5] = 15

Numeri positivi: 3

Array originale:  [ -5 12 -3 8 0 15 ]
Array positivi:   [ 12 8 15 ]
```

</details>

---

## Esercizio 4: Trova e Sostituisci (5 min)

Alloca un array, cerca un valore e sostituiscilo con un altro (conta quante sostituzioni fai).

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;

    printf("Dimensione array: ");
    scanf("%d", &n);

    int* arr = (int*) malloc(n * sizeof(int));
    if (arr == NULL) return 1;

    printf("Inserisci %d numeri:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int vecchio, nuovo;
    printf("\nValore da cercare: ");
    scanf("%d", &vecchio);
    printf("Valore sostitutivo: ");
    scanf("%d", &nuovo);

    int sostituzioni = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == vecchio) {
            arr[i] = nuovo;
            sostituzioni++;
        }
    }

    printf("\nSostituzioni effettuate: %d\n\n", sostituzioni);
    printf("Array modificato: [ ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("]\n");

    free(arr);
    arr = NULL;

    return 0;
}
```

</details>

---

## Esercizio 5: Copia e Inverti (5 min)

Alloca due array: uno originale e uno che è la copia invertita del primo.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;

    printf("Dimensione: ");
    scanf("%d", &n);

    int* arr = (int*) malloc(n * sizeof(int));
    int* invertito = (int*) malloc(n * sizeof(int));
    
    if (arr == NULL || invertito == NULL) {
        free(arr);
        free(invertito);
        return 1;
    }

    printf("Inserisci %d numeri:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Copia invertendo
    for (int i = 0; i < n; i++) {
        invertito[i] = arr[n - 1 - i];
    }

    printf("\nOriginale:  [ ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("]\n");

    printf("Invertito:  [ ");
    for (int i = 0; i < n; i++) printf("%d ", invertito[i]);
    printf("]\n");

    free(arr);
    free(invertito);

    return 0;
}
```

</details>

---

## PARTE 2: ESERCIZI CALLOC

## Esercizio 6: Inizializzazione con calloc (10 min)

Alloca un array con `calloc`, stampa i valori iniziali (tutti 0), poi inserisci solo nelle posizioni pari.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;

    printf("Quanti elementi? ");
    scanf("%d", &n);

    // calloc: alloca E inizializza tutto a zero
    float* arr = (float*) calloc(n, sizeof(float));

    if (arr == NULL) {
        printf("ERRORE: Allocazione fallita!\n");
        return 1;
    }

    // Stampa valori iniziali (tutti zero grazie a calloc)
    printf("\nValori iniziali:\n[ ");
    for (int i = 0; i < n; i++) {
        printf("%.1f ", arr[i]);
    }
    printf("]\n");

    // Inserisce solo nelle posizioni pari
    printf("\nInserisci i valori nelle posizioni pari:\n");
    for (int i = 0; i < n; i += 2) {
        printf("  arr[%d] = ", i);
        scanf("%f", &arr[i]);
    }

    // Stampa array finale
    printf("\nArray finale:\n[ ");
    for (int i = 0; i < n; i++) {
        printf("%.1f ", arr[i]);
    }
    printf("]\n");

    free(arr);
    arr = NULL;

    return 0;
}
```

**Esempio:**
```
Quanti elementi? 6

Valori iniziali:
[ 0.0 0.0 0.0 0.0 0.0 0.0 ]

Inserisci i valori nelle posizioni pari:
  arr[0] = 1.5
  arr[2] = 3.0
  arr[4] = 7.5

Array finale:
[ 1.5 0.0 3.0 0.0 7.5 0.0 ]
```

</details>

---

## Esercizio 7: Contatore di Voti (10 min)

Usa `calloc` per creare un array di contatori (da 0 a 10), poi conta quante volte compare ogni voto.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;

    printf("Quanti voti? ");
    scanf("%d", &n);

    // Array dei voti
    int* voti = (int*) malloc(n * sizeof(int));
    if (voti == NULL) return 1;

    // Contatori per ogni voto da 0 a 10
    // calloc: partono tutti da 0, pronti per il conteggio
    int* contatori = (int*) calloc(11, sizeof(int));
    if (contatori == NULL) {
        free(voti);
        return 1;
    }

    printf("Inserisci i voti (0-10):\n");
    for (int i = 0; i < n; i++) {
        printf("  Voto %d: ", i + 1);
        scanf("%d", &voti[i]);
    }

    // Conta le occorrenze
    for (int i = 0; i < n; i++) {
        if (voti[i] >= 0 && voti[i] <= 10) {
            contatori[voti[i]]++;
        }
    }

    // Stampa distribuzione
    printf("\n=== DISTRIBUZIONE VOTI ===\n");
    for (int v = 0; v <= 10; v++) {
        if (contatori[v] > 0) {
            printf("  Voto %2d: ", v);
            for (int i = 0; i < contatori[v]; i++) printf("█");
            printf(" (%d)\n", contatori[v]);
        }
    }

    free(voti);
    free(contatori);

    return 0;
}
```

</details>

---

## Esercizio 8: Matrice con calloc (10 min)

Simula una matrice 3x3 usando un array monodimensionale allocato con `calloc`. Inizia tutto a 0, poi chiedi all'utente di riempire solo alcune celle.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int righe = 3, colonne = 3;
    int dimensione = righe * colonne;

    // calloc: parte tutta a zero
    int* matrice = (int*) calloc(dimensione, sizeof(int));
    if (matrice == NULL) return 1;

    printf("Matrice iniziale (calloc → tutto 0):\n");
    for (int i = 0; i < righe; i++) {
        for (int j = 0; j < colonne; j++) {
            int indice = i * colonne + j;
            printf("%3d ", matrice[indice]);
        }
        printf("\n");
    }

    printf("\nQuante celle vuoi modificare? ");
    int n;
    scanf("%d", &n);

    for (int k = 0; k < n; k++) {
        int i, j, valore;
        printf("  Cella [riga][colonna] valore: ");
        scanf("%d %d %d", &i, &j, &valore);
        
        if (i >= 0 && i < righe && j >= 0 && j < colonne) {
            matrice[i * colonne + j] = valore;
        }
    }

    printf("\nMatrice finale:\n");
    for (int i = 0; i < righe; i++) {
        for (int j = 0; j < colonne; j++) {
            int indice = i * colonne + j;
            printf("%3d ", matrice[indice]);
        }
        printf("\n");
    }

    free(matrice);

    return 0;
}
```

</details>

---

## Esercizio 9: Array Paralleli - Studenti (10 min)

Usa `calloc` per creare array paralleli per nomi e voti. Stampa solo gli studenti che hanno passato (voto >= 6).

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int n;

    printf("Quanti studenti? ");
    scanf("%d", &n);
    getchar();

    // Array di puntatori per i nomi
    char** nomi = (char**) malloc(n * sizeof(char*));
    if (nomi == NULL) return 1;

    // Array di voti con calloc (partono da 0)
    float* voti = (float*) calloc(n, sizeof(float));
    if (voti == NULL) {
        free(nomi);
        return 1;
    }

    // Inserimento
    for (int i = 0; i < n; i++) {
        char buffer[100];
        printf("\nStudente %d:\n", i + 1);

        printf("  Nome: ");
        fgets(buffer, sizeof(buffer), stdin);
        buffer[strcspn(buffer, "\n")] = '\0';

        nomi[i] = (char*) malloc((strlen(buffer) + 1) * sizeof(char));
        if (nomi[i] == NULL) {
            for (int j = 0; j < i; j++) free(nomi[j]);
            free(nomi);
            free(voti);
            return 1;
        }
        strcpy(nomi[i], buffer);

        printf("  Voto: ");
        scanf("%f", &voti[i]);
        getchar();
    }

    // Stampa solo i promossi
    printf("\n=== STUDENTI PROMOSSI (voto >= 6) ===\n");
    int promossi = 0;
    for (int i = 0; i < n; i++) {
        if (voti[i] >= 6) {
            printf("  %-20s → %.2f\n", nomi[i], voti[i]);
            promossi++;
        }
    }
    printf("\nTotale promossi: %d su %d\n", promossi, n);

    // Libera tutto
    for (int i = 0; i < n; i++) {
        free(nomi[i]);
    }
    free(nomi);
    free(voti);

    return 0;
}
```

</details>

---

## Esercizio 10: Inventario Prodotti (10 min)

Array paralleli per nomi prodotti, quantità (con calloc = 0 iniziale), prezzi. Permetti di aggiungere/rimuovere quantità.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int n = 5;
    char* prodotti[] = {"Laptop", "Mouse", "Tastiera", "Monitor", "Cuffie"};
    float prezzi[] = {899.99, 29.99, 79.99, 349.99, 149.99};

    // Quantità partono da 0 (magazzino vuoto)
    int* quantita = (int*) calloc(n, sizeof(int));
    if (quantita == NULL) return 1;

    printf("=== INVENTARIO INIZIALE ===\n");
    for (int i = 0; i < n; i++) {
        printf("%d. %-15s | €%.2f | Qnt: %d\n", 
               i + 1, prodotti[i], prezzi[i], quantita[i]);
    }

    // Operazioni
    while (1) {
        printf("\n1. Aggiungi stock\n2. Rimuovi stock\n3. Visualizza\n0. Esci\n> ");
        int scelta;
        scanf("%d", &scelta);

        if (scelta == 0) break;

        if (scelta == 1 || scelta == 2) {
            printf("Prodotto (1-%d): ", n);
            int prod;
            scanf("%d", &prod);
            prod--;

            if (prod >= 0 && prod < n) {
                printf("Quantità: ");
                int q;
                scanf("%d", &q);

                if (scelta == 1) {
                    quantita[prod] += q;
                    printf("✓ Aggiunti %d %s\n", q, prodotti[prod]);
                } else {
                    if (quantita[prod] >= q) {
                        quantita[prod] -= q;
                        printf("✓ Rimossi %d %s\n", q, prodotti[prod]);
                    } else {
                        printf("✗ Stock insufficiente!\n");
                    }
                }
            }
        } else if (scelta == 3) {
            printf("\n=== INVENTARIO ATTUALE ===\n");
            for (int i = 0; i < n; i++) {
                printf("%d. %-15s | €%.2f | Qnt: %d\n", 
                       i + 1, prodotti[i], prezzi[i], quantita[i]);
            }
        }
    }

    free(quantita);

    return 0;
}
```

</details>

---

## PARTE 3: ESERCIZI REALLOC

## Esercizio 11: Array che Cresce On-Demand (10 min)

Inizia con capacità 2, raddoppia ogni volta che l'array si riempie.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int capacita = 2;
    int dimensione = 0;

    int* arr = (int*) malloc(capacita * sizeof(int));
    if (arr == NULL) return 1;

    printf("Inserisci numeri (0 per terminare):\n");

    while (1) {
        int num;
        printf("  Numero: ");
        scanf("%d", &num);

        if (num == 0) break;

        // Se pieno, raddoppia
        if (dimensione == capacita) {
            capacita *= 2;
            printf("    → Raddoppio capacità a %d...\n", capacita);

            int* temp = (int*) realloc(arr, capacita * sizeof(int));
            if (temp == NULL) {
                free(arr);
                return 1;
            }
            arr = temp;
        }

        arr[dimensione++] = num;
    }

    printf("\nArray finale (%d elementi, capacità %d):\n[ ",
           dimensione, capacita);
    for (int i = 0; i < dimensione; i++) {
        printf("%d ", arr[i]);
    }
    printf("]\n");

    free(arr);

    return 0;
}
```

</details>

---

## Esercizio 12: Ridimensiona Array (5 min)

Alloca un array, riempilo, poi chiedi all'utente una nuova dimensione e usa `realloc`.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;

    printf("Dimensione iniziale: ");
    scanf("%d", &n);

    int* arr = (int*) malloc(n * sizeof(int));
    if (arr == NULL) return 1;

    printf("Inserisci %d numeri:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("\nArray originale: [ ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("]\n");

    printf("\nNuova dimensione: ");
    int nuova;
    scanf("%d", &nuova);

    int* temp = (int*) realloc(arr, nuova * sizeof(int));
    if (temp == NULL) {
        free(arr);
        return 1;
    }
    arr = temp;

    if (nuova > n) {
        printf("Inserisci i %d nuovi elementi:\n", nuova - n);
        for (int i = n; i < nuova; i++) {
            printf("  arr[%d] = ", i);
            scanf("%d", &arr[i]);
        }
    }

    printf("\nArray ridimensionato: [ ");
    for (int i = 0; i < nuova; i++) printf("%d ", arr[i]);
    printf("]\n");

    free(arr);

    return 0;
}
```

</details>

---

## Esercizio 13: Lista Dinamica di Stringhe (10 min)

Permetti all'utente di inserire stringhe una alla volta, usando `realloc` per far crescere l'array.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int dimensione = 0;
    int capacita = 2;

    char** lista = (char**) malloc(capacita * sizeof(char*));
    if (lista == NULL) return 1;

    printf("Inserisci stringhe (invio vuoto per terminare):\n\n");

    while (1) {
        char buffer[100];
        printf("  Stringa %d: ", dimensione + 1);
        fgets(buffer, sizeof(buffer), stdin);
        buffer[strcspn(buffer, "\n")] = '\0';

        if (strlen(buffer) == 0) break;

        // Se pieno, raddoppia
        if (dimensione == capacita) {
            capacita *= 2;
            printf("    → Espando a capacità %d\n", capacita);

            char** temp = (char**) realloc(lista, capacita * sizeof(char*));
            if (temp == NULL) {
                for (int i = 0; i < dimensione; i++) free(lista[i]);
                free(lista);
                return 1;
            }
            lista = temp;
        }

        lista[dimensione] = (char*) malloc((strlen(buffer) + 1) * sizeof(char));
        if (lista[dimensione] == NULL) {
            for (int i = 0; i < dimensione; i++) free(lista[i]);
            free(lista);
            return 1;
        }
        strcpy(lista[dimensione], buffer);
        dimensione++;
    }

    printf("\n=== LISTA FINALE (%d stringhe) ===\n", dimensione);
    for (int i = 0; i < dimensione; i++) {
        printf("%d. %s\n", i + 1, lista[i]);
    }

    for (int i = 0; i < dimensione; i++) free(lista[i]);
    free(lista);

    return 0;
}
```

</details>

---

## Esercizio 14: Compatta Array (5 min)

Alloca un array, rimuovi tutti gli elementi negativi usando `realloc` per ridurre la dimensione.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;

    printf("Dimensione: ");
    scanf("%d", &n);

    int* arr = (int*) malloc(n * sizeof(int));
    if (arr == NULL) return 1;

    printf("Inserisci %d numeri:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("\nArray originale: [ ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("]\n");

    // Compatta rimuovendo negativi
    int nuovaDim = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] >= 0) {
            arr[nuovaDim++] = arr[i];
        }
    }

    printf("Negativi rimossi: %d\n", n - nuovaDim);

    // Riduci dimensione
    int* temp = (int*) realloc(arr, nuovaDim * sizeof(int));
    if (temp == NULL && nuovaDim > 0) {
        free(arr);
        return 1;
    }
    arr = temp;

    printf("\nArray compattato: [ ");
    for (int i = 0; i < nuovaDim; i++) printf("%d ", arr[i]);
    printf("]\n");

    free(arr);

    return 0;
}
```

</details>

---

## Esercizio 15: Buffer Circolare con realloc (10 min)

Simula un buffer in cui aggiungi elementi, rimuovi elementi, visualizza elementi che può espandersi: quando si riempie, raddoppia con `realloc`.

Comandi: 1=Aggiungi 2=Rimuovi 3=Visualizza 0=Esci

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int capacita = 3;
    int dimensione = 0;

    int* buffer = (int*) malloc(capacita * sizeof(int));
    if (buffer == NULL) return 1;

    printf("=== BUFFER DINAMICO ===\n");
    printf("Comandi: 1=Aggiungi 2=Rimuovi 3=Visualizza 0=Esci\n\n");

    while (1) {
        printf("> ");
        int cmd;
        scanf("%d", &cmd);

        if (cmd == 0) break;

        if (cmd == 1) {
            // Aggiungi
            if (dimensione == capacita) {
                capacita *= 2;
                printf("  Buffer pieno → espando a capacità %d\n", capacita);

                int* temp = (int*) realloc(buffer, capacita * sizeof(int));
                if (temp == NULL) {
                    free(buffer);
                    return 1;
                }
                buffer = temp;
            }

            printf("  Valore: ");
            int val;
            scanf("%d", &val);
            buffer[dimensione++] = val;
            printf("  ✓ Aggiunto (size=%d/%d)\n", dimensione, capacita);

        } else if (cmd == 2) {
            // Rimuovi
            if (dimensione > 0) {
                dimensione--;
                printf("  ✓ Rimosso (size=%d/%d)\n", dimensione, capacita);
            } else {
                printf("  ✗ Buffer vuoto!\n");
            }

        } else if (cmd == 3) {
            // Visualizza
            printf("  Buffer (%d/%d): [ ", dimensione, capacita);
            for (int i = 0; i < dimensione; i++) {
                printf("%d ", buffer[i]);
            }
            printf("]\n");
        }
    }

    free(buffer);

    return 0;
}
```

</details>

---

## Riepilogo: Cosa Hai Praticato

| Esercizio | malloc | calloc | realloc | Tecnica |
|-----------|--------|--------|---------|---------|
| 1 | ✅ | | | Input dinamico |
| 2 | ✅ | | | Trova max/min |
| 3 | ✅ | | | Filtraggio con secondo array |
| 4 | ✅ | | | Ricerca e sostituzione |
| 5 | ✅ | | | Copia invertita |
| 6 | | ✅ | | Posizioni pari/dispari |
| 7 | | ✅ | | Contatori |
| 8 | | ✅ | | Matrice monodimensionale |
| 9 | ✅ | ✅ | | Array paralleli |
| 10 | | ✅ | | Inventario con operazioni |
| 11 | ✅ | | ✅ | Crescita automatica |
| 12 | ✅ | | ✅ | Ridimensionamento manuale |
| 13 | ✅ | | ✅ | Lista stringhe dinamica |
| 14 | ✅ | | ✅ | Compattazione |
| 15 | ✅ | | ✅ | Buffer espandibile |

---

## Checklist Finale

**Prima di ogni esercizio, ricorda:**
```
✓ Includi <stdlib.h>
✓ Controlla sempre se malloc/calloc/realloc ritornano NULL
✓ Usa sizeof(tipo) per calcolare i byte
✓ Per realloc, usa una variabile temporanea
✓ Fai free() prima di uscire dal programma
✓ Imposta il puntatore a NULL dopo free
```

**Complimenti! Ora padroneggi l'allocazione dinamica in C! 🎉**



---

# 18B guida didattica array dinamici

**File:** `18B guida didattica array dinamici.md`
**Tipo:** `.md`
**Dimensione:** 32.1 KB
**Ultima modifica:** 02/07/2026 09:24

---

# GUIDA DIDATTICA - LEZIONE 20
## Array Dinamici in C: malloc e calloc

### DURATA TOTALE: 5 ORE (con realloc)

---

## STRUTTURA DELLA LEZIONE

### Parte 1: MOTIVAZIONE (30 minuti)
- Limite degli array statici
- Concetto di allocazione dinamica
- Stack vs Heap

### Parte 2: MALLOC (60 minuti)
- Sintassi e parametri
- sizeof e calcolo dei byte
- Controllo NULL
- free e buone pratiche

### Parte 3: CALLOC (45 minuti)
- Sintassi e differenze da malloc
- Quando usare calloc
- Esempi pratici

### Parte 4: REALLOC (45 minuti)
- Ridimensionare la memoria
- Sintassi e comportamento
- Array dinamici che crescono

### Parte 5: PRATICA GUIDATA (60 minuti)
- Tre esercizi costruiti insieme alla classe

### Parte 6: ERRORI COMUNI E RIEPILOGO (45 minuti)
- Memory leak
- Dangling pointer
- Double free
- Riepilogo e domande

---

## PARTE 1: MOTIVAZIONE (30 minuti)

### 1.1 Il Problema degli Array Statici (10 min)

Scrivi questo codice alla lavagna e chiedi alla classe cosa non va:

```c
int voti[30];  // Cosa succede se ho 31 studenti?
               // Cosa succede se ho solo 5 studenti?
```

**Problema 1 — Dimensione fissa troppo piccola:**
```c
#define MAX 30
int voti[MAX];

// Arriva il 31° studente...
// Non c'è spazio! Non possiamo fare nulla.
```

**Problema 2 — Spreco di memoria:**
```c
int voti[1000];  // Alloco spazio per 1000 studenti

// Oggi ci sono solo 5 studenti.
// 995 spazi allocati per nulla!
```

**Problema 3 — Dimensione non nota a priori:**
```c
// L'utente decide quanti elementi vuole a runtime.
// Con un array statico non possiamo saperlo
// prima di eseguire il programma.

printf("Quanti voti? ");
int n;
scanf("%d", &n);

int voti[n];  // ⚠️ VLA: tecnicamente permesso in C99
              // ma sconsigliato: non funziona su tutti i compilatori
              // e non è mai sicuro per dimensioni grandi
```

> "Ci serve un modo per allocare la **quantità esatta** di memoria necessaria, decidendo **durante l'esecuzione**."

---

### 1.2 Memoria Statica vs Dinamica (10 min)

**Dove vivono le variabili in C?**

```
┌──────────────────────────────────────────┐
│                MEMORIA                   │
├──────────────────────────────────────────┤
│  STACK (pila delle chiamate)             │
│  • Variabili locali                      │
│  • Parametri delle funzioni              │
│  • Gestita automaticamente               │
│  • Dimensione limitata (~1-8 MB)         │
│                                          │
│  int x = 10;      → qui                  │
│  int arr[5];      → qui                  │
├──────────────────────────────────────────┤
│  HEAP (memoria libera)                   │
│  • Allocazione dinamica con malloc/calloc│
│  • Gestita MANUALMENTE dal programmatore │
│  • Dimensione molto grande (GB)          │
│  • Deve essere liberata con free()       │
│                                          │
│  malloc(...)      → alloca qui           │
│  calloc(...)      → alloca qui           │
└──────────────────────────────────────────┘
```

**Schema con esempio concreto:**

```
Codice:                   Memoria durante l'esecuzione:

int n = 5;                STACK:
int* arr = malloc(...);   ┌─────────────────┐
                          │ n      = 5      │
                          │ arr    = 0x2A00 │ → punta alla heap
                          └─────────────────┘

                          HEAP (indirizzo 0x2A00):
                          ┌────┬────┬────┬────┬────┐
                          │  ? │  ? │  ? │  ? │  ? │
                          └────┴────┴────┴────┴────┘
                          (malloc: valori casuali)
```

---

### 1.3 Cosa Serve per l'Allocazione Dinamica (10 min)

**Libreria necessaria:**
```c
#include <stdlib.h>  // stdlib = standard library
```

**Le due funzioni:**

| Funzione | Significato | Inizializza? |
|----------|-------------|-------------|
| `malloc` | Memory ALLOCation | ❌ No |
| `calloc` | Contiguous ALLOCation | ✅ Sì (tutto a zero) |

**La funzione per liberare:**
```c
free(puntatore);  // OBBLIGATORIO quando hai finito
```

---

## PARTE 2: MALLOC (60 minuti)

### 2.1 Sintassi e Significato (15 min)

```c
void* malloc(size_t numero_di_byte);
```

Decomposizione della sintassi:

```
void*         → tipo del valore restituito
               → "puntatore generico" (non tipizzato)
               → va convertito al tipo corretto con il cast

size_t        → tipo del parametro
               → è un intero senza segno (per contare i byte)

numero_di_byte → quanti byte contigui allocare nell'heap
```

**Come si usa:**
```c
int* arr = (int*) malloc(n * sizeof(int));
//          ↑              ↑      ↑
//        cast           quanti  quanti byte
//      al tipo          elementi occupa un int
//      corretto
```

**Scrivi alla lavagna il calcolo:**
```
Se n = 5 e sizeof(int) = 4 byte:
→ malloc(5 * 4) = malloc(20)
→ Alloca 20 byte contigui nell'heap
→ Abbastanza per 5 interi
```

---

### 2.2 sizeof — Calcolo Automatico dei Byte (10 min)

**Perché usare `sizeof` invece di un numero fisso?**

```c
// ❌ Sbagliato: numero fisso
int* arr = (int*) malloc(n * 4);  // E se int fosse 8 byte?

// ✅ Corretto: sizeof si adatta al sistema
int* arr = (int*) malloc(n * sizeof(int));
```

**`sizeof` per i tipi più comuni:**

```c
printf("%lu\n", sizeof(int));     // Di solito 4
printf("%lu\n", sizeof(float));   // Di solito 4
printf("%lu\n", sizeof(double));  // Di solito 8
printf("%lu\n", sizeof(char));    // Sempre 1
```

**Esempi di calcolo:**
```c
// Array di 10 interi
int* a = (int*) malloc(10 * sizeof(int));       // 40 byte

// Array di 10 float
float* b = (float*) malloc(10 * sizeof(float)); // 40 byte

// Array di 10 double
double* c = (double*) malloc(10 * sizeof(double)); // 80 byte

// Array di 10 caratteri
char* d = (char*) malloc(10 * sizeof(char));    // 10 byte
```

---

### 2.3 Controllo NULL — Mai Saltarlo (10 min)

> "Se il sistema non ha abbastanza memoria libera, `malloc` restituisce `NULL`."

**Senza controllo — PERICOLOSO:**
```c
int* arr = (int*) malloc(n * sizeof(int));
arr[0] = 10;  // ❌ Se malloc ha fallito, arr è NULL!
              //    → CRASH (segmentation fault)
```

**Con controllo — CORRETTO:**
```c
int* arr = (int*) malloc(n * sizeof(int));

if (arr == NULL) {
    printf("ERRORE: Memoria insufficiente!\n");
    return 1;  // Termina con codice di errore
}

// Da qui in poi arr è sicuramente valido
arr[0] = 10;  // ✅ Sicuro
```

**Regola da ripetere alla classe:**
> "Ogni volta che chiami `malloc` o `calloc`, la riga subito dopo è il controllo `if (ptr == NULL)`."

---

### 2.4 Usare l'Array Dinamico (10 min)

**Buona notizia:** Una volta allocato, si usa esattamente come un array normale!

```c
int n = 5;
int* arr = (int*) malloc(n * sizeof(int));
if (arr == NULL) { return 1; }

// Scrittura — identica agli array normali
arr[0] = 10;
arr[1] = 20;
arr[2] = 30;

// Lettura — identica agli array normali
printf("%d\n", arr[0]);   // 10
printf("%d\n", arr[1]);   // 20

// Ciclo — identico agli array normali
for (int i = 0; i < n; i++) {
    arr[i] = i * 10;
}

// Con puntatori — come abbiamo già visto
int* p = arr;
while (p < arr + n) {
    printf("%d ", *p);
    p++;
}
```

---

### 2.5 free — Liberare la Memoria (15 min)

> "La memoria allocata dinamicamente NON viene liberata automaticamente. Devi farlo tu con `free()`."

**Uso corretto:**
```c
int* arr = (int*) malloc(n * sizeof(int));
if (arr == NULL) { return 1; }

// ... usa arr ...

free(arr);       // 1. Libera la memoria nell'heap
arr = NULL;      // 2. Azzera il puntatore (buona pratica)
```

**Perché `arr = NULL` dopo `free`?**
```c
free(arr);
// arr contiene ancora l'indirizzo di prima!
// Ma quella memoria non ci appartiene più.

*arr = 10;  // ❌ CRASH: stai scrivendo in memoria altrui
            //    (dangling pointer = puntatore pendente)

// Se però fai arr = NULL:
arr = NULL;

*arr = 10;  // Segmentation fault chiaro e immediato
            // Più facile da diagnosticare
if (arr != NULL) { ... }  // Il controllo funziona correttamente
```

**Schema completo del ciclo di vita:**
```
int* arr = (int*) malloc(n * sizeof(int));
     ↓
if (arr == NULL) → ERRORE
     ↓
Usa arr[0], arr[1], ..., arr[n-1]
     ↓
free(arr)   → Memoria restituita al sistema
     ↓
arr = NULL  → Puntatore sicuro
```

---

### 2.6 Esempio Completo con malloc (riassunto) (10 min)

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;

    printf("Quanti numeri? ");
    scanf("%d", &n);

    // 1. Alloca
    int* arr = (int*) malloc(n * sizeof(int));
    if (arr == NULL) {
        printf("Errore: memoria insufficiente!\n");
        return 1;
    }

    // 2. Usa
    for (int i = 0; i < n; i++) {
        printf("arr[%d] = ", i);
        scanf("%d", &arr[i]);
    }

    printf("Array: [ ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("]\n");

    // 3. Libera
    free(arr);
    arr = NULL;

    return 0;
}
```

---

## PARTE 3: CALLOC (45 minuti)

### 3.1 Sintassi e Differenza da malloc (15 min)

```c
void* calloc(size_t numero_elementi, size_t dimensione_elemento);
```

Confronto immediato:
```c
// malloc: un solo parametro (byte totali), NON inizializza
int* a = (int*) malloc(n * sizeof(int));

// calloc: due parametri separati, inizializza a ZERO
int* b = (int*) calloc(n, sizeof(int));
//                     ↑      ↑
//               quanti    quanto è grande
//               elementi  ciascuno
```

**Visualizzazione della differenza:**

```
Dopo malloc(5 * sizeof(int)):
┌──────┬──────┬──────┬──────┬──────┐
│  ?   │  ?   │  ?   │  ?   │  ?   │
└──────┴──────┴──────┴──────┴──────┘
  valori casuali (garbage)

Dopo calloc(5, sizeof(int)):
┌──────┬──────┬──────┬──────┬──────┐
│  0   │  0   │  0   │  0   │  0   │
└──────┴──────┴──────┴──────┴──────┘
  tutto a zero, garantito
```

**Mostra alla classe con codice concreto:**
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n = 5;

    // Con calloc → tutto a zero
    int* arr = (int*) calloc(n, sizeof(int));
    if (arr == NULL) { return 1; }

    printf("Valori dopo calloc:\n[ ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);   // Stampa: 0 0 0 0 0
    }
    printf("]\n");

    free(arr);
    arr = NULL;
    return 0;
}
```

---

### 3.2 Tabella Comparativa malloc vs calloc (10 min)

| | `malloc` | `calloc` |
|---|---|---|
| **Parametri** | `(byte_totali)` | `(n_elementi, dim_elemento)` |
| **Inizializzazione** | ❌ Valori casuali | ✅ Tutto a zero |
| **Velocità** | Leggermente più veloce | Leggermente più lenta |
| **Uso tipico** | Scrivi subito tutti i valori | Vuoi partire da zero |
| **Controllo NULL** | ✅ Sempre necessario | ✅ Sempre necessario |
| **free** | ✅ Sempre necessario | ✅ Sempre necessario |

**Sono equivalenti per lo spazio:**
```c
// Questi due allocano la stessa quantità di byte:
int* a = (int*) malloc(5 * sizeof(int));   // 20 byte, casuali
int* b = (int*) calloc(5, sizeof(int));    // 20 byte, tutti 0
```

---

### 3.3 Quando Usare Quale (10 min)

**Usa `malloc` quando:**
```c
// Stai per sovrascrivere subito tutti i valori
int* arr = (int*) malloc(n * sizeof(int));
for (int i = 0; i < n; i++) {
    scanf("%d", &arr[i]);  // Scrivo subito → non importa il valore iniziale
}
```

**Usa `calloc` quando:**
```c
// Vuoi che tutti i valori partano da zero
// (es: contatori, accumulatori, flag)
int* contatori = (int*) calloc(n, sizeof(int));
// contatori[i] parte già da 0 → pronto per essere incrementato

// Oppure: scrivi solo alcune posizioni, le altre restano 0
int* arr = (int*) calloc(n, sizeof(int));
arr[2] = 100;  // Solo questa posizione cambia
arr[4] = 200;  // Le altre rimangono 0
```

---

### 3.4 Esempio Completo con calloc (10 min)

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;

    printf("Quanti studenti? ");
    scanf("%d", &n);

    // calloc: partono tutti da 0
    float* voti = (float*) calloc(n, sizeof(float));
    if (voti == NULL) {
        printf("Errore: memoria insufficiente!\n");
        return 1;
    }

    printf("\nVoti iniziali (tutti 0 grazie a calloc):\n[ ");
    for (int i = 0; i < n; i++) {
        printf("%.1f ", voti[i]);
    }
    printf("]\n\n");

    // Inserisci solo alcuni voti
    printf("Inserisci i voti (inserisci -1 per saltare):\n");
    for (int i = 0; i < n; i++) {
        printf("  Studente %d: ", i + 1);
        float v;
        scanf("%f", &v);
        if (v != -1) {
            voti[i] = v;
        }
        // Se -1, rimane 0 (grazie a calloc)
    }

    printf("\nVoti finali:\n[ ");
    for (int i = 0; i < n; i++) {
        printf("%.1f ", voti[i]);
    }
    printf("]\n");

    free(voti);
    voti = NULL;

    return 0;
}
```

---

## PARTE 4: REALLOC — Ridimensionare la Memoria (45 minuti)

### 4.1 Il Problema: Array Troppo Piccolo (10 min)

**Scenario alla lavagna:**

```c
int n = 5;
int* arr = (int*) malloc(n * sizeof(int));

// Riempi l'array...
arr[0] = 10;
arr[1] = 20;
arr[2] = 30;
arr[3] = 40;
arr[4] = 50;

// Ops! Arriva un sesto elemento!
// Come faccio? arr[5] non esiste...
```

**Soluzione ingenua (SBAGLIATA):**
```c
// ❌ NON funziona: malloc alloca un NUOVO blocco
//    I vecchi dati sono PERSI
arr = (int*) malloc(10 * sizeof(int));
// arr[0]...arr[4] adesso contengono valori casuali!
```

**Soluzione manuale (FUNZIONA ma è scomoda):**
```c
// Alloca nuovo array più grande
int* nuovo = (int*) malloc(10 * sizeof(int));

// Copia i vecchi dati
for (int i = 0; i < n; i++) {
    nuovo[i] = arr[i];
}

// Libera il vecchio
free(arr);

// Usa il nuovo
arr = nuovo;
```

> "Questa procedura è così comune che C fornisce `realloc` per farla automaticamente!"

---

### 4.2 Sintassi di realloc (15 min)

```c
void* realloc(void* vecchio_puntatore, size_t nuova_dimensione_in_byte);
```

**Cosa fa `realloc`:**
1. Cerca di **espandere** il blocco di memoria esistente
2. Se non è possibile, **alloca un nuovo blocco** della nuova dimensione
3. **Copia automaticamente** i vecchi dati nel nuovo blocco
4. **Libera automaticamente** il vecchio blocco
5. Ritorna il puntatore al blocco (nuovo o espanso)

**Uso tipico:**
```c
int n = 5;
int* arr = (int*) malloc(n * sizeof(int));
if (arr == NULL) { return 1; }

// ... riempi arr ...

// Devo ingrandire a 10 elementi
n = 10;
int* temp = (int*) realloc(arr, n * sizeof(int));
if (temp == NULL) {
    // Errore: realloc fallita, ma arr è ancora valido!
    free(arr);
    return 1;
}

arr = temp;  // Ora arr punta al blocco ridimensionato
// arr[0]...arr[4] hanno ancora i vecchi valori ✓
// arr[5]...arr[9] hanno valori casuali (come malloc)
```

**⚠️ IMPORTANTE — Usa una variabile temporanea:**

```c
// ❌ SBAGLIATO: se realloc fallisce, arr diventa NULL
//    e perdi l'accesso ai vecchi dati!
arr = (int*) realloc(arr, nuova_dimensione);

// ✅ CORRETTO: usa temp, controlla NULL, poi assegna
int* temp = (int*) realloc(arr, nuova_dimensione);
if (temp == NULL) {
    // arr è ancora valido, puoi fare free
    free(arr);
    return 1;
}
arr = temp;  // Ora sì, sostituisci arr
```

---

### 4.3 Tre Scenari di realloc (10 min)

**Scenario 1: Espansione (ingrandire)**
```c
int* arr = (int*) malloc(5 * sizeof(int));
// ... riempi ...

// Raddoppia la dimensione
int* temp = (int*) realloc(arr, 10 * sizeof(int));
if (temp == NULL) { free(arr); return 1; }
arr = temp;

// arr[0]...arr[4] → dati originali (preservati)
// arr[5]...arr[9] → valori casuali (nuova memoria)
```

**Scenario 2: Riduzione (rimpicciolire)**
```c
int* arr = (int*) malloc(10 * sizeof(int));
// ... usa solo le prime 5 posizioni ...

// Riduci a 5 elementi per risparmiare memoria
int* temp = (int*) realloc(arr, 5 * sizeof(int));
if (temp == NULL) { free(arr); return 1; }
arr = temp;

// arr[0]...arr[4] → dati originali (preservati)
// arr[5]...arr[9] → non esistono più
```

**Scenario 3: realloc(NULL, size)**
```c
// realloc con NULL si comporta come malloc
int* arr = (int*) realloc(NULL, 5 * sizeof(int));
// Equivalente a: malloc(5 * sizeof(int))
```

---

### 4.4 Esempio Completo: Array Dinamico che Cresce (10 min)

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int capacita = 2;  // Capacità iniziale piccola
    int dimensione = 0; // Quanti elementi effettivi

    int* arr = (int*) malloc(capacita * sizeof(int));
    if (arr == NULL) {
        printf("Errore allocazione!\n");
        return 1;
    }

    printf("Inserisci numeri (0 per terminare):\n");

    while (1) {
        int num;
        printf("  Numero: ");
        scanf("%d", &num);

        if (num == 0) break;

        // Se l'array è pieno, raddoppia la capacità
        if (dimensione == capacita) {
            capacita *= 2;
            printf("    → Array pieno! Raddoppio a %d elementi...\n", capacita);

            int* temp = (int*) realloc(arr, capacita * sizeof(int));
            if (temp == NULL) {
                printf("Errore realloc!\n");
                free(arr);
                return 1;
            }
            arr = temp;
        }

        arr[dimensione++] = num;
    }

    // Stampa risultato
    printf("\nArray finale (%d elementi, capacità %d):\n[ ",
           dimensione, capacita);
    for (int i = 0; i < dimensione; i++) {
        printf("%d ", arr[i]);
    }
    printf("]\n");

    free(arr);
    arr = NULL;

    return 0;
}
```

**Output esempio:**
```
Inserisci numeri (0 per terminare):
  Numero: 10
  Numero: 20
  Numero: 30
    → Array pieno! Raddoppio a 4 elementi...
  Numero: 40
  Numero: 50
    → Array pieno! Raddoppio a 8 elementi...
  Numero: 60
  Numero: 0

Array finale (6 elementi, capacità 8):
[ 10 20 30 40 50 60 ]
```

**Concetto chiave da sottolineare:**
> "Questa è la tecnica usata dai vettori dinamici in altri linguaggi (es: `ArrayList` in Java, `vector` in C++, `list` in Python). Quando l'array è pieno, si raddoppia automaticamente!"

---

## PARTE 5: PRATICA GUIDATA (60 minuti)

### Esercizio Guidato 1: Array di float con malloc (15 min)

**Da costruire insieme:**
Chiedere n temperature, calcolare media, trovare la più alta e la più bassa.

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;

    printf("Quante temperature? ");
    scanf("%d", &n);

    float* temp = (float*) malloc(n * sizeof(float));
    if (temp == NULL) {
        printf("Errore allocazione!\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        printf("  Temperatura %d: ", i + 1);
        scanf("%f", &temp[i]);
    }

    // Media
    float somma = 0;
    for (int i = 0; i < n; i++) somma += temp[i];
    float media = somma / n;

    // Max e min
    float max = temp[0], min = temp[0];
    for (int i = 1; i < n; i++) {
        if (temp[i] > max) max = temp[i];
        if (temp[i] < min) min = temp[i];
    }

    printf("\nMedia:    %.2f°C\n", media);
    printf("Massima:  %.2f°C\n", max);
    printf("Minima:   %.2f°C\n", min);

    free(temp);
    temp = NULL;

    return 0;
}
```

---

### Esercizio Guidato 2: Contatori con calloc (20 min)

**Scenario:** Hai un array di voti (da 0 a 10). Conta quante volte compare ogni voto.

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;

    printf("Quanti voti? ");
    scanf("%d", &n);

    // Array dei voti
    int* voti = (int*) malloc(n * sizeof(int));
    if (voti == NULL) { return 1; }

    // Contatori per ogni voto da 0 a 10
    // calloc: partono tutti da 0, pronti per il conteggio
    int* contatori = (int*) calloc(11, sizeof(int));
    if (contatori == NULL) {
        free(voti);
        return 1;
    }

    for (int i = 0; i < n; i++) {
        printf("  Voto %d: ", i + 1);
        scanf("%d", &voti[i]);
    }

    // Conta le occorrenze
    for (int i = 0; i < n; i++) {
        if (voti[i] >= 0 && voti[i] <= 10) {
            contatori[voti[i]]++;
        }
    }

    // Stampa distribuzione
    printf("\n=== DISTRIBUZIONE VOTI ===\n");
    for (int v = 0; v <= 10; v++) {
        if (contatori[v] > 0) {
            printf("  Voto %2d: %d volte\n", v, contatori[v]);
        }
    }

    free(voti);
    voti = NULL;
    free(contatori);
    contatori = NULL;

    return 0;
}
```

**Punto chiave da sottolineare:**
> "Senza `calloc`, i contatori avrebbero valori casuali e il conteggio sarebbe sbagliato. Con `calloc` partono tutti da 0, perfetti per essere incrementati."

---

### Esercizio Guidato 3: Due Array Paralleli (25 min)

**Scenario:** Gestisci una classe con nomi e voti in due array dinamici separati.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int n;

    printf("Quanti studenti? ");
    scanf("%d", &n);
    getchar();

    // Array di puntatori a stringhe (per i nomi)
    char** nomi = (char**) malloc(n * sizeof(char*));
    if (nomi == NULL) { return 1; }

    // Array di voti
    float* voti = (float*) calloc(n, sizeof(float));
    if (voti == NULL) {
        free(nomi);
        return 1;
    }

    // Inserimento
    for (int i = 0; i < n; i++) {
        char buffer[100];
        printf("\nStudente %d:\n", i + 1);

        printf("  Nome: ");
        fgets(buffer, sizeof(buffer), stdin);
        buffer[strcspn(buffer, "\n")] = '\0';

        // Alloca esattamente la dimensione giusta per il nome
        nomi[i] = (char*) malloc((strlen(buffer) + 1) * sizeof(char));
        if (nomi[i] == NULL) {
            // Libera tutto ciò che è già stato allocato
            for (int j = 0; j < i; j++) free(nomi[j]);
            free(nomi);
            free(voti);
            return 1;
        }
        strcpy(nomi[i], buffer);

        printf("  Voto: ");
        scanf("%f", &voti[i]);
        getchar();
    }

    // Calcola media
    float somma = 0;
    for (int i = 0; i < n; i++) somma += voti[i];
    float media = somma / n;

    // Stampa risultati
    printf("\n=== RISULTATI CLASSE ===\n");
    printf("%-20s | %s\n", "NOME", "VOTO");
    printf("%-20s | %s\n", "--------------------", "------");
    for (int i = 0; i < n; i++) {
        printf("%-20s | %.2f  %s\n",
               nomi[i],
               voti[i],
               voti[i] >= media ? "✓" : "");
    }
    printf("\nMedia classe: %.2f\n", media);

    // Libera tutta la memoria
    for (int i = 0; i < n; i++) {
        free(nomi[i]);
        nomi[i] = NULL;
    }
    free(nomi);
    nomi = NULL;
    free(voti);
    voti = NULL;

    return 0;
}
```

---

## PARTE 6: ERRORI COMUNI E RIEPILOGO (45 minuti)

### 5.1 I Tre Errori Più Frequenti (20 min)

---

**Errore 1: MEMORY LEAK (Perdita di Memoria)**

> "Allochi memoria ma non la liberi mai."

```c
// ❌ SBAGLIATO: memory leak
void funzioneConLeak() {
    int* arr = (int*) malloc(100 * sizeof(int));
    // ... usa arr ...
    return;  // La funzione termina senza free!
             // La memoria rimane occupata per sempre
             // (fino alla fine del programma)
}

// ✅ CORRETTO
void funzioneSicura() {
    int* arr = (int*) malloc(100 * sizeof(int));
    if (arr == NULL) return;
    // ... usa arr ...
    free(arr);      // Libera prima di uscire
    arr = NULL;
}
```

**Analogia:**
> "Un memory leak è come affittare una stanza e non restituirla mai. Il sistema alla fine non ha più stanze da affittare."

---

**Errore 2: DANGLING POINTER (Puntatore Pendente)**

> "Usi un puntatore dopo averlo liberato."

```c
// ❌ SBAGLIATO: dangling pointer
int* arr = (int*) malloc(5 * sizeof(int));
arr[0] = 10;

free(arr);     // Memoria liberata

arr[0] = 20;  // ❌ CRASH o comportamento indefinito!
               // arr punta a memoria che non ci appartiene più

// ✅ CORRETTO
free(arr);
arr = NULL;    // Azzera subito

if (arr != NULL) {  // Il controllo ora funziona correttamente
    arr[0] = 20;
}
```

---

**Errore 3: DOUBLE FREE**

> "Liberi la stessa memoria due volte."

```c
// ❌ SBAGLIATO: double free
int* arr = (int*) malloc(5 * sizeof(int));
free(arr);
free(arr);   // ❌ CRASH! Liberato due volte → corruzione dell'heap

// ✅ CORRETTO
free(arr);
arr = NULL;  // NULL rende il secondo free innocuo

free(arr);   // free(NULL) è sicuro: non fa nulla
```

---

### 6.2 Riepilogo Visivo (10 min)

Scrivi alla lavagna questo schema riassuntivo:

```
CICLO DI VITA DI UN ARRAY DINAMICO
────────────────────────────────────

  1. DICHIARA il puntatore
     int* arr;

  2. ALLOCA la memoria
     arr = (int*) malloc(n * sizeof(int));
          oppure
     arr = (int*) calloc(n, sizeof(int));

  3. CONTROLLA se è riuscita
     if (arr == NULL) { gestisci l'errore }

  4. USA l'array normalmente
     arr[0] = 10;
     arr[i] = valore;
     printf("%d", arr[j]);

  5. (OPZIONALE) RIDIMENSIONA se necessario
     int* temp = (int*) realloc(arr, nuova_dim * sizeof(int));
     if (temp == NULL) { free(arr); return 1; }
     arr = temp;

  6. LIBERA la memoria
     free(arr);
     arr = NULL;

────────────────────────────────────

  malloc   → valori CASUALI, un solo parametro
  calloc   → valori ZERO,    due parametri
  realloc  → RIDIMENSIONA,   preserva i dati esistenti
  free     → SEMPRE, per ogni malloc/calloc/realloc
  = NULL   → SEMPRE dopo free
```

---

### 6.3 Domande di Verifica (15 min)

1. **"Qual è la differenza tra `malloc` e `calloc`?"**
2. **"Perché dobbiamo sempre controllare se il risultato è `NULL`?"**
3. **"Cos'è un memory leak? Come si evita?"**
4. **"Cos'è un dangling pointer? Come si evita?"**
5. **"Cosa succede se chiami `free` due volte sullo stesso puntatore?"**
6. **"Quando usi `realloc` e perché devi usare una variabile temporanea?"**

---

<details>
<summary><b>📝 RISPOSTE PER IL DOCENTE</b></summary>

### 1. Differenza malloc vs calloc

**Risposta:**

**`malloc(n * sizeof(tipo))`:**
- Un solo parametro: il numero totale di byte
- NON inizializza: i valori sono casuali (garbage)
- Leggermente più veloce

**`calloc(n, sizeof(tipo))`:**
- Due parametri separati: numero di elementi e dimensione di ciascuno
- INIZIALIZZA tutto a zero
- Leggermente più lenta (deve scrivere zero ovunque)

**Sono equivalenti per lo spazio allocato:**
```c
malloc(5 * sizeof(int))  ≡  calloc(5, sizeof(int))  // 20 byte
```

**Quando preferire quale:**
- `malloc` → se scrivi subito tutti i valori (l'inizializzazione verrebbe sovrascritta)
- `calloc` → se vuoi partire da zero (contatori, flag, array parzialmente riempiti)

---

### 2. Perché controllare NULL

**Risposta:**

`malloc` e `calloc` restituiscono `NULL` quando il sistema non riesce ad allocare la memoria richiesta (es: memoria insufficiente, richiesta troppo grande).

Se non si controlla e si usa direttamente un puntatore `NULL`:
```c
int* arr = (int*) malloc(n * sizeof(int));
arr[0] = 10;  // Se arr è NULL → SEGMENTATION FAULT → crash del programma
```

Il controllo permette di gestire l'errore in modo controllato:
```c
if (arr == NULL) {
    printf("Errore!\n");
    return 1;  // Termina in modo pulito
}
```

**Analogia:** È come aprire uno sportello bancomat e usare i soldi che escono, senza prima controllare se ne sono effettivamente usciti.

---

### 3. Memory Leak

**Risposta:**

Un **memory leak** (perdita di memoria) si verifica quando si alloca memoria dinamicamente ma non la si libera mai con `free`.

**Conseguenze:**
- La memoria rimane occupata finché il programma è in esecuzione
- In programmi longevi (server, app) porta all'esaurimento della memoria disponibile
- Il sistema operativo recupera la memoria alla chiusura del programma, ma è cattiva pratica

**Come si evita:**
- Regola semplice: per ogni `malloc`/`calloc` ci deve essere un `free`
- Liberare sempre prima di uscire da una funzione
- Liberare sempre prima di rassegnare un puntatore:

```c
// ❌ Leak: il vecchio blocco è perso
arr = (int*) malloc(10 * sizeof(int));
arr = (int*) malloc(20 * sizeof(int));  // Il primo blocco non si può più liberare!

// ✅ Corretto
arr = (int*) malloc(10 * sizeof(int));
free(arr);
arr = (int*) malloc(20 * sizeof(int));
```

---

### 4. Dangling Pointer

**Risposta:**

Un **dangling pointer** (puntatore pendente) è un puntatore che continua a contenere un indirizzo di memoria dopo che quella memoria è stata liberata con `free`.

**Il problema:**
```c
free(arr);   // La memoria è stata restituita al sistema
arr[0] = 5;  // arr punta ancora lì, ma quella memoria
             // potrebbe essere stata assegnata ad altro!
             // → Comportamento indefinito, crash, dati corrotti
```

**Come si evita:**
Subito dopo `free`, assegnare `NULL` al puntatore:
```c
free(arr);
arr = NULL;  // arr non punta più a nulla
             // Qualsiasi accesso a NULL dà segfault immediato
             // → più facile da diagnosticare
```

---

### 5. Double Free

**Risposta:**

Un **double free** si verifica quando si chiama `free` due volte sullo stesso puntatore.

**Il problema:**
```c
free(arr);
free(arr);  // La struttura interna dell'heap viene corrotta
            // → crash, comportamento imprevedibile
```

**Come si evita:**
```c
free(arr);
arr = NULL;  // free(NULL) è definito dallo standard come "non fare nulla"

free(arr);   // Ora è sicuro: free(NULL) viene ignorato
```

Impostare `arr = NULL` dopo `free` rende il double free innocuo.

---

### 6. realloc e variabile temporanea

**Risposta:**

`realloc` si usa quando hai bisogno di **ridimensionare** un array dinamico già allocato (ingrandire o rimpicciolire).

**Cosa fa `realloc`:**
```c
int* temp = (int*) realloc(arr, nuova_dimensione);
```
1. Cerca di espandere il blocco esistente
2. Se non può, alloca un nuovo blocco della nuova dimensione
3. Copia automaticamente i vecchi dati
4. Libera automaticamente il vecchio blocco
5. Ritorna il puntatore al blocco (nuovo o espanso)

**Perché usare una variabile temporanea:**
```c
// ❌ SBAGLIATO
arr = (int*) realloc(arr, nuova_dimensione);
// Se realloc fallisce (ritorna NULL), perdi l'accesso
// ai vecchi dati! arr diventa NULL e non puoi più fare free.

// ✅ CORRETTO
int* temp = (int*) realloc(arr, nuova_dimensione);
if (temp == NULL) {
    // realloc è fallita, ma arr è ancora valido!
    // Puoi gestire l'errore, usare i vecchi dati, o fare free
    free(arr);
    return 1;
}
arr = temp;  // Solo ora sostituisci arr
```

La variabile temporanea protegge il puntatore originale in caso di fallimento.

**Cosa preserva `realloc`:**
- Se ingrandisci: i vecchi dati sono copiati, le nuove posizioni hanno valori casuali
- Se rimpicciolisci: i primi N elementi sono preservati, il resto viene scartato

</details>

---

## NOTE PER IL DOCENTE

### ⚠️ Punti critici da monitorare:

1. **Dimenticare il controllo NULL** — gli studenti tendono a saltarlo
2. **Dimenticare `free`** — abituarsi a scriverlo subito dopo `malloc`
3. **Confondere `malloc` e `calloc`** — i valori iniziali non sono la stessa cosa
4. **Riassegnare un puntatore senza `free`** — il memory leak più comune
5. **Usare array dopo `free`** — dangling pointer difficile da debuggare

### 💡 Suggerimenti didattici:

- Scrivi sempre il `free` subito dopo il `malloc` nel codice, poi aggiungi il codice in mezzo
- Mostra con `valgrind` (se disponibile) i memory leak: è molto efficace
- Fai disegnare la memoria (stack + heap) per ogni programma
- Insisti sul fatto che l'array dinamico si usa **esattamente come uno statico**
- Il punto di forza è la **flessibilità**: mostralo con un programma che funziona per qualsiasi n

### 🎯 Obiettivi minimi per questa lezione:

Lo studente è pronto se:
- Sa allocare un array con `malloc` e `calloc`
- Controlla sempre `NULL`
- Sa usare `free` correttamente
- Capisce la differenza tra array statico e dinamico
- Conosce i tre errori principali (leak, dangling, double free)

---

**Buona lezione! 🚀**



---

# 19 pila coda studente completo

**File:** `19 pila coda studente completo.md`
**Tipo:** `.md`
**Dimensione:** 26.2 KB
**Ultima modifica:** 02/07/2026 09:24

---

# Lezione: Pila e Coda (Stack e Queue)
**Durata totale:** 4 ore
**Teoria:** 1.5 ore | **Esercizi:** 2.5 ore
**Data:** _______________
**Ambiente:** CLion (JetBrains)

> ⚠️ NOTA DIDATTICA: Tutte le implementazioni usano **array e variabili separate** senza `struct`.

---

# PARTE 1 — TEORIA (1.5 ore)

## 1.1 Introduzione e Motivazione

Immagina di essere in fila alla cassa del supermercato: il primo ad arrivare è il primo a essere servito. Oppure pensa a una pila di piatti: li metti uno sopra l'altro e prendi sempre quello in cima.

Questi due scenari descrivono due strutture dati fondamentali in informatica:

- **Pila (Stack):** LIFO — *Last In, First Out* (l'ultimo inserito è il primo a uscire)
- **Coda (Queue):** FIFO — *First In, First Out* (il primo inserito è il primo a uscire)

**Dove si usano nella realtà e nei programmi?**

- **Stack:** la cronologia "Indietro" del browser, il meccanismo di chiamata delle funzioni, il controllo delle parentesi bilanciate in un compilatore, l'operazione "Annulla" (Ctrl+Z).
- **Queue:** la coda di stampa, i messaggi in attesa di elaborazione, le richieste a un server web, le animazioni in un videogioco.

---

## 1.2 Spiegazione dell'Argomento

### La Pila (Stack)

Una pila è una struttura in cui gli elementi vengono inseriti e rimossi sempre dalla stessa estremità, chiamata **cima** (*top*).

**Operazioni principali:**
- `push(x)` — inserisce x in cima
- `pop()` — rimuove e restituisce l'elemento in cima
- `peek()` — legge la cima senza rimuoverla
- `isEmpty()` — true se la pila è vuota
- `isFull()` — true se la pila è piena

**Visualizzazione passo-passo:**

```
Inizio        push(10)      push(20)      push(30)      pop()
              +------+      +------+      +------+      +------+
              |  10  |<top  |  20  |<top  |  30  |<top  |  20  |<top
              +------+      +------+      +------+      +------+
                            |  10  |      |  20  |      |  10  |
                            +------+      +------+      +------+
                                          |  10  |
                                          +------+
top = -1      top = 0       top = 1       top = 2       top = 1
```

**Implementazione con array:**

Usiamo un array per memorizzare gli elementi e una variabile intera `top` come indice dell'elemento in cima. Convenzione: `top = -1` significa pila vuota.

```
Array:   [ 10 | 20 | 30 | -- | -- ]
indici:     0    1    2    3    4
                      ^
                   top = 2
```

- `push(x)`: incrementa `top`, poi assegna `pila[top] = x`
- `pop()`: salva `pila[top]`, poi decrementa `top`

---

### La Coda (Queue)

Una coda è una struttura in cui i nuovi elementi entrano in **fondo** (*tail*) ed escono dalla **testa** (*head*).

**Operazioni principali:**
- `enqueue(x)` — inserisce x in fondo
- `dequeue()` — rimuove e restituisce l'elemento in testa
- `isEmpty()` — true se la coda è vuota
- `isFull()` — true se la coda è piena

**Visualizzazione passo-passo:**

```
Inizio       enqueue(10)   enqueue(20)   enqueue(30)   dequeue()
             +------+      +------+---+  +------+---+--+  +------+---+
             |  10  |      |  10  |20 |  |  10  |20 |30|  |  20  |30 |
             +------+      +------+---+  +------+---+--+  +------+---+
             ^      ^      ^         ^   ^            ^        ^      ^
            h=0   t=0+1   h=0      t=1  h=0         t=2      h=1    t=2
```

**Implementazione con array:**

Usiamo un array e tre variabili: `head` (indice da cui si estrae), `tail` (prossimo slot libero), `size` (numero elementi presenti).

```
Array:   [ 10 | 20 | 30 | -- | -- ]
indici:     0    1    2    3    4
            ^              ^
         head=0          tail=3    size=3
```

Dopo `dequeue()`:
```
Array:   [ -- | 20 | 30 | -- | -- ]
                ^         ^
             head=1     tail=3    size=2
```

---

### Il Problema della Coda Lineare

La coda lineare ha un limite importante: dopo molte operazioni di `enqueue`/`dequeue`, `tail` raggiunge la fine dell'array anche se ci sono slot liberi all'inizio (quelli già "consumati" dai `dequeue`). Lo spazio non viene mai recuperato.

```
Dopo 3 enqueue + 2 dequeue:

Array:   [ -- | -- | 30 | -- | -- ]   (MAX = 5)
                     ^         ^
                  head=2     tail=3    size=1

Posizioni 0 e 1 sono libere ma inaccessibili!
Se facessi altri 2 enqueue, tail arriverebbe a 5 → fuori dall'array.
```

---

### La Coda Circolare (Circular Buffer)

La soluzione è trattare l'array come se fosse **un cerchio**: quando `tail` raggiunge la fine, riparte dall'indice 0. Questo si ottiene con l'operatore **modulo** (`%`).

**Regola chiave:**
```
tail = (tail + 1) % MAX
head = (head + 1) % MAX
```

**Visualizzazione — array di 5 slot come cerchio:**

```
        indice 0
           |
    4 ---- 0
   /         \
  3           1
   \         /
    2 ---- 2
           |
        indice 2

Stato: head=3, tail=1, size=3  →  elementi in posizioni 3, 4, 0
Array:  [ 70 | -- | -- | 30 | 50 ]
              ^              ^
            tail=1         head=3
```

**Confronto passo-passo con MAX=5:**

```
Operazione     head  tail  size  Array (indici 0..4)
-----------    ----  ----  ----  -------------------
enqueue(10)      0     1     1   [10| - | - | - | - ]
enqueue(20)      0     2     2   [10|20 | - | - | - ]
enqueue(30)      0     3     3   [10|20 |30 | - | - ]
dequeue()→10     1     3     2   [ - |20 |30 | - | - ]
dequeue()→20     2     3     1   [ - | - |30 | - | - ]
enqueue(40)      2     4     2   [ - | - |30 |40 | - ]
enqueue(50)      2     0     3   [ - | - |30 |40 |50 ]
  (tail torna a 0 con % 5!)
enqueue(60)      2     1     4   [60 | - |30 |40 |50 ]
  (slot 0 riciclato!)
```

**Condizioni di pieno e vuoto:**
- Vuota: `size == 0`
- Piena: `size == MAX`

---

## 1.3 Esempi di Codice Commentati

### Esempio 1 — Pila (Stack) con array

```c
#include <stdio.h>

#define MAX 5

int pila[MAX];
int top = -1;  // -1 = pila vuota

int isEmpty() { return top == -1; }
int isFull()  { return top == MAX - 1; }

void push(int valore) {
    if (isFull()) {
        printf("Errore: pila piena!\n");
        return;
    }
    top++;
    pila[top] = valore;
}

int pop() {
    if (isEmpty()) {
        printf("Errore: pila vuota!\n");
        return -1;
    }
    int valore = pila[top];
    top--;
    return valore;
}

int peek() {
    if (isEmpty()) {
        printf("Errore: pila vuota!\n");
        return -1;
    }
    return pila[top];
}

int main() {
    push(10);
    push(20);
    push(30);

    printf("Cima: %d\n", peek());  // 30
    printf("Pop: %d\n", pop());    // 30
    printf("Pop: %d\n", pop());    // 20
    printf("Cima: %d\n", peek());  // 10

    return 0;
}
```

**Output atteso:**
```
Cima: 30
Pop: 30
Pop: 20
Cima: 10
```

---

### Esempio 2 — Coda (Queue) con array

```c
#include <stdio.h>

#define MAX 5

int coda[MAX];
int head = 0;
int tail = 0;
int size = 0;

int isEmpty() { return size == 0; }
int isFull()  { return size == MAX; }

void enqueue(int valore) {
    if (isFull()) {
        printf("Errore: coda piena!\n");
        return;
    }
    coda[tail] = valore;
    tail++;
    size++;
}

int dequeue() {
    if (isEmpty()) {
        printf("Errore: coda vuota!\n");
        return -1;
    }
    int valore = coda[head];
    head++;
    size--;
    return valore;
}

int main() {
    enqueue(10);
    enqueue(20);
    enqueue(30);

    printf("Dequeue: %d\n", dequeue());  // 10 — FIFO
    printf("Dequeue: %d\n", dequeue());  // 20
    enqueue(40);
    printf("Dequeue: %d\n", dequeue());  // 30
    printf("Dequeue: %d\n", dequeue());  // 40

    return 0;
}
```

**Output atteso:**
```
Dequeue: 10
Dequeue: 20
Dequeue: 30
Dequeue: 40
```

---

### Esempio 3 — Stampare il contenuto della pila

```c
#include <stdio.h>

#define MAX 5

int pila[MAX];
int top = -1;

void push(int v) {
    if (top < MAX - 1) pila[++top] = v;
}

void stampaPila() {
    if (top == -1) {
        printf("Pila vuota.\n");
        return;
    }
    printf("Pila (dalla cima alla base):\n");
    for (int i = top; i >= 0; i--) {
        printf("  [%d]\n", pila[i]);
    }
}

int main() {
    push(5);
    push(15);
    push(25);
    stampaPila();
    return 0;
}
```

**Output atteso:**
```
Pila (dalla cima alla base):
  [25]
  [15]
  [5]
```

---

### Esempio 4 — Coda Circolare con array

```c
#include <stdio.h>

#define MAX 5

int coda[MAX];
int head = 0;
int tail = 0;
int size = 0;

int isEmpty() { return size == 0; }
int isFull()  { return size == MAX; }

void enqueue(int valore) {
    if (isFull()) { printf("Errore: coda piena!\n"); return; }
    coda[tail] = valore;
    tail = (tail + 1) % MAX;  // avanza circolarmente
    size++;
}

int dequeue() {
    if (isEmpty()) { printf("Errore: coda vuota!\n"); return -1; }
    int valore = coda[head];
    head = (head + 1) % MAX;  // avanza circolarmente
    size--;
    return valore;
}

void stampaCoda() {
    printf("Coda (%d elementi): ", size);
    for (int i = 0; i < size; i++)
        printf("%d ", coda[(head + i) % MAX]);
    printf("\n");
}

int main() {
    enqueue(10); enqueue(20); enqueue(30);
    stampaCoda();
    dequeue(); dequeue();
    stampaCoda();
    enqueue(40); enqueue(50); enqueue(60);
    stampaCoda();
    printf("Dequeue: %d\n", dequeue());
    stampaCoda();
    return 0;
}
```

**Output atteso:**
```
Coda (3 elementi): 10 20 30
Coda (1 elementi): 30
Coda (4 elementi): 30 40 50 60
Dequeue: 30
Coda (3 elementi): 40 50 60
```

> 💡 **Il trucco del modulo:** `(head + i) % MAX` permette di visitare gli elementi nell'ordine corretto anche quando "scavalcano" la fine dell'array e ripartono da 0.

---

## 1.4 Riepilogo Visivo

```
╔══════════════════════════════════════════════════════╗
║              PILA (STACK) — LIFO                     ║
╠══════════════════╦═══════════════════════════════════╣
║ Operazione       ║ Descrizione                       ║
╠══════════════════╬═══════════════════════════════════╣
║ push(x)          ║ Inserisce x in CIMA               ║
║ pop()            ║ Rimuove e restituisce la CIMA      ║
║ peek()           ║ Legge la CIMA (senza rimuovere)   ║
║ isEmpty()        ║ top == -1                         ║
║ isFull()         ║ top == MAX-1                      ║
╚══════════════════╩═══════════════════════════════════╝
  Accesso consentito: solo dalla CIMA

╔════════════════════════╦════════════════════════════════╗
║   CODA LINEARE         ║   CODA CIRCOLARE               ║
╠════════════════════════╬════════════════════════════════╣
║ tail++                 ║ tail = (tail+1) % MAX          ║
║ head++                 ║ head = (head+1) % MAX          ║
║ Spazio non riciclato   ║ Spazio riciclato automaticam.  ║
║ Semplice da capire     ║ Più efficiente in memoria      ║
╚════════════════════════╩════════════════════════════════╝
  Entrambe: isEmpty → size==0 | isFull → size==MAX

╔═══════════════╦═══════════╦═══════════════════════════╗
║ Caratteristica║   STACK   ║    QUEUE (circolare)       ║
╠═══════════════╬═══════════╬═══════════════════════════╣
║ Ordine        ║   LIFO    ║         FIFO              ║
║ Inserimento   ║   cima    ║         fondo             ║
║ Rimozione     ║   cima    ║         testa             ║
║ Var. chiave   ║   top     ║   head, tail, size        ║
║ Avanzamento   ║   +1/-1   ║   (indice+1) % MAX        ║
╚═══════════════╩═══════════╩═══════════════════════════╝
```

---

## 1.5 Domande di Verifica Orale

**D1:** Cosa significa LIFO e FIFO? Fai un esempio concreto per ciascuno.

<details>
<summary><b>💡 RISPOSTA</b></summary>

LIFO = Last In First Out — l'ultimo elemento inserito è il primo ad uscire (es. pila di piatti, cronologia del browser). FIFO = First In First Out — il primo elemento inserito è il primo ad uscire (es. fila alla cassa, coda di stampa).

</details>

---

**D2:** In una pila implementata con array, cosa significa `top == -1`?

<details>
<summary><b>💡 RISPOSTA</b></summary>

La pila è vuota: non contiene alcun elemento.

</details>

---

**D3:** Qual è la differenza tra `pop()` e `peek()`?

<details>
<summary><b>💡 RISPOSTA</b></summary>

`pop()` rimuove e restituisce l'elemento in cima (la pila cambia). `peek()` restituisce l'elemento in cima senza rimuoverlo (la pila rimane invariata).

</details>

---

**D4:** In una coda, dove entrano i nuovi elementi e da dove escono?

<details>
<summary><b>💡 RISPOSTA</b></summary>

I nuovi elementi entrano in fondo (tail). Gli elementi escono dalla testa (head).

</details>

---

**D5:** Eseguo: `push(1)`, `push(2)`, `push(3)`, `pop()`, `pop()`. Qual è la cima?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Dopo i push la pila è [1, 2, 3] con 3 in cima. Dopo due `pop()` vengono rimossi 3 e poi 2. La cima è ora 1.

</details>

---

**D6:** Eseguo su una coda: `enqueue(1)`, `enqueue(2)`, `enqueue(3)`, `dequeue()`. Qual è il prossimo da estrarre?

<details>
<summary><b>💡 RISPOSTA</b></summary>

La coda è [1, 2, 3] con 1 in testa. Dopo `dequeue()` viene rimosso 1. Il prossimo da estrarre è 2.

</details>

---

**D7:** Cosa succede se chiamo `pop()` su una pila vuota nel codice degli esempi?

<details>
<summary><b>💡 RISPOSTA</b></summary>

La funzione `isEmpty()` restituisce vero, viene stampato "Errore: pila vuota!" e la funzione restituisce -1 come valore sentinella.

</details>

---

**D8:** Qual è il limite della coda lineare che la coda circolare risolve?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Nella coda lineare, le posizioni prima di `head` non vengono mai riutilizzate: dopo molti `enqueue`/`dequeue`, `tail` raggiunge la fine dell'array anche se ci sono slot liberi all'inizio. La coda circolare usa `(tail + 1) % MAX` per far "girare" l'indice e riciclare quegli spazi.

</details>

---

**D9:** In una coda circolare con MAX=4, se `tail` vale 3 e faccio un `enqueue`, dove si trova il prossimo `tail`?

<details>
<summary><b>💡 RISPOSTA</b></summary>

`tail = (3 + 1) % 4 = 0`. L'indice riparte da capo, sfruttando lo spazio liberato dai precedenti `dequeue`.

</details>

---

# PARTE 2 — ESERCIZI (2.5 ore)

---

## 🟢 Livello Base

### Esercizio 1 — Inverti una sequenza con la Pila (15–20 min)

**Testo:**
Leggi 5 interi inseriti dall'utente e stampali in ordine inverso usando una pila. Inserisci gli elementi nella pila uno per uno con `push`, poi estraili con `pop` e stampali.

**Esempio input/output:**
```
Inserisci 5 numeri: 1 2 3 4 5
Ordine inverso: 5 4 3 2 1
```

**💡 Hint:**
1. Dichiara `int pila[5]` e `int top = -1`.
2. Primo ciclo `for`: leggi 5 numeri con `scanf` e chiama `push` per ciascuno.
3. Secondo ciclo: chiama `pop` finché la pila non è vuota e stampa ogni valore.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

#define MAX 5

int pila[MAX];
int top = -1;

void push(int v) {
    if (top < MAX - 1) pila[++top] = v;
}

int pop() {
    if (top == -1) return -1;
    return pila[top--];
}

int isEmpty() { return top == -1; }

int main() {
    printf("Inserisci 5 numeri: ");
    for (int i = 0; i < MAX; i++) {
        int n;
        scanf("%d", &n);
        push(n);
    }

    printf("Ordine inverso:");
    while (!isEmpty()) {
        printf(" %d", pop());
    }
    printf("\n");

    return 0;
}
```

</details>

---

### Esercizio 2 — Gestione di una coda clienti (15–20 min)

**Testo:**
Simula una coda di 4 clienti al banco. Aggiungi i clienti numerati da 1 a 4 alla coda, poi servili uno alla volta stampando `"Cliente N servito."` a ogni estrazione.

**Esempio output:**
```
Cliente 1 servito.
Cliente 2 servito.
Cliente 3 servito.
Cliente 4 servito.
```

**💡 Hint:**
1. Dichiara `int coda[10]`, `head = 0`, `tail = 0`, `size = 0`.
2. Ciclo `for` da 1 a 4: chiama `enqueue(i)`.
3. Ciclo `while (!isEmpty())`: chiama `dequeue()` e stampa il risultato.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

#define MAX 10

int coda[MAX];
int head = 0, tail = 0, size = 0;

void enqueue(int v) {
    if (size < MAX) { coda[tail++] = v; size++; }
}

int dequeue() {
    if (size == 0) return -1;
    size--;
    return coda[head++];
}

int isEmpty() { return size == 0; }

int main() {
    for (int i = 1; i <= 4; i++) enqueue(i);

    while (!isEmpty()) {
        printf("Cliente %d servito.\n", dequeue());
    }
    return 0;
}
```

</details>

---

## 🟡 Livello Intermedio

### Esercizio 3 — Controlla parentesi bilanciate (20–30 min)

**Testo:**
Leggi una stringa (max 50 caratteri) e verifica se le parentesi tonde `(` e `)` sono bilanciate usando una pila di caratteri.

Esempi:
- `(a+(b*c))` → **Bilanciata: SI**
- `((x+y)` → **Bilanciata: NO**
- `)x+y(` → **Bilanciata: NO**

**Esempio input/output:**
```
Inserisci stringa: (a+(b*c))
Parentesi bilanciate: SI
```

**💡 Hint:**
1. Scorri la stringa con un ciclo `for` e `strlen`.
2. Se trovi `(`, fai `push('(')`.
3. Se trovi `)`: se la pila è vuota → NO; altrimenti `pop()`.
4. Alla fine: se la pila è vuota → SI; altrimenti → NO.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <string.h>

#define MAX 50

char pila[MAX];
int top = -1;

void push(char c) { if (top < MAX-1) pila[++top] = c; }
char pop()        { return (top == -1) ? '\0' : pila[top--]; }
int isEmpty()     { return top == -1; }

int main() {
    char s[MAX + 1];
    printf("Inserisci stringa: ");
    scanf("%s", s);

    int ok = 1;
    int len = strlen(s);

    for (int i = 0; i < len && ok; i++) {
        if (s[i] == '(') {
            push('(');
        } else if (s[i] == ')') {
            if (isEmpty()) ok = 0;
            else pop();
        }
    }

    if (!isEmpty()) ok = 0;

    printf("Parentesi bilanciate: %s\n", ok ? "SI" : "NO");
    return 0;
}
```

</details>

---

### Esercizio 4 — Due code con priorità (25–30 min)

**Testo:**
Simula uno sportello con due code: **urgenti** e **normali**. Il programma legge N persone (max 6), ciascuna con numero e priorità (1=urgente, 0=normale). Prima vengono servite tutte le urgenti (nell'ordine di arrivo), poi le normali.

**Esempio input:**
```
Quante persone? 4
Persona 1, priorita (1=urgente, 0=normale): 0
Persona 2, priorita (1=urgente, 0=normale): 1
Persona 3, priorita (1=urgente, 0=normale): 0
Persona 4, priorita (1=urgente, 0=normale): 1
```

**Esempio output:**
```
Ordine di servizio:
Persona 2 (urgente)
Persona 4 (urgente)
Persona 1 (normale)
Persona 3 (normale)
```

**💡 Hint:**
1. Usa due array separati `coda_urgenti[]` e `coda_normali[]` con indici `tu` e `tn`.
2. Leggi le N persone e smistale nell'array giusto.
3. Stampa prima `coda_urgenti`, poi `coda_normali`.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

#define MAX 6

int coda_urgenti[MAX], tu = 0;
int coda_normali[MAX], tn = 0;

int main() {
    int n;
    printf("Quante persone? ");
    scanf("%d", &n);
    if (n > MAX) n = MAX;

    for (int i = 1; i <= n; i++) {
        int p;
        printf("Persona %d, priorita (1=urgente, 0=normale): ", i);
        scanf("%d", &p);
        if (p == 1) coda_urgenti[tu++] = i;
        else        coda_normali[tn++] = i;
    }

    printf("Ordine di servizio:\n");
    for (int i = 0; i < tu; i++)
        printf("Persona %d (urgente)\n", coda_urgenti[i]);
    for (int i = 0; i < tn; i++)
        printf("Persona %d (normale)\n", coda_normali[i]);

    return 0;
}
```

</details>

---

### Esercizio 5 — Interprete di comandi per la pila (20–25 min)

**Testo:**
Leggi comandi da tastiera:
- `P N` → push del numero N
- `O` → pop (stampa il valore rimosso, o `"vuota"` se la pila è vuota)
- `F` → fine programma

**Esempio input:**
```
P 5
P 12
O
P 3
O
O
F
```

**Esempio output:**
```
Pop: 12
Pop: 3
Pop: 5
```

**💡 Hint:**
1. Usa `scanf(" %c", &cmd)` per leggere il carattere comando.
2. Se `cmd == 'P'`: leggi anche un intero e fai push.
3. Se `cmd == 'O'`: fai pop e stampa.
4. Se `cmd == 'F'`: `break`.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

#define MAX 10

int pila[MAX];
int top = -1;

void push(int v) { if (top < MAX-1) pila[++top] = v; }
int pop()        { return (top == -1) ? -999 : pila[top--]; }
int isEmpty()    { return top == -1; }

int main() {
    char cmd;
    while (scanf(" %c", &cmd) == 1) {
        if (cmd == 'P') {
            int n; scanf("%d", &n);
            push(n);
        } else if (cmd == 'O') {
            if (isEmpty()) printf("Pop: vuota\n");
            else printf("Pop: %d\n", pop());
        } else if (cmd == 'F') {
            break;
        }
    }
    return 0;
}
```

</details>

---

### Esercizio 5b — Coda Circolare: riempi, svuota e riempi (20–25 min)

**Testo:**
Dimostra il vantaggio della coda circolare rispetto a quella lineare. Con un array di 4 slot:
1. Inserisci 3 elementi (10, 20, 30)
2. Estrai 2 elementi
3. Inserisci altri 3 elementi (40, 50, 60)
4. Stampa tutti gli elementi rimasti in coda

Con la coda **lineare** il passo 3 fallirebbe (tail raggiungerebbe il limite). Con la coda **circolare** funziona perché gli slot liberati vengono riutilizzati.

**Esempio output:**
```
Estratto: 10
Estratto: 20
Coda finale: 30 40 50 60
```

**💡 Hint:**
1. Implementa `enqueue` e `dequeue` usando `(indice + 1) % MAX` con `MAX = 4`.
2. Dopo i 2 `dequeue`, `head` è a 2. Inserendo altri elementi, `tail` passa per 3 poi torna a 0 e 1.
3. Per stampare: `for (i = 0; i < size; i++) printf("%d ", coda[(head + i) % MAX])`.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

#define MAX 4

int coda[MAX];
int head = 0, tail = 0, size = 0;

int isEmpty() { return size == 0; }
int isFull()  { return size == MAX; }

void enqueue(int v) {
    if (isFull()) { printf("Coda piena!\n"); return; }
    coda[tail] = v;
    tail = (tail + 1) % MAX;
    size++;
}

int dequeue() {
    if (isEmpty()) { printf("Coda vuota!\n"); return -1; }
    int v = coda[head];
    head = (head + 1) % MAX;
    size--;
    return v;
}

void stampa() {
    printf("Coda finale:");
    for (int i = 0; i < size; i++)
        printf(" %d", coda[(head + i) % MAX]);
    printf("\n");
}

int main() {
    enqueue(10); enqueue(20); enqueue(30);
    printf("Estratto: %d\n", dequeue());
    printf("Estratto: %d\n", dequeue());
    enqueue(40); enqueue(50); enqueue(60);
    stampa();
    return 0;
}
```

</details>

---

## 🔴 Livello Avanzato

### Esercizio 6 — Coda di messaggi interattiva (30–40 min)

**Testo:**
Simula una coda di messaggi di testo. Comandi:
- `A TESTO` → aggiunge il messaggio TESTO (max 20 car.)
- `L` → legge ed elimina il primo messaggio
- `S` → mostra tutti i messaggi in coda
- `Q` → termina

Capacità massima: 5 messaggi.

**Esempio sessione:**
```
> A Ciao
> A Buongiorno
> A HaiVisto
> S
  [0] Ciao
  [1] Buongiorno
  [2] HaiVisto
> L
Messaggio letto: Ciao
> S
  [0] Buongiorno
  [1] HaiVisto
> Q
```

**💡 Hint:**
1. Usa `char coda[5][21]` per i messaggi.
2. `enqueue`: `strcpy(coda[tail], testo)` poi incrementa `tail` e `size`.
3. `dequeue`: stampa `coda[head]`, incrementa `head`, decrementa `size`.
4. `mostra`: ciclo `for (i = 0; i < size; i++)` — accede a `coda[(head + i) % MAX_MSG]`.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <string.h>

#define MAX_MSG 5
#define MAX_LEN 21

char coda[MAX_MSG][MAX_LEN];
int head = 0, tail = 0, size = 0;

void enqueue(char *testo) {
    if (size == MAX_MSG) { printf("Coda piena!\n"); return; }
    strcpy(coda[tail], testo);
    tail = (tail + 1) % MAX_MSG;
    size++;
}

void dequeue() {
    if (size == 0) { printf("Nessun messaggio.\n"); return; }
    printf("Messaggio letto: %s\n", coda[head]);
    head = (head + 1) % MAX_MSG;
    size--;
}

void mostra() {
    if (size == 0) { printf("Coda vuota.\n"); return; }
    for (int i = 0; i < size; i++)
        printf("  [%d] %s\n", i, coda[(head + i) % MAX_MSG]);
}

int main() {
    char cmd;
    char testo[MAX_LEN];
    while (1) {
        printf("> ");
        scanf(" %c", &cmd);
        if      (cmd == 'A') { scanf("%20s", testo); enqueue(testo); }
        else if (cmd == 'L') dequeue();
        else if (cmd == 'S') mostra();
        else if (cmd == 'Q') break;
    }
    return 0;
}
```

</details>

---

### Esercizio 7 — Valuta un'espressione aritmetica (35–45 min)

**Testo:**
Leggi un'espressione con **interi a una cifra** e operatori `+` e `-` senza spazi (es. `3+5-2+1`) e calcolane il valore.

> ⚠️ NOTA: Per semplicità gli operatori non hanno precedenza — l'espressione viene elaborata da sinistra a destra.

**Esempio input/output:**
```
Espressione: 3+5-2+1
Risultato: 7
```

**💡 Hint:**
1. Leggi la stringa con `scanf`.
2. Il valore di un carattere cifra si ottiene con `c - '0'`.
3. Inizializza `risultato` con il primo carattere convertito in intero.
4. Scorri la stringa a passi di 2 (`i += 2`): leggi operatore e operando, aggiorna `risultato`.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <string.h>

int main() {
    char expr[50];
    printf("Espressione: ");
    scanf("%s", expr);

    int risultato = expr[0] - '0';
    int len = strlen(expr);

    for (int i = 1; i < len - 1; i += 2) {
        char op = expr[i];
        int operando = expr[i + 1] - '0';
        if (op == '+') risultato += operando;
        else if (op == '-') risultato -= operando;
    }

    printf("Risultato: %d\n", risultato);
    return 0;
}
```

</details>



---

# 20 lezione ordinamento studente completo

**File:** `20 lezione ordinamento studente completo.md`
**Tipo:** `.md`
**Dimensione:** 28.3 KB
**Ultima modifica:** 02/07/2026 09:24

---

# Lezione: Algoritmi di Ordinamento
**Durata totale:** 4 ore
**Teoria:** 1.5 ore | **Esercizi:** 2.5 ore
**Data:** _______________
**Ambiente:** CLion (JetBrains)

---

## PARTE 1 — TEORIA (1.5 ore)

---

### 1.1 Introduzione e Motivazione

#### Perché ordinare?

Immagina di avere una rubrica telefonica con 1000 contatti in ordine casuale. Cercare "Verdi Mario" richiede di leggere ogni nome, uno per uno, fino a trovarlo — nel caso peggiore, tutti e 1000. Se invece la rubrica è in ordine alfabetico, si apre direttamente nella sezione "V" e in pochi secondi il contatto è trovato.

**Questo è il potere dell'ordinamento:** rendere i dati più facili da consultare, cercare e gestire.

Nella programmazione, ordinare un array è una delle operazioni più frequenti:
- Visualizzare una classifica di punteggi dal più alto al più basso
- Mostrare prodotti dal più economico al più costoso
- Trovare il valore minimo o massimo
- Preparare i dati per algoritmi più efficienti

#### Definizione

Ordinare un array significa riorganizzare i suoi elementi in modo che rispettino un criterio — tipicamente **crescente** (dal più piccolo al più grande) o **decrescente** (dal più grande al più piccolo).

```
Prima:  [64, 25, 12, 22, 11]
Dopo:   [11, 12, 22, 25, 64]   ← ordine crescente
```

---

### 1.2 Spiegazione degli Algoritmi

In questa lezione studiamo tre algoritmi classici, tutti con complessità **O(n²)**: adatti a dataset piccoli e ottimi per capire i principi fondamentali dell'ordinamento.

---

#### 🫧 Bubble Sort — Ordinamento a Bolle

**Idea di base:** confronta coppie di elementi adiacenti e scambiali se sono nell'ordine sbagliato. Ripeti finché l'array non è ordinato. Gli elementi grandi "affondano" verso destra come bolle che salgono.

**Visualizzazione passo-passo su `[64, 25, 12, 22, 11]`:**

```
PASSATA 1:
[64, 25, 12, 22, 11]
 ↑   ↑
 64 > 25 → SCAMBIA
[25, 64, 12, 22, 11]
     ↑   ↑
     64 > 12 → SCAMBIA
[25, 12, 64, 22, 11]
         ↑   ↑
         64 > 22 → SCAMBIA
[25, 12, 22, 64, 11]
             ↑   ↑
             64 > 11 → SCAMBIA
[25, 12, 22, 11, 64]  ← 64 è al suo posto!

PASSATA 2:
[25, 12, 22, 11 | 64]
 ↑   ↑
 25 > 12 → SCAMBIA
[12, 25, 22, 11 | 64]
     ↑   ↑
     25 > 22 → SCAMBIA
[12, 22, 25, 11 | 64]
         ↑   ↑
         25 > 11 → SCAMBIA
[12, 22, 11, 25 | 64]  ← 25 è al suo posto!

... continua fino a ordinamento completo ...

RISULTATO: [11, 12, 22, 25, 64]
```

**Struttura del codice:**
```
Per ogni passata i da 0 a n-2:
    Per ogni posizione j da 0 a n-2-i:
        Se arr[j] > arr[j+1]:
            scambia arr[j] e arr[j+1]
```

**Caratteristiche:**
- Complessità: O(n²) — due cicli annidati
- Stabile: sì (elementi uguali non vengono scambiati)
- Semplice da capire e implementare

---

#### 🎯 Selection Sort — Ordinamento per Selezione

**Idea di base:** trova il minimo nell'array non ancora ordinato e mettilo nella posizione corretta. Ripeti riducendo ogni volta la porzione da esaminare.

**Visualizzazione passo-passo su `[64, 25, 12, 22, 11]`:**

```
PASSO 1: cerca il minimo in [64, 25, 12, 22, 11]
         minimo = 11 (indice 4)
         scambia posizione 0 con posizione 4
[11 | 25, 12, 22, 64]
 ↑ ordinato

PASSO 2: cerca il minimo in [25, 12, 22, 64]
         minimo = 12 (indice 2)
         scambia posizione 1 con posizione 2
[11, 12 | 25, 22, 64]
     ↑ ordinato

PASSO 3: cerca il minimo in [25, 22, 64]
         minimo = 22 (indice 3)
         scambia posizione 2 con posizione 3
[11, 12, 22 | 25, 64]
         ↑ ordinato

PASSO 4: cerca il minimo in [25, 64]
         minimo = 25 (indice 3)
         nessuno scambio necessario
[11, 12, 22, 25 | 64]
             ↑ ordinato

RISULTATO: [11, 12, 22, 25, 64]
```

**Struttura del codice:**
```
Per ogni posizione i da 0 a n-2:
    Trova l'indice del minimo tra i e n-1
    Se il minimo non è già in posizione i:
        scambia arr[i] con arr[indice_minimo]
```

**Caratteristiche:**
- Complessità: O(n²) — sempre, anche su array già ordinato
- Numero di scambi: O(n) — al massimo n-1 scambi (vantaggio!)
- Non stabile: può scambiare elementi uguali distanti

---

#### 🃏 Insertion Sort — Ordinamento per Inserimento

**Idea di base:** considera l'array diviso in una parte sinistra ordinata e una parte destra non ancora ordinata. Prende ogni nuovo elemento dalla parte destra e lo "inserisce" nella posizione giusta a sinistra. È come ordinare le carte da gioco in mano.

**Visualizzazione passo-passo su `[64, 25, 12, 22, 11]`:**

```
Stato iniziale: [64 | 25, 12, 22, 11]
                 ↑ ordinato (1 elemento)

PASSO 1: prendo 25, lo confronto con 64
         25 < 64 → sposto 64 a destra
         inserisco 25 in posizione 0
[25, 64 | 12, 22, 11]
 ↑   ↑ ordinato

PASSO 2: prendo 12, lo confronto con 64 → sposto 64
         12 < 25 → sposto 25
         inserisco 12 in posizione 0
[12, 25, 64 | 22, 11]
 ↑   ↑   ↑ ordinato

PASSO 3: prendo 22, lo confronto con 64 → sposto 64
         22 < 25 → sposto 25
         22 > 12 → stop, inserisco 22 in posizione 2
[12, 25, 64 | 22, 11]  →  [12, 22, 25, 64 | 11]

PASSO 4: prendo 11, lo confronto con tutti → sposto tutto
         inserisco 11 in posizione 0
[11, 12, 22, 25, 64]

RISULTATO: [11, 12, 22, 25, 64]
```

**Struttura del codice:**
```
Per ogni posizione i da 1 a n-1:
    chiave = arr[i]
    j = i - 1
    Mentre j >= 0 e arr[j] > chiave:
        arr[j+1] = arr[j]   (sposta a destra)
        j--
    arr[j+1] = chiave       (inserisci)
```

**Caratteristiche:**
- Complessità: O(n²) peggiore, O(n) su array già ordinato
- Stabile: sì
- Ottimo per array piccoli o quasi ordinati

---

### 1.3 Esempi di Codice Commentati

#### Esempio 1 — Bubble Sort

```c
#include <stdio.h>

// Funzione che stampa gli elementi di un array
void stampa_array(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Funzione che ordina l'array con Bubble Sort
void bubble_sort(int arr[], int n) {
    int temp;
    // i = numero di passata (ogni passata mette a posto un elemento)
    for (int i = 0; i < n - 1; i++) {
        // j = indice di confronto (si ferma prima degli elementi già ordinati)
        for (int j = 0; j < n - 1 - i; j++) {
            // Se l'elemento corrente è maggiore del successivo, scambia
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int numeri[] = {64, 25, 12, 22, 11};
    int n = 5;

    printf("Prima: ");
    stampa_array(numeri, n);

    bubble_sort(numeri, n);

    printf("Dopo:  ");
    stampa_array(numeri, n);

    return 0;
}
```

**Output atteso:**
```
Prima: 64 25 12 22 11
Dopo:  11 12 22 25 64
```

---

#### Esempio 2 — Selection Sort

```c
#include <stdio.h>

void stampa_array(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void selection_sort(int arr[], int n) {
    int indice_min, temp;

    for (int i = 0; i < n - 1; i++) {
        // Supponiamo che il minimo sia nella posizione i
        indice_min = i;

        // Cerca il vero minimo nella parte non ordinata
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[indice_min]) {
                indice_min = j;  // aggiorna l'indice del minimo
            }
        }

        // Scambia solo se il minimo non è già in posizione
        if (indice_min != i) {
            temp = arr[i];
            arr[i] = arr[indice_min];
            arr[indice_min] = temp;
        }
    }
}

int main() {
    int numeri[] = {29, 10, 14, 37, 13};
    int n = 5;

    printf("Prima: ");
    stampa_array(numeri, n);

    selection_sort(numeri, n);

    printf("Dopo:  ");
    stampa_array(numeri, n);

    return 0;
}
```

**Output atteso:**
```
Prima: 29 10 14 37 13
Dopo:  10 13 14 29 37
```

---

#### Esempio 3 — Insertion Sort

```c
#include <stdio.h>

void stampa_array(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void insertion_sort(int arr[], int n) {
    int chiave, j;

    for (int i = 1; i < n; i++) {
        chiave = arr[i];  // elemento da inserire nella parte ordinata
        j = i - 1;

        // Sposta a destra tutti gli elementi maggiori della chiave
        while (j >= 0 && arr[j] > chiave) {
            arr[j + 1] = arr[j];
            j--;
        }

        // Inserisci la chiave nella posizione corretta
        arr[j + 1] = chiave;
    }
}

int main() {
    int numeri[] = {5, 2, 9, 1, 7};
    int n = 5;

    printf("Prima: ");
    stampa_array(numeri, n);

    insertion_sort(numeri, n);

    printf("Dopo:  ");
    stampa_array(numeri, n);

    return 0;
}
```

**Output atteso:**
```
Prima: 5 2 9 1 7
Dopo:  1 2 5 7 9
```

---

### 1.4 Riepilogo Visivo

```
╔══════════════════════════════════════════════════════════════════╗
║           CONFRONTO ALGORITMI DI ORDINAMENTO O(n²)               ║
╠═══════════════════╦══════════════╦═══════════╦═══════════════════╣
║ Algoritmo         ║ Come funziona║  Stabile? ║ Punto di forza    ║
╠═══════════════════╬══════════════╬═══════════╬═══════════════════╣
║ Bubble Sort       ║ Confronta    ║    SÌ     ║ Semplicità        ║
║                   ║ adiacenti e  ║           ║ Didattico         ║
║                   ║ scambia      ║           ║                   ║
╠═══════════════════╬══════════════╬═══════════╬═══════════════════╣
║ Selection Sort    ║ Cerca il     ║    NO     ║ Pochi scambi      ║
║                   ║ minimo e lo  ║           ║ (utile se scamb.  ║
║                   ║ porta davanti║           ║  sono costosi)    ║
╠═══════════════════╬══════════════╬═══════════╬═══════════════════╣
║ Insertion Sort    ║ Inserisce    ║    SÌ     ║ Veloce su array   ║
║                   ║ ogni elem.   ║           ║ piccoli/quasi     ║
║                   ║ nella pos.   ║           ║ ordinati          ║
║                   ║ corretta     ║           ║                   ║
╚═══════════════════╩══════════════╩═══════════╩═══════════════════╝

Tutti e tre: complessità O(n²), in-place (non servono array extra)
```

**La tecnica dello scambio — da memorizzare:**
```
Per scambiare arr[a] e arr[b]:
    temp   = arr[a]   // salvo arr[a]
    arr[a] = arr[b]   // sovrascrivo arr[a]
    arr[b] = temp     // metto il valore salvato in arr[b]

⚠️ Senza variabile temp, il valore originale andrebbe perso!
```

---

### 1.5 Domande di Verifica Orale

**D1:** Cosa significa che un algoritmo di ordinamento è "stabile"?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Un algoritmo stabile preserva l'ordine relativo degli elementi con lo stesso valore. Se prima dell'ordinamento A viene prima di B e A = B, dopo l'ordinamento A è ancora prima di B. Tra gli algoritmi visti, Bubble Sort e Insertion Sort sono stabili, Selection Sort non lo è.

</details>

**D2:** Perché nel Bubble Sort il ciclo interno arriva fino a `n - 1 - i` invece di `n - 1`?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Perché dopo ogni passata i, l'elemento più grande della porzione esaminata è già "affondato" nella posizione corretta in fondo all'array. Non ha senso ricontrollarlo. In questo modo si risparmia qualche confronto inutile.

</details>

**D3:** Quanti scambi esegue al massimo il Selection Sort su un array di n elementi?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Al massimo n-1 scambi, uno per ogni passata. È il suo punto di forza: esegue pochi scambi rispetto al Bubble Sort che può farne molti di più.

</details>

**D4:** Perché nella tecnica dello scambio è necessaria una variabile temporanea `temp`?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Perché se scrivessi direttamente `arr[a] = arr[b]`, perderei il valore originale di `arr[a]` prima di averlo salvato da qualche parte. La variabile `temp` funge da deposito temporaneo che permette di non perdere nessun valore.

</details>

**D5:** In quale situazione Insertion Sort è particolarmente efficiente? Perché?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Su array già ordinati o quasi ordinati. Perché il ciclo `while` interno non esegue quasi nessun passo: ogni nuovo elemento è già nella posizione giusta (o molto vicino), quindi non servono spostamenti. In questo caso la complessità diventa O(n) invece di O(n²).

</details>

**D6:** Quale dei tre algoritmi visti sceglieresti per ordinare un array di soli 5 elementi? Ha importanza la scelta?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Per 5 elementi qualsiasi dei tre va benissimo — le differenze di prestazione sono trascurabili. In generale, Insertion Sort è considerato il migliore per array molto piccoli. Su dataset così ridotti l'importante è la correttezza del codice, non l'efficienza.

</details>

**D7:** Cosa succederebbe se dimenticassimo la variabile `temp` e scrivessimo `arr[j] = arr[j+1]; arr[j+1] = arr[j];`?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Entrambi gli elementi finirebbero per avere lo stesso valore (quello di `arr[j+1]`), perdendo il valore originale di `arr[j]`. Lo scambio non avverrebbe correttamente.

</details>

---

## PARTE 2 — ESERCIZI (2.5 ore)

---

### 🟢 Livello Base

---

#### Esercizio B1 — Simulazione manuale del Bubble Sort (15-20 min)

**Testo:**
Scrivi un programma che esegue il Bubble Sort su un array di 6 interi inseriti dall'utente, stampando lo stato dell'array dopo ogni passata completa.

**Esempio input/output:**
```
Inserisci 6 numeri: 5 3 8 1 9 2

Passata 1: 3 5 1 8 2 9
Passata 2: 3 1 5 2 8 9
Passata 3: 1 3 2 5 8 9
Passata 4: 1 2 3 5 8 9
Passata 5: 1 2 3 5 8 9

Array ordinato: 1 2 3 5 8 9
```

**💡 Hint:**
1. Usa `scanf` in un ciclo per leggere i 6 elementi
2. Aggiungi una `printf` dentro il ciclo esterno del Bubble Sort (dopo il ciclo interno) per stampare l'array a ogni passata
3. Crea una funzione `stampa_array` separata per non ripetere codice
4. Il numero di passate è sempre `n - 1`

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

#define N 6

void stampa_array(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[N];
    int temp;

    printf("Inserisci %d numeri: ", N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    for (int i = 0; i < N - 1; i++) {
        for (int j = 0; j < N - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
        printf("Passata %d: ", i + 1);
        stampa_array(arr, N);
    }

    printf("\nArray ordinato: ");
    stampa_array(arr, N);

    return 0;
}
```

</details>

---

#### Esercizio B2 — Trova il minimo con Selection Sort (15-20 min)

**Testo:**
Scrivi un programma che ordina un array di 5 numeri interi (definiti direttamente nel codice) usando il Selection Sort, e stampa quale scambio viene effettuato a ogni passo nel formato: `Passo X: scambio arr[i]=V1 con arr[j]=V2`.

**Esempio input/output:**
```
Array iniziale: 29 10 14 37 13

Passo 1: scambio arr[0]=29 con arr[1]=10
Passo 2: scambio arr[1]=29 con arr[4]=13
Passo 3: nessuno scambio necessario
Passo 4: nessuno scambio necessario

Array ordinato: 10 13 14 29 37
```

**💡 Hint:**
1. Tieni traccia dell'indice del minimo durante la ricerca
2. Prima dello scambio, stampa i valori coinvolti
3. Se `indice_min == i` non serve scambiare — stampalo esplicitamente

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

void stampa_array(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {29, 10, 14, 37, 13};
    int n = 5;
    int indice_min, temp;

    printf("Array iniziale: ");
    stampa_array(arr, n);
    printf("\n");

    for (int i = 0; i < n - 1; i++) {
        indice_min = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[indice_min]) {
                indice_min = j;
            }
        }

        if (indice_min != i) {
            printf("Passo %d: scambio arr[%d]=%d con arr[%d]=%d\n",
                   i + 1, i, arr[i], indice_min, arr[indice_min]);
            temp = arr[i];
            arr[i] = arr[indice_min];
            arr[indice_min] = temp;
        } else {
            printf("Passo %d: nessuno scambio necessario\n", i + 1);
        }
    }

    printf("\nArray ordinato: ");
    stampa_array(arr, n);

    return 0;
}
```

</details>

---

### 🟡 Livello Intermedio

---

#### Esercizio I1 — Ordinamento decrescente con Insertion Sort (20-25 min)

**Testo:**
Scrivi un programma che legge dall'utente N interi (con N definito come costante a 7) e li ordina in ordine **decrescente** usando Insertion Sort. Stampa l'array prima e dopo l'ordinamento.

**Esempio input/output:**
```
Inserisci 7 numeri: 4 7 2 9 1 6 3

Prima:  4 7 2 9 1 6 3
Dopo:   9 7 6 4 3 2 1
```

**💡 Hint:**
1. L'Insertion Sort decrescente cambia solo la condizione del `while`: invece di `arr[j] > chiave`, usa `arr[j] < chiave`
2. Il resto della logica rimane identico
3. Prova prima a implementare l'Insertion Sort crescente, poi modifica la condizione

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

#define N 7

void stampa_array(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void insertion_sort_decrescente(int arr[], int n) {
    int chiave, j;
    for (int i = 1; i < n; i++) {
        chiave = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] < chiave) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = chiave;
    }
}

int main() {
    int arr[N];

    printf("Inserisci %d numeri: ", N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    printf("\nPrima:  ");
    stampa_array(arr, N);

    insertion_sort_decrescente(arr, N);

    printf("Dopo:   ");
    stampa_array(arr, N);

    return 0;
}
```

</details>

---

#### Esercizio I2 — Conta gli scambi (20-25 min)

**Testo:**
Scrivi un programma che chiede all'utente 8 numeri interi e li ordina con il Bubble Sort, contando e stampando il numero totale di scambi effettuati. Alla fine stampa anche il numero di passate eseguite prima che l'array risultasse ordinato.

**Esempio input/output:**
```
Inserisci 8 numeri: 3 1 4 1 5 9 2 6

Ordinamento completato in 5 passate.
Numero totale di scambi: 8

Array ordinato: 1 1 2 3 4 5 6 9
```

**💡 Hint:**
1. Usa due variabili contatore: `scambi` e `passate`
2. Per contare le passate realmente utili, aggiungi un flag booleano (intero 0/1) che segnala se è avvenuto almeno uno scambio in una passata — se non è avvenuto nessuno scambio, l'array è già ordinato e si può fermare
3. Inizializza il flag a 0 all'inizio di ogni passata e mettilo a 1 quando avviene uno scambio

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

#define N 8

void stampa_array(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[N];
    int temp;
    int scambi = 0;
    int passate = 0;
    int scambio_avvenuto;

    printf("Inserisci %d numeri: ", N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    for (int i = 0; i < N - 1; i++) {
        scambio_avvenuto = 0;
        for (int j = 0; j < N - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                scambi++;
                scambio_avvenuto = 1;
            }
        }
        passate++;
        if (!scambio_avvenuto) {
            break;
        }
    }

    printf("\nOrdinamento completato in %d passate.\n", passate);
    printf("Numero totale di scambi: %d\n", scambi);
    printf("\nArray ordinato: ");
    stampa_array(arr, N);

    return 0;
}
```

</details>

---

#### Esercizio I3 — Ordinamento di voti (25-30 min)

**Testo:**
Un professore ha i voti di 10 studenti (interi da 0 a 30) inseriti dall'utente. Scrivi un programma che:
1. Legge i 10 voti
2. Li ordina in ordine crescente con uno dei tre algoritmi visti
3. Stampa i voti ordinati
4. Stampa il voto minimo, massimo e la media (come numero decimale)

**Esempio input/output:**
```
Inserisci 10 voti: 18 27 30 22 15 28 19 24 30 20

Voti ordinati: 15 18 19 20 22 24 27 28 30 30

Voto minimo:  15
Voto massimo: 30
Media:        23.30
```

**💡 Hint:**
1. Dopo l'ordinamento, il minimo è `arr[0]` e il massimo è `arr[n-1]` — non serve cercarli!
2. Per la media, usa una variabile `float` o fai la divisione con `(float)`
3. Usa `%.2f` in `printf` per stampare due decimali
4. Puoi usare qualsiasi algoritmo di ordinamento tra quelli visti

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

#define N 10

void stampa_array(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void bubble_sort(int arr[], int n) {
    int temp;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int voti[N];
    int somma = 0;
    float media;

    printf("Inserisci %d voti: ", N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &voti[i]);
        somma += voti[i];
    }

    bubble_sort(voti, N);

    printf("\nVoti ordinati: ");
    stampa_array(voti, N);

    media = (float)somma / N;

    printf("\nVoto minimo:  %d\n", voti[0]);
    printf("Voto massimo: %d\n", voti[N - 1]);
    printf("Media:        %.2f\n", media);

    return 0;
}
```

</details>

---

### 🔴 Livello Avanzato

---

#### Esercizio A1 — Confronto tra algoritmi (30-40 min)

**Testo:**
Scrivi un programma che chiede all'utente un array di 10 interi e lo ordina con tutti e tre gli algoritmi (Bubble, Selection, Insertion). Per ciascuno, stampa il numero di confronti e di scambi effettuati. Lavora su tre copie dell'array originale in modo che gli algoritmi partano tutti dagli stessi dati.

**Esempio input/output:**
```
Inserisci 10 numeri: 9 3 7 1 5 8 2 6 4 10

=== Bubble Sort ===
Confronti: 45   Scambi: 21
Risultato: 1 2 3 4 5 6 7 8 9 10

=== Selection Sort ===
Confronti: 45   Scambi: 8
Risultato: 1 2 3 4 5 6 7 8 9 10

=== Insertion Sort ===
Confronti: 21   Scambi: 21
Risultato: 1 2 3 4 5 6 7 8 9 10
```

**💡 Hint:**
1. Copia l'array originale in tre array distinti (con un ciclo `for`) prima di applicare gli algoritmi
2. Aggiungi contatori `confronti` e `scambi` come parametri per ogni funzione — oppure usa variabili globali (più semplice, ma meno elegante)
3. Ogni `if (arr[j] > arr[j+1])` è un confronto; ogni successivo scambio è... uno scambio
4. I valori esatti dipendono dall'input: l'importante è che i tre risultati siano tutti ordinati correttamente

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

#define N 10

void stampa_array(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void copia_array(int src[], int dst[], int n) {
    for (int i = 0; i < n; i++) {
        dst[i] = src[i];
    }
}

void bubble_sort(int arr[], int n, int *confronti, int *scambi) {
    int temp;
    *confronti = 0;
    *scambi = 0;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            (*confronti)++;
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                (*scambi)++;
            }
        }
    }
}

void selection_sort(int arr[], int n, int *confronti, int *scambi) {
    int indice_min, temp;
    *confronti = 0;
    *scambi = 0;
    for (int i = 0; i < n - 1; i++) {
        indice_min = i;
        for (int j = i + 1; j < n; j++) {
            (*confronti)++;
            if (arr[j] < arr[indice_min]) {
                indice_min = j;
            }
        }
        if (indice_min != i) {
            temp = arr[i];
            arr[i] = arr[indice_min];
            arr[indice_min] = temp;
            (*scambi)++;
        }
    }
}

void insertion_sort(int arr[], int n, int *confronti, int *scambi) {
    int chiave, j;
    *confronti = 0;
    *scambi = 0;
    for (int i = 1; i < n; i++) {
        chiave = arr[i];
        j = i - 1;
        while (j >= 0 && ((*confronti)++, arr[j] > chiave)) {
            arr[j + 1] = arr[j];
            j--;
            (*scambi)++;
        }
        arr[j + 1] = chiave;
    }
}

int main() {
    int originale[N];
    int a1[N], a2[N], a3[N];
    int confronti, scambi;

    printf("Inserisci %d numeri: ", N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &originale[i]);
    }

    copia_array(originale, a1, N);
    copia_array(originale, a2, N);
    copia_array(originale, a3, N);

    printf("\n=== Bubble Sort ===\n");
    bubble_sort(a1, N, &confronti, &scambi);
    printf("Confronti: %d   Scambi: %d\n", confronti, scambi);
    printf("Risultato: ");
    stampa_array(a1, N);

    printf("\n=== Selection Sort ===\n");
    selection_sort(a2, N, &confronti, &scambi);
    printf("Confronti: %d   Scambi: %d\n", confronti, scambi);
    printf("Risultato: ");
    stampa_array(a2, N);

    printf("\n=== Insertion Sort ===\n");
    insertion_sort(a3, N, &confronti, &scambi);
    printf("Confronti: %d   Scambi: %d\n", confronti, scambi);
    printf("Risultato: ");
    stampa_array(a3, N);

    return 0;
}
```

</details>

---

#### Esercizio A2 — Ordinamento di stringhe (40-45 min)

**Testo:**
Scrivi un programma che legge 5 parole (stringhe di massimo 20 caratteri) e le ordina alfabeticamente usando il Selection Sort. Usa `strcmp` per confrontare le stringhe e `strcpy` per copiarle. Stampa l'elenco prima e dopo l'ordinamento.

**Esempio input/output:**
```
Inserisci 5 parole:
Parola 1: mela
Parola 2: arancia
Parola 3: banana
Parola 4: kiwi
Parola 5: fico

Prima:  mela arancia banana kiwi fico
Dopo:   arancia banana fico kiwi mela
```

**💡 Hint:**
1. Dichiara l'array come `char parole[5][21]` — 5 stringhe, ognuna da max 20 caratteri + terminatore
2. Usa `scanf("%s", parole[i])` per leggere ogni stringa
3. `strcmp(a, b)` restituisce un valore negativo se `a` viene prima di `b` alfabeticamente, 0 se sono uguali, positivo se `a` viene dopo
4. Per scambiare due stringhe, usa un array temporaneo `char temp[21]` e `strcpy`

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <string.h>

#define N 5
#define MAX_LEN 21

void stampa_parole(char parole[][MAX_LEN], int n) {
    for (int i = 0; i < n; i++) {
        printf("%s ", parole[i]);
    }
    printf("\n");
}

void selection_sort_stringhe(char parole[][MAX_LEN], int n) {
    int indice_min;
    char temp[MAX_LEN];

    for (int i = 0; i < n - 1; i++) {
        indice_min = i;
        for (int j = i + 1; j < n; j++) {
            if (strcmp(parole[j], parole[indice_min]) < 0) {
                indice_min = j;
            }
        }
        if (indice_min != i) {
            strcpy(temp, parole[i]);
            strcpy(parole[i], parole[indice_min]);
            strcpy(parole[indice_min], temp);
        }
    }
}

int main() {
    char parole[N][MAX_LEN];

    printf("Inserisci %d parole:\n", N);
    for (int i = 0; i < N; i++) {
        printf("Parola %d: ", i + 1);
        scanf("%s", parole[i]);
    }

    printf("\nPrima:  ");
    stampa_parole(parole, N);

    selection_sort_stringhe(parole, N);

    printf("Dopo:   ");
    stampa_parole(parole, N);

    return 0;
}
```

</details>



---

# 21 lezione stringhe studente completo

**File:** `21 lezione stringhe studente completo.md`
**Tipo:** `.md`
**Dimensione:** 23.8 KB
**Ultima modifica:** 02/07/2026 09:24

---

# Lezione G13: Ordinamento e Stringhe — Operazioni su stringhe con `string.h`

**Durata totale:** 4 ore
**Teoria:** 3 ore | **Esercizi:** 1 ora
**Data:** _______________
**Ambiente:** CLion (JetBrains)
**Giornata:** G13 di 19 — Ore corso: 48/76

---

## PARTE 1 — TEORIA (3 ore)

### 1.1 Introduzione e motivazione

Nella vita reale i dati non sono solo numeri: nomi, cognomi, città, codici fiscali, email — tutto è testo. Un programma che sa gestire e ordinare stringhe è molto più vicino a un'applicazione reale.

Pensiamo a una rubrica telefonica: vogliamo visualizzare l'elenco in ordine alfabetico. Pensiamo a un motore di ricerca: deve trovare una parola all'interno di un testo. Pensiamo a un form di registrazione: deve verificare che la password abbia almeno 8 caratteri e contenga un numero.

Tutte queste operazioni richiedono la manipolazione di stringhe. In C le stringhe non sono un tipo primitivo: sono **array di `char`** terminati da un carattere speciale, il **terminatore nullo `'\0'`**. La libreria `string.h` fornisce le funzioni standard per operare su di esse in modo efficiente e sicuro.

---

### 1.2 Spiegazione dell'argomento

#### Le stringhe in C: struttura interna

Una stringa in C è un array di caratteri che termina obbligatoriamente con `'\0'` (valore ASCII 0):

```
char nome[10] = "Mario";

Indice:  [0]  [1]  [2]  [3]  [4]  [5]  [6]  [7]  [8]  [9]
Valore:  'M'  'a'  'r'  'i'  'o'  '\0'  ?    ?    ?    ?
                                    ↑
                              terminatore nullo
                              (OBBLIGATORIO)
```

Il terminatore `'\0'` è fondamentale: senza di esso le funzioni non sanno dove finisce la stringa e leggono dati in memoria casuali (comportamento indefinito).

---

#### Dichiarazione e inizializzazione

```c
// Metodo 1: dimensione esplicita con inizializzazione letterale
char s1[20] = "Ciao";
// Memoria: 'C' 'i' 'a' 'o' '\0' ? ? ? ? ? ...

// Metodo 2: dimensione automatica (conta i char + '\0')
char s2[] = "Mondo";
// Dimensione = 6 (5 caratteri + '\0')

// Metodo 3: array non inizializzato
char s3[50];
// Contenuto imprevedibile — va scritto prima di essere letto

// Lettura da tastiera
char s4[50];
scanf("%s", s4);         // legge fino al primo spazio
fgets(s4, 50, stdin);    // legge l'intera riga (inclusi spazi)
```

**Regola critica — NON si usa `=` per assegnare dopo la dichiarazione:**
```c
char s[20];
s = "Ciao";        // ❌ ERRORE di compilazione
s = s2;            // ❌ ERRORE di compilazione
strcpy(s, "Ciao"); // ✅ corretto
strcpy(s, s2);     // ✅ corretto
```

---

#### `strlen` — lunghezza della stringa

```c
#include <string.h>
size_t strlen(const char *s);
```

Conta i caratteri fino a `'\0'` (escluso). Restituisce un `size_t` (intero senza segno).

```
"Mario"   →   strlen = 5
"Ciao"    →   strlen = 4
""        →   strlen = 0   (stringa vuota: solo '\0')
```

```c
char nome[] = "Giovanni";
int len = strlen(nome);          // len = 8
char ultimo = nome[len - 1];     // ultimo = 'i'
```

**Uso frequente:** rimuovere `'\n'` da `fgets`:
```c
char s[100];
fgets(s, sizeof(s), stdin);
if (s[strlen(s) - 1] == '\n')
    s[strlen(s) - 1] = '\0';
```

---

#### `strcpy` — copia di stringa

```c
char *strcpy(char *dest, const char *src);
```

Copia `src` in `dest`, incluso il `'\0'` finale. Il buffer `dest` deve essere abbastanza grande.

```
src:  'C' 'i' 'a' 'o' '\0'
              ↓ copia tutto
dest: 'C' 'i' 'a' 'o' '\0'
```

```c
char originale[] = "Programmazione";
char copia[20];
strcpy(copia, originale);
printf("%s\n", copia);  // stampa: Programmazione
```

**Attenzione al buffer overflow:**
```c
char piccolo[5];
strcpy(piccolo, "Programmazione");  // ❌ PERICOLOSO: scrive fuori dall'array!
```

---

#### `strcat` — concatenazione

```c
char *strcat(char *dest, const char *src);
```

Aggiunge `src` alla fine di `dest`, sovrascrivendo il `'\0'` di `dest`.

```
Prima:   dest = "Ciao, \0"       src = "Mondo\0"
                       ↑ qui inizia la scrittura
Dopo:    dest = "Ciao, Mondo\0"
```

```c
char saluto[50] = "Ciao, ";
char nome[] = "Maria";
strcat(saluto, nome);
strcat(saluto, "!");
printf("%s\n", saluto);  // stampa: Ciao, Maria!
```

**Regola pratica:** la dimensione di `dest` deve essere ≥ `strlen(dest) + strlen(src) + 1`.

---

#### `strcmp` — confronto di stringhe

```c
int strcmp(const char *s1, const char *s2);
```

Confronta carattere per carattere secondo il codice ASCII. Restituisce:

```
┌─────────────────┬──────────────────────────────────────────┐
│ Valore ritorno  │ Significato                              │
├─────────────────┼──────────────────────────────────────────┤
│      0          │ s1 e s2 sono identiche                  │
│    < 0          │ s1 viene prima di s2 (ordine alfab.)    │
│    > 0          │ s1 viene dopo di s2 (ordine alfab.)     │
└─────────────────┴──────────────────────────────────────────┘
```

**Come funziona internamente:**
```
strcmp("Anna", "Carlo"):
  'A' (65) vs 'C' (67)  →  65 - 67 = -2  →  risultato negativo

strcmp("Luca", "Luca"):
  tutti i char uguali fino a '\0'  →  0

strcmp("Zara", "Zorro"):
  'Z'='Z', 'a'(97) vs 'o'(111)  →  risultato negativo
```

**Errore classico — non usare `==` per le stringhe:**
```c
char s1[] = "Ciao";
char s2[] = "Ciao";

if (s1 == s2)            // ❌ SBAGLIATO: confronta indirizzi di memoria!
    printf("Uguali\n");

if (strcmp(s1, s2) == 0) // ✅ CORRETTO: confronta il contenuto
    printf("Uguali\n");
```

---

#### `strchr` — ricerca di un carattere

```c
char *strchr(const char *s, int c);
```

Cerca la **prima occorrenza** del carattere `c` nella stringa `s`. Restituisce un puntatore al carattere trovato, oppure `NULL` se non esiste.

```c
char frase[] = "Programmazione";
char *ptr = strchr(frase, 'a');

if (ptr != NULL) {
    printf("Trovata 'a' alla posizione %ld\n", ptr - frase);
}
```

**Uso pratico — verificare la presenza di un carattere:**
```c
char email[] = "utente@esempio.it";
if (strchr(email, '@') != NULL)
    printf("Email valida (contiene @)\n");
else
    printf("Email non valida\n");
```

---

#### `strstr` — ricerca di una sottostringa

```c
char *strstr(const char *haystack, const char *needle);
```

Cerca la **prima occorrenza** della sottostringa `needle` all'interno di `haystack`. Restituisce un puntatore all'inizio della sottostringa trovata, oppure `NULL`.

```c
char testo[] = "Il linguaggio C è potente";
char *ptr = strstr(testo, "linguaggio");

if (ptr != NULL) {
    printf("Trovato a posizione %ld\n", ptr - testo);  // posizione 3
    printf("Da lì: %s\n", ptr);  // stampa: linguaggio C è potente
}
```

---

#### Ordinamento alfabetico con `strcmp` e Bubble Sort

Applicare l'ordinamento alfabetico richiede solo due cambiamenti rispetto al Bubble Sort numerico:

```
ORDINAMENTO NUMERICO          ORDINAMENTO ALFABETICO
─────────────────────         ──────────────────────────────────
Confronto:                    Confronto:
  if (a[i] > a[i+1])           if (strcmp(a[i], a[i+1]) > 0)

Scambio:                      Scambio:
  int temp = a[i];              char temp[MAX];
  a[i] = a[i+1];                strcpy(temp, a[i]);
  a[i+1] = temp;                strcpy(a[i], a[i+1]);
                                strcpy(a[i+1], temp);
```

**Schema del processo:**
```
Array iniziale:  ["Zara", "Anna", "Marco", "Giulia"]

Passata 1:
  strcmp("Zara","Anna") > 0  →  SCAMBIA  →  ["Anna", "Zara", "Marco", "Giulia"]
  strcmp("Zara","Marco") > 0 →  SCAMBIA  →  ["Anna", "Marco", "Zara", "Giulia"]
  strcmp("Zara","Giulia") > 0 → SCAMBIA  →  ["Anna", "Marco", "Giulia", "Zara"]

Passata 2:
  strcmp("Anna","Marco") < 0  →  no scambio
  strcmp("Marco","Giulia") > 0 → SCAMBIA →  ["Anna", "Giulia", "Marco", "Zara"]

Risultato: ["Anna", "Giulia", "Marco", "Zara"] ✅
```

---

#### Array bidimensionale di stringhe

```c
char nomi[5][30];
//        ↑   ↑
//   quante   lunghezza massima
//   stringhe  di ogni stringa (incluso '\0')
```

**Visualizzazione in memoria:**
```
nomi[0]: 'A' 'n' 'n' 'a' '\0' ? ? ...
nomi[1]: 'M' 'a' 'r' 'c' 'o' '\0' ? ...
nomi[2]: 'G' 'i' 'u' 'l' 'i' 'a' '\0' ...
```

Ogni riga è una stringa indipendente, accessibile con `nomi[i]`.

---

### 1.3 Esempi di codice commentati

#### Esempio 1 — Funzioni base di `string.h`

```c
#include <stdio.h>
#include <string.h>

int main() {
    char s1[50] = "Ciao";
    char s2[50] = "Mondo";
    char s3[50];

    printf("Lunghezza di '%s': %zu\n", s1, strlen(s1));

    strcpy(s3, s1);
    printf("s3 dopo strcpy: %s\n", s3);

    strcat(s1, ", ");
    strcat(s1, s2);
    strcat(s1, "!");
    printf("s1 dopo strcat: %s\n", s1);

    int cmp = strcmp("Anna", "Carla");
    if (cmp < 0)
        printf("Anna viene prima di Carla\n");
    else if (cmp > 0)
        printf("Anna viene dopo Carla\n");
    else
        printf("Stringhe uguali\n");

    return 0;
}
```

**Output atteso:**
```
Lunghezza di 'Ciao': 4
s3 dopo strcpy: Ciao
s1 dopo strcat: Ciao, Mondo!
Anna viene prima di Carla
```

---

#### Esempio 2 — Ricerca con `strchr` e `strstr`

```c
#include <stdio.h>
#include <string.h>

int main() {
    char frase[] = "Programmazione in C";
    char *ptr;

    ptr = strchr(frase, 'z');
    if (ptr != NULL)
        printf("'z' trovata alla posizione %ld\n", ptr - frase);
    else
        printf("'z' non trovata\n");

    if (strchr(frase, 'C') != NULL)
        printf("La frase contiene 'C'\n");

    ptr = strstr(frase, "in C");
    if (ptr != NULL)
        printf("Sottostringa 'in C' trovata: \"%s\"\n", ptr);

    ptr = strstr(frase, "Python");
    if (ptr == NULL)
        printf("'Python' non presente\n");

    return 0;
}
```

**Output atteso:**
```
'z' trovata alla posizione 8
La frase contiene 'C'
Sottostringa 'in C' trovata: "in C"
'Python' non presente
```

---

#### Esempio 3 — Ordinamento alfabetico con Bubble Sort

```c
#include <stdio.h>
#include <string.h>

#define N 5
#define MAX_LEN 30

void stampa_array(char arr[][MAX_LEN], int n) {
    int i;
    for (i = 0; i < n; i++)
        printf("  [%d] %s\n", i, arr[i]);
}

int main() {
    char nomi[N][MAX_LEN] = {"Zara", "Anna", "Marco", "Giulia", "Bruno"};
    char temp[MAX_LEN];
    int i, j;

    printf("Prima dell'ordinamento:\n");
    stampa_array(nomi, N);

    for (i = 0; i < N - 1; i++) {
        for (j = 0; j < N - 1 - i; j++) {
            if (strcmp(nomi[j], nomi[j+1]) > 0) {
                strcpy(temp,      nomi[j]);
                strcpy(nomi[j],   nomi[j+1]);
                strcpy(nomi[j+1], temp);
            }
        }
    }

    printf("\nDopo l'ordinamento:\n");
    stampa_array(nomi, N);

    return 0;
}
```

**Output atteso:**
```
Prima dell'ordinamento:
  [0] Zara
  [1] Anna
  [2] Marco
  [3] Giulia
  [4] Bruno

Dopo l'ordinamento:
  [0] Anna
  [1] Bruno
  [2] Giulia
  [3] Marco
  [4] Zara
```

---

#### Esempio 4 — Lettura da tastiera con `fgets`

```c
#include <stdio.h>
#include <string.h>

#define MAX_NOMI 4
#define MAX_LEN 50

int main() {
    char nomi[MAX_NOMI][MAX_LEN];
    char temp[MAX_LEN];
    int i, j;

    for (i = 0; i < MAX_NOMI; i++) {
        printf("Inserisci nome %d: ", i + 1);
        fgets(nomi[i], MAX_LEN, stdin);
        if (nomi[i][strlen(nomi[i]) - 1] == '\n')
            nomi[i][strlen(nomi[i]) - 1] = '\0';
    }

    for (i = 0; i < MAX_NOMI - 1; i++) {
        for (j = 0; j < MAX_NOMI - 1 - i; j++) {
            if (strcmp(nomi[j], nomi[j+1]) > 0) {
                strcpy(temp,      nomi[j]);
                strcpy(nomi[j],   nomi[j+1]);
                strcpy(nomi[j+1], temp);
            }
        }
    }

    printf("\nNomi in ordine alfabetico:\n");
    for (i = 0; i < MAX_NOMI; i++)
        printf("  %s\n", nomi[i]);

    return 0;
}
```

**Output atteso (esempio):**
```
Inserisci nome 1: Zara
Inserisci nome 2: Anna
Inserisci nome 3: Marco
Inserisci nome 4: Bruno

Nomi in ordine alfabetico:
  Anna
  Bruno
  Marco
  Zara
```

---

### 1.4 Riepilogo visivo

```
┌──────────────────────────────────────────────────────────────────────┐
│                    FUNZIONI DI string.h                              │
├──────────────────┬─────────────────┬───────────────────────────────  │
│ FUNZIONE         │ RESTITUISCE     │ USO TIPICO                      │
├──────────────────┼─────────────────┼───────────────────────────────  │
│ strlen(s)        │ size_t          │ Lunghezza, accesso ultimo char  │
│ strcpy(dst, src) │ char* (dst)     │ Copia / assegnazione            │
│ strcat(dst, src) │ char* (dst)     │ Concatenazione                  │
│ strcmp(s1, s2)   │ int <0, 0, >0   │ Confronto / ordinamento         │
│ strchr(s, c)     │ char* o NULL    │ Presenza/posizione di un char   │
│ strstr(s, sub)   │ char* o NULL    │ Presenza/posizione sottostringa │
└──────────────────┴─────────────────┴───────────────────────────────  ┘

BUBBLE SORT STRINGHE
─────────────────────────────────────────────
  for (i = 0; i < n-1; i++)
    for (j = 0; j < n-1-i; j++)
      if (strcmp(nomi[j], nomi[j+1]) > 0) {
        strcpy(temp,       nomi[j]);
        strcpy(nomi[j],    nomi[j+1]);
        strcpy(nomi[j+1],  temp);
      }

ERRORI FREQUENTI
─────────────────────────────────────────────
  ❌  s1 == s2           ✅  strcmp(s1, s2) == 0
  ❌  s1 = "testo"       ✅  strcpy(s1, "testo")
  ❌  s1 = s2            ✅  strcpy(s1, s2)
  ❌  s1 + s2            ✅  strcat(s1, s2)
  ❌  temp = nomi[i]     ✅  strcpy(temp, nomi[i])
```

---

### 1.5 Domande di verifica orale

**D1:** Cos'è il terminatore nullo `'\0'`? Perché è indispensabile?

<details>
<summary><b>💡 RISPOSTA</b></summary>

È il carattere con valore ASCII 0 che marca la fine di ogni stringa in C. Tutte le funzioni di `string.h` si basano su di esso per sapere dove si ferma la stringa: senza `'\0'`, `strlen`, `strcpy`, `printf` con `%s` continuerebbero a leggere oltre i limiti della stringa, con risultati imprevedibili.

</details>

---

**D2:** Perché non si può usare `==` per confrontare due stringhe? Cosa confronta realmente?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Il nome di un array in C è un puntatore al suo primo elemento. Usare `==` confronta quindi gli *indirizzi di memoria* delle due stringhe, non il loro contenuto. Due array diversi hanno sempre indirizzi diversi, anche se contengono gli stessi caratteri. Si deve usare `strcmp()` che confronta carattere per carattere.

</details>

---

**D3:** `strcmp("Banana", "Ananas")` restituisce un valore positivo o negativo? Perché?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Positivo. `strcmp` confronta il primo carattere diverso: `'B'` (ASCII 66) vs `'A'` (ASCII 65). Poiché `'B' > 'A'`, il risultato è positivo, indicando che "Banana" viene *dopo* "Ananas" in ordine alfabetico.

</details>

---

**D4:** Ho un array `char nomi[10][50]`. Quanta memoria totale occupa? E quante stringhe può contenere?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Occupa `10 × 50 = 500 byte`. Può contenere al massimo 10 stringhe, ciascuna lunga al massimo 49 caratteri (il cinquantesimo è riservato al `'\0'`).

</details>

---

**D5:** Perché nel Bubble Sort per stringhe non posso scrivere `temp = nomi[i]`?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Perché `nomi[i]` è un array e in C non si possono assegnare array con `=`. L'operatore `=` copierebbe solo il puntatore (l'indirizzo), non il contenuto. È necessario usare `strcpy(temp, nomi[i])` per copiare effettivamente tutti i caratteri.

</details>

---

**D6:** Cosa restituisce `strchr("Hello", 'l')`? E se il carattere non c'è?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Restituisce un puntatore alla *prima* occorrenza di `'l'` nella stringa, che si trova all'indice 2. Se il carattere non fosse presente, restituirebbe `NULL`. Il valore `NULL` va sempre controllato prima di usare il puntatore restituito.

</details>

---

**D7:** `fgets` include il carattere `'\n'` nella stringa letta? Come si rimuove?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Sì, `fgets` include il `'\n'` se c'è spazio nel buffer. Lo si rimuove controllando l'ultimo carattere: `if (s[strlen(s)-1] == '\n') s[strlen(s)-1] = '\0';` — si sovrascrive il `'\n'` con il terminatore nullo.

</details>

---

## PARTE 2 — ESERCIZI (1 ora)

---

### 🟢 Esercizio 1 — Analisi di una stringa (Base)

**Testo:** Scrivi un programma che legge una stringa dall'utente (max 100 caratteri) e stampa:
- La lunghezza della stringa
- Il primo e l'ultimo carattere
- Se contiene la lettera `'a'` (maiuscola o minuscola)

**Esempio input/output:**
```
Inserisci una stringa: Programmazione
Lunghezza: 14
Primo carattere: P
Ultimo carattere: e
Contiene 'a': SI
```

**💡 Hint:**
1. Usa `fgets` per leggere e rimuovi il `'\n'`
2. `strlen(s)` dà la lunghezza; l'ultimo char è `s[strlen(s)-1]`
3. `strchr(s, 'a') != NULL` controlla la presenza

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <string.h>

int main() {
    char s[101];
    int len;

    printf("Inserisci una stringa: ");
    fgets(s, sizeof(s), stdin);
    if (s[strlen(s)-1] == '\n')
        s[strlen(s)-1] = '\0';

    len = strlen(s);
    printf("Lunghezza: %d\n", len);
    printf("Primo carattere: %c\n", s[0]);
    printf("Ultimo carattere: %c\n", s[len-1]);

    if (strchr(s, 'a') != NULL || strchr(s, 'A') != NULL)
        printf("Contiene 'a': SI\n");
    else
        printf("Contiene 'a': NO\n");

    return 0;
}
```

</details>

---

### 🟡 Esercizio 2 — Ordinamento alfabetico di nomi (Intermedio)

**Testo:** Il programma legge N nomi dall'utente (max 20, max 50 caratteri ciascuno), li ordina in ordine alfabetico con il Bubble Sort e li stampa ordinati.

**Esempio input/output:**
```
Quanti nomi? 4
Nome 1: Zara
Nome 2: Anna
Nome 3: Marco
Nome 4: Giulia

Nomi ordinati:
  Anna
  Giulia
  Marco
  Zara
```

**💡 Hint:**
1. Dichiara `char nomi[20][51]` e `char temp[51]`
2. Dopo ogni `fgets`, rimuovi il `'\n'`
3. Confronto: `strcmp(nomi[j], nomi[j+1]) > 0`
4. Scambio: tre `strcpy` con `temp`

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <string.h>

#define MAX_NOMI 20
#define MAX_LEN  51

int main() {
    char nomi[MAX_NOMI][MAX_LEN];
    char temp[MAX_LEN];
    int n, i, j;

    printf("Quanti nomi? ");
    scanf("%d", &n);
    getchar();

    if (n > MAX_NOMI) n = MAX_NOMI;

    for (i = 0; i < n; i++) {
        printf("Nome %d: ", i + 1);
        fgets(nomi[i], MAX_LEN, stdin);
        if (nomi[i][strlen(nomi[i])-1] == '\n')
            nomi[i][strlen(nomi[i])-1] = '\0';
    }

    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - 1 - i; j++) {
            if (strcmp(nomi[j], nomi[j+1]) > 0) {
                strcpy(temp,       nomi[j]);
                strcpy(nomi[j],    nomi[j+1]);
                strcpy(nomi[j+1],  temp);
            }
        }
    }

    printf("\nNomi ordinati:\n");
    for (i = 0; i < n; i++)
        printf("  %s\n", nomi[i]);

    return 0;
}
```

</details>

---

### 🔴 Esercizio 3 — Mini rubrica con ricerca (Avanzato)

**Testo:** Il programma gestisce una mini rubrica di massimo 10 contatti (nome max 30 char, telefono max 15 char). Deve:
1. Leggere N contatti dall'utente
2. Ordinarli alfabeticamente per nome (ricorda: scambia anche i telefoni!)
3. Stampare la rubrica ordinata
4. Chiedere un nome da cercare e stampare il risultato (ricerca lineare con `strcmp`)

**Esempio input/output:**
```
Quanti contatti? 3
Nome: Rossi Luca
Tel:  3331234567
Nome: Bianchi Mario
Tel:  3337654321
Nome: Verdi Anna
Tel:  3339876543

Rubrica ordinata:
  Bianchi Mario       3337654321
  Rossi Luca          3331234567
  Verdi Anna          3339876543

Cerca: Rossi Luca
Trovato → Rossi Luca: 3331234567
```

**💡 Hint:**
1. Usa due array paralleli: `char nomi[10][31]` e `char tel[10][16]`
2. Quando scambi due nomi nel Bubble Sort, scambia subito anche i telefoni corrispondenti
3. Per la ricerca, scorri l'array con `strcmp(nomi[i], cerca) == 0`
4. Usa una variabile `trovato = 0` e impostala a `1` quando trovi il contatto

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <string.h>

#define MAX_C   10
#define MAX_N   31
#define MAX_T   16

int main() {
    char nomi[MAX_C][MAX_N];
    char tel[MAX_C][MAX_T];
    char tempN[MAX_N], tempT[MAX_T];
    char cerca[MAX_N];
    int n, i, j, trovato;

    printf("Quanti contatti? ");
    scanf("%d", &n);
    getchar();
    if (n > MAX_C) n = MAX_C;

    for (i = 0; i < n; i++) {
        printf("Nome: ");
        fgets(nomi[i], MAX_N, stdin);
        if (nomi[i][strlen(nomi[i])-1] == '\n') nomi[i][strlen(nomi[i])-1] = '\0';

        printf("Tel:  ");
        fgets(tel[i], MAX_T, stdin);
        if (tel[i][strlen(tel[i])-1] == '\n') tel[i][strlen(tel[i])-1] = '\0';
    }

    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - 1 - i; j++) {
            if (strcmp(nomi[j], nomi[j+1]) > 0) {
                strcpy(tempN,    nomi[j]);
                strcpy(nomi[j],  nomi[j+1]);
                strcpy(nomi[j+1], tempN);

                strcpy(tempT,   tel[j]);
                strcpy(tel[j],  tel[j+1]);
                strcpy(tel[j+1], tempT);
            }
        }
    }

    printf("\nRubrica ordinata:\n");
    for (i = 0; i < n; i++)
        printf("  %-20s  %s\n", nomi[i], tel[i]);

    printf("\nCerca: ");
    fgets(cerca, MAX_N, stdin);
    if (cerca[strlen(cerca)-1] == '\n') cerca[strlen(cerca)-1] = '\0';

    trovato = 0;
    for (i = 0; i < n; i++) {
        if (strcmp(nomi[i], cerca) == 0) {
            printf("Trovato → %s: %s\n", nomi[i], tel[i]);
            trovato = 1;
            break;
        }
    }
    if (!trovato)
        printf("Contatto \"%s\" non trovato.\n", cerca);

    return 0;
}
```

</details>

---

## 🎯 Recap finale (5 min)

- **Le stringhe in C sono array di `char` terminati da `'\0'`** — il terminatore è obbligatorio e viene gestito automaticamente da tutte le funzioni di `string.h`.
- **`strcmp` è l'unico modo corretto per confrontare stringhe**: restituisce `0` se uguali, valore negativo se la prima precede la seconda, positivo se la segue — identica logica usata nel Bubble Sort.
- **Ordinare stringhe = Bubble Sort già noto**, con due soli cambiamenti: `strcmp` al posto di `>` per il confronto, e tre `strcpy` al posto dell'assegnazione diretta per lo scambio.
- **`strchr` e `strstr` cercano** rispettivamente un carattere e una sottostringa — restituiscono sempre `NULL` se non trovano nulla, e questo va sempre controllato prima di usare il puntatore.
- ⚠️ **Errore comune da evitare:** usare `s1 = s2` per copiare o `s1 == s2` per confrontare — entrambi operano sugli indirizzi, non sul contenuto. Usare sempre `strcpy` e `strcmp`.
- 📌 **Prossima lezione (G14):** introduzione alle `struct` — come raggruppare dati di tipo diverso (nome, età, stipendio) in un'unica variabile composita, evitando gli array paralleli usati oggi.



---

# 22 lezione struct studente completo

**File:** `22 lezione struct studente completo.md`
**Tipo:** `.md`
**Dimensione:** 30.5 KB
**Ultima modifica:** 02/07/2026 09:24

---

# Lezione G14: Strutture (`struct`) — Definizione, accesso, array di struct

**Durata totale:** 4 ore
**Teoria:** 3 ore | **Esercizi:** 1 ora
**Data:** _______________
**Ambiente:** CLion (JetBrains)
**Giornata:** G14 di 19 — Ore corso: 52/76

---

## PARTE 1 — TEORIA (3 ore)

### 1.1 Introduzione e motivazione

Nella lezione precedente (G13) abbiamo gestito una rubrica con **due array paralleli**: uno per i nomi e uno per i telefoni. Questo approccio funziona, ma ha un difetto importante: i dati che appartengono allo stesso contatto sono **sparpagliati** in strutture separate. Basta un errore di indice e nome e telefono non corrispondono più.

```
APPROCCIO CON ARRAY PARALLELI (G13):

nomi[0]  = "Bianchi Mario"   tel[0] = "3337654321"
nomi[1]  = "Rossi Luca"      tel[1] = "3331234567"
nomi[2]  = "Verdi Anna"      tel[2] = "3339876543"

Problema: cosa succede se ordino solo nomi[] e dimentico tel[]?
→ I dati si disallineano e la rubrica è corrotta. ❌
```

Le **struct** risolvono questo problema raggruppando in un'unica variabile tutti i dati che descrivono la stessa entità del mondo reale. Un contatto ha nome E telefono — perché tenerli separati?

```
APPROCCIO CON STRUCT:

contatti[0] → { nome: "Bianchi Mario", tel: "3337654321" }
contatti[1] → { nome: "Rossi Luca",    tel: "3331234567" }
contatti[2] → { nome: "Verdi Anna",    tel: "3339876543" }

Nome e telefono viaggiano sempre insieme. ✅
```

Le struct sono il primo passo verso la **programmazione orientata agli oggetti**: raggruppare dati correlati in un tipo personalizzato è esattamente il concetto alla base delle classi in Java e C++.

---

### 1.2 Spiegazione dell'argomento

#### Definizione di una struct

Una `struct` è un tipo di dato **composto**, definito dal programmatore, che raggruppa variabili di tipo anche diverso chiamate **campi** (o *membri*).

**Sintassi:**
```c
struct NomeStruct {
    tipo1 campo1;
    tipo2 campo2;
    /* ... altri campi ... */
};
```

**Esempio concreto — un punto nel piano cartesiano:**
```c
struct Punto {
    float x;
    float y;
};
```

**Esempio — uno studente:**
```c
struct Studente {
    char nome[50];
    char cognome[50];
    int matricola;
    float media;
};
```

> **Importante:** la definizione di una struct NON alloca memoria — è solo la descrizione di come sarà fatto il tipo. La memoria viene allocata quando si dichiara una **variabile** di quel tipo.

---

#### Dichiarazione di variabili struct

Dopo aver definito la struct, si dichiarano le variabili:

```c
struct Studente s1;           // variabile singola
struct Studente s2, s3;       // più variabili

// Inizializzazione alla dichiarazione (in ordine dei campi)
struct Studente s4 = {"Mario", "Rossi", 12345, 27.5};
```

**Visualizzazione in memoria:**
```
struct Studente s1:
┌────────────────────────────────────────────────┐
│ nome[50]  │ cognome[50] │ matricola │  media   │
│ "Mario"   │ "Rossi"     │   12345   │  27.5    │
└────────────────────────────────────────────────┘
  50 byte      50 byte      4 byte     4 byte
                        Totale ≈ 108 byte
```

Tutti i campi della stessa variabile struct sono **contigui in memoria** e si spostano sempre insieme.

---

#### Accesso ai campi: operatore `.`

Per leggere o scrivere un campo di una struct si usa l'**operatore punto** `.`:

```c
struct Studente s;

/* Scrittura dei campi */
strcpy(s.nome, "Luigi");
strcpy(s.cognome, "Bianchi");
s.matricola = 54321;
s.media = 29.0;

/* Lettura dei campi */
printf("Nome: %s %s\n", s.nome, s.cognome);
printf("Matricola: %d\n", s.matricola);
printf("Media: %.1f\n", s.media);
```

**Schema dell'operatore `.`:**
```
  s  .  nome
  ↑  ↑    ↑
  │  │    └─ campo a cui accedere
  │  └─ operatore punto
  └─ variabile struct
```

---

#### `typedef` — semplificare il nome del tipo

Scrivere `struct Studente` ogni volta è verboso. Il costrutto `typedef` permette di creare un **alias** più breve:

```c
/* Senza typedef */
struct Studente s1;
struct Studente s2;

/* Con typedef */
typedef struct {
    char nome[50];
    char cognome[50];
    int matricola;
    float media;
} Studente;

/* Ora si può scrivere semplicemente: */
Studente s1;
Studente s2;
```

> **Convenzione:** i nomi dei tipi definiti con `typedef` si scrivono con la **prima lettera maiuscola** (es. `Studente`, `Punto`, `Prodotto`).

---

#### Assegnazione tra struct

A differenza degli array, due variabili struct dello stesso tipo si possono assegnare direttamente con `=`: il compilatore copia tutti i campi automaticamente.

```c
Studente a = {"Anna", "Verdi", 11111, 28.5};
Studente b;

b = a;   // copia TUTTI i campi di a in b ✅

/* Equivale a: */
strcpy(b.nome, a.nome);
strcpy(b.cognome, a.cognome);
b.matricola = a.matricola;
b.media = a.media;
```

Questo rende lo **scambio tra struct** molto più semplice:
```c
Studente temp = a;
a = b;
b = temp;
/* Nessuna strcpy necessaria! */
```

---

#### Array di struct

La combinazione più potente: un **array di struct** permette di gestire collezioni di entità complesse in modo pulito e ordinato.

```c
Studente classe[30];   /* array di 30 studenti */
```

**Visualizzazione in memoria:**
```
classe[0]: [ nome | cognome | matricola | media ]
classe[1]: [ nome | cognome | matricola | media ]
classe[2]: [ nome | cognome | matricola | media ]
...
classe[29]:[ nome | cognome | matricola | media ]
```

**Accesso ai campi dell'i-esimo elemento:**
```c
/* Sintassi: array[indice].campo */
strcpy(classe[0].nome, "Mario");
classe[0].media = 27.0;

printf("%s — media: %.1f\n", classe[i].nome, classe[i].media);
```

---

#### Lettura di un array di struct da tastiera

```c
Studente classe[30];
int n;

printf("Quanti studenti? ");
scanf("%d", &n);
getchar();   /* consuma il '\n' residuo */

for (int i = 0; i < n; i++) {
    printf("--- Studente %d ---\n", i + 1);

    printf("Nome: ");
    fgets(classe[i].nome, sizeof(classe[i].nome), stdin);
    if (classe[i].nome[strlen(classe[i].nome)-1] == '\n')
        classe[i].nome[strlen(classe[i].nome)-1] = '\0';

    printf("Cognome: ");
    fgets(classe[i].cognome, sizeof(classe[i].cognome), stdin);
    if (classe[i].cognome[strlen(classe[i].cognome)-1] == '\n')
        classe[i].cognome[strlen(classe[i].cognome)-1] = '\0';

    printf("Matricola: ");
    scanf("%d", &classe[i].matricola);

    printf("Media: ");
    scanf("%f", &classe[i].media);
    getchar();
}
```

---

#### Ordinamento di un array di struct

Per ordinare un array di struct si usa il Bubble Sort già noto. Poiché `=` copia tutti i campi automaticamente, lo **scambio è semplicissimo**:

```c
/* Ordinamento per media crescente */
for (int i = 0; i < n - 1; i++) {
    for (int j = 0; j < n - 1 - i; j++) {
        if (classe[j].media > classe[j+1].media) {
            Studente temp = classe[j];       /* copia intera struct */
            classe[j]     = classe[j+1];
            classe[j+1]   = temp;
        }
    }
}

/* Ordinamento per cognome (alfabetico) */
for (int i = 0; i < n - 1; i++) {
    for (int j = 0; j < n - 1 - i; j++) {
        if (strcmp(classe[j].cognome, classe[j+1].cognome) > 0) {
            Studente temp = classe[j];
            classe[j]     = classe[j+1];
            classe[j+1]   = temp;
        }
    }
}
```

> **Confronto con G13:** prima servivano due array paralleli (nomi + telefoni) e due serie di `strcpy` per lo scambio. Con le struct, lo scambio di **tutti i dati** di un contatto si fa con **tre semplici assegnazioni** `=`.

---

#### Struct come parametro di funzione

Le struct si possono passare alle funzioni **per valore** (viene passata una copia):

```c
void stampa_studente(Studente s) {
    printf("%-10s %-10s  matr: %d  media: %.1f\n",
           s.nome, s.cognome, s.matricola, s.media);
}

/* Chiamata */
stampa_studente(classe[i]);
```

---

### 1.3 Esempi di codice commentati

#### Esempio 1 — Prima struct: definizione, accesso e stampa

```c
#include <stdio.h>
#include <string.h>

typedef struct {
    char nome[30];
    int eta;
    float altezza;
} Persona;

int main() {
    Persona p1;
    Persona p2 = {"Maria", 25, 1.68};

    strcpy(p1.nome, "Luca");
    p1.eta     = 30;
    p1.altezza = 1.82;

    printf("Persona 1: %s, %d anni, %.2f m\n",
           p1.nome, p1.eta, p1.altezza);
    printf("Persona 2: %s, %d anni, %.2f m\n",
           p2.nome, p2.eta, p2.altezza);

    Persona p3 = p1;   /* copia completa */
    p3.eta = 31;       /* modifica solo p3 */

    printf("Persona 3 (copia di p1): %s, %d anni\n",
           p3.nome, p3.eta);
    printf("p1 invariata: %s, %d anni\n",
           p1.nome, p1.eta);

    return 0;
}
```

**Output atteso:**
```
Persona 1: Luca, 30 anni, 1.82 m
Persona 2: Maria, 25 anni, 1.68 m
Persona 3 (copia di p1): Luca, 31 anni
p1 invariata: Luca, 30 anni
```

---

#### Esempio 2 — Array di struct: rubrica migliorata

```c
#include <stdio.h>
#include <string.h>

#define MAX 5

typedef struct {
    char nome[30];
    char telefono[16];
} Contatto;

void stampa_rubrica(Contatto rubrica[], int n) {
    printf("\n%-25s %-15s\n", "NOME", "TELEFONO");
    printf("%-25s %-15s\n", "─────────────────────────", "───────────────");
    for (int i = 0; i < n; i++)
        printf("%-25s %-15s\n", rubrica[i].nome, rubrica[i].telefono);
}

int main() {
    Contatto rubrica[MAX] = {
        {"Bianchi Mario", "3337654321"},
        {"Rossi Luca",    "3331234567"},
        {"Verdi Anna",    "3339876543"},
        {"Conti Sara",    "3335551234"},
        {"Neri Paolo",    "3338889876"}
    };

    printf("Rubrica originale:");
    stampa_rubrica(rubrica, MAX);

    for (int i = 0; i < MAX - 1; i++) {
        for (int j = 0; j < MAX - 1 - i; j++) {
            if (strcmp(rubrica[j].nome, rubrica[j+1].nome) > 0) {
                Contatto temp = rubrica[j];
                rubrica[j]    = rubrica[j+1];
                rubrica[j+1]  = temp;
            }
        }
    }

    printf("\nRubrica ordinata:");
    stampa_rubrica(rubrica, MAX);

    return 0;
}
```

**Output atteso:**
```
Rubrica originale:
NOME                      TELEFONO
───────────────────────── ───────────────
Bianchi Mario             3337654321
Rossi Luca                3331234567
Verdi Anna                3339876543
Conti Sara                3335551234
Neri Paolo                3338889876

Rubrica ordinata:
NOME                      TELEFONO
───────────────────────── ───────────────
Bianchi Mario             3337654321
Conti Sara                3335551234
Neri Paolo                3338889876
Rossi Luca                3331234567
Verdi Anna                3339876543
```

---

#### Esempio 3 — Array di struct con input da tastiera e ricerca

```c
#include <stdio.h>
#include <string.h>

#define MAX_PROD 20

typedef struct {
    char descrizione[50];
    float prezzo;
    int quantita;
} Prodotto;

void stampa_prodotto(Prodotto p) {
    printf("  %-30s  €%7.2f  qty: %d\n",
           p.descrizione, p.prezzo, p.quantita);
}

int main() {
    Prodotto magazzino[MAX_PROD];
    int n, i;

    printf("Quanti prodotti? ");
    scanf("%d", &n);
    getchar();
    if (n > MAX_PROD) n = MAX_PROD;

    for (i = 0; i < n; i++) {
        printf("\n--- Prodotto %d ---\n", i + 1);
        printf("Descrizione: ");
        fgets(magazzino[i].descrizione, sizeof(magazzino[i].descrizione), stdin);
        if (magazzino[i].descrizione[strlen(magazzino[i].descrizione)-1] == '\n')
            magazzino[i].descrizione[strlen(magazzino[i].descrizione)-1] = '\0';

        printf("Prezzo: ");
        scanf("%f", &magazzino[i].prezzo);
        printf("Quantita': ");
        scanf("%d", &magazzino[i].quantita);
        getchar();
    }

    /* Ordina per prezzo crescente */
    for (i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (magazzino[j].prezzo > magazzino[j+1].prezzo) {
                Prodotto temp  = magazzino[j];
                magazzino[j]   = magazzino[j+1];
                magazzino[j+1] = temp;
            }
        }
    }

    printf("\n=== Prodotti ordinati per prezzo ===\n");
    for (i = 0; i < n; i++)
        stampa_prodotto(magazzino[i]);

    int idx_min = 0;
    for (i = 1; i < n; i++)
        if (magazzino[i].quantita < magazzino[idx_min].quantita)
            idx_min = i;

    printf("\nProdotto con scorte minime:\n");
    stampa_prodotto(magazzino[idx_min]);

    return 0;
}
```

**Output atteso (esempio):**
```
=== Prodotti ordinati per prezzo ===
  Mouse wireless                   € 22.50  qty: 8
  Tastiera USB                     € 45.90  qty: 12
  Monitor 24"                      €189.00  qty: 3

Prodotto con scorte minime:
  Monitor 24"                      €189.00  qty: 3
```

---

#### Esempio 4 — Struct come parametro di funzione

```c
#include <stdio.h>
#include <string.h>

typedef struct {
    char nome[50];
    int voti[5];
    int num_voti;
} Studente;

float calcola_media(Studente s) {
    float somma = 0;
    for (int i = 0; i < s.num_voti; i++)
        somma += s.voti[i];
    return (s.num_voti > 0) ? somma / s.num_voti : 0;
}

void stampa_studente(Studente s) {
    printf("%-20s  voti: ", s.nome);
    for (int i = 0; i < s.num_voti; i++)
        printf("%d ", s.voti[i]);
    printf(" → media: %.1f\n", calcola_media(s));
}

int main() {
    Studente classe[3] = {
        {"Anna Rossi",   {28, 30, 27, 29, 30}, 5},
        {"Luca Bianchi", {22, 25, 24},          3},
        {"Sara Conti",   {30, 28, 29, 27},      4}
    };

    printf("=== Registro della classe ===\n");
    for (int i = 0; i < 3; i++)
        stampa_studente(classe[i]);

    int idx_max = 0;
    for (int i = 1; i < 3; i++)
        if (calcola_media(classe[i]) > calcola_media(classe[idx_max]))
            idx_max = i;

    printf("\nMiglior studente: %s (media %.1f)\n",
           classe[idx_max].nome, calcola_media(classe[idx_max]));

    return 0;
}
```

**Output atteso:**
```
=== Registro della classe ===
Anna Rossi            voti: 28 30 27 29 30  → media: 28.8
Luca Bianchi          voti: 22 25 24        → media: 23.7
Sara Conti            voti: 30 28 29 27     → media: 28.5

Miglior studente: Anna Rossi (media 28.8)
```

---

### 1.4 Riepilogo visivo

```
┌──────────────────────────────────────────────────────────────────┐
│                   SINTASSI DELLE STRUCT                          │
├──────────────────────────────────────────────────────────────────┤
│  DEFINIZIONE (con typedef):                                      │
│  typedef struct {                                                │
│      tipo1 campo1;                                               │
│      tipo2 campo2;                                               │
│  } NomeTipo;                                                     │
│                                                                  │
│  DICHIARAZIONE:                                                  │
│  NomeTipo var;                                                   │
│  NomeTipo var = {val1, val2};   /* inizializzazione */          │
│  NomeTipo arr[N];               /* array di struct */            │
│                                                                  │
│  ACCESSO:                                                        │
│  var.campo        /* variabile singola */                        │
│  arr[i].campo     /* elemento di array */                        │
│                                                                  │
│  ASSEGNAZIONE:                                                   │
│  var2 = var1;     /* copia tutti i campi ✅ */                   │
│                                                                  │
│  SCAMBIO (Bubble Sort):                                          │
│  NomeTipo temp = arr[j];                                         │
│  arr[j]        = arr[j+1];                                       │
│  arr[j+1]      = temp;                                           │
└──────────────────────────────────────────────────────────────────┘

CONFRONTO: ARRAY PARALLELI vs STRUCT
──────────────────────────────────────────────────────────────────
  PRIMA (G13 — array paralleli):     ORA (G14 — struct):
  char nomi[10][30];                 typedef struct {
  char tel[10][16];                      char nome[30];
                                         char tel[16];
  Scambio: 6 strcpy!                 } Contatto;
  strcpy(tempN, nomi[j]);            Contatto rubrica[10];
  strcpy(nomi[j], nomi[j+1]);
  strcpy(nomi[j+1], tempN);          Scambio: 3 righe!
  strcpy(tempT, tel[j]);             Contatto t = rubrica[j];
  strcpy(tel[j], tel[j+1]);          rubrica[j] = rubrica[j+1];
  strcpy(tel[j+1], tempT);           rubrica[j+1] = t;

ERRORI FREQUENTI
──────────────────────────────────────────────────────────────────
  ❌  s.nome = "Mario"       ✅  strcpy(s.nome, "Mario")
  ❌  s1 == s2               ✅  confronta campo per campo
  ❌  printf("%s", s)        ✅  printf("%s", s.nome)
  ✅  s2 = s1  (copia intera struct — funziona!)
```

---

### 1.5 Domande di verifica orale

**D1:** Cos'è una `struct` in C? Cosa si intende per "campo"?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Una `struct` è un tipo di dato composto definito dal programmatore che raggruppa variabili di tipo anche diverso in un'unica entità. Le singole variabili che la compongono si chiamano **campi** (o membri). Esempio: una struct `Studente` può avere i campi `nome` (stringa), `matricola` (intero) e `media` (float).

</details>

---

**D2:** Qual è la differenza tra la *definizione* di una struct e la *dichiarazione* di una variabile struct?

<details>
<summary><b>💡 RISPOSTA</b></summary>

La **definizione** (`typedef struct { ... } Nome;`) descrive al compilatore come è fatto il tipo — non alloca memoria. La **dichiarazione** (`Nome var;`) crea una variabile di quel tipo e alloca la memoria necessaria. È la stessa distinzione che esiste tra il progetto di una casa (definizione) e la costruzione effettiva (dichiarazione).

</details>

---

**D3:** Come si accede al campo `prezzo` della terza struct in un array `Prodotto magazzino[10]`?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Con `magazzino[2].prezzo`. Si usa la notazione `array[indice].campo`: prima l'indice per selezionare l'elemento dell'array, poi il punto per accedere al campo desiderato.

</details>

---

**D4:** Perché l'assegnazione `s2 = s1` funziona per le struct ma NON per gli array?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Per le struct, il compilatore sa esattamente quanta memoria occupa il tipo e genera automaticamente il codice per copiare campo per campo. Per gli array, il nome è un puntatore al primo elemento e `=` copierebbe solo l'indirizzo, non il contenuto. Questa è una delle differenze fondamentali tra struct e array in C.

</details>

---

**D5:** Nel Bubble Sort applicato a un array di struct, come si esegue lo scambio?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Grazie all'assegnazione diretta tra struct, lo scambio si riduce a tre righe con una variabile temporanea dello stesso tipo:
```c
NomeTipo temp = arr[j];
arr[j]        = arr[j+1];
arr[j+1]      = temp;
```
Questo copia automaticamente **tutti i campi** in una sola operazione — molto più semplice dei 6 `strcpy` necessari con gli array paralleli.

</details>

---

**D6:** Ho una struct `Studente` con un campo `char nome[50]`. Perché devo usare `strcpy(s.nome, "Mario")` e non `s.nome = "Mario"`?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Il campo `nome` è un array di `char`. Come per tutti gli array in C, non si può assegnare direttamente con `=` (copierebbe solo il puntatore). Si deve usare `strcpy` per copiare i caratteri uno ad uno. Questa regola vale per tutti i campi di tipo array all'interno di una struct, mentre per campi di tipo semplice (`int`, `float`, `char`) si usa normalmente `=`.

</details>

---

**D7:** Cosa significa `typedef` applicato a una struct? Quale vantaggio offre?

<details>
<summary><b>💡 RISPOSTA</b></summary>

`typedef` crea un **alias** — un nome alternativo per un tipo già esistente. Applicato a una struct, permette di evitare di scrivere la parola chiave `struct` ogni volta: invece di `struct Studente s1;` si scrive semplicemente `Studente s1;`. Il codice diventa più leggibile e manutenibile, e il nome del tipo si comporta esattamente come i tipi primitivi (`int`, `float`, ecc.).

</details>

---

## PARTE 2 — ESERCIZI (1 ora)

---

### 🟢 Esercizio 1 — Struct Libro (Base)

**Testo:** Definisci una struct `Libro` con i campi: `titolo` (stringa, max 60 caratteri), `autore` (stringa, max 40 caratteri), `anno` (intero), `prezzo` (float). Scrivi un programma che:
1. Dichiara e inizializza manualmente nel codice 3 libri
2. Li stampa in formato tabellare

**Esempio input/output:**
```
=== Catalogo Libri ===
TITOLO                          AUTORE                   ANNO   PREZZO
Il nome della rosa              Umberto Eco              1980   €12.50
1984                            George Orwell            1949    €9.90
Il Signore degli Anelli         J.R.R. Tolkien           1954   €24.00
```

**💡 Hint:**
1. Usa `typedef struct { ... } Libro;`
2. Inizializza con `Libro libri[3] = { {"titolo", "autore", anno, prezzo}, ... };`
3. Per la stampa allineata usa `%-30s` per le stringhe e `%6.2f` per i float

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

typedef struct {
    char titolo[61];
    char autore[41];
    int  anno;
    float prezzo;
} Libro;

void stampa_libro(Libro l) {
    printf("%-32s %-25s %4d  €%6.2f\n",
           l.titolo, l.autore, l.anno, l.prezzo);
}

int main() {
    Libro libri[3] = {
        {"Il nome della rosa",        "Umberto Eco",      1980, 12.50},
        {"1984",                      "George Orwell",    1949,  9.90},
        {"Il Signore degli Anelli",   "J.R.R. Tolkien",  1954, 24.00}
    };

    printf("=== Catalogo Libri ===\n");
    printf("%-32s %-25s %4s  %6s\n",
           "TITOLO", "AUTORE", "ANNO", "PREZZO");

    for (int i = 0; i < 3; i++)
        stampa_libro(libri[i]);

    return 0;
}
```

</details>

---

### 🟡 Esercizio 2 — Registro studenti con ordinamento (Intermedio)

**Testo:** Scrivi un programma che:
1. Legge da tastiera N studenti (max 20), ciascuno con: cognome (max 30 char), nome (max 30 char), voto (intero 18–30)
2. Ordina gli studenti per voto **decrescente** usando il Bubble Sort
3. Stampa il registro ordinato con posizione, cognome, nome e voto
4. Stampa il voto più alto, il più basso e la media della classe

**Esempio input/output:**
```
Quanti studenti? 4
...

=== Registro (ordinato per voto) ===
 1. Bianchi Anna           30
 2. Conti Sara             28
 3. Rossi Luca             27
 4. Verdi Marco            24

Voto massimo: 30 | Voto minimo: 24 | Media: 27.25
```

**💡 Hint:**
1. Definisci `typedef struct { char cognome[31]; char nome[31]; int voto; } Studente;`
2. Per ordinamento decrescente: `if (classe[j].voto < classe[j+1].voto)` → scambia
3. Lo scambio è `Studente temp = classe[j]; classe[j] = classe[j+1]; classe[j+1] = temp;`
4. Per la media, somma tutti i voti e dividi per n (usa `float`)

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <string.h>

#define MAX 20

typedef struct {
    char cognome[31];
    char nome[31];
    int  voto;
} Studente;

int main() {
    Studente classe[MAX];
    int n, i, j;

    printf("Quanti studenti? ");
    scanf("%d", &n);
    getchar();
    if (n > MAX) n = MAX;

    for (i = 0; i < n; i++) {
        printf("Cognome: ");
        fgets(classe[i].cognome, sizeof(classe[i].cognome), stdin);
        if (classe[i].cognome[strlen(classe[i].cognome)-1] == '\n')
            classe[i].cognome[strlen(classe[i].cognome)-1] = '\0';

        printf("Nome: ");
        fgets(classe[i].nome, sizeof(classe[i].nome), stdin);
        if (classe[i].nome[strlen(classe[i].nome)-1] == '\n')
            classe[i].nome[strlen(classe[i].nome)-1] = '\0';

        printf("Voto: ");
        scanf("%d", &classe[i].voto);
        getchar();
    }

    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - 1 - i; j++) {
            if (classe[j].voto < classe[j+1].voto) {
                Studente temp = classe[j];
                classe[j]     = classe[j+1];
                classe[j+1]   = temp;
            }
        }
    }

    printf("\n=== Registro (ordinato per voto) ===\n");
    for (i = 0; i < n; i++)
        printf("%2d. %-15s %-15s  %d\n",
               i+1, classe[i].cognome, classe[i].nome, classe[i].voto);

    int max = classe[0].voto, min = classe[n-1].voto;
    float somma = 0;
    for (i = 0; i < n; i++) somma += classe[i].voto;

    printf("\nVoto massimo: %d | Voto minimo: %d | Media: %.2f\n",
           max, min, somma / n);

    return 0;
}
```

</details>

---

### 🔴 Esercizio 3 — Gestione magazzino (Avanzato)

**Testo:** Scrivi un programma per la gestione di un magazzino con al massimo 15 prodotti. Ogni prodotto ha: `codice` (stringa max 10 char), `descrizione` (stringa max 40 char), `prezzo` (float), `quantita` (intero). Il programma deve:
1. Leggere N prodotti da tastiera
2. Calcolare e stampare il **valore totale** di ogni prodotto (prezzo × quantità)
3. Trovare e stampare il prodotto con il **valore totale più alto**
4. Ordinare i prodotti per **valore totale decrescente** e stampare il magazzino
5. Segnalare tutti i prodotti con quantità ≤ 2 (scorte critiche)

**Esempio input/output:**
```
=== Magazzino ordinato per valore ===
COD    DESCRIZIONE                    PREZZO   QTY   VALORE TOT
P001   Monitor 24"                   €189.00     5   €  945.00
P002   Mouse wireless                € 22.50    15   €  337.50
P003   Tastiera USB                  € 45.90     2   €   91.80

Prodotto di maggior valore: Monitor 24" (€945.00)

⚠ Scorte critiche (qty <= 2):
  [P003] Tastiera USB — qty: 2
```

**💡 Hint:**
1. Definisci la struct con i 4 campi; calcola il valore come `p.prezzo * p.quantita` al momento della stampa
2. Per trovare il massimo, usa `idx_max = 0` e aggiorna confrontando il valore dei prodotti
3. Per l'ordinamento, confronta `magazzino[j].prezzo * magazzino[j].quantita`
4. Per le scorte critiche, un ciclo `for` con `if (magazzino[i].quantita <= 2)`

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <string.h>

#define MAX 15

typedef struct {
    char codice[11];
    char descrizione[41];
    float prezzo;
    int   quantita;
} Prodotto;

float valore(Prodotto p) {
    return p.prezzo * p.quantita;
}

void stampa_prodotto(Prodotto p) {
    printf("%-6s %-30s €%7.2f  %4d  €%8.2f\n",
           p.codice, p.descrizione,
           p.prezzo, p.quantita, valore(p));
}

int main() {
    Prodotto magazzino[MAX];
    int n, i, j;

    printf("Quanti prodotti? ");
    scanf("%d", &n);
    getchar();
    if (n > MAX) n = MAX;

    for (i = 0; i < n; i++) {
        printf("\nCodice: ");
        fgets(magazzino[i].codice, sizeof(magazzino[i].codice), stdin);
        if (magazzino[i].codice[strlen(magazzino[i].codice)-1] == '\n')
            magazzino[i].codice[strlen(magazzino[i].codice)-1] = '\0';

        printf("Descrizione: ");
        fgets(magazzino[i].descrizione, sizeof(magazzino[i].descrizione), stdin);
        if (magazzino[i].descrizione[strlen(magazzino[i].descrizione)-1] == '\n')
            magazzino[i].descrizione[strlen(magazzino[i].descrizione)-1] = '\0';

        printf("Prezzo: ");
        scanf("%f", &magazzino[i].prezzo);
        printf("Quantita': ");
        scanf("%d", &magazzino[i].quantita);
        getchar();
    }

    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - 1 - i; j++) {
            if (valore(magazzino[j]) < valore(magazzino[j+1])) {
                Prodotto temp  = magazzino[j];
                magazzino[j]   = magazzino[j+1];
                magazzino[j+1] = temp;
            }
        }
    }

    printf("\n=== Magazzino ordinato per valore ===\n");
    printf("%-6s %-30s %7s  %4s  %9s\n",
           "COD", "DESCRIZIONE", "PREZZO", "QTY", "VALORE TOT");
    for (i = 0; i < n; i++)
        stampa_prodotto(magazzino[i]);

    printf("\nProdotto di maggior valore: %s (€%.2f)\n",
           magazzino[0].descrizione, valore(magazzino[0]));

    int critici = 0;
    for (i = 0; i < n; i++) {
        if (magazzino[i].quantita <= 2) {
            if (!critici) printf("\n⚠ Scorte critiche (qty <= 2):\n");
            printf("  [%s] %s — qty: %d\n",
                   magazzino[i].codice,
                   magazzino[i].descrizione,
                   magazzino[i].quantita);
            critici++;
        }
    }
    if (!critici)
        printf("\nNessuna scorta critica.\n");

    return 0;
}
```

</details>

---

## 🎯 Recap finale (5 min)

- **Una `struct` raggruppa dati di tipo diverso** in un'unica variabile composita — nome, telefono, prezzo e quantità viaggiano sempre insieme, eliminando il rischio di disallineamento degli array paralleli.
- **L'operatore `.` accede ai campi**: `variabile.campo` per variabili singole, `array[i].campo` per array di struct.
- **L'assegnazione `=` funziona tra struct**: copia automaticamente tutti i campi — questo rende lo scambio nel Bubble Sort semplicissimo (3 righe con una variabile temporanea dello stesso tipo).
- **`typedef struct { ... } Nome;`** crea un alias che elimina la parola chiave `struct` dalla dichiarazione delle variabili, rendendo il codice più leggibile.
- ⚠️ **Errore comune da evitare:** usare `s.nome = "testo"` per i campi di tipo stringa — i campi array all'interno di una struct seguono le stesse regole degli array normali: si deve usare `strcpy(s.nome, "testo")`.
- 📌 **Prossima lezione (G15):** approfondimento delle struct in un contesto progettuale più ampio — introduzione al progetto Faber, dove i concetti di oggi verranno applicati a un problema reale.



---

# 23 lezione strutture oggetti faber studente completo

**File:** `23 lezione strutture oggetti faber studente completo.md`
**Tipo:** `.md`
**Dimensione:** 29.4 KB
**Ultima modifica:** 02/07/2026 09:24

---

# Lezione G15: Strutture, Oggetti e Progetto Faber

**Durata totale:** 4 ore
**Teoria:** 3 ore | **Esercizi:** 1 ora
**Data:** _______________
**Ambiente:** CLion (JetBrains)
**Giornata:** G15 di 19 — Ore corso: 56/76

---

## PARTE 1 — TEORIA (3 ore)

### 1.1 Introduzione e motivazione

Immagina di dover gestire un archivio di dipendenti di un'azienda. Per ogni dipendente ti servono: nome, cognome, età, stipendio, reparto. Con quello che sai finora, dovresti usare array separati:

```c
char nomi[100][50];
char cognomi[100][50];
int eta[100];
float stipendi[100];
char reparti[100][30];
```

Questo approccio è fragile: se vuoi spostare il dipendente numero 5 in un'altra posizione, devi aggiornare tutti e cinque gli array separatamente. Un errore è quasi garantito.

Le **strutture** (`struct`) risolvono questo problema: permettono di raggruppare dati di tipo diverso sotto un unico nome. Sono il mattone fondamentale della programmazione orientata ai dati — e, come vedremo, il precursore diretto degli **oggetti** della programmazione orientata agli oggetti (OOP).

Il **Progetto Faber** è un sistema gestionale per un negozio di strumenti musicali. Oggi costruiremo insieme le strutture dati che lo sostengono: un catalogo di strumenti, un registro di vendite, e le funzioni per gestirli.

---

### 1.2 Spiegazione dell'argomento

#### 1.2.1 Ripasso: cos'è una `struct`

Una `struct` è un tipo di dato composto, definito dal programmatore, che raccoglie variabili (chiamate **campi** o **membri**) anche di tipo diverso.

**Sintassi:**

```c
struct NomeTipo {
    tipo1 campo1;
    tipo2 campo2;
    // ...
};
```

**Dichiarazione di una variabile:**

```c
struct NomeTipo variabile;
```

**Accesso ai campi (operatore punto):**

```c
variabile.campo1 = valore;
```

**Memoria — come è organizzata una struct:**

```
struct Punto { int x; int y; };

Memoria RAM:
+--------+--------+
|   x    |   y    |
| 4 byte | 4 byte |
+--------+--------+
   ^
   indirizzo della struct
```

Ogni campo occupa spazio contiguo in memoria. La dimensione totale è (almeno) la somma dei campi — il compilatore può aggiungere padding per l'allineamento.

#### 1.2.2 `typedef` — dare un nome pulito alla struct

Scrivere `struct Strumento s;` ogni volta è verboso. Con `typedef` possiamo rinominare il tipo:

```c
typedef struct {
    char nome[50];
    char categoria[30];
    float prezzo;
    int quantita;
} Strumento;
```

Ora possiamo scrivere semplicemente:

```c
Strumento s;
```

Questa è la forma moderna e preferita in C.

#### 1.2.3 Inizializzazione di una struct

**Modo 1 — inizializzazione per posizione:**

```c
Strumento s = {"Chitarra Classica", "Cordofoni", 349.90f, 5};
```

**Modo 2 — inizializzazione per nome (C99, più leggibile):**

```c
Strumento s = {
    .nome = "Chitarra Classica",
    .categoria = "Cordofoni",
    .prezzo = 349.90f,
    .quantita = 5
};
```

**Modo 3 — assegnazione campo per campo:**

```c
Strumento s;
strcpy(s.nome, "Chitarra Classica");
strcpy(s.categoria, "Cordofoni");
s.prezzo = 349.90f;
s.quantita = 5;
```

⚠️ Per i campi stringa, non usare `=` ma sempre `strcpy()` — oppure `snprintf()` se vuoi più sicurezza.

#### 1.2.4 Array di struct

È la combinazione più utile: un catalogo, un archivio, un registro.

```
Strumento catalogo[100]:

catalogo[0]             catalogo[1]             catalogo[2]
+------------------+   +------------------+   +------------------+
| nome: "Chitarra" |   | nome: "Violino"  |   | nome: "Tromba"   |
| cat:  "Cordof."  |   | cat:  "Cordof."  |   | cat:  "Ottoni"   |
| prezzo: 349.90   |   | prezzo: 890.00   |   | prezzo: 520.00   |
| quantita: 5      |   | quantita: 2      |   | quantita: 8      |
+------------------+   +------------------+   +------------------+
```

Accesso:

```c
catalogo[0].prezzo = 399.90f;
printf("%s: %.2f €\n", catalogo[1].nome, catalogo[1].prezzo);
```

#### 1.2.5 Struct come parametri di funzione

**Passaggio per valore (copia):** la funzione riceve una copia. Modifiche non si propagano.

```c
void stampa_strumento(Strumento s) {
    printf("[%s] %s — %.2f €, qty: %d\n",
           s.categoria, s.nome, s.prezzo, s.quantita);
}
```

**Passaggio per indirizzo (puntatore):** la funzione lavora sull'originale. Modifiche si propagano. Si usa l'operatore `->` per accedere ai campi.

```c
void applica_sconto(Strumento *s, float percentuale) {
    s->prezzo *= (1.0f - percentuale / 100.0f);
}
```

Regola pratica:
- Se la funzione **legge** la struct → passa per valore (o `const *`)
- Se la funzione **modifica** la struct → passa per puntatore

#### 1.2.6 Operatore `->` vs `.`

```
Strumento s;          →  s.prezzo         (variabile diretta)
Strumento *p = &s;   →  p->prezzo        (puntatore)
                         (*p).prezzo      (equivalente, ma più verboso)
```

```
Accesso diretto:              Accesso tramite puntatore:
   s                              p
+--------+                    +------+     +--------+
| prezzo |   <-- s.prezzo     | addr |---> | prezzo |  <-- p->prezzo
+--------+                    +------+     +--------+
```

#### 1.2.7 Struct annidate

Una struct può contenere un'altra struct come campo:

```c
typedef struct {
    int giorno;
    int mese;
    int anno;
} Data;

typedef struct {
    char cliente[50];
    Strumento articolo;
    int quantita_venduta;
    Data data_vendita;
    float totale;
} Vendita;
```

Accesso:

```c
Vendita v;
v.data_vendita.giorno = 15;
v.data_vendita.mese   = 3;
v.data_vendita.anno   = 2025;
```

#### 1.2.8 Dal C agli oggetti — il ponte concettuale

Le `struct` del C e gli **oggetti** dell'OOP (Java, C++, Python) condividono l'idea di fondo: raggruppare dati correlati. La differenza principale è che gli oggetti aggiungono **metodi** (funzioni) direttamente all'interno del tipo.

```
STRUCT in C:                    OGGETTO in Java/C++:
+------------------------+      +----------------------------+
| DATI                   |      | DATI (attributi)           |
|  nome, prezzo, qty     |      |  nome, prezzo, qty         |
+------------------------+      +----------------------------+
                                | COMPORTAMENTI (metodi)     |
Funzioni ESTERNE:               |  stampa(), applica_sconto()|
stampa_strumento(&s);           +----------------------------+
applica_sconto(&s, 10);         s.stampa(); s.sconto(10);
```

In C, il "collegamento" tra dati e funzioni è implicito (convezione: passiamo sempre la struct come primo parametro). Negli OOP è esplicito e garantito dal linguaggio.

Questa è la **radice storica e concettuale** dell'OOP: C → C with classes → C++ → Java.

---

### 1.3 Esempi di codice commentati

#### Esempio 1 — Struttura base e stampa

```c
#include <stdio.h>
#include <string.h>

typedef struct {
    char nome[50];
    char categoria[30];
    float prezzo;
    int quantita;
} Strumento;

void stampa_strumento(Strumento s) {
    printf("%-25s | %-15s | %8.2f € | qty: %d\n",
           s.nome, s.categoria, s.prezzo, s.quantita);
}

int main() {
    Strumento s1, s2, s3;

    strcpy(s1.nome, "Chitarra Classica");
    strcpy(s1.categoria, "Cordofoni");
    s1.prezzo    = 349.90f;
    s1.quantita  = 5;

    Strumento s2_init = {"Violino 4/4", "Cordofoni", 890.00f, 2};
    s2 = s2_init;

    Strumento s3_init = {
        .nome      = "Tromba in Sib",
        .categoria = "Ottoni",
        .prezzo    = 520.00f,
        .quantita  = 8
    };
    s3 = s3_init;

    printf("%-25s | %-15s | %8s   | %s\n",
           "NOME", "CATEGORIA", "PREZZO", "QTY");
    printf("%-25s-+-%-15s-+-%-8s---+------\n",
           "-------------------------", "---------------", "--------");

    stampa_strumento(s1);
    stampa_strumento(s2);
    stampa_strumento(s3);

    return 0;
}
```

**Output atteso:**
```
NOME                      | CATEGORIA       |   PREZZO   | QTY
--------------------------+-----------------+------------+------
Chitarra Classica         | Cordofoni       |   349.90 € | qty: 5
Violino 4/4               | Cordofoni       |   890.00 € | qty: 2
Tromba in Sib             | Ottoni          |   520.00 € | qty: 8
```

---

#### Esempio 2 — Array di struct e funzione con puntatore

```c
#include <stdio.h>
#include <string.h>

#define MAX_CATALOGO 100

typedef struct {
    char nome[50];
    char categoria[30];
    float prezzo;
    int quantita;
} Strumento;

int aggiungi_strumento(Strumento catalogo[], int *n,
                       const char *nome, const char *cat,
                       float prezzo, int qty) {
    if (*n >= MAX_CATALOGO) return 0;
    strcpy(catalogo[*n].nome, nome);
    strcpy(catalogo[*n].categoria, cat);
    catalogo[*n].prezzo   = prezzo;
    catalogo[*n].quantita = qty;
    (*n)++;
    return 1;
}

void sconto_categoria(Strumento catalogo[], int n,
                      const char *categoria, float perc) {
    for (int i = 0; i < n; i++) {
        if (strcmp(catalogo[i].categoria, categoria) == 0) {
            catalogo[i].prezzo *= (1.0f - perc / 100.0f);
        }
    }
}

void stampa_catalogo(const Strumento catalogo[], int n) {
    printf("\n--- CATALOGO (%d articoli) ---\n", n);
    for (int i = 0; i < n; i++) {
        printf("%2d. %-25s [%-12s] %8.2f €  qty:%d\n",
               i + 1,
               catalogo[i].nome,
               catalogo[i].categoria,
               catalogo[i].prezzo,
               catalogo[i].quantita);
    }
}

int main() {
    Strumento catalogo[MAX_CATALOGO];
    int n = 0;

    aggiungi_strumento(catalogo, &n, "Chitarra Classica",  "Cordofoni", 349.90f, 5);
    aggiungi_strumento(catalogo, &n, "Chitarra Elettrica", "Cordofoni", 720.00f, 3);
    aggiungi_strumento(catalogo, &n, "Violino 4/4",        "Cordofoni", 890.00f, 2);
    aggiungi_strumento(catalogo, &n, "Tromba in Sib",      "Ottoni",    520.00f, 8);
    aggiungi_strumento(catalogo, &n, "Basso Elettrico",    "Cordofoni", 480.00f, 4);

    stampa_catalogo(catalogo, n);

    printf("\nApplico sconto 10%% ai Cordofoni...\n");
    sconto_categoria(catalogo, n, "Cordofoni", 10.0f);

    stampa_catalogo(catalogo, n);

    return 0;
}
```

**Output atteso:**
```
--- CATALOGO (5 articoli) ---
 1. Chitarra Classica      [Cordofoni   ]   349.90 €  qty:5
 2. Chitarra Elettrica     [Cordofoni   ]   720.00 €  qty:3
 3. Violino 4/4            [Cordofoni   ]   890.00 €  qty:2
 4. Tromba in Sib          [Ottoni      ]   520.00 €  qty:8
 5. Basso Elettrico        [Cordofoni   ]   480.00 €  qty:4

Applico sconto 10% ai Cordofoni...

--- CATALOGO (5 articoli) ---
 1. Chitarra Classica      [Cordofoni   ]   314.91 €  qty:5
 2. Chitarra Elettrica     [Cordofoni   ]   648.00 €  qty:3
 3. Violino 4/4            [Cordofoni   ]   801.00 €  qty:2
 4. Tromba in Sib          [Ottoni      ]   520.00 €  qty:8
 5. Basso Elettrico        [Cordofoni   ]   432.00 €  qty:4
```

---

#### Esempio 3 — Struct annidate: Vendita con Data

```c
#include <stdio.h>
#include <string.h>

typedef struct {
    char nome[50];
    char categoria[30];
    float prezzo;
    int quantita;
} Strumento;

typedef struct {
    int giorno;
    int mese;
    int anno;
} Data;

typedef struct {
    char cliente[50];
    Strumento articolo;
    int quantita_venduta;
    Data data_vendita;
    float totale;
} Vendita;

void stampa_vendita(const Vendita *v) {
    printf("Cliente:  %s\n", v->cliente);
    printf("Articolo: %s (%.2f € x %d)\n",
           v->articolo.nome,
           v->articolo.prezzo,
           v->quantita_venduta);
    printf("Totale:   %.2f €\n", v->totale);
    printf("Data:     %02d/%02d/%04d\n",
           v->data_vendita.giorno,
           v->data_vendita.mese,
           v->data_vendita.anno);
}

int main() {
    Strumento ch;
    strcpy(ch.nome, "Chitarra Classica");
    strcpy(ch.categoria, "Cordofoni");
    ch.prezzo   = 349.90f;
    ch.quantita = 5;

    Vendita v;
    strcpy(v.cliente, "Marco Rossi");
    v.articolo         = ch;
    v.quantita_venduta = 2;
    v.data_vendita.giorno = 15;
    v.data_vendita.mese   = 3;
    v.data_vendita.anno   = 2025;
    v.totale = v.articolo.prezzo * v.quantita_venduta;

    printf("=== SCONTRINO ===\n");
    stampa_vendita(&v);

    return 0;
}
```

**Output atteso:**
```
=== SCONTRINO ===
Cliente:  Marco Rossi
Articolo: Chitarra Classica (349.90 € x 2)
Totale:   699.80 €
Data:     15/03/2025
```

---

### 1.4 Riepilogo visivo

```
CONCETTI CHIAVE — STRUCT IN C
═══════════════════════════════════════════════════════════════

 DEFINIZIONE                    ACCESSO
 ──────────                     ───────
 typedef struct {               Diretta:    s.campo
     tipo1 campo1;              Puntatore:  p->campo
     tipo2 campo2;              Annidato:   s.inner.campo
 } NomeTipo;

 INIZIALIZZAZIONE               FUNZIONI
 ──────────────                 ────────
 Per posizione: {"a", 1, 2.0}  Lettura → passa per valore
 Per nome: {.campo = val}       Modifica → passa per puntatore
 Campo per campo: s.x = 5;

 ARRAY DI STRUCT                STRUCT ANNIDATE
 ──────────────                 ───────────────
 NomeTipo arr[N];               typedef struct {
 arr[i].campo = val;                Data d;     ← struct dentro struct
 for (i = 0..n) arr[i]...          float tot;
                                } Vendita;

 DAL C AGLI OGGETTI
 ──────────────────
 C struct    →  dati raggruppati
 C funzioni  →  comportamenti separati
 OOP objects →  dati + metodi insieme (incapsulamento)
```

---

### 1.5 Domande di verifica orale

**D1:** Qual è la differenza tra `s.campo` e `p->campo`?

<details>
<summary><b>💡 RISPOSTA</b></summary>

`s.campo` si usa quando `s` è una variabile struct (accesso diretto). `p->campo` si usa quando `p` è un puntatore a struct; equivale a `(*p).campo`.

</details>

---

**D2:** Perché per copiare una stringa in un campo struct si usa `strcpy` e non l'operatore `=`?

<details>
<summary><b>💡 RISPOSTA</b></summary>

I campi stringa sono array di char. In C non si possono assegnare array con `=` (assegnerebbe l'indirizzo, non il contenuto). `strcpy` copia byte per byte il contenuto. L'eccezione è l'inizializzazione con letterale stringa alla dichiarazione.

</details>

---

**D3:** Quando conviene passare una struct per puntatore invece che per valore?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Sempre quando la funzione deve **modificare** la struct originale. Anche quando la struct è grande, per evitare la copia in memoria (efficienza). Per sola lettura si può usare `const Strumento *s`.

</details>

---

**D4:** Cosa sono le struct annidate? Fai un esempio.

<details>
<summary><b>💡 RISPOSTA</b></summary>

Una struct che contiene un campo di tipo struct. Esempio: una struct `Vendita` che ha un campo `Data data_vendita` di tipo struct `Data`. Si accede con doppio punto: `v.data_vendita.giorno`.

</details>

---

**D5:** Qual è la differenza concettuale tra una struct in C e un oggetto in Java/C++?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Entrambi raggruppano dati correlati. La differenza è che gli oggetti includono anche i metodi (funzioni) all'interno del tipo, realizzando l'incapsulamento. In C, le funzioni che lavorano su una struct sono esterne e ricevono la struct come parametro.

</details>

---

**D6:** Come si scorre un array di struct con un ciclo `for`? Scrivi la sintassi.

<details>
<summary><b>💡 RISPOSTA</b></summary>

```c
for (int i = 0; i < n; i++) {
    // accesso: arr[i].campo
    printf("%s\n", arr[i].nome);
}
```

</details>

---

**D7:** `sizeof(Strumento)` sarà sempre uguale alla somma dei `sizeof` dei singoli campi?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Non necessariamente. Il compilatore può inserire **padding** (byte di allineamento) tra i campi per ottimizzare l'accesso in memoria. Quindi `sizeof(struct)` può essere ≥ alla somma dei campi.

</details>

---

## PARTE 2 — ESERCIZI (1 ora)

---

### 🟢 Livello Base

#### Esercizio 1 — Schedario Strumenti (20 min)

**Testo:**
Crea una struttura `Strumento` con i campi: `nome` (stringa, max 50 char), `categoria` (stringa, max 30 char), `prezzo` (float), `quantita` (int). Scrivi un programma che:
1. Chiede all'utente di inserire 3 strumenti da tastiera
2. Stampa un riepilogo tabellare di tutti gli strumenti inseriti

**Esempio Input:**
```
Strumento 1:
  Nome: Chitarra Classica
  Categoria: Cordofoni
  Prezzo: 349.90
  Quantita: 5
...
```

**Esempio Output:**
```
--- CATALOGO ---
1. Chitarra Classica     [Cordofoni]  349.90 € qty:5
2. Tromba in Sib         [Ottoni   ]  520.00 € qty:8
3. Flauto Traverso       [Legni    ]  280.00 € qty:3
```

**💡 Hint:**
1. Definisci `typedef struct { ... } Strumento;` prima del `main`
2. Usa un array `Strumento catalogo[3];` e un ciclo `for` per l'inserimento
3. Per leggere stringhe con spazi usa `fgets` e rimuovi il `\n` finale con `strcspn`
4. Per leggere float usa `scanf("%f", &catalogo[i].prezzo)`

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <string.h>

typedef struct {
    char nome[50];
    char categoria[30];
    float prezzo;
    int quantita;
} Strumento;

int main() {
    Strumento catalogo[3];
    int n = 3;

    for (int i = 0; i < n; i++) {
        printf("\nStrumento %d:\n", i + 1);

        printf("  Nome: ");
        fgets(catalogo[i].nome, sizeof(catalogo[i].nome), stdin);
        catalogo[i].nome[strcspn(catalogo[i].nome, "\n")] = '\0';

        printf("  Categoria: ");
        fgets(catalogo[i].categoria, sizeof(catalogo[i].categoria), stdin);
        catalogo[i].categoria[strcspn(catalogo[i].categoria, "\n")] = '\0';

        printf("  Prezzo: ");
        scanf("%f", &catalogo[i].prezzo);

        printf("  Quantita: ");
        scanf("%d", &catalogo[i].quantita);

        while (getchar() != '\n');
    }

    printf("\n--- CATALOGO ---\n");
    for (int i = 0; i < n; i++) {
        printf("%d. %-20s [%-10s] %8.2f € qty:%d\n",
               i + 1,
               catalogo[i].nome,
               catalogo[i].categoria,
               catalogo[i].prezzo,
               catalogo[i].quantita);
    }

    return 0;
}
```

</details>

---

### 🟡 Livello Intermedio

#### Esercizio 2 — Valore del Magazzino (25 min)

**Testo:**
Partendo da un catalogo di 5 strumenti hardcoded, scrivi una funzione `float valore_magazzino(Strumento catalogo[], int n)` che restituisce il valore totale del magazzino (prezzo × quantità per ogni strumento). Aggiungi anche una funzione `Strumento strumento_piu_costoso(Strumento catalogo[], int n)` che restituisce lo strumento con il prezzo più alto.

**Esempio Output:**
```
Valore totale magazzino: 13029.50 EUR
Strumento piu costoso: Violino 4/4 (890.00 EUR)
```

**💡 Hint:**
1. `valore_magazzino` scorre l'array con un `for` e accumula `catalogo[i].prezzo * catalogo[i].quantita`
2. `strumento_piu_costoso` tiene traccia dell'indice del massimo, come l'algoritmo di ricerca del massimo su array
3. Le funzioni ricevono l'array per indirizzo (automatico per gli array) e la dimensione `n`
4. Una funzione può restituire una struct per valore: `return catalogo[idx_max];`

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <string.h>

typedef struct {
    char nome[50];
    char categoria[30];
    float prezzo;
    int quantita;
} Strumento;

float valore_magazzino(Strumento catalogo[], int n) {
    float totale = 0.0f;
    for (int i = 0; i < n; i++) {
        totale += catalogo[i].prezzo * catalogo[i].quantita;
    }
    return totale;
}

Strumento strumento_piu_costoso(Strumento catalogo[], int n) {
    int idx_max = 0;
    for (int i = 1; i < n; i++) {
        if (catalogo[i].prezzo > catalogo[idx_max].prezzo) {
            idx_max = i;
        }
    }
    return catalogo[idx_max];
}

int main() {
    Strumento catalogo[] = {
        {"Chitarra Classica",  "Cordofoni", 349.90f, 5},
        {"Chitarra Elettrica", "Cordofoni", 720.00f, 3},
        {"Violino 4/4",        "Cordofoni", 890.00f, 2},
        {"Tromba in Sib",      "Ottoni",    520.00f, 8},
        {"Basso Elettrico",    "Cordofoni", 480.00f, 4}
    };
    int n = 5;

    float valore = valore_magazzino(catalogo, n);
    printf("Valore totale magazzino: %.2f EUR\n", valore);

    Strumento piu_costoso = strumento_piu_costoso(catalogo, n);
    printf("Strumento piu costoso: %s (%.2f EUR)\n",
           piu_costoso.nome, piu_costoso.prezzo);

    return 0;
}
```

</details>

---

#### Esercizio 3 — Mini Progetto Faber: Registro Vendite (30 min)

**Testo:**
Crea una struct `Vendita` con i campi: `cliente` (stringa), `nome_strumento` (stringa), `prezzo_unitario` (float), `quantita` (int), `totale` (float). Scrivi un programma che:
1. Permette di registrare fino a 10 vendite (inserimento da tastiera)
2. Al termine, stampa tutte le vendite e il totale incassato

**Esempio Output:**
```
=== REGISTRO VENDITE ===
1. Marco Rossi       | Chitarra Classica   | 2 x 349.90 = 699.80 EUR
2. Laura Bianchi     | Tromba in Sib       | 1 x 520.00 = 520.00 EUR
---------------------------------
Totale incassato: 1219.80 EUR
```

**💡 Hint:**
1. La struct `Vendita` non ha bisogno di contenere la struct `Strumento` — basta `nome_strumento` come stringa e `prezzo_unitario` come float
2. Calcola `totale = prezzo_unitario * quantita` al momento dell'inserimento
3. Usa un ciclo `do-while` con una condizione di uscita ("s/n")
4. Tieni un contatore `n_vendite` da passare alla funzione di stampa

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <string.h>

#define MAX_VENDITE 10

typedef struct {
    char cliente[50];
    char nome_strumento[50];
    float prezzo_unitario;
    int quantita;
    float totale;
} Vendita;

void stampa_registro(const Vendita registro[], int n) {
    float totale_incassato = 0.0f;
    printf("\n=== REGISTRO VENDITE ===\n");
    for (int i = 0; i < n; i++) {
        printf("%2d. %-20s | %-20s | %d x %.2f = %.2f EUR\n",
               i + 1,
               registro[i].cliente,
               registro[i].nome_strumento,
               registro[i].quantita,
               registro[i].prezzo_unitario,
               registro[i].totale);
        totale_incassato += registro[i].totale;
    }
    printf("---------------------------------\n");
    printf("Totale incassato: %.2f EUR\n", totale_incassato);
}

int main() {
    Vendita registro[MAX_VENDITE];
    int n = 0;
    char continua;

    do {
        if (n >= MAX_VENDITE) { printf("Registro pieno!\n"); break; }

        printf("\n--- Nuova vendita (#%d) ---\n", n + 1);

        printf("Cliente: ");
        fgets(registro[n].cliente, sizeof(registro[n].cliente), stdin);
        registro[n].cliente[strcspn(registro[n].cliente, "\n")] = '\0';

        printf("Strumento: ");
        fgets(registro[n].nome_strumento, sizeof(registro[n].nome_strumento), stdin);
        registro[n].nome_strumento[strcspn(registro[n].nome_strumento, "\n")] = '\0';

        printf("Prezzo unitario: ");
        scanf("%f", &registro[n].prezzo_unitario);

        printf("Quantita: ");
        scanf("%d", &registro[n].quantita);

        registro[n].totale = registro[n].prezzo_unitario * registro[n].quantita;
        n++;

        printf("Altra vendita? (s/n): ");
        scanf(" %c", &continua);
        while (getchar() != '\n');

    } while (continua == 's' || continua == 'S');

    stampa_registro(registro, n);

    return 0;
}
```

</details>

---

### 🔴 Livello Avanzato

#### Esercizio 4 — Progetto Faber Completo (45 min)

**Testo:**
Integra tutto in un mini-gestionale con menu interattivo:
```
1. Aggiungi strumento al catalogo
2. Visualizza catalogo
3. Registra una vendita (scegliendo da catalogo, aggiorna la quantità)
4. Visualizza registro vendite e totale incassato
5. Esci
```

Regole:
- Non è possibile vendere più pezzi di quanti ce ne siano in magazzino
- Ogni vendita aggiorna il campo `quantita` dello strumento venduto nel catalogo
- Il programma termina solo scegliendo l'opzione 5

**💡 Hint:**
1. Definisci due array: `Strumento catalogo[MAX]` e `Vendita registro[MAX]` con relativi contatori
2. Scrivi una funzione per ogni voce di menu — mantieni il `main` pulito (solo il ciclo del menu)
3. Per la vendita: mostra prima il catalogo, chiedi l'indice, controlla `qty_richiesta <= catalogo[idx].quantita`
4. Aggiorna `catalogo[idx].quantita -= qty_venduta` dopo la vendita

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <string.h>

#define MAX_CAT 50
#define MAX_VEN 100

typedef struct {
    char nome[50];
    char categoria[30];
    float prezzo;
    int quantita;
} Strumento;

typedef struct {
    char cliente[50];
    char nome_strumento[50];
    float prezzo_unitario;
    int quantita;
    float totale;
} Vendita;

Strumento catalogo[MAX_CAT];
int n_cat = 0;

Vendita registro[MAX_VEN];
int n_ven = 0;

void leggi_stringa(const char *prompt, char *dest, int size) {
    printf("%s", prompt);
    fgets(dest, size, stdin);
    dest[strcspn(dest, "\n")] = '\0';
}

void aggiungi_strumento(void) {
    if (n_cat >= MAX_CAT) { printf("Catalogo pieno.\n"); return; }
    Strumento *s = &catalogo[n_cat];
    leggi_stringa("Nome: ", s->nome, sizeof(s->nome));
    leggi_stringa("Categoria: ", s->categoria, sizeof(s->categoria));
    printf("Prezzo: "); scanf("%f", &s->prezzo);
    printf("Quantita: "); scanf("%d", &s->quantita);
    while (getchar() != '\n');
    n_cat++;
    printf("Strumento aggiunto.\n");
}

void visualizza_catalogo(void) {
    if (n_cat == 0) { printf("Catalogo vuoto.\n"); return; }
    printf("\n%-3s %-25s %-15s %8s %5s\n", "#", "NOME", "CATEGORIA", "PREZZO", "QTY");
    for (int i = 0; i < n_cat; i++) {
        printf("%-3d %-25s %-15s %8.2f %5d\n",
               i + 1,
               catalogo[i].nome, catalogo[i].categoria,
               catalogo[i].prezzo, catalogo[i].quantita);
    }
}

void registra_vendita(void) {
    if (n_cat == 0) { printf("Catalogo vuoto.\n"); return; }
    if (n_ven >= MAX_VEN) { printf("Registro pieno.\n"); return; }

    visualizza_catalogo();

    int idx;
    printf("Scegli strumento (1-%d): ", n_cat);
    scanf("%d", &idx);
    while (getchar() != '\n');
    idx--;

    if (idx < 0 || idx >= n_cat) { printf("Indice non valido.\n"); return; }
    if (catalogo[idx].quantita == 0) { printf("Esaurito.\n"); return; }

    int qty;
    printf("Quantita (disponibili: %d): ", catalogo[idx].quantita);
    scanf("%d", &qty);
    while (getchar() != '\n');

    if (qty <= 0 || qty > catalogo[idx].quantita) {
        printf("Quantita non valida.\n"); return;
    }

    Vendita *v = &registro[n_ven];
    leggi_stringa("Cliente: ", v->cliente, sizeof(v->cliente));
    strcpy(v->nome_strumento, catalogo[idx].nome);
    v->prezzo_unitario = catalogo[idx].prezzo;
    v->quantita        = qty;
    v->totale          = v->prezzo_unitario * v->quantita;

    catalogo[idx].quantita -= qty;
    n_ven++;

    printf("Vendita registrata: %.2f EUR\n", v->totale);
}

void visualizza_vendite(void) {
    if (n_ven == 0) { printf("Nessuna vendita.\n"); return; }
    float totale = 0.0f;
    printf("\n=== REGISTRO VENDITE ===\n");
    for (int i = 0; i < n_ven; i++) {
        printf("%2d. %-18s | %-20s | %dx%.2f = %.2f EUR\n",
               i + 1,
               registro[i].cliente,
               registro[i].nome_strumento,
               registro[i].quantita,
               registro[i].prezzo_unitario,
               registro[i].totale);
        totale += registro[i].totale;
    }
    printf("Totale incassato: %.2f EUR\n", totale);
}

int main() {
    int scelta;

    Strumento init[] = {
        {"Chitarra Classica",  "Cordofoni", 349.90f, 5},
        {"Tromba in Sib",      "Ottoni",    520.00f, 8},
        {"Violino 4/4",        "Cordofoni", 890.00f, 2}
    };
    for (int i = 0; i < 3; i++) catalogo[n_cat++] = init[i];

    do {
        printf("\n=== FABER MUSIC MANAGER ===\n");
        printf("1. Aggiungi strumento\n");
        printf("2. Visualizza catalogo\n");
        printf("3. Registra vendita\n");
        printf("4. Visualizza vendite\n");
        printf("5. Esci\n");
        printf("Scelta: ");
        scanf("%d", &scelta);
        while (getchar() != '\n');

        switch (scelta) {
            case 1: aggiungi_strumento(); break;
            case 2: visualizza_catalogo(); break;
            case 3: registra_vendita();    break;
            case 4: visualizza_vendite();  break;
            case 5: printf("Arrivederci!\n"); break;
            default: printf("Scelta non valida.\n");
        }
    } while (scelta != 5);

    return 0;
}
```

</details>

---

## 🎯 Recap finale (5 min)

- **`typedef struct`** permette di creare tipi composti personalizzati che raggruppano dati eterogenei sotto un unico nome — il mattone base della modellazione dati in C.
- **Operatore `.` vs `->`**: si usa `.` per accedere ai campi di una variabile struct, `->` per accedere ai campi tramite un puntatore a struct.
- **Passaggio per valore vs puntatore**: le funzioni che devono modificare una struct ricevono un puntatore (`Strumento *s`); quelle che la leggono soltanto possono riceverla per valore o come `const Strumento *s`.
- **Struct annidate e array di struct**: strumenti potenti per modellare entità reali complesse — un archivio, un registro vendite, un catalogo.
- ⚠️ **Errore comune da evitare**: assegnare una stringa a un campo con `s.nome = "valore"` — questo non compila (o produce un warning grave) perché `nome` è un array. Usa sempre `strcpy(s.nome, "valore")`.
- 📌 **Prossima lezione (G16):** Le struct incontrano i file — impareremo a salvare e leggere strutture su disco usando `fwrite`/`fread` e `fprintf`/`fscanf`, rendendo i dati persistenti tra un'esecuzione e l'altra.



---

# 24 lezione strutture file studente completo

**File:** `24 lezione strutture file studente completo.md`
**Tipo:** `.md`
**Dimensione:** 25.2 KB
**Ultima modifica:** 02/07/2026 09:24

---

# Lezione G16: Strutture e Gestione File — Lettura e Scrittura su File

**Durata totale:** 4 ore
**Teoria:** 3 ore | **Esercizi:** 1 ora
**Data:** _______________
**Ambiente:** CLion (JetBrains)
**Giornata:** G16 di 19 — Ore corso: 64/76

---

# PARTE 1 — TEORIA (3 ore)

## 1.1 Introduzione e Motivazione

Finora tutti i dati del nostro programma esistono soltanto mentre il programma è in esecuzione: appena termina, ogni array, ogni struct, ogni variabile scompare. Immagina un programma gestionale per una piccola biblioteca: se alla chiusura del programma l'elenco dei libri viene perso, il sistema è inutilizzabile.

La **gestione dei file** risolve questo problema: permette di salvare dati su disco e rileggerne ad ogni avvio, rendendo i programmi **persistenti**.

Combinando `struct` (già note da G14–G15) con la lettura/scrittura su file otteniamo uno degli strumenti più potenti del C standard: la capacità di costruire archivi dati rudimentali, simili a un database minimo.

---

## 1.2 Spiegazione dell'Argomento

### 1.2.1 Il tipo `FILE` e le funzioni principali

In C la gestione dei file avviene tramite un **puntatore a FILE**:

```c
FILE *fp;
```

`FILE` è un tipo definito in `<stdio.h>`. Il puntatore `fp` non punta direttamente al file su disco, ma a una struttura interna che gestisce il buffer e lo stato del file.

**Apertura e chiusura:**

```
fopen(nome_file, modalità)  →  restituisce FILE* oppure NULL se errore
fclose(fp)                  →  chiude il file e svuota il buffer
```

**Modalità di apertura:**

```
┌──────┬──────────────────────────────────────────────────────────┐
│ Modo │ Significato                                              │
├──────┼──────────────────────────────────────────────────────────┤
│ "r"  │ Lettura — il file deve esistere                          │
│ "w"  │ Scrittura — crea nuovo o svuota se esiste               │
│ "a"  │ Append — aggiunge in fondo, crea se non esiste           │
│ "rb" │ Lettura binaria                                          │
│ "wb" │ Scrittura binaria                                        │
│ "ab" │ Append binario                                           │
└──────┴──────────────────────────────────────────────────────────┘
```

### 1.2.2 File di testo vs file binari

**File di testo:** i dati vengono salvati come caratteri leggibili. Un intero `42` viene scritto come due byte: `'4'` e `'2'`. Utile per file leggibili con un editor.

**File binari:** i dati vengono scritti esattamente come sono in memoria. Un intero `42` occupa 4 byte (la sua rappresentazione binaria). Più compatti e veloci, ma non leggibili direttamente.

```
Valore int: 42

Testo:   [ '4' ][ '2' ][ '\n' ]   → 3 byte
Binario: [ 0x00 ][ 0x00 ][ 0x00 ][ 0x2A ]  → 4 byte (big-endian)
```

### 1.2.3 Operazioni su file di testo

**Scrittura con `fprintf`:**
```c
fprintf(fp, formato, argomenti);
// Esattamente come printf, ma scrive su file
```

**Lettura con `fscanf`:**
```c
fscanf(fp, formato, &variabile);
// Esattamente come scanf, ma legge da file
// Restituisce il numero di valori letti (utile per rilevare EOF)
```

**Lettura/scrittura di righe con `fgets` / `fputs`:**
```c
fgets(buffer, dimensione, fp);   // legge una riga (include '\n')
fputs(stringa, fp);              // scrive una stringa (senza '\n' automatico)
```

**Rilevamento fine file:**
```c
while (fscanf(fp, ...) == n_campi) { ... }  // preferibile
// oppure
while (!feof(fp)) { ... }                   // meno robusto, evitare come condizione principale
```

### 1.2.4 Operazioni su file binari: `fwrite` e `fread`

Questi due comandi permettono di leggere/scrivere blocchi di memoria raw.

```c
fwrite(ptr, dim_elemento, n_elementi, fp);
fread(ptr, dim_elemento, n_elementi, fp);
```

Entrambe restituiscono il numero di elementi effettivamente scritti/letti.

**Esempio concettuale:**
```
struct Libro libro = {"Il nome della rosa", "Eco", 1980};

fwrite(&libro, sizeof(struct Libro), 1, fp);
         │          │                │
         │          │                └── quanti elementi
         │          └─────────────────── dimensione di ciascuno
         └────────────────────────────── indirizzo da cui leggere
```

### 1.2.5 Salvataggio e caricamento di array di struct

Il pattern più comune in C per la persistenza dei dati è:

```
SALVATAGGIO                        CARICAMENTO
──────────                         ───────────
apri file in "wb"                  apri file in "rb"
fwrite(array, sizeof(T), n, fp)    n = fread(array, sizeof(T), MAX, fp)
chiudi file                        chiudi file
                                   usa n come dimensione effettiva
```

### 1.2.6 Schema generale del flusso

```
PROGRAMMA
   │
   ├─► fopen("dati.bin", "wb") ──────────────────────────────────────►  FILE SU DISCO
   │         │                                                              dati.bin
   │    fwrite(&struct, sizeof, n, fp)  ────────────────────────────►   [raw bytes...]
   │         │
   │    fclose(fp)
   │
   └─► fopen("dati.bin", "rb") ──────────────────────────────────────►  FILE SU DISCO
             │                                                              dati.bin
        fread(&struct, sizeof, MAX, fp) ◄──────────────────────────────  [raw bytes...]
             │
        fclose(fp)
             │
        usa i dati in memoria
```

### 1.2.7 Controllo errori — sempre obbligatorio

```c
FILE *fp = fopen("archivio.bin", "rb");
if (fp == NULL) {
    printf("Errore: impossibile aprire il file.\n");
    return 1;  // o exit(1)
}
```

---

## 1.3 Esempi di Codice Commentati

### Esempio 1 — Scrittura e lettura di testo con struct

```c
#include <stdio.h>
#include <string.h>

struct Studente {
    char nome[50];
    int  voto;
};

int main() {
    // --- SCRITTURA ---
    FILE *fp = fopen("studenti.txt", "w");
    if (fp == NULL) {
        printf("Errore apertura file in scrittura.\n");
        return 1;
    }

    struct Studente lista[3] = {
        {"Alice",  28},
        {"Bruno",  25},
        {"Carla",  30}
    };

    for (int i = 0; i < 3; i++) {
        fprintf(fp, "%s %d\n", lista[i].nome, lista[i].voto);
    }
    fclose(fp);
    printf("Scrittura completata.\n");

    // --- LETTURA ---
    fp = fopen("studenti.txt", "r");
    if (fp == NULL) {
        printf("Errore apertura file in lettura.\n");
        return 1;
    }

    struct Studente letto;
    printf("\nContenuto del file:\n");
    while (fscanf(fp, "%49s %d", letto.nome, &letto.voto) == 2) {
        printf("Nome: %-15s  Voto: %d\n", letto.nome, letto.voto);
    }
    fclose(fp);

    return 0;
}
```

**Output atteso:**
```
Scrittura completata.

Contenuto del file:
Nome: Alice            Voto: 28
Nome: Bruno            Voto: 25
Nome: Carla            Voto: 30
```

---

### Esempio 2 — Scrittura e lettura binaria di un array di struct

```c
#include <stdio.h>

#define MAX 100

struct Prodotto {
    char  nome[40];
    float prezzo;
    int   quantita;
};

void salva(struct Prodotto arr[], int n, const char *nome_file) {
    FILE *fp = fopen(nome_file, "wb");
    if (fp == NULL) {
        printf("Errore: impossibile creare il file.\n");
        return;
    }
    fwrite(&n, sizeof(int), 1, fp);
    fwrite(arr, sizeof(struct Prodotto), n, fp);
    fclose(fp);
    printf("Salvati %d prodotti.\n", n);
}

int carica(struct Prodotto arr[], const char *nome_file) {
    FILE *fp = fopen(nome_file, "rb");
    if (fp == NULL) {
        printf("File non trovato, archivio vuoto.\n");
        return 0;
    }
    int n = 0;
    fread(&n, sizeof(int), 1, fp);
    fread(arr, sizeof(struct Prodotto), n, fp);
    fclose(fp);
    printf("Caricati %d prodotti.\n", n);
    return n;
}

int main() {
    struct Prodotto magazzino[MAX];
    int n = 0;

    n = carica(magazzino, "magazzino.bin");

    struct Prodotto nuovo = {"Tastiera meccanica", 89.99f, 15};
    magazzino[n++] = nuovo;

    salva(magazzino, n, "magazzino.bin");

    printf("\n--- Inventario ---\n");
    for (int i = 0; i < n; i++) {
        printf("%-25s  €%.2f  qty:%d\n",
               magazzino[i].nome,
               magazzino[i].prezzo,
               magazzino[i].quantita);
    }

    return 0;
}
```

**Output atteso (prima esecuzione):**
```
File non trovato, archivio vuoto.
Salvati 1 prodotti.

--- Inventario ---
Tastiera meccanica         €89.99  qty:15
```

---

### Esempio 3 — Append su file di testo (log eventi)

```c
#include <stdio.h>
#include <time.h>

void registra_evento(const char *messaggio) {
    FILE *fp = fopen("log.txt", "a");
    if (fp == NULL) return;

    time_t ora = time(NULL);
    char timestamp[30];
    strftime(timestamp, sizeof(timestamp), "%Y-%m-%d %H:%M:%S", localtime(&ora));

    fprintf(fp, "[%s] %s\n", timestamp, messaggio);
    fclose(fp);
}

int main() {
    registra_evento("Programma avviato");
    registra_evento("Utente connesso: admin");
    registra_evento("Operazione completata");
    registra_evento("Programma terminato");

    printf("Log aggiornato. Contenuto:\n\n");

    FILE *fp = fopen("log.txt", "r");
    if (fp == NULL) return 1;
    char riga[200];
    while (fgets(riga, sizeof(riga), fp)) {
        printf("%s", riga);
    }
    fclose(fp);

    return 0;
}
```

**Output atteso (esempio):**
```
Log aggiornato. Contenuto:

[2025-03-15 10:23:41] Programma avviato
[2025-03-15 10:23:41] Utente connesso: admin
[2025-03-15 10:23:41] Operazione completata
[2025-03-15 10:23:41] Programma terminato
```

---

## 1.4 Riepilogo Visivo

```
┌─────────────────────────────────────────────────────────────────┐
│                  GESTIONE FILE IN C — RIEPILOGO                 │
├──────────────┬──────────────────────┬───────────────────────────┤
│ OPERAZIONE   │ TESTO                │ BINARIO                   │
├──────────────┼──────────────────────┼───────────────────────────┤
│ Apertura     │ fopen("f","r"/"w")   │ fopen("f","rb"/"wb")      │
│ Scrittura    │ fprintf(fp,fmt,...)  │ fwrite(&var,sz,n,fp)      │
│ Lettura      │ fscanf(fp,fmt,...)   │ fread(&var,sz,n,fp)       │
│ Riga intera  │ fgets / fputs        │ —                         │
│ Chiusura     │ fclose(fp)           │ fclose(fp)                │
├──────────────┼──────────────────────┼───────────────────────────┤
│ PRO          │ Leggibile con editor │ Compatto, veloce, preciso │
│ CONTRO       │ Parsing complesso    │ Non leggibile a occhio    │
└──────────────┴──────────────────────┴───────────────────────────┘

MODALITÀ fopen:
  "r"  solo lettura (file deve esistere)
  "w"  scrittura (sovrascrive o crea)
  "a"  append (aggiunge in fondo o crea)
  +b   versione binaria di ognuna

SEMPRE: controllare che fopen non restituisca NULL!
```

---

## 1.5 Domande di Verifica Orale

**D1:** Cosa succede se chiami `fopen("dati.txt", "w")` su un file che esiste già?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Il file viene svuotato (troncato a 0 byte) e riscritto da capo. Tutti i dati precedenti vengono persi. Per aggiungere senza cancellare si usa `"a"`.

</details>

---

**D2:** Qual è la differenza tra `fprintf` e `fwrite`?

<details>
<summary><b>💡 RISPOSTA</b></summary>

`fprintf` scrive dati in formato testuale leggibile (come printf su file). `fwrite` scrive i byte grezzi della memoria — più veloce e compatto ma non leggibile con un editor di testo.

</details>

---

**D3:** Perché è importante chiamare `fclose` dopo aver finito di usare un file?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Perché le operazioni di I/O usano buffer interni. Senza `fclose`, dati scritti con `fprintf`/`fwrite` potrebbero rimanere nel buffer e non essere effettivamente scritti su disco. Inoltre, lasciare file aperti spreca risorse di sistema.

</details>

---

**D4:** Come si riconosce la fine di un file durante la lettura con `fscanf`?

<details>
<summary><b>💡 RISPOSTA</b></summary>

`fscanf` restituisce il numero di campi letti con successo. Quando raggiunge la fine del file (o incontra un dato non valido), restituisce un valore inferiore al numero atteso (spesso `EOF` = -1). Si usa tipicamente `while (fscanf(...) == N_CAMPI)`.

</details>

---

**D5:** Qual è il vantaggio di salvare un array di struct con un singolo `fwrite` invece di un ciclo con `fprintf`?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Con `fwrite` si scrive l'intera area di memoria in un solo accesso al disco — più veloce. Con `fprintf` in un ciclo si scrivono tanti blocchi separati e i numeri vengono convertiti in testo. La lettura con `fread` è simmetrica: un solo accesso rilegge tutto l'array.

</details>

---

**D6:** Cosa stampa `fopen` se il file non esiste e si apre in modalità `"r"`?

<details>
<summary><b>💡 RISPOSTA</b></summary>

`fopen` non stampa nulla: restituisce `NULL`. È il programmatore che deve controllare il valore restituito e gestire l'errore.

</details>

---

**D7:** Se salvo una struct con `fwrite` su un computer e provo a leggerla con `fread` su un altro, è garantito che funzioni?

<details>
<summary><b>💡 RISPOSTA</b></summary>

Non necessariamente. I file binari dipendono dall'architettura (endianness, dimensione dei tipi, padding della struct). Per portabilità tra sistemi diversi si preferisce il formato testo. Tra macchine dello stesso tipo (es. tutti x86-64 con lo stesso compilatore) funziona.

</details>

---

# PARTE 2 — ESERCIZI (1 ora)

## 🟢 Esercizio 1 — Livello Base: Rubrica Telefonica su File di Testo

**Testo:**
Scrivi un programma che definisce una struct `Contatto` con campi `nome` (stringa, max 30 car.), `cognome` (stringa, max 30 car.) e `telefono` (stringa, max 15 car.). Il programma deve:
1. Creare un array di 3 contatti inseriti direttamente nel codice (hardcoded)
2. Salvarli su un file di testo `rubrica.txt`, uno per riga nel formato: `nome cognome telefono`
3. Rileggere il file e stampare a schermo i contatti letti

**Esempio input/output:**
```
Scrittura completata: 3 contatti salvati.

Lettura da file:
Mario Rossi 3331234567
Anna Bianchi 3479876543
Luca Verdi 3201112233
```

**💡 Hint:**
1. Usa `fprintf(fp, "%s %s %s\n", ...)` per scrivere ogni contatto
2. Usa `fscanf(fp, "%29s %29s %14s", ...)` per leggere — nota i limiti per sicurezza
3. Controlla sempre che `fopen` non restituisca `NULL`

**Output atteso:**
```
Scrittura completata: 3 contatti salvati.

Lettura da file:
Mario Rossi 3331234567
Anna Bianchi 3479876543
Luca Verdi 3201112233
```

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

struct Contatto {
    char nome[30];
    char cognome[30];
    char telefono[15];
};

int main() {
    struct Contatto rubrica[3] = {
        {"Mario",  "Rossi",   "3331234567"},
        {"Anna",   "Bianchi", "3479876543"},
        {"Luca",   "Verdi",   "3201112233"}
    };

    // Scrittura
    FILE *fp = fopen("rubrica.txt", "w");
    if (fp == NULL) {
        printf("Errore apertura file.\n");
        return 1;
    }
    for (int i = 0; i < 3; i++) {
        fprintf(fp, "%s %s %s\n",
                rubrica[i].nome,
                rubrica[i].cognome,
                rubrica[i].telefono);
    }
    fclose(fp);
    printf("Scrittura completata: 3 contatti salvati.\n\n");

    // Lettura
    fp = fopen("rubrica.txt", "r");
    if (fp == NULL) {
        printf("Errore apertura file.\n");
        return 1;
    }
    struct Contatto c;
    printf("Lettura da file:\n");
    while (fscanf(fp, "%29s %29s %14s", c.nome, c.cognome, c.telefono) == 3) {
        printf("%s %s %s\n", c.nome, c.cognome, c.telefono);
    }
    fclose(fp);

    return 0;
}
```

</details>

---

## 🟡 Esercizio 2 — Livello Intermedio: Archivio Libri Binario

**Testo:**
Crea un programma per gestire un piccolo archivio di libri. La struct `Libro` ha: `titolo` (60 car.), `autore` (40 car.), `anno` (int), `prezzo` (float). Il programma deve:
1. Definire un array di 4 libri con valori a piacere
2. Salvarlo in un file binario `libri.bin` (scrivi prima il numero di libri, poi l'array)
3. Ricaricare il file in un nuovo array e stampare tutti i libri con formattazione tabellare
4. Calcolare e stampare il prezzo medio

**Esempio input/output:**
```
Salvati 4 libri in libri.bin.

--- ARCHIVIO LIBRI ---
Titolo                        Autore              Anno    Prezzo
Il nome della rosa            Umberto Eco         1980    €12.50
1984                          George Orwell       1949    €8.90
Il Signore degli Anelli       J.R.R. Tolkien      1954    €18.00
Fondazione                    Isaac Asimov        1951    €10.00

Prezzo medio: €12.35
```

**💡 Hint:**
1. Scrivi prima `fwrite(&n, sizeof(int), 1, fp)` poi `fwrite(arr, sizeof(struct Libro), n, fp)`
2. In lettura, prima `fread(&n, sizeof(int), 1, fp)` poi `fread(arr, sizeof(struct Libro), n, fp)`
3. Per il prezzo medio: somma tutti i prezzi e dividi per n
4. Usa `%-30s` per allineare a sinistra le stringhe nella stampa

**Output atteso:**
```
Salvati 4 libri in libri.bin.

--- ARCHIVIO LIBRI ---
Titolo                         Autore               Anno    Prezzo
Il nome della rosa             Umberto Eco          1980    €12.50
1984                           George Orwell        1949    €8.90
Il Signore degli Anelli        J.R.R. Tolkien       1954    €18.00
Fondazione                     Isaac Asimov         1951    €10.00

Prezzo medio: €12.35
```

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

#define MAX 100

struct Libro {
    char  titolo[60];
    char  autore[40];
    int   anno;
    float prezzo;
};

int main() {
    struct Libro archivio[MAX];
    int n = 4;

    archivio[0] = (struct Libro){"Il nome della rosa",      "Umberto Eco",    1980, 12.50f};
    archivio[1] = (struct Libro){"1984",                    "George Orwell",  1949,  8.90f};
    archivio[2] = (struct Libro){"Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 18.00f};
    archivio[3] = (struct Libro){"Fondazione",              "Isaac Asimov",   1951, 10.00f};

    // Salvataggio binario
    FILE *fp = fopen("libri.bin", "wb");
    if (fp == NULL) { printf("Errore scrittura.\n"); return 1; }
    fwrite(&n, sizeof(int), 1, fp);
    fwrite(archivio, sizeof(struct Libro), n, fp);
    fclose(fp);
    printf("Salvati %d libri in libri.bin.\n\n", n);

    // Caricamento binario
    struct Libro caricati[MAX];
    int m = 0;
    fp = fopen("libri.bin", "rb");
    if (fp == NULL) { printf("Errore lettura.\n"); return 1; }
    fread(&m, sizeof(int), 1, fp);
    fread(caricati, sizeof(struct Libro), m, fp);
    fclose(fp);

    // Stampa tabellare
    printf("--- ARCHIVIO LIBRI ---\n");
    printf("%-30s %-20s %-6s  %s\n", "Titolo", "Autore", "Anno", "Prezzo");
    float somma = 0.0f;
    for (int i = 0; i < m; i++) {
        printf("%-30s %-20s %-6d  €%.2f\n",
               caricati[i].titolo,
               caricati[i].autore,
               caricati[i].anno,
               caricati[i].prezzo);
        somma += caricati[i].prezzo;
    }
    printf("\nPrezzo medio: €%.2f\n", somma / m);

    return 0;
}
```

</details>

---

## 🔴 Esercizio 3 — Livello Avanzato: Gestionale Studenti con Menu

**Testo:**
Realizza un programma completo con menu interattivo per gestire un archivio studenti persistente. La struct `Studente` ha: `matricola` (int), `nome` (40 car.), `cognome` (40 car.), `voto_medio` (float). Il file si chiama `studenti.bin`. Il menu deve offrire:
1. Visualizza tutti gli studenti
2. Aggiungi uno studente
3. Salva archivio su file
4. Cerca studente per matricola
0. Esci (con salvataggio automatico)

Il programma deve caricare automaticamente l'archivio all'avvio.

**Esempio input/output:**
```
=== GESTIONALE STUDENTI ===
Caricati 2 studenti da file.

1. Visualizza studenti
2. Aggiungi studente
3. Salva su file
4. Cerca per matricola
0. Esci
Scelta: 2

Matricola: 1003
Nome: Carlo
Cognome: Neri
Voto medio: 27.5
Studente aggiunto.

Scelta: 0
Salvati 3 studenti. Arrivederci!
```

**💡 Hint:**
1. Struttura il programma con funzioni separate: `carica()`, `salva()`, `visualizza()`, `aggiungi()`, `cerca()`
2. Usa un array globale o passa l'array e il contatore per indirizzo alle funzioni
3. Per la ricerca, scorri l'array confrontando `studenti[i].matricola == mat_cercata`
4. Il salvataggio automatico all'uscita evita che l'utente dimentichi di salvare

**Output atteso:** (vedi esempio input/output sopra)

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>
#include <string.h>

#define MAX 200
#define FILENAME "studenti.bin"

struct Studente {
    int   matricola;
    char  nome[40];
    char  cognome[40];
    float voto_medio;
};

struct Studente archivio[MAX];
int n = 0;

void carica() {
    FILE *fp = fopen(FILENAME, "rb");
    if (fp == NULL) {
        printf("Nessun archivio trovato, partenza vuota.\n");
        return;
    }
    fread(&n, sizeof(int), 1, fp);
    fread(archivio, sizeof(struct Studente), n, fp);
    fclose(fp);
    printf("Caricati %d studenti da file.\n", n);
}

void salva() {
    FILE *fp = fopen(FILENAME, "wb");
    if (fp == NULL) {
        printf("Errore salvataggio.\n");
        return;
    }
    fwrite(&n, sizeof(int), 1, fp);
    fwrite(archivio, sizeof(struct Studente), n, fp);
    fclose(fp);
    printf("Salvati %d studenti.\n", n);
}

void visualizza() {
    if (n == 0) { printf("Archivio vuoto.\n"); return; }
    printf("%-6s %-20s %-20s %s\n", "Matr.", "Nome", "Cognome", "Voto");
    for (int i = 0; i < n; i++) {
        printf("%-6d %-20s %-20s %.2f\n",
               archivio[i].matricola,
               archivio[i].nome,
               archivio[i].cognome,
               archivio[i].voto_medio);
    }
}

void aggiungi() {
    if (n >= MAX) { printf("Archivio pieno.\n"); return; }
    printf("Matricola: "); scanf("%d", &archivio[n].matricola);
    printf("Nome: ");      scanf("%39s", archivio[n].nome);
    printf("Cognome: ");   scanf("%39s", archivio[n].cognome);
    printf("Voto medio: "); scanf("%f", &archivio[n].voto_medio);
    n++;
    printf("Studente aggiunto.\n");
}

void cerca() {
    int mat;
    printf("Matricola da cercare: ");
    scanf("%d", &mat);
    for (int i = 0; i < n; i++) {
        if (archivio[i].matricola == mat) {
            printf("Trovato: %s %s — voto %.2f\n",
                   archivio[i].nome, archivio[i].cognome, archivio[i].voto_medio);
            return;
        }
    }
    printf("Studente con matricola %d non trovato.\n", mat);
}

int main() {
    printf("=== GESTIONALE STUDENTI ===\n");
    carica();

    int scelta;
    do {
        printf("\n1. Visualizza studenti\n2. Aggiungi studente\n3. Salva su file\n4. Cerca per matricola\n0. Esci\nScelta: ");
        scanf("%d", &scelta);
        switch (scelta) {
            case 1: visualizza(); break;
            case 2: aggiungi();   break;
            case 3: salva();      break;
            case 4: cerca();      break;
            case 0: salva(); printf("Arrivederci!\n"); break;
            default: printf("Scelta non valida.\n");
        }
    } while (scelta != 0);

    return 0;
}
```

</details>

---

# PARTE 3 — RECAP FINALE (5 min)

## 🎯 Recap finale (5 min)

- **File e persistenza:** i file permettono di conservare i dati tra un'esecuzione e l'altra del programma, salvandoli su disco tramite `fopen`, `fwrite`/`fprintf` e `fclose`.
- **Testo vs binario:** i file di testo usano `fprintf`/`fscanf` e sono leggibili con un editor; i file binari usano `fwrite`/`fread` e salvano i byte grezzi della memoria — più veloci e compatti.
- **Array di struct su file:** il pattern `fwrite(&n, ...) + fwrite(array, ...)` / `fread(&n, ...) + fread(array, ...)` è il modo standard per salvare e ricaricare interi archivi in C.
- **Controllo errori:** `fopen` restituisce `NULL` in caso di errore — controllare sempre prima di usare il puntatore al file.
- ⚠️ **Errore comune da evitare:** dimenticare `fclose()`. Dati scritti con `fprintf`/`fwrite` possono restare nel buffer interno e non essere scritti su disco se il file non viene chiuso correttamente.
- ➡️ **Prossima lezione (G17):** Esercitazione riepilogativa parte 1 — ripasseremo struct, array, funzioni e file combinando tutto in un mini-progetto guidato.



---

# esercizi ripasso lezione15

**File:** `esercizi ripasso lezione15.md`
**Tipo:** `.md`
**Dimensione:** 22.3 KB
**Ultima modifica:** 02/07/2026 09:24

---

# ESERCIZI DI RIPASSO - LEZIONE 15
## Funzioni: Parte 1

### TEMPO STIMATO: 1 ora

---

## Esercizio 1: Funzioni Base (15 minuti)

Crea un programma con le seguenti funzioni:

1. `int cubo(int n)` - ritorna il cubo di un numero
2. `float mediaAritmetica(float a, float b, float c)` - ritorna la media di tre numeri
3. `int massimo2(int a, int b)` - ritorna il massimo tra due numeri
4. `void stampaBordo(int lunghezza)` - stampa una linea di asterischi della lunghezza specificata

**Test nel main:**
```c
// Testa con:
// cubo(4) → 64
// mediaAritmetica(8.0, 6.0, 10.0) → 8.0
// massimo2(15, 23) → 23
// stampaBordo(30) → ******************************
```

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

// Prototipi
int cubo(int n);
float mediaAritmetica(float a, float b, float c);
int massimo2(int a, int b);
void stampaBordo(int lunghezza);

int main() {
    printf("=== TEST FUNZIONI BASE ===\n\n");
    
    // Test cubo
    printf("Cubo di 4: %d\n", cubo(4));
    printf("Cubo di -3: %d\n", cubo(-3));
    printf("Cubo di 10: %d\n\n", cubo(10));
    
    // Test media
    printf("Media di 8.0, 6.0, 10.0: %.2f\n", mediaAritmetica(8.0, 6.0, 10.0));
    printf("Media di 5.5, 7.2, 9.3: %.2f\n\n", mediaAritmetica(5.5, 7.2, 9.3));
    
    // Test massimo
    printf("Massimo tra 15 e 23: %d\n", massimo2(15, 23));
    printf("Massimo tra 100 e 50: %d\n", massimo2(100, 50));
    printf("Massimo tra -5 e -10: %d\n\n", massimo2(-5, -10));
    
    // Test bordo
    printf("Bordo di 30 caratteri:\n");
    stampaBordo(30);
    printf("\nBordo di 50 caratteri:\n");
    stampaBordo(50);
    
    return 0;
}

// Definizioni
int cubo(int n) {
    return n * n * n;
}

float mediaAritmetica(float a, float b, float c) {
    return (a + b + c) / 3.0;
}

int massimo2(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
    // Alternativa più compatta:
    // return (a > b) ? a : b;
}

void stampaBordo(int lunghezza) {
    for (int i = 0; i < lunghezza; i++) {
        printf("*");
    }
    printf("\n");
}
```

**Output atteso:**
```
=== TEST FUNZIONI BASE ===

Cubo di 4: 64
Cubo di -3: -27
Cubo di 10: 1000

Media di 8.0, 6.0, 10.0: 8.00
Media di 5.5, 7.2, 9.3: 7.33

Massimo tra 15 e 23: 23
Massimo tra 100 e 50: 100
Massimo tra -5 e -10: -5

Bordo di 30 caratteri:
******************************
Bordo di 50 caratteri:
**************************************************
```

</details>

---

## Esercizio 2: Validazione (15 minuti)

Crea funzioni di validazione che ritornano 1 (vero) o 0 (falso):

1. `int isMultiplo(int numero, int divisore)` - verifica se numero è multiplo di divisore
2. `int isCompreso(int n, int min, int max)` - verifica se n è compreso tra min e max (inclusi)
3. `int isVocale(char c)` - verifica se c è una vocale (a,e,i,o,u maiuscole o minuscole)
4. `int isBisestile(int anno)` - verifica se l'anno è bisestile

**Regola anno bisestile:** 
- Divisibile per 4 E non per 100, OPPURE divisibile per 400

**Test nel main:**
```c
// isMultiplo(15, 3) → 1 (vero)
// isMultiplo(15, 4) → 0 (falso)
// isCompreso(50, 1, 100) → 1
// isVocale('a') → 1
// isVocale('b') → 0
// isBisestile(2024) → 1
// isBisestile(1900) → 0
```

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

// Prototipi
int isMultiplo(int numero, int divisore);
int isCompreso(int n, int min, int max);
int isVocale(char c);
int isBisestile(int anno);

int main() {
    printf("=== TEST FUNZIONI DI VALIDAZIONE ===\n\n");
    
    // Test multiplo
    printf("15 è multiplo di 3? %s\n", isMultiplo(15, 3) ? "SI" : "NO");
    printf("15 è multiplo di 4? %s\n", isMultiplo(15, 4) ? "SI" : "NO");
    printf("100 è multiplo di 10? %s\n\n", isMultiplo(100, 10) ? "SI" : "NO");
    
    // Test compreso
    printf("50 è compreso tra 1 e 100? %s\n", isCompreso(50, 1, 100) ? "SI" : "NO");
    printf("150 è compreso tra 1 e 100? %s\n", isCompreso(150, 1, 100) ? "SI" : "NO");
    printf("-5 è compreso tra 0 e 10? %s\n\n", isCompreso(-5, 0, 10) ? "SI" : "NO");
    
    // Test vocale
    printf("'a' è una vocale? %s\n", isVocale('a') ? "SI" : "NO");
    printf("'E' è una vocale? %s\n", isVocale('E') ? "SI" : "NO");
    printf("'b' è una vocale? %s\n", isVocale('b') ? "SI" : "NO");
    printf("'x' è una vocale? %s\n\n", isVocale('x') ? "SI" : "NO");
    
    // Test bisestile
    printf("2024 è bisestile? %s\n", isBisestile(2024) ? "SI" : "NO");
    printf("1900 è bisestile? %s\n", isBisestile(1900) ? "SI" : "NO");
    printf("2000 è bisestile? %s\n", isBisestile(2000) ? "SI" : "NO");
    printf("2023 è bisestile? %s\n", isBisestile(2023) ? "SI" : "NO");
    
    return 0;
}

// Definizioni
int isMultiplo(int numero, int divisore) {
    if (divisore == 0) {
        return 0;  // Non è possibile dividere per zero
    }
    return (numero % divisore == 0);
}

int isCompreso(int n, int min, int max) {
    return (n >= min && n <= max);
}

int isVocale(char c) {
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
}

int isBisestile(int anno) {
    // Un anno è bisestile se:
    // - è divisibile per 4 E non per 100
    // OPPURE
    // - è divisibile per 400
    
    if (anno % 400 == 0) {
        return 1;  // Divisibile per 400 → bisestile
    }
    if (anno % 100 == 0) {
        return 0;  // Divisibile per 100 ma non per 400 → non bisestile
    }
    if (anno % 4 == 0) {
        return 1;  // Divisibile per 4 → bisestile
    }
    return 0;  // Non bisestile
}
```

**Output atteso:**
```
=== TEST FUNZIONI DI VALIDAZIONE ===

15 è multiplo di 3? SI
15 è multiplo di 4? NO
100 è multiplo di 10? SI

50 è compreso tra 1 e 100? SI
150 è compreso tra 1 e 100? NO
-5 è compreso tra 0 e 10? NO

'a' è una vocale? SI
'E' è una vocale? SI
'b' è una vocale? NO
'x' è una vocale? NO

2024 è bisestile? SI
1900 è bisestile? NO
2000 è bisestile? SI
2023 è bisestile? NO
```

</details>

---

## Esercizio 3: Funzioni per Array (15 minuti)

Crea le seguenti funzioni per lavorare con array:

1. `int contaDispari(int arr[], int dim)` - conta quanti numeri dispari ci sono nell'array
2. `int sommaPositivi(int arr[], int dim)` - somma solo i numeri positivi dell'array
3. `void stampaPari(int arr[], int dim)` - stampa solo i numeri pari dell'array
4. `int trovaIndiceMax(int arr[], int dim)` - ritorna l'indice del valore massimo

**Test con array:**
```c
int numeri[] = {-5, 12, 7, -3, 8, 15, 4, -10, 9};
```

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

// Prototipi
int contaDispari(int arr[], int dim);
int sommaPositivi(int arr[], int dim);
void stampaPari(int arr[], int dim);
int trovaIndiceMax(int arr[], int dim);
void stampaArray(int arr[], int dim);

int main() {
    int numeri[] = {-5, 12, 7, -3, 8, 15, 4, -10, 9};
    int dim = 9;
    
    printf("=== ARRAY ORIGINALE ===\n");
    stampaArray(numeri, dim);
    printf("\n");
    
    // Test conta dispari
    printf("Numeri dispari: %d\n", contaDispari(numeri, dim));
    
    // Test somma positivi
    printf("Somma dei positivi: %d\n", sommaPositivi(numeri, dim));
    
    // Test stampa pari
    printf("Numeri pari: ");
    stampaPari(numeri, dim);
    printf("\n");
    
    // Test indice massimo
    int indiceMax = trovaIndiceMax(numeri, dim);
    printf("Indice del massimo: %d (valore = %d)\n", indiceMax, numeri[indiceMax]);
    
    return 0;
}

// Definizioni
int contaDispari(int arr[], int dim) {
    int conta = 0;
    for (int i = 0; i < dim; i++) {
        if (arr[i] % 2 != 0) {
            conta++;
        }
    }
    return conta;
}

int sommaPositivi(int arr[], int dim) {
    int somma = 0;
    for (int i = 0; i < dim; i++) {
        if (arr[i] > 0) {
            somma += arr[i];
        }
    }
    return somma;
}

void stampaPari(int arr[], int dim) {
    printf("[ ");
    for (int i = 0; i < dim; i++) {
        if (arr[i] % 2 == 0) {
            printf("%d ", arr[i]);
        }
    }
    printf("]");
}

int trovaIndiceMax(int arr[], int dim) {
    if (dim == 0) {
        return -1;  // Array vuoto
    }
    
    int indiceMax = 0;
    for (int i = 1; i < dim; i++) {
        if (arr[i] > arr[indiceMax]) {
            indiceMax = i;
        }
    }
    return indiceMax;
}

void stampaArray(int arr[], int dim) {
    printf("[ ");
    for (int i = 0; i < dim; i++) {
        printf("%d ", arr[i]);
    }
    printf("]\n");
}
```

**Output atteso:**
```
=== ARRAY ORIGINALE ===
[ -5 12 7 -3 8 15 4 -10 9 ]

Numeri dispari: 5
Somma dei positivi: 55
Numeri pari: [ 12 8 4 -10 ]
Indice del massimo: 5 (valore = 15)
```

</details>

---

## Esercizio 4: Calcolatrice Modulare (15 minuti)

Crea una calcolatrice con le seguenti funzioni:

1. `float somma(float a, float b)`
2. `float sottrazione(float a, float b)`
3. `float moltiplicazione(float a, float b)`
4. `float divisione(float a, float b)` - gestire divisione per zero
5. `void stampaMenu()` - stampa il menu delle operazioni
6. `void eseguiOperazione(int scelta, float a, float b)` - esegue l'operazione scelta

Il main deve mostrare un menu e permettere all'utente di scegliere l'operazione.

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

// Prototipi
float somma(float a, float b);
float sottrazione(float a, float b);
float moltiplicazione(float a, float b);
float divisione(float a, float b);
void stampaMenu();
void eseguiOperazione(int scelta, float a, float b);

int main() {
    int scelta;
    float num1, num2;
    
    do {
        stampaMenu();
        printf("Scelta: ");
        scanf("%d", &scelta);
        
        if (scelta >= 1 && scelta <= 4) {
            printf("Inserisci il primo numero: ");
            scanf("%f", &num1);
            printf("Inserisci il secondo numero: ");
            scanf("%f", &num2);
            
            eseguiOperazione(scelta, num1, num2);
        } else if (scelta != 0) {
            printf("Scelta non valida!\n");
        }
        
        printf("\n");
        
    } while (scelta != 0);
    
    printf("Arrivederci!\n");
    return 0;
}

// Definizioni
float somma(float a, float b) {
    return a + b;
}

float sottrazione(float a, float b) {
    return a - b;
}

float moltiplicazione(float a, float b) {
    return a * b;
}

float divisione(float a, float b) {
    if (b == 0) {
        printf("ERRORE: Divisione per zero!\n");
        return 0;
    }
    return a / b;
}

void stampaMenu() {
    printf("============================\n");
    printf("      CALCOLATRICE\n");
    printf("============================\n");
    printf("1. Somma\n");
    printf("2. Sottrazione\n");
    printf("3. Moltiplicazione\n");
    printf("4. Divisione\n");
    printf("0. Esci\n");
    printf("============================\n");
}

void eseguiOperazione(int scelta, float a, float b) {
    float risultato;
    char operazione;
    
    switch (scelta) {
        case 1:
            risultato = somma(a, b);
            operazione = '+';
            printf("%.2f %c %.2f = %.2f\n", a, operazione, b, risultato);
            break;
        case 2:
            risultato = sottrazione(a, b);
            operazione = '-';
            printf("%.2f %c %.2f = %.2f\n", a, operazione, b, risultato);
            break;
        case 3:
            risultato = moltiplicazione(a, b);
            operazione = '*';
            printf("%.2f %c %.2f = %.2f\n", a, operazione, b, risultato);
            break;
        case 4:
            risultato = divisione(a, b);
            operazione = '/';
            if (b != 0) {
                printf("%.2f %c %.2f = %.2f\n", a, operazione, b, risultato);
            }
            break;
        default:
            printf("Operazione non valida!\n");
    }
}
```

**Esempio di esecuzione:**
```
============================
      CALCOLATRICE
============================
1. Somma
2. Sottrazione
3. Moltiplicazione
4. Divisione
0. Esci
============================
Scelta: 1
Inserisci il primo numero: 15.5
Inserisci il secondo numero: 4.5
15.50 + 4.50 = 20.00

============================
      CALCOLATRICE
============================
...
Scelta: 4
Inserisci il primo numero: 10
Inserisci il secondo numero: 0
ERRORE: Divisione per zero!

...
Scelta: 0
Arrivederci!
```

</details>

---

## Esercizio Sfida: Statistiche Complete (Bonus, 20 minuti)

Crea un programma che analizza un array di voti (0-100) con le seguenti funzioni:

1. `float calcolaMedia(int voti[], int dim)`
2. `int contaPromozioni(int voti[], int dim)` - conta voti >= 60
3. `int contaEccellenze(int voti[], int dim)` - conta voti >= 90
4. `int trovaVotoMinimo(int voti[], int dim)`
5. `int trovaVotoMassimo(int voti[], int dim)`
6. `void stampaStatistiche(int voti[], int dim)` - usa tutte le funzioni precedenti

**Array di test:**
```c
int voti[] = {75, 45, 92, 88, 55, 100, 72, 38, 95, 68, 50, 85};
```

<details>
<summary><b>💡 SOLUZIONE</b></summary>

```c
#include <stdio.h>

// Prototipi
float calcolaMedia(int voti[], int dim);
int contaPromozioni(int voti[], int dim);
int contaEccellenze(int voti[], int dim);
int trovaVotoMinimo(int voti[], int dim);
int trovaVotoMassimo(int voti[], int dim);
void stampaStatistiche(int voti[], int dim);
void stampaVoti(int voti[], int dim);

int main() {
    int voti[] = {75, 45, 92, 88, 55, 100, 72, 38, 95, 68, 50, 85};
    int dim = 12;
    
    printf("=== ANALISI VOTI CLASSE ===\n\n");
    
    printf("Voti registrati:\n");
    stampaVoti(voti, dim);
    printf("\n");
    
    stampaStatistiche(voti, dim);
    
    return 0;
}

// Definizioni
float calcolaMedia(int voti[], int dim) {
    if (dim == 0) return 0.0;
    
    int somma = 0;
    for (int i = 0; i < dim; i++) {
        somma += voti[i];
    }
    return (float)somma / dim;
}

int contaPromozioni(int voti[], int dim) {
    int conta = 0;
    for (int i = 0; i < dim; i++) {
        if (voti[i] >= 60) {
            conta++;
        }
    }
    return conta;
}

int contaEccellenze(int voti[], int dim) {
    int conta = 0;
    for (int i = 0; i < dim; i++) {
        if (voti[i] >= 90) {
            conta++;
        }
    }
    return conta;
}

int trovaVotoMinimo(int voti[], int dim) {
    if (dim == 0) return 0;
    
    int min = voti[0];
    for (int i = 1; i < dim; i++) {
        if (voti[i] < min) {
            min = voti[i];
        }
    }
    return min;
}

int trovaVotoMassimo(int voti[], int dim) {
    if (dim == 0) return 0;
    
    int max = voti[0];
    for (int i = 1; i < dim; i++) {
        if (voti[i] > max) {
            max = voti[i];
        }
    }
    return max;
}

void stampaStatistiche(int voti[], int dim) {
    printf("========================================\n");
    printf("          STATISTICHE CLASSE\n");
    printf("========================================\n");
    printf("Numero studenti:      %d\n", dim);
    printf("Media classe:         %.2f\n", calcolaMedia(voti, dim));
    printf("Voto minimo:          %d\n", trovaVotoMinimo(voti, dim));
    printf("Voto massimo:         %d\n", trovaVotoMassimo(voti, dim));
    printf("Promozioni (>=60):    %d (%.1f%%)\n", 
           contaPromozioni(voti, dim),
           (float)contaPromozioni(voti, dim) / dim * 100);
    printf("Eccellenze (>=90):    %d (%.1f%%)\n", 
           contaEccellenze(voti, dim),
           (float)contaEccellenze(voti, dim) / dim * 100);
    printf("Bocciature (<60):     %d (%.1f%%)\n", 
           dim - contaPromozioni(voti, dim),
           (float)(dim - contaPromozioni(voti, dim)) / dim * 100);
    printf("========================================\n");
}

void stampaVoti(int voti[], int dim) {
    printf("[ ");
    for (int i = 0; i < dim; i++) {
        printf("%d ", voti[i]);
    }
    printf("]\n");
}
```

**Output atteso:**
```
=== ANALISI VOTI CLASSE ===

Voti registrati:
[ 75 45 92 88 55 100 72 38 95 68 50 85 ]

========================================
          STATISTICHE CLASSE
========================================
Numero studenti:      12
Media classe:         71.92
Voto minimo:          38
Voto massimo:         100
Promozioni (>=60):    9 (75.0%)
Eccellenze (>=90):    3 (25.0%)
Bocciature (<60):     3 (25.0%)
========================================
```

</details>

---

## Domande di Verifica

1. Qual è la differenza tra **dichiarazione** e **definizione** di una funzione?

2. Cosa significa **passaggio per valore**? Cosa succede alle variabili originali?

3. Quando è obbligatorio usare `return` in una funzione?

4. Cosa succede se provi a usare il valore ritornato da una funzione `void`?

5. Come si passano gli array alle funzioni? Gli array seguono il passaggio per valore?

---

<details>
<summary><b>📝 RISPOSTE ALLE DOMANDE</b></summary>

### 1. Differenza tra dichiarazione e definizione

**DICHIARAZIONE (prototipo):**
- Dice al compilatore che la funzione esiste
- Specifica solo la firma: tipo di ritorno, nome, parametri
- Termina con punto e virgola `;`
- Di solito si mette all'inizio del file

```c
int somma(int a, int b);  // DICHIARAZIONE
```

**DEFINIZIONE:**
- Implementa effettivamente la funzione
- Include il corpo della funzione tra `{}`
- Contiene il codice che viene eseguito

```c
int somma(int a, int b) {  // DEFINIZIONE
    return a + b;
}
```

**In sintesi:**
- Dichiarazione = "questa funzione esiste"
- Definizione = "ecco come funziona"

---

### 2. Passaggio per valore

**Passaggio per valore** significa che quando passi una variabile a una funzione, la funzione riceve una **copia** del valore, NON la variabile originale.

**Conseguenze:**
- Modificare il parametro dentro la funzione NON modifica la variabile originale
- La variabile originale rimane invariata

**Esempio:**
```c
void incrementa(int x) {
    x = x + 1;
    printf("Dentro: %d\n", x);  // Stampa 11
}

int main() {
    int numero = 10;
    incrementa(numero);
    printf("Fuori: %d\n", numero);  // Stampa 10 (NON è cambiato!)
    return 0;
}
```

**Cosa succede:**
1. `numero` vale 10
2. Viene creata una **copia** di `numero` chiamata `x`
3. La funzione modifica `x` (la copia), non `numero`
4. Quando la funzione termina, `x` viene distrutta
5. `numero` rimane 10

**Per modificare la variabile originale:**
- Devi usare i **puntatori** (argomento futuro)
- Oppure ritornare il nuovo valore: `numero = incrementa(numero);`

---

### 3. Quando è obbligatorio usare `return`

**È OBBLIGATORIO usare `return`:**
- In tutte le funzioni che hanno un tipo di ritorno **diverso da `void`**
- Ogni percorso di esecuzione deve avere un `return`

**Esempi:**

```c
// ✅ CORRETTO
int somma(int a, int b) {
    return a + b;  // Obbligatorio!
}

// ❌ ERRORE: manca return
int massimo(int a, int b) {
    if (a > b) {
        return a;
    }
    // ERRORE: manca return per il caso else!
}

// ✅ CORRETTO
int massimo(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;  // Tutti i percorsi hanno return
    }
}
```

**NON è obbligatorio `return` in funzioni `void`:**
```c
void stampa(int n) {
    printf("%d\n", n);
    // Non serve return
}

// Ma puoi usare return per uscire anticipatamente
void stampaSePositivo(int n) {
    if (n < 0) {
        return;  // Esce subito (senza valore)
    }
    printf("%d\n", n);
}
```

**Cosa succede se manca `return`?**
- Comportamento **indefinito** (undefined behavior)
- Il programma potrebbe compilare ma dare risultati casuali
- È un bug grave!

---

### 4. Usare il valore di una funzione `void`

**Cosa succede:**
- Ottieni un **errore di compilazione**
- Le funzioni `void` NON ritornano alcun valore
- Non puoi assegnare il "risultato" a una variabile

**Esempi:**

```c
void stampaMessaggio() {
    printf("Ciao!\n");
}

int main() {
    // ❌ ERRORE: void non ritorna niente!
    int x = stampaMessaggio();
    
    // ❌ ERRORE: non puoi usare void in espressioni
    printf("%d\n", stampaMessaggio());
    
    // ✅ CORRETTO: chiama la funzione senza usare il "risultato"
    stampaMessaggio();
    
    return 0;
}
```

**Errore del compilatore:**
```
error: void value not ignored as it ought to be
```

**Quando usare `void`:**
- Funzioni che eseguono azioni (stampa, modifica array, ecc.)
- Funzioni che non producono un risultato da ritornare
- Funzioni che modificano parametri tramite puntatori (argomento futuro)

---

### 5. Passaggio degli array alle funzioni

**Gli array NON seguono il passaggio per valore!**

Quando passi un array a una funzione:
- La funzione riceve un **puntatore** al primo elemento
- NON viene creata una copia dell'intero array
- Le modifiche all'array **sono permanenti**

**Esempio:**

```c
void raddoppiaArray(int arr[], int dim) {
    for (int i = 0; i < dim; i++) {
        arr[i] *= 2;  // Modifica l'array originale!
    }
}

int main() {
    int numeri[] = {1, 2, 3, 4, 5};
    
    raddoppiaArray(numeri, 5);
    
    // numeri è ora {2, 4, 6, 8, 10}
    // L'array originale è stato modificato!
    
    for (int i = 0; i < 5; i++) {
        printf("%d ", numeri[i]);  // Stampa: 2 4 6 8 10
    }
    
    return 0;
}
```

**Perché questo comportamento?**
- Gli array sono molto grandi
- Copiare un array intero sarebbe lento e spreca memoria
- C passa automaticamente il **puntatore** all'array

**Conseguenze importanti:**

1. **Le funzioni possono modificare gli array:**
   ```c
   void azzeraArray(int arr[], int dim) {
       for (int i = 0; i < dim; i++) {
           arr[i] = 0;  // Modifica permanente
       }
   }
   ```

2. **Devi sempre passare la dimensione:**
   ```c
   // ❌ SBAGLIATO: la funzione non sa quanto è grande l'array
   void stampa(int arr[]) {
       // Quanto è grande arr? Non lo sappiamo!
   }
   
   // ✅ CORRETTO: passa sempre la dimensione
   void stampa(int arr[], int dim) {
       for (int i = 0; i < dim; i++) {
           printf("%d ", arr[i]);
       }
   }
   ```

3. **Non puoi ritornare array locali:**
   ```c
   // ❌ ERRORE GRAVE!
   int* creaArray() {
       int arr[5] = {1, 2, 3, 4, 5};
       return arr;  // ERRORE: arr viene distrutto!
   }
   ```

**Riepilogo:**
- Variabili semplici (int, float, char): **passaggio per valore** (copia)
- Array: **passaggio per riferimento** (puntatore, nessuna copia)
- Le modifiche agli array sono permanenti
- Devi sempre passare la dimensione insieme all'array

</details>

---

## Checklist Concetti

Prima di passare alla Lezione 16, assicurati di aver compreso:

- ✅ Come definire e dichiarare funzioni
- ✅ La differenza tra parametri formali e attuali
- ✅ Come funziona il `return`
- ✅ Il concetto di passaggio per valore
- ✅ Come lavorare con array nelle funzioni
- ✅ Lo scope delle variabili (locali vs globali)
- ✅ L'utilità delle funzioni `void`

---

**Ottimo lavoro! Ora sei pronto per la Lezione 16! 🚀**



---

# guida didattica lezione16

**File:** `guida didattica lezione16.md`
**Tipo:** `.md`
**Dimensione:** 19.2 KB
**Ultima modifica:** 02/07/2026 09:24

---

# GUIDA DIDATTICA - LEZIONE 16
## Funzioni: Parte 2 (Ricorsione, Prototipazione, Best Practices)

### DURATA TOTALE: 4 ORE

---

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

---

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

---

## PARTE 2: TEORIA LEZIONE 16 (90 minuti)

### 2.1 FUNZIONI RICORSIVE (35 minuti)

**Introduzione (5 min):**
> "Una funzione ricorsiva è come le matrioske russe: ogni funzione contiene una versione più piccola di sé stessa!"

**Concetti fondamentali:**
1. **Caso base**: condizione di uscita (SEMPRE necessario!)
2. **Caso ricorsivo**: chiamata a sé stessa con parametri ridotti

**Esempio 1: Fattoriale (10 min)**

esempio:
```
5! = 5 × 4!
   = 5 × 4 × 3!
   = 5 × 4 × 3 × 2!
   = 5 × 4 × 3 × 2 × 1!
   = 5 × 4 × 3 × 2 × 1
   = 120
```

codice:
```c
int fattoriale(int n) {
    // Caso base: STOP!
    if (n == 0 || n == 1) {
        return 1;
    }
    // Caso ricorsivo: chiama sé stessa
    return n * fattoriale(n - 1);
}
```

**Visualizzazione dello stack (10 min):**

Stack per `fattoriale(5)`:
```
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

Poi risale:
fattoriale(2) ritorna 2 × 1 = 2
fattoriale(3) ritorna 3 × 2 = 6
fattoriale(4) ritorna 4 × 6 = 24
fattoriale(5) ritorna 5 × 24 = 120
```

**⚠️ ATTENZIONE: Errori comuni (5 min)**

Cosa NON fare:
```c
// ERRORE 1: Manca il caso base
int sbagliata(int n) {
    return n * sbagliata(n - 1);  // Ricorsione infinita!
}

// ERRORE 2: Caso base irraggiungibile
int sbagliata2(int n) {
    if (n == 0) return 0;
    return n + sbagliata2(n + 1);  // n aumenta invece di diminuire!
}
```

**Esempio 2: Somma primi N numeri (5 min)**

```c
int somma(int n) {
    if (n == 0) return 0;         // Caso base
    return n + somma(n - 1);      // Caso ricorsivo
}

// somma(5) = 5 + somma(4)
//          = 5 + 4 + somma(3)
//          = 5 + 4 + 3 + 2 + 1 + 0
//          = 15
```

**🎯 ESERCIZIO RAPIDO DA FARE INSIEME:**
"Scriviamo insieme una funzione ricorsiva per calcolare la potenza: `pow(base, esp)`"

Soluzione:
```c
int potenza(int base, int esp) {
    if (esp == 0) return 1;              // Qualsiasi numero^0 = 1
    return base * potenza(base, esp - 1);
}
```

---

### 2.2 PROTOTIPAZIONE (20 minuti)

**Motivazione (5 min):**

Problema:
```c
// Questo NON compila!
int main() {
    int risultato = somma(5, 3);  // ERRORE: somma non è ancora stata dichiarata
    return 0;
}

int somma(int a, int b) {
    return a + b;
}
```

**Soluzione: Prototipazione (5 min)**

```c
// PROTOTIPO (dichiarazione)
int somma(int a, int b);

// Main può stare in alto
int main() {
    int risultato = somma(5, 3);  // OK!
    return 0;
}

// DEFINIZIONE (implementazione)
int somma(int a, int b) {
    return a + b;
}
```

**Vantaggi della prototipazione:**
1. Main() in alto → più leggibile
2. Funzioni che si chiamano a vicenda
3. Separazione interfaccia/implementazione
4. Preparazione per header files (.h)

**Ricorsione mutua (10 min):**

```c
// Senza prototipi: ERRORE!
int pari(int n) {
    if (n == 0) return 1;
    return dispari(n - 1);  // ERRORE: dispari non dichiarata!
}

int dispari(int n) {
    if (n == 0) return 0;
    return pari(n - 1);
}
```

```c
// Con prototipi: OK!
int pari(int n);      // Prototipo
int dispari(int n);   // Prototipo

int pari(int n) {
    if (n == 0) return 1;
    return dispari(n - 1);  // OK!
}

int dispari(int n) {
    if (n == 0) return 0;
    return pari(n - 1);     // OK!
}
```

---

### 2.3 FUNZIONI VOID AVANZATE (15 minuti)

**Richiamo concetto (3 min):**
- void = nessun valore di ritorno
- Utili per: stampa, modifica array, operazioni

**Esempi pratici (7 min):**

```c
// 1. Stampa formattata
void stampaIntestazione(char titolo[]) {
    printf("\n");
    printf("================================\n");
    printf("  %s\n", titolo);
    printf("================================\n");
}

// 2. Modifica array
void azzeraArray(int arr[], int dim) {
    for (int i = 0; i < dim; i++) {
        arr[i] = 0;
    }
}

// 3. Return anticipato
void stampaSePositivo(int n) {
    if (n <= 0) {
        printf("Numero non valido!\n");
        return;  // Esce subito
    }
    printf("Numero valido: %d\n", n);
}
```

**💡 IMPORTANTE (5 min):**

> "Le funzioni void NON ritornano valori, ma possono MODIFICARE gli array che ricevono come parametri!"

Esempio:
```c
void raddoppiaValori(int arr[], int dim) {
    for (int i = 0; i < dim; i++) {
        arr[i] *= 2;
    }
}

int main() {
    int numeri[] = {1, 2, 3, 4, 5};
    raddoppiaValori(numeri, 5);
    // numeri è ora {2, 4, 6, 8, 10}
}
```

---

### 2.4 VARIABILI STATIC (10 minuti)

**Introduzione (3 min):**
> "Le variabili static sono come la memoria di una funzione: ricordano il loro valore tra una chiamata e l'altra!"

**Esempio contatore (4 min):**

```c
void contatoreNormale() {
    int contatore = 0;  // Ricomincia da 0 ogni volta
    contatore++;
    printf("Chiamata #%d\n", contatore);
}

void contatoreStatic() {
    static int contatore = 0;  // Si inizializza UNA SOLA VOLTA
    contatore++;
    printf("Chiamata #%d\n", contatore);
}

int main() {
    contatoreNormale();  // Stampa: 1
    contatoreNormale();  // Stampa: 1 (riparte da 0!)
    contatoreNormale();  // Stampa: 1
    
    printf("\n");
    
    contatoreStatic();   // Stampa: 1
    contatoreStatic();   // Stampa: 2
    contatoreStatic();   // Stampa: 3 (ricorda il valore!)
}
```

**Quando usare static (3 min):**
- Contatori di chiamate
- Cache/memoization
- Generatori di ID univoci
- Stato interno della funzione

---

### 2.5 BEST PRACTICES (10 minuti)

**1. Nomi significativi**
```c
// ❌ BAD
int f(int x, int y) { return x + y; }

// ✅ GOOD
int calcolaSomma(int addendo1, int addendo2) {
    return addendo1 + addendo2;
}
```

**2. Una funzione, un compito**
```c
// ❌ BAD: fa troppe cose
void gestisciUtente(char nome[], int eta) {
    printf("Nome: %s\n", nome);
    printf("Età: %d\n", eta);
    if (eta >= 18) {
        printf("Maggiorenne\n");
    }
    // calcoli complessi...
    // validazioni...
    // salvataggio...
}

// ✅ GOOD: funzioni separate
void stampaUtente(char nome[], int eta);
int isMaggiorenne(int eta);
void salvaUtente(char nome[], int eta);
```

**3. Validazione input**
```c
float dividi(float a, float b) {
    if (b == 0) {
        printf("ERRORE: divisione per zero!\n");
        return 0;
    }
    return a / b;
}
```

**4. Principio DRY (Don't Repeat Yourself)**
```c
// ❌ Codice ripetuto
printf("Area rettangolo 1: %d\n", base1 * altezza1);
printf("Area rettangolo 2: %d\n", base2 * altezza2);
printf("Area rettangolo 3: %d\n", base3 * altezza3);

// ✅ Usa una funzione
int calcolaArea(int base, int altezza) {
    return base * altezza;
}
```

**5. Principio KISS (Keep It Simple, Stupid)**
```c
// ❌ Troppo complesso
int isPari(int n) {
    if (n % 2 == 0) {
        return 1;
    } else {
        return 0;
    }
}

// ✅ Semplice e chiaro
int isPari(int n) {
    return n % 2 == 0;
}
```

---

## PARTE 3: PRATICA GUIDATA (60 minuti)

### Esercizio Guidato 1: Fibonacci Ricorsivo (15 min)

**Da fare insieme alla lavagna/schermo:**

```c
/*
Sequenza di Fibonacci:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

Regola:
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2)
*/

int fibonacci(int n) {
    // Casi base
    if (n == 0) return 0;
    if (n == 1) return 1;
    
    // Caso ricorsivo
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    printf("Sequenza di Fibonacci:\n");
    for (int i = 0; i <= 10; i++) {
        printf("fib(%d) = %d\n", i, fibonacci(i));
    }
    return 0;
}
```

**Discussione:**
- Disegnare l'albero delle chiamate per `fibonacci(5)`
- Far notare che calcola gli stessi valori più volte
- Introdurre il concetto di memoization (opzionale)

---

### Esercizio Guidato 2: Conta Cifre Ricorsivo (15 min)

**Problema:**
"Creiamo una funzione ricorsiva che conta quante cifre ha un numero"

**Ragionamento insieme:**
- 5 → 1 cifra
- 42 → 2 cifre
- 123 → 3 cifre

**Approccio ricorsivo:**
- Caso base: n < 10 → 1 cifra
- Caso ricorsivo: conta 1 + cifre(n/10)

**Soluzione:**
```c
int contaCifre(int n) {
    // Gestione numeri negativi
    if (n < 0) {
        n = -n;
    }
    
    // Caso base
    if (n < 10) {
        return 1;
    }
    
    // Caso ricorsivo
    return 1 + contaCifre(n / 10);
}

// Test
printf("123 ha %d cifre\n", contaCifre(123));     // 3
printf("5 ha %d cifre\n", contaCifre(5));         // 1
printf("9876 ha %d cifre\n", contaCifre(9876));   // 4
```

---

### Esercizio Guidato 3: Menu con Funzioni (30 min)

**Creare insieme un menu interattivo che usa tutte le tecniche:**

```c
#include <stdio.h>

// Prototipi
void stampaMenu();
int leggiScelta();
void eseguiScelta(int scelta);
int fattoriale(int n);
int fibonacci(int n);
int potenza(int base, int esp);
void stampaStatistiche();

// Variabile static per statistiche
static int totaleOperazioni = 0;

int main() {
    int scelta;
    
    do {
        stampaMenu();
        scelta = leggiScelta();
        eseguiScelta(scelta);
    } while (scelta != 0);
    
    printf("\nProgramma terminato.\n");
    stampaStatistiche();
    
    return 0;
}

void stampaMenu() {
    printf("\n================================\n");
    printf("   CALCOLATRICE RICORSIVA\n");
    printf("================================\n");
    printf("1. Fattoriale\n");
    printf("2. Fibonacci\n");
    printf("3. Potenza\n");
    printf("4. Statistiche\n");
    printf("0. Esci\n");
    printf("================================\n");
}

int leggiScelta() {
    int scelta;
    printf("Scelta: ");
    scanf("%d", &scelta);
    return scelta;
}

void eseguiScelta(int scelta) {
    int n, base, esp;
    
    switch (scelta) {
        case 1:
            printf("Inserisci n: ");
            scanf("%d", &n);
            printf("%d! = %d\n", n, fattoriale(n));
            totaleOperazioni++;
            break;
            
        case 2:
            printf("Inserisci n: ");
            scanf("%d", &n);
            printf("fib(%d) = %d\n", n, fibonacci(n));
            totaleOperazioni++;
            break;
            
        case 3:
            printf("Inserisci base: ");
            scanf("%d", &base);
            printf("Inserisci esponente: ");
            scanf("%d", &esp);
            printf("%d^%d = %d\n", base, esp, potenza(base, esp));
            totaleOperazioni++;
            break;
            
        case 4:
            stampaStatistiche();
            break;
            
        case 0:
            printf("Uscita...\n");
            break;
            
        default:
            printf("Scelta non valida!\n");
    }
}

int fattoriale(int n) {
    if (n == 0 || n == 1) return 1;
    return n * fattoriale(n - 1);
}

int fibonacci(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int potenza(int base, int esp) {
    if (esp == 0) return 1;
    return base * potenza(base, esp - 1);
}

void stampaStatistiche() {
    printf("\n=== STATISTICHE ===\n");
    printf("Operazioni eseguite: %d\n", totaleOperazioni);
}
```

---

## PARTE 4: ESERCIZI AUTONOMI (30 minuti)

**Assegna gli esercizi del file "esercizi_lezione16.md"**

**Organizzazione:**
- Esercizi 1-2: individuali (base)
- Esercizi 3-4: a coppie (intermedi)
- Esercizio sfida: per chi finisce prima

**Circola tra i banchi per:**
- Rispondere a domande
- Verificare la comprensione
- Aiutare chi è in difficoltà
- Sfidare chi è avanti

---

## CHIUSURA E DOMANDE (10 minuti)

### Riepilogo Rapido:

**Oggi abbiamo imparato:**
1. ✅ Le funzioni ricorsive (caso base + caso ricorsivo)
2. ✅ La prototipazione delle funzioni
3. ✅ Le funzioni void avanzate
4. ✅ Le variabili static
5. ✅ Le best practices

### Domande per verificare comprensione:

1. "Cosa succede se dimentichi il caso base in una funzione ricorsiva?"
2. "Perché usiamo i prototipi?"
3. "Qual è la differenza tra una variabile locale normale e una static?"

---

<details>
<summary><b>📝 RISPOSTE PER IL DOCENTE</b></summary>

### 1. Cosa succede senza caso base?

**Risposta attesa dagli studenti:**
- Si ottiene una ricorsione infinita
- La funzione continua a chiamare se stessa all'infinito
- Si esaurisce la memoria dello stack (stack overflow)
- Il programma va in crash con errore "Segmentation fault"

**Dimostrazione pratica da fare:**
```c
// Mostra questo codice ed eseguilo
int sbagliata(int n) {
    printf("n = %d\n", n);
    return n + sbagliata(n - 1);  // Nessun caso base!
}

int main() {
    sbagliata(5);
    return 0;
}

// Output:
// n = 5
// n = 4
// n = 3
// ...
// n = -9834
// ...
// Segmentation fault (core dumped)
```

**Approfondimento per gli studenti avanzati:**
- Lo stack ha dimensione limitata (tipicamente 1-8 MB)
- Ogni chiamata ricorsiva aggiunge un "frame" allo stack
- Quando lo stack si riempie → crash
- Alcuni linguaggi hanno "tail call optimization" che previene questo problema

---

### 2. Perché usiamo i prototipi?

**Risposta attesa dagli studenti:**
- Per poter chiamare funzioni prima di definirle
- Per tenere il main() in alto nel file
- Per permettere a funzioni di chiamarsi a vicenda

**Spiegazione completa da dare:**

**Motivo 1: Ordine di lettura del compilatore**
```c
// Senza prototipo: ERRORE!
int main() {
    somma(5, 3);  // ERRORE: somma non è ancora stata dichiarata!
    return 0;
}

int somma(int a, int b) {
    return a + b;
}

// Con prototipo: OK!
int somma(int a, int b);  // Prototipo

int main() {
    somma(5, 3);  // OK: il compilatore sa che somma esiste
    return 0;
}

int somma(int a, int b) {
    return a + b;
}
```

**Motivo 2: Organizzazione del codice**
- main() in alto → più facile da leggere
- Funzioni di utilità in basso
- Separazione tra "cosa fa" (prototipo) e "come lo fa" (definizione)

**Motivo 3: Ricorsione mutua**
```c
// Senza prototipi: impossibile!
int pari(int n) {
    if (n == 0) return 1;
    return dispari(n-1);  // ERRORE: dispari non dichiarata
}

int dispari(int n) {
    if (n == 0) return 0;
    return pari(n-1);
}

// Con prototipi: OK!
int pari(int n);     // Prototipi necessari
int dispari(int n);

int pari(int n) {
    if (n == 0) return 1;
    return dispari(n-1);  // OK!
}

int dispari(int n) {
    if (n == 0) return 0;
    return pari(n-1);     // OK!
}
```

**Motivo 4: Preparazione per file header (.h)**
- I prototipi vanno nei file .h
- Le definizioni vanno nei file .c
- Permette di creare librerie

---

### 3. Differenza tra variabile locale e static?

**Risposta attesa dagli studenti:**
- Variabile locale: si azzera ad ogni chiamata
- Variabile static: mantiene il valore tra le chiamate
- Static viene inizializzata una sola volta

**Dimostrazione pratica da fare insieme:**

```c
void contatoreNormale() {
    int conta = 0;        // Si ricrea ogni volta
    conta++;
    printf("Normale: %d\n", conta);
}

void contatoreStatic() {
    static int conta = 0; // Si inizializza UNA SOLA VOLTA
    conta++;
    printf("Static: %d\n", conta);
}

int main() {
    printf("=== VARIABILE NORMALE ===\n");
    contatoreNormale();  // Stampa: 1
    contatoreNormale();  // Stampa: 1 (ricomincia da 0!)
    contatoreNormale();  // Stampa: 1
    
    printf("\n=== VARIABILE STATIC ===\n");
    contatoreStatic();   // Stampa: 1
    contatoreStatic();   // Stampa: 2 (ricorda il valore!)
    contatoreStatic();   // Stampa: 3
    
    return 0;
}
```

**Tabella comparativa da mostrare:**

| Caratteristica | Variabile locale | Variabile static |
|----------------|------------------|------------------|
| **Inizializzazione** | Ad ogni chiamata | Una volta sola |
| **Durata** | Durante la funzione | Tutta l'esecuzione |
| **Valore iniziale** | Indeterminato* | 0 (default) |
| **Memoria** | Stack | Segmento dati |
| **Visibilità** | Solo nella funzione | Solo nella funzione |
| **Uso tipico** | Calcoli temporanei | Contatori, cache |

*Nota: variabili locali non inizializzate contengono "spazzatura"

**Casi d'uso pratici:**

1. **Contatore di chiamate**
```c
void logChiamata() {
    static int chiamate = 0;
    chiamate++;
    printf("Questa funzione è stata chiamata %d volte\n", chiamate);
}
```

2. **Generatore ID univoci**
```c
int generaID() {
    static int ultimoID = 0;
    ultimoID++;
    return ultimoID;
}

// Uso:
int id1 = generaID();  // 1
int id2 = generaID();  // 2
int id3 = generaID();  // 3
```

3. **Cache/Memoization**
```c
int fibonacci(int n) {
    static int cache[100];  // Mantiene i valori calcolati
    static int inizializzato = 0;
    
    if (!inizializzato) {
        for (int i = 0; i < 100; i++) cache[i] = -1;
        inizializzato = 1;
    }
    
    if (n <= 1) return n;
    if (cache[n] != -1) return cache[n];
    
    cache[n] = fibonacci(n-1) + fibonacci(n-2);
    return cache[n];
}
```

**Errore comune da evidenziare:**
```c
void sbagliata() {
    static int x = funzioneComplessa();  // ERRORE!
    // L'inizializzazione di static deve essere con valore costante!
}

void corretta() {
    static int x = 10;  // OK: valore costante
}
```

</details>

### Compiti per casa (opzionale):

- Completare tutti gli esercizi
- Provare a scrivere 3 funzioni ricorsive originali
- Refactoring di un vecchio programma usando le best practices

---

## NOTE PER IL DOCENTE

### ⚠️ Punti critici da monitorare:

1. **Ricorsione infinita**: molti studenti dimenticano il caso base
2. **Stack overflow**: far capire che la ricorsione ha limiti
3. **Confusione prototype/definizione**: ribadire la differenza
4. **Static**: concetto astratto, serve tempo

### 💡 Suggerimenti:

- Usa MOLTI disegni per la ricorsione (stack, alberi)
- Fai eseguire gli esempi passo-passo alla lavagna
- Collega i concetti a situazioni reali
- Incoraggia gli studenti a "pensare ricorsivamente"

### 📊 Valutazione comprensione:

- Chi scrive funzioni ricorsive corrette al primo tentativo: ottimo
- Chi le scrive con aiuto: buono
- Chi fatica con il caso base: serve rinforzo
- Chi non capisce la ricorsione: serve ripasso 1-1

### 🎯 Obiettivi raggiunti se gli studenti:

- ✅ Scrivono funzioni ricorsive con caso base
- ✅ Usano correttamente i prototipi
- ✅ Applicano le best practices
- ✅ Comprendono il concetto di static

---

**Buona lezione! 🚀**



---

# lezione 11 cicli

**File:** `lezione 11 cicli.pdf`
**Tipo:** `.pdf`
**Dimensione:** 76.0 KB
**Ultima modifica:** 02/07/2026 09:24

---

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
2. Ciclo while
Il ciclo while ripete un blocco di codice finché la condizione è vera. La condizione viene
verificata prima di ogni iterazione.
Sintassi:
• 
• 
• 
1. 
2. 
3. 
4. 
while(condizione){
// corpo del ciclo
// istruzioni da ripetere
}

Flowchart del while:
Esempio 1: Contare da 1 a 5
Esempio 2: Somma di numeri inseriti dall’utente
#include <stdio.h>
int main(){
int i =1; // Inizializzazione
while(i <=5){ // Condizione
        printf("%d\n", i);
        i++;// Aggiornamento
}
return0;
}

3. Ciclo do-while
Il ciclo do-while esegue il corpo almeno una volta, poi controlla la condizione. La
verifica avviene dopo ogni iterazione.
Sintassi:
Flowchart del do-while:
#include <stdio.h>
int main(){
int numero;
int somma =0;
    printf("Inserisci numeri (0 per terminare):\n");
    scanf("%d", &numero);
while(numero !=0){
        somma += numero;
        printf("Somma parziale: %d\n", somma);
        scanf("%d", &numero);
}
    printf("Somma totale: %d\n", somma);
return0;
}
do{
// corpo del ciclo
// istruzioni da ripetere
}while(condizione); // NOTA: il punto e virgola è obbligatorio!

Esempio: Menu con validazione
#include <stdio.h>
int main(){
int scelta;
do{
        printf("\n=== MENU ===\n");
        printf("1. Opzione A\n");
        printf("2. Opzione B\n");
        printf("3. Esci\n");
        printf("Scelta: ");
        scanf("%d", &scelta);
switch(scelta){
case1:
                printf("Hai scelto A\n");
break;

4. Differenze tra while e do-while
Caratteristica while do-while
Controllo
condizione Prima del corpo Dopo il corpo
Esecuzioni minime0 (può non eseguire mai)1 (esegue sempre almeno una
volta)
Uso tipico Quando non si sa se
eseguire
Quando serve almeno
un’esecuzione
Esempio comparativo:
case2:
                printf("Hai scelto B\n");
break;
case3:
                printf("Arrivederci!\n");
break;
default:
                printf("Scelta non valida!\n");
}
}while(scelta !=3);
return0;
}
// while - potrebbe non stampare nulla
int x =10;
while(x <5){
    printf("Questo non viene mai stampato\n");
    x++;
}

Quando usare do-while:
Menu interattivi
Validazione input (richiedi finché non è valido)
Quando serve almeno un’iterazione garantita
5. Cicli Infiniti e Condizioni di Uscita
Ciclo infinito (da evitare accidentalmente!):
Ciclo infinito intenzionale:
// do-while - stampa almeno una volta
int y =10;
do{
    printf("Questo viene stampato una volta: %d\n", y);
    y++;
}while(y <5);
• 
• 
• 
// ERRORE: condizione sempre vera
int i =1;
while(i >0){
    printf("Loop infinito!\n");
// Manca i++ o una condizione di uscita
}
// OK se gestito con break
while(1){ // o while(1) sempre vero
int input;
    printf("Inserisci numero (0 per uscire): ");
    scanf("%d", &input);
if(input ==0){

Errori comuni:
break; // Esce dal ciclo
}
    printf("Hai inserito: %d\n", input);
}
// ERRORE 1: dimenticare l'aggiornamento
int i =0;
while(i <10){
    printf("%d\n", i);
// Manca i++! Ciclo infinito
}
// ERRORE 2: punto e virgola dopo while
int i =0;
while(i <10); // ERRORE: corpo vuoto!
{
    printf("%d\n", i);
    i++;
}
// ERRORE 3: condizione sbagliata
int i =0;
while(i =5){ // ERRORE: assegnamento invece di confronto!
    printf("%d\n", i);
    i++;
}

PARTE PRATICA (2h)
Esercizio 1: Somma di numeri fino a condizione
Compito: Modifica il programma per trovare anche il massimo tra i numeri inseriti.
#include <stdio.h>
int main(){
int numero;
int somma =0;
int contatore =0;
    printf("Inserisci numeri positivi (numero negativo per terminare):\n");
    scanf("%d", &numero);
while(numero >=0){
        somma += numero;
        contatore++;
        printf("Inserisci un altro numero: ");
        scanf("%d", &numero);
}
if(contatore >0){
        printf("\nSomma: %d\n", somma);
        printf("Media: %.2f\n", (float)somma / contatore);
}else{
        printf("Nessun numero inserito.\n");
}
return0;
}

Esercizio 2: Validazione input con cicli
#include <stdio.h>
int main(){
int eta;
// Validazione con do-while
do{
        printf("Inserisci la tua età (0-120): ");
        scanf("%d", &eta);
if(eta <0|| eta >120){
            printf("Età non valida! Riprova.\n");
}
}while(eta <0|| eta >120);
    printf("Età valida: %d anni\n", eta);
// Classificazione
if(eta <18){
        printf("Sei minorenne\n");
}elseif(eta <65){
        printf("Sei adulto\n");
}else{
        printf("Sei senior\n");
}
return0;
}

Esercizio 3: Gioco “Indovina il numero”
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
int numeroSegreto, tentativo, tentativi =0;
// Inizializza il generatore di numeri casuali
    srand(time(NULL));
    numeroSegreto = rand()%100+1; // Numero tra 1 e 100
    printf("=== INDOVINA IL NUMERO ===\n");
    printf("Ho pensato un numero tra 1 e 100\n\n");
do{
        printf("Il tuo tentativo: ");
        scanf("%d", &tentativo);
        tentativi++;
if(tentativo < numeroSegreto){
            printf("Troppo basso! Riprova.\n");
}elseif(tentativo > numeroSegreto){
            printf("Troppo alto! Riprova.\n");
}else{
            printf("\n🎉 COMPLIMENTI! Hai indovinato in %d tentativi!\n",
tentativi);
}
}while(tentativo != numeroSegreto);
return0;
}

Esercizio 4: Calcolo del fattoriale
Compito: Riscrivi il programma usando un ciclo do-while.
Esercizi da svolgere autonomamente:
Contatore alla rovescia: Scrivi un programma che conta da 10 a 0 usando un
ciclo while
#include <stdio.h>
int main(){
int n, i;
longlong fattoriale =1;
    printf("Inserisci un numero: ");
    scanf("%d", &n);
if(n <0){
        printf("Il fattoriale non è definito per numeri negativi!\n");
}else{
// Versione con while
        i =1;
while(i <= n){
            fattoriale *= i;
            i++;
}
        printf("%d! = %lld\n", n, fattoriale);
}
return0;
}
1. 

Tabellina: Chiedi all’utente un numero e stampa la sua tabellina (da 1 a 10)
usando do-while
Somma pari e dispari: Inserisci numeri fino a 0, poi stampa la somma dei numeri
pari e quella dei dispari separatamente
Password: Crea un sistema che chiede una password e permette massimo 3
tentativi usando do-while
Sequenza Fibonacci: Stampa i primi N numeri della sequenza di Fibonacci
usando while
MCD (Massimo Comun Divisore): Calcola l’MCD di due numeri usando
l’algoritmo di Euclide con un ciclo while
Riepilogo Concetti Chiave
✓ Il while controlla la condizione prima di eseguire il corpo
✓ Il do-while esegue il corpo almeno una volta, poi controlla
✓ Ogni ciclo necessita di inizializzazione, condizione e aggiornamento
✓ Attenzione ai cicli infiniti accidentali
✓ do-while è ideale per menu e validazione input
Prossima lezione: Approfondiremo il ciclo for e i cicli annidati!
2. 
3. 
4. 
5. 
6. 


---

# lezione 12 for

**File:** `lezione 12 for.pdf`
**Tipo:** `.pdf`
**Dimensione:** 98.9 KB
**Ultima modifica:** 02/07/2026 09:28

---

LEZIONE 12 - Ciclo for
PARTE TEORICA (2h)
1. Ciclo for: sintassi e semantica
Il ciclo for è il ciclo più utilizzato quando si conosce in anticipo il numero di iterazioni da
eseguire. È particolarmente utile per contatori e iterazioni su sequenze.
Sintassi:
Componenti del for:
Inizializzazione: eseguita una sola volta all’inizio (es: i = 0)
Condizione: verificata prima di ogni iterazione (es: i < 10)
Aggiornamento: eseguito dopo ogni iterazione (es: i++)
Corpo: blocco di istruzioni da ripetere
Flowchart del for:
   ┌──────────────┐
   │Inizializzazione│
   └──────┬─────────┘
          │
    ┌─────▼──────┐
    │ Condizione? │
    └──────┬──────┘
           │
      ┌────┴────┐
for(inizializzazione; condizione; aggiornamento){
// corpo del ciclo
}
1. 
2. 
3. 
4. 

      │ VERO    │ FALSO ──> Continua
      │         │
      ▼         │
  ┌───────┐    │
  │ Corpo │    │
  └───┬───┘    │
      │        │
  ┌───▼────┐   │
  │Aggiorna│   │
  └───┬────┘   │
      │        │
      └────────┘
Esempio base:
Equivalenza con while:
#include <stdio.h>
int main(){
// Stampa numeri da 1 a 10
for(int i =1; i <=10; i++){
        printf("%d ", i);
}
    printf("\n");
return0;
}
// Output: 1 2 3 4 5 6 7 8 9 10
// Ciclo for
for(int i =0; i <5; i++){
    printf("%d\n", i);
}

2. Varianti del ciclo for
Contare all’indietro:
Incremento personalizzato:
For con espressioni complesse:
// Equivalente con while
int i =0; // inizializzazione
while(i <5){ // condizione
    printf("%d\n", i);
    i++; // aggiornamento
}
for(int i =10; i >=1; i--){
    printf("%d ", i);
}
printf("Partenza!\n");
// Output: 10 9 8 7 6 5 4 3 2 1 Partenza!
// Numeri pari da 0 a 20
for(int i =0; i <=20; i +=2){
    printf("%d ", i);
}
// Output: 0 2 4 6 8 10 12 14 16 18 20
// Multipli di 5
for(int i =5; i <=50; i +=5){
    printf("%d ", i);
}
// Output: 5 10 15 20 25 30 35 40 45 50

For “infinito”:
3. Cicli annidati
I cicli annidati sono cicli dentro altri cicli. Il ciclo interno viene eseguito completamente
per ogni iterazione del ciclo esterno.
Struttura base:
// Più variabili
for(int i =0, j =10; i < j; i++, j--){
    printf("i=%d, j=%d\n", i, j);
}
// Condizione complessa
for(int i =1; i <=100&& i*i <=50; i++){
    printf("%d ", i);
}
// Tutte le parti sono opzionali
for(;;){
    printf("Ciclo infinito\n");
// Serve un break per uscire!
}
// Equivalente a while(1)
for(int i =0; i < righe; i++){ // ciclo esterno
for(int j =0; j < colonne; j++){ // ciclo interno
// eseguito righe × colonne volte
}
}

Esempio 1: Tabella di moltiplicazione
Esempio 2: Pattern con asterischi
#include <stdio.h>
int main(){
    printf("TABELLA PITAGORICA\n");
    printf("    ");
// Intestazione
for(int i =1; i <=10; i++){
        printf("%4d", i);
}
    printf("\n");
    printf("   ");
for(int i =0; i <40; i++) printf("-");
    printf("\n");
// Righe della tabella
for(int i =1; i <=10; i++){
        printf("%2d |", i);
for(int j =1; j <=10; j++){
            printf("%4d", i * j);
}
        printf("\n");
}
return0;
}
#include <stdio.h>
int main(){

int n =5;
// Triangolo rettangolo
    printf("Triangolo:\n");
for(int i =1; i <= n; i++){
for(int j =1; j <= i; j++){
            printf("* ");
}
        printf("\n");
}
// Output:
// *
// * *
// * * *
// * * * *
// * * * * *
    printf("\nQuadrato:\n");
for(int i =0; i < n; i++){
for(int j =0; j < n; j++){
            printf("* ");
}
        printf("\n");
}
// Output:
// * * * * *
// * * * * *
// * * * * *
// * * * * *
// * * * * *

Complessità dei cicli annidati:
4. Break e Continue
Break: esce immediatamente dal ciclo
return0;
}
// Un ciclo: O(n) - n iterazioni
for(int i =0; i < n; i++){
// eseguito n volte
}
// Due cicli annidati: O(n²) - n×n iterazioni
for(int i =0; i < n; i++){
for(int j =0; j < n; j++){
// eseguito n×n volte
}
}
// Tre cicli annidati: O(n³) - n×n×n iterazioni
for(int i =0; i < n; i++){
for(int j =0; j < n; j++){
for(int k =0; k < n; k++){
// eseguito n×n×n volte
}
}
}
#include <stdio.h>
int main(){

Continue: salta alla prossima iterazione
// Cerca il primo numero divisibile per 7
for(int i =1; i <=100; i++){
if(i %7==0){
            printf("Primo multiplo di 7: %d\n", i);
break; // Esce dal ciclo
}
}
// Break in cicli annidati (esce solo dal ciclo interno)
for(int i =0; i <3; i++){
        printf("Ciclo esterno: %d\n", i);
for(int j =0; j <5; j++){
if(j ==2)break; // Esce solo dal for interno
            printf("  Ciclo interno: %d\n", j);
}
}
return0;
}
#include <stdio.h>
int main(){
// Stampa solo numeri dispari
    printf("Numeri dispari da 1 a 20:\n");
for(int i =1; i <=20; i++){
if(i %2==0){
continue; // Salta i numeri pari
}
        printf("%d ", i);
}
    printf("\n");

Differenza tra break e continue:
// Salta il numero 5
    printf("Numeri da 1 a 10 (escluso 5):\n");
for(int i =1; i <=10; i++){
if(i ==5)continue;
        printf("%d ", i);
}
    printf("\n");
return0;
}
// Con break
for(int i =0; i <10; i++){
if(i ==5)break;
    printf("%d ", i);
}
// Output: 0 1 2 3 4
// Con continue
for(int i =0; i <10; i++){
if(i ==5)continue;
    printf("%d ", i);
}
// Output: 0 1 2 3 4 6 7 8 9

5. Scelta del ciclo appropriato
Situazione Ciclo
consigliato Esempio
Numero iterazioni noto for Stampare numeri da 1 a 100
Iterare su array/sequenzafor Processare elementi array
Condizione di uscita variabilewhile Leggere input fino a valore
speciale
Almeno un’esecuzione
necessaria do-while Menu, validazione input
Cicli infiniti con break for(;;) o while(1)Server, game loop
Esempi comparativi:
// FOR - quando sai quante volte
for(int i =0; i <10; i++){
    printf("%d ", i);
}
// WHILE - quando la condizione è dinamica
int somma =0, n;
while(somma <100){
    scanf("%d", &n);
    somma += n;
}
// DO-WHILE - quando serve almeno un'esecuzione
int scelta;
do{
    printf("Menu: ");

6. Pattern comuni di iterazione
Sommatoria:
Produttoria:
Ricerca:
Conteggio:
    scanf("%d", &scelta);
}while(scelta <1|| scelta >3);
int somma =0;
for(int i =1; i <= n; i++){
    somma += i;
}
int prodotto =1;
for(int i =1; i <= n; i++){
    prodotto *= i;
}
int trovato =0;
for(int i =0; i < n; i++){
if(array[i]== target){
        trovato =1;
break;
}
}
int contatore =0;
for(int i =0; i < n; i++){

PARTE PRATICA (2h)
Esercizio 1: Tabelle e sequenze numeriche
if(condizione){
        contatore++;
}
}
#include <stdio.h>
int main(){
int n;
    printf("Inserisci un numero: ");
    scanf("%d", &n);
// Tabellina
    printf("\nTabellina del %d:\n", n);
for(int i =1; i <=10; i++){
        printf("%d x %d = %d\n", n, i, n * i);
}
// Quadrati
    printf("\nQuadrati da 1 a %d:\n", n);
for(int i =1; i <= n; i++){
        printf("%d² = %d\n", i, i * i);
}
// Cubi
    printf("\nCubi da 1 a %d:\n", n);
for(int i =1; i <= n; i++){

Esercizio 2: Disegno di pattern con asterischi
        printf("%d³ = %d\n", i, i * i * i);
}
return0;
}
#include <stdio.h>
int main(){
int n;
    printf("Inserisci l'altezza del pattern: ");
    scanf("%d", &n);
// Pattern 1: Triangolo crescente
    printf("\nPattern 1 - Triangolo:\n");
for(int i =1; i <= n; i++){
for(int j =1; j <= i; j++){
            printf("* ");
}
        printf("\n");
}
// Pattern 2: Triangolo decrescente
    printf("\nPattern 2 - Triangolo invertito:\n");
for(int i = n; i >=1; i--){
for(int j =1; j <= i; j++){
            printf("* ");
}
        printf("\n");
}

// Pattern 3: Piramide
    printf("\nPattern 3 - Piramide:\n");
for(int i =1; i <= n; i++){
// Spazi iniziali
for(int j =1; j <= n - i; j++){
            printf("  ");
}
// Asterischi
for(int j =1; j <=2* i -1; j++){
            printf("* ");
}
        printf("\n");
}
// Pattern 4: Rombo
    printf("\nPattern 4 - Rombo:\n");
// Parte superiore
for(int i =1; i <= n; i++){
for(int j =1; j <= n - i; j++){
            printf(" ");
}
for(int j =1; j <=2* i -1; j++){
            printf("*");
}
        printf("\n");
}
// Parte inferiore
for(int i = n -1; i >=1; i--){
for(int j =1; j <= n - i; j++){
            printf(" ");
}
for(int j =1; j <=2* i -1; j++){
            printf("*");
}

Esercizio 3: Sommatorie e produttorie
        printf("\n");
}
return0;
}
#include <stdio.h>
int main(){
int n;
    printf("Inserisci un numero: ");
    scanf("%d", &n);
// Somma dei primi n numeri naturali
int somma =0;
for(int i =1; i <= n; i++){
        somma += i;
}
    printf("\nSomma 1+2+...+%d = %d\n", n, somma);
    printf("Formula: %d*(%d+1)/2 = %d\n", n, n, n*(n+1)/2);
// Somma dei quadrati
int sommaQuadrati =0;
for(int i =1; i <= n; i++){
        sommaQuadrati += i * i;
}
    printf("\nSomma 1²+2²+...+%d² = %d\n", n, sommaQuadrati);
// Fattoriale
longlong fattoriale =1;

Esercizio 4: Ricerca di numeri primi
for(int i =1; i <= n; i++){
        fattoriale *= i;
}
    printf("\n%d! = %lld\n", n, fattoriale);
// Potenza (n^k)
int k;
    printf("\nInserisci l'esponente: ");
    scanf("%d", &k);
longlong potenza =1;
for(int i =0; i < k; i++){
        potenza *= n;
}
    printf("%d^%d = %lld\n", n, k, potenza);
return0;
}
#include <stdio.h>
int main(){
int n;
    printf("Trova tutti i numeri primi fino a: ");
    scanf("%d", &n);
    printf("\nNumeri primi fino a %d:\n", n);
int contatore =0;

for(int num =2; num <= n; num++){
int isPrimo =1; // Assumiamo che sia primo
// Verifichiamo se num è divisibile per qualche numero
for(int i =2; i * i <= num; i++){
if(num % i ==0){
                isPrimo =0; // Non è primo
break;
}
}
if(isPrimo){
            printf("%d ", num);
            contatore++;
if(contatore %10==0) printf("\n"); // A capo ogni 10 numeri
}
}
    printf("\n\nTotale numeri primi: %d\n", contatore);
// Verifica se un numero specifico è primo
int test;
    printf("\nVerifica se un numero è primo: ");
    scanf("%d", &test);
if(test <2){
        printf("%d non è primo\n", test);
}else{
int primo =1;
for(int i =2; i * i <= test; i++){
if(test % i ==0){
                primo =0;
                printf("%d non è primo (divisibile per %d)\n", test, i);
break;
}

Esercizio 5: Tavola degli scacchi
}
if(primo){
            printf("%d è primo!\n", test);
}
}
return0;
}
#include <stdio.h>
int main(){
int dimensione =8;
    printf("TAVOLA DEGLI SCACCHI (%dx%d)\n\n", dimensione, dimensione);
// Metodo 1: con caratteri
for(int i =0; i < dimensione; i++){
for(int j =0; j < dimensione; j++){
if((i + j)%2==0){
                printf("█ "); // Casella scura
}else{
                printf("  "); // Casella chiara
}
}
        printf("\n");
}
    printf("\n");
// Metodo 2: con numeri

Esercizi da svolgere autonomamente:
Calendario: Crea un programma che stampa i giorni di un mese (da 1 a 30/31)
disposti in righe da 7 giorni
Serie di Fibonacci: Stampa i primi N numeri della serie di Fibonacci usando un
ciclo for
Triangolo di Floyd: Stampa il triangolo di Floyd (numeri consecutivi disposti a
triangolo)
1
2 3
4 5 6
7 8 9 10
Statistica numeri: Chiedi N numeri all’utente e calcola: somma, media, massimo,
minimo, quanti sono pari/dispari
Conversione binario: Converti un numero decimale in binario usando il ciclo for e
l’operatore modulo
for(int i =0; i < dimensione; i++){
for(int j =0; j < dimensione; j++){
if((i + j)%2==0){
                printf("0 ");
}else{
                printf("1 ");
}
}
        printf("\n");
}
return0;
}
1. 
2. 
3. 
4. 
5. 

Triangolo di Pascal: Stampa le prime N righe del triangolo di Pascal
MCD ed mcm: Calcola il Massimo Comun Divisore e il minimo comune multiplo di
due numeri
Numeri perfetti: Trova tutti i numeri perfetti fino a N (un numero è perfetto se è
uguale alla somma dei suoi divisori propri, es: 6 = 1+2+3)
Tabella ASCII: Stampa la tabella ASCII dei caratteri stampabili (da 32 a 126)
Stella a 5 punte: Disegna una stella a 5 punte usando cicli annidati e asterischi
Riepilogo Concetti Chiave
✓ Il ciclo for è ideale quando si conosce il numero di iterazioni
✓ Struttura: for (init; condizione; aggiornamento) { corpo }
✓ I cicli annidati moltiplicano il numero di iterazioni
✓ Break esce dal ciclo, continue salta all’iterazione successiva
✓ Scegli il ciclo in base al problema: for, while o do-while
✓ Pattern comuni: sommatoria, produttoria, ricerca, conteggio
Prossima lezione: Approfondiremo gli array monodimensionali!
6. 
7. 
8. 
9. 
10. 


---

# lezione 13 array

**File:** `lezione 13 array.pdf`
**Tipo:** `.pdf`
**Dimensione:** 129.3 KB
**Ultima modifica:** 02/07/2026 09:24

---

LEZIONE 13 - Array
Monodimensionali
PARTE TEORICA (2h)
1. Concetto di Array
Un array è una struttura dati che permette di memorizzare più valori dello stesso tipo
in una sequenza contigua di memoria, accessibili tramite un indice.
Perché usare gli array?
Gestire collezioni di dati correlati (es: voti di studenti, temperature del mese)
Evitare di dichiarare decine di variabili separate
Facilitare l’elaborazione di grandi quantità di dati
Permettere l’accesso rapido tramite indice
Caratteristiche principali:
Tutti gli elementi hanno lo stesso tipo di dato
La dimensione è fissa (definita alla dichiarazione)
Gli elementi sono contigui in memoria
L’accesso avviene tramite indice che parte da 0
Rappresentazione in memoria:
Array: int numeri[5];
Indici:     0     1     2     3     4
         ┌─────┬─────┬─────┬─────┬─────┐
numeri   │  10 │  20 │  30 │  40 │  50 │
         └─────┴─────┴─────┴─────┴─────┘
Indirizzi: 1000  1004  1008  1012  1016  (ogni int occupa 4 byte)
• 
• 
• 
• 
• 
• 
• 
• 

2. Dichiarazione e Inizializzazione
Sintassi base:
Esempi di dichiarazione:
Inizializzazione:
Esempio completo:
tipo nomeArray[dimensione];
int voti[30]; // Array di 30 interi
float temperature[12]; // Array di 12 float
char nome[50]; // Array di 50 caratteri
double prezzi[100]; // Array di 100 double
// Metodo 1: Inizializzazione alla dichiarazione
int numeri[5]={10, 20, 30, 40, 50};
// Metodo 2: Inizializzazione parziale (i restanti elementi sono 0)
int numeri[5]={10, 20}; // {10, 20, 0, 0, 0}
// Metodo 3: Dimensione automatica
int numeri[]={10, 20, 30, 40, 50}; // Dimensione = 5
// Metodo 4: Inizializzazione a zero
int numeri[5]={0}; // Tutti gli elementi a 0
// Metodo 5: Senza inizializzazione (valori casuali!)
int numeri[5]; // ATTENZIONE: contiene valori casuali (garbage)
#include <stdio.h>

3. Accesso agli Elementi
L’accesso agli elementi avviene tramite l’operatore di indicizzazione[] utilizzando un
indice da 0 a dimensione-1.
Sintassi:
Lettura e scrittura:
int main(){
// Dichiarazione e inizializzazione
int numeri[5]={10, 20, 30, 40, 50};
// Dichiarazione senza inizializzazione
float temperature[7];
// Inizializzazione manuale
    temperature[0]=18.5;
    temperature[1]=19.2;
    temperature[2]=21.0;
    temperature[3]=22.5;
    temperature[4]=20.8;
    temperature[5]=19.5;
    temperature[6]=18.0;
return0;
}
nomeArray[indice]
int numeri[5]={10, 20, 30, 40, 50};
// Lettura
int primo = numeri[0]; // primo = 10

ATTENZIONE agli indici:
Conseguenze degli errori di indice:
Comportamento indefinito (undefined behavior)
Possibili crash del programma
Corruzione di dati in memoria
Bug difficili da trovare
4. Dimensione dell’Array
Calcolare la dimensione:
int terzo = numeri[2]; // terzo = 30
int ultimo = numeri[4]; // ultimo = 50
// Scrittura
numeri[0]=100; // Modifica il primo elemento
numeri[2]=300; // Modifica il terzo elemento
// Uso in espressioni
int somma = numeri[0]+ numeri[1]; // somma = 100 + 20 = 120
numeri[3]= numeri[1]*2; // numeri[3] = 20 * 2 = 40
int array[5];
// CORRETTO: indici da 0 a 4
array[0]=10; // OK
array[4]=50; // OK
// ERRORE: indice fuori range
array[5]=60; // ERRORE! Non esiste array[5]
array[-1]=10; // ERRORE! Indice negativo
array[10]=99; // ERRORE! Accesso fuori dai limiti
• 
• 
• 
• 

Esempio pratico:
5. Array e Cicli
I cicli sono essenziali per lavorare con gli array. Il ciclo for è il più utilizzato.
int numeri[10];
// Numero di elementi
int dimensione =sizeof(numeri)/sizeof(numeri[0]);
// sizeof(numeri) = 40 byte (10 elementi × 4 byte)
// sizeof(numeri[0]) = 4 byte (1 int)
// dimensione = 40 / 4 = 10
// Definire costanti per la dimensione
#define MAX_ELEMENTI 100
int array[MAX_ELEMENTI];
#include <stdio.h>
int main(){
int numeri[]={10, 20, 30, 40, 50};
int dimensione =sizeof(numeri)/sizeof(numeri[0]);
    printf("Dimensione dell'array: %d elementi\n", dimensione);
    printf("Dimensione in byte: %lu\n", sizeof(numeri));
    printf("Dimensione di un elemento: %lu byte\n", sizeof(numeri[0]));
return0;
}

Pattern base:
Esempio completo: Input e Output
int array[10];
int dimensione =10;
// Inizializzazione
for(int i =0; i < dimensione; i++){
    array[i]= i *10;
}
// Lettura/Stampa
for(int i =0; i < dimensione; i++){
    printf("%d ", array[i]);
}
// Elaborazione
for(int i =0; i < dimensione; i++){
    array[i]= array[i]*2; // Raddoppia ogni elemento
}
#include <stdio.h>
#define MAX 5
int main(){
int numeri[MAX];
// Input: chiede all'utente di inserire i valori
    printf("Inserisci %d numeri:\n", MAX);
for(int i =0; i < MAX; i++){
        printf("Numero %d: ", i +1);
        scanf("%d", &numeri[i]);

6. Operazioni Comuni sugli Array
1. Somma di tutti gli elementi:
2. Media:
3. Ricerca del massimo:
}
// Output: stampa i valori
    printf("\nNumeri inseriti:\n");
for(int i =0; i < MAX; i++){
        printf("numeri[%d] = %d\n", i, numeri[i]);
}
return0;
}
int somma =0;
for(int i =0; i < dimensione; i++){
    somma += array[i];
}
float media =(float)somma / dimensione;
int massimo = array[0];
for(int i =1; i < dimensione; i++){
if(array[i]> massimo){
        massimo = array[i];
}
}

4. Ricerca del minimo:
5. Ricerca di un elemento:
6. Conteggio elementi che soddisfano una condizione:
int minimo = array[0];
for(int i =1; i < dimensione; i++){
if(array[i]< minimo){
        minimo = array[i];
}
}
int target =30;
int trovato =0;
int posizione =-1;
for(int i =0; i < dimensione; i++){
if(array[i]== target){
        trovato =1;
        posizione = i;
break;
}
}
if(trovato){
    printf("Elemento trovato in posizione %d\n", posizione);
}else{
    printf("Elemento non trovato\n");
}
// Conta numeri pari
int contatore =0;
for(int i =0; i < dimensione; i++){

PARTE PRATICA (2h)
Esercizio 1: Inserimento e stampa di array
if(array[i]%2==0){
        contatore++;
}
}
#include <stdio.h>
#define MAX 10
int main(){
int numeri[MAX];
int n;
// Chiedi quanti elementi inserire
do{
        printf("Quanti numeri vuoi inserire (max %d)? ", MAX);
        scanf("%d", &n);
}while(n <1|| n > MAX);
// Inserimento
    printf("\nInserisci %d numeri:\n", n);
for(int i =0; i < n; i++){
        printf("Numero %d: ", i +1);
        scanf("%d", &numeri[i]);
}
// Stampa normale
    printf("\nArray in ordine normale:\n");

Esercizio 2: Ricerca di elementi
for(int i =0; i < n; i++){
        printf("%d ", numeri[i]);
}
    printf("\n");
// Stampa inversa
    printf("\nArray in ordine inverso:\n");
for(int i = n -1; i >=0; i--){
        printf("%d ", numeri[i]);
}
    printf("\n");
// Stampa con indici
    printf("\nArray con indici:\n");
for(int i =0; i < n; i++){
        printf("[%d] = %d\n", i, numeri[i]);
}
return0;
}
#include <stdio.h>
#define MAX 10
int main(){
int numeri[MAX]={15, 8, 23, 42, 7, 19, 31, 5, 12, 28};
int dimensione = MAX;
int target;
// Stampa array

    printf("Array: ");
for(int i =0; i < dimensione; i++){
        printf("%d ", numeri[i]);
}
    printf("\n\n");
// Ricerca elemento
    printf("Inserisci il numero da cercare: ");
    scanf("%d", &target);
// Ricerca lineare
int trovato =0;
int posizioni[MAX];
int contatore =0;
for(int i =0; i < dimensione; i++){
if(numeri[i]== target){
            posizioni[contatore]= i;
            contatore++;
            trovato =1;
}
}
// Risultato
if(trovato){
        printf("\nElemento %d trovato in %d posizione/i:\n", target, contatore);
for(int i =0; i < contatore; i++){
            printf("  - Indice %d\n", posizioni[i]);
}
}else{
        printf("\nElemento %d non trovato nell'array\n", target);
}
// Verifica se un numero è presente
    printf("\nVerifichiamo la presenza di alcuni numeri:\n");

Esercizio 3: Calcolo di media, massimo, minimo
int daVerificare[]={7, 100, 23, 50};
for(int i =0; i <4; i++){
int presente =0;
for(int j =0; j < dimensione; j++){
if(numeri[j]== daVerificare[i]){
                presente =1;
break;
}
}
        printf("%d: %s\n", daVerificare[i], presente ?"PRESENTE": "ASSENTE");
}
return0;
}
#include <stdio.h>
#define MAX 100
int main(){
float numeri[MAX];
int n;
// Input
    printf("Quanti numeri vuoi inserire? ");
    scanf("%d", &n);
    printf("\nInserisci %d numeri:\n", n);
for(int i =0; i < n; i++){
        printf("Numero %d: ", i +1);

        scanf("%f", &numeri[i]);
}
// Calcolo somma
float somma =0;
for(int i =0; i < n; i++){
        somma += numeri[i];
}
// Calcolo media
float media = somma / n;
// Ricerca massimo e minimo
float massimo = numeri[0];
float minimo = numeri[0];
int indiceMassimo =0;
int indiceMinimo =0;
for(int i =1; i < n; i++){
if(numeri[i]> massimo){
            massimo = numeri[i];
            indiceMassimo = i;
}
if(numeri[i]< minimo){
            minimo = numeri[i];
            indiceMinimo = i;
}
}
// Calcolo range
float range = massimo - minimo;
// Conteggio sopra/sotto media
int sopraMadia =0, sottoMedia =0, ugualeMedia =0;
for(int i =0; i < n; i++){

Esercizio 4: Inversione di un array
if(numeri[i]> media) sopraMadia++;
elseif(numeri[i]< media) sottoMedia++;
else ugualeMedia++;
}
// Output statistiche
    printf("\n=== STATISTICHE ===\n");
    printf("Numero di elementi: %d\n", n);
    printf("Somma: %.2f\n", somma);
    printf("Media: %.2f\n", media);
    printf("Massimo: %.2f (posizione %d)\n", massimo, indiceMassimo);
    printf("Minimo: %.2f (posizione %d)\n", minimo, indiceMinimo);
    printf("Range: %.2f\n", range);
    printf("\nDistribuzione rispetto alla media:\n");
    printf("  Sopra la media: %d (%.1f%%)\n", sopraMadia, (float)sopraMadia/
n*100);
    printf("  Sotto la media: %d (%.1f%%)\n", sottoMedia, (float)sottoMedia/
n*100);
    printf("  Uguale alla media: %d (%.1f%%)\n", ugualeMedia, (float)ugualeM
edia/n*100);
return0;
}
#include <stdio.h>
#define MAX 20
void stampaArray(int arr[],int n, constchar* messaggio){
    printf("%s: ", messaggio);
for(int i =0; i < n; i++){
        printf("%d ", arr[i]);

}
    printf("\n");
}
int main(){
int numeri[MAX];
int n;
// Input
    printf("Quanti numeri vuoi inserire? ");
    scanf("%d", &n);
    printf("Inserisci %d numeri:\n", n);
for(int i =0; i < n; i++){
        scanf("%d", &numeri[i]);
}
// Stampa array originale
    stampaArray(numeri, n, "Array originale");
// Metodo 1: Inversione con array temporaneo
int temp[MAX];
for(int i =0; i < n; i++){
        temp[i]= numeri[n -1- i];
}
for(int i =0; i < n; i++){
        numeri[i]= temp[i];
}
    stampaArray(numeri, n, "Dopo inversione (metodo 1)");
// Rimettiamo l'array come prima (per testare metodo 2)
for(int i =0; i < n; i++){
        temp[i]= numeri[n -1- i];
}
for(int i =0; i < n; i++){

Esercizio 5: Operazioni avanzate su array
        numeri[i]= temp[i];
}
// Metodo 2: Inversione in place (scambio elementi)
    printf("\nMetodo 2: Inversione in place\n");
for(int i =0; i < n /2; i++){
// Scambia numeri[i] con numeri[n-1-i]
int temporaneo = numeri[i];
        numeri[i]= numeri[n -1- i];
        numeri[n -1- i]= temporaneo;
// Mostra lo scambio
        printf("Scambio %d: ", i +1);
        stampaArray(numeri, n, "");
}
    stampaArray(numeri, n, "\nArray finale invertito");
return0;
}
#include <stdio.h>
#define MAX 50
int main(){
int numeri[MAX]={12, 7, 23, 7, 45, 12, 89, 7, 23, 56};
int n =10;
    printf("Array originale: ");
for(int i =0; i < n; i++){

        printf("%d ", numeri[i]);
}
    printf("\n\n");
// 1. Conta elementi pari e dispari
int pari =0, dispari =0;
for(int i =0; i < n; i++){
if(numeri[i]%2==0) pari++;
else dispari++;
}
    printf("Numeri pari: %d, Numeri dispari: %d\n\n", pari, dispari);
// 2. Trova duplicati
    printf("Elementi duplicati:\n");
for(int i =0; i < n; i++){
for(int j = i +1; j < n; j++){
if(numeri[i]== numeri[j]){
// Verifica che non l'abbiamo già stampato
int giàStampato =0;
for(int k =0; k < i; k++){
if(numeri[k]== numeri[i]){
                        giàStampato =1;
break;
}
}
if(!giàStampato){
                    printf("  %d appare più volte\n", numeri[i]);
}
break;
}
}
}
// 3. Frequenza degli elementi
    printf("\nFrequenza degli elementi:\n");

int visitato[MAX]={0};
for(int i =0; i < n; i++){
if(visitato[i]==0){
int conteggio =1;
for(int j = i +1; j < n; j++){
if(numeri[i]== numeri[j]){
                    conteggio++;
                    visitato[j]=1;
}
}
            printf("  %d appare %d volta/e\n", numeri[i], conteggio);
}
}
// 4. Secondo elemento più grande
int max1 = numeri[0], max2 =-1;
for(int i =1; i < n; i++){
if(numeri[i]> max1){
            max2 = max1;
            max1 = numeri[i];
}elseif(numeri[i]> max2 && numeri[i]!= max1){
            max2 = numeri[i];
}
}
    printf("\nMassimo: %d, Secondo massimo: %d\n", max1, max2);
// 5. Copia elementi pari in un nuovo array
int arrayPari[MAX];
int contatorePari =0;
for(int i =0; i < n; i++){
if(numeri[i]%2==0){
            arrayPari[contatorePari]= numeri[i];
            contatorePari++;
}
}

Esercizi da svolgere autonomamente:
Ordinamento Bubble Sort: Implementa l’algoritmo bubble sort per ordinare un
array in ordine crescente
Rotazione array: Ruota gli elementi di un array verso destra di K posizioni (es:
[1,2,3,4,5] ruotato di 2 diventa [4,5,1,2,3])
Merge di due array: Dati due array ordinati, crea un terzo array contenente tutti gli
elementi in ordine
Rimozione duplicati: Rimuovi tutti gli elementi duplicati da un array mantenendo
solo la prima occorrenza
Array palindromo: Verifica se un array è palindromo (si legge uguale da sinistra a
destra e viceversa)
Differenza tra array: Dati due array, trova gli elementi presenti nel primo ma non
nel secondo
Prodotto scalare: Calcola il prodotto scalare di due array (somma dei prodotti
degli elementi corrispondenti)
Elementi unici: Crea un nuovo array contenente solo gli elementi che appaiono
una sola volta
Shift ciclico: Implementa uno shift ciclico a sinistra (il primo elemento va alla fine)
    printf("\nArray contenente solo numeri pari:\n");
for(int i =0; i < contatorePari; i++){
        printf("%d ", arrayPari[i]);
}
    printf("\n");
return0;
}
1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
9. 

Array di Fibonacci: Riempi un array con i primi N numeri della sequenza di
Fibonacci
Riepilogo Concetti Chiave
✓ Gli array sono collezioni di elementi dello stesso tipo
✓ Gli indici vanno da 0 a dimensione-1
✓ Accesso fuori dai limiti causa comportamento indefinito
✓ I cicli for sono perfetti per iterare sugli array
✓ Operazioni comuni: ricerca, massimo/minimo, somma, media
✓ sizeof(array)/sizeof(array[0]) calcola il numero di elementi
Prossima lezione: Approfondiremo gli array multidimensionali e le stringhe!
10. 


---

# lezione 14 matrici

**File:** `lezione 14 matrici.pdf`
**Tipo:** `.pdf`
**Dimensione:** 341.6 KB
**Ultima modifica:** 02/07/2026 09:24

---

LEZIONE 14 - Array Multidimensionali e
Stringhe
PARTE TEORICA (2h)
1. Array Bidimensionali (Matrici)
Un 
array bidimensionale
 (o 
matrice
) è un array di array: una struttura che organizza i
dati in 
righe
 e 
colonne
.
Rappresentazione concettuale:
Array bidimensionale: int matrice[3][4]
      Colonna:  0    1    2    3
              ┌────┬────┬────┬────┐
    Riga 0    │  1 │  2 │  3 │  4 │
              ├────┼────┼────┼────┤
    Riga 1    │  5 │  6 │  7 │  8 │
              ├────┼────┼────┼────┤
    Riga 2    │  9 │ 10 │ 11 │ 12 │
              └────┴────┴────┴────┘
matrice[0][0] = 1    matrice[0][1] = 2
matrice[1][2] = 7    matrice[2][3] = 12
Utilizzi comuni:
 - Tabelle di dati (es: vendite per mese/prodotto) - Immagini bitmap -
Giochi da tavolo (scacchiera, tris) - Matrici matematiche - Griglie geografiche
2. Dichiarazione e Inizializzazione delle Matrici
Sintassi base:
Esempi di dichiarazione:
Inizializzazione:
tipo nomeMatrice
[
righe
][
colonne
];
int
 matrice
[
3
][
4
];
        
// 3 righe, 4 colonne (12 elementi totali)
float
 temperature
[
12
][
7
];
 
// 12 mesi, 7 giorni/settimana
char
 scacchiera
[
8
][
8
];
    
// Scacchiera 8×8

Esempio completo:
3. Accesso agli Elementi
Sintassi:
Accesso in lettura e scrittura:
// Metodo 1: Inizializzazione completa
int
 matrice
[
3
][
4
]
 
=
 
{
    
{
1
,
 
2
,
 
3
,
 
4
},
      
// Riga 0
    
{
5
,
 
6
,
 
7
,
 
8
},
      
// Riga 1
    
{
9
,
 
10
,
 
11
,
 
12
}
    
// Riga 2
};
// Metodo 2: Inizializzazione lineare (stesso risultato)
int
 matrice
[
3
][
4
]
 
=
 
{
1
,
 
2
,
 
3
,
 
4
,
 
5
,
 
6
,
 
7
,
 
8
,
 
9
,
 
10
,
 
11
,
 
12
};
// Metodo 3: Inizializzazione parziale
int
 matrice
[
3
][
4
]
 
=
 
{
    
{
1
,
 
2
},
         
// Riga 0: {1, 2, 0, 0}
    
{
5
},
            
// Riga 1: {5, 0, 0, 0}
    
{}
              
// Riga 2: {0, 0, 0, 0}
};
// Metodo 4: Inizializzazione a zero
int
 matrice
[
3
][
4
]
 
=
 
{
0
};
  
// Tutti gli elementi a 0
// Metodo 5: Prima dimensione automatica
int
 matrice
[][
4
]
 
=
 
{
    
{
1
,
 
2
,
 
3
,
 
4
},
    
{
5
,
 
6
,
 
7
,
 
8
},
    
{
9
,
 
10
,
 
11
,
 
12
}
};
  
// Il compilatore deduce 3 righe
#include 
<stdio.h>
int
 main
()
 
{
    
// Matrice 3×3 (identità)
    
int
 identita
[
3
][
3
]
 
=
 
{
        
{
1
,
 
0
,
 
0
},
        
{
0
,
 
1
,
 
0
},
        
{
0
,
 
0
,
 
1
}
    
};
    
    
// Matrice non inizializzata
    
float
 valori
[
2
][
3
];
    
    
// Inizializzazione manuale
    valori
[
0
][
0
]
 
=
 
1.5
;
    valori
[
0
][
1
]
 
=
 
2.3
;
    valori
[
0
][
2
]
 
=
 
3.7
;
    valori
[
1
][
0
]
 
=
 
4.2
;
    valori
[
1
][
1
]
 
=
 
5.8
;
    valori
[
1
][
2
]
 
=
 
6.1
;
    
    
return
 
0
;
}
nomeMatrice
[
indiceRiga
][
indiceColonna
]

Iterazione con cicli annidati:
Output:
Matrice:
  1   2   3   4
  5   6   7   8
  9  10  11  12
4. Operazioni su Matrici
Input da utente:
int
 matrice
[
3
][
4
]
 
=
 
{
    
{
1
,
 
2
,
 
3
,
 
4
},
    
{
5
,
 
6
,
 
7
,
 
8
},
    
{
9
,
 
10
,
 
11
,
 
12
}
};
// Lettura
int
 valore 
=
 matrice
[
1
][
2
];
  
// valore = 7
// Scrittura
matrice
[
0
][
0
]
 
=
 
100
;
         
// Primo elemento = 100
matrice
[
2
][
3
]
 
=
 
200
;
         
// Ultimo elemento = 200
// Uso in espressioni
int
 somma 
=
 matrice
[
0
][
1
]
 
+
 matrice
[
1
][
1
];
  
// 2 + 6 = 8
matrice
[
1
][
0
]
 
=
 matrice
[
0
][
0
]
 
*
 
2
;
          
// matrice[1][0] = 200
int
 matrice
[
3
][
4
];
int
 righe 
=
 
3
,
 colonne 
=
 
4
;
// Riempimento
for
 
(
int
 i 
=
 
0
;
 i 
<
 righe
;
 i
++)
 
{
    
for
 
(
int
 j 
=
 
0
;
 j 
<
 colonne
;
 j
++)
 
{
        matrice
[
i
][
j
]
 
=
 i 
*
 colonne 
+
 j 
+
 
1
;
    
}
}
// Stampa
printf
(
"Matrice:
\n
"
);
for
 
(
int
 i 
=
 
0
;
 i 
<
 righe
;
 i
++)
 
{
    
for
 
(
int
 j 
=
 
0
;
 j 
<
 colonne
;
 j
++)
 
{
        printf
(
"
%3d
 "
,
 matrice
[
i
][
j
]);
    
}
    printf
(
"
\n
"
);
}

Somma di matrici:
Trasposizione (scambio righe ↔  colonne):
Prodotto matrice per scalare:
Ricerca elemento:
#include 
<stdio.h>
#define RIGHE 
3
#define COLONNE 
3
int
 main
()
 
{
    
int
 matrice
[
RIGHE
][
COLONNE
];
    
    printf
(
"Inserisci gli elementi della matrice 
%d
x
%d
:
\n
"
,
 RIGHE
,
 COLONNE
    
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 RIGHE
;
 i
++)
 
{
        
for
 
(
int
 j 
=
 
0
;
 j 
<
 COLONNE
;
 j
++)
 
{
            printf
(
"Elemento [
%d
][
%d
]: "
,
 i
,
 j
);
            scanf
(
"
%d
"
,
 
&
matrice
[
i
][
j
]);
        
}
    
}
    
    
return
 
0
;
}
// C = A + B
for
 
(
int
 i 
=
 
0
;
 i 
<
 righe
;
 i
++)
 
{
    
for
 
(
int
 j 
=
 
0
;
 j 
<
 colonne
;
 j
++)
 
{
        C
[
i
][
j
]
 
=
 A
[
i
][
j
]
 
+
 B
[
i
][
j
];
    
}
}
// Matrice originale: 3×4
// Matrice trasposta: 4×3
for
 
(
int
 i 
=
 
0
;
 i 
<
 righe
;
 i
++)
 
{
    
for
 
(
int
 j 
=
 
0
;
 j 
<
 colonne
;
 j
++)
 
{
        trasposta
[
j
][
i
]
 
=
 originale
[
i
][
j
];
    
}
}
int
 scalare 
=
 
5
;
for
 
(
int
 i 
=
 
0
;
 i 
<
 righe
;
 i
++)
 
{
    
for
 
(
int
 j 
=
 
0
;
 j 
<
 colonne
;
 j
++)
 
{
        risultato
[
i
][
j
]
 
=
 matrice
[
i
][
j
]
 
*
 scalare
;
    
}
}
int
 target 
=
 
42
;
int
 trovato 
=
 
0
;
int
 posizioneI
,
 posizioneJ
;
for
 
(
int
 i 
=
 
0
;
 i 
<
 righe
;
 i
++)
 
{
    
for
 
(
int
 j 
=
 
0
;
 j 
<
 colonne
;
 j
++)
 
{
        
if
 
(
matrice
[
i
][
j
]
 
==
 target
)
 
{
            trovato 
=
 
1
;
            posizioneI 
=
 i
;
            posizioneJ 
=
 j
;
            
break
;
        
}
    
}
    
if
 
(
trovato
)
 
break
;
}

5. Stringhe in C: Array di Caratteri
In C, una 
stringa
 è un array di caratteri terminato dal carattere speciale 
‘\0’
 (null
terminator).
Rappresentazione in memoria:
Stringa: char nome[] = "Ciao";
Indice:    0    1    2    3    4
         ┌────┬────┬────┬────┬────┐
nome     │ 'C'│ 'i'│ 'a'│ 'o'│ '\0'│
         └────┴────┴────┴────┴────┘
Dichiarazione e inizializzazione:
Importante:
 - Il terminatore ‘\0’ è 
obbligatorio
 - La dimensione dell’array deve essere
lunghezza + 1
 - Le stringhe letterali (tra virgolette) includono automaticamente ‘\0’
6. Terminatore ‘\0’
Il carattere 
‘\0’
 (valore ASCII = 0) indica la fine della stringa.
Perché è necessario?
Cosa succede senza ‘\0’?
Aggiungere manualmente ‘\0’:
// Metodo 1: Inizializzazione diretta con stringa letterale
char
 nome
[]
 
=
 
"Mario"
;
        
// Dimensione automatica = 6 (5 + '\0')
// Metodo 2: Specificare dimensione
char
 cognome
[
20
]
 
=
 
"Rossi"
;
   
// cognome[5] = '\0', resto = spazio inutilizzato
// Metodo 3: Carattere per carattere
char
 saluto
[
6
]
 
=
 
{
'C'
,
 
'i'
,
 
'a'
,
 
'o'
,
 
'!'
,
 
'
\0
'
};
  
// '\0' OBBLIGATORIO!
// Metodo 4: Senza inizializzazione
char
 buffer
[
100
];
  
// Contiene valori casuali
// ERRORE COMUNE: Dimenticare '\0'
char
 sbagliato
[
4
]
 
=
 
{
'C'
,
 
'i'
,
 
'a'
,
 
'o'
};
  
// ERRORE! Manca '\0'
char
 nome
[
10
]
 
=
 
"Anna"
;
// In memoria:
// [0]='A', [1]='n', [2]='n', [3]='a', [4]='\0', [5-9]=garbage
// Le funzioni sanno dove fermarsi grazie a '\0'
printf
(
"
%s
"
,
 nome
);
  
// Stampa "Anna" e si ferma a '\0'
char
 malformata
[
4
]
 
=
 
{
'T'
,
 
'e'
,
 
's'
,
 
't'
};
  
// Manca '\0'!
printf
(
"
%s
"
,
 malformata
);
  
// Stampa "Test" + caratteri casuali finché non trova un '\0'
// COMPORTAMENTO INDEFINITO!
char
 parola
[
10
];
parola
[
0
]
 
=
 
'C'
;
parola
[
1
]
 
=
 
'i'
;
parola
[
2
]
 
=
 
'a'
;
parola
[
3
]
 
=
 
'o'
;
parola
[
4
]
 
=
 
'
\0
'
;
  
// FONDAMENTALE!
printf
(
"
%s\n
"
,
 parola
);
  
// Output: Ciao

7. Input/Output di Stringhe
Output con printf():
Input con scanf():
Input con gets() (DEPRECATO - NON USARE!):
Input con fgets() (RACCOMANDATO):
8. Introduzione alle Funzioni string.h
La libreria 
string.h
 fornisce funzioni per manipolare stringhe.
Funzioni principali:
char
 nome
[]
 
=
 
"Mario"
;
printf
(
"
%s\n
"
,
 nome
);
           
// Stampa "Mario"
printf
(
"Nome: 
%s\n
"
,
 nome
);
     
// Stampa "Nome: Mario"
printf
(
"
%10s\n
"
,
 nome
);
         
// Stampa "     Mario" (allineato a destra)
printf
(
"
%-10s\n
"
,
 nome
);
        
// Stampa "Mario     " (allineato a sinistra)
char
 nome
[
50
];
printf
(
"Inserisci il tuo nome: "
);
scanf
(
"
%s
"
,
 nome
);
  
// ATTENZIONE: legge fino al primo spazio!
// Problema: "Mario Rossi" → legge solo "Mario"
char
 nome
[
50
];
gets
(
nome
);
  
// PERICOLOSO! Non controlla la dimensione
char
 nome
[
50
];
printf
(
"Inserisci il tuo nome completo: "
);
fgets
(
nome
,
 
sizeof
(
nome
),
 stdin
);
  
// Sicuro: limita a 49 caratteri + '\0'
// fgets() include '\n' alla fine, potrebbe servire rimuoverlo
nome
[
strcspn
(
nome
,
 
"
\n
"
)]
 
=
 
'
\0
'
;

ATTENZIONE alla sicurezza:
PARTE PRATICA (2h)
Esercizio 1: Operazioni su Matrici
#include 
<string.h>
// strlen() - Lunghezza della stringa (senza '\0')
char
 parola
[]
 
=
 
"Ciao"
;
int
 lunghezza 
=
 strlen
(
parola
);
  
// lunghezza = 4
// strcpy() - Copia una stringa
char
 dest
[
20
];
char
 src
[]
 
=
 
"Hello"
;
strcpy
(
dest
,
 src
);
  
// dest = "Hello"
// strcat() - Concatena stringhe
char
 str1
[
20
]
 
=
 
"Hello"
;
char
 str2
[]
 
=
 
" World"
;
strcat
(
str1
,
 str2
);
  
// str1 = "Hello World"
// strcmp() - Confronta stringhe
char
 s1
[]
 
=
 
"abc"
;
char
 s2
[]
 
=
 
"abc"
;
char
 s3
[]
 
=
 
"xyz"
;
if
 
(
strcmp
(
s1
,
 s2
)
 
==
 
0
)
 
{
    printf
(
"s1 e s2 sono uguali
\n
"
);
}
// strcmp() ritorna:
//   0  se uguali
//   <0 se s1 < s2
//   >0 se s1 > s2
// strchr() - Cerca carattere
char
 str
[]
 
=
 
"Hello World"
;
char
*
 pos 
=
 strchr
(
str
,
 
'W'
);
  
// pos punta a "World"
// strstr() - Cerca sottostringa
char
*
 pos2 
=
 strstr
(
str
,
 
"World"
);
  
// pos2 punta a "World"
// VERSIONI SICURE (con limite di dimensione)
strncpy
(
dest
,
 src
,
 n
);
   
// Copia max n caratteri
strncat
(
dest
,
 src
,
 n
);
   
// Concatena max n caratteri
strncmp
(
s1
,
 s2
,
 n
);
      
// Confronta max n caratteri
#include 
<stdio.h>
#define RIGHE 
3
#define COLONNE 
3
void
 stampaMatrice
(
int
 mat
[][
COLONNE
],
 
int
 r
,
 
int
 c
)
 
{
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 r
;
 i
++)
 
{
        
for
 
(
int
 j 
=
 
0
;
 j 
<
 c
;
 j
++)
 
{
            printf
(
"
%4d
 "
,
 mat
[
i
][
j
]);
        
}
        printf
(
"
\n
"
);
    
}
    printf
(
"
\n
"
);
}
int
 main
()
 
{
    
int
 matrice
[
RIGHE
][
COLONNE
];
    
    
// Input matrice
    printf
(
"Inserisci gli elementi della matrice 
%d
x
%d
:
\n
"
,
 RIGHE
,
 COLONNE

    
for
 
(
int
 i 
=
 
0
;
 i 
<
 RIGHE
;
 i
++)
 
{
        
for
 
(
int
 j 
=
 
0
;
 j 
<
 COLONNE
;
 j
++)
 
{
            printf
(
"Elemento [
%d
][
%d
]: "
,
 i
,
 j
);
            scanf
(
"
%d
"
,
 
&
matrice
[
i
][
j
]);
        
}
    
}
    
    printf
(
"
\n
Matrice inserita:
\n
"
);
    stampaMatrice
(
matrice
,
 RIGHE
,
 COLONNE
);
    
    
// Somma di tutti gli elementi
    
int
 somma 
=
 
0
;
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 RIGHE
;
 i
++)
 
{
        
for
 
(
int
 j 
=
 
0
;
 j 
<
 COLONNE
;
 j
++)
 
{
            somma 
+=
 matrice
[
i
][
j
];
        
}
    
}
    printf
(
"Somma totale: 
%d\n\n
"
,
 somma
);
    
    
// Somma per righe
    printf
(
"Somma per righe:
\n
"
);
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 RIGHE
;
 i
++)
 
{
        
int
 sommaRiga 
=
 
0
;
        
for
 
(
int
 j 
=
 
0
;
 j 
<
 COLONNE
;
 j
++)
 
{
            sommaRiga 
+=
 matrice
[
i
][
j
];
        
}
        printf
(
"Riga 
%d
: 
%d\n
"
,
 i
,
 sommaRiga
);
    
}
    printf
(
"
\n
"
);
    
    
// Somma per colonne
    printf
(
"Somma per colonne:
\n
"
);
    
for
 
(
int
 j 
=
 
0
;
 j 
<
 COLONNE
;
 j
++)
 
{
        
int
 sommaColonna 
=
 
0
;
        
for
 
(
int
 i 
=
 
0
;
 i 
<
 RIGHE
;
 i
++)
 
{
            sommaColonna 
+=
 matrice
[
i
][
j
];
        
}
        printf
(
"Colonna 
%d
: 
%d\n
"
,
 j
,
 sommaColonna
);
    
}
    printf
(
"
\n
"
);
    
    
// Diagonale principale
    printf
(
"Diagonale principale: "
);
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 RIGHE
;
 i
++)
 
{
        printf
(
"
%d
 "
,
 matrice
[
i
][
i
]);
    
}
    printf
(
"
\n
"
);
    
    
// Diagonale secondaria
    printf
(
"Diagonale secondaria: "
);
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 RIGHE
;
 i
++)
 
{
        printf
(
"
%d
 "
,
 matrice
[
i
][
COLONNE 
-
 
1
 
-
 i
]);
    
}
    printf
(
"
\n\n
"
);
    
    
// Elemento massimo e minimo
    
int
 max 
=
 matrice
[
0
][
0
],
 min 
=
 matrice
[
0
][
0
];
    
int
 maxI 
=
 
0
,
 maxJ 
=
 
0
,
 minI 
=
 
0
,
 minJ 
=
 
0
;
    
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 RIGHE
;
 i
++)
 
{
        
for
 
(
int
 j 
=
 
0
;
 j 
<
 COLONNE
;
 j
++)
 
{
            
if
 
(
matrice
[
i
][
j
]
 
>
 max
)
 
{
                max 
=
 matrice
[
i
][
j
];
                maxI 
=
 i
;
                maxJ 
=
 j
;
            
}
            
if
 
(
matrice
[
i
][
j
]
 
<
 min
)
 
{
                min 
=
 matrice
[
i
][
j
];
                minI 
=
 i
;
                minJ 
=
 j
;

Esercizio 2: Trasposizione di Matrice
                minJ 
=
 j
;
            
}
        
}
    
}
    
    printf
(
"Massimo: 
%d
 in posizione [
%d
][
%d
]
\n
"
,
 max
,
 maxI
,
 maxJ
);
    printf
(
"Minimo: 
%d
 in posizione [
%d
][
%d
]
\n
"
,
 min
,
 minI
,
 minJ
);
    
    
return
 
0
;
}
#include 
<stdio.h>
#define RIGHE 
3
#define COLONNE 
4
void
 stampaMatrice
(
int
 mat
[][
COLONNE
],
 
int
 r
,
 
int
 c
)
 
{
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 r
;
 i
++)
 
{
        
for
 
(
int
 j 
=
 
0
;
 j 
<
 c
;
 j
++)
 
{
            printf
(
"
%4d
 "
,
 mat
[
i
][
j
]);
        
}
        printf
(
"
\n
"
);
    
}
}
void
 stampaMatriceTr
(
int
 mat
[][
RIGHE
],
 
int
 r
,
 
int
 c
)
 
{
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 r
;
 i
++)
 
{
        
for
 
(
int
 j 
=
 
0
;
 j 
<
 c
;
 j
++)
 
{
            printf
(
"
%4d
 "
,
 mat
[
i
][
j
]);
        
}
        printf
(
"
\n
"
);
    
}
}
int
 main
()
 
{
    
int
 matrice
[
RIGHE
][
COLONNE
]
 
=
 
{
        
{
1
,
 
2
,
 
3
,
 
4
},
        
{
5
,
 
6
,
 
7
,
 
8
},
        
{
9
,
 
10
,
 
11
,
 
12
}
    
};
    
    
int
 trasposta
[
COLONNE
][
RIGHE
];
    
    printf
(
"Matrice originale (
%d
x
%d
):
\n
"
,
 RIGHE
,
 COLONNE
);
    stampaMatrice
(
matrice
,
 RIGHE
,
 COLONNE
);
    
    
// Trasposizione
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 RIGHE
;
 i
++)
 
{
        
for
 
(
int
 j 
=
 
0
;
 j 
<
 COLONNE
;
 j
++)
 
{
            trasposta
[
j
][
i
]
 
=
 matrice
[
i
][
j
];
        
}
    
}
    
    printf
(
"
\n
Matrice trasposta (
%d
x
%d
):
\n
"
,
 COLONNE
,
 RIGHE
);
    stampaMatriceTr
(
trasposta
,
 COLONNE
,
 RIGHE
);
    
    
// Verifica trasposizione
    printf
(
"
\n
Verifica: trasposta[1][2] = matrice[2][1]
\n
"
);
    printf
(
"trasposta[1][2] = 
%d
, matrice[2][1] = 
%d\n
"
,
 
           trasposta
[
1
][
2
],
 matrice
[
2
][
1
]);
    
    
return
 
0
;
}

Esercizio 3: Somma di Matrici
Esercizio 4: Manipolazione di Stringhe Base
#include 
<stdio.h>
#define DIM 
3
void
 inputMatrice
(
int
 mat
[][
DIM
],
 
int
 dim
,
 
const
 
char
*
 nome
)
 
{
    printf
(
"Inserisci elementi di 
%s
:
\n
"
,
 nome
);
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 dim
;
 i
++)
 
{
        
for
 
(
int
 j 
=
 
0
;
 j 
<
 dim
;
 j
++)
 
{
            printf
(
"
%s
[
%d
][
%d
]: "
,
 nome
,
 i
,
 j
);
            scanf
(
"
%d
"
,
 
&
mat
[
i
][
j
]);
        
}
    
}
}
void
 stampaMatrice
(
int
 mat
[][
DIM
],
 
int
 dim
,
 
const
 
char
*
 nome
)
 
{
    printf
(
"
\n%s
:
\n
"
,
 nome
);
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 dim
;
 i
++)
 
{
        
for
 
(
int
 j 
=
 
0
;
 j 
<
 dim
;
 j
++)
 
{
            printf
(
"
%4d
 "
,
 mat
[
i
][
j
]);
        
}
        printf
(
"
\n
"
);
    
}
}
void
 sommaMatrici
(
int
 A
[][
DIM
],
 
int
 B
[][
DIM
],
 
int
 C
[][
DIM
],
 
int
 dim
)
 
{
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 dim
;
 i
++)
 
{
        
for
 
(
int
 j 
=
 
0
;
 j 
<
 dim
;
 j
++)
 
{
            C
[
i
][
j
]
 
=
 A
[
i
][
j
]
 
+
 B
[
i
][
j
];
        
}
    
}
}
int
 main
()
 
{
    
int
 A
[
DIM
][
DIM
],
 B
[
DIM
][
DIM
],
 C
[
DIM
][
DIM
];
    
    inputMatrice
(
A
,
 DIM
,
 
"Matrice A"
);
    inputMatrice
(
B
,
 DIM
,
 
"Matrice B"
);
    
    sommaMatrici
(
A
,
 B
,
 C
,
 DIM
);
    
    stampaMatrice
(
A
,
 DIM
,
 
"Matrice A"
);
    stampaMatrice
(
B
,
 DIM
,
 
"Matrice B"
);
    stampaMatrice
(
C
,
 DIM
,
 
"Matrice C (A+B)"
);
    
    
return
 
0
;
}

Esercizio 5: Conteggio Caratteri e Parole
#include 
<stdio.h>
#include 
<string.h>
int
 main
()
 
{
    
char
 str1
[
100
],
 str2
[
100
],
 str3
[
200
];
    
    
// Input stringhe
    printf
(
"Inserisci la prima stringa: "
);
    fgets
(
str1
,
 
sizeof
(
str1
),
 stdin
);
    str1
[
strcspn
(
str1
,
 
"
\n
"
)]
 
=
 
'
\0
'
;
  
// Rimuove '\n'
    
    printf
(
"Inserisci la seconda stringa: "
);
    fgets
(
str2
,
 
sizeof
(
str2
),
 stdin
);
    str2
[
strcspn
(
str2
,
 
"
\n
"
)]
 
=
 
'
\0
'
;
    
    
// Lunghezza
    printf
(
"
\n
Lunghezza str1: 
%lu
 caratteri
\n
"
,
 strlen
(
str1
));
    printf
(
"Lunghezza str2: 
%lu
 caratteri
\n
"
,
 strlen
(
str2
));
    
    
// Copia
    strcpy
(
str3
,
 str1
);
    printf
(
"
\n
str3 (copia di str1): 
%s\n
"
,
 str3
);
    
    
// Concatenazione
    strcat
(
str3
,
 
" "
);
    strcat
(
str3
,
 str2
);
    printf
(
"str3 (concatenazione): 
%s\n
"
,
 str3
);
    
    
// Confronto
    printf
(
"
\n
Confronto str1 e str2:
\n
"
);
    
int
 risultato 
=
 strcmp
(
str1
,
 str2
);
    
if
 
(
risultato 
==
 
0
)
 
{
        printf
(
"Le stringhe sono uguali
\n
"
);
    
}
 
else
 
if
 
(
risultato 
<
 
0
)
 
{
        printf
(
"str1 < str2 (lessicograficamente)
\n
"
);
    
}
 
else
 
{
        printf
(
"str1 > str2 (lessicograficamente)
\n
"
);
    
}
    
    
// Ricerca carattere
    printf
(
"
\n
Inserisci un carattere da cercare in str1: "
);
    
char
 ch
;
    scanf
(
" 
%c
"
,
 
&
ch
);
    
    
char
*
 pos 
=
 strchr
(
str1
,
 ch
);
    
if
 
(
pos 
!=
 NULL
)
 
{
        printf
(
"Carattere '
%c
' trovato in posizione 
%ld\n
"
,
 ch
,
 pos 
-
 str1
    
}
 
else
 
{
        printf
(
"Carattere '
%c
' non trovato
\n
"
,
 ch
);
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
#include 
<string.h>
#include 
<ctype.h>
int
 main
()
 
{
    
char
 testo
[
1000
];
    
    printf
(
"Inserisci un testo (max 999 caratteri):
\n
"
);
    fgets
(
testo
,
 
sizeof
(
testo
),
 stdin
);
    testo
[
strcspn
(
testo
,
 
"
\n
"
)]
 
=
 
'
\0
'
;
    

    
    
// Statistiche
    
int
 lunghezza 
=
 strlen
(
testo
);
    
int
 lettere 
=
 
0
,
 cifre 
=
 
0
,
 spazi 
=
 
0
,
 punteggiatura 
=
 
0
,
 altri 
=
 
0
;
    
int
 vocali 
=
 
0
,
 consonanti 
=
 
0
;
    
int
 parole 
=
 
0
;
    
    
// Conteggi
    
int
 inParola 
=
 
0
;
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 lunghezza
;
 i
++)
 
{
        
char
 c 
=
 testo
[
i
];
        
        
// Conta parole
        
if
 
(
isspace
(
c
))
 
{
            spazi
++;
            inParola 
=
 
0
;
        
}
 
else
 
{
            
if
 
(!
inParola
)
 
{
                parole
++;
                inParola 
=
 
1
;
            
}
        
}
        
        
// Classifica caratteri
        
if
 
(
isalpha
(
c
))
 
{
            lettere
++;
            
char
 lower 
=
 tolower
(
c
);
            
if
 
(
lower 
==
 
'a'
 
||
 lower 
==
 
'e'
 
||
 lower 
==
 
'i'
 
||
 
                lower 
==
 
'o'
 
||
 lower 
==
 
'u'
)
 
{
                vocali
++;
            
}
 
else
 
{
                consonanti
++;
            
}
        
}
 
else
 
if
 
(
isdigit
(
c
))
 
{
            cifre
++;
        
}
 
else
 
if
 
(
ispunct
(
c
))
 
{
            punteggiatura
++;
        
}
 
else
 
if
 
(!
isspace
(
c
))
 
{
            altri
++;
        
}
    
}
    
    
// Output statistiche
    printf
(
"
\n
=== STATISTICHE ===
\n
"
);
    printf
(
"Lunghezza totale: 
%d
 caratteri
\n
"
,
 lunghezza
);
    printf
(
"Numero di parole: 
%d\n
"
,
 parole
);
    printf
(
"
\n
Caratteri:
\n
"
);
    printf
(
"  Lettere: 
%d
 (vocali: 
%d
, consonanti: 
%d
)
\n
"
,
 lettere
,
 vocali
    printf
(
"  Cifre: 
%d\n
"
,
 cifre
);
    printf
(
"  Spazi: 
%d\n
"
,
 spazi
);
    printf
(
"  Punteggiatura: 
%d\n
"
,
 punteggiatura
);
    printf
(
"  Altri: 
%d\n
"
,
 altri
);
    
    
// Frequenza lettere
    
int
 frequenza
[
26
]
 
=
 
{
0
};
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 lunghezza
;
 i
++)
 
{
        
if
 
(
isalpha
(
testo
[
i
]))
 
{
            frequenza
[
tolower
(
testo
[
i
])
 
-
 
'a'
]++;
        
}
    
}
    
    printf
(
"
\n
Frequenza lettere:
\n
"
);
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 
26
;
 i
++)
 
{
        
if
 
(
frequenza
[
i
]
 
>
 
0
)
 
{
            printf
(
"
%c
: 
%d
 "
,
 
'a'
 
+
 i
,
 frequenza
[
i
]);
        
}
    
}
    printf
(
"
\n
"
);
    
    
return
 
0
;
}

Esercizi da svolgere autonomamente:
1
. 
Matrice identità
: Crea e verifica se una matrice è una matrice identità
2
. 
Prodotto matrici
: Implementa il prodotto tra due matrici compatibili
3
. 
Matrice simmetrica
: Verifica se una matrice è simmetrica rispetto alla diagonale
principale
4
. 
Palindromo
: Verifica se una stringa è palindroma (si legge uguale al contrario)
5
. 
Inversione stringa
: Inverti i caratteri di una stringa senza usare funzioni di libreria
6
. 
Conta occorrenze
: Data una stringa e una sottostringa, conta quante volte appare
7
. 
Rimozione spazi
: Rimuovi tutti gli spazi da una stringa
8
. 
Cifrario di Cesare
: Implementa il cifrario di Cesare (shift di caratteri)
9
. 
Anagrammi
: Verifica se due stringhe sono anagrammi l’una dell’altra
10
. 
Serpente in matrice
: Riempi una matrice NxN con numeri da 1 a N² a serpente (zig-
zag)
Riepilogo Concetti Chiave
✓
 Le 
matrici
 sono array bidimensionali: 
tipo[righe][colonne]
✓
 Accesso: 
matrice[i][j]
 con cicli annidati
✓
 Le 
stringhe
 sono array di char terminati da 
‘\0’
✓
 Funzioni string.h: strlen, strcpy, strcat, strcmp
✓
 Usare 
fgets()
 per input sicuro di stringhe
✓
 Il terminatore ‘\0’ è fondamentale per le stringhe
Prossima lezione
: Approfondiremo le 
funzioni
 in C - parte 1!
}


---

# lezione 15 funzioni1

**File:** `lezione 15 funzioni1.pdf`
**Tipo:** `.pdf`
**Dimensione:** 355.2 KB
**Ultima modifica:** 02/07/2026 09:24

---

LEZIONE 15 - Funzioni: Parte 1
PARTE TEORICA (2h)
1. Concetto di Funzione e Modularità
Una 
funzione
 è un blocco di codice riutilizzabile che esegue un compito specifico. Le
funzioni sono il fondamento della 
programmazione modulare
.
Vantaggi delle funzioni:
 - 
Riutilizzabilità
: scrivi una volta, usa molte volte - 
Modularità
:
divide programmi complessi in parti gestibili - 
Manutenibilità
: più facile trovare e
correggere errori - 
Leggibilità
: codice più chiaro e organizzato - 
Testing
: puoi testare
singole funzioni - 
Collaborazione
: diversi programmatori su funzioni diverse
Analogia della vita reale:
Preparare una pizza:
├─ Preparare l'impasto()
├─ Stendere la pasta()
├─ Aggiungere ingredienti()
└─ Cuocere in forno()
Ogni fase è una "funzione" con un compito specifico!
Esempio senza funzioni (codice duplicato):
Esempio con funzioni (codice riutilizzabile):
2. Definizione e Dichiarazione
Struttura di una funzione:
// Calcolo area rettangolo 1
int
 base1 
=
 
5
,
 altezza1 
=
 
3
;
int
 area1 
=
 base1 
*
 altezza1
;
printf
(
"Area 1: 
%d\n
"
,
 area1
);
// Calcolo area rettangolo 2
int
 base2 
=
 
8
,
 altezza2 
=
 
4
;
int
 area2 
=
 base2 
*
 altezza2
;
printf
(
"Area 2: 
%d\n
"
,
 area2
);
// Calcolo area rettangolo 3
int
 base3 
=
 
10
,
 altezza3 
=
 
6
;
int
 area3 
=
 base3 
*
 altezza3
;
printf
(
"Area 3: 
%d\n
"
,
 area3
);
int
 calcolaArea
(
int
 base
,
 
int
 altezza
)
 
{
    
return
 base 
*
 altezza
;
}
int
 main
()
 
{
    printf
(
"Area 1: 
%d\n
"
,
 calcolaArea
(
5
,
 
3
));
    printf
(
"Area 2: 
%d\n
"
,
 calcolaArea
(
8
,
 
4
));
    printf
(
"Area 3: 
%d\n
"
,
 calcolaArea
(
10
,
 
6
));
    
return
 
0
;
}

Componenti:
 1. 
Tipo di ritorno
: tipo del valore restituito (int, float, void, ecc.) 2. 
Nome
della funzione
: identificatore univoco (convenzioni camelCase o snake_case) 3.
Parametri
: input della funzione (opzionali) 4. 
Corpo
: blocco di codice tra {} 5. 
Return
:
restituisce un valore (obbligatorio se tipo != void)
Esempi:
Dichiarazione vs Definizione:
3. Parametri Formali e Attuali
tipoRitorno nomeFunzione
(
parametro1
,
 parametro2
,
 
...)
 
{
    
// corpo della funzione
    
// istruzioni
    
return
 valore
;
  
// se tipoRitorno != void
}
// Funzione che calcola la somma di due numeri
int
 somma
(
int
 a
,
 
int
 b
)
 
{
    
int
 risultato 
=
 a 
+
 b
;
    
return
 risultato
;
}
// Funzione che stampa un saluto (nessun ritorno)
void
 saluta
(
char
 nome
[])
 
{
    printf
(
"Ciao, 
%s
!
\n
"
,
 nome
);
    
// Non serve return
}
// Funzione senza parametri
int
 getNumeroFisso
()
 
{
    
return
 
42
;
}
// Funzione che verifica se un numero è pari
int
 isPari
(
int
 n
)
 
{
    
return
 
(
n 
%
 
2
 
==
 
0
);
  
// Ritorna 1 (vero) o 0 (falso)
}
// DICHIARAZIONE (prototipo): dice al compilatore che la funzione esiste
int
 somma
(
int
 a
,
 
int
 b
);
// DEFINIZIONE: implementa la funzione
int
 somma
(
int
 a
,
 
int
 b
)
 
{
    
return
 a 
+
 b
;
}
// Esempio completo
#include 
<stdio.h>
// Dichiarazioni (in alto)
int
 somma
(
int
 a
,
 
int
 b
);
int
 prodotto
(
int
 a
,
 
int
 b
);
int
 main
()
 
{
    printf
(
"
%d\n
"
,
 somma
(
5
,
 
3
));
      
// 8
    printf
(
"
%d\n
"
,
 prodotto
(
5
,
 
3
));
   
// 15
    
return
 
0
;
}
// Definizioni (dopo main)
int
 somma
(
int
 a
,
 
int
 b
)
 
{
    
return
 a 
+
 b
;
}
int
 prodotto
(
int
 a
,
 
int
 b
)
 
{
    
return
 a 
*
 b
;
}

Parametri formali
: variabili nella definizione della funzione 
Parametri attuali (o
argomenti)
: valori passati quando si chiama la funzione
Corrispondenza parametri:
ATTENZIONE all’ordine:
4. Return: Restituzione del Valore
Il comando 
return
 termina l’esecuzione della funzione e restituisce un valore al chiamante.
Sintassi:
Esempi:
// a e b sono PARAMETRI FORMALI
int
 somma
(
int
 a
,
 
int
 b
)
 
{
    
return
 a 
+
 b
;
}
int
 main
()
 
{
    
int
 x 
=
 
10
,
 y 
=
 
20
;
    
    
// x e y sono PARAMETRI ATTUALI (argomenti)
    
int
 risultato 
=
 somma
(
x
,
 y
);
    
    
// 5 e 3 sono PARAMETRI ATTUALI (valori letterali)
    
int
 risultato2 
=
 somma
(
5
,
 
3
);
    
    
return
 
0
;
}
int
 calcola
(
int
 primo
,
 
int
 secondo
,
 
int
 terzo
)
 
{
    
return
 primo 
+
 secondo 
*
 terzo
;
}
int
 main
()
 
{
    
int
 risultato 
=
 calcola
(
10
,
 
5
,
 
2
);
    
// primo = 10
    
// secondo = 5
    
// terzo = 2
    
// ritorna: 10 + 5 * 2 = 20
    
    
return
 
0
;
}
int
 sottrai
(
int
 a
,
 
int
 b
)
 
{
    
return
 a 
-
 b
;
}
int
 main
()
 
{
    printf
(
"
%d\n
"
,
 sottrai
(
10
,
 
3
));
  
// 7
    printf
(
"
%d\n
"
,
 sottrai
(
3
,
 
10
));
  
// -7 (DIVERSO!)
    
return
 
0
;
}
return
 espressione
;

Funzioni void (senza return):
ERRORI COMUNI:
// Return con valore semplice
int
 getNumero
()
 
{
    
return
 
42
;
}
// Return con espressione
int
 quadrato
(
int
 n
)
 
{
    
return
 n 
*
 n
;
}
// Return con calcolo
int
 massimo
(
int
 a
,
 
int
 b
)
 
{
    
if
 
(
a 
>
 b
)
 
{
        
return
 a
;
    
}
 
else
 
{
        
return
 b
;
    
}
}
// Return multipli (la funzione esce al primo return)
int
 segno
(
int
 n
)
 
{
    
if
 
(
n 
>
 
0
)
 
return
 
1
;
    
if
 
(
n 
<
 
0
)
 
return
 
-
1
;
    
return
 
0
;
}
// Return anticipato
int
 divide
(
int
 a
,
 
int
 b
)
 
{
    
if
 
(
b 
==
 
0
)
 
{
        printf
(
"Errore: divisione per zero!
\n
"
);
        
return
 
0
;
  
// Esce subito
    
}
    
return
 a 
/
 b
;
}
void
 stampaQuadrato
(
int
 n
)
 
{
    printf
(
"
%d\n
"
,
 n 
*
 n
);
    
// Non serve return
}
void
 stampaMessaggio
()
 
{
    printf
(
"Ciao!
\n
"
);
    
return
;
  
// Opzionale, esce dalla funzione
}
void
 esempio
(
int
 x
)
 
{
    
if
 
(
x 
<
 
0
)
 
{
        printf
(
"Numero negativo!
\n
"
);
        
return
;
  
// Esce subito senza fare altro
    
}
    printf
(
"Numero valido: 
%d\n
"
,
 x
);
}

5. Passaggio per Valore
In C, i parametri vengono passati 
per valore
: la funzione riceve una 
copia
 dei dati, non gli
originali.
Conseguenza
: modificare un parametro NON modifica la variabile originale.
Spiegazione visiva:
main():                   incrementa():
┌──────────┐             ┌──────────┐
│ numero=10│ ────copia──→│   x=10   │
└──────────┘             └──────────┘
                              ↓
                         x diventa 11
                              ↓
                         funzione termina
                         x viene distrutto
                              
numero rimane 10!
Come restituire il valore modificato:
// ERRORE: funzione int senza return
int
 sbagliata
()
 
{
    
int
 x 
=
 
10
;
    
// Manca return! Comportamento indefinito
}
// ERRORE: tipo di ritorno sbagliato
int
 altraFunzione
()
 
{
    
return
 
3.14
;
  
// Ritorna int, ma 3.14 è float (viene troncato a 3)
}
// CORRETTO: conversione esplicita
float
 funzioneFloat
()
 
{
    
return
 
3.14
;
  
// OK, tipo corretto
}
void
 incrementa
(
int
 x
)
 
{
    x 
=
 x 
+
 
1
;
    printf
(
"Dentro la funzione: x = 
%d\n
"
,
 x
);
}
int
 main
()
 
{
    
int
 numero 
=
 
10
;
    
    incrementa
(
numero
);
    
// Output: Dentro la funzione: x = 11
    
    printf
(
"Fuori dalla funzione: numero = 
%d\n
"
,
 numero
);
    
// Output: Fuori dalla funzione: numero = 10
    
// numero NON è cambiato!
    
    
return
 
0
;
}
// Soluzione: usare return
int
 incrementa
(
int
 x
)
 
{
    
return
 x 
+
 
1
;
}
int
 main
()
 
{
    
int
 numero 
=
 
10
;
    numero 
=
 incrementa
(
numero
);
  
// Assegna il nuovo valore
    printf
(
"numero = 
%d\n
"
,
 numero
);
  
// Output: 11
    
return
 
0
;
}

Passaggio di array (caso speciale):
6. Scope delle Variabili
Lo 
scope
 (ambito) di una variabile definisce dove può essere usata.
Tipi di scope:
1. Variabili locali (dentro funzioni):
2. Variabili globali (fuori da tutte le funzioni):
3. Parametri (locali alla funzione):
void
 modificaArray
(
int
 arr
[],
 
int
 dim
)
 
{
    arr
[
0
]
 
=
 
999
;
  
// Questo MODIFICA l'array originale!
}
int
 main
()
 
{
    
int
 numeri
[]
 
=
 
{
1
,
 
2
,
 
3
};
    modificaArray
(
numeri
,
 
3
);
    printf
(
"
%d\n
"
,
 numeri
[
0
]);
  
// Output: 999
    
// Gli array vengono passati per riferimento (vedremo meglio dopo)
    
return
 
0
;
}
void
 funzione1
()
 
{
    
int
 x 
=
 
10
;
  
// x è locale a funzione1
    printf
(
"
%d\n
"
,
 x
);
  
// OK
}
void
 funzione2
()
 
{
    printf
(
"
%d\n
"
,
 x
);
  
// ERRORE! x non esiste qui
}
int
 main
()
 
{
    printf
(
"
%d\n
"
,
 x
);
  
// ERRORE! x non esiste qui
    funzione1
();
    
return
 
0
;
}
#include 
<stdio.h>
int
 globale 
=
 
100
;
  
// Variabile globale
void
 stampa
()
 
{
    printf
(
"globale = 
%d\n
"
,
 globale
);
  
// OK
}
void
 modifica
()
 
{
    globale 
=
 
200
;
  
// OK, modifica la variabile globale
}
int
 main
()
 
{
    printf
(
"globale = 
%d\n
"
,
 globale
);
  
// 100
    modifica
();
    printf
(
"globale = 
%d\n
"
,
 globale
);
  
// 200
    stampa
();
                            
// 200
    
return
 
0
;
}

Shadowing (ombreggiamento):
Best practices:
 - Preferisci variabili locali - Usa variabili globali solo se necessario - Evita
nomi ambigui che causano shadowing - Ogni funzione dovrebbe avere responsabilità chiare
PARTE PRATICA (2h)
Esercizio 1: Funzioni Matematiche Base
void
 funzione
(
int
 param
)
 
{
    param 
=
 
100
;
  
// param è locale
    printf
(
"
%d\n
"
,
 param
);
}
int
 main
()
 
{
    funzione
(
50
);
    
// printf("%d\n", param);  // ERRORE! param non esiste qui
    
return
 
0
;
}
int
 x 
=
 
100
;
  
// Globale
void
 funzione
()
 
{
    
int
 x 
=
 
50
;
  
// Locale, "nasconde" la globale
    printf
(
"x locale = 
%d\n
"
,
 x
);
  
// 50
}
int
 main
()
 
{
    printf
(
"x globale = 
%d\n
"
,
 x
);
  
// 100
    funzione
();
                     
// 50
    printf
(
"x globale = 
%d\n
"
,
 x
);
  
// 100 (globale non modificata)
    
return
 
0
;
}

Esercizio 2: Funzioni per Validazione
#include 
<stdio.h>
// Dichiarazioni
int
 somma
(
int
 a
,
 
int
 b
);
int
 sottrazione
(
int
 a
,
 
int
 b
);
int
 moltiplicazione
(
int
 a
,
 
int
 b
);
float
 divisione
(
int
 a
,
 
int
 b
);
int
 potenza
(
int
 base
,
 
int
 esponente
);
int
 fattoriale
(
int
 n
);
int
 main
()
 
{
    
int
 x 
=
 
10
,
 y 
=
 
5
;
    
    printf
(
"=== CALCOLATRICE ===
\n
"
);
    printf
(
"
%d
 + 
%d
 = 
%d\n
"
,
 x
,
 y
,
 somma
(
x
,
 y
));
    printf
(
"
%d
 - 
%d
 = 
%d\n
"
,
 x
,
 y
,
 sottrazione
(
x
,
 y
));
    printf
(
"
%d
 * 
%d
 = 
%d\n
"
,
 x
,
 y
,
 moltiplicazione
(
x
,
 y
));
    printf
(
"
%d
 / 
%d
 = 
%.2f\n
"
,
 x
,
 y
,
 divisione
(
x
,
 y
));
    printf
(
"
%d
 ^ 
%d
 = 
%d\n
"
,
 x
,
 y
,
 potenza
(
x
,
 y
));
    printf
(
"
%d
! = 
%d\n
"
,
 y
,
 fattoriale
(
y
));
    
    
return
 
0
;
}
// Definizioni
int
 somma
(
int
 a
,
 
int
 b
)
 
{
    
return
 a 
+
 b
;
}
int
 sottrazione
(
int
 a
,
 
int
 b
)
 
{
    
return
 a 
-
 b
;
}
int
 moltiplicazione
(
int
 a
,
 
int
 b
)
 
{
    
return
 a 
*
 b
;
}
float
 divisione
(
int
 a
,
 
int
 b
)
 
{
    
if
 
(
b 
==
 
0
)
 
{
        printf
(
"Errore: divisione per zero!
\n
"
);
        
return
 
0
.0
;
    
}
    
return
 
(
float
)
a 
/
 b
;
}
int
 potenza
(
int
 base
,
 
int
 esponente
)
 
{
    
int
 risultato 
=
 
1
;
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 esponente
;
 i
++)
 
{
        risultato 
*=
 base
;
    
}
    
return
 risultato
;
}
int
 fattoriale
(
int
 n
)
 
{
    
if
 
(
n 
<
 
0
)
 
return
 
-
1
;
  
// Errore
    
if
 
(
n 
==
 
0
 
||
 n 
==
 
1
)
 
return
 
1
;
    
    
int
 risultato 
=
 
1
;
    
for
 
(
int
 i 
=
 
2
;
 i 
<=
 n
;
 i
++)
 
{
        risultato 
*=
 i
;
    
}
    
return
 risultato
;
}

#include 
<stdio.h>
// Dichiarazioni
int
 isPari
(
int
 n
);
int
 isDispari
(
int
 n
);
int
 isPrimo
(
int
 n
);
int
 isPerfetto
(
int
 n
);
int
 isPositivo
(
int
 n
);
int
 isNegativo
(
int
 n
);
int
 main
()
 
{
    
int
 numeri
[]
 
=
 
{
2
,
 
7
,
 
15
,
 
28
,
 
-
5
,
 
0
,
 
11
,
 
6
};
    
int
 dim 
=
 
8
;
    
    printf
(
"=== VALIDAZIONE NUMERI ===
\n\n
"
);
    
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 dim
;
 i
++)
 
{
        
int
 n 
=
 numeri
[
i
];
        printf
(
"Numero: 
%d\n
"
,
 n
);
        printf
(
"  Pari: 
%s\n
"
,
 isPari
(
n
)
 
?
 
"SI"
 
:
 
"NO"
);
        printf
(
"  Dispari: 
%s\n
"
,
 isDispari
(
n
)
 
?
 
"SI"
 
:
 
"NO"
);
        printf
(
"  Primo: 
%s\n
"
,
 isPrimo
(
n
)
 
?
 
"SI"
 
:
 
"NO"
);
        printf
(
"  Perfetto: 
%s\n
"
,
 isPerfetto
(
n
)
 
?
 
"SI"
 
:
 
"NO"
);
        printf
(
"  Positivo: 
%s\n
"
,
 isPositivo
(
n
)
 
?
 
"SI"
 
:
 
"NO"
);
        printf
(
"
\n
"
);
    
}
    
    
return
 
0
;
}
// Definizioni
int
 isPari
(
int
 n
)
 
{
    
return
 n 
%
 
2
 
==
 
0
;
}
int
 isDispari
(
int
 n
)
 
{
    
return
 n 
%
 
2
 
!=
 
0
;
}
int
 isPrimo
(
int
 n
)
 
{
    
if
 
(
n 
<
 
2
)
 
return
 
0
;
    
if
 
(
n 
==
 
2
)
 
return
 
1
;
    
if
 
(
n 
%
 
2
 
==
 
0
)
 
return
 
0
;
    
    
for
 
(
int
 i 
=
 
3
;
 i 
*
 i 
<=
 n
;
 i 
+=
 
2
)
 
{
        
if
 
(
n 
%
 i 
==
 
0
)
 
return
 
0
;
    
}
    
return
 
1
;
}
int
 isPerfetto
(
int
 n
)
 
{
    
if
 
(
n 
<=
 
0
)
 
return
 
0
;
    
    
int
 somma 
=
 
0
;
    
for
 
(
int
 i 
=
 
1
;
 i 
<
 n
;
 i
++)
 
{
        
if
 
(
n 
%
 i 
==
 
0
)
 
{
            somma 
+=
 i
;
        
}
    
}
    
return
 somma 
==
 n
;
}
int
 isPositivo
(
int
 n
)
 
{
    
return
 n 
>
 
0
;
}
int
 isNegativo
(
int
 n
)
 
{
    
return
 n 
<
 
0
;
}

Esercizio 3: Funzioni per Array
#include 
<stdio.h>
#define MAX 
100
// Dichiarazioni
void
 stampaArray
(
int
 arr
[],
 
int
 dim
);
int
 sommaArray
(
int
 arr
[],
 
int
 dim
);
float
 mediaArray
(
int
 arr
[],
 
int
 dim
);
int
 massimoArray
(
int
 arr
[],
 
int
 dim
);
int
 minimoArray
(
int
 arr
[],
 
int
 dim
);
int
 cercaElemento
(
int
 arr
[],
 
int
 dim
,
 
int
 target
);
int
 contaPari
(
int
 arr
[],
 
int
 dim
);
void
 invertiArray
(
int
 arr
[],
 
int
 dim
);
int
 main
()
 
{
    
int
 numeri
[]
 
=
 
{
15
,
 
8
,
 
23
,
 
42
,
 
7
,
 
19
,
 
31
,
 
5
,
 
12
,
 
28
};
    
int
 dim 
=
 
10
;
    
    printf
(
"Array originale:
\n
"
);
    stampaArray
(
numeri
,
 dim
);
    
    printf
(
"
\n
Somma: 
%d\n
"
,
 sommaArray
(
numeri
,
 dim
));
    printf
(
"Media: 
%.2f\n
"
,
 mediaArray
(
numeri
,
 dim
));
    printf
(
"Massimo: 
%d\n
"
,
 massimoArray
(
numeri
,
 dim
));
    printf
(
"Minimo: 
%d\n
"
,
 minimoArray
(
numeri
,
 dim
));
    printf
(
"Numeri pari: 
%d\n
"
,
 contaPari
(
numeri
,
 dim
));
    
    
int
 target 
=
 
19
;
    
int
 pos 
=
 cercaElemento
(
numeri
,
 dim
,
 target
);
    
if
 
(
pos 
!=
 
-
1
)
 
{
        printf
(
"Elemento 
%d
 trovato in posizione 
%d\n
"
,
 target
,
 pos
);
    
}
 
else
 
{
        printf
(
"Elemento 
%d
 non trovato
\n
"
,
 target
);
    
}
    
    printf
(
"
\n
Array invertito:
\n
"
);
    invertiArray
(
numeri
,
 dim
);
    stampaArray
(
numeri
,
 dim
);
    
    
return
 
0
;
}
// Definizioni
void
 stampaArray
(
int
 arr
[],
 
int
 dim
)
 
{
    printf
(
"[ "
);
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 dim
;
 i
++)
 
{
        printf
(
"
%d
 "
,
 arr
[
i
]);
    
}
    printf
(
"]
\n
"
);
}
int
 sommaArray
(
int
 arr
[],
 
int
 dim
)
 
{
    
int
 somma 
=
 
0
;
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 dim
;
 i
++)
 
{
        somma 
+=
 arr
[
i
];
    
}
    
return
 somma
;
}
float
 mediaArray
(
int
 arr
[],
 
int
 dim
)
 
{
    
if
 
(
dim 
==
 
0
)
 
return
 
0
.0
;
    
return
 
(
float
)
sommaArray
(
arr
,
 dim
)
 
/
 dim
;
}
int
 massimoArray
(
int
 arr
[],
 
int
 dim
)
 
{
    
if
 
(
dim 
==
 
0
)
 
return
 
0
;

Esercizio 4: Libreria di Utility
    
    
int
 max 
=
 arr
[
0
];
    
for
 
(
int
 i 
=
 
1
;
 i 
<
 dim
;
 i
++)
 
{
        
if
 
(
arr
[
i
]
 
>
 max
)
 
{
            max 
=
 arr
[
i
];
        
}
    
}
    
return
 max
;
}
int
 minimoArray
(
int
 arr
[],
 
int
 dim
)
 
{
    
if
 
(
dim 
==
 
0
)
 
return
 
0
;
    
    
int
 min 
=
 arr
[
0
];
    
for
 
(
int
 i 
=
 
1
;
 i 
<
 dim
;
 i
++)
 
{
        
if
 
(
arr
[
i
]
 
<
 min
)
 
{
            min 
=
 arr
[
i
];
        
}
    
}
    
return
 min
;
}
int
 cercaElemento
(
int
 arr
[],
 
int
 dim
,
 
int
 target
)
 
{
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 dim
;
 i
++)
 
{
        
if
 
(
arr
[
i
]
 
==
 target
)
 
{
            
return
 i
;
        
}
    
}
    
return
 
-
1
;
  
// Non trovato
}
int
 contaPari
(
int
 arr
[],
 
int
 dim
)
 
{
    
int
 contatore 
=
 
0
;
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 dim
;
 i
++)
 
{
        
if
 
(
arr
[
i
]
 
%
 
2
 
==
 
0
)
 
{
            contatore
++;
        
}
    
}
    
return
 contatore
;
}
void
 invertiArray
(
int
 arr
[],
 
int
 dim
)
 
{
    
for
 
(
int
 i 
=
 
0
;
 i 
<
 dim 
/
 
2
;
 i
++)
 
{
        
int
 temp 
=
 arr
[
i
];
        arr
[
i
]
 
=
 arr
[
dim 
-
 
1
 
-
 i
];
        arr
[
dim 
-
 
1
 
-
 i
]
 
=
 temp
;
    
}
}
#include 
<stdio.h>
#include 
<math.h>
// Dichiarazioni - Conversioni
float
 celsiusToFahrenheit
(
float
 celsius
);
float
 fahrenheitToCelsius
(
float
 fahrenheit
);
float
 kmToMiles
(
float
 km
);
float
 milesToKm
(
float
 miles
);
// Dichiarazioni - Geometria
float
 areaRettangolo
(
float
 base
,
 
float
 altezza
);
float
 areaTriangolo
(
float
 base
,
 
float
 altezza
);
float
 areaCerchio
(
float
 raggio
);
float
 perimetroRettangolo
(
float
 base
,
 
float
 altezza
);
float
 perimetroQuadrato
(
float
 lato
);
float
 circonferenza
(
float
 raggio
);
// Dichiarazioni - Matematica

// Dichiarazioni - Matematica
int
 massimoDi3
(
int
 a
,
 
int
 b
,
 
int
 c
);
int
 minimoDi3
(
int
 a
,
 
int
 b
,
 
int
 c
);
float
 distanza2D
(
float
 x1
,
 
float
 y1
,
 
float
 x2
,
 
float
 y2
);
int
 main
()
 
{
    
// Test conversioni
    printf
(
"=== CONVERSIONI ===
\n
"
);
    printf
(
"25°C = 
%.2f
°F
\n
"
,
 celsiusToFahrenheit
(
25
));
    printf
(
"77°F = 
%.2f
°C
\n
"
,
 fahrenheitToCelsius
(
77
));
    printf
(
"10 km = 
%.2f
 miglia
\n
"
,
 kmToMiles
(
10
));
    printf
(
"5 miglia = 
%.2f
 km
\n
"
,
 milesToKm
(
5
));
    
    
// Test geometria
    printf
(
"
\n
=== GEOMETRIA ===
\n
"
);
    printf
(
"Area rettangolo (5x3): 
%.2f\n
"
,
 areaRettangolo
(
5
,
 
3
));
    printf
(
"Area triangolo (6x4): 
%.2f\n
"
,
 areaTriangolo
(
6
,
 
4
));
    printf
(
"Area cerchio (r=5): 
%.2f\n
"
,
 areaCirc chio
(
5
));
    printf
(
"Perimetro rettangolo (5x3): 
%.2f\n
"
,
 perimetroRettangolo
(
5
,
 
3
));
    
    
// Test matematica
    printf
(
"
\n
=== MATEMATICA ===
\n
"
);
    printf
(
"Massimo tra 10, 25, 18: 
%d\n
"
,
 massimoDi3
(
10
,
 
25
,
 
18
));
    printf
(
"Minimo tra 10, 25, 18: 
%d\n
"
,
 minimoDi3
(
10
,
 
25
,
 
18
));
    printf
(
"Distanza tra (0,0) e (3,4): 
%.2f\n
"
,
 distanza2D
(
0
,
 
0
,
 
3
,
 
4
));
    
    
return
 
0
;
}
// Definizioni - Conversioni
float
 celsiusToFahrenheit
(
float
 celsius
)
 
{
    
return
 celsius 
*
 
9.0
 
/
 
5.0
 
+
 
32.0
;
}
float
 fahrenheitToCelsius
(
float
 fahrenheit
)
 
{
    
return
 
(
fahrenheit 
-
 
32.0
)
 
*
 
5.0
 
/
 
9.0
;
}
float
 kmToMiles
(
float
 km
)
 
{
    
return
 km 
*
 
0
.621371
;
}
float
 milesToKm
(
float
 miles
)
 
{
    
return
 miles 
/
 
0
.621371
;
}
// Definizioni - Geometria
float
 areaRettangolo
(
float
 base
,
 
float
 altezza
)
 
{
    
return
 base 
*
 altezza
;
}
float
 areaTriangolo
(
float
 base
,
 
float
 altezza
)
 
{
    
return
 
(
base 
*
 altezza
)
 
/
 
2.0
;
}
float
 areaCerchio
(
float
 raggio
)
 
{
    
return
 
3.14159
 
*
 raggio 
*
 raggio
;
}
float
 perimetroRettangolo
(
float
 base
,
 
float
 altezza
)
 
{
    
return
 
2
 
*
 
(
base 
+
 altezza
);
}
float
 perimetroQuadrato
(
float
 lato
)
 
{
    
return
 
4
 
*
 lato
;
}
float
 circonferenza
(
float
 raggio
)
 
{
    
return
 
2
 
*
 
3.14159
 
*
 raggio
;
}

Esercizi da svolgere autonomamente:
1
. 
Calcolatrice avanzata
: Crea funzioni per calcolare MCD, mcm, radice quadrata
(approssimata)
2
. 
Funzioni stringhe
: Implementa le tue versioni di strlen, strcpy, strcmp senza usare
string.h
3
. 
Statistiche avanzate
: Crea funzioni per calcolare varianza, deviazione standard,
mediana
4
. 
Validazione password
: Funzione che verifica se una password è valida (lunghezza,
maiuscole, numeri, caratteri speciali)
5
. 
Conversione numeri
: Funzioni per convertire decimale→binario e binario→decimale
6
. 
Giochi
: Crea funzioni per un gioco (es: lancio dadi, morra cinese)
7
. 
Date
: Funzioni per validare date, calcolare giorni tra due date, verificare anno bisestile
8
. 
Ordinamento
: Implementa bubble sort, selection sort in funzioni separate
9
. 
Matrici
: Funzioni per moltiplicare matrici, calcolare determinante, verificare simmetria
10
. 
Menu interattivo
: Crea un menu che chiama diverse funzioni in base alla scelta
dell’utente
Riepilogo Concetti Chiave
✓
 Le 
funzioni
 rendono il codice modulare e riutilizzabile
✓
 Struttura: 
tipo nome(parametri) { corpo; return valore; }
✓
 
Dichiarazione
 (prototipo) vs 
Definizione
 (implementazione)
✓
 
Parametri formali
 nella definizione, 
parametri attuali
 nella chiamata
✓
 
Passaggio per valore
: la funzione riceve una copia
✓
 
Scope
: variabili locali vs globali
Prossima lezione
: Approfondiremo le 
funzioni ricorsive
, prototipazione, variabili static e
best practices!
// Definizioni - Matematica
int
 massimoDi3
(
int
 a
,
 
int
 b
,
 
int
 c
)
 
{
    
int
 max 
=
 a
;
    
if
 
(
b 
>
 max
)
 max 
=
 b
;
    
if
 
(
c 
>
 max
)
 max 
=
 c
;
    
return
 max
;
}
int
 minimoDi3
(
int
 a
,
 
int
 b
,
 
int
 c
)
 
{
    
int
 min 
=
 a
;
    
if
 
(
b 
<
 min
)
 min 
=
 b
;
    
if
 
(
c 
<
 min
)
 min 
=
 c
;
    
return
 min
;
}
float
 distanza2D
(
float
 x1
,
 
float
 y1
,
 
float
 x2
,
 
float
 y2
)
 
{
    
float
 dx 
=
 x2 
-
 x1
;
    
float
 dy 
=
 y2 
-
 y1
;
    
return
 sqrt
(
dx 
*
 dx 
+
 dy 
*
 dy
);
}


---

# lezione1 programmazione

**File:** `lezione1 programmazione.pdf`
**Tipo:** `.pdf`
**Dimensione:** 59.9 KB
**Ultima modifica:** 02/07/2026 09:11

---

LEZIONE 1 - Introduzione alla
Programmazione e agli Algoritmi
Durata: 4 ore | Teoria: 2h | Esercizi: 2h
PARTE TEORICA (2 ore)
1.1 Cos’è un Programma e la Programmazione (20 min)
Definizione di Programma
Un programma è una sequenza di istruzioni che un computer può eseguire per
risolvere un problema o svolgere un compito specifico. Possiamo pensare al programma
come a una “ricetta” che il computer segue passo dopo passo.
Esempi nella vita quotidiana:
Una ricetta di cucina è un “programma” per preparare un piatto
Le istruzioni di montaggio di un mobile IKEA
Le indicazioni stradali per raggiungere una destinazione
Cos’è la Programmazione?
La programmazione è l’attività di:
Analizzare un problema
Progettare una soluzione
Tradurre la soluzione in un linguaggio comprensibile al computer
Verificare che la soluzione funzioni correttamente
Il processo di sviluppo software:
Problema → Analisi → Algoritmo → Codice → Test → Soluzione
• 
• 
• 
1. 
2. 
3. 
4. 

1.2 Hardware e Software: Panoramica Generale (20 min)
Hardware
L’hardware è la parte fisica del computer, ciò che possiamo toccare:
CPU (Central Processing Unit): il “cervello” che esegue le istruzioni
Memoria RAM: memoria temporanea veloce
Hard Disk/SSD: memoria permanente per salvare i dati
Periferiche di Input: tastiera, mouse, scanner
Periferiche di Output: monitor, stampante, altoparlanti
Software
Il software è la parte logica, l’insieme di programmi e dati:
Sistema Operativo: gestisce le risorse hardware (Windows, Linux, macOS)
Applicazioni: programmi per l’utente finale (browser, editor di testo)
Librerie: collezioni di funzioni riutilizzabili
Driver: programmi che permettono al sistema di comunicare con l’hardware
Relazione Hardware-Software
Utente
  ↓
Applicazioni
  ↓
Sistema Operativo
  ↓
Hardware
• 
• 
• 
• 
• 
• 
• 
• 
• 

1.3 Concetto di Algoritmo (30 min)
Definizione
Un algoritmo è una sequenza finita e ordinata di passi elementari e non ambigui che
portano alla soluzione di un problema.
Caratteristiche di un Algoritmo
Finito: deve terminare dopo un numero finito di passi
Definito: ogni passo deve essere descritto in modo preciso e non ambiguo
Input: può ricevere zero o più dati in ingresso
Output: produce uno o più risultati
Efficace: ogni operazione deve essere eseguibile in tempo finito
Generale: deve risolvere una classe di problemi, non solo un caso specifico
Esempio 1: Algoritmo per Fare il Caffè
1. Riempire la moka d'acqua fino alla valvola
2. Inserire il filtro
3. Riempire il filtro di caffè macinato
4. Avvitare la parte superiore della moka
5. Mettere la moka sul fuoco
6. Attendere che il caffè salga
7. Spegnere il fuoco
8. Versare il caffè nella tazzina
Esempio 2: Algoritmo per Calcolare la Media di Due Numeri
1. INIZIO
2. Leggi il primo numero (chiamalo A)
3. Leggi il secondo numero (chiamalo B)
4. Calcola SOMMA = A + B
5. Calcola MEDIA = SOMMA / 2
1. 
2. 
3. 
4. 
5. 
6. 

6. Scrivi MEDIA
7. FINE
Proprietà Importanti
Correttezza: l’algoritmo deve produrre il risultato corretto per tutti i possibili input validi.
Efficienza: un algoritmo efficiente utilizza meno risorse (tempo e memoria).
Complessità temporale: quanto tempo impiega
Complessità spaziale: quanta memoria utilizza
Determinismo: a parità di input, l’algoritmo produce sempre lo stesso output.
1.4 Esempi di Algoritmi nella Vita Quotidiana (15 min)
Esempio 3: Trovare il Massimo tra Tre Numeri
1. Leggi tre numeri: A, B, C
2. Poni MAX = A
3. Se B > MAX allora MAX = B
4. Se C > MAX allora MAX = C
5. Scrivi MAX
Esempio 4: Attraversare la Strada in Sicurezza
1. Avvicinati al bordo del marciapiede
2. Guarda a sinistra
3. Guarda a destra
4. Guarda di nuovo a sinistra
5. Se arrivano veicoli:
   - Aspetta che passino
   - Torna al passo 2
6. Se non ci sono veicoli:
• 
• 

   - Attraversa rapidamente
7. Fine
Esempio 5: Algoritmo di Ricerca (trovare un nome in rubrica)
1. Apri la rubrica telefonica
2. Stima approssimativamente la posizione del nome
3. Apri la rubrica in quella posizione
4. Se il nome cercato viene prima:
   - Sfoglia all'indietro
5. Se il nome cercato viene dopo:
   - Sfoglia in avanti
6. Se hai trovato il nome:
   - Leggi il numero di telefono
7. Altrimenti torna al passo 3
1.5 Linguaggi di Programmazione (20 min)
Livelli di Linguaggi
Linguaggio Macchina (Basso Livello)
Codice binario (0 e 1)
Direttamente eseguibile dalla CPU
Esempio: 10110000 01100001
Molto difficile da scrivere e leggere
Linguaggio Assembly (Basso Livello)
Istruzioni mnemoniche
Più leggibile del linguaggio macchina
Specifico per ogni architettura
Esempio: MOV AX, 61h
• 
• 
• 
• 
• 
• 
• 
• 

Linguaggi di Alto Livello
Più vicini al linguaggio umano
Indipendenti dall’hardware
Necessitano di compilazione o interpretazione
Esempi: C, Python, Java, JavaScript
Classificazione dei Linguaggi
Linguaggi Compilati:
Il codice sorgente viene tradotto tutto in una volta in linguaggio macchina
Producono un file eseguibile
Più veloci in esecuzione
Esempi: C, C++, Rust
Linguaggi Interpretati:
Il codice viene tradotto ed eseguito riga per riga
Non producono un eseguibile
Più lenti ma più flessibili
Esempi: Python, JavaScript, Ruby
Processo di Compilazione (C):
Codice Sorgente (.c)
        ↓
   Preprocessore
        ↓
    Compilatore
        ↓
   Codice Oggetto (.o)
        ↓
      Linker
        ↓
  Eseguibile (.exe)
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

1.6 Introduzione al Linguaggio C (15 min)
Storia del C
Sviluppato da Dennis Ritchie nei Bell Laboratories (1972)
Creato per sviluppare il sistema operativo UNIX
Influenzato dai linguaggi B e BCPL
Base per molti linguaggi moderni (C++, C#, Java, JavaScript)
Caratteristiche del C
Vantaggi:
Efficiente: produce codice veloce e ottimizzato
Portabile: programmi C possono girare su diverse piattaforme
Potente: accesso diretto alla memoria e all’hardware
Standard: definito dagli standard ANSI/ISO
Diffuso: utilizzato in sistemi operativi, embedded systems, videogiochi
Svantaggi:
Complesso: richiede gestione manuale della memoria
Pericoloso: possibili errori con puntatori e memoria
Verboso: richiede più codice rispetto a linguaggi moderni
Dove viene utilizzato il C?
Sistemi operativi (Linux, Windows)
Database (MySQL, PostgreSQL)
Linguaggi di programmazione (Python, Ruby interpreters)
Sistemi embedded (elettrodomestici, automobili)
Hardware drivers
Applicazioni real-time
Primo Sguardo al C
Un semplice programma in C:
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

Spiegazione base:
#include <stdio.h>: include funzioni di input/output
int main(): funzione principale del programma
printf(): funzione per stampare a video
return 0: indica che il programma è terminato correttamente
PARTE PRATICA (2 ore)
ESERCIZI GUIDATI
Esercizio 1: Algoritmi in Linguaggio Naturale (30 min)
Consegna: Scrivi in linguaggio naturale (italiano) gli algoritmi per risolvere i seguenti
problemi. Usa la forma numerata come negli esempi visti.
1.1 Algoritmo per preparare un tè
Soluzione:
1. Riempire il bollitore d'acqua
2. Accendere il bollitore
3. Attendere che l'acqua bolla
4. Mettere la bustina di tè nella tazza
5. Versare l'acqua bollente nella tazza
6. Lasciare in infusione 3-5 minuti
7. Rimuovere la bustina
#include <stdio.h>
int main(){
    printf("Hello, World!\n");
return0;
}
• 
• 
• 
• 

8. (Opzionale) Aggiungere zucchero o latte
9. Fine
1.2 Algoritmo per calcolare l’area di un rettangolo
Soluzione:
1. INIZIO
2. Leggi la BASE del rettangolo
3. Leggi l'ALTEZZA del rettangolo
4. Calcola AREA = BASE × ALTEZZA
5. Scrivi AREA
6. FINE
1.3 Algoritmo per determinare se un numero è pari o dispari
Soluzione:
1. INIZIO
2. Leggi un numero N
3. Calcola RESTO = N diviso 2 (resto della divisione)
4. Se RESTO = 0:
   - Scrivi "Il numero è pari"
5. Altrimenti:
   - Scrivi "Il numero è dispari"
6. FINE
Esercizio 2: Analisi di Algoritmi (30 min)
Consegna: Analizza i seguenti algoritmi e rispondi alle domande.
2.1 Algoritmo Misterioso
1. Leggi un numero N
2. Poni RISULTATO = 1
3. Poni CONTATORE = 1

4. Finché CONTATORE ≤ N ripeti:
   - RISULTATO = RISULTATO × CONTATORE
   - CONTATORE = CONTATORE + 1
5. Scrivi RISULTATO
Domande:
Cosa fa questo algoritmo? (Calcola il fattoriale di N)
Qual è l’input? (Un numero N)
Qual è l’output? (N! = 1×2×3×…×N)
L’algoritmo termina sempre? (Sì, se N ≥ 0)
2.2 Algoritmo con Problema
1. Leggi un numero N
2. Finché N ≠ 0 ripeti:
   - Scrivi N
   - N = N + 1
Domande:
Cosa fa questo algoritmo?
Qual è il problema? (Ciclo infinito se N ≠ 0)
Come si può correggere? (Cambiare N = N + 1 in N = N - 1, oppure cambiare la
condizione)
Esercizio 3: Creazione di Algoritmi (40 min)
Consegna: Scrivi algoritmi completi per i seguenti problemi.
3.1 Calcolare il perimetro di un rettangolo
Soluzione proposta:
1. INIZIO
2. Leggi BASE
3. Leggi ALTEZZA
4. Calcola PERIMETRO = 2 × (BASE + ALTEZZA)
• 
• 
• 
• 
• 
• 
• 

5. Scrivi PERIMETRO
6. FINE
3.2 Trovare il minore tra tre numeri
Soluzione proposta:
1. INIZIO
2. Leggi tre numeri: A, B, C
3. Poni MIN = A
4. Se B < MIN allora MIN = B
5. Se C < MIN allora MIN = C
6. Scrivi MIN
7. FINE
3.3 Convertire temperatura da Celsius a Fahrenheit
Formula: F = (C × 9/5) + 32
Soluzione proposta:
1. INIZIO
2. Leggi CELSIUS
3. Calcola FAHRENHEIT = (CELSIUS × 9 / 5) + 32
4. Scrivi FAHRENHEIT
5. FINE
3.4 Calcolare il costo totale di una spesa con sconto
Soluzione proposta:
1. INIZIO
2. Leggi PREZZO_ORIGINALE
3. Leggi PERCENTUALE_SCONTO
4. Calcola SCONTO = PREZZO_ORIGINALE × PERCENTUALE_SCONTO / 100
5. Calcola PREZZO_FINALE = PREZZO_ORIGINALE - SCONTO

6. Scrivi PREZZO_FINALE
7. FINE
3.5 Verificare se un anno è bisestile
Regole: divisibile per 4 E (non divisibile per 100 O divisibile per 400)
Soluzione proposta:
1. INIZIO
2. Leggi ANNO
3. Se ANNO è divisibile per 400:
   - Scrivi "Anno bisestile"
4. Altrimenti se ANNO è divisibile per 100:
   - Scrivi "Anno NON bisestile"
5. Altrimenti se ANNO è divisibile per 4:
   - Scrivi "Anno bisestile"
6. Altrimenti:
   - Scrivi "Anno NON bisestile"
7. FINE
Esercizio 4: Installazione Ambiente di Sviluppo (20 min)
Obiettivo: Configurare l’ambiente per programmare in C
Opzione 1: Windows con MinGW
Scarica MinGW da: https://sourceforge.net/projects/mingw/
Installa selezionando “gcc” e “g++”
Aggiungi MinGW al PATH di sistema
Verifica aprendo cmd e digitando: gcc --version
Opzione 2: Linux
Apri il terminale
Installa gcc: sudo apt-get install build-essential
Verifica: gcc --version
1. 
2. 
3. 
4. 
1. 
2. 
3. 

Opzione 3: macOS
Installa Xcode Command Line Tools
Apri Terminal e digita: xcode-select --install
Verifica: gcc --version
IDE Consigliati:
Visual Studio Code: leggero, estensioni per C/C++
Code::Blocks: IDE specifico per C/C++
Dev-C++: semplice per principianti (Windows)
CLion: professionale (a pagamento, gratis per studenti)
Test dell’installazione:
Crea un file test.c
Scrivi un programma minimo (non preoccuparti della sintassi ora):
Compila: gcc test.c -o test
Esegui: ./test (Linux/Mac) o test.exe (Windows)
ESERCIZI DA SVOLGERE A CASA
Homework 1: Scrivi un algoritmo per ordinare tre numeri in ordine crescente.
Homework 2: Scrivi un algoritmo per calcolare il prezzo finale di un prodotto dopo
l’applicazione di IVA (22%).
Homework 3: Scrivi un algoritmo che legge i voti di uno studente (5 voti) e calcola la
media. Se la media è >= 6, scrive “Promosso”, altrimenti “Bocciato”.
Homework 4: Ricerca online esempi di programmi scritti in C e prova a capire cosa
fanno (anche se non capisci ancora la sintassi).
1. 
2. 
3. 
• 
• 
• 
• 
1. 
2. 
#include <stdio.h>
int main(){
    printf("Funziona!\n");
return0;
}
1. 
2. 

Homework 5: Completa l’installazione dell’ambiente di sviluppo e familiarizza con l’IDE
scelto.
MATERIALE DI APPROFONDIMENTO
Libri Consigliati
“Il linguaggio C” - Kernighan & Ritchie (K&R)
“Programmazione in C” - Kim N. King
“C: The Complete Reference” - Herbert Schildt
Risorse Online
https://www.learn-c.org/ - Tutorial interattivo
https://www.cprogramming.com/ - Guide e tutorial
https://en.cppreference.com/ - Riferimento completo del linguaggio
Video Tutorial
Cerca su YouTube: “C programming for beginners”
Canali consigliati: FreeCodeCamp, CS50 di Harvard
PUNTI CHIAVE DELLA LEZIONE
✓ Un algoritmo è una sequenza finita di passi per risolvere un problema
✓ Gli algoritmi devono essere finiti, definiti e efficaci
✓ La programmazione è il processo di tradurre algoritmi in codice
✓ Il C è un linguaggio potente, efficiente e ampiamente utilizzato
✓ Prima di scrivere codice, è importante pensare all’algoritmo
✓ La pratica è fondamentale: più algoritmi scrivi, più diventi bravo
• 
• 
• 
• 
• 
• 
• 
• 

PREPARAZIONE PER LA PROSSIMA
LEZIONE
Nella prossima lezione studieremo:
Flow Chart: rappresentazione grafica degli algoritmi
Costrutti fondamentali: sequenza, selezione, iterazione
Pseudocodice: linguaggio intermedio tra italiano e codice
Porta con te:
Ambiente di sviluppo installato e funzionante
Esercizi homework completati
Domande e dubbi sulla lezione di oggi
• 
• 
• 
• 
• 
• 


---

# lezione10 switch

**File:** `lezione10 switch.pdf`
**Tipo:** `.pdf`
**Dimensione:** 694.0 KB
**Ultima modifica:** 02/07/2026 09:24

---

LEZIONE 10 - Costrutto di Selezione:
switch-case
Durata: 4 ore | Teoria: 2h | Esercizi: 2h
PARTE TEORICA (2 ore)
10.1 Introduzione allo switch (15 min)
Cos’è lo switch?
Lo 
switch
 è un costrutto di selezione multipla che permette di scegliere tra diverse
alternative in base al valore di una 
singola espressione
.
Analogia:
 Come un centralino telefonico che smista le chiamate verso estensioni diverse.
Quando usare switch?
✓
✓
 USA switch quando:
 - Confronti 
una variabile
 con 
molte costanti
 - Hai 
4+
alternative
 discrete - I valori sono 
interi
 o 
caratteri
 - Vuoi codice più 
leggibile
 e
performante
✗
✗
 USA if-else quando:
 - Condizioni 
complesse
 (range, AND, OR) - Confronti con 
float
- Poche alternative (2-3) - Condizioni 
non costanti
Confronto if-else vs switch
Con if-else (verboso):
Con switch (più chiaro):
int
 scelta 
=
 
2
;
if
 
(
scelta 
==
 
1
)
 
{
    printf
(
"Opzione 1
\n
"
);
}
 
else
 
if
 
(
scelta 
==
 
2
)
 
{
    printf
(
"Opzione 2
\n
"
);
}
 
else
 
if
 
(
scelta 
==
 
3
)
 
{
    printf
(
"Opzione 3
\n
"
);
}
 
else
 
if
 
(
scelta 
==
 
4
)
 
{
    printf
(
"Opzione 4
\n
"
);
}
 
else
 
{
    printf
(
"Opzione non valida
\n
"
);
}

10.2 Sintassi dello switch (20 min)
Struttura Base
Componenti
1. switch (espressione)
 - 
espressione
: valutata UNA sola volta - Deve essere 
intero
 o
carattere
 - Non può essere float, double, stringa
2. case costante:
 - 
costante
: deve essere 
letterale
 o 
costante nota a compile-time
 -
Non può essere variabile - Ogni case deve essere 
unico
3. break:
 - 
Esce
 dallo switch - Senza break, l’esecuzione 
continua
 al caso successivo
(fall-through)
4. default:
 - Caso 
opzionale
 - Eseguito se 
nessun case
 corrisponde - Può essere in
qualsiasi posizione
 (convenzionalmente alla fine)
Flow Chart: switch
int
 scelta 
=
 
2
;
switch
 
(
scelta
)
 
{
    
case
 
1
:
        printf
(
"Opzione 1
\n
"
);
        
break
;
    
case
 
2
:
        printf
(
"Opzione 2
\n
"
);
        
break
;
    
case
 
3
:
        printf
(
"Opzione 3
\n
"
);
        
break
;
    
case
 
4
:
        printf
(
"Opzione 4
\n
"
);
        
break
;
    
default
:
        printf
(
"Opzione non valida
\n
"
);
}
switch
 
(
espressione
)
 
{
    
case
 costante1
:
        
// Istruzioni per costante1
        
break
;
    
    
case
 costante2
:
        
// Istruzioni per costante2
        
break
;
    
    
case
 costante3
:
        
// Istruzioni per costante3
        
break
;
    
    
default
:
        
// Istruzioni se nessun case corrisponde
        
break
;
  
// Opzionale nell'ultimo caso
}

          ┌──────────┐
          │Valuta    │
          │espressione│
          └────┬─────┘
               │
      ┌────────┼────────┬────────┐
      │        │        │        │
   case 1?  case 2?  case 3?  default
      │        │        │        │
      ▼        ▼        ▼        ▼
   ┌────┐  ┌────┐  ┌────┐  ┌────┐
   │Code│  │Code│  │Code│  │Code│
   └─┬──┘  └─┬──┘  └─┬──┘  └─┬──┘
     │       │       │       │
  break?  break?  break?     │
     │       │       │       │
     └───────┴───────┴───────┘
              │
         (continua)
Esempi Base
Esempio 1: Menu semplice
Esempio 2: Giorni della settimana
int
 opzione
;
printf
(
"Scegli (1-3): "
);
scanf
(
"
%d
"
,
 
&
opzione
);
switch
 
(
opzione
)
 
{
    
case
 
1
:
        printf
(
"Hai scelto opzione 1
\n
"
);
        
break
;
    
case
 
2
:
        printf
(
"Hai scelto opzione 2
\n
"
);
        
break
;
    
case
 
3
:
        printf
(
"Hai scelto opzione 3
\n
"
);
        
break
;
    
default
:
        printf
(
"Opzione non valida
\n
"
);
}

Esempio 3: Caratteri
10.3 L’istruzione break (15 min)
Ruolo del break
Il 
break
 esce immediatamente dallo switch, saltando tutti i case successivi.
Con break (normale):
int
 giorno
;
printf
(
"Numero giorno (1-7): "
);
scanf
(
"
%d
"
,
 
&
giorno
);
switch
 
(
giorno
)
 
{
    
case
 
1
:
        printf
(
"Lunedì
\n
"
);
        
break
;
    
case
 
2
:
        printf
(
"Martedì
\n
"
);
        
break
;
    
case
 
3
:
        printf
(
"Mercoledì
\n
"
);
        
break
;
    
case
 
4
:
        printf
(
"Giovedì
\n
"
);
        
break
;
    
case
 
5
:
        printf
(
"Venerdì
\n
"
);
        
break
;
    
case
 
6
:
        printf
(
"Sabato
\n
"
);
        
break
;
    
case
 
7
:
        printf
(
"Domenica
\n
"
);
        
break
;
    
default
:
        printf
(
"Giorno non valido
\n
"
);
}
char
 voto
;
printf
(
"Voto letterale (A-F): "
);
scanf
(
" 
%c
"
,
 
&
voto
);
switch
 
(
voto
)
 
{
    
case
 
'A'
:
        printf
(
"Ottimo! 90-100
\n
"
);
        
break
;
    
case
 
'B'
:
        printf
(
"Buono! 80-89
\n
"
);
        
break
;
    
case
 
'C'
:
        printf
(
"Discreto! 70-79
\n
"
);
        
break
;
    
case
 
'D'
:
        printf
(
"Sufficiente! 60-69
\n
"
);
        
break
;
    
case
 
'F'
:
        printf
(
"Insufficiente! <60
\n
"
);
        
break
;
    
default
:
        printf
(
"Voto non riconosciuto
\n
"
);
}

Senza break (fall-through):
Quando omettere break
Fall-through intenzionale
 (raro ma utile):
Esempio 1: Più case stessa azione
Esempio 2: Azioni cumulative
int
 x 
=
 
2
;
switch
 
(
x
)
 
{
    
case
 
1
:
        printf
(
"Uno
\n
"
);
        
break
;
    
case
 
2
:
        printf
(
"Due
\n
"
);
        
break
;
  
// Esce qui
    
case
 
3
:
        printf
(
"Tre
\n
"
);
        
break
;
}
// Output: Due
int
 x 
=
 
2
;
switch
 
(
x
)
 
{
    
case
 
1
:
        printf
(
"Uno
\n
"
);
        
// Manca break!
    
case
 
2
:
        printf
(
"Due
\n
"
);
        
// Manca break!
    
case
 
3
:
        printf
(
"Tre
\n
"
);
        
break
;
}
// Output: Due
//         Tre
char
 ch
;
scanf
(
" 
%c
"
,
 
&
ch
);
switch
 
(
ch
)
 
{
    
case
 
'a'
:
    
case
 
'e'
:
    
case
 
'i'
:
    
case
 
'o'
:
    
case
 
'u'
:
        printf
(
"È una vocale
\n
"
);
        
break
;
    
default
:
        printf
(
"È una consonante
\n
"
);
}

Esempio 3: Giorni del mese
Best Practice: Commenta fall-through
10.4 Il caso default (10 min)
Scopo di default
default
 gestisce tutti i valori 
non coperti
 dai case espliciti.
Senza default:
int
 livello 
=
 
2
;
switch
 
(
livello
)
 
{
    
case
 
3
:
        printf
(
"Attiva scudo
\n
"
);
        
// Fall-through intenzionale
    
case
 
2
:
        printf
(
"Attiva arma
\n
"
);
        
// Fall-through intenzionale
    
case
 
1
:
        printf
(
"Attiva movimento
\n
"
);
        
break
;
    
default
:
        printf
(
"Livello non valido
\n
"
);
}
// Con livello=2, output:
// Attiva arma
// Attiva movimento
int
 mese
;
int
 giorni
;
scanf
(
"
%d
"
,
 
&
mese
);
switch
 
(
mese
)
 
{
    
case
 
1
:
 
case
 
3
:
 
case
 
5
:
 
case
 
7
:
    
case
 
8
:
 
case
 
10
:
 
case
 
12
:
        giorni 
=
 
31
;
        
break
;
    
case
 
4
:
 
case
 
6
:
 
case
 
9
:
 
case
 
11
:
        giorni 
=
 
30
;
        
break
;
    
case
 
2
:
        giorni 
=
 
28
;
  
// Ignoriamo bisestile per semplicità
        
break
;
    
default
:
        printf
(
"Mese non valido
\n
"
);
        giorni 
=
 
0
;
}
if
 
(
giorni 
>
 
0
)
 
{
    printf
(
"Giorni: 
%d\n
"
,
 giorni
);
}
switch
 
(
x
)
 
{
    
case
 
1
:
        printf
(
"Uno
\n
"
);
        
// Intenzionale: fall-through al caso 2
    
case
 
2
:
        printf
(
"Due
\n
"
);
        
break
;
}

Con default:
Posizione di default
Convenzionalmente alla fine:
Ma può essere ovunque:
Best Practice:
 Metti default 
sempre alla fine
 per chiarezza.
default è opzionale?
Sì
, ma 
raccomandata
 per: - 
Validazione input
 - 
Gestione errori
 - 
Debug
 (cattura valori
inaspettati)
int
 x 
=
 
10
;
switch
 
(
x
)
 
{
    
case
 
1
:
        printf
(
"Uno
\n
"
);
        
break
;
    
case
 
2
:
        printf
(
"Due
\n
"
);
        
break
;
    
// x=10 non fa nulla!
}
int
 x 
=
 
10
;
switch
 
(
x
)
 
{
    
case
 
1
:
        printf
(
"Uno
\n
"
);
        
break
;
    
case
 
2
:
        printf
(
"Due
\n
"
);
        
break
;
    
default
:
        printf
(
"Valore non gestito: 
%d\n
"
,
 x
);
}
switch
 
(
x
)
 
{
    
case
 
1
:
        
// ...
        
break
;
    
case
 
2
:
        
// ...
        
break
;
    
default
:
  
// Alla fine (standard)
        
// ...
}
switch
 
(
x
)
 
{
    
case
 
1
:
        
// ...
        
break
;
    
default
:
  
// In mezzo (funziona ma poco comune)
        
// ...
        
break
;
    
case
 
2
:
        
// ...
        
break
;
}

10.5 Limitazioni dello switch (15 min)
1. Solo Tipi Interi e Char
✓
✓
 Funziona:
✗
✗
 NON funziona:
2. Solo Costanti nei case
✓
✓
 Funziona:
✗
✗
 NON funziona:
// Senza default (silenziosamente ignora valori invalidi)
switch
 
(
opzione
)
 
{
    
case
 
1
:
        
// ...
        
break
;
    
case
 
2
:
        
// ...
        
break
;
}
// Con default (segnala problema)
switch
 
(
opzione
)
 
{
    
case
 
1
:
        
// ...
        
break
;
    
case
 
2
:
        
// ...
        
break
;
    
default
:
        printf
(
"ERRORE: opzione 
%d
 non valida
\n
"
,
 opzione
);
}
int
 n 
=
 
5
;
switch
 
(
n
)
 
{
 
/* ... */
 
}
char
 c 
=
 
'A'
;
switch
 
(
c
)
 
{
 
/* ... */
 
}
enum
 Colore 
{
 ROSSO
,
 VERDE
,
 BLU 
};
enum
 Colore col 
=
 ROSSO
;
switch
 
(
col
)
 
{
 
/* ... */
 
}
float
 f 
=
 
3.14
;
switch
 
(
f
)
 
{
 
/* ... */
 
}
  
// ERRORE!
double
 d 
=
 
2.718
;
switch
 
(
d
)
 
{
 
/* ... */
 
}
  
// ERRORE!
char
 str
[]
 
=
 
"ciao"
;
switch
 
(
str
)
 
{
 
/* ... */
 
}
  
// ERRORE!
#define MAX 
100
switch
 
(
x
)
 
{
    
case
 
1
:
        
// Letterale
        
break
;
    
case
 MAX
:
      
// Costante definita
        
break
;
    
case
 
'A'
:
      
// Carattere
        
break
;
}

3. Non Supporta Range
✗
✗
 NON funziona (sintassi desiderata):
✓
✓
 Soluzione con case multipli:
✓
✓
 Meglio: usa if-else per range:
4. case Duplicati Non Permessi
✗
✗
 ERRORE:
10.6 switch vs if-else: Quando Usare Cosa (20 min)
Tabella Comparativa
int
 limite 
=
 
100
;
switch
 
(
x
)
 
{
    
case
 limite
:
   
// ERRORE! Variabile
        
break
;
    
case
 x 
+
 
1
:
    
// ERRORE! Espressione
        
break
;
}
switch
 
(
voto
)
 
{
    
case
 
90
-
100
:
   
// ERRORE! Range non supportato
        printf
(
"A
\n
"
);
        
break
;
}
switch
 
(
voto
)
 
{
    
case
 
90
:
 
case
 
91
:
 
case
 
92
:
 
case
 
93
:
 
case
 
94
:
    
case
 
95
:
 
case
 
96
:
 
case
 
97
:
 
case
 
98
:
 
case
 
99
:
    
case
 
100
:
        printf
(
"A
\n
"
);
        
break
;
}
if
 
(
voto 
>=
 
90
 
&&
 voto 
<=
 
100
)
 
{
    printf
(
"A
\n
"
);
}
 
else
 
if
 
(
voto 
>=
 
80
 
&&
 voto 
<
 
90
)
 
{
    printf
(
"B
\n
"
);
}
// ...
switch
 
(
x
)
 
{
    
case
 
1
:
        printf
(
"Primo
\n
"
);
        
break
;
    
case
 
1
:
        
// ERRORE! Duplicato
        printf
(
"Altro
\n
"
);
        
break
;
}

Criterio
switch
if-else
Tipo espressione
Int, char, enum
Qualsiasi
Condizioni
Solo uguaglianza (==)
Qualsiasi (<, >, &&, ||)
Range
No (workaround verboso)
Sì, facile
Float
No
Sì
Molte alternative
Ottimo
Verboso
Poche alternative
OK
Meglio
Leggibilità
Alta (se appropriato)
Varia
Performance
Potenzialmente più veloce*
Dipende
*Con molti case, il compilatore può usare jump table (O(1)) invece di confronti sequenziali
(O(n)).
Esempi di Scelta
Scenario 1: Menu con numeri → switch
Scenario 2: Range di valori → if-else
Scenario 3: Condizioni complesse → if-else
Scenario 4: Carattere singolo → switch
Scenario 5: Float → if-else (obbligatorio)
int
 scelta
;
scanf
(
"
%d
"
,
 
&
scelta
);
switch
 
(
scelta
)
 
{
    
case
 
1
:
 
/* ... */
 
break
;
    
case
 
2
:
 
/* ... */
 
break
;
    
case
 
3
:
 
/* ... */
 
break
;
    
case
 
4
:
 
/* ... */
 
break
;
    
default
:
 
/* ... */
}
int
 voto
;
scanf
(
"
%d
"
,
 
&
voto
);
if
 
(
voto 
>=
 
90
)
 
{
    printf
(
"A
\n
"
);
}
 
else
 
if
 
(
voto 
>=
 
80
)
 
{
    printf
(
"B
\n
"
);
}
 
else
 
if
 
(
voto 
>=
 
70
)
 
{
    printf
(
"C
\n
"
);
}
if
 
(
eta 
>=
 
18
 
&&
 ha_patente 
&&
 credito_sufficiente
)
 
{
    printf
(
"Può noleggiare
\n
"
);
}
 
else
 
{
    printf
(
"Non può noleggiare
\n
"
);
}
char
 operatore
;
scanf
(
" 
%c
"
,
 
&
operatore
);
switch
 
(
operatore
)
 
{
    
case
 
'+'
:
 
/* addizione */
 
break
;
    
case
 
'-'
:
 
/* sottrazione */
 
break
;
    
case
 
'*'
:
 
/* moltiplicazione */
 
break
;
    
case
 
'/'
:
 
/* divisione */
 
break
;
    
default
:
 printf
(
"Operatore non valido
\n
"
);
}

Conversione if-else → switch
Se hai:
Puoi convertire a:
Ma NON convertire se:
10.7 Esempi Pratici Avanzati (15 min)
Esempio 1: Calcolatrice
float
 temperatura
;
scanf
(
"
%f
"
,
 
&
temperatura
);
if
 
(
temperatura 
<
 
0
)
 
{
    printf
(
"Sotto zero
\n
"
);
}
 
else
 
if
 
(
temperatura 
<
 
15
)
 
{
    printf
(
"Freddo
\n
"
);
}
 
else
 
{
    printf
(
"Caldo
\n
"
);
}
if
 
(
x 
==
 
1
)
 
{
    
// ...
}
 
else
 
if
 
(
x 
==
 
2
)
 
{
    
// ...
}
 
else
 
if
 
(
x 
==
 
3
)
 
{
    
// ...
}
 
else
 
{
    
// ...
}
switch
 
(
x
)
 
{
    
case
 
1
:
        
// ...
        
break
;
    
case
 
2
:
        
// ...
        
break
;
    
case
 
3
:
        
// ...
        
break
;
    
default
:
        
// ...
}
if
 
(
x 
>
 
10
)
 
{
        
// Range, non ==
if
 
(
x 
==
 
1
 
||
 y 
==
 
2
)
 
{
  
// Condizione composta
if
 
(
f 
==
 
3.14
)
       
// Float

Esempio 2: Conversione Voto
#include 
<stdio.h>
int
 main
()
 
{
    
float
 a
,
 b
,
 risultato
;
    
char
 operatore
;
    
    printf
(
"Inserisci espressione (es: 5 + 3): "
);
    scanf
(
"
%f
 
%c
 
%f
"
,
 
&
a
,
 
&
operatore
,
 
&
b
);
    
    
switch
 
(
operatore
)
 
{
        
case
 
'+'
:
            risultato 
=
 a 
+
 b
;
            printf
(
"
%.2f
 + 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 risultato
);
            
break
;
        
        
case
 
'-'
:
            risultato 
=
 a 
-
 b
;
            printf
(
"
%.2f
 - 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 risultato
);
            
break
;
        
        
case
 
'*'
:
        
case
 
'x'
:
  
// Accetta sia * che x
            risultato 
=
 a 
*
 b
;
            printf
(
"
%.2f
 × 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 risultato
);
            
break
;
        
        
case
 
'/'
:
            
if
 
(
b 
!=
 
0
)
 
{
                risultato 
=
 a 
/
 b
;
                printf
(
"
%.2f
 ÷ 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 risultato
);
            
}
 
else
 
{
                printf
(
"ERRORE: Divisione per zero!
\n
"
);
            
}
            
break
;
        
        
default
:
            printf
(
"Operatore '
%c
' non riconosciuto
\n
"
,
 operatore
);
    
}
    
    
return
 
0
;
}

Esempio 3: Stato Semaforo
#include 
<stdio.h>
int
 main
()
 
{
    
int
 voto
;
    printf
(
"Voto (0-100): "
);
    scanf
(
"
%d
"
,
 
&
voto
);
    
    
if
 
(
voto 
<
 
0
 
||
 voto 
>
 
100
)
 
{
        printf
(
"Voto non valido
\n
"
);
        
return
 
1
;
    
}
    
    
// Converti a decine per usare switch
    
int
 decina 
=
 voto 
/
 
10
;
    
    
switch
 
(
decina
)
 
{
        
case
 
10
:
  
// 100
        
case
 
9
:
   
// 90-99
            printf
(
"Voto: A (Ottimo)
\n
"
);
            
break
;
        
        
case
 
8
:
   
// 80-89
            printf
(
"Voto: B (Buono)
\n
"
);
            
break
;
        
        
case
 
7
:
   
// 70-79
            printf
(
"Voto: C (Discreto)
\n
"
);
            
break
;
        
        
case
 
6
:
   
// 60-69
            printf
(
"Voto: D (Sufficiente)
\n
"
);
            
break
;
        
        
default
:
  
// 0-59
            printf
(
"Voto: F (Insufficiente)
\n
"
);
    
}
    
    
return
 
0
;
}

Esempio 4: Menu Bancario
#include 
<stdio.h>
int
 main
()
 
{
    
char
 colore
;
    
    printf
(
"Colore semaforo (R/G/Y): "
);
    scanf
(
" 
%c
"
,
 
&
colore
);
    
    
// Gestisci maiuscole e minuscole
    
switch
 
(
colore
)
 
{
        
case
 
'R'
:
        
case
 
'r'
:
            printf
(
"  STOP - Fermati
\n
"
);
            
break
;
        
        
case
 
'G'
:
        
case
 
'g'
:
            printf
(
"  GO - Procedi
\n
"
);
            
break
;
        
        
case
 
'Y'
:
        
case
 
'y'
:
            printf
(
"  ATTENZIONE - Rallenta
\n
"
);
            
break
;
        
        
default
:
            printf
(
"Colore non valido
\n
"
);
    
}
    
    
return
 
0
;
}

PARTE PRATICA (2 ore)
ESERCIZI GUIDATI
Esercizio 1: switch Base (20 min)
1.1
 Menu semplice:
#include 
<stdio.h>
int
 main
()
 
{
    
float
 saldo 
=
 
1000.0
;
    
int
 scelta
;
    
float
 importo
;
    
    
do
 
{
        printf
(
"
\n
=== MENU BANCOMAT ===
\n
"
);
        printf
(
"1. Visualizza saldo
\n
"
);
        printf
(
"2. Deposita
\n
"
);
        printf
(
"3. Preleva
\n
"
);
        printf
(
"4. Esci
\n
"
);
        printf
(
"Scelta: "
);
        scanf
(
"
%d
"
,
 
&
scelta
);
        
        
switch
 
(
scelta
)
 
{
            
case
 
1
:
                printf
(
"Saldo attuale: 
%.2f
€
\n
"
,
 saldo
);
                
break
;
            
            
case
 
2
:
                printf
(
"Importo da depositare: "
);
                scanf
(
"
%f
"
,
 
&
importo
);
                
if
 
(
importo 
>
 
0
)
 
{
                    saldo 
+=
 importo
;
                    printf
(
"Deposito effettuato. Nuovo saldo: 
%.2f
€
\n
"
,
 saldo
                
}
 
else
 
{
                    printf
(
"Importo non valido
\n
"
);
                
}
                
break
;
            
            
case
 
3
:
                printf
(
"Importo da prelevare: "
);
                scanf
(
"
%f
"
,
 
&
importo
);
                
if
 
(
importo 
>
 
0
 
&&
 importo 
<=
 saldo
)
 
{
                    saldo 
-=
 importo
;
                    printf
(
"Prelievo effettuato. Nuovo saldo: 
%.2f
€
\n
"
,
 saldo
                
}
 
else
 
if
 
(
importo 
>
 saldo
)
 
{
                    printf
(
"Saldo insufficiente
\n
"
);
                
}
 
else
 
{
                    printf
(
"Importo non valido
\n
"
);
                
}
                
break
;
            
            
case
 
4
:
                printf
(
"Arrivederci!
\n
"
);
                
break
;
            
            
default
:
                printf
(
"Scelta non valida
\n
"
);
        
}
    
}
 
while
 
(
scelta 
!=
 
4
);
    
    
return
 
0
;
}

Esercizio 2: Fall-through Intenzionale (20 min)
2.1
 Vocali e consonanti:
#include 
<stdio.h>
int
 main
()
 
{
    
int
 scelta
;
    
float
 a
,
 b
,
 risultato
;
    printf
(
"=== MENU SEMPLICE ===
\n
"
);
    printf
(
"1. Saluta
\n
"
);
    printf
(
"2. Esegui operazioni esempio (add, sub, mul)
\n
"
);
    printf
(
"3. Esci
\n
"
);
    printf
(
"Scelta: "
);
    
if
 
(
scanf
(
"
%d
"
,
 
&
scelta
)
 
!=
 
1
)
 
{
        printf
(
"Input non valido
\n
"
);
        
return
 
1
;
    
}
    
switch
 
(
scelta
)
 
{
        
case
 
1
:
            printf
(
"Ciao, mondo!
\n
"
);
            
break
;
        
case
 
2
:
            printf
(
"Inserisci primo numero: "
);
            
if
 
(
scanf
(
"
%f
"
,
 
&
a
)
 
!=
 
1
)
 
{
 printf
(
"Input non valido
\n
"
);
 
return
            printf
(
"Inserisci secondo numero: "
);
            
if
 
(
scanf
(
"
%f
"
,
 
&
b
)
 
!=
 
1
)
 
{
 printf
(
"Input non valido
\n
"
);
 
return
            printf
(
"
\n
=== ESEMPI OPERAZIONI ===
\n
"
);
            risultato 
=
 a 
+
 b
;
            printf
(
"
%.2f
 + 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 risultato
);
            risultato 
=
 a 
-
 b
;
            printf
(
"
%.2f
 - 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 risultato
);
            risultato 
=
 a 
*
 b
;
            printf
(
"
%.2f
 × 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 risultato
);
            
break
;
        
case
 
3
:
            printf
(
"Uscita...
\n
"
);
            
break
;
        
default
:
            printf
(
"Scelta non valida
\n
"
);
    
}
    
return
 
0
;
}

2.2
 Giorni del mese:
#include 
<stdio.h>
int
 main
()
 
{
    
char
 lettera
;
    
    printf
(
"Inserisci una lettera: "
);
    scanf
(
" 
%c
"
,
 
&
lettera
);
    
    
switch
 
(
lettera
)
 
{
        
case
 
'a'
:
 
case
 
'A'
:
        
case
 
'e'
:
 
case
 
'E'
:
        
case
 
'i'
:
 
case
 
'I'
:
        
case
 
'o'
:
 
case
 
'O'
:
        
case
 
'u'
:
 
case
 
'U'
:
            printf
(
"'
%c
' è una VOCALE
\n
"
,
 lettera
);
            
break
;
        
        
default
:
            
if
 
((
lettera 
>=
 
'a'
 
&&
 lettera 
<=
 
'z'
)
 
||
                
(
lettera 
>=
 
'A'
 
&&
 lettera 
<=
 
'Z'
))
 
{
                printf
(
"'
%c
' è una CONSONANTE
\n
"
,
 lettera
);
            
}
 
else
 
{
                printf
(
"'
%c
' non è una lettera
\n
"
,
 lettera
);
            
}
    
}
    
    
return
 
0
;
}

2.3
 Classificazione carattere:
#include 
<stdio.h>
int
 main
()
 
{
    
int
 mese
;
    
int
 giorni
;
    
    printf
(
"Mese (1-12): "
);
    scanf
(
"
%d
"
,
 
&
mese
);
    
    
switch
 
(
mese
)
 
{
        
case
 
1
:
  
// Gennaio
        
case
 
3
:
  
// Marzo
        
case
 
5
:
  
// Maggio
        
case
 
7
:
  
// Luglio
        
case
 
8
:
  
// Agosto
        
case
 
10
:
 
// Ottobre
        
case
 
12
:
 
// Dicembre
            giorni 
=
 
31
;
            
break
;
        
        
case
 
4
:
  
// Aprile
        
case
 
6
:
  
// Giugno
        
case
 
9
:
  
// Settembre
        
case
 
11
:
 
// Novembre
            giorni 
=
 
30
;
            
break
;
        
        
case
 
2
:
  
// Febbraio
            giorni 
=
 
28
;
  
// Semplificato
            
break
;
        
        
default
:
            printf
(
"Mese non valido
\n
"
);
            
return
 
1
;
    
}
    
    printf
(
"Il mese 
%d
 ha 
%d
 giorni
\n
"
,
 mese
,
 giorni
);
    
    
return
 
0
;
}

Esercizio 3: Calcolatore Avanzato (25 min)
Sostituito blocco troncato con versione completa, usa math.h e gestisce input non valido e
divisione per zero.
#include 
<stdio.h>
int
 main
()
 
{
    
char
 ch
;
    
    printf
(
"Inserisci carattere: "
);
    scanf
(
" 
%c
"
,
 
&
ch
);
    
    
switch
 
(
ch
)
 
{
        
case
 
'0'
:
 
case
 
'1'
:
 
case
 
'2'
:
 
case
 
'3'
:
 
case
 
'4'
:
        
case
 
'5'
:
 
case
 
'6'
:
 
case
 
'7'
:
 
case
 
'8'
:
 
case
 
'9'
:
            printf
(
"È una CIFRA
\n
"
);
            
break
;
        
        
case
 
'+'
:
 
case
 
'-'
:
 
case
 
'*'
:
 
case
 
'/'
:
            printf
(
"È un OPERATORE
\n
"
);
            
break
;
        
        
case
 
' '
:
 
case
 
'
\t
'
:
 
case
 
'
\n
'
:
            printf
(
"È uno SPAZIO BIANCO
\n
"
);
            
break
;
        
        
default
:
            
if
 
((
ch 
>=
 
'a'
 
&&
 ch 
<=
 
'z'
)
 
||
 
(
ch 
>=
 
'A'
 
&&
 ch 
<=
 
'Z'
))
 
{
                printf
(
"È una LETTERA
\n
"
);
            
}
 
else
 
{
                printf
(
"È un SIMBOLO SPECIALE
\n
"
);
            
}
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
#include 
<math.h>
int
 main
()
 
{
    
int
 scelta
;
    
double
 a
,
 b
,
 risultato
;
    printf
(
"=== CALCOLATRICE AVANZATA ===
\n
"
);
    printf
(
"1. Addizione
\n
"
);
    printf
(
"2. Sottrazione
\n
"
);
    printf
(
"3. Moltiplicazione
\n
"
);
    printf
(
"4. Divisione
\n
"
);
    printf
(
"5. Potenza (a^b)
\n
"
);
    printf
(
"6. Radice quadrata (√a)
\n
"
);
    printf
(
"7. Percentuale (b
%%
 di a)
\n
"
);
    printf
(
"Scegli operazione (1-7): "
);
    
if
 
(
scanf
(
"
%d
"
,
 
&
scelta
)
 
!=
 
1
)
 
{
        printf
(
"Input non valido
\n
"
);
        
return
 
1
;
    
}
    
switch
 
(
scelta
)
 
{
        
case
 
1
:
            printf
(
"Inserisci a e b: "
);
            
if
 
(
scanf
(
"
%lf
 
%lf
"
,
 
&
a
,
 
&
b
)
 
!=
 
2
)
 
{
 printf
(
"Input non valido
\n
            risultato 
=
 a 
+
 b
;
            printf
(
"
%.6g
 + 
%.6g
 = 
%.6g\n
"
,
 a
,
 b
,
 risultato
);
            
break
;
        
case
 
2
:

Esercizio 4: Conversioni (25 min)
4.1
 Convertitore temperature:
        
case
 
2
:
            printf
(
"Inserisci a e b: "
);
            
if
 
(
scanf
(
"
%lf
 
%lf
"
,
 
&
a
,
 
&
b
)
 
!=
 
2
)
 
{
 printf
(
"Input non valido
\n
            risultato 
=
 a 
-
 b
;
            printf
(
"
%.6g
 - 
%.6g
 = 
%.6g\n
"
,
 a
,
 b
,
 risultato
);
            
break
;
        
case
 
3
:
            printf
(
"Inserisci a e b: "
);
            
if
 
(
scanf
(
"
%lf
 
%lf
"
,
 
&
a
,
 
&
b
)
 
!=
 
2
)
 
{
 printf
(
"Input non valido
\n
            risultato 
=
 a 
*
 b
;
            printf
(
"
%.6g
 × 
%.6g
 = 
%.6g\n
"
,
 a
,
 b
,
 risultato
);
            
break
;
        
case
 
4
:
            printf
(
"Inserisci dividendo e divisore: "
);
            
if
 
(
scanf
(
"
%lf
 
%lf
"
,
 
&
a
,
 
&
b
)
 
!=
 
2
)
 
{
 printf
(
"Input non valido
\n
            
if
 
(
b 
==
 
0
.0
)
 
{
                printf
(
"ERRORE: Divisione per zero!
\n
"
);
            
}
 
else
 
{
                risultato 
=
 a 
/
 b
;
                printf
(
"
%.6g
 ÷ 
%.6g
 = 
%.6g\n
"
,
 a
,
 b
,
 risultato
);
            
}
            
break
;
        
case
 
5
:
            printf
(
"Inserisci base e esponente: "
);
            
if
 
(
scanf
(
"
%lf
 
%lf
"
,
 
&
a
,
 
&
b
)
 
!=
 
2
)
 
{
 printf
(
"Input non valido
\n
            risultato 
=
 pow
(
a
,
 b
);
            printf
(
"
%.6g
 ^ 
%.6g
 = 
%.6g\n
"
,
 a
,
 b
,
 risultato
);
            
break
;
        
case
 
6
:
            printf
(
"Inserisci numero (a): "
);
            
if
 
(
scanf
(
"
%lf
"
,
 
&
a
)
 
!=
 
1
)
 
{
 printf
(
"Input non valido
\n
"
);
 
return
            
if
 
(
a 
<
 
0
.0
)
 
{
                printf
(
"ERRORE: radice di numero negativo
\n
"
);
            
}
 
else
 
{
                risultato 
=
 sqrt
(
a
);
                printf
(
"√
%.6g
 = 
%.6g\n
"
,
 a
,
 risultato
);
            
}
            
break
;
        
case
 
7
:
            printf
(
"Inserisci valore e percentuale (a percent): "
);
            
if
 
(
scanf
(
"
%lf
 
%lf
"
,
 
&
a
,
 
&
b
)
 
!=
 
2
)
 
{
 printf
(
"Input non valido
\n
            risultato 
=
 
(
a 
*
 b
)
 
/
 
100.0
;
            printf
(
"
%.6g%%
 di 
%.6g
 = 
%.6g\n
"
,
 b
,
 a
,
 risultato
);
            
break
;
        
default
:
            printf
(
"Operazione non valida
\n
"
);
    
}
    
return
 
0
;
}

4.2
 Convertitore numeri romani (1-10):
#include 
<stdio.h>
int
 main
()
 
{
    
int
 scelta
;
    
float
 temp
,
 risultato
;
    
    printf
(
"=== CONVERTITORE TEMPERATURE ===
\n
"
);
    printf
(
"1. Celsius → Fahrenheit
\n
"
);
    printf
(
"2. Celsius → Kelvin
\n
"
);
    printf
(
"3. Fahrenheit → Celsius
\n
"
);
    printf
(
"4. Fahrenheit → Kelvin
\n
"
);
    printf
(
"5. Kelvin → Celsius
\n
"
);
    printf
(
"6. Kelvin → Fahrenheit
\n
"
);
    printf
(
"
\n
Scegli conversione: "
);
    scanf
(
"
%d
"
,
 
&
scelta
);
    
    printf
(
"Temperatura: "
);
    scanf
(
"
%f
"
,
 
&
temp
);
    
    
switch
 
(
scelta
)
 
{
        
case
 
1
:
            risultato 
=
 
(
temp 
*
 
9.0
 
/
 
5.0
)
 
+
 
32.0
;
            printf
(
"
%.2f
°C = 
%.2f
°F
\n
"
,
 temp
,
 risultato
);
            
break
;
        
        
case
 
2
:
            risultato 
=
 temp 
+
 
273.15
;
            printf
(
"
%.2f
°C = 
%.2f
K
\n
"
,
 temp
,
 risultato
);
            
break
;
        
        
case
 
3
:
            risultato 
=
 
(
temp 
-
 
32.0
)
 
*
 
5.0
 
/
 
9.0
;
            printf
(
"
%.2f
°F = 
%.2f
°C
\n
"
,
 temp
,
 risultato
);
            
break
;
        
        
case
 
4
:
            risultato 
=
 
(
temp 
-
 
32.0
)
 
*
 
5.0
 
/
 
9.0
 
+
 
273.15
;
            printf
(
"
%.2f
°F = 
%.2f
K
\n
"
,
 temp
,
 risultato
);
            
break
;
        
        
case
 
5
:
            risultato 
=
 temp 
-
 
273.15
;
            printf
(
"
%.2f
K = 
%.2f
°C
\n
"
,
 temp
,
 risultato
);
            
break
;
        
        
case
 
6
:
            risultato 
=
 
(
temp 
-
 
273.15
)
 
*
 
9.0
 
/
 
5.0
 
+
 
32.0
;
            printf
(
"
%.2f
K = 
%.2f
°F
\n
"
,
 temp
,
 risultato
);
            
break
;
        
        
default
:
            printf
(
"Scelta non valida
\n
"
);
    
}
    
    
return
 
0
;
}

Esercizio 5: Progetti Completi (30 min)
5.1
 Sistema di gestione studente:
#include 
<stdio.h>
int
 main
()
 
{
    
int
 numero
;
    
    printf
(
"Inserisci numero (1-10): "
);
    scanf
(
"
%d
"
,
 
&
numero
);
    
    printf
(
"
%d
 in romano: "
,
 numero
);
    
    
switch
 
(
numero
)
 
{
        
case
 
1
:
            printf
(
"I
\n
"
);
            
break
;
        
case
 
2
:
            printf
(
"II
\n
"
);
            
break
;
        
case
 
3
:
            printf
(
"III
\n
"
);
            
break
;
        
case
 
4
:
            printf
(
"IV
\n
"
);
            
break
;
        
case
 
5
:
            printf
(
"V
\n
"
);
            
break
;
        
case
 
6
:
            printf
(
"VI
\n
"
);
            
break
;
        
case
 
7
:
            printf
(
"VII
\n
"
);
            
break
;
        
case
 
8
:
            printf
(
"VIII
\n
"
);
            
break
;
        
case
 
9
:
            printf
(
"IX
\n
"
);
            
break
;
        
case
 
10
:
            printf
(
"X
\n
"
);
            
break
;
        
default
:
            printf
(
"Numero fuori range
\n
"
);
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 scelta
;
    
char
 nome
[
50
]
 
=
 
"Non impostato"
;
    
int
 eta 
=
 
0
;
    
float
 media 
=
 
0
.0
;
    
    
do
 
{
        printf
(
"
\n
=== GESTIONE STUDENTE ===
\n
"
);
        printf
(
"1. Inserisci nome
\n
"
);
        printf
(
"2. Inserisci età
\n
"
);
        printf
(
"3. Inserisci media voti
\n
"
);
        printf
(
"4. Visualizza dati
\n
"
);
        printf
(
"5. Esci
\n
"
);
        printf
(
"
\n
Scelta: "
);

5.2
 Gioco “Scelta Avventura”:
        scanf
(
"
%d
"
,
 
&
scelta
);
        
        
switch
 
(
scelta
)
 
{
            
case
 
1
:
                printf
(
"Nome: "
);
                scanf
(
"
%s
"
,
 nome
);
                printf
(
"Nome salvato!
\n
"
);
                
break
;
            
            
case
 
2
:
                printf
(
"Età: "
);
                scanf
(
"
%d
"
,
 
&
eta
);
                
if
 
(
eta 
>
 
0
 
&&
 eta 
<
 
120
)
 
{
                    printf
(
"Età salvata!
\n
"
);
                
}
 
else
 
{
                    printf
(
"Età non valida
\n
"
);
                    eta 
=
 
0
;
                
}
                
break
;
            
            
case
 
3
:
                printf
(
"Media voti (0-30): "
);
                scanf
(
"
%f
"
,
 
&
media
);
                
if
 
(
media 
>=
 
0
 
&&
 media 
<=
 
30
)
 
{
                    printf
(
"Media salvata!
\n
"
);
                
}
 
else
 
{
                    printf
(
"Media non valida
\n
"
);
                    media 
=
 
0
;
                
}
                
break
;
            
            
case
 
4
:
                printf
(
"
\n
=== DATI STUDENTE ===
\n
"
);
                printf
(
"Nome: 
%s\n
"
,
 nome
);
                printf
(
"Età: 
%d
 anni
\n
"
,
 eta
);
                printf
(
"Media: 
%.1f\n
"
,
 media
);
                
                
if
 
(
media 
>=
 
18
)
 
{
                    printf
(
"Esito: PROMOSSO
\n
"
);
                    
if
 
(
media 
>=
 
27
)
 
{
                        printf
(
"Qualifica: OTTIMO
\n
"
);
                    
}
 
else
 
if
 
(
media 
>=
 
24
)
 
{
                        printf
(
"Qualifica: BUONO
\n
"
);
                    
}
 
else
 
{
                        printf
(
"Qualifica: SUFFICIENTE
\n
"
);
                    
}
                
}
 
else
 
if
 
(
media 
>
 
0
)
 
{
                    printf
(
"Esito: BOCCIATO
\n
"
);
                
}
                
break
;
            
            
case
 
5
:
                printf
(
"Uscita...
\n
"
);
                
break
;
            
            
default
:
                printf
(
"Scelta non valida
\n
"
);
        
}
    
}
 
while
 
(
scelta 
!=
 
5
);
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 scelta1
,
 scelta2
,
 scelta3
;
    

    
    printf
(
"=== AVVENTURA NEL CASTELLO ===
\n\n
"
);
    
    
// Livello 1
    printf
(
"Ti trovi davanti a un castello misterioso.
\n
"
);
    printf
(
"1. Entra dalla porta principale
\n
"
);
    printf
(
"2. Cerca un'entrata laterale
\n
"
);
    printf
(
"3. Torna indietro
\n
"
);
    printf
(
"
\n
Scelta: "
);
    scanf
(
"
%d
"
,
 
&
scelta1
);
    
    
switch
 
(
scelta1
)
 
{
        
case
 
1
:
            printf
(
"
\n
Entri dalla porta principale...
\n
"
);
            printf
(
"Vedi due scale: una sale, una scende.
\n
"
);
            printf
(
"1. Sali le scale
\n
"
);
            printf
(
"2. Scendi le scale
\n
"
);
            printf
(
"
\n
Scelta: "
);
            scanf
(
"
%d
"
,
 
&
scelta2
);
            
            
switch
 
(
scelta2
)
 
{
                
case
 
1
:
                    printf
(
"
\n
Sali e trovi una stanza con un tesoro!
\n
"
);
                    printf
(
"  HAI VINTO!
\n
"
);
                    
break
;
                
                
case
 
2
:
                    printf
(
"
\n
Scendi e incontri un drago!
\n
"
);
                    printf
(
"  GAME OVER
\n
"
);
                    
break
;
                
                
default
:
                    printf
(
"
\n
Non fai nulla e vieni catturato.
\n
"
);
                    printf
(
"  GAME OVER
\n
"
);
            
}
            
break
;
        
        
case
 
2
:
            printf
(
"
\n
Cerchi un'entrata laterale...
\n
"
);
            printf
(
"Trovi una finestra aperta.
\n
"
);
            printf
(
"1. Entra dalla finestra
\n
"
);
            printf
(
"2. Continua a cercare
\n
"
);
            printf
(
"
\n
Scelta: "
);
            scanf
(
"
%d
"
,
 
&
scelta3
);
            
            
switch
 
(
scelta3
)
 
{
                
case
 
1
:
                    printf
(
"
\n
Entri dalla finestra in una cucina.
\n
"
);
                    printf
(
"Trovi cibo e una mappa segreta!
\n
"
);
                    printf
(
"   HAI VINTO!
\n
"
);
                    
break
;
                
                
case
 
2
:
                    printf
(
"
\n
Continui a cercare ma si fa buio.
\n
"
);
                    printf
(
"Ti perdi nel bosco.
\n
"
);
                    printf
(
"  GAME OVER
\n
"
);
                    
break
;
                
                
default
:
                    printf
(
"
\n
Indecisione fatale!
\n
"
);
                    printf
(
"  GAME OVER
\n
"
);
            
}
            
break
;
        
        
case
 
3
:
            printf
(
"
\n
Torni indietro... saggia decisione!
\n
"
);
            printf
(
"  Sei salvo, ma niente avventura.
\n
"
);
            
break
;
        
        
default
:

5.3
 Menu ristorante con ordine:
            printf
(
"
\n
Non fai una scelta valida.
\n
"
);
            printf
(
"Un guardiano ti cattura!
\n
"
);
            printf
(
"   GAME OVER
\n
"
);
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 antipasto 
=
 
0
,
 primo 
=
 
0
,
 secondo 
=
 
0
,
 dolce 
=
 
0
;
    
int
 scelta
;
    
float
 totale 
=
 
0
.0
;
    
    printf
(
"=== RISTORANTE DA MARIO ===
\n\n
"
);
    
    
// Antipasto
    printf
(
"ANTIPASTI:
\n
"
);
    printf
(
"1. Bruschette (5€)
\n
"
);
    printf
(
"2. Prosciutto e melone (8€)
\n
"
);
    printf
(
"3. Nessun antipasto
\n
"
);
    printf
(
"Scelta: "
);
    scanf
(
"
%d
"
,
 
&
antipasto
);
    
    
switch
 
(
antipasto
)
 
{
        
case
 
1
:
            printf
(
"Hai scelto: Bruschette
\n
"
);
            totale 
+=
 
5.0
;
            
break
;
        
case
 
2
:
            printf
(
"Hai scelto: Prosciutto e melone
\n
"
);
            totale 
+=
 
8.0
;
            
break
;
        
case
 
3
:
            printf
(
"Nessun antipasto
\n
"
);
            
break
;
        
default
:
            printf
(
"Scelta non valida, salto...
\n
"
);
    
}
    
    
// Primo
    printf
(
"
\n
PRIMI PIATTI:
\n
"
);
    printf
(
"1. Spaghetti al pomodoro (10€)
\n
"
);
    printf
(
"2. Risotto ai funghi (12€)
\n
"
);
    printf
(
"3. Lasagne (11€)
\n
"
);
    printf
(
"Scelta: "
);
    scanf
(
"
%d
"
,
 
&
primo
);
    
    
switch
 
(
primo
)
 
{
        
case
 
1
:
            printf
(
"Hai scelto: Spaghetti al pomodoro
\n
"
);
            totale 
+=
 
10.0
;
            
break
;
        
case
 
2
:
            printf
(
"Hai scelto: Risotto ai funghi
\n
"
);
            totale 
+=
 
12.0
;
            
break
;
        
case
 
3
:
            printf
(
"Hai scelto: Lasagne
\n
"
);
            totale 
+=
 
11.0
;
            
break
;
        
default
:
            printf
(
"Scelta non valida, salto...
\n
"
);
    
}
    
    
// Secondo
    printf
(
"
\n
SECONDI PIATTI:
\n
"
);

    printf
(
"
\n
SECONDI PIATTI:
\n
"
);
    printf
(
"1. Bistecca (15€)
\n
"
);
    printf
(
"2. Pesce al forno (18€)
\n
"
);
    printf
(
"3. Pollo arrosto (13€)
\n
"
);
    printf
(
"4. Nessun secondo
\n
"
);
    printf
(
"Scelta: "
);
    scanf
(
"
%d
"
,
 
&
secondo
);
    
    
switch
 
(
secondo
)
 
{
        
case
 
1
:
            printf
(
"Hai scelto: Bistecca
\n
"
);
            totale 
+=
 
15.0
;
            
break
;
        
case
 
2
:
            printf
(
"Hai scelto: Pesce al forno
\n
"
);
            totale 
+=
 
18.0
;
            
break
;
        
case
 
3
:
            printf
(
"Hai scelto: Pollo arrosto
\n
"
);
            totale 
+=
 
13.0
;
            
break
;
        
case
 
4
:
            printf
(
"Nessun secondo
\n
"
);
            
break
;
        
default
:
            printf
(
"Scelta non valida, salto...
\n
"
);
    
}
    
    
// Dolce
    printf
(
"
\n
DOLCI:
\n
"
);
    printf
(
"1. Tiramisù (6€)
\n
"
);
    printf
(
"2. Panna cotta (5€)
\n
"
);
    printf
(
"3. Gelato (4€)
\n
"
);
    printf
(
"4. Nessun dolce
\n
"
);
    printf
(
"Scelta: "
);
    scanf
(
"
%d
"
,
 
&
dolce
);
    
    
switch
 
(
dolce
)
 
{
        
case
 
1
:
            printf
(
"Hai scelto: Tiramisù
\n
"
);
            totale 
+=
 
6.0
;
            
break
;
        
case
 
2
:
            printf
(
"Hai scelto: Panna cotta
\n
"
);
            totale 
+=
 
5.0
;
            
break
;
        
case
 
3
:
            printf
(
"Hai scelto: Gelato
\n
"
);
            totale 
+=
 
4.0
;
            
break
;
        
case
 
4
:
            printf
(
"Nessun dolce
\n
"
);
            
break
;
        
default
:
            printf
(
"Scelta non valida, salto...
\n
"
);
    
}
    
    
// Conto finale
    printf
(
"
\n
=== CONTO ===
\n
"
);
    printf
(
"Totale: 
%.2f
€
\n
"
,
 totale
);
    
    
if
 
(
totale 
>
 
50
)
 
{
        
float
 sconto 
=
 totale 
*
 
0
.10
;
        printf
(
"Sconto 10
%%
: -
%.2f
€
\n
"
,
 sconto
);
        printf
(
"Totale finale: 
%.2f
€
\n
"
,
 totale 
-
 sconto
);
    
}
    
    printf
(
"
\n
Grazie e buon appetito!
\n
"
);
    
    
return
 
0
;

ESERCIZI AUTONOMI
Esercizio 6: Pratica Libera
6.1
 Crea un convertitore unità di misura (lunghezza, peso, volume).
6.2
 Sistema di voto elettorale: chiedi partito (1-5) e conta voti.
6.3
 Gioco “Carta più alta”: confronta carte (1-13 = Asso-Re).
6.4
 Classificatore animali: mammifero/uccello/pesce/rettile con caratteristiche.
6.5
 Menu gestione libreria (aggiungi/cerca/rimuovi libri - simulato).
ESERCIZI DA SVOLGERE A CASA
Homework 1:
 Convertitore valute completo: - Menu con 5+ valute - Conversioni
bidirezionali - Tassi di cambio hardcoded - Visualizza tabella conversioni
Homework 2:
 Gioco battaglia navale (singola cella): - Griglia 5×5 (25 posizioni) - Utente
sceglie posizione (1-25) - Switch determina se colpito/mancato - 3 tentativi - Conta colpi e
mancati
Homework 3:
 Sistema di prenotazione cinema: - Menu film (1-5) - Menu orario
(mattina/pomeriggio/sera) - Menu tipo biglietto (intero/ridotto/famiglia) - Calcola prezzo
totale con sconti - Conferma prenotazione
Homework 4:
 Calcolatore IMC con consigli: - Chiedi peso e altezza - Calcola IMC - Usa
switch su decine di IMC - Fornisci consigli personalizzati per categoria
Homework 5:
 Gioco “Indovina l’animale”: - Switch su caratteristiche (ha ali? ha pelliccia?
vive in acqua?) - Catena di domande - Indovina animale in base a risposte
Homework 6:
 Traduttore numeri (1-100): - Chiedi numero - Traduci in italiano a parole -
Gestisci unità, decine, centinaia - Usa switch multipli
APPROFONDIMENTI
Jump Table (Ottimizzazione Compilatore)
Quando usi switch con molti case consecutivi, il compilatore può generare una 
jump table
invece di confronti sequenziali.
Jump Table:
Il compilatore crea:
indirizzo_base + (x * sizeof(puntatore)) → salta direttamente al case
Complessità:
 - if-else sequenziali: O(n) - n confronti nel caso peggiore - Jump table: O(1)
- un solo calcolo indirizzo
    
return
 
0
;
}
switch
 
(
x
)
 
{
    
case
 
0
:
 
/* ... */
 
break
;
    
case
 
1
:
 
/* ... */
 
break
;
    
case
 
2
:
 
/* ... */
 
break
;
    
// ...
    
case
 
99
:
 
/* ... */
 
break
;
}

Quando viene usata:
 - Case numericamente vicini (0-9, 1-10, etc.) - Molti case
(tipicamente 10+) - Case consecutivi o con pochi buchi
Duff’s Device (Trick Avanzato)
Un uso estremamente avanzato (e raro) di switch con cicli:
Perché funziona:
 Fall-through intenzionale + loop unrolling. 
Usa moderno:
 Compilatori
ottimizzano automaticamente, non serve!
Computed Goto (GCC Extension)
GCC supporta etichette come valori:
Ancora più veloce di switch, ma 
non portabile
 (solo GCC/Clang).
Enum con switch
Ottima pratica:
 Usa enum invece di numeri magici.
// NON usare in codice normale! Solo curiosità storica
void
 copy
(
char
 
*
to
,
 
char
 
*
from
,
 
int
 count
)
 
{
    
int
 n 
=
 
(
count 
+
 
7
)
 
/
 
8
;
    
switch
 
(
count 
%
 
8
)
 
{
        
case
 
0
:
 
do
 
{
 
*
to
++
 
=
 
*
from
++;
        
case
 
7
:
      
*
to
++
 
=
 
*
from
++;
        
case
 
6
:
      
*
to
++
 
=
 
*
from
++;
        
case
 
5
:
      
*
to
++
 
=
 
*
from
++;
        
case
 
4
:
      
*
to
++
 
=
 
*
from
++;
        
case
 
3
:
      
*
to
++
 
=
 
*
from
++;
        
case
 
2
:
      
*
to
++
 
=
 
*
from
++;
        
case
 
1
:
      
*
to
++
 
=
 
*
from
++;
               
}
 
while
 
(--
n 
>
 
0
);
    
}
}
void
 
*
labels
[]
 
=
 
{&&
case0
,
 
&&
case1
,
 
&&
case2
};
goto
 
*
labels
[
x
];
  
// Salta a etichetta calcolata
case0
:
    printf
(
"Case 0
\n
"
);
    
goto
 end
;
case1
:
    printf
(
"Case 1
\n
"
);
    
goto
 end
;
case2
:
    printf
(
"Case 2
\n
"
);
end
:
    
;

Vantaggi:
 - Codice auto-documentato - Compilatore avvisa se manca un case -
Refactoring più facile
RIEPILOGO CONCETTI CHIAVE
Sintassi switch
Regole Fondamentali
Espressione: 
int
 o 
char
 (no float)
case: solo 
costanti
 (no variabili)
break: 
necessario
 per uscire
default: 
opzionale
 ma raccomandato
Fall-through
TABELLE DI RIFERIMENTO RAPIDO
enum
 Giorno 
{
    LUNEDI 
=
 
1
,
    MARTEDI
,
    MERCOLEDI
,
    GIOVEDI
,
    VENERDI
,
    SABATO
,
    DOMENICA
};
enum
 Giorno oggi 
=
 MERCOLEDI
;
switch
 
(
oggi
)
 
{
    
case
 LUNEDI
:
        printf
(
"Inizio settimana
\n
"
);
        
break
;
    
case
 VENERDI
:
        printf
(
"Quasi weekend!
\n
"
);
        
break
;
    
case
 SABATO
:
    
case
 DOMENICA
:
        printf
(
"Weekend!
\n
"
);
        
break
;
    
default
:
        printf
(
"Giorno feriale
\n
"
);
}
switch
 
(
espressione
)
 
{
    
case
 valore1
:
        
// codice
        
break
;
    
case
 valore2
:
        
// codice
        
break
;
    
default
:
        
// codice
}
case
 
1
:
case
 
2
:
case
 
3
:
    
// Eseguito per 1, 2 o 3
    
break
;

switch vs if-else
Caratteristica
switch
if-else
Tipo supportato
int, char, enum
Qualsiasi
Condizione
Solo ==
Qualsiasi
Range
No (workaround)
Sì
Float
No
Sì
Leggibilità (molti case)
Alta
Bassa
Performance (molti case)
Alta (jump table)
Media
Quando Usare Cosa
Scenario
Usa
Menu numerico
switch
Singolo carattere
switch
Range di valori
if-else
Condizioni complesse
if-else
Float comparison
if-else
2-3 alternative
if-else
5+ alternative discrete
switch
PROBLEMI COMUNI E SOLUZIONI
Problema 1: Dimenticare break
Soluzione:
 Aggiungi sempre break (o commenta fall-through).
Problema 2: Variabile nel case
Soluzione:
 Usa #define o enum.
Problema 3: Range nel case
//   MALE
switch
 
(
x
)
 
{
    
case
 
1
:
        printf
(
"Uno
\n
"
);
    
case
 
2
:
  
// Esegue anche questo!
        printf
(
"Due
\n
"
);
        
break
;
}
int
 limite 
=
 
10
;
switch
 
(
x
)
 
{
    
case
 limite
:
  
//   ERRORE! Non compila
        
break
;
}
#define LIMITE 
10
switch
 
(
x
)
 
{
    
case
 LIMITE
:
  
// 
✓
 OK
        
break
;
}

Soluzione:
 Usa if-else o case multipli.
Problema 4: Float in switch
Soluzione:
 Usa if-else.
Problema 5: case Duplicati
Soluzione:
 Ogni case deve essere unico.
PUNTI CHIAVE DELLA LEZIONE
✓
 
switch
 ottimo per 
selezione multipla
 con valori discreti
✓
 Supporta solo 
int, char, enum
 (no float)
✓
 
break
 necessario per uscire (altrimenti fall-through)
✓
 
case
 solo con 
costanti
 (no variabili)
✓
 
default
 gestisce casi non previsti
✓
 
Fall-through
 utile per case multipli stessa azione
✓
 
Più leggibile
 di molti if-else per menu/opzioni
✓
 
Jump table
 rende switch O(1) vs if-else O(n)
✓
 
Commenta
 fall-through intenzionali
✓
 
Usa enum
 per codice auto-documentato
PREPARAZIONE PER LA PROSSIMA LEZIONE
Nella prossima lezione studieremo: - 
Ciclo while
: iterazione con condizione iniziale - 
Ciclo
do-while
: iterazione con condizione finale - 
Differenze while vs do-while
 - 
Cicli infiniti e
break
 - 
Continue
: salta iterazione corrente - 
Cicli annidati
Porta con te: - Esercizi homework completati - Domande su switch o fall-through - Esempi
di operazioni ripetitive - Idee per programmi con cicli
Eccellente! Ora padroneggi la selezione multipla!  
Con if-else e switch hai tutti gli strumenti per gestire decisioni semplici e complesse. Nella
switch
 
(
voto
)
 
{
    
case
 
90
-
100
:
  
//   ERRORE! Sintassi non valida
        printf
(
"A
\n
"
);
        
break
;
}
if
 
(
voto 
>=
 
90
 
&&
 voto 
<=
 
100
)
 
{
    printf
(
"A
\n
"
);
}
 
else
 
if
 
(
voto 
>=
 
80
 
&&
 voto 
<
 
90
)
 
{
    printf
(
"B
\n
"
);
}
// ...
float
 x 
=
 
3.14
;
switch
 
(
x
)
 
{
  
//   ERRORE! Float non supportato
    
// ...
}
switch
 
(
x
)
 
{
    
case
 
1
:
        
break
;
    
case
 
1
:
  
//   ERRORE! Duplicato
        
break
;
}

prossima lezione aggiungeremo i 
cicli
 per ripetere operazioni, completando così i tre
costrutti fondamentali della programmazione strutturata (sequenza, selezione, iterazione).


---

# lezione2 flowchart

**File:** `lezione2 flowchart.pdf`
**Tipo:** `.pdf`
**Dimensione:** 388.7 KB
**Ultima modifica:** 02/07/2026 09:28

---

LEZIONE 2 - Flow Chart e Costrutti
Base
Durata: 4 ore | Teoria: 2h | Esercizi: 2h
PARTE TEORICA (2 ore)
2.1 Introduzione ai Diagrammi di Flusso (20 min)
Cos’è un Flow Chart?
Un diagramma di flusso (flow chart o flowchart) è una rappresentazione grafica di un
algoritmo che utilizza simboli geometrici standardizzati collegati da frecce per mostrare il
flusso di esecuzione.
Perché usare i Flow Chart?
Visualizzazione: rappresentazione visiva più chiara rispetto al testo
Comunicazione: facile da condividere con altri programmatori
Progettazione: aiuta a pensare alla logica prima di scrivere codice
Documentazione: documenta il funzionamento di un programma
Debug: facilita l’individuazione di errori logici
Vantaggi e Svantaggi
Vantaggi:
Indipendenti dal linguaggio di programmazione
Facili da comprendere anche per non programmatori
Evidenziano chiaramente i punti decisionali
Utili per programmi di media complessità
• 
• 
• 
• 
• 
• 
• 
• 
• 

Svantaggi:
Possono diventare troppo complessi per programmi grandi
Richiedono tempo per essere disegnati
Difficili da modificare su carta
2.2 Simboli dei Flow Chart (30 min)
Simboli Fondamentali
1. TERMINATORE (Ovale/Ellisse)
Indica l’inizio o la fine di un algoritmo
Ogni flow chart ha esattamente UN inizio e almeno UNA fine
2. PROCESSO (Rettangolo)
Rappresenta un’operazione o istruzione
Calcoli, assegnazioni, operazioni matematiche
Esempi: X = 5, SOMMA = A + B, CONTATORE = CONTATORE + 1
3. INPUT/OUTPUT (Parallelogramma)
Rappresenta input (lettura di dati)
Rappresenta output (scrittura/stampa di risultati)
Esempi: Leggi N, Scrivi "Risultato", Stampa MEDIA
4. DECISIONE (Rombo)
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

Rappresenta una condizione o test
Ha due uscite: VERO (SI/TRUE) e FALSO (NO/FALSE)
La condizione è sempre una domanda con risposta SI/NO
Esempi: N > 0?, A = B?, SOMMA < 100?
5. FRECCE (Linee di Flusso)
    │
    ↓
    →
    ←
    ↑
Indicano il flusso di esecuzione
Mostrano l’ordine in cui vengono eseguite le istruzioni
Di solito vanno dall’alto verso il basso e da sinistra a destra
6. CONNETTORI (Cerchi)
Connettore in-page
Connettore off-page
Usati per collegare parti del flow chart quando le frecce si incrocerebbero
Connettori con la stessa etichetta sono collegati
Utili per mantenere il diagramma leggibile
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

Simboli Aggiuntivi (Meno Comuni)
7. PREDEFINITO (Rettangolo con barre laterali)
Rappresenta una funzione o procedura predefinita
2.3 Regole per Disegnare Flow Chart (15 min)
Convenzioni Standard
Direzione del flusso: dall’alto verso il basso, da sinistra a destra
Un solo inizio: un unico terminatore “INIZIO”
Una o più fine: almeno un terminatore “FINE”
Frecce chiare: sempre indicare la direzione con frecce
Etichette decisioni: indicare chiaramente SI/NO o VERO/FALSO
Testo conciso: istruzioni brevi e chiare nei simboli
No incroci: evitare che le linee si incrocino (usare connettori)
Allineamento: mantenere i simboli allineati per leggibilità
• 
1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 

Esempio Completo: Calcolare la Media di Due Numeri
2.4 Costrutti Fondamentali (35 min)
I costrutti fondamentali sono i mattoni con cui si costruisce qualsiasi algoritmo. Secondo
il Teorema di Böhm-Jacopini (1966), qualsiasi algoritmo può essere espresso usando
solo tre costrutti di base.
1. SEQUENZA
Definizione: Esecuzione di istruzioni una dopo l’altra, in ordine.
Caratteristiche:
Le istruzioni vengono eseguite dall’alto verso il basso
• 

Ogni istruzione viene eseguita esattamente una volta
Non ci sono scelte o ripetizioni
Flow Chart - Esempio: Scambio di due variabili
• 
• 


2. SELEZIONE (o Alternativa)
Definizione: Esecuzione di istruzioni diverse in base a una condizione.
Tipi di Selezione:
a) Selezione Semplice (IF)
b) Selezione Binaria (IF-ELSE)


c) Selezione Multipla (Nidificata)


3. ITERAZIONE (o Ciclo o Loop)
Definizione: Ripetizione di un blocco di istruzioni finché una condizione è vera.
Tipi di Iterazione:
a) WHILE (Condizione all’inizio)
Controlla la condizione PRIMA di eseguire il blocco
Se la condizione è falsa inizialmente, il blocco non viene mai eseguito
Esempio: Contare da 1 a 5
• 
• 

b) DO-WHILE (Condizione alla fine)
Esegue il blocco PRIMA di controllare la condizione
Il blocco viene eseguito almeno una volta
Esempio: Validazione input (ripeti finché valido)
• 
• 

c) FOR (Ciclo con contatore)
Usato quando si conosce in anticipo il numero di ripetizioni
Combina inizializzazione, condizione e incremento
Esempio: Somma dei primi N numeri
• 
• 

2.5 Pseudocodice (20 min)
Cos’è lo Pseudocodice?
Lo pseudocodice è un linguaggio di descrizione degli algoritmi che sta a metà strada
tra il linguaggio naturale e un linguaggio di programmazione.


Caratteristiche:
Non è un linguaggio di programmazione vero
Non ha una sintassi rigida
È più strutturato del linguaggio naturale
Facilita la traduzione in codice reale
Indipendente dal linguaggio di programmazione
Parole Chiave Comuni
Struttura base:
INIZIO
    istruzioni
FINE
Input/Output:
LEGGI variabile
SCRIVI variabile
STAMPA "messaggio"
Assegnamento:
variabile ← valore
variabile = espressione
Selezione:
SE condizione ALLORA
    istruzioni
FINE SE
SE condizione ALLORA
    istruzioni1
• 
• 
• 
• 
• 

ALTRIMENTI
    istruzioni2
FINE SE
Iterazione:
MENTRE condizione FARE
    istruzioni
FINE MENTRE
RIPETI
    istruzioni
FINCHÉ condizione
PER variabile DA inizio A fine FARE
    istruzioni
FINE PER
Esempi di Pseudocodice
Esempio 1: Calcolare il fattoriale
INIZIO
    LEGGI n
    fattoriale ← 1
    i ← 1
    MENTRE i <= n FARE
        fattoriale ← fattoriale * i
        i ← i + 1
    FINE MENTRE
    SCRIVI fattoriale
FINE
Esempio 2: Trovare il massimo in un array

INIZIO
    LEGGI n (dimensione array)
    PER i DA 0 A n-1 FARE
        LEGGI array[i]
    FINE PER
    max ← array[0]
    PER i DA 1 A n-1 FARE
        SE array[i] > max ALLORA
            max ← array[i]
        FINE SE
    FINE PER
    SCRIVI max
FINE
Esempio 3: Numeri pari da 1 a N
INIZIO
    LEGGI n
    i ← 2
    MENTRE i <= n FARE
        SCRIVI i
        i ← i + 2
    FINE MENTRE
FINE
2.6 Dal Flow Chart al Codice (10 min)
Processo di Traduzione
Analizza il problema → capisci cosa deve fare
Disegna il flow chart → visualizza la logica
1. 
2. 

Scrivi lo pseudocodice → struttura l’algoritmo
Traduci in linguaggio → scrivi il codice vero
Esempio Completo: Verifica se un numero è positivo, negativo o zero
1. Problema: Leggere un numero e dire se è positivo, negativo o zero.
2. Flow Chart:
3. Pseudocodice:
INIZIO
    LEGGI numero
3. 
4. 


    SE numero > 0 ALLORA
        SCRIVI "Positivo"
    ALTRIMENTI SE numero < 0 ALLORA
        SCRIVI "Negativo"
    ALTRIMENTI
        SCRIVI "Zero"
    FINE SE
FINE
4. Codice C (anticipazione):
#include <stdio.h>
int main(){
int numero;
    printf("Inserisci un numero: ");
    scanf("%d", &numero);
if(numero >0){
        printf("Positivo\n");
}elseif(numero <0){
        printf("Negativo\n");
}else{
        printf("Zero\n");
}
return0;
}

PARTE PRATICA (2 ore)
ESERCIZI GUIDATI
Esercizio 1: Disegnare Flow Chart Semplici (30 min)
1.1 Disegna il flow chart per calcolare la somma di due numeri.
Soluzione:
1.2 Disegna il flow chart per determinare se un numero è pari.
Soluzione:


1.3 Disegna il flow chart per trovare il maggiore tra due numeri.
Soluzione:


Esercizio 2: Flow Chart con Cicli (30 min)
2.1 Disegna il flow chart per stampare i numeri da 1 a 10.
Soluzione (con WHILE):


2.2 Disegna il flow chart per calcolare la somma dei primi N numeri naturali.
Soluzione:


Esercizio 3: Pseudocodice (30 min)
3.1 Scrivi lo pseudocodice per calcolare l’area di un cerchio.
Soluzione:
INIZIO
    COSTANTE PI = 3.14159


    LEGGI raggio
    area ← PI * raggio * raggio
    SCRIVI area
FINE
3.2 Scrivi lo pseudocodice per determinare se un anno è bisestile.
Soluzione:
INIZIO
    LEGGI anno
    SE (anno % 400 = 0) ALLORA
        SCRIVI "Bisestile"
    ALTRIMENTI SE (anno % 100 = 0) ALLORA
        SCRIVI "Non bisestile"
    ALTRIMENTI SE (anno % 4 = 0) ALLORA
        SCRIVI "Bisestile"
    ALTRIMENTI
        SCRIVI "Non bisestile"
    FINE SE
FINE
3.3 Scrivi lo pseudocodice per calcolare il fattoriale di un numero.
Soluzione:
INIZIO
    LEGGI n
    SE n < 0 ALLORA
        SCRIVI "Errore: numero negativo"
    ALTRIMENTI
        fattoriale ← 1
        i ← 1
        MENTRE i <= n FARE
            fattoriale ← fattoriale * i

            i ← i + 1
        FINE MENTRE
        SCRIVI fattoriale
    FINE SE
FINE
3.4 Scrivi lo pseudocodice per trovare il minimo in una sequenza di N numeri.
Soluzione:
INIZIO
    LEGGI n
    LEGGI primo_numero
    minimo ← primo_numero
    PER i DA 2 A n FARE
        LEGGI numero
        SE numero < minimo ALLORA
            minimo ← numero
        FINE SE
    FINE PER
    SCRIVI minimo
FINE
Esercizio 4: Traduzione Flow Chart → Pseudocodice (30 min)
4.1 Dato il seguente flow chart, scrivi il corrispondente pseudocodice.
Flow Chart: Tabellina di un numero

Soluzione:
INIZIO
    LEGGI n
    i ← 1
    MENTRE i <= 10 FARE
        risultato ← n * i
        SCRIVI risultato


        i ← i + 1
    FINE MENTRE
FINE
4.2 Scrivi il pseudocodice per il seguente flow chart che conta i numeri positivi.
Flow Chart: Contare quanti numeri positivi in una sequenza di N numeri

Soluzione:
INIZIO
    LEGGI n
    contatore ← 0
    PER i DA 1 A n FARE
        LEGGI numero
        SE numero > 0 ALLORA
            contatore ← contatore + 1
        FINE SE
    FINE PER
    SCRIVI contatore
FINE
4.3 Scrivi il pseudocodice per validare un voto (deve essere tra 0 e 10).
Soluzione:
INIZIO
    RIPETI
        LEGGI voto
        SE voto < 0 O voto > 10 ALLORA
            SCRIVI "Voto non valido, riprova"
        FINE SE
    FINCHÉ voto >= 0 E voto <= 10
    SCRIVI "Voto accettato:", voto
FINE

ESERCIZI AUTONOMI
Esercizio 5: Flow Chart Complessi (da svolgere in classe)
5.1 Disegna il flow chart per un programma che legge 3 numeri e li stampa in ordine
crescente.
Suggerimenti:
Usa variabili A, B, C per i tre numeri
Confronta a coppie e scambia se necessario
Puoi usare variabili temporanee per lo scambio
5.2 Disegna il flow chart per calcolare la media di N voti, escludendo il voto più basso e
il voto più alto.
Suggerimenti:
Leggi N voti
Trova il minimo e il massimo
Calcola la somma totale
Sottrai min e max dalla somma
Dividi per (N-2)
5.3 Disegna il flow chart per verificare se un numero è primo.
Suggerimenti:
Un numero è primo se divisibile solo per 1 e se stesso
Controlla divisibilità da 2 fino a N-1 (o meglio, fino a √N)
Se trovi un divisore, non è primo
Esercizio 6: Pseudocodice Avanzato
6.1 Scrivi lo pseudocodice per la ricerca sequenziale di un elemento in un array.
Specifiche:
Input: array di N elementi, elemento da cercare
Output: posizione dell’elemento (o -1 se non trovato)
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

6.2 Scrivi lo pseudocodice per invertire un array.
Specifiche:
Input: array di N elementi
Output: array con elementi in ordine inverso
Suggerimento: scambia primo con ultimo, secondo con penultimo, ecc.
6.3 Scrivi lo pseudocodice per il gioco “Indovina il numero”.
Specifiche:
Il computer “pensa” un numero tra 1 e 100
L’utente ha 7 tentativi per indovinarlo
Dopo ogni tentativo, il computer dice se il numero è più alto o più basso
Se l’utente indovina, vince; altrimenti perde
ESERCIZI DA SVOLGERE A CASA
Homework 1: Disegna il flow chart e scrivi lo pseudocodice per calcolare il massimo
comun divisore (MCD) tra due numeri usando l’algoritmo di Euclide.
Algoritmo: MCD(a,b) = MCD(b, a%b) finché b ≠ 0
Homework 2: Disegna il flow chart per convertire un numero decimale in binario.
Suggerimento: dividi ripetutamente per 2 e memorizza i resti
Homework 3: Scrivi lo pseudocodice per ordinare un array di N numeri in ordine
crescente (usa il Bubble Sort).
Confronta elementi adiacenti e scambiali se non in ordine
Ripeti finché non ci sono più scambi
Homework 4: Disegna il flow chart per calcolare la sequenza di Fibonacci fino all’N-
esimo termine.
Fibonacci: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

Homework 5: Scrivi lo pseudocodice per un programma che gestisce un menu con 4
opzioni:
Calcola area cerchio
Calcola area rettangolo
Calcola area triangolo
Esci
ESERCIZI DI ANALISI E CORREZIONE
Esercizio 7: Trova gli Errori
7.1 Il seguente flow chart ha degli errori logici. Individuali e correggili.
Flow Chart Errato: Somma numeri positivi
1. 
2. 
3. 
4. 

Problemi:
Manca una condizione di uscita dal ciclo
Il flusso non è chiaro
Non si sa quanti numeri leggere
Versione Corretta:
1. 
2. 
3. 

7.2 Correggi il seguente pseudocodice che dovrebbe calcolare la media di N numeri:
Pseudocodice Errato:
INIZIO
    LEGGI n
    somma ← 0
    PER i DA 1 A n FARE
        LEGGI numero
        somma ← numero
    FINE PER
    media ← somma / i
    SCRIVI media
FINE
Errori:
somma ← numero sovrascrive invece di sommare
somma / i usa i che vale n+1 dopo il ciclo
Dovrebbe dividere per n, non per i
Pseudocodice Corretto:
INIZIO
    LEGGI n
    somma ← 0
    PER i DA 1 A n FARE
        LEGGI numero
        somma ← somma + numero
    FINE PER
    media ← somma / n
    SCRIVI media
FINE
1. 
2. 
3. 

APPROFONDIMENTI E CURIOSITÀ
Storia dei Flow Chart
I diagrammi di flusso furono introdotti da Frank Gilbreth nel 1921 per documentare i
processi industriali. Nel 1947, Herman Goldstine e John von Neumann li adattarono
per la programmazione. Divennero standard con l’ANSI (American National Standards
Institute) negli anni ’60.
Diagrammi di Nassi-Shneiderman
Alternativa ai flow chart tradizionali, usano blocchi rettangolari nidificati invece di frecce.
Utili per evidenziare la programmazione strutturata.
Unified Modeling Language (UML)
Nei progetti software moderni, i flow chart sono stati in parte sostituiti da diagrammi UML
più sofisticati:
Diagrammi di attività
Diagrammi di sequenza
Diagrammi di stato
Tool Online per Flow Chart
draw.io (diagrams.net): gratuito, potente
Lucidchart: professionale, con collaborazione
Flowgorithm: specifico per algoritmi, genera anche codice
Creately: semplice e intuitivo
Visual Paradigm: completo ma complesso
• 
• 
• 
• 
• 
• 
• 
• 

RIEPILOGO COSTRUTTI
Costrutto Scopo Quando usarlo
SEQUEN
ZA Eseguire azioni in ordineSempre, è la base
IF Decidere tra due
alternative Quando hai una scelta binaria
IF
nidificato
Decidere tra più
alternative Quando hai più condizioni da verificare
WHILE Ripetere finché
condizione vera Quando non sai quante iterazioni servono
DO-
WHILE
Ripetere almeno una
volta
Quando il blocco deve eseguirsi sempre
almeno 1 volta
FOR Ripetere N volte Quando sai esattamente quante iterazioni
servono
CHECKLIST PER DISEGNARE FLOW CHART
✓ Hai un solo terminatore “INIZIO”?
✓ Hai almeno un terminatore “FINE”?
✓ Tutte le frecce hanno una direzione chiara?
✓ Ogni rombo decisionale ha esattamente 2 uscite (SI/NO)?
✓ Non ci sono percorsi che portano a nulla (deadlock)?
✓ Non ci sono cicli infiniti involontari?
✓ I nomi delle variabili sono significativi?
✓ Il flow chart è leggibile e ben spaziato?
✓ Hai evitato incroci di linee (usando connettori)?
✓ Ogni simbolo è usato correttamente?

PUNTI CHIAVE DELLA LEZIONE
✓ I flow chart visualizzano gli algoritmi usando simboli standard
✓ I tre costrutti fondamentali sono: sequenza, selezione, iterazione
✓ Qualsiasi algoritmo può essere espresso con questi tre costrutti
✓ Lo pseudocodice è un ponte tra algoritmo e codice
✓ WHILE controlla prima, DO-WHILE controlla dopo
✓ FOR è ideale quando conosci il numero di iterazioni
✓ Disegnare flow chart aiuta a pensare prima di programmare
✓ Dal flow chart al codice è un passaggio naturale
PREPARAZIONE PER LA PROSSIMA
LEZIONE
Nella prossima lezione studieremo:
Sistemi numerici: decimale, binario, ottale, esadecimale
Conversioni tra basi numeriche
Rappresentazione degli interi in binario
Complemento a 2 per numeri negativi
Porta con te:
Flow chart degli esercizi homework completati
Calcolatrice (utile per conversioni)
Domande sui costrutti o pseudocodice
ESERCIZIO FINALE DI SINTESI
Progetto Mini: Disegna il flow chart completo e scrivi lo pseudocodice per un
programma che:
Chiede all’utente quanti numeri vuole inserire (N)
Legge N numeri
• 
• 
• 
• 
• 
• 
• 
1. 
2. 

Calcola e visualizza: 
La somma di tutti i numeri
La media
Il numero più grande
Il numero più piccolo
Quanti numeri sono pari
Quanti numeri sono dispari
Questo esercizio riassume tutti i costrutti visti oggi!
Suggerimento: Dividi il problema in sottoproblemi più piccoli, crea un flow chart per
ognuno, poi combinali.
GLOSSARIO TECNICO
Algoritmo: Sequenza di istruzioni per risolvere un problema
Flow Chart: Rappresentazione grafica di un algoritmo
Costrutti: Strutture di controllo fondamentali (sequenza, selezione, iterazione)
Pseudocodice: Linguaggio semi-formale per descrivere algoritmi
Iterazione: Ripetizione di un blocco di istruzioni (loop/ciclo)
Condizione: Espressione logica che può essere vera o falsa
Terminatore: Simbolo che indica inizio o fine di un algoritmo
Decisione: Punto in cui l’algoritmo sceglie tra percorsi alternativi
Connettore: Simbolo usato per collegare parti del flow chart
Nidificazione: Inserimento di un costrutto dentro un altro
Buon lavoro e ci vediamo alla prossima lezione! 🚀
3. 
◦ 
◦ 
◦ 
◦ 
◦ 
◦ 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 


---

# lezione3 binario

**File:** `lezione3 binario.pdf`
**Tipo:** `.pdf`
**Dimensione:** 140.0 KB
**Ultima modifica:** 02/07/2026 09:24

---

LEZIONE 3 - Sistemi Numerici e
Rappresentazione Binaria degli Interi
Durata: 4 ore | Teoria: 2h | Esercizi: 2h
PARTE TEORICA (2 ore)
3.1 Sistemi di Numerazione Posizionali (25 min)
Cosa Significa “Posizionale”?
Un sistema di numerazione è posizionale quando il valore di una cifra dipende sia dal
suo valore intrinseco che dalla sua posizione.
Esempio in base 10:
Il numero 352 significa:
3 centinaia (3 × 100)
5 decine (5 × 10)
2 unità (2 × 1)
Formula generale:
352₁₀ = 3×10² + 5×10¹ + 2×10⁰
      = 3×100 + 5×10 + 2×1
      = 300 + 50 + 2
      = 352
Componenti di un Sistema Posizionale
1. Base (o radice):
Determina quante cifre diverse si possono usare
• 
• 
• 
• 

Base 10: cifre da 0 a 9
Base 2: cifre 0 e 1
Base 8: cifre da 0 a 7
Base 16: cifre da 0 a 9 e A a F
2. Cifre:
Simboli usati per rappresentare valori
Il valore massimo di una cifra è (base - 1)
3. Peso Posizionale:
Ogni posizione ha un peso che è una potenza della base
Le posizioni si numerano da destra verso sinistra partendo da 0
Rappresentazione generale:
N = dₙ×baseⁿ + dₙ₋₁×baseⁿ⁻¹ + ... + d₁×base¹ + d₀×base⁰
3.2 Il Sistema Decimale (Base 10) (10 min)
Il sistema decimale è quello che usiamo quotidianamente.
Caratteristiche:
Base: 10
Cifre: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
Pesi posizionali: …10³, 10², 10¹, 10⁰ = …1000, 100, 10, 1
Esempio Dettagliato: 2547₁₀
Posizione:    3    2    1    0
Cifra:        2    5    4    7
Peso:       10³  10²  10¹  10⁰
            1000  100   10    1
Valore: 2×1000 + 5×100 + 4×10 + 7×1
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

      = 2000 + 500 + 40 + 7
      = 2547
Numeri con Virgola:
Numero: 123.45₁₀
Posizione:   2    1    0   -1   -2
Cifra:       1    2    3    4    5
Peso:      10²  10¹  10⁰  10⁻¹ 10⁻²
           100   10    1   0.1  0.01
Valore: 1×100 + 2×10 + 3×1 + 4×0.1 + 5×0.01
      = 100 + 20 + 3 + 0.4 + 0.05
      = 123.45
3.3 Il Sistema Binario (Base 2) (30 min)
Il sistema binario è fondamentale per i computer, che lavorano solo con due stati:
acceso/spento, vero/falso, 1/0.
Caratteristiche:
Base: 2
Cifre: 0, 1 (chiamate bit = binary digit)
Pesi posizionali: …2³, 2², 2¹, 2⁰ = …8, 4, 2, 1
Tabella delle Potenze di 2 (da memorizzare!)
Esponente Potenza Valore Decimale
2⁰ 2⁰ 1
2¹ 2¹ 2
• 
• 
• 

Esponente Potenza Valore Decimale
2² 2² 4
2³ 2³ 8
2⁴ 2⁴ 16
2⁵ 2⁵ 32
2⁶ 2⁶ 64
2⁷ 2⁷ 128
2⁸ 2⁸ 256
2⁹ 2⁹ 512
2¹⁰ 2¹⁰ 1024
2¹⁶ 2¹⁶ 65536
Esempio: Convertire 1011₂ in Decimale
Posizione:    3    2    1    0
Cifra:        1    0    1    1
Peso:        2³   2²   2¹   2⁰
              8    4    2    1
Valore: 1×8 + 0×4 + 1×2 + 1×1
      = 8 + 0 + 2 + 1
      = 11₁₀
Conversione Binario → Decimale (Metodo Generale)
Formula:
Somma di (cifra × 2^posizione) per ogni bit

Esempi:
10101₂ in decimale:
= 1×2⁴ + 0×2³ + 1×2² + 0×2¹ + 1×2⁰
= 1×16 + 0×8 + 1×4 + 0×2 + 1×1
= 16 + 0 + 4 + 0 + 1
= 21₁₀
11111111₂ in decimale:
= 1×128 + 1×64 + 1×32 + 1×16 + 1×8 + 1×4 + 1×2 + 1×1
= 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1
= 255₁₀
10000000₂ in decimale:
= 1×128 = 128₁₀
Conversione Decimale → Binario
Metodo delle Divisioni Successive:
Dividi il numero decimale per 2
Annota il resto (0 o 1)
Usa il quoziente per la divisione successiva
Ripeti fino a quando il quoziente diventa 0
Il numero binario si legge dai resti dal basso verso l’alto
Esempio 1: Convertire 13₁₀ in binario
13 ÷ 2 = 6  resto 1  ←┐
 6 ÷ 2 = 3  resto 0   │
 3 ÷ 2 = 1  resto 1   │ Leggi dal basso
 1 ÷ 2 = 0  resto 1  ←┘ verso l'alto
1. 
1. 
1. 
1. 
2. 
3. 
4. 
5. 

Risultato: 13₁₀ = 1101₂
Verifica:
1101₂ = 1×8 + 1×4 + 0×2 + 1×1 = 8+4+0+1 = 13₁₀ ✓
Esempio 2: Convertire 25₁₀ in binario
25 ÷ 2 = 12  resto 1  ←┐
12 ÷ 2 = 6   resto 0   │
 6 ÷ 2 = 3   resto 0   │ Leggi
 3 ÷ 2 = 1   resto 1   │
 1 ÷ 2 = 0   resto 1  ←┘
Risultato: 25₁₀ = 11001₂
Esempio 3: Convertire 100₁₀ in binario
100 ÷ 2 = 50  resto 0  ←┐
 50 ÷ 2 = 25  resto 0   │
 25 ÷ 2 = 12  resto 1   │
 12 ÷ 2 = 6   resto 0   │
  6 ÷ 2 = 3   resto 0   │ Leggi
  3 ÷ 2 = 1   resto 1   │
  1 ÷ 2 = 0   resto 1  ←┘
Risultato: 100₁₀ = 1100100₂

Operazioni Aritmetiche in Binario
Addizione:
Regole base:
0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 10 (scrivi 0, riporta 1)
1 + 1 + 1 (riporto) = 11 (scrivi 1, riporta 1)
Esempio: 1011₂ + 0110₂
    1011  (11₁₀)
  + 0110  ( 6₁₀)
  ------
   10001  (17₁₀)
Passo per passo:
Colonna 0: 1+0 = 1
Colonna 1: 1+1 = 0, riporto 1
Colonna 2: 0+1+1(riporto) = 0, riporto 1
Colonna 3: 1+0+1(riporto) = 0, riporto 1
Colonna 4: 1(riporto) = 1
Sottrazione:
Regole base:
0 - 0 = 0
1 - 0 = 1
1 - 1 = 0
0 - 1 = 1 (con prestito dalla posizione successiva)
Esempio: 1010₂ - 0011₂
    1010  (10₁₀)
  - 0011  ( 3₁₀)
• 
• 
• 
• 
• 
• 
• 
• 
• 

  ------
    0111  ( 7₁₀)
3.4 Sistema Ottale (Base 8) (15 min)
Il sistema ottale usa 8 cifre ed era molto utilizzato nei primi computer.
Caratteristiche:
Base: 8
Cifre: 0, 1, 2, 3, 4, 5, 6, 7
Pesi posizionali: …8³, 8², 8¹, 8⁰ = …512, 64, 8, 1
Conversione Ottale → Decimale
Esempio: 347₈ in decimale
347₈ = 3×8² + 4×8¹ + 7×8⁰
     = 3×64 + 4×8 + 7×1
     = 192 + 32 + 7
     = 231₁₀
Conversione Decimale → Ottale
Metodo: Divisioni successive per 8
Esempio: 100₁₀ in ottale
100 ÷ 8 = 12  resto 4  ←┐
 12 ÷ 8 = 1   resto 4   │ Leggi
  1 ÷ 8 = 0   resto 1  ←┘
Risultato: 100₁₀ = 144₈
• 
• 
• 

Conversione Binario ↔ Ottale
Regola veloce: Ogni cifra ottale corrisponde a 3 bit.
Tabella di conversione:
Ottale Binario
0 000
1 001
2 010
3 011
4 100
5 101
6 110
7 111
Esempio 1: 101110101₂ → Ottale
Raggruppa da destra in gruppi di 3:
101 110 101
 5   6   5
Risultato: 101110101₂ = 565₈
Esempio 2: 743₈ → Binario
7    4    3
111  100  011
Risultato: 743₈ = 111100011₂

3.5 Sistema Esadecimale (Base 16) (20 min)
Il sistema esadecimale è molto usato in informatica per rappresentare indirizzi di
memoria e codici colore.
Caratteristiche:
Base: 16
Cifre: 0-9, A-F (dove A=10, B=11, C=12, D=13, E=14, F=15)
Pesi posizionali: …16³, 16², 16¹, 16⁰ = …4096, 256, 16, 1
Tabella Esadecimale
Esadecimale Decimale Binario
0 0 0000
1 1 0001
2 2 0010
3 3 0011
4 4 0100
5 5 0101
6 6 0110
7 7 0111
8 8 1000
9 9 1001
A 10 1010
B 11 1011
C 12 1100
D 13 1101
• 
• 
• 

Esadecimale Decimale Binario
E 14 1110
F 15 1111
Conversione Esadecimale → Decimale
Esempio: 2A3₁₆ in decimale
2A3₁₆ = 2×16² + A×16¹ + 3×16⁰
      = 2×256 + 10×16 + 3×1
      = 512 + 160 + 3
      = 675₁₀
Esempio: FF₁₆ in decimale
FF₁₆ = F×16¹ + F×16⁰
     = 15×16 + 15×1
     = 240 + 15
     = 255₁₀
Conversione Decimale → Esadecimale
Metodo: Divisioni successive per 16
Esempio: 1000₁₀ in esadecimale
1000 ÷ 16 = 62  resto 8   ←┐
  62 ÷ 16 = 3   resto 14(E) │ Leggi
   3 ÷ 16 = 0   resto 3    ←┘
Risultato: 1000₁₀ = 3E8₁₆

Conversione Binario ↔ Esadecimale
Regola veloce: Ogni cifra esadecimale corrisponde a 4 bit.
Esempio 1: 11010110₂ → Esadecimale
Raggruppa da destra in gruppi di 4:
1101 0110
 D    6
Risultato: 11010110₂ = D6₁₆
Esempio 2: 1A7F₁₆ → Binario
1     A     7     F
0001  1010  0111  1111
Risultato: 1A7F₁₆ = 0001101001111111₂
Esempio 3: Semplifica 101111010011₂
Conversione diretta: lungo e complicato
Via esadecimale:
1011 1101 0011
 B    D    3
Più facile ricordare BD3₁₆!

3.6 Rappresentazione degli Interi Positivi (20 min)
Bit, Byte e Parole
Terminologia:
Bit: singola cifra binaria (0 o 1)
Nibble: 4 bit (una cifra esadecimale)
Byte: 8 bit (standard de facto)
Word (Parola): dimensione dipende dall’architettura (16, 32, 64 bit)
Range di Rappresentazione
Con n bit si possono rappresentare 2ⁿ numeri diversi.
Per interi positivi (senza segno):
Valore minimo: 0
Valore massimo: 2ⁿ - 1
Tabella Range:
Bit Numeri Rappresentabili Range (0 a max)
1 bit 2 0 - 1
2 bit 4 0 - 3
3 bit 8 0 - 7
4 bit 16 0 - 15
8 bit 256 0 - 255
16 bit 65,536 0 - 65,535
32 bit 4,294,967,296 0 - 4,294,967,295
64 bit 18,446,744,073,709,551,6160 - 18,446,744,073,709,551,615
Esempi:
• 
• 
• 
• 
• 
• 

8 bit senza segno:
Minimo: 00000000₂ = 0₁₀
Massimo: 11111111₂ = 255₁₀
16 bit senza segno:
Minimo: 0000000000000000₂ = 0₁₀
Massimo: 1111111111111111₂ = 65535₁₀
Tipi in C (Unsigned)
In C, i tipi senza segno si dichiarano con unsigned:
3.7 Rappresentazione degli Interi con Segno (20 min)
Problema: Come Rappresentare i Negativi?
Con n bit dobbiamo rappresentare sia positivi che negativi. Servono 3 metodi storici:
1. Modulo e Segno (Sign-Magnitude)
Bit più significativo (MSB): 0 = positivo, 1 = negativo
Altri bit: valore assoluto
Con 8 bit:
unsignedchar c; // 8 bit: 0 a 255
unsignedshort s; // 16 bit: 0 a 65535
unsignedint i; // 32 bit: 0 a 4294967295
unsignedlong l; // 32/64 bit (dipende da architettura)
unsignedlonglong ll; // 64 bit
• 
• 

+5 = 00000101
-5 = 10000101
+0 = 00000000
-0 = 10000000  (problema: due rappresentazioni per zero!)
Svantaggi:
Due rappresentazioni per lo zero
Circuiti di addizione complessi
Non più usato nei computer moderni
2. Complemento a 1
Positivi: come al solito
Negativi: inverti tutti i bit del corrispondente positivo
Con 8 bit:
+5 = 00000101
-5 = 11111010 (NOT di 00000101)
+0 = 00000000
-0 = 11111111  (problema: ancora due zeri!)
Svantaggio: Ancora due rappresentazioni per zero
3. Complemento a 2 (Usato Oggi!)
Metodo più importante! Tutti i computer moderni usano il complemento a 2.
Regola per calcolare il complemento a 2:
Prendi il valore binario positivo
Inverti tutti i bit (complemento a 1)
Aggiungi 1
Esempio: -5 in complemento a 2 (8 bit)
• 
• 
• 
• 
• 
1. 
2. 
3. 

+5 = 00000101
Complemento a 1: 11111010
Aggiungi 1:     + 00000001
               -----------
-5 = 11111011
Esempio: -1 in complemento a 2 (8 bit)
+1 = 00000001
Complemento a 1: 11111110
Aggiungi 1:     + 00000001
               -----------
-1 = 11111111
Esempio: -128 in complemento a 2 (8 bit)
+128 non rappresentabile in 8 bit signed!
Ma -128 = 10000000
Range con Complemento a 2
Con n bit in complemento a 2:
Valore minimo: -2ⁿ⁻¹
Valore massimo: +2ⁿ⁻¹ - 1
Tabella Range Signed:
Bit Range (min a max)
8 bit -128 a +127
16 bit -32,768 a +32,767
32 bit -2,147,483,648 a +2,147,483,647
• 
• 

Bit Range (min a max)
64 bit -9,223,372,036,854,775,808 a +9,223,372,036,854,775,807
Nota: C’è un numero negativo in più del massimo positivo!
Come Riconoscere il Segno
Regola: Se il bit più significativo (MSB) è:
0 → numero positivo
1 → numero negativo
Esempi 8 bit:
00000101 = +5  (MSB = 0)
10000101 = -123 (MSB = 1)
11111111 = -1  (MSB = 1)
01111111 = +127 (MSB = 0)
Convertire da Complemento a 2 a Decimale
Se MSB = 0 (positivo): conversione normale
Se MSB = 1 (negativo):
Sottrai 1
Inverti tutti i bit
Converti in decimale
Aggiungi il segno meno
Esempio: 11111011₂ (8 bit) in decimale
MSB = 1, quindi negativo
Sottrai 1:       11111011
                -00000001
                ---------
• 
• 
1. 
2. 
3. 
4. 

                 11111010
Inverti bit:     00000101
Converti:        00000101 = 5₁₀
Risultato: -5₁₀
Metodo alternativo veloce:
11111011₂ = -128 + 64 + 32 + 16 + 8 + 2 + 1
          = -128 + 123
          = -5₁₀
Il bit MSB vale -2⁷ = -128!
Vantaggi del Complemento a 2
Una sola rappresentazione per zero
Addizione semplice: stessa circuiteria per positivi e negativi
Estensione del segno: facile convertire tra dimensioni diverse
Esempio Addizione:
  +5:  00000101
+ -3:  11111101
      ---------
  +2:  00000010  (ignora il riporto finale)
Overflow e Underflow
Overflow: il risultato supera il massimo rappresentabile
Esempio 8 bit signed:
1. 
2. 
3. 

  +100:  01100100
+ +50:   00110010
       ----------
  -106:  10010110  ← OVERFLOW! Risultato errato
Underflow: il risultato è minore del minimo rappresentabile
  -100:  10011100
+ -50:   11001110
       ----------
  +106:  01101010  ← UNDERFLOW! Risultato errato
Come rilevare overflow in somma:
Due positivi → risultato negativo = OVERFLOW
Due negativi → risultato positivo = UNDERFLOW
Positivo + negativo → NO overflow possibile
PARTE PRATICA (2 ore)
ESERCIZI GUIDATI
Esercizio 1: Conversioni Binario ↔ Decimale (20 min)
1.1 Converti in decimale i seguenti numeri binari:
1010₂
Soluzione:
1010₂ = 1×2³ + 0×2² + 1×2¹ + 0×2⁰
      = 8 + 0 + 2 + 0
      = 10₁₀
11001₂
• 
• 
• 
1. 
1. 

Soluzione:
11001₂ = 1×16 + 1×8 + 0×4 + 0×2 + 1×1
       = 16 + 8 + 1
       = 25₁₀
10000001₂
Soluzione:
10000001₂ = 1×128 + 0×64 + ... + 1×1
          = 128 + 1
          = 129₁₀
11111111₂
Soluzione:
11111111₂ = 128+64+32+16+8+4+2+1
          = 255₁₀
(oppure: 2⁸-1 = 256-1 = 255)
1.2 Converti in binario i seguenti numeri decimali:
18₁₀
Soluzione:
18 ÷ 2 = 9  resto 0  ←┐
 9 ÷ 2 = 4  resto 1   │
 4 ÷ 2 = 2  resto 0   │
 2 ÷ 2 = 1  resto 0   │
 1 ÷ 2 = 0  resto 1  ←┘
18₁₀ = 10010₂
63₁₀
1. 
1. 
1. 
1. 

Soluzione:
63 ÷ 2 = 31  resto 1  ←┐
31 ÷ 2 = 15  resto 1   │
15 ÷ 2 = 7   resto 1   │
 7 ÷ 2 = 3   resto 1   │
 3 ÷ 2 = 1   resto 1   │
 1 ÷ 2 = 0   resto 1  ←┘
63₁₀ = 111111₂
200₁₀
Soluzione:
200 ÷ 2 = 100  resto 0
100 ÷ 2 = 50   resto 0
 50 ÷ 2 = 25   resto 0
 25 ÷ 2 = 12   resto 1
 12 ÷ 2 = 6    resto 0
  6 ÷ 2 = 3    resto 0
  3 ÷ 2 = 1    resto 1
  1 ÷ 2 = 0    resto 1
200₁₀ = 11001000₂
Esercizio 3: Operazioni Aritmetiche in Binario (25 min)
3.1 Esegui le seguenti addizioni in binario:
1011₂ + 0110₂
Soluzione:
    1011  (11₁₀)
  + 0110  ( 6₁₀)
1. 
1. 

  ------
   10001  (17₁₀)
Verifica: 11 + 6 = 17 ✓
1111₂ + 0001₂
Soluzione:
    1111  (15₁₀)
  + 0001  ( 1₁₀)
  ------
   10000  (16₁₀)
Verifica: 15 + 1 = 16 ✓
10110₂ + 1101₂
Soluzione:
    10110  (22₁₀)
  +  1101  (13₁₀)
  -------
   100011  (35₁₀)
Passo per passo:
  1 1 1   (riporti)
    10110
  +  1101
  -------
   100011
Verifica: 22 + 13 = 35 ✓
1. 
1. 

3.2 Esegui le seguenti sottrazioni in binario:
1010₂ - 0011₂
Soluzione:
    1010  (10₁₀)
  - 0011  ( 3₁₀)
  ------
    0111  ( 7₁₀)
Verifica: 10 - 3 = 7 ✓
10000₂ - 0001₂
Soluzione:
    10000  (16₁₀)
  -  0001  ( 1₁₀)
  -------
    01111  (15₁₀)
Verifica: 16 - 1 = 15 ✓
3.3 Moltiplica 101₂ × 11₂:
Soluzione:
      101  (5₁₀)
    ×  11  (3₁₀)
    -----
      101  (5×1)
     101   (5×1, spostato)
    -----
     1111  (15₁₀)
Verifica: 5 × 3 = 15 ✓
1. 
1. 

Esercizio 4: Complemento a 2 (30 min)
4.1 Calcola il complemento a 2 dei seguenti numeri (8 bit):
Complemento a 2 di +10:
Soluzione:
+10 = 00001010
Step 1 - Inverti i bit:
11110101
Step 2 - Aggiungi 1:
  11110101
+ 00000001
----------
  11110110
-10 in complemento a 2 = 11110110₂
Complemento a 2 di +25:
Soluzione:
+25 = 00011001
Step 1 - Inverti i bit:
11100110
Step 2 - Aggiungi 1:
  11100110
+ 00000001
----------
  11100111
1. 
1. 

-25 in complemento a 2 = 11100111₂
Complemento a 2 di +127:
Soluzione:
+127 = 01111111
Step 1 - Inverti i bit:
10000000
Step 2 - Aggiungi 1:
  10000000
+ 00000001
----------
  10000001
-127 in complemento a 2 = 10000001₂
Complemento a 2 di +1:
Soluzione:
+1 = 00000001
Step 1 - Inverti i bit:
11111110
Step 2 - Aggiungi 1:
  11111110
+ 00000001
----------
  11111111
1. 
1. 

-1 in complemento a 2 = 11111111₂
4.2 Converti da complemento a 2 (8 bit) a decimale:
10000101₂
Soluzione:
MSB = 1, quindi negativo
Metodo 1 (tradizionale):
Step 1 - Sottrai 1:
  10000101
- 00000001
----------
  10000100
Step 2 - Inverti bit:
01111011
Step 3 - Converti:
01111011 = 64+32+16+8+2+1 = 123₁₀
Step 4 - Aggiungi segno:
Risultato: -123₁₀
Metodo 2 (veloce):
10000101₂ = -128 + 0 + 0 + 0 + 0 + 4 + 0 + 1
          = -128 + 5
          = -123₁₀
11111111₂
1. 
1. 

Soluzione:
MSB = 1, quindi negativo
Metodo veloce:
11111111₂ = -128 + 127 = -1₁₀
(Oppure: tutti 1 in complemento a 2 = sempre -1)
10000000₂
Soluzione:
MSB = 1, quindi negativo
10000000₂ = -128 + 0 = -128₁₀
(Il numero negativo più piccolo in 8 bit!)
01111111₂
Soluzione:
MSB = 0, quindi positivo
01111111₂ = 64+32+16+8+4+2+1 = 127₁₀
(Il numero positivo più grande in 8 bit!)
4.3 Esegui le seguenti operazioni in complemento a 2 (8 bit):
+5 + (-3)
Soluzione:
+5 = 00000101
-3: complemento a 2 di +3
+3 = 00000011
1. 
1. 
1. 

Inverti: 11111100
+1:      11111101
-3 = 11111101
Addizione:
    00000101  (+5)
  + 11111101  (-3)
  ----------
   100000010
Ignora il riporto (overflow oltre 8 bit):
00000010 = +2₁₀
Verifica: 5 + (-3) = 2 ✓
(-10) + (-20)
Soluzione:
+10 = 00001010
-10 = 11110110 (complemento a 2)
+20 = 00010100
-20 = 11101100 (complemento a 2)
Addizione:
    11110110  (-10)
  + 11101100  (-20)
  ----------
   111100010
Ignora riporto oltre 8 bit:
11100010
Converti in decimale (è negativo):
1. 

11100010 = -128 + 96 + 32 + 2
         = -128 + 130
         = -30₁₀ (WAIT! Errato!)
Metodo corretto:
11100010
- 1 = 11100001
NOT = 00011110 = 30₁₀
Quindi: -30₁₀
Verifica: -10 + (-20) = -30 ✓
Esercizio 5: Range e Overflow (20 min)
5.1 Determina il range di rappresentazione per:
4 bit unsigned
Soluzione:
2⁴ = 16 numeri
Range: 0 a 15
Minimo: 0000₂ = 0₁₀
Massimo: 1111₂ = 15₁₀
4 bit signed (complemento a 2)
Soluzione:
Range: -2³ a 2³-1
Range: -8 a +7
Minimo: 1000₂ = -8₁₀
Massimo: 0111₂ = +7₁₀
12 bit unsigned
1. 
1. 
1. 

Soluzione:
2¹² = 4096 numeri
Range: 0 a 4095₁₀
12 bit signed (complemento a 2)
Soluzione:
Range: -2¹¹ a 2¹¹-1
Range: -2048 a +2047₁₀
5.2 Identifica gli overflow (8 bit signed):
+100 + +50
Soluzione:
+100 = 01100100
+50  = 00110010
Addizione:
    01100100
  + 00110010
  ----------
    10010110
Risultato: 10010110₂
MSB = 1, quindi sembra negativo
Convertiamo: -106₁₀
OVERFLOW! ✗
Due positivi danno negativo = overflow
Risultato corretto sarebbe +150, ma non rappresentabile in 8 bit signed (max 
+127)
+50 + (-30)
1. 
1. 
1. 

Soluzione:
+50 = 00110010
-30 = 11100010 (complemento a 2 di +30)
Addizione:
    00110010
  + 11100010
  ----------
   100010100
Ignora riporto:
00010100 = +20₁₀
NESSUN OVERFLOW ✓
Verifica: 50 + (-30) = 20 ✓
(-100) + (-50)
Soluzione:
-100 = 10011100
-50  = 11001110
Addizione:
    10011100
  + 11001110
  ----------
   101101010
Ignora riporto:
01101010 = +106₁₀
UNDERFLOW! ✗
1. 

Due negativi danno positivo = underflow
Risultato corretto sarebbe -150, ma non rappresentabile
5.3 Qual è il valore di 11111111₂ in:
8 bit unsigned
Soluzione:
11111111₂ = 255₁₀
8 bit signed (complemento a 2)
Soluzione:
MSB = 1, quindi negativo
11111111₂ = -1₁₀
Esercizio 6: Problemi Applicativi (25 min)
6.1 Un sensore di temperatura invia valori in formato binario a 8 bit unsigned. Converti le
seguenti letture:
01100100₂ (temperatura in gradi Celsius)
Soluzione:
01100100₂ = 64 + 32 + 4 = 100₁₀
Temperatura: 100°C
11111111₂ (temperatura massima rilevabile)
1. 
1. 
1. 
1. 

Soluzione:
11111111₂ = 255₁₀
Temperatura massima: 255°C
Se il sensore deve misurare temperature da -50°C a +100°C, è sufficiente 8 bit
unsigned?
Soluzione:
NO! 8 bit unsigned va da 0 a 255.
Non può rappresentare valori negativi.
Serve 8 bit SIGNED (complemento a 2):
Range: -128 a +127
Copre da -50 a +100 ✓
6.2 Un sistema di controllo accessi usa codici a 16 bit. Quanti codici diversi sono
possibili?
Soluzione:
Con 16 bit: 2¹⁶ = 65,536 codici diversi
6.3 In un videogioco, le coordinate X,Y dei personaggi sono memorizzate come interi a
16 bit signed. Qual è l’area di gioco massima?
Soluzione:
16 bit signed: da -32,768 a +32,767
Coordinate X: da -32,768 a +32,767 (65,536 posizioni)
Coordinate Y: da -32,768 a +32,767 (65,536 posizioni)
Area totale: 65,536 × 65,536 = 4,294,967,296 posizioni
6.4 Un colore RGB usa 8 bit per canale (Rosso, Verde, Blu). Quanti colori diversi si
possono rappresentare?
1. 

Soluzione:
Ogni canale: 2⁸ = 256 livelli (0-255)
Totale combinazioni: 256 × 256 × 256 = 16,777,216 colori
Esempi:
Rosso puro: (255, 0, 0) = FF0000₁₆
Verde puro: (0, 255, 0) = 00FF00₁₆
Blu puro: (0, 0, 255) = 0000FF₁₆
Bianco: (255, 255, 255) = FFFFFF₁₆
Nero: (0, 0, 0) = 000000₁₆
6.5 Un contatore a 8 bit parte da 250 e viene incrementato di 1 per 10 volte. Cosa
succede?
Se è unsigned:
Soluzione:
250₁₀ = 11111010₂
Incrementi:
250 → 251 → 252 → 253 → 254 → 255 → 0 → 1 → 2 → 3 → 4
Dopo 10 incrementi: 4₁₀
(Overflow al 6° incremento: 255 + 1 = 0)
Se è signed (complemento a 2):
Soluzione:
250 non è rappresentabile in 8 bit signed (max +127)
Ma se partiamo da -6 (= 11111010 in complemento a 2):
-6 → -5 → -4 → -3 → -2 → -1 → 0 → 1 → 2 → 3 → 4
Dopo 10 incrementi: +4₁₀
1. 
1. 

ESERCIZI AUTONOMI DA COMPLETARE IN CLASSE
Esercizio 7: Tabella di Conversione
Completa la seguente tabella di conversione:
Decimale Binario (8 bit) Ottale Esadecimale
15 00001111 17 F
32 ? ? ?
? 01010101 ? ?
? ? 144 ?
200 ? ? ?
? ? ? A5
Soluzioni:
Decimale Binario (8 bit) Ottale Esadecimale
15 00001111 17 F
32 00100000 40 20
85 01010101 125 55
100 01100100 144 64
200 11001000 310 C8
165 10100101 245 A5

Esercizio 8: Problemi Misti
8.1 Converti 10101010₂ in tutte le basi:
Decimale (unsigned): _______
Decimale (signed): _______
Ottale: _______
Esadecimale: _______
8.2 Trova il numero binario a 8 bit che rappresenta:
Il più grande numero positivo in signed: _______
Il più piccolo numero negativo in signed: _______
Il numero 100 in unsigned: _______
8.3 Esegui 11110000₂ + 00001111₂ e interpreta il risultato come:
Unsigned: _______
Signed (complemento a 2): _______
ESERCIZI DA SVOLGERE A CASA
Homework 1: Crea una tabella con tutti i numeri da 0 a 31 in:
Decimale
Binario (5 bit)
Ottale
Esadecimale
Homework 2: Calcola il complemento a 2 (8 bit) di tutti i numeri da -10 a +10 e verifica
sommando numero + complemento che ottieni sempre zero (ignorando il riporto).
Homework 3: Scrivi un algoritmo (flow chart o pseudocodice) per convertire un numero
decimale in binario usando il metodo delle divisioni successive.
Homework 4: Ricerca su internet e spiega brevemente:
Cos’è la codifica BCD (Binary Coded Decimal)
Cos’è la codifica Gray (o codifica riflessa)
Dove vengono utilizzate queste codifiche
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

Homework 5: Problemi applicativi:
a) Quanti bit servono per rappresentare gli anni dal 1900 al 2100?
b) Un disco rigido ha capacità di 512 GB. Quanti bit servono per indirizzare ogni byte?
c) IPv4 usa indirizzi a 32 bit. Quanti indirizzi IP diversi esistono?
APPROFONDIMENTI
Storia dei Sistemi di Numerazione
Sistema Babilonese (2000 a.C.)
Base 60 (sessagesimale)
Ancora usato oggi: 60 secondi, 60 minuti, 360 gradi
Sistema Romano
Non posizionale: VII, XIV, MCMXCIV
Difficile fare calcoli!
Sistema Indiano-Arabo (500 d.C.)
Base 10 posizionale
Introdotto in Europa da Fibonacci (1202)
Sistema Binario
Gottfried Leibniz (1679): “De Progressione Dyadica”
George Boole (1854): algebra booleana
Claude Shannon (1937): applicazione ai circuiti elettrici
ENIAC (1945): primo computer elettronico binario
Perché i Computer Usano il Binario?
Ragioni tecnologiche:
Affidabilità: Più facile distinguere tra 2 stati (0/1) che tra 10 (0-9)
Componenti semplici: Transistor = interruttore on/off
Rumore: Sistema binario molto resistente ai disturbi elettrici
Logica: Algebra booleana (AND, OR, NOT) naturalmente binaria
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
1. 
2. 
3. 
4. 

Furono tentate alternative:
Computer ternari (URSS, anni ’50): Setun usava base 3
Computer decimali: ENIAC inizialmente era parzialmente decimale
Tutti abbandonati perché il binario è più efficiente
Altre Rappresentazioni dei Negativi
Eccesso-K (Biased Representation):
Usato negli esponenti dei floating-point (IEEE 754)
Aggiungi una costante K a tutti i numeri
Esempio: Eccesso-128 con 8 bit 
0₁₀ → 128₁₀ → 10000000₂
-128₁₀ → 0₁₀ → 00000000₂
+127₁₀ → 255₁₀ → 11111111₂
Il Problema dell’Anno 2038
Y2K Bug per Unix!
I sistemi Unix memorizzano il tempo come:
Secondi dal 1 gennaio 1970
Tipo time_t: intero signed a 32 bit
Range:
Minimo: -2,147,483,648 sec → 13 dicembre 1901
Massimo: +2,147,483,647 sec → 19 gennaio 2038 03:14:07 UTC
Dopo questa data: overflow! Il tempo tornerebbe al 1901.
Soluzione: Passare a time_t a 64 bit (già implementato in sistemi moderni)
Curiosità: Base64
NON è base 64 matematica! È una codifica per trasmettere dati binari come testo.
• 
• 
• 
• 
• 
◦ 
◦ 
◦ 
• 
• 
• 
• 

Usa 64 caratteri:
A-Z (26)
a-z (26)
0-9 (10)
e / (2)
Usato in:
Email (MIME)
URL
Immagini embedded in HTML
Esempio:
"Hello" → "SGVsbG8="
Codici di Correzione Errori
Codice di Hamming:
Aggiunge bit di parità per rilevare e correggere errori
Esempio: trasmissione dati
Dati: 1011
Hamming: 1011010 (con 3 bit di parità)
Se 1 bit viene corrotto durante la trasmissione, può essere corretto automaticamente!
Usato in:
RAM ECC (Error Correcting Code)
Hard disk
Trasmissioni satellitari
• 
• 
• 
• ◦ 
• 
• 
• 
• 
• 
• 

RIEPILOGO FORMULE
Conversione da Base B a Decimale
N_B = dₙ×Bⁿ + dₙ₋₁×Bⁿ⁻¹ + ... + d₁×B¹ + d₀×B⁰
Conversione da Decimale a Base B
Divisioni successive per B, leggi i resti dal basso verso l'alto
Range Unsigned (n bit)
Min = 0
Max = 2ⁿ - 1
Numeri = 2ⁿ
Range Signed Complemento a 2 (n bit)
Min = -2ⁿ⁻¹
Max = 2ⁿ⁻¹ - 1
Numeri = 2ⁿ
Complemento a 2
-X = NOT(X) + 1
oppure
-X = 2ⁿ - X

Conversione Binario ↔ Ottale
1 cifra ottale = 3 bit
Conversione Binario ↔ Esadecimale
1 cifra esadecimale = 4 bit = 1 nibble
TABELLE DI RIFERIMENTO RAPIDO
Potenze di 2 (Memorizza!)
2⁰ = 1        2⁸ = 256
2¹ = 2        2⁹ = 512
2² = 4        2¹⁰ = 1,024 (≈ 1K)
2³ = 8        2²⁰ = 1,048,576 (≈ 1M)
2⁴ = 16       2³⁰ = 1,073,741,824 (≈ 1G)
2⁵ = 32
2⁶ = 64
2⁷ = 128
Prefissi Binari (IEC Standard)
1 KiB = 2¹⁰ byte = 1,024 byte
1 MiB = 2²⁰ byte = 1,048,576 byte
1 GiB = 2³⁰ byte ≈ 1.07 GB
1 TiB = 2⁴⁰ byte ≈ 1.10 TB

Primi 16 Numeri in Tutte le Basi
Dec Bin Oct Hex
0 0000 0 0
1 0001 1 1
2 0010 2 2
3 0011 3 3
4 0100 4 4
5 0101 5 5
6 0110 6 6
7 0111 7 7
8 1000 10 8
9 1001 11 9
10 1010 12 A
11 1011 13 B
12 1100 14 C
13 1101 15 D
14 1110 16 E
15 1111 17 F
PUNTI CHIAVE DELLA LEZIONE
✓ I computer usano il sistema binario (base 2) internamente
✓ Ottale (base 8) e esadecimale (base 16) semplificano la lettura del binario

✓ Con n bit si rappresentano 2ⁿ numeri diversi
✓ Unsigned: da 0 a 2ⁿ-1
✓ Signed (complemento a 2): da -2ⁿ⁻¹ a 2ⁿ⁻¹-1
✓ Il complemento a 2 è lo standard per i numeri negativi
✓ Overflow = risultato troppo grande per il numero di bit
✓ MSB = Most Significant Bit = bit del segno in complemento a 2
✓ Esadecimale è fondamentale in programmazione (indirizzi, colori, debug)
PREPARAZIONE PER LA PROSSIMA
LEZIONE
Nella prossima lezione studieremo:
Numeri decimali in binario (virgola fissa e mobile)
Standard IEEE 754 (floating-point)
Rappresentazione dei caratteri: ASCII
Charset estesi: Unicode e UTF-8
Differenza tra numero e carattere
Porta con te:
Esercizi homework completati
Calcolatrice scientifica
Tabelle di conversione create negli esercizi
Domande su complemento a 2 o conversioni
GLOSSARIO TECNICO
Bit: Cifra binaria (0 o 1), Binary Digit
Byte: 8 bit, unità base di memoria
Nibble: 4 bit, mezza byte
Word: Parola, dipende dall’architettura (16/32/64 bit)
MSB: Most Significant Bit, bit più significativo (a sinistra)
LSB: Least Significant Bit, bit meno significativo (a destra)
Base/Radix: Numero di cifre in un sistema posizionale
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

Complemento a 2: Metodo standard per rappresentare negativi
Overflow: Risultato troppo grande per essere rappresentato
Underflow: Risultato troppo piccolo (negativo) per essere rappresentato
Signed: Con segno (positivo/negativo)
Unsigned: Senza segno (solo positivi)
Range: Intervallo di valori rappresentabili
Ottimo lavoro! Ora sai come i computer “pensano” internamente! 🎯
Nella prossima lezione vedremo come vengono rappresentati numeri con virgola e
testo.izio 2: Conversioni con Ottale ed Esadecimale (20 min)
2.1 Converti in decimale:
75₈
Soluzione:
75₈ = 7×8¹ + 5×8⁰
    = 7×8 + 5×1
    = 56 + 5
    = 61₁₀
2F₁₆
Soluzione:
2F₁₆ = 2×16¹ + F×16⁰
     = 2×16 + 15×1
     = 32 + 15
     = 47₁₀
1A0₁₆
Soluzione:
1A0₁₆ = 1×16² + A×16¹ + 0×16⁰
      = 1×256 + 10×16 + 0
• 
• 
• 
• 
• 
• 
1. 
1. 
1. 

      = 256 + 160
      = 416₁₀
2.2 Converti 11010110₂ in ottale ed esadecimale:
Soluzione Ottale:
Raggruppa da destra in gruppi di 3:
011 010 110
 3   2   6
11010110₂ = 326₈
Soluzione Esadecimale:
Raggruppa in gruppi di 4:
1101 0110
 D    6
11010110₂ = D6₁₆
2.3 Converti 3E8₁₆ in binario:
Soluzione:
3     E     8
0011  1110  1000
3E8₁₆ = 001111101000₂
Eserc


---

# lezione4 decimali char

**File:** `lezione4 decimali char.pdf`
**Tipo:** `.pdf`
**Dimensione:** 191.1 KB
**Ultima modifica:** 02/07/2026 09:24

---

LEZIONE 4 - Numeri Decimali in
Binario e Rappresentazione Caratteri
Durata: 4 ore | Teoria: 2h | Esercizi: 2h
PARTE TEORICA (2 ore)
4.1 Rappresentazione dei Numeri con Virgola (30 min)
Finora abbiamo visto solo numeri interi. Ma come rappresentare numeri con la virgola
(es. 3.14, -0.5, 123.456)?
Virgola Fissa vs Virgola Mobile
Due approcci principali:
Fixed Point (Virgola Fissa): la posizione della virgola è predefinita
Floating Point (Virgola Mobile): la virgola può “galleggiare” - maggiore flessibilità
4.2 Virgola Fissa (Fixed Point) (25 min)
Concetto Base
Nella virgola fissa, si decide a priori quanti bit dedicare alla parte intera e quanti alla
parte decimale.
Esempio: Formato 8.8 (8 bit per parte intera, 8 bit per parte decimale)
Totale: 16 bit
┌─────────────┬─────────────┐
│  Parte      │   Parte     │
│  Intera     │  Decimale   │
1. 
2. 

│  8 bit      │   8 bit     │
└─────────────┴─────────────┘
Posizioni Decimali in Binario
Come nel sistema decimale, le posizioni dopo la virgola hanno pesi negativi:
Sistema Decimale:
123.45 = 1×10² + 2×10¹ + 3×10⁰ + 4×10⁻¹ + 5×10⁻²
       = 100  + 20   + 3    + 0.4   + 0.05
Sistema Binario:
Posizioni:  2²  2¹  2⁰ . 2⁻¹ 2⁻² 2⁻³ 2⁻⁴
Pesi:       4   2   1  . 0.5 0.25 0.125 0.0625
Tabella Potenze Negative di 2
Esponente Potenza Valore Decimale Frazione
2⁻¹ 1/2 0.5 1/2
2⁻² 1/4 0.25 1/4
2⁻³ 1/8 0.125 1/8
2⁻⁴ 1/16 0.0625 1/16
2⁻⁵ 1/32 0.03125 1/32
2⁻⁶ 1/64 0.015625 1/64
2⁻⁷ 1/128 0.0078125 1/128
2⁻⁸ 1/256 0.00390625 1/256

Conversione Decimale → Binario (Parte Frazionaria)
Metodo delle Moltiplicazioni Successive:
Moltiplica la parte decimale per 2
Prendi la parte intera del risultato (0 o 1)
Usa solo la parte decimale per la moltiplicazione successiva
Ripeti finché la parte decimale diventa 0 o raggiungi il numero di bit desiderato
Leggi i bit dall’alto verso il basso (ordine di generazione)
Esempio 1: Convertire 0.75₁₀ in binario
0.75 × 2 = 1.50  → bit 1, continua con 0.50
0.50 × 2 = 1.00  → bit 1, continua con 0.00
0.00           → STOP
Risultato: 0.75₁₀ = 0.11₂
Verifica: 0.11₂ = 1×2⁻¹ + 1×2⁻² = 0.5 + 0.25 = 0.75 ✓
Esempio 2: Convertire 0.625₁₀ in binario
0.625 × 2 = 1.25  → bit 1, continua con 0.25
0.25  × 2 = 0.50  → bit 0, continua con 0.50
0.50  × 2 = 1.00  → bit 1, continua con 0.00
0.00            → STOP
Risultato: 0.625₁₀ = 0.101₂
Verifica: 0.101₂ = 1×0.5 + 0×0.25 + 1×0.125 = 0.5 + 0.125 = 0.625 ✓
Esempio 3: Convertire 0.1₁₀ in binario (PROBLEMA!)
0.1 × 2 = 0.2  → bit 0, continua con 0.2
0.2 × 2 = 0.4  → bit 0, continua con 0.4
0.4 × 2 = 0.8  → bit 0, continua con 0.8
0.8 × 2 = 1.6  → bit 1, continua con 0.6
1. 
2. 
3. 
4. 
5. 

0.6 × 2 = 1.2  → bit 1, continua con 0.2
0.2 × 2 = 0.4  → bit 0, continua con 0.4  (CICLO!)
...
Risultato: 0.1₁₀ = 0.0001100110011... (periodico!)
IMPORTANTE: Non tutti i numeri decimali hanno una rappresentazione binaria finita!
0.5, 0.25, 0.125, 0.75, 0.625 → rappresentazione finita
0.1, 0.2, 0.3, 0.6, 0.7 → rappresentazione periodica infinita
Questo causa errori di arrotondamento nei calcoli con virgola mobile!
Conversione Binario → Decimale (Numeri con Virgola)
Metodo: Somma dei bit moltiplicati per i loro pesi (potenze negative di 2)
Esempio 1: Convertire 101.011₂ in decimale
  1   0   1 . 0   1   1
  ↓   ↓   ↓   ↓   ↓   ↓
  4   2   1   0.5 0.25 0.125
Calcolo:
= 1×4 + 0×2 + 1×1 + 0×0.5 + 1×0.25 + 1×0.125
= 4 + 0 + 1 + 0 + 0.25 + 0.125
= 5.375₁₀
Esempio 2: Convertire 11.11₂ in decimale
  1   1 . 1   1
  ↓   ↓   ↓   ↓
  2   1   0.5 0.25
= 1×2 + 1×1 + 1×0.5 + 1×0.25
= 2 + 1 + 0.5 + 0.25
= 3.75₁₀
• 
• 

Conversione Numero Completo (Parte Intera + Decimale)
Esempio: Convertire 13.625₁₀ in binario
Passo 1 - Parte intera (13):
13 ÷ 2 = 6  resto 1  ←┐
 6 ÷ 2 = 3  resto 0   │
 3 ÷ 2 = 1  resto 1   │
 1 ÷ 2 = 0  resto 1  ←┘
Parte intera: 1101₂
Passo 2 - Parte decimale (0.625):
0.625 × 2 = 1.25  → bit 1
0.25  × 2 = 0.50  → bit 0
0.50  × 2 = 1.00  → bit 1
Parte decimale: .101₂
Risultato: 13.625₁₀ = 1101.101₂
Verifica:
1101.101₂ = 8 + 4 + 0 + 1 + 0.5 + 0 + 0.125
          = 13 + 0.625
          = 13.625₁₀ ✓
Limitazioni della Virgola Fissa
Vantaggi:
Veloce
Prevedibile
Semplice da implementare
• 
• 
• 

Svantaggi:
Range limitato
Precisione fissa (non può rappresentare sia numeri molto grandi che molto piccoli)
Spreco di bit se i numeri sono molto diversi tra loro
Esempio con formato 8.8:
Range: da 0.00390625 a 255.99609375
Precisione: 1/256 ≈ 0.004
Non può rappresentare:
- 1000.5 (troppo grande)
- 0.0001 (troppo piccolo)
4.3 Virgola Mobile (Floating Point) (35 min)
Notazione Scientifica
Prima di capire il floating point, ricordiamo la notazione scientifica:
Formato: ±mantissa × 10^esponente
Esempi:
1,234,000 = 1.234 × 10⁶
0.000056 = 5.6 × 10⁻⁵
-299.8 = -2.998 × 10²
Il floating point binario usa lo stesso concetto!
Standard IEEE 754
Lo standard IEEE 754 (1985) definisce come rappresentare i numeri in virgola mobile
nei computer. È universalmente adottato.
Due formati principali:
• 
• 
• 

1. Singola Precisione (32 bit) - float in C
┌──┬─────────────┬──────────────────────────┐
│S │  Esponente  │       Mantissa           │
│  │   8 bit     │        23 bit            │
└──┴─────────────┴──────────────────────────┘
 1      8              23           = 32 bit totali
2. Doppia Precisione (64 bit) - double in C
┌──┬─────────────┬──────────────────────────────────
────────────────┐
│S │  Esponente  │               Mantissa                           │
│  │   11 bit    │              52 bit                              │
└──┴─────────────┴──────────────────────────────────
────────────────┘
 1     11                    52                  = 64 bit totali
Componenti di un Numero Floating Point
1. SEGNO (Sign - S): 1 bit
0 = positivo
1 = negativo
2. ESPONENTE (Exponent - E): 8 bit (float) o 11 bit (double)
Rappresentato con Eccesso-127 (float) o Eccesso-1023 (double)
Permette esponenti positivi e negativi
3. MANTISSA (Significand/Fraction - M): 23 bit (float) o 52 bit (double)
Rappresenta le cifre significative del numero
Bit nascosto (hidden bit): il primo bit (sempre 1) non viene memorizzato!
Formato del Numero
Formula generale:
• 
• 
• 
• 
• 
• 

Valore = (-1)^S × (1.M) × 2^(E-bias)
Dove:
- S = bit di segno
- M = mantissa (bits frazionari)
- E = esponente (come memorizzato)
- bias = 127 (float) o 1023 (double)
Il “1.” nascosto: In formato normalizzato, la mantissa è sempre tra 1.0 e 2.0, quindi il
“1” iniziale non viene memorizzato (guadagno di 1 bit di precisione!)
Esempio Completo: Float 32 bit
Rappresentare 12.375₁₀ in IEEE 754 singola precisione
Passo 1: Converti in binario
Parte intera: 12₁₀ = 1100₂
Parte decimale: 0.375₁₀ = 0.011₂
12.375₁₀ = 1100.011₂
Passo 2: Normalizza in forma 1.xxx × 2^n
1100.011₂ = 1.100011 × 2³
(Sposta la virgola a sinistra di 3 posizioni)
Passo 3: Determina i componenti
Segno:
12.375 è positivo → S = 0
Esponente:

Esponente reale: 3
Esponente con bias: 3 + 127 = 130₁₀ = 10000010₂
Mantissa:
Parte dopo "1.": 100011
Completata a 23 bit: 10001100000000000000000
(aggiungi zeri a destra)
Passo 4: Assembla il numero
┌─┬────────┬───────────────────────┐
│0│10000010│10001100000000000000000│
└─┴────────┴───────────────────────┘
 S    E              M
In esadecimale: 0x41460000
Verifica:
S = 0 (positivo)
E = 10000010₂ = 130₁₀
Esponente reale = 130 - 127 = 3
Mantissa = 1.100011₂ = 1 + 0.5 + 0 + 0 + 0.0625 + 0.03125
         = 1.59375
Valore = +1 × 1.59375 × 2³
       = 1.59375 × 8
       = 12.75... ERRORE!
Ops! Ho fatto un errore. Correggiamo:
0.375 in binario:

0.375 × 2 = 0.75  → 0
0.75  × 2 = 1.5   → 1
0.5   × 2 = 1.0   → 1
0.375₁₀ = 0.011₂ ✓
Quindi 12.375₁₀ = 1100.011₂ = 1.100011 × 2³ ✓
Mantissa dopo “1.”: 100011… (solo 6 bit significativi)
Verifica:
1.100011₂ = 1 + 1×2⁻¹ + 0×2⁻² + 0×2⁻³ + 0×2⁻⁴ + 1×2⁻⁵ + 1×2⁻⁶
          = 1 + 0.5 + 0.03125 + 0.015625
          = 1.546875
Valore = 1.546875 × 2³ = 1.546875 × 8 = 12.375 ✓
Casi Speciali in IEEE 754
1. Zero
Esponente = 0
Mantissa = 0
Nota: esistono +0 e -0 (differiscono solo nel bit di segno)
2. Infinito
Esponente = tutti 1 (255 per float)
Mantissa = 0
+∞: S=0, E=11111111, M=0
-∞: S=1, E=11111111, M=0

3. NaN (Not a Number)
Esponente = tutti 1 (255 per float)
Mantissa ≠ 0
Esempi di operazioni che producono NaN:
- 0 / 0
- ∞ - ∞
- √(-1)
4. Numeri Denormalizzati (Subnormal)
Esponente = 0
Mantissa ≠ 0
Usati per numeri molto piccoli, vicini a zero
Formula: (-1)^S × (0.M) × 2^(-126)
Range e Precisione
Float (32 bit):
Range: ±1.18 × 10⁻³⁸ a ±3.4 × 10³⁸
Precisione: circa 7 cifre decimali
Epsilon (differenza minima): ~1.19 × 10⁻⁷
Double (64 bit):
Range: ±2.23 × 10⁻³⁰⁸ a ±1.8 × 10³⁰⁸
Precisione: circa 15-16 cifre decimali
Epsilon: ~2.22 × 10⁻¹⁶
Problemi del Floating Point
1. Errori di Arrotondamento

2. Perdita di Precisione con Numeri Molto Diversi
3. Confronti Pericolosi
4. Operazioni Non Associative
4.4 Caratteri e Codifica ASCII (30 min)
Cos’è un Carattere?
Un carattere è un simbolo (lettera, numero, punteggiatura, simbolo speciale) che
rappresentiamo con un codice numerico.
float a =0.1f;
float b =0.2f;
float c = a + b;
// c potrebbe NON essere esattamente 0.3!
// c ≈ 0.30000001 (esempio)
float grande =1000000.0f;
float piccolo =0.000001f;
float somma = grande + piccolo;
// somma == grande (piccolo viene "perso")
// MALE!
if(x ==0.3){...}
// BENE!
if(fabs(x -0.3)<0.00001){...}
(a + b)+ c ≠ a +(b + c) // Possibile!

IMPORTANTE: Il numero 5 e il carattere ‘5’ sono diversi!
Numero 5: valore numerico, su cui fare calcoli
Carattere ‘5’: simbolo da visualizzare, codice 53 in ASCII
ASCII - American Standard Code for Information Interchange
Storia: Sviluppato negli anni ’60 per standardizzare la rappresentazione dei caratteri.
Caratteristiche:
Usa 7 bit (128 caratteri: 0-127)
Spesso memorizzato in 8 bit (1 byte), con l’8° bit inutilizzato o usato per parità
Standard universale per caratteri inglesi di base
Struttura della Tabella ASCII
Divisione in gruppi:
0-31: Caratteri di Controllo (non stampabili)
0   = NUL (Null)
7   = BEL (Bell/campanello)
8   = BS  (Backspace)
9   = TAB (Tab orizzontale)
10  = LF  (Line Feed / new line)
13  = CR  (Carriage Return)
27  = ESC (Escape)
32-47: Spazio e Simboli
32  = spazio
33  = !
...
47  = /
48-57: Cifre Numeriche
• 
• 
• 
• 
• 

48  = '0'
49  = '1'
...
57  = '9'
58-64: Simboli
58  = :
...
64  = @
65-90: Lettere Maiuscole
65  = 'A'
66  = 'B'
...
90  = 'Z'
91-96: Simboli
91  = [
...
96  = `
97-122: Lettere Minuscole
97  = 'a'
98  = 'b'
...
122 = 'z'
123-126: Simboli

123 = {
...
126 = ~
127: DEL (Delete)
Tabella ASCII Completa (Caratteri Principali)
Dec Hex Binario Char Descrizione
0 00 00000000 NUL Null
9 09 00001001 TAB Tab
10 0A 00001010 LF Line Feed
13 0D 00001101 CR Carriage Return
32 20 00100000 ’ ’ Spazio
48 30 00110000 ‘0’ Zero
49 31 00110001 ‘1’ Uno
57 39 00111001 ‘9’ Nove
65 41 01000001 ‘A’ A maiuscola
66 42 01000010 ‘B’ B maiuscola
90 5A 01011010 ‘Z’ Z maiuscola
97 61 01100001 ‘a’ a minuscola
98 62 01100010 ‘b’ b minuscola
122 7A 01111010 ‘z’ z minuscola
Relazioni Utili in ASCII
1. Maiuscole ↔ Minuscole:

Differenza = 32 (0x20)
'A' (65) + 32 = 'a' (97)
'Z' (90) + 32 = 'z' (122)
Per convertire:
maiuscola → minuscola: aggiungi 32 (o OR con 0x20)
minuscola → maiuscola: sottrai 32 (o AND con ~0x20)
2. Carattere Cifra → Valore Numerico:
'0' = 48
'1' = 49
...
'9' = 57
Per convertire:
Carattere → numero: sottrai 48 (o '0')
'5' - '0' = 53 - 48 = 5
Numero → carattere: aggiungi 48 (o '0')
5 + '0' = 5 + 48 = 53 = '5'
3. Bit di Differenza Maiuscola/Minuscola:
Binario:
'A' = 01000001
'a' = 01100001
       ↑
Solo il 6° bit (da destra, partendo da 0) cambia!
Bit 5 (0x20) = differenza maiuscola/minuscola

Codifica di Stringhe
Una stringa è una sequenza di caratteri.
In C, le stringhe sono array di caratteri terminati con \0 (NULL, codice 0):
Lunghezza: 5 caratteri visibili + 1 terminatore = 6 byte totali
Limitazioni di ASCII
Problema: ASCII supporta solo caratteri inglesi di base!
Non può rappresentare:
Lettere accentate (à, è, ñ, ü)
Alfabeti non latini (greco, cirillico, arabo, cinese, giapponese, ecc.)
Simboli matematici avanzati
Emoji 😀
Soluzione: Charset estesi!
4.5 Charset Estesi: Unicode e UTF-8 (30 min)
ASCII Esteso (8 bit)
Extended ASCII: Usa tutti gli 8 bit (256 caratteri: 0-255)
Codici 128-255 usati per:
Lettere accentate
Simboli matematici
"HELLO" in memoria:
┌───┬───┬───┬───┬───┬───┐
│ H │ E │ L │ L │ O │\0 │
├───┼───┼───┼───┼───┼───┤
│72 │69 │76 │76 │79 │ 0 │  (codici ASCII)
└───┴───┴───┴───┴───┴───┘
0 1 2 3 4 5 (indici)
• 
• 
• 
• 
• 
• 

Box drawing characters
Simboli valuta (€, £, ¥)
Problema: Molti standard incompatibili!
ISO 8859-1 (Latin-1): Europa occidentale
Windows-1252: Variante Microsoft
ISO 8859-5: Cirillico
…
Non esiste un modo universale per rappresentare tutti i linguaggi!
Unicode - La Soluzione Universale
Unicode è uno standard che assegna un codice univoco (chiamato code point) a ogni
carattere di ogni lingua del mondo.
Versione attuale: Unicode 15.0 (2022)
Oltre 149,000 caratteri
Supporta più di 150 scritture
Include emoji, simboli matematici, caratteri storici
Formato Code Point: U+XXXX (esadecimale)
Esempi:
U+0041 = 'A'
U+00E9 = 'é'
U+03B1 = 'α' (alfa greco)
U+4E2D = '中' (cinese)
U+1F600 = '😀' (emoji)
Unicode NON è una codifica! È solo un’assegnazione di numeri ai caratteri.
Per memorizzare Unicode serve una codifica: UTF-8, UTF-16, UTF-32.
UTF-8 - Codifica Universale
UTF-8 (Unicode Transformation Format - 8 bit) è la codifica Unicode più usata su
Internet.
• 
• 
• 
• 
• 
• 
• 
• 
• 

Caratteristiche:
Lunghezza variabile: da 1 a 4 byte per carattere
Compatibile con ASCII: primi 128 caratteri = ASCII
Auto-sincronizzante: si capisce dove inizia un carattere
Efficiente: caratteri comuni usano meno byte
Schema di Codifica UTF-8
1 byte (0-127): caratteri ASCII
0xxxxxxx
Esempio: 'A' = U+0041 = 0x41 = 01000001
2 byte (128-2047): alfabeti latini estesi, greco, cirillico, arabo, ebraico
110xxxxx 10xxxxxx
Esempio: 'é' = U+00E9 = 11000011 10101001 = 0xC3 0xA9
3 byte (2048-65535): la maggior parte degli altri alfabeti (cinese, giapponese, coreano)
1110xxxx 10xxxxxx 10xxxxxx
Esempio: '中' = U+4E2D = 11100100 10111000 10101101
4 byte (65536-1114111): emoji, caratteri rari, simboli matematici avanzati
11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Esempio: '😀' = U+1F600 = 11110000 10011111 10011000 10000000
Esempio: Codifica “Hello, 世界!” in UTF-8
Carattere  | Code Point | UTF-8 (hex)     | Byte
-----------|------------|-----------------|------
'H'        | U+0048     | 48              | 1
'e'        | U+0065     | 65              | 1
• 
• 
• 
• 

'l'        | U+006C     | 6C              | 1
'l'        | U+006C     | 6C              | 1
'o'        | U+006F     | 6F              | 1
','        | U+002C     | 2C              | 1
' '        | U+0020     | 20              | 1
'世'       | U+4E16     | E4 B8 96        | 3
'界'       | U+754C     | E7 95 8C        | 3
'!'        | U+0021     | 21              | 1
Totale: 14 byte
UTF-16 e UTF-32
UTF-16:
Usa 2 o 4 byte per carattere
Caratteri comuni (BMP): 2 byte
Caratteri rari: 4 byte (coppia surrogata)
Usato internamente da Windows, Java, JavaScript
UTF-32:
Usa sempre 4 byte per carattere
Semplice ma spreca spazio
Raramente usato
Confronto Codifiche
Codifica Byte per
char Range Pro Contro
ASCII 1 128 car. Semplice, veloce Solo inglese
ASCII
Esteso 1 256 car. Compatto Incompatibilità
UTF-8 1-4 1.1M+
car.
Compatibile ASCII,
efficiente
Lunghezza
variabile
• 
• 
• 
• 
• 
• 
• 

Codifica Byte per
char Range Pro Contro
UTF-16 2-4 1.1M+
car.
Efficiente per lingue
asiatiche
Non compatibile
ASCII
UTF-32 4 1.1M+
car. Accesso diretto Spreco di spazio
BOM (Byte Order Mark)
BOM è una sequenza speciale all’inizio di un file per indicare:
Quale codifica UTF viene usata
L’ordine dei byte (big-endian o little-endian per UTF-16/32)
UTF-8: EF BB BF
UTF-16 BE: FE FF
UTF-16 LE: FF FE
UTF-32 BE: 00 00 FE FF
UTF-32 LE: FF FE 00 00
4.6 Differenza tra Numero e Carattere (10 min)
Questa è una distinzione fondamentale in programmazione!
Numero vs Carattere
Il numero 5:
Tipo: int
Valore binario: 00000101 (se 8 bit)
Uso: calcoli matematici (5 + 3 = 8)
In memoria: rappresentazione binaria diretta
Il carattere ‘5’:
• 
• 

Tipo: char
Codice ASCII: 53 (0x35)
Valore binario: 00110101
Uso: visualizzazione, testo
In memoria: codice ASCII del simbolo '5'
Esempi Pratici
In C:
Operazioni:
Array di Caratteri vs Array di Numeri
Stringa “123”:
int numero =5; // Valore numerico 5
char carattere ='5'; // Codice ASCII 53
printf("%d\n", numero); // Stampa: 5
printf("%d\n", carattere); // Stampa: 53 (codice ASCII)
printf("%c\n", carattere); // Stampa: 5 (il simbolo)
int a =5;
int b =3;
int somma = a + b; // somma = 8 ✓
char c1 ='5'; // ASCII 53
char c2 ='3'; // ASCII 51
int somma2 = c1 + c2; // somma2 = 104 (53+51) ✗ NON è 8!
// Per convertire:
int valore1 = c1 -'0'; // valore1 = 53 - 48 = 5 ✓
int valore2 = c2 -'0'; // valore2 = 51 - 48 = 3 ✓
int somma3 = valore1 + valore2; // somma3 = 8 ✓

Array di numeri [1, 2, 3]:
Conversioni Comuni
Carattere cifra → Numero:
Numero → Carattere cifra:
char stringa[]="123";
In memoria:
┌────┬────┬────┬────┐
│ 49 │ 50 │ 51 │ 0  │  (codici ASCII + terminatore)
└────┴────┴────┴────┘
'1' '2' '3' '\0'
Lunghezza: 4 byte
int numeri[]={1, 2, 3};
In memoria (assumendo int=4 byte):
┌──────────┬──────────┬──────────┐
│    1     │    2     │    3     │  (valori interi)
└──────────┴──────────┴──────────┘
0x000000010x000000020x00000003
Lunghezza: 12 byte
char c ='7';
int n = c -'0'; // n = 7
// Oppure
int n = c -48; // n = 7

Stringa → Numero:
Numero → Stringa:
int n =7;
char c = n +'0'; // c = '7'
// Oppure
char c = n +48; // c = '7'
char str[]="123";
int num = atoi(str); // num = 123 (funzione stdlib.h)
// Manualmente:
int num =0;
for(int i =0; str[i]!='\0'; i++){
    num = num *10+(str[i]-'0');
}
// num = 0*10 + 1 = 1
// num = 1*10 + 2 = 12
// num = 12*10 + 3 = 123
int num =123;
char str[20];
sprintf(str, "%d", num); // str = "123"
// O usa itoa() se disponibile

PARTE PRATICA (2 ore)
ESERCIZI GUIDATI
Esercizio 1: Numeri con Virgola - Conversioni (25 min)
1.1 Converti in decimale i seguenti numeri binari con virgola:
110.101₂
Soluzione:
  1   1   0 . 1   0   1
  ↓   ↓   ↓   ↓   ↓   ↓
  4   2   1  0.5 0.25 0.125
= 1×4 + 1×2 + 0×1 + 1×0.5 + 0×0.25 + 1×0.125
= 4 + 2 + 0 + 0.5 + 0 + 0.125
= 6.625₁₀
1.001₂
Soluzione:
  1 . 0   0   1
  ↓   ↓   ↓   ↓
  1  0.5 0.25 0.125
= 1×1 + 0×0.5 + 0×0.25 + 1×0.125
= 1 + 0.125
= 1.125₁₀
101.11₂
Soluzione:
  1   0   1 . 1   1
  ↓   ↓   ↓   ↓   ↓
1. 
1. 
1. 

  4   2   1  0.5 0.25
= 1×4 + 0×2 + 1×1 + 1×0.5 + 1×0.25
= 4 + 1 + 0.5 + 0.25
= 5.75₁₀
1.2 Converti in binario (con massimo 8 bit decimali):
3.5₁₀
Soluzione:
Parte intera: 3₁₀ = 11₂
Parte decimale: 0.5
0.5 × 2 = 1.0 → bit 1, STOP
Risultato: 3.5₁₀ = 11.1₂
Verifica: 11.1₂ = 2 + 1 + 0.5 = 3.5 ✓
5.25₁₀
Soluzione:
Parte intera: 5₁₀ = 101₂
Parte decimale: 0.25
0.25 × 2 = 0.5 → bit 0
0.5  × 2 = 1.0 → bit 1, STOP
Risultato: 5.25₁₀ = 101.01₂
Verifica: 101.01₂ = 4 + 1 + 0.25 = 5.25 ✓
7.875₁₀
1. 
1. 
1. 

Soluzione:
Parte intera: 7₁₀ = 111₂
Parte decimale: 0.875
0.875 × 2 = 1.75 → bit 1
0.75  × 2 = 1.5  → bit 1
0.5   × 2 = 1.0  → bit 1, STOP
Risultato: 7.875₁₀ = 111.111₂
Verifica: 111.111₂ = 4 + 2 + 1 + 0.5 + 0.25 + 0.125 = 7.875 ✓
0.1₁₀ (mostra il problema!)
Soluzione:
0.1 × 2 = 0.2 → bit 0
0.2 × 2 = 0.4 → bit 0
0.4 × 2 = 0.8 → bit 0
0.8 × 2 = 1.6 → bit 1
0.6 × 2 = 1.2 → bit 1
0.2 × 2 = 0.4 → bit 0 (si ripete!)
0.4 × 2 = 0.8 → bit 0
0.8 × 2 = 1.6 → bit 1
Risultato: 0.1₁₀ = 0.00011001100110011... (periodico!)
Con 8 bit: 0.00011001₂
Valore approssimato: 0.09765625₁₀
Errore: 0.1 - 0.09765625 = 0.00234375
1.3 Dimostra che 0.3 ≠ 0.1 + 0.2 in binario (con 8 bit decimali):
Soluzione:
0.1₁₀ ≈ 0.00011001₂ (troncato a 8 bit)
1. 

0.2₁₀ ≈ 0.00110011₂ (troncato a 8 bit)
Somma in binario:
    0.00011001
  + 0.00110011
  ------------
    0.01001100₂
Converti in decimale:
0.01001100₂ = 0.25 + 0.0625 + 0.015625 = 0.328125₁₀
Ma 0.3 in binario (8 bit):
0.3 × 2 = 0.6 → 0
0.6 × 2 = 1.2 → 1
0.2 × 2 = 0.4 → 0
0.4 × 2 = 0.8 → 0
0.8 × 2 = 1.6 → 1
0.6 × 2 = 1.2 → 1 (ciclo)
...
0.3₁₀ ≈ 0.01001100₂ (troncato)
Ma attendevi 0.3, ottieni 0.328125!
Ecco perché 0.1 + 0.2 ≠ 0.3 nei computer!
Esercizio 2: IEEE 754 Float (30 min)
2.1 Analizza il seguente numero IEEE 754 (32 bit):
0 10000010 10100000000000000000000
Soluzione:
Segno: 0 → positivo
Esponente: 10000010₂ = 130₁₀

Esponente reale: 130 - 127 = 3
Mantissa: 10100000000000000000000
Con bit nascosto: 1.101₂
= 1 + 1×2⁻¹ + 0×2⁻² + 1×2⁻³
= 1 + 0.5 + 0.125
= 1.625
Valore: (+1) × 1.625 × 2³
      = 1.625 × 8
      = 13.0₁₀
2.2 Rappresenta -6.75₁₀ in IEEE 754 (32 bit):
Soluzione:
Passo 1: Converti in binario
6₁₀ = 110₂
0.75₁₀: 
0.75 × 2 = 1.5 → 1
0.5  × 2 = 1.0 → 1
6.75₁₀ = 110.11₂
Passo 2: Normalizza
110.11₂ = 1.1011 × 2²
Passo 3: Componenti
Segno: negativo → S = 1
Esponente: 2 + 127 = 129₁₀ = 10000001₂
Mantissa: 1011 (dopo "1.")
Completa a 23 bit: 10110000000000000000000
Passo 4: Risultato
┌─┬────────┬───────────────────────┐
│1│10000001│10110000000000000000000│
└─┴────────┴───────────────────────┘

In esadecimale: 0xC0D80000
2.3 Identifica questi valori speciali IEEE 754:
0 11111111 00000000000000000000000
Soluzione:
S = 0
E = 11111111 (tutti 1)
M = 0
Valore: +∞ (infinito positivo)
1 11111111 00000000000000000000000
Soluzione:
S = 1
E = 11111111 (tutti 1)
M = 0
Valore: -∞ (infinito negativo)
0 11111111 10000000000000000000000
Soluzione:
S = 0
E = 11111111 (tutti 1)
M ≠ 0
Valore: NaN (Not a Number)
0 00000000 00000000000000000000000
1. 
1. 
1. 
1. 

Soluzione:
S = 0
E = 0
M = 0
Valore: +0 (zero positivo)
Esercizio 3: ASCII e Caratteri (25 min)
3.1 Converti le seguenti stringhe in codici ASCII (decimali):
“ABC”
Soluzione:
'A' = 65
'B' = 66
'C' = 67
Sequenza: 65 66 67
“Hello”
Soluzione:
'H' = 72
'e' = 101
'l' = 108
'l' = 108
'o' = 111
Sequenza: 72 101 108 108 111
“123”
1. 
1. 
1. 

Soluzione:
'1' = 49
'2' = 50
'3' = 51
Sequenza: 49 50 51
ATTENZIONE: Non è il numero 123!
3.2 Converti i seguenti codici ASCII in caratteri:
65 66 67
Soluzione: "ABC"
72 105 33
Soluzione:
72 = 'H'
105 = 'i'
33 = '!'
Stringa: "Hi!"
48 49 50
Soluzione:
48 = '0'
49 = '1'
50 = '2'
Stringa: "012"
1. 
1. 
1. 

3.3 Conversione maiuscole/minuscole:
Converti ‘A’ in ‘a’
Soluzione:
'A' = 65
Differenza = 32
'a' = 65 + 32 = 97 ✓
In binario:
'A' = 01000001
'a' = 01100001
       ↑
Solo il bit 5 cambia!
Metodo veloce: 'A' | 0x20 = 'a'
Converti ‘z’ in ‘Z’
Soluzione:
'z' = 122
Differenza = -32
'Z' = 122 - 32 = 90 ✓
Metodo veloce: 'z' & ~0x20 = 'Z'
3.4 Conversione carattere ↔ numero:
Converti ‘7’ in numero 7
Soluzione:
'7' = 55 (ASCII)
'0' = 48 (ASCII)
1. 
1. 
1. 

numero = '7' - '0' = 55 - 48 = 7 ✓
Converti numero 9 in carattere ‘9’
Soluzione:
numero = 9
'0' = 48
carattere = 9 + '0' = 9 + 48 = 57 = '9' ✓
Converti la stringa “42” nel numero 42
Soluzione:
'4' = 52, valore = 52 - 48 = 4
'2' = 50, valore = 50 - 48 = 2
numero = 4 × 10 + 2 = 42 ✓
Esercizio 4: UTF-8 (20 min)
4.1 Determina quanti byte servono per codificare in UTF-8:
‘A’ (U+0041)
Soluzione:
U+0041 = 65₁₀ < 128
Range 0-127: 1 byte
Codifica: 0x41 = 01000001
‘è’ (U+00E8)
Soluzione:
U+00E8 = 232₁₀
1. 
1. 
1. 
1. 

Range 128-2047: 2 byte
Formato: 110xxxxx 10xxxxxx
Calcolo:
232₁₀ = 11101000₂
Dividi in bit:
11 101000
↓↓ ↓↓↓↓↓↓
110(00011) 10(101000)
Codifica: 0xC3 0xA8 = 11000011 10101000
‘€’ (U+20AC)
Soluzione:
U+20AC = 8364₁₀
Range 2048-65535: 3 byte
Formato: 1110xxxx 10xxxxxx 10xxxxxx
8364₁₀ = 0010000010101100₂
       = 0010 000010 101100
1110(0010) 10(000010) 10(101100)
Codifica: 0xE2 0x82 0xAC = 11100010 10000010 10101100
‘😀’ (U+1F600)
Soluzione:
U+1F600 = 128512₁₀
Range 65536-1114111: 4 byte
Formato: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
1. 
1. 

128512₁₀ = 11111011000000000₂
         = 000 011111 011000 000000
11110(000) 10(011111) 10(011000) 10(000000)
Codifica: 0xF0 0x9F 0x98 0x80
4.2 Calcola la dimensione in byte della stringa UTF-8:
"Hello, 世界!"
Soluzione:
'H' = U+0048 → 1 byte
'e' = U+0065 → 1 byte
'l' = U+006C → 1 byte
'l' = U+006C → 1 byte
'o' = U+006F → 1 byte
',' = U+002C → 1 byte
' ' = U+0020 → 1 byte
'世' = U+4E16 → 3 byte (CJK)
'界' = U+754C → 3 byte (CJK)
'!' = U+0021 → 1 byte
Totale: 7 + 3 + 3 + 1 = 14 byte
Caratteri visibili: 10
Nota: in UTF-16 sarebbero 20 byte (10×2)
      in UTF-32 sarebbero 40 byte (10×4)
Esercizio 5: Numero vs Carattere (20 min)
5.1 Qual è la differenza in memoria tra:

Soluzione:
int x = 5:
- Tipo: intero
- Valore: 5
- In memoria (4 byte, little-endian):
  0x00000005 = 00000000 00000000 00000000 00000101
- Uso: calcoli matematici
char c = '5':
- Tipo: carattere
- Valore ASCII: 53
- In memoria (1 byte):
  0x35 = 00110101
- Uso: rappresentazione testuale
NON sono intercambiabili!
x + 2 = 7
c + 2 = 55 (ASCII di '7'... no, sarebbe 55, che è '7'? No!)
Corretto:
(c - '0') + 2 = 5 + 2 = 7
5.2 Cosa stampa il seguente codice?
int x =5;
char c ='5';
char c ='A';
printf("%c\n", c);
printf("%d\n", c);
printf("%c\n", c +1);
printf("%d\n", c +32);

Soluzione:
char c = 'A';  // c = 65
printf("%c\n", c);      // Stampa: A (come carattere)
printf("%d\n", c);      // Stampa: 65 (come numero)
printf("%c\n", c + 1);  // Stampa: B (65+1=66='B')
printf("%d\n", c + 32); // Stampa: 97 (65+32=97, codice di 'a')
5.3 Scrivi pseudocodice per convertire una stringa di cifre in numero:
Input: “3456”
Output: 3456
Soluzione:
INIZIO
    LEGGI stringa
    numero ← 0
    PER ogni carattere c in stringa FARE
        SE c è una cifra ('0' a '9') ALLORA
            cifra ← valore_ASCII(c) - valore_ASCII('0')
            numero ← numero × 10 + cifra
        ALTRIMENTI
            ERRORE "Carattere non valido"
        FINE SE
    FINE PER
    SCRIVI numero
FINE
Esempio traccia con "3456":
Inizio: numero = 0
c='3': cifra=51-48=3, numero=0×10+3=3
c='4': cifra=52-48=4, numero=3×10+4=34
c='5': cifra=53-48=5, numero=34×10+5=345

c='6': cifra=54-48=6, numero=345×10+6=3456
Fine: numero = 3456
ESERCIZI AUTONOMI
Esercizio 6: Problemi Misti
6.1 Una temperatura viene memorizzata come float IEEE 754. Il valore in memoria è:
0 10000010 01000000000000000000000
Qual è la temperatura in gradi Celsius?
6.2 Scrivi in binario (virgola fissa 8.8):
15.75
0.5
127.99609375
6.3 Codifica la stringa “C Programming!” in:
ASCII (decimale)
ASCII (esadecimale)
UTF-8 (esadecimale)
6.4 Determina la dimensione totale in byte delle seguenti stringhe in UTF-8:
“Caffè”
“Привет” (russo: “Ciao”)
“こんにちは” (giapponese: “Ciao”)
“Hello 🌍!”
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

ESERCIZI DA SVOLGERE A CASA
Homework 1: Crea una tabella con i numeri da 0 a 1 con passo 0.125 (0, 0.125, 0.250,
…, 1.0) e converti ognuno in:
Binario (parte decimale)
IEEE 754 singola precisione (rappresentazione schematica)
Homework 2: Scrivi un algoritmo (pseudocodice o flow chart) che:
Legge una stringa contenente solo cifre
Converte la stringa nel corrispondente numero intero
Gestisce il caso di stringhe vuote o con caratteri non validi
Homework 3: Analizza il problema del confronto di float:
Perché 0.1 + 0.2 == 0.3 è falso?
Come si dovrebbe fare il confronto correttamente?
Scrivi una funzione (pseudocodice) per confrontare due float con tolleranza
Homework 4: Ricerca e documenta:
Cos’è l’ULP (Unit in the Last Place)?
Cosa significa “denormalized number” in IEEE 754?
Casi pratici dove float causa problemi (finanza, fisica, ecc.)
Homework 5: Crea un programma (pseudocodice) che:
Legge una stringa UTF-8
Conta quanti byte occupa in memoria
Conta quanti caratteri visibili contiene
Distingue tra caratteri ASCII e non-ASCII
Homework 6: Esercizio di conversione completo:
Dato il numero -25.625₁₀:
a) Convertilo in binario (parte intera e decimale)
b) Rappresentalo in virgola fissa 16.16
c) Rappresentalo in IEEE 754 (32 bit)
d) Verifica entrambe le rappresentazioni riconvertendo in decimale
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

APPROFONDIMENTI
Il Problema dello 0.1 + 0.2
Questo è uno dei problemi più famosi del floating point:
Perché succede?
0.1 in binario è periodico:
0.1₁₀ = 0.000110011001100110011...₂ (infinito)
Il computer deve troncare, quindi memorizza un’approssimazione:
0.1 ≈ 0.1000000000000000055511151231257827...
0.2 ≈ 0.2000000000000000111022302462515654...
Somma ≈ 0.3000000000000000444089209850062...
Conseguenze:
Mai usare == per confrontare float/double
Problemi nei cicli: for (float x = 0; x != 1.0; x += 0.1) → infinito!
Errori accumulati nei calcoli lunghi
Soluzioni:
Usare epsilon per confronti: fabs(a - b) < 1e-9
Librerie di precisione arbitraria (GMP, MPFR)
Aritmetica decimale per finanza (Java BigDecimal, Python Decimal)
Floating Point in Hardware
Le CPU moderne hanno unità dedicate per floating point: FPU (Floating Point Unit).
>>>0.1+0.2
0.30000000000000004
• 
• 
• 
• 
• 
• 

Ottimizzazioni:
Istruzioni SIMD: SSE, AVX (calcoli paralleli)
Fusione operazioni: FMA (Fused Multiply-Add: a×b+c in una istruzione)
Pipeline specializzate
Modalità di arrotondamento IEEE 754:
Round to nearest (default)
Round toward zero
Round toward +∞
Round toward -∞
Storia di Unicode
Timeline:
1987: Joe Becker (Xerox) propone Unicode
1991: Unicode 1.0 (7,161 caratteri)
1996: UTF-8 creato da Ken Thompson e Rob Pike
2001: UTF-8 diventa dominante sul web
2010: Emoji aggiunte a Unicode
2022: Unicode 15.0 (149,186 caratteri)
Curiosità:
Il code point più alto: U+10FFFF
Esistono blocchi riservati per uso privato
Emoji con toni della pelle usano “modifier”
Alcune emoji sono sequenze: 👨 ‍👩 ‍👧 ‍👦  = 7 code point!
Endianness nei Floating Point
Anche i float hanno problemi di endianness quando trasferiti tra sistemi!
Esempio: 12.375 in IEEE 754
Big-endian:    41 46 00 00
Little-endian: 00 00 46 41
• 
• 
• 
1. 
2. 
3. 
4. 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

Per questo esistono formati di serializzazione neutrali (JSON, Protocol Buffers).
Confronto Prestazioni: Virgola Fissa vs Mobile
Virgola Fissa:
Più veloce (operazioni intere)
Usata in DSP, embedded systems
Librerie: libfixmath
Virgola Mobile:
Più flessibile
Standard moderno
Hardware dedicato (FPU)
Benchmark tipico (milioni di operazioni/sec):
Integer:        1000
Fixed-point:    800
Float (FPU):    500
Float (software): 50
Charset Storici
EBCDIC (IBM):
Usato su mainframe IBM
Incompatibile con ASCII!
Ancora in uso in sistemi legacy
ISO 8859 (15 varianti):
ISO 8859-1 (Latin-1): Europa occidentale
ISO 8859-2 (Latin-2): Europa centrale
ISO 8859-5: Cirillico
Problema: incompatibili tra loro!
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

Windows-1252:
“ANSI” di Windows
Estensione non standard di ISO 8859-1
Aggiunge caratteri 128-159
Il Futuro: Oltre IEEE 754?
Problemi dell’IEEE 754:
Errori di arrotondamento inevitabili
NaN e infiniti complicano la semantica
Confronti non intuitivi
Alternative proposte:
Posit (John Gustafson, 2017): maggiore precisione dinamica
Unums: numeri con incertezza incorporata
Decimale binario: IEEE 754-2008 include float decimali
Nessuna ha ancora sostituito lo standard consolidato.
RIEPILOGO FORMULE E CONCETTI
Conversione Binario con Virgola → Decimale
N.M₂ = Σ(bit × 2^posizione)
Esempio: 101.11₂
= 1×2² + 0×2¹ + 1×2⁰ + 1×2⁻¹ + 1×2⁻²
= 4 + 0 + 1 + 0.5 + 0.25
= 5.75₁₀
• 
• 
• 
• 
• 
• 
• 
• 
• 

Conversione Decimale → Binario (Parte Decimale)
Moltiplica ripetutamente per 2
Prendi la parte intera (0 o 1)
Continua con la parte decimale
Leggi dall'alto verso il basso
IEEE 754 Formula
Valore = (-1)^S × (1.M) × 2^(E-bias)
Float (32 bit):
- S: 1 bit
- E: 8 bit (bias = 127)
- M: 23 bit (+ 1 bit nascosto)
- Range: ±1.18×10⁻³⁸ a ±3.4×10³⁸
Double (64 bit):
- S: 1 bit
- E: 11 bit (bias = 1023)
- M: 52 bit (+ 1 bit nascosto)
- Range: ±2.23×10⁻³⁰⁸ a ±1.8×10³⁰⁸
ASCII - Relazioni Chiave
Maiuscola ↔ Minuscola: differenza = 32 (0x20)
'A' = 65, 'a' = 97
'Z' = 90, 'z' = 122
Cifra → Numero: sottrai 48 (o '0')
'0' = 48, '9' = 57
'5' - '0' = 53 - 48 = 5

Numero → Cifra: aggiungi 48 (o '0')
5 + '0' = 5 + 48 = 53 = '5'
UTF-8 Schema
1 byte:  0xxxxxxx                    (0-127)
2 byte:  110xxxxx 10xxxxxx           (128-2047)
3 byte:  1110xxxx 10xxxxxx 10xxxxxx  (2048-65535)
4 byte:  11110xxx 10xxxxxx 10xxxxxx 10xxxxxx (65536+)
TABELLE DI RIFERIMENTO RAPIDO
Potenze di 2 (Decimali)
2⁻⁸ = 0.00390625    2⁰ = 1
2⁻⁷ = 0.0078125     2¹ = 2
2⁻⁶ = 0.015625      2² = 4
2⁻⁵ = 0.03125       2³ = 8
2⁻⁴ = 0.0625        2⁴ = 16
2⁻³ = 0.125         2⁵ = 32
2⁻² = 0.25          2⁶ = 64
2⁻¹ = 0.5           2⁷ = 128
Frazioni Binarie Comuni
Decimale | Binario  | Frazione
---------|----------|----------
0.5      | .1       | 1/2
0.25     | .01      | 1/4
0.125    | .001     | 1/8
0.75     | .11      | 3/4

0.625    | .101     | 5/8
0.375    | .011     | 3/8
0.875    | .111     | 7/8
ASCII Caratteri Speciali
Dec | Hex | Char | Nome
----|-----|------|-------------
0   | 00  | NUL  | Null
9   | 09  | TAB  | Tab
10  | 0A  | LF   | Line Feed
13  | 0D  | CR   | Carriage Return
32  | 20  | ' '  | Spazio
33  | 21  | !    | Punto esclamativo
48  | 30  | 0    | Zero
65  | 41  | A    | A maiuscola
97  | 61  | a    | a minuscola
127 | 7F  | DEL  | Delete
Valori Speciali IEEE 754
Caso          | Esponente | Mantissa | Esempio (32-bit)
--------------|-----------|----------|------------------
Zero          | Tutti 0   | 0        | 0x00000000
Denormalized  | Tutti 0   | ≠ 0      | 0x00000001
Normalized    | 1-254     | qualsiasi| 0x3F800000 (1.0)
+Infinito     | Tutti 1   | 0        | 0x7F800000
-Infinito     | Tutti 1   | 0        | 0xFF800000
NaN           | Tutti 1   | ≠ 0      | 0x7FC00000

PROBLEMI COMUNI E SOLUZIONI
Problema 1: Confronto Float
Problema 2: Cicli con Float
// ❌ MALE
if(x ==0.1){...}
// ✅ BENE
#define EPSILON 1e-9
if(fabs(x -0.1)< EPSILON){...}
// ❌ MALE (può non terminare!)
for(float x =0.0; x !=1.0; x +=0.1){
    printf("%f\n", x);
}
// ✅ BENE
for(float x =0.0; x <1.0; x +=0.1){
    printf("%f\n", x);
}
// ✅ ANCORA MEGLIO
for(int i =0; i <10; i++){
float x = i *0.1f;
    printf("%f\n", x);
}

Problema 3: Perdita di Precisione
Problema 4: Conversione Char/Int
Problema 5: Stringhe vs Numeri
// ❌ Problema
float grande =1e20f;
float piccolo =1.0f;
float somma = grande + piccolo; // somma == grande!
// ✅ Soluzione: ordina le operazioni
// Somma prima i valori piccoli
char c ='5';
// ❌ MALE
int n =(int)c; // n = 53 (ASCII!)
// ✅ BENE
int n = c -'0'; // n = 5
// ❌ Confusione
char str[]="123";
int x = str; // ERRORE! str è un puntatore
// ✅ BENE
char str[]="123";
int x = atoi(str); // x = 123

ESERCIZI DI RIEPILOGO COMPLETO
Esercizio Integrato 1
Dato il numero 13.625₁₀:
a) Convertilo in binario (parte intera + decimale)
b) Rappresentalo in virgola fissa 8.8
c) Rappresentalo in IEEE 754 (32 bit)
d) Quanto spazio occuperebbe la stringa “13.625” in:
ASCII
UTF-8
Soluzioni:
a) Binario:
   13₁₀ = 1101₂
   0.625₁₀ = .101₂
   Risultato: 1101.101₂
b) Virgola fissa 8.8:
   Parte intera: 00001101 (8 bit)
   Parte decimale: 10100000 (8 bit, .101 + zeri)
   Totale: 00001101.10100000
c) IEEE 754:
   Normalizzato: 1.101101 × 2³
   S = 0 (positivo)
   E = 3 + 127 = 130 = 10000010₂
   M = 10110100000000000000000 (dopo il bit nascosto)
   Risultato: 0 10000010 10110100000000000000000
d) Stringa "13.625":
   6 caratteri visibili + 1 terminatore '\0' = 7 byte
   Tutti i caratteri sono ASCII (< 128):
• 
• 

   ASCII: 7 byte
   UTF-8: 7 byte (identico per caratteri ASCII)
Esercizio Integrato 2
Analizza la seguente sequenza di byte in memoria:
48 65 6C 6C 6F 20 F0 9F 98 80 21
Determina:
a) È una stringa ASCII valida?
b) È una stringa UTF-8 valida?
c) Cosa rappresenta?
d) Quanti caratteri visibili contiene?
e) Quanti byte occupa?
Soluzioni:
a) NO - I byte F0 9F 98 80 sono > 127 (non ASCII)
b) SÌ - È UTF-8 valido
c) Decodifica:
   48 = 'H'
   65 = 'e'
   6C = 'l'
   6C = 'l'
   6F = 'o'
   20 = ' ' (spazio)
   F0 9F 98 80 = 😀 (emoji, 4 byte UTF-8)
   21 = '!'
   Stringa: "Hello 😀!"
d) 8 caratteri visibili (l'emoji conta come 1 carattere)

e) 11 byte totali (7 ASCII + 4 emoji)
Esercizio Integrato 3
Un programma deve memorizzare temperature da -50.0°C a +150.0°C con precisione di
0.1°C.
Conviene usare virgola fissa o mobile? Perché?
Se si usa virgola fissa, quale formato scegliere?
Se si usa float, quanti bit di mantissa sono necessari per la precisione richiesta?
Quale occupa meno memoria?
Soluzioni:
a) Virgola FISSA è migliore per questo caso:
   - Range limitato e noto
   - Precisione fissa richiesta
   - Più veloce
   - Più predicibile
b) Formato virgola fissa:
   Range: -50.0 a +150.0 → serve segno
   Max valore assoluto: 150.0
   150 richiede 8 bit (256 > 150)
   Precisione 0.1 → serve 1 cifra decimale
   0.1 = 1/10, ma in binario serve più precisione
   Soluzione pratica:
   - Moltiplica tutto per 10: range -500 a +1500
   - Memorizza come intero signed a 16 bit (-32768 a +32767)
   - Quando leggi, dividi per 10.0
   - Spazio: 2 byte
c) Float IEEE 754:
   Mantissa: 23 bit
1. 
2. 
3. 
4. 

   Precisione: ~7 cifre decimali
   Sufficiente per 0.1°C su range 200°C
   Spazio: 4 byte
d) Virgola fissa: 2 byte
   Float: 4 byte
   → Virgola fissa più efficiente (50% spazio in meno)
PUNTI CHIAVE DELLA LEZIONE
✓ Virgola fissa: range e precisione predefiniti, veloce, semplice
✓ Virgola mobile (IEEE 754): flessibile, standard universale
✓ Non tutti i decimali hanno rappresentazione binaria finita (es. 0.1)
✓ Mai confrontare float con ==, usare epsilon
✓ ASCII: 7 bit, 128 caratteri, solo inglese base
✓ UTF-8: lunghezza variabile, compatibile ASCII, universale
✓ Numero ≠ Carattere: ‘5’ (codice 53) ≠ 5 (valore numerico)
✓ Conversione char→int: sottrai ‘0’ (48)
✓ Maiuscola/minuscola: differenza di 32 (bit 5)
✓ Float problematici: arrotondamenti, confronti, accumulo errori
PREPARAZIONE PER LA PROSSIMA
LEZIONE
Nella prossima lezione studieremo:
Architettura del computer: Von Neumann
CPU: ALU, Control Unit, registri
Ciclo fetch-decode-execute: come la CPU esegue istruzioni
Memoria: RAM, cache, gerarchia
Istruzioni a basso livello: introduzione all’assembly
• 
• 
• 
• 
• 

Porta con te:
Esercizi homework completati
Calcolatrice programmabile (se disponibile)
Domande su floating point o charset
Tabelle di conversione create
Suggerimento: Installa un emulatore di CPU semplice (es. CPU Simulator, Little Man
Computer) per visualizzare il funzionamento interno.
GLOSSARIO TECNICO
Fixed Point: Virgola fissa, posizione decimale predefinita
Floating Point: Virgola mobile, esponente variabile
IEEE 754: Standard per numeri in virgola mobile
Mantissa/Significand: Cifre significative di un numero float
Esponente: Potenza nella notazione scientifica
Bias: Offset per esponente (127 float, 1023 double)
Bit nascosto: Il “1.” implicito nella mantissa IEEE 754
NaN: Not a Number, risultato di operazioni invalide
Denormalized: Numeri molto piccoli vicini a zero
ULP: Unit in Last Place, precisione minima
ASCII: American Standard Code for Information Interchange
Code Point: Numero assegnato a un carattere in Unicode
UTF-8: Codifica Unicode lunghezza variabile (1-4 byte)
BOM: Byte Order Mark, intestazione file per indicare encoding
Endianness: Ordine dei byte in memoria (big/little-endian)
RISORSE AGGIUNTIVE
Tool Online Utili
Conversione Float:
https://www.h-schmidt.net/FloatConverter/IEEE754.html
Visualizza IEEE 754 in dettaglio
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

Tabelle ASCII:
https://www.asciitable.com/
https://ascii.cl/
Unicode Explorer:
https://unicode-table.com/
Cerca code point e visualizza caratteri
Conversioni Numeriche:
https://www.rapidtables.com/convert/number/
Binario, ottale, decimale, esadecimale
Letture Consigliate
Paper fondamentali:
“What Every Computer Scientist Should Know About Floating-Point Arithmetic”
(David Goldberg, 1991)
“The Unicode Standard” (Unicode Consortium)
Libri:
“Computer Systems: A Programmer’s Perspective” (Bryant & O’Hallaron) - Capitolo
2
“The Art of Computer Programming, Vol 2” (Knuth) - Aritmetica
Esercizi Interattivi
Float Toy: http://evanw.github.io/float-toy/
Visualizza IEEE 754 interattivamente
UTF-8 Tool: https://mothereff.in/utf-8
Analizza stringhe UTF-8
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

DOMANDE DI AUTOVALUTAZIONE
Rispondi senza guardare gli appunti, poi controlla:
Perché 0.1 non ha rappresentazione binaria finita?
Qual è la differenza principale tra float e double?
Cosa significa il bit nascosto in IEEE 754?
Quando un float diventa NaN?
Qual è il codice ASCII di ‘A’? E di ‘a’?
Come converto velocemente maiuscola in minuscola?
Quanti byte usa UTF-8 per ‘è’? E per ‘😀’?
Qual è la differenza tra numero 5 e carattere ‘5’?
Come si converte ‘7’ nel numero 7?
Perché x == 0.3 è pericoloso con float?
Risposte rapide:
0.1₁₀ = 0.00011001100…₂ (periodico)
float: 32 bit, 7 cifre; double: 64 bit, 15 cifre
Il “1.” della mantissa non viene memorizzato (guadagno 1 bit)
Operazioni invalide: 0/0, ∞-∞, √(-1)
‘A’ = 65; ‘a’ = 97
Somma/sottrai 32, o usa OR 0x20 / AND ~0x20
‘è’ = 2 byte; ‘😀’ = 4 byte
5 = valore numerico (0x05); ‘5’ = codice ASCII 53 (0x35)
‘7’ - ‘0’ = 55 - 48 = 7
Errori di arrotondamento rendono confronti imprecisi
PROGETTO FINALE LEZIONE 4
Mini-Progetto: Analizzatore di Stringhe e Numeri
Scrivi uno pseudocodice per un programma che:
Input: Una stringa qualsiasi (può contenere numeri, lettere, spazi, UTF-8)
1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
9. 
10. 
1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
9. 
10. 

Output:
Numero totale di caratteri
Numero di byte occupati
Quanti caratteri ASCII
Quanti caratteri non-ASCII
Quante lettere maiuscole
Quante lettere minuscole
Quante cifre numeriche
Se la stringa contiene solo cifre, convertila in numero
Esempio:
Input: "Hello123 😀"
Output:
- Caratteri totali: 10
- Byte occupati: 14 (7 ASCII + 1 spazio + 4 emoji + 1 terminatore)
- Caratteri ASCII: 9
- Caratteri non-ASCII: 1 (emoji)
- Maiuscole: 1 ('H')
- Minuscole: 4 ('e','l','l','o')
- Cifre: 3 ('1','2','3')
- Non è un numero puro
Input: "42"
Output:
- Caratteri totali: 2
- Byte occupati: 3
- Caratteri ASCII: 2
- Caratteri non-ASCII: 0
- Maiuscole: 0
- Minuscole: 0
- Cifre: 2
- Valore numerico: 42
1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 

Estensione (difficile):
Aggiungi la capacità di rilevare se una stringa è UTF-8 valida analizzando i pattern dei
byte.
Ottimo lavoro! Ora comprendi come i computer rappresentano numeri e testo! 🎯
Nella prossima lezione scenderemo ancora più in profondità: vedremo come la CPU
esegue fisicamente le istruzioni e come funziona la memoria.


---

# lezione6 primo c

**File:** `lezione6 primo c.pdf`
**Tipo:** `.pdf`
**Dimensione:** 211.6 KB
**Ultima modifica:** 02/07/2026 09:24

---

LEZIONE 6 - Primo Programma in C
Durata: 4 ore | Teoria: 2h | Esercizi: 2h
PARTE TEORICA (2 ore)
6.1 Introduzione al Linguaggio C (15 min)
Storia del C
Timeline:
1972: Dennis Ritchie crea il C ai Bell Labs (AT&T)
1978: Pubblicazione “The C Programming Language” (K&R)
1989: Standard ANSI C (C89)
1999: Standard C99 (nuove funzionalità)
2011: Standard C11 (thread, atomics)
2018: Standard C18 (correzioni bug)
Perché Studiare C?
Vantaggi:
Vicino all’hardware: controllo diretto su memoria e CPU
Efficiente: codice veloce e compatto
Portabile: gira su qualsiasi piattaforma
Fondamentale: base per C++, Java, C#, JavaScript
Diffuso: sistemi operativi, embedded, database, compilatori
Utilizzi del C:
Sistemi operativi (Linux, Windows kernel)
Database (MySQL, PostgreSQL, SQLite)
Linguaggi (Python, Ruby, PHP interpreters)
Embedded systems (Arduino, IoT)
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

Driver hardware
Applicazioni real-time
Caratteristiche:
Linguaggio di medio livello (tra assembly e alto livello)
Compilato (non interpretato)
Tipizzazione statica
Gestione manuale della memoria
Preprocessore potente
6.2 Ambiente di Sviluppo (10 min)
Strumenti Necessari
1. Compilatore:
GCC (GNU Compiler Collection) - Linux, macOS, Windows
Clang - LLVM, moderno e veloce
MSVC (Microsoft Visual C++) - Windows
MinGW - GCC per Windows
2. Editor/IDE:
Visual Studio Code: leggero, estensioni
Code::Blocks: IDE specifico per C/C++
CLion: professionale (JetBrains)
Dev-C++: semplice per principianti
Vim/Emacs: per puristi
3. Debugger:
GDB (GNU Debugger)
LLDB (LLVM Debugger)
Integrato nell’IDE
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

Processo di Compilazione
┌─────────────┐
│ Codice C    │  esempio.c
│ (sorgente)  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│PREPROCESSORE│  #include, #define
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ COMPILATORE │  traduce in assembly
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ ASSEMBLER   │  crea codice oggetto
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   LINKER    │  collega librerie
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ ESEGUIBILE  │  esempio.exe / a.out
└─────────────┘
Comandi base:

6.3 Struttura di un Programma C (20 min)
Il Primo Programma: Hello World
Errori:
Manca # prima di include
Manca ; dopo primo printf
# Compilazione semplice
gcc programma.c -o programma
# Con warning abilitati (RACCOMANDATO!)
gcc-Wall-Wextra programma.c -o programma
# Con informazioni di debug
gcc-g programma.c -o programma
# Ottimizzazione
gcc-O2 programma.c -o programma
# Solo preprocessing
gcc-E programma.c
# Solo compilazione (no linking)
gcc-c programma.c
#include <stdio.h>
int main(){
    printf("Numero: %d\n", 42)
    printf("Testo: %s\n""Ciao");
    Return 0;
1. 
2. 

Manca , tra formato e stringa nel secondo printf
Return dovrebbe essere minuscolo return
Manca } di chiusura
Codice corretto:
4.3 Errori logici (compila ma risultato sbagliato):
Output errato:
Percentuale: 50%
Percorso: C:
uovo    est
Codice corretto:
3. 
4. 
5. 
#include <stdio.h>
int main(){
    printf("Numero: %d\n", 42);
    printf("Testo: %s\n", "Ciao");
return0;
}
#include <stdio.h>
int main(){
    printf("Percentuale: %d%%\n", 50); // Corretto: doppio %
    printf("Percorso: C:\nuovo\test\n");// ERRORE: \n interpretato come 
newline!
return0;
}
#include <stdio.h>

Output corretto:
Percentuale: 50%
Percorso: C:\nuovo\test
Esercizio 5: Progetti Completi (45 min)
5.1 Biglietto di presentazione:
int main(){
    printf("Percentuale: %d%%\n", 50);
    printf("Percorso: C:\\nuovo\\test\n");// Backslash doppio!
return0;
}
/*
 * Programma: Biglietto da Visita
 * Crea un biglietto di presentazione formattato
 */
#include <stdio.h>
int main(){
    printf("╔════════════════════════════════════════╗\n");
    printf("║                                        ║\n");
    printf("║         MARIO ROSSI                    ║\n");
    printf("║         Programmatore C                ║\n");
    printf("║                                        ║\n");
    printf("║  Email:  mario.rossi@email.com        ║\n");
    printf("║  Tel:    +39 123 456 7890             ║\n");
    printf("║  Web:    www.mariorossi.it            ║\n");
    printf("║                                        ║\n");
    printf("╚════════════════════════════════════════╝\n");

5.2 Calcolatrice valori (solo output, no input ancora):
return0;
}
/*
 * Programma: Calcolatrice Semplice
 * Esegue operazioni su due numeri predefiniti
 */
#include <stdio.h>
int main(){
// Numeri da calcolare
int a =15;
int b =4;
    printf("====== CALCOLATRICE ======\n");
    printf("Primo numero:  %d\n", a);
    printf("Secondo numero: %d\n", b);
    printf("==========================\n");
// Operazioni
    printf("%d + %d = %d\n", a, b, a + b);
    printf("%d - %d = %d\n", a, b, a - b);
    printf("%d × %d = %d\n", a, b, a * b);
    printf("%d ÷ %d = %d (quoziente)\n", a, b, a / b);
    printf("%d%%%d = %d (resto)\n", a, b, a % b);
    printf("==========================\n");
return0;
}

Output:
====== CALCOLATRICE ======
Primo numero:  15
Secondo numero: 4
==========================
15 + 4 = 19
15 - 4 = 11
15 × 4 = 60
15 ÷ 4 = 3 (quoziente)
15 % 4 = 3 (resto)
==========================
5.3 Tabella ASCII:
/*
 * Programma: Tabella ASCII
 * Stampa una porzione della tabella ASCII
 */
#include <stdio.h>
int main(){
    printf("=== TABELLA ASCII (caratteri stampabili) ===\n\n");
    printf("Dec  Hex  Char  |  Dec  Hex  Char\n");
    printf("-----------------------------------\n");
// Caratteri da 32 a 126 (stampabili)
    printf(" 32  0x20  '%c'  |   65  0x41  '%c'\n", 32, 65);
    printf(" 33  0x21  '%c'  |   66  0x42  '%c'\n", 33, 66);
    printf(" 34  0x22  '%c'  |   67  0x43  '%c'\n", 34, 67);
    printf(" 48  0x30  '%c'  |   97  0x61  '%c'\n", 48, 97);
    printf(" 49  0x31  '%c'  |   98  0x62  '%c'\n", 49, 98);
    printf(" 50  0x32  '%c'  |   99  0x63  '%c'\n", 50, 99);

5.4 Conversione temperature (valori fissi):
    printf("\nNote:\n");
    printf("- 32 = spazio\n");
    printf("- 48-57 = cifre '0'-'9'\n");
    printf("- 65-90 = lettere 'A'-'Z'\n");
    printf("- 97-122 = lettere 'a'-'z'\n");
return0;
}
/*
 * Programma: Convertitore Temperature
 * Converte da Celsius a Fahrenheit e Kelvin
 */
#include <stdio.h>
int main(){
float celsius =25.0;
float fahrenheit, kelvin;
// Conversioni
    fahrenheit =(celsius *9.0/5.0)+32.0;
    kelvin = celsius +273.15;
    printf("===== CONVERSIONE TEMPERATURE =====\n");
    printf("Temperatura in Celsius:    %.2f°C\n", celsius);
    printf("-----------------------------------\n");
    printf("In Fahrenheit:             %.2f°F\n", fahrenheit);
    printf("In Kelvin:                 %.2fK\n", kelvin);
    printf("===================================\n");

Output:
===== CONVERSIONE TEMPERATURE =====
Temperatura in Celsius:    25.00°C
-----------------------------------
In Fahrenheit:             77.00°F
In Kelvin:                 298.15K
===================================
5.5 Menu informativo:
return0;
}
/*
 * Programma: Sistema Informativo
 * Mostra informazioni sul sistema
 */
#include <stdio.h>
int main(){
    printf("\n");
    printf("╔═══════════════════════════════════════╗\n");
    printf("║    SISTEMA INFORMATIVO - v1.0         ║\n");
    printf("╚═══════════════════════════════════════╝\n");
    printf("\n");
    printf("┌───────────────────────────────────────┐\n");
    printf("│ INFORMAZIONI SUL PROGRAMMA            │\n");
    printf("├───────────────────────────────────────┤\n");
    printf("│ Compilato con: GCC                    │\n");
    printf("│ Standard:      C99                    │\n");
    printf("│ Dimensione:    ~8 KB                  │\n");

Congratulazioni! Hai scritto i tuoi primi programmi in C! 🎉
Ora conosci la struttura base di un programma C e sai come stampare output
formattato. Nelle prossime lezioni aggiungeremo input, variabili e logica per creare
programmi interattivi e potenti!) {
printf(“Hello, World!\n”);
return 0;
}
**Analisi riga per riga:**
**Riga 1: `#include <stdio.h>`**
    printf("│ Architettura:  x86-64                 │\n");
    printf("└───────────────────────────────────────┘\n");
    printf("\n");
    printf("┌───────────────────────────────────────┐\n");
    printf("│ LIMITI TIPI DI DATO (tipici)          │\n");
    printf("├───────────────────────────────────────┤\n");
    printf("│ int:     %d byte                     │\n", (int)sizeof(int));
    printf("│ float:   %d byte                     │\n", (int)sizeof(float));
    printf("│ double:  %d byte                     │\n", (int)sizeof(double));
    printf("│ char:    %d byte                     │\n", (int)sizeof(char));
    printf("└───────────────────────────────────────┘\n");
    printf("\n");
    printf("Premi INVIO per terminare...\n");
return0;
}

```c
#include <stdio.h>
#include: direttiva del preprocessore
<stdio.h>: header file (Standard Input/Output)
Include funzioni per I/O: printf, scanf, getchar, etc.
Il preprocessore “copia-incolla” il contenuto di stdio.h
Riga 3: int main() {
int: tipo di ritorno della funzione (intero)
main: nome della funzione principale
(): lista parametri (vuota in questo caso)
{: inizio blocco funzione
main() è il punto di ingresso del programma
Riga 4: printf("Hello, World!\n");
printf: funzione per stampare (print formatted)
"Hello, World!\n": stringa da stampare
\n: carattere newline (a capo)
;: terminatore istruzione (obbligatorio!)
Riga 5: return 0;
return: restituisce un valore
0: codice di uscita (0 = successo)
Convenzione: 0 = OK, diverso da 0 = errore
Il sistema operativo riceve questo codice
• 
• 
• 
• 
int main(){
• 
• 
• 
• 
• 
    printf("Hello, World!\n");
• 
• 
• 
• 
return0;
• 
• 
• 
• 

Riga 6: }
}: fine blocco funzione
Struttura Generale
Varianti di main()
Forma 1: Senza parametri
}
• 
// 1. DIRETTIVE PREPROCESSORE
#include <libreria.h>
#define COSTANTE valore
// 2. DICHIARAZIONI GLOBALI
int variabile_globale;
// 3. PROTOTIPI FUNZIONI
void mia_funzione(int parametro);
// 4. FUNZIONE MAIN (obbligatoria)
int main(){
// Istruzioni
return0;
}
// 5. DEFINIZIONI FUNZIONI
void mia_funzione(int parametro){
// Corpo funzione
}

Forma 2: Con void esplicito
Forma 3: Con argomenti da riga di comando
Forma 4: Con variabili ambiente (non standard)
6.4 La Funzione printf() (25 min)
Sintassi Base
Esempi:
int main(){
return0;
}
int main(void){
return0;
}
int main(int argc, char*argv[]){
// argc = numero argomenti
// argv = array di stringhe (argomenti)
return0;
}
int main(int argc, char*argv[],char*envp[]){
// envp = variabili ambiente
return0;
}
printf("formato", argomenti);

Specificatori di Formato
Gli specificatori iniziano con % e indicano come stampare i dati.
Tabella completa:
Specificator
e Tipo Esempio Output
%d int (decimale) printf("%d", 42) 42
%i int (decimale) printf("%i", 42) 42
%u unsigned int printf("%u", 42) 42
%ld long printf("%ld", 
123456L) 123456
%lld long long printf("%lld", 123LL)123
%f float/double printf("%f", 3.14) 3.140000
%.2f float (2 decimali) printf("%.2f", 3.14)3.14
%e notazione scientifica printf("%e", 1234.5)1.234500e+0
3
%c char (carattere) printf("%c", 'A') A
%s stringa printf("%s", "ciao")ciao
%p puntatore printf("%p", ptr) 0x7fff5fbff6a0
%x esadecimale minuscoloprintf("%x", 255) ff
%X printf("%X", 255) FF
printf("Ciao"); // Stampa stringa semplice
printf("Numero: %d", 42); // Stampa numero
printf("X=%d, Y=%d", 10, 20);// Stampa due numeri

Specificator
e Tipo Esempio Output
esadecimale
MAIUSCOLO
%o ottale printf("%o", 8) 10
%% carattere % printf("100%%") 100%
Modificatori di Larghezza e Precisione
Larghezza minima:
Precisione per float:
Precisione per stringhe:
Sequenze di Escape
Le sequenze di escape iniziano con \ e rappresentano caratteri speciali.
Sequenza Significato Codice ASCII
\n Newline (a capo) 10
\t Tab orizzontale 9
printf("%5d", 42); // "   42" (5 caratteri, allineato a destra)
printf("%-5d", 42); // "42   " (allineato a sinistra)
printf("%05d", 42); // "00042" (riempito con zeri)
printf("%.2f", 3.14159); // "3.14" (2 decimali)
printf("%.4f", 3.14159); // "3.1416" (4 decimali, arrotondato)
printf("%8.2f", 3.14); // "    3.14" (larghezza 8, 2 decimali)
printf("%.5s", "Hello World"); // "Hello" (primi 5 caratteri)

Sequenza Significato Codice ASCII
\\ Backslash 92
\' Apice singolo 39
\" Doppi apici 34
\0 Null (terminatore stringa) 0
\r Carriage return 13
\b Backspace 8
\a Bell (suono) 7
\v Tab verticale 11
\? Punto interrogativo 63
Esempi:
Esempi Completi
Esempio 1: Stampa formattata
printf("Riga 1\nRiga 2\n"); // Due righe
printf("Nome\tCognome\n"); // Separati da tab
printf("Percorso: C:\\Windows\n");// Backslash
printf("Disse: \"Ciao\"\n"); // Virgolette
#include <stdio.h>
int main(){
int eta =25;
float altezza =1.75;
char iniziale ='M';

Output:
Età: 25 anni
Altezza: 1.75 metri
Iniziale: M
Esempio 2: Tabella formattata
Output:
Nome           Età Stipendio
Mario           30  1500.50
Lucia           28  1800.75
Giuseppe        35  2200.00
Esempio 3: Conversioni di base
    printf("Età: %d anni\n", eta);
    printf("Altezza: %.2f metri\n", altezza);
    printf("Iniziale: %c\n", iniziale);
return0;
}
#include <stdio.h>
int main(){
    printf("%-10s%5s%8s\n", "Nome", "Età", "Stipendio");
    printf("%-10s%5d%8.2f\n", "Mario", 30, 1500.50);
    printf("%-10s%5d%8.2f\n", "Lucia", 28, 1800.75);
    printf("%-10s%5d%8.2f\n", "Giuseppe", 35, 2200.00);
return0;
}

Output:
Decimale: 255
Esadecimale: ff
Esadecimale (maiuscolo): FF
Ottale: 377
Binario: (non supportato direttamente)
6.5 Commenti nel Codice (15 min)
I commenti sono testo ignorato dal compilatore, usati per documentare il codice.
Commenti su Singola Riga
#include <stdio.h>
int main(){
int numero =255;
    printf("Decimale: %d\n", numero);
    printf("Esadecimale: %x\n", numero);
    printf("Esadecimale (maiuscolo): %X\n", numero);
    printf("Ottale: %o\n", numero);
    printf("Binario: (non supportato direttamente)\n");
return0;
}
// Questo è un commento su una riga
int x =5; // Commento dopo codice

Commenti Multi-Riga
Stili di Documentazione
Stile 1: Breve e conciso
Stile 2: Documentazione funzione
Stile 3: Doxygen (documentazione automatica)
/*
 * Questo è un commento
 * su più righe
 */
/* Anche questo funziona */
// Calcola la media di due numeri
float media =(a + b)/2.0;
/*
 * Calcola il fattoriale di un numero
 * 
 * Parametri:
 *   n - numero intero positivo
 * 
 * Ritorna:
 *   n! (fattoriale di n)
 * 
 * Nota: non gestisce overflow
 */
int fattoriale(int n){
// Implementazione...
}

Best Practices per i Commenti
✓ BUONI commenti:
✗ CATTIVI commenti:
/**
 * @brief Calcola la somma di due numeri
 * 
 * @parama Primo numero
 * @paramb Secondo numero
 * @return Somma di a e b
 */
int somma(int a, int b){
return a + b;
}
// Converti temperatura da Celsius a Fahrenheit
float fahrenheit = celsius *9.0/5.0+32.0;
// FIXME: Questo algoritmo è O(n²), da ottimizzare
void ordinamento_lento(int array[],int n){
// ...
}
// TODO: Aggiungere gestione errori
int dividi(int a, int b){
return a / b;
}
// Incrementa i
i++;// Ovvio!
// Questa funzione somma a e b

Regole d’oro:
Spiega il PERCHÉ, non il COSA: il codice dice già cosa fa
Mantieni aggiornati: commenti obsoleti sono peggio di nessun commento
Sii conciso: commenti troppo lunghi non vengono letti
Usa nomi variabili chiari: riduce bisogno di commenti
Documenta algoritmi complessi: aiuta chi legge (incluso te futuro)
6.6 Compilazione ed Esecuzione (15 min)
Step-by-Step: Dal Codice all’Esecuzione
1. Scrivi il codice
2. Salva il file
Nome: hello.c (estensione .c obbligatoria)
Usa editor di testo semplice (non Word!)
3. Compila
int somma(int a, int b){// Ridondante, il nome è chiaro
return a + b;
}
// Codice scritto il 15/03/2023 da Mario
// Non toccare!!! (Cattiva pratica)
1. 
2. 
3. 
4. 
5. 
// hello.c
#include <stdio.h>
int main(){
    printf("Hello, World!\n");
return0;
}
• 
• 

gcc: compilatore
hello.c: file sorgente
-o hello: output eseguibile (nome “hello”)
4. Esegui
5. Vedi output
Hello, World!
Opzioni Utili del Compilatore
Warning (SEMPRE usare!):
-Wall: abilita warning comuni
-Wextra: abilita warning extra
-Werror: tratta warning come errori
Debug:
-g: include simboli debug (per gdb)
Ottimizzazione:
gcc hello.c -o hello
• 
• 
• 
# Linux/macOS
./hello
# Windows
hello.exe
gcc-Wall-Wextra-Werror hello.c -o hello
• 
• 
• 
gcc-g hello.c -o hello
• 

-O0: nessuna ottimizzazione (default)
-O1: ottimizzazione base
-O2: ottimizzazione media (raccomandato)
-O3: ottimizzazione aggressiva
-Os: ottimizza dimensione
Standard C:
-std=c89: ANSI C (1989)
-std=c99: C99 (1999)
-std=c11: C11 (2011)
-std=c18: C18 (2018)
Esempio completo (raccomandato per sviluppo):
Errori Comuni di Compilazione
Errore 1: File non trovato
ciao.c: No such file or directory
Soluzione: Verifica nome file e percorso
Errore 2: Punto e virgola mancante
gcc-O2 hello.c -o hello
• 
• 
• 
• 
• 
gcc-std=c99 hello.c -o hello
• 
• 
• 
• 
gcc-Wall-Wextra-std=c99 -g hello.c -o hello
gcc ciao.c -o ciao
printf("Hello") // Manca ;

error: expected ';' before 'return'
Soluzione: Aggiungi ;
Errore 3: Include mancante
warning: implicit declaration of function 'printf'
Soluzione: Aggiungi #include <stdio.h>
Errore 4: Parentesi non bilanciate
error: expected declaration or statement at end of input
Soluzione: Chiudi tutte le parentesi
6.7 Stile e Indentazione (10 min)
Lo stile del codice è importante per leggibilità e manutenibilità.
Indentazione
Stile K&R (Kernighan & Ritchie):
// Manca #include <stdio.h>
int main(){
    printf("Hello");
}
int main(){
    printf("Hello\n");
return0;
// Manca }

Stile Allman:
Raccomandazione: Scegli uno stile e mantienilo consistente!
Indentazione:
4 spazi (raccomandato per C)
2 spazi (compatto)
Tab (evitare, problemi di visualizzazione)
int main(){
if(condizione){
        istruzione1;
        istruzione2;
}else{
        istruzione3;
}
return0;
}
int main()
{
if(condizione)
{
        istruzione1;
        istruzione2;
}
else
{
        istruzione3;
}
return0;
}
• 
• 
• 

Nomi Variabili
Convenzioni:
Regole:
Nomi descrittivi: temperatura non t
Costanti in MAIUSCOLO: MAX_SIZE, PI
Evita abbreviazioni criptiche
Non usare parole chiave riservate
Spazi e Formattazione
Operatori:
// snake_case (raccomandato per C)
int numero_studenti;
float valore_medio;
// camelCase (comune in altri linguaggi)
int numeroStudenti;
float valoreMedio;
// PascalCase (per tipi/strutture)
struct PersonaDati {
// ...
};
• 
• 
• 
• 
// ✓ BUONO
x = a + b * c;
if(x >0){}
// ✗ CATTIVO
x=a+b*c;
if(x>0){}

Funzioni:
PARTE PRATICA (2 ore)
ESERCIZI GUIDATI
Esercizio 1: Hello World e Varianti (20 min)
1.1 Scrivi e compila il classico “Hello, World!”:
Compila ed esegui:
Output atteso:
// ✓ BUONO
printf("Hello");
somma(a, b);
// ✗ CATTIVO
printf ("Hello");
somma (a,b);
#include <stdio.h>
int main(){
    printf("Hello, World!\n");
return0;
}
gcc hello.c -o hello
./hello

Hello, World!
1.2 Modifica per stampare il tuo nome:
1.3 Stampa su più righe:
Output:
Benvenuto nel corso di C!
Questa è la lezione 6.
Buono studio!
1.4 Usa un’unica printf con sequenze di escape:
#include <stdio.h>
int main(){
    printf("Ciao, mi chiamo Mario!\n");
return0;
}
#include <stdio.h>
int main(){
    printf("Benvenuto nel corso di C!\n");
    printf("Questa è la lezione 6.\n");
    printf("Buono studio!\n");
return0;
}
#include <stdio.h>
int main(){

1.5 Crea un “disegno” ASCII:
Output:
  *****  
 *     * 
*  O O  *
*   ^   *
 * _/ * 
  *****  
Esercizio 2: Esperimenti con printf() (25 min)
2.1 Stampa numeri interi:
    printf("Riga 1\nRiga 2\nRiga 3\n");
return0;
}
#include <stdio.h>
int main(){
    printf("  *****  \n");
    printf(" *     * \n");
    printf("*  O O  *\n");
    printf("*   ^   *\n");
    printf(" * \_/ * \n");
    printf("  *****  \n");
return0;
}
#include <stdio.h>

Output:
Numero: 42
Negativo: -15
Grande: 1000000
2.2 Stampa numeri decimali:
Output:
Pi greco: 3.141590
Pi (2 decimali): 3.14
Piccolo: 0.0000001000
Scientifico: 1.234568e+06
int main(){
    printf("Numero: %d\n", 42);
    printf("Negativo: %d\n", -15);
    printf("Grande: %d\n", 1000000);
return0;
}
#include <stdio.h>
int main(){
    printf("Pi greco: %f\n", 3.14159);
    printf("Pi (2 decimali): %.2f\n", 3.14159);
    printf("Piccolo: %.10f\n", 0.0000001);
    printf("Scientifico: %e\n", 1234567.89);
return0;
}

2.3 Stampa caratteri e stringhe:
Output:
Carattere: A
Codice ASCII: 65
Stringa: Programmazione
Primi 5 caratteri: Progr
2.4 Formato tabellare:
Output:
#include <stdio.h>
int main(){
    printf("Carattere: %c\n", 'A');
    printf("Codice ASCII: %d\n", 'A');
    printf("Stringa: %s\n", "Programmazione");
    printf("Primi 5 caratteri: %.5s\n", "Programmazione");
return0;
}
#include <stdio.h>
int main(){
    printf("%-15s%10s%8s\n", "Prodotto", "Quantità", "Prezzo");
    printf("%-15s%10d%8.2f€\n", "Mele", 10, 2.50);
    printf("%-15s%10d%8.2f€\n", "Arance", 5, 3.20);
    printf("%-15s%10d%8.2f€\n", "Banane", 12, 1.80);
return0;
}

Prodotto            Quantità   Prezzo
Mele                      10     2.50€
Arance                     5     3.20€
Banane                    12     1.80€
2.5 Conversioni di base:
Output:
Decimale:      255
Esadecimale:   0xFF
Ottale:        0377
Carattere:     'ÿ'
Esercizio 3: Commenti e Documentazione (20 min)
3.1 Documenta un programma semplice:
#include <stdio.h>
int main(){
int num =255;
    printf("Decimale:      %d\n", num);
    printf("Esadecimale:   0x%X\n", num);
    printf("Ottale:        0%o\n", num);
    printf("Carattere:     '%c'\n", num);
return0;
}
/*
 * Programma: Calcolatore età

3.2 Commenta codice esistente:
 * Autore: Mario Rossi
 * Data: 10/10/2024
 * Descrizione: Stampa l'anno di nascita data l'età
 */
#include <stdio.h>
int main(){
// Anno corrente
int anno_corrente =2024;
// Età della persona
int eta =25;
// Calcola anno di nascita (approssimativo)
int anno_nascita = anno_corrente - eta;
// Stampa risultato
    printf("Se hai %d anni, sei nato nel %d\n", eta, anno_nascita);
return0; // Successo
}
#include <stdio.h>
int main(){
// Prezzi dei prodotti (in euro)
float prezzo_mela =0.50;
float prezzo_pane =1.20;
float prezzo_latte =0.95;
// Quantità acquistate

Esercizio 4: Debug Errori Comuni (30 min)
4.1 Trova e correggi gli errori:
Codice con errori:
int qta_mele =5;
int qta_pane =2;
int qta_latte =3;
// Calcolo totale spesa
float totale =(prezzo_mela * qta_mele)+
(prezzo_pane * qta_pane)+
(prezzo_latte * qta_latte);
// Visualizza scontrino
    printf("=== SCONTRINO ===\n");
    printf("Mele:  %d × %.2f€ = %.2f€\n", qta_mele, prezzo_mela, prezzo_mela 
* qta_mele);
    printf("Pane:  %d × %.2f€ = %.2f€\n", qta_pane, prezzo_pane, prezzo_pane 
* qta_pane);
    printf("Latte: %d × %.2f€ = %.2f€\n", qta_latte, prezzo_latte, prezzo_latte *
qta_latte);
    printf("=================\n");
    printf("TOTALE: %.2f€\n", totale);
return0;
}
#include <stdio.h>
int main(){
    printf("Hello World)
return0
}

Errori:
Manca " di chiusura in printf
Manca ; dopo printf
Manca ; dopo return
Codice corretto:
4.2 Codice con errori multipli:
ESERCIZI AUTONOMI
Esercizio 6: Creatività
6.1 Crea un programma che stampa un banner ASCII con il tuo nome.
6.2 Crea una “ricevuta fiscale” formattata con almeno 5 prodotti.
6.3 Crea un programma che mostra la tua “schedina” sportiva preferita (squadre e
punteggi).
6.4 Disegna una bandiera usando caratteri ASCII.
6.5 Crea un “orologio” che mostra l’ora (fissa, es. 14:30:45) in formato digitale ASCII.
1. 
2. 
3. 
#include <stdio.h>
int main(){
    printf("Hello World\n");
return0;
}

ESERCIZI DA SVOLGERE A CASA
Homework 1: Scrivi un programma che stampa la tua presentazione personale
includendo:
Nome completo
Età e data di nascita
Città di residenza
3 hobby preferiti
Messaggio di chiusura
Usa printf formattato e sequenze di escape per renderlo leggibile.
Homework 2: Crea un programma che converte:
Un valore in metri in: centimetri, millimetri, chilometri
Stampa i risultati in formato tabellare
Homework 3: Scrivi un programma che calcola e visualizza:
Perimetro e area di un rettangolo (dati base e altezza)
Perimetro e area di un cerchio (dato raggio)
Usa π = 3.14159
Homework 4: Crea un “menu di ristorante” formattato con:
Intestazione
Antipasti (almeno 3) con prezzi
Primi (almeno 3) con prezzi
Secondi (almeno 3) con prezzi
Dolci (almeno 2) con prezzi
Usa allineamento e formattazione
Homework 5: Ricerca ed esperimenta:
Cosa fa la funzione puts()?
Differenza tra printf() e puts()
Cosa fa putchar()?
Scrivi esempi pratici
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

Homework 6: Crea un programma che mostra una tabella di conversione:
Numeri da 0 a 16
In decimale, binario (scritto manualmente), ottale, esadecimale
Formato tabellare pulito
Esempio output:
Dec  Bin   Oct  Hex
  0  0000   0    0
  1  0001   1    1
  2  0010   2    2
...
 16 10000  20   10
APPROFONDIMENTI
Storia del “Hello, World!”
Origine:
Prima apparizione: “A Tutorial Introduction to the Language B” (Brian Kernighan,
1972)
Reso famoso da “The C Programming Language” (K&R, 1978)
Diventato lo standard de facto per test di linguaggi
Versione originale (B language):
main() {
    extrn a, b, c;
    putchar(a); putchar(b); putchar(c);
}
a 'hel';
b 'lo,';
c ' wo\n';
• 
• 
• 
• 
• 
• 

Versione C (K&R 1978):
Versione moderna:
Printf: Storia e Funzionamento Interno
Origine nome: “print formatted” (stampa formattata)
Implementazione semplificata:
Vulnerabilità “format string”:
main()
{
    printf("hello, world\n");
}
#include <stdio.h>
int main(void){
    printf("Hello, World!\n");
return0;
}
// printf è una funzione variadica (numero variabile argomenti)
int printf(constchar*format, ...){
// 1. Parse stringa formato
// 2. Per ogni %X trovato:
//    - Preleva prossimo argomento
//    - Converti secondo specificatore
//    - Stampa
// 3. Ritorna numero caratteri stampati
}

Preprocessore C
Il preprocessore elabora il codice PRIMA della compilazione.
Direttive principali:
1. #include:
2. #define:
3. Compilazione condizionale:
// PERICOLOSO! Mai fare così:
char input[100];
gets(input);// Input da utente
printf(input);// BUG DI SICUREZZA!
// Se input = "%x%x%x%x" legge memoria stack!
// SICURO:
printf("%s", input);
#include <stdio.h>// Header di sistema (cerchi standard)
#include "miofile.h"// Header locale (directory corrente)
#define PI 3.14159
#define MAX(a,b)((a)>(b)?(a): (b))
// Uso:
float area = PI * raggio * raggio;
int maggiore = MAX(10, 20);
#ifdef DEBUG
    printf("Debug: x = %d\n", x);

4. Pragma:
Esempio espansione:
Ottimizzazione Compilatore
Il compilatore può ottimizzare il codice per renderlo più veloce.
Esempio:
#endif
#if VERSIONE >= 2
    nuova_funzione();
#else
    vecchia_funzione();
#endif
#pragma once  // Include una sola volta (alternativa a include guard)
// Codice originale
#define QUADRATO(x)((x)*(x))
int y = QUADRATO(5);
// Dopo preprocessore
int y =((5)*(5));
// Codice originale
int calcola(){
int x =2;
int y =3;
int z = x * y +1;
return z;
}

Livelli ottimizzazione:
-O0: Nessuna (default, veloce compilazione)
-O1: Base (poco impatto compile time)
-O2: Media (raccomandato per release)
-O3: Aggressiva (può aumentare dimensione)
-Os: Dimensione (binario piccolo)
-Ofast: Massima velocità (può violare standard)
Esempio impatto:
Cross-Compilation
Puoi compilare per piattaforme diverse dalla tua.
Esempio: compilare per ARM su x86:
// Dopo ottimizzazione (-O2)
int calcola(){
return7; // Tutto calcolato a compile-time!
}
• 
• 
• 
• 
• 
• 
// Benchmark: somma 1 miliardo di numeri
int somma =0;
for(int i =0; i <1000000000; i++){
    somma += i;
}
Risultati:
-O0: 2.5 secondi
-O1: 1.2 secondi
-O2: 0.3 secondi
-O3: 0.001 secondi (loop eliminato! calcolo diretto)

Usi:
Sviluppo embedded (Arduino, Raspberry Pi)
Sviluppo mobile
Sistemi industriali
Standard Library vs System Calls
Standard Library (libc):
Funzioni portabili (printf, malloc, fopen)
Astratte dal sistema operativo
Garantite su tutte le piattaforme
System Calls:
Funzioni specifiche OS (Linux: fork, Windows: CreateProcess)
Accesso diretto al kernel
Non portabili
Esempio:
# Installa cross-compiler
sudo apt-get install gcc-arm-linux-gnueabi
# Compila per ARM
arm-linux-gnueabi-gcc-o hello_arm hello.c
# Non puoi eseguire direttamente su x86!
# Serve emulatore o dispositivo ARM
• 
• 
• 
• 
• 
• 
• 
• 
• 
// Standard Library (portabile)
FILE*f = fopen("file.txt", "r");
fclose(f);
// System Call Linux (non portabile)

Undefined Behavior (UB)
Alcuni errori causano comportamento indefinito: il programma può fare QUALSIASI
COSA.
Esempi UB:
Conseguenze UB:
Crash
Risultati casuali
Funziona su PC ma non su server
“Nasal demons” (folklore: può far uscire demoni dal naso!)
int fd = open("file.txt", O_RDONLY);
close(fd);
// 1. Array out of bounds
int arr[5];
arr[10]=42; // UB!
// 2. Divisione per zero
int x =10/0; // UB!
// 3. Signed integer overflow
int max =2147483647;
int y = max +1; // UB!
// 4. Dereferenziare NULL
int*p = NULL;
*p =5; // UB!
// 5. Usare variabile non inizializzata
int x;
printf("%d", x); // UB!
• 
• 
• 
• 

Prevenzione:
Usa -Wall -Wextra -Werror
Usa sanitizer: -fsanitize=address,undefined
Inizializza sempre variabili
Controlla limiti array
RIEPILOGO CONCETTI CHIAVE
Struttura Programma C
Printf Essenziale
• 
• 
• 
• 
#include <librerie.h>// Preprocessore
int main(){ // Funzione principale
// Istruzioni
return0; // Codice uscita
}
printf("formato", argomenti);
Specificatori principali:
%d /%i  -int
%f       -float/double
%c       -char
%s       - stringa
%x /%X  - esadecimale
%p       - puntatore
%% - carattere %

Sequenze Escape
Compilazione
TABELLE DI RIFERIMENTO RAPIDO
Specificatori Printf Comuni
Tipo Specificatore Esempio
int %d printf(“%d”, 42)
unsigned %u printf(“%u”, 42)
long %ld printf(“%ld”, 123456L)
float/double %f printf(“%f”, 3.14)
float (2 dec) %.2f printf(“%.2f”, 3.14)
char %c printf(“%c”, ‘A’)
string %s printf(“%s”, “ciao”)
hex %x printf(“%x”, 255)
\n  - newline
\t  - tab
\\  - backslash
\"  - doppi apici
\'  - apice singolo
gcc-Wall-Wextra file.c -o programma
./programma

Tipo Specificatore Esempio
pointer %p printf(“%p”, &var)
Opzioni GCC Utili
Opzione Scopo
-Wall Warning comuni
-Wextra Warning extra
-Werror Warning → errori
-g Debug info
-O2 Ottimizzazione
-std=c99 Standard C99
-o file Nome output
-c Compila senza link
Caratteri Escape
Sequenza Nome ASCII
\n Newline 10
\t Tab 9
\r Carriage return 13
\\ Backslash 92
\' Apice 39
\" Doppi apici 34

Sequenza Nome ASCII
\0 Null 0
\a Bell 7
PROBLEMI COMUNI E SOLUZIONI
Problema 1: Printf non stampa
Causa: Buffer non svuotato
Soluzione:
Problema 2: Warning “implicit declaration”
warning: implicit declaration of function 'printf'
Causa: Manca include
Soluzione:
printf("Hello"); // Non appare!
printf("Hello\n"); // \n svuota buffer
// oppure
printf("Hello");
fflush(stdout);
#include <stdio.h>// In cima al file

Problema 3: Caratteri strani su Windows
Causa: Encoding diverso (Windows usa CP-1252, non UTF-8)
Soluzione:
Problema 4: Return type mismatch
warning: control reaches end of non-void function
Causa: Manca return in funzione
Soluzione:
PUNTI CHIAVE DELLA LEZIONE
✓ main() è il punto di ingresso, obbligatorio
✓ #include <stdio.h> per usare printf
✓ printf() stampa output formattato con specificatori %
✓ return 0 indica successo (0 = OK, altro = errore)
✓ ; termina ogni istruzione
✓ Commenti con // (singola) o /* */ (multi-riga)
✓ Compilazione: gcc file.c -o programma
// Aggiungi in main():
#ifdef _WIN32
    system("chcp 65001 > nul"); // UTF-8 su Windows
#endif
int main(){
    printf("Hello\n");
return0; // ← Obbligatorio!
}

✓ Indentazione e stile: mantieni consistenza
✓ Warning: sempre abilitare con -Wall -Wextra
✓ Documentazione: commenta il PERCHÉ, non il COSA
PREPARAZIONE PER LA PROSSIMA
LEZIONE
Nella prossima lezione studieremo:
Variabili e tipi di dato: int, float, char, double
Dichiarazione e inizializzazione
Input con scanf(): leggere dati da utente
Operatori aritmetici: +, -, *, /, %
Conversioni di tipo: casting
Porta con te:
Ambiente C funzionante
Esercizi homework completati
Domande su printf o compilazione
Esperimenti fatti autonomamente
Verifica preparazione:
Riesci a compilare ed eseguire programmi?
Conosci i principali specificatori printf?
Sai come commentare il codice?
Hai familiarità con errori compilazione?
GLOSSARIO TECNICO
Compilatore: Traduce codice C in eseguibile
Preprocessore: Elabora direttive # prima compilazione
Header file: File .h con dichiarazioni funzioni
main(): Funzione principale, punto ingresso
printf(): Funzione stampa formattata
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

Specificatore formato: %d, %f, %s in printf
Sequenza escape: \n, \t, \ caratteri speciali
Commento: Testo ignorato dal compilatore
Indentazione: Spaziatura per leggibilità
Warning: Avviso compilatore (non errore fatale)
Linking: Collegamento librerie a programma
Standard library: Libreria funzioni C standard (libc)
Return code: Valore ritornato da main (0 = successo)
Buffer: Memoria temporanea per I/O
Undefined Behavior: Comportamento non specificato standard
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 


---

# lezione7 variabili input

**File:** `lezione7 variabili input.pdf`
**Tipo:** `.pdf`
**Dimensione:** 198.6 KB
**Ultima modifica:** 02/07/2026 09:24

---

LEZIONE 7 - Variabili e Tipi di Dato
Durata: 4 ore | Teoria: 2h | Esercizi: 2h
PARTE TEORICA (2 ore)
7.1 Concetto di Variabile (15 min)
Cos’è una Variabile?
Una variabile è un contenitore che può memorizzare un valore in memoria durante
l’esecuzione del programma.
Analogia: Una variabile è come una scatola etichettata:
Nome (etichetta): identifica la variabile
Tipo (dimensione scatola): determina cosa può contenere
Valore (contenuto): dato memorizzato
Indirizzo (posizione): dove si trova in memoria
┌─────────────────────┐
│  Nome: eta          │  ← Etichetta
├─────────────────────┤
│  Tipo: int          │  ← Tipo di dato
├─────────────────────┤
│  Valore: 25         │  ← Contenuto
├─────────────────────┤
│  Indirizzo: 0x7fff  │  ← Posizione memoria
└─────────────────────┘
• 
• 
• 
• 

Caratteristiche Variabili in C
1. Tipizzazione Statica:
Il tipo è dichiarato e non cambia
Controllato a compile-time
2. Dichiarazione Obbligatoria:
Devi dichiarare prima di usare
Il compilatore riserva spazio in memoria
3. Scope (Ambito):
Locali: dentro funzioni, visibili solo lì
Globali: fuori funzioni, visibili ovunque
• 
• 
int x =5; // x è intero e rimarrà intero
x ="ciao"; // ERRORE! Non puoi assegnare stringa
• 
• 
int x; // Dichiarazione
x =10; // Assegnazione
// OPPURE
int y =20; // Dichiarazione + Inizializzazione
• 
• 
int globale =100; // Variabile globale
int main(){
int locale =50; // Variabile locale
    printf("%d\n", globale); // OK
    printf("%d\n", locale); // OK
return0;
}

Memoria e Variabili
Quando dichiari una variabile, il compilatore:
Alloca spazio in memoria (RAM o registri)
Assegna indirizzo univoco
Associa nome all’indirizzo
Esempio in memoria:
Indirizzo | Variabile | Valore
----------|-----------|--------
0x1000    | int x     | 42
0x1004    | float y   | 3.14
0x1008    | char c    | 'A'
0x1009    | int z     | 100
7.2 Tipi di Dato Primitivi (25 min)
Il C offre diversi tipi primitivi (built-in) per memorizzare dati.
Numeri Interi
1. int (Integer)
Dimensione: tipicamente 4 byte (32 bit)
void altra_funzione(){
    printf("%d\n", globale); // OK
    printf("%d\n", locale); // ERRORE! locale non visibile qui
}
1. 
2. 
3. 
int eta =25;
int anno =2024;
int temperatura =-5;
• 

Range: -2,147,483,648 a +2,147,483,647
Uso: numeri interi, contatori, indici
2. short (Short Integer)
Dimensione: tipicamente 2 byte (16 bit)
Range: -32,768 a +32,767
Uso: quando serve meno spazio
3. long (Long Integer)
Dimensione: tipicamente 4 o 8 byte
Range: almeno come int, spesso 64 bit
Uso: numeri molto grandi
4. long long
Dimensione: 8 byte (64 bit)
Range: -9,223,372,036,854,775,808 a +9,223,372,036,854,775,807
Uso: numeri enormi (timestamp, grandi calcoli)
5. Unsigned (senza segno)
Unsigned: solo numeri positivi (no negativi)
• 
• 
short giorno =15;
short mese =10;
• 
• 
• 
long popolazione =1400000000L; // Nota la 'L'
long distanza =384400000L;
• 
• 
• 
longlong big_number =9223372036854775807LL; // Nota 'LL'
• 
• 
• 
unsignedint positivo =42;
unsignedshort porta =8080;
unsignedlong id =4294967295UL;
• 

Range raddoppia in positivo
unsigned int: 0 a 4,294,967,295
Tabella Riassuntiva Interi:
Tipo Dimensio
ne Range (signed) Range (unsigned)
char 1 byte -128 a 127 0 a 255
short 2 byte -32,768 a 32,767 0 a 65,535
int 4 byte -2,147,483,648 a
2,147,483,647 0 a 4,294,967,295
long 4/8 byte varia varia
long
long 8 byte -9,223,372,036,854,775,808
a …
0 a
18,446,744,073,709,551,615
Numeri Decimali (Floating Point)
1. float (Single Precision)
Dimensione: 4 byte (32 bit)
Precisione: ~7 cifre decimali
Range: ±3.4 × 10³⁸
Uso: calcoli scientifici base, coordinate
2. double (Double Precision)
Dimensione: 8 byte (64 bit)
• 
• 
float pi =3.14159f; // Nota la 'f'
float temperatura =36.5f;
float peso =75.3f;
• 
• 
• 
• 
double pi_preciso =3.141592653589793;
double distanza_terra_sole =1.496e11; // Notazione scientifica
• 

Precisione: ~15 cifre decimali
Range: ±1.7 × 10³⁰⁸
Uso: calcoli precisi, default per float in C
3. long double (Extended Precision)
Dimensione: 10, 12 o 16 byte (dipende da sistema)
Precisione: ~19 cifre decimali
Uso: calcoli estremamente precisi
Confronto float vs double:
Caratteri
char (Character)
Dimensione: 1 byte (8 bit)
Range: -128 a 127 (signed) o 0 a 255 (unsigned)
Uso: singolo carattere, piccoli interi
Importante: 'A' ≠ "A" (carattere vs stringa)
• 
• 
• 
longdouble molto_preciso =3.141592653589793238462643383279L;
• 
• 
• 
float f =0.1f+0.2f;
double d =0.1+0.2;
printf("float:  %.20f\n", f); // 0.30000001192092895508
printf("double: %.20f\n", d); // 0.29999999999999998890
// Nessuno è esattamente 0.3!
char lettera ='A';
char cifra ='5';
char simbolo ='@';
char newline ='\n';
• 
• 
• 
• 

char come intero:
Tipo Booleano (C99+)
_Bool / bool
Dimensione: 1 byte
Valori: 0 (false) o 1 (true)
Prima di C99: si usava int (0 = falso, diverso da 0 = vero)
Tipo Void
void
Non è un valore: indica “assenza di tipo”
char c =65; // Equivalente a 'A' (codice ASCII)
printf("%c\n", c); // Stampa: A
printf("%d\n", c); // Stampa: 65
#include <stdbool.h>// Per 'bool', 'true', 'false'
bool attivo =true;
bool completato =false;
if(attivo){
    printf("Sistema attivo\n");
}
• 
• 
• 
void funzione_senza_ritorno(){
    printf("Non ritorno nulla\n");
// Nessun return
}
void*puntatore_generico; // Puntatore a tipo sconosciuto
• 

Uso: funzioni senza return, puntatori generici
7.3 Dichiarazione e Inizializzazione (15 min)
Dichiarazione
Sintassi:
Esempi:
Dichiarazioni multiple:
Inizializzazione
Inizializzazione diretta:
Inizializzazione vs Assegnazione:
• 
tipo nome_variabile;
int x;
float temperatura;
char iniziale;
double pi;
int a, b, c; // Tre variabili int
float x, y, z; // Tre variabili float
int i =0, j =1, k; // Due inizializzate, una no
int x =10;
float y =3.14f;
char c ='A';

Valori Non Inizializzati
ATTENZIONE: Variabili non inizializzate contengono garbage (spazzatura)!
Comportamento:
Variabili locali: garbage (valori casuali in memoria)
Variabili globali/statiche: inizializzate a 0 automaticamente
Best Practice:Inizializza SEMPRE le variabili!
// Inizializzazione (alla dichiarazione)
int x =5;
// Assegnazione (dopo dichiarazione)
int y;
y =10;
int x; // NON inizializzato
printf("%d\n", x); // Stampa valore casuale (garbage)!
• 
• 
int globale; // Automaticamente = 0
int main(){
int locale; // Contiene garbage!
    printf("Globale: %d\n", globale); // Stampa: 0
    printf("Locale: %d\n", locale); // Stampa: ??? (casuale)
return0;
}
// ✓ BUONO
int x =0;

Costanti
const (variabili immutabili):
#define (macro preprocessore):
Differenza const vs #define:
float y =0.0f;
char c ='\0';
// ✗ CATTIVO
int x;
float y;
char c;
constint MAX_STUDENTI =100;
constfloat PI =3.14159f;
constchar NUOVA_LINEA ='\n';
// Tentativo di modifica → ERRORE
MAX_STUDENTI =200; // ERRORE! const non modificabile
#define MAX_SIZE 1000
#define PI 3.14159
#define NOME_PROGRAMMA "MioApp"
// Uso:
int array[MAX_SIZE];
float circonferenza =2* PI * raggio;
// const: variabile vera con tipo e indirizzo
constint x =10;
printf("%p\n", &x); // OK, ha indirizzo

7.4 Operatore di Assegnazione (10 min)
Assegnazione Base
Sintassi:
Esempi:
Assegnazioni Multiple
Concatenazione:
// #define: semplice sostituzione testuale
#define Y 10
printf("%p\n", &Y); // ERRORE! Y è sostituito con 10
variabile = valore;
int x;
x =42; // Assegna 42 a x
float y;
y =3.14f; // Assegna 3.14 a y
char c;
c ='A'; // Assegna 'A' a c
int a, b, c;
a = b = c =10; // Tutti = 10 (da destra a sinistra)
// Equivalente a:
c =10;

Swap (scambio) di variabili:
L-value e R-value
L-value (left-value): può stare a sinistra di = (indirizzo modificabile)
R-value (right-value): può stare solo a destra di = (valore)
7.5 Input con scanf() (25 min)
La funzione scanf() legge input da tastiera (standard input).
b = c;
a = b;
int x =5, y =10, temp;
// Scambio tradizionale (con variabile temporanea)
temp = x; // temp = 5
x = y; // x = 10
y = temp; // y = 5
printf("x = %d, y = %d\n", x, y); // x = 10, y = 5
int x =5;
int y =10;
x = y; // OK: x è l-value, y è r-value
y = x +5; // OK: y è l-value, x+5 è r-value
10= x; // ERRORE! 10 è r-value, non può stare a sinistra
x + y =15; // ERRORE! x+y è r-value

Sintassi Base
Nota importante: Il simbolo & (indirizzo di) è obbligatorio!
Leggere Diversi Tipi
Numeri interi:
Numeri decimali:
Caratteri:
Stringhe (anticipazione):
scanf("formato", &variabile);
int eta;
printf("Inserisci età: ");
scanf("%d", &eta);
printf("Hai %d anni\n", eta);
float altezza;
printf("Inserisci altezza (m): ");
scanf("%f", &altezza);
printf("Altezza: %.2f metri\n", altezza);
char iniziale;
printf("Inserisci iniziale: ");
scanf(" %c", &iniziale); // Nota lo SPAZIO prima di %c
printf("Iniziale: %c\n", iniziale);
char nome[50];
printf("Inserisci nome: ");

Specificatori scanf()
Tipo Specificatore Esempio
int %d scanf(“%d”, &x)
unsigned int %u scanf(“%u”, &x)
short %hd scanf(“%hd”, &x)
long %ld scanf(“%ld”, &x)
long long %lld scanf(“%lld”, &x)
float %f scanf(“%f”, &x)
double %lf scanf(“%lf”, &x)
long double %Lf scanf(“%Lf”, &x)
char %c scanf(“%c”, &x)
string %s scanf(“%s”, str)
ATTENZIONE:
printf float: %f
scanf float: %f
printf double: %f (o %lf)
scanf double: %lf (importante!)
Input Multiplo
Più variabili in una volta:
scanf("%s", nome); // Nota: NO & per array/stringhe!
printf("Ciao, %s!\n", nome);
• 
• 
• 
• 
int giorno, mese, anno;
printf("Inserisci data (gg mm aaaa): ");

Input:
15 10 2024
Output:
Data: 15/10/2024
Problemi Comuni con scanf()
Problema 1: Carattere dopo numero
Problema 2: Buffer non svuotato
scanf("%d%d%d", &giorno, &mese, &anno);
printf("Data: %02d/%02d/%d\n", giorno, mese, anno);
int num;
char car;
scanf("%d", &num); // Legge numero
scanf("%c", &car); // Legge '\n' residuo! BUG!
// SOLUZIONE: spazio prima di %c
scanf(" %c", &car); // Salta whitespace
char c1, c2;
scanf("%c", &c1); // Inserisci 'A' + INVIO
scanf("%c", &c2); // Legge '\n'! Non chiede input
// SOLUZIONE 1: spazio
scanf(" %c", &c2);

Problema 3: Input non valido
Valore di Ritorno scanf()
scanf() ritorna il numero di elementi letti con successo.
Alternative a scanf()
fgets() per stringhe (più sicuro):
// SOLUZIONE 2: svuota buffer
while(getchar()!='\n'); // Consuma fino a newline
int x;
scanf("%d", &x); // Utente inserisce "abc"
// scanf fallisce, x rimane non modificato, buffer corrotto
// SOLUZIONE: controlla valore di ritorno
if(scanf("%d", &x)!=1){
    printf("Input non valido!\n");
while(getchar()!='\n'); // Svuota buffer
}
int x, y;
int letti = scanf("%d%d", &x, &y);
if(letti ==2){
    printf("Entrambi letti: %d, %d\n", x, y);
}elseif(letti ==1){
    printf("Solo primo letto: %d\n", x);
}else{
    printf("Nessun numero letto!\n");
}

getchar() per singolo carattere:
7.6 Operatore sizeof (10 min)
L’operatore sizeof restituisce la dimensione in byte di un tipo o variabile.
Sintassi
Esempi
Dimensione tipi:
Output tipico (x86-64):
char nome[50];
printf("Nome: ");
fgets(nome, 50, stdin); // Legge max 49 caratteri + '\0'
char c;
printf("Premi un tasto: ");
c = getchar();
printf("Hai premuto: %c\n", c);
sizeof(tipo)
sizeof(variabile)
sizeof variabile  // Parentesi opzionali per variabili
printf("sizeof(char): %zu byte\n", sizeof(char));
printf("sizeof(int): %zu byte\n", sizeof(int));
printf("sizeof(float): %zu byte\n", sizeof(float));
printf("sizeof(double): %zu byte\n", sizeof(double));
printf("sizeof(long long): %zu byte\n", sizeof(longlong));

sizeof(char): 1 byte
sizeof(int): 4 byte
sizeof(float): 4 byte
sizeof(double): 8 byte
sizeof(long long): 8 byte
Dimensione variabili:
Array (anticipazione):
Note Importante
%zu per sizeof:
int x =42;
float y =3.14f;
double z =2.718;
printf("x occupa %zu byte\n", sizeof(x)); // 4
printf("y occupa %zu byte\n", sizeof(y)); // 4
printf("z occupa %zu byte\n", sizeof(z)); // 8
int array[10];
printf("Array occupa %zu byte\n", sizeof(array)); // 40 (10 × 4)
printf("Elementi: %zu\n", sizeof(array)/sizeof(array[0]));// 10
// ✓ CORRETTO
printf("%zu\n", sizeof(int));
// ✗ SBAGLIATO (può funzionare ma non portabile)
printf("%d\n", sizeof(int));
printf("%lu\n", sizeof(int));

sizeof è compile-time:
7.7 Conversioni di Tipo (15 min)
Le conversioni permettono di cambiare tipo a un dato.
Conversioni Implicite (Automatiche)
Promozione intera:
Promozione in espressioni:
Perdita di informazione:
Conversioni Esplicite (Casting)
Sintassi:
int size =sizeof(int); // Calcolato a compile-time, non runtime
char c ='A'; // 1 byte
int i = c; // Promosso automaticamente a int
printf("%d\n", i);// 65
int x =10;
float y =3.5f;
float risultato = x + y; // x promosso a float, risultato float
float f =3.14f;
int i = f; // f troncato a 3 (perde decimali)
printf("%d\n", i);// 3
(tipo) espressione

Esempi:
Cast necessari:
Regole Conversione Automatica
Gerarchia tipi (dal più piccolo al più grande):
char → short → int → long → long long → float → double → long double
In espressioni miste:
Il tipo più piccolo viene promosso al più grande
Il risultato ha il tipo più grande
int x =10;
int y =3;
float risultato =(float)x / y; // 10.0 / 3 = 3.333...
// Senza cast:
float risultato2 = x / y; // 10 / 3 = 3 (divisione intera!)
// Divisione intera vs reale
int a =7, b =2;
printf("Senza cast: %d\n", a / b); // 3
printf("Con cast: %.2f\n", (float)a / b);// 3.50
// Perdita precisione controllata
double pi =3.141592653;
int pi_int =(int)pi; // Esplicito: voglio troncare
printf("%d\n", pi_int);// 3
• 
• 
int i =10;
float f =3.5f;
double d =2.7;

Divisione intera vs reale:
Warning e Conversioni
Il compilatore avvisa per conversioni pericolose:
PARTE PRATICA (2 ore)
ESERCIZI GUIDATI
Esercizio 1: Dichiarazione e Inizializzazione (20 min)
1.1 Dichiara variabili di vari tipi e stampale:
auto result = i + f; // int → float, result è float
auto result2 = f + d; // float → double, result2 è double
int a =5, b =2;
int r1 = a / b; // 2 (divisione intera)
float r2 = a / b; // 2.0 (divisione intera, poi assegnato a float)
float r3 =(float)a / b; // 2.5 (a promosso, divisione reale)
float r4 = a /(float)b; // 2.5 (b promosso, divisione reale)
float r5 =(float)(a / b);// 2.0 (divisione intera, poi cast)
double d =3.14159;
int i = d; // Warning: possibile perdita dati
// Soluzione: cast esplicito (dice "lo so, lo voglio")
int i =(int)d; // OK, nessun warning

Output:
Età: 25 anni
Altezza: 1.75 metri
Peso: 70.5 kg
Iniziale: M
1.2 Esperimento con valori non inizializzati:
#include <stdio.h>
int main(){
// Dichiarazione e inizializzazione
int eta =25;
float altezza =1.75f;
double peso =70.5;
char iniziale ='M';
// Stampa
    printf("Età: %d anni\n", eta);
    printf("Altezza: %.2f metri\n", altezza);
    printf("Peso: %.1f kg\n", peso);
    printf("Iniziale: %c\n", iniziale);
return0;
}
#include <stdio.h>
int globale_non_init; // Globale
int main(){
int locale_non_init; // Locale

1.3 Uso di const:
1.4 Sizeof dei tipi:
    printf("Globale non inizializzata: %d\n", globale_non_init);
    printf("Locale non inizializzata: %d\n", locale_non_init);
// Valori attesi:
// Globale: 0 (inizializzata automaticamente)
// Locale: ??? (garbage, valore casuale)
return0;
}
#include <stdio.h>
int main(){
constfloat PI =3.14159f;
constint GIORNI_SETTIMANA =7;
float raggio =5.0f;
float circonferenza =2* PI * raggio;
    printf("Circonferenza: %.2f\n", circonferenza);
    printf("Giorni in una settimana: %d\n", GIORNI_SETTIMANA);
// PI = 3.0f;  // ERRORE! const non modificabile
return0;
}
#include <stdio.h>
int main(){

Esercizio 2: Input con scanf() (25 min)
2.1 Input singolo intero:
Esempio esecuzione:
    printf("=== DIMENSIONI TIPI ===\n");
    printf("char:       %zu byte\n", sizeof(char));
    printf("short:      %zu byte\n", sizeof(short));
    printf("int:        %zu byte\n", sizeof(int));
    printf("long:       %zu byte\n", sizeof(long));
    printf("long long:  %zu byte\n", sizeof(longlong));
    printf("float:      %zu byte\n", sizeof(float));
    printf("double:     %zu byte\n", sizeof(double));
    printf("long double: %zu byte\n", sizeof(longdouble));
return0;
}
#include <stdio.h>
int main(){
int numero;
    printf("Inserisci un numero intero: ");
    scanf("%d", &numero);
    printf("Hai inserito: %d\n", numero);
    printf("Il doppio è: %d\n", numero *2);
return0;
}

Inserisci un numero intero: 15
Hai inserito: 15
Il doppio è: 30
2.2 Input di più valori:
2.3 Input float e calcolo IMC:
#include <stdio.h>
int main(){
int giorno, mese, anno;
    printf("Inserisci data di nascita (gg mm aaaa): ");
    scanf("%d%d%d", &giorno, &mese, &anno);
    printf("Sei nato il %02d/%02d/%d\n", giorno, mese, anno);
int eta_approssimativa =2024- anno;
    printf("Età approssimativa: %d anni\n", eta_approssimativa);
return0;
}
#include <stdio.h>
int main(){
float peso, altezza, imc;
    printf("=== CALCOLO IMC ===\n");
    printf("Inserisci peso (kg): ");
    scanf("%f", &peso);
    printf("Inserisci altezza (m): ");

Esempio esecuzione:
=== CALCOLO IMC ===
Inserisci peso (kg): 70
Inserisci altezza (m): 1.75
=== RISULTATO ===
Peso: 70.0 kg
Altezza: 1.75 m
IMC: 22.9
    scanf("%f", &altezza);
// Calcolo IMC = peso / (altezza²)
    imc = peso /(altezza * altezza);
    printf("\n=== RISULTATO ===\n");
    printf("Peso: %.1f kg\n", peso);
    printf("Altezza: %.2f m\n", altezza);
    printf("IMC: %.1f\n", imc);
    printf("\nClassificazione:\n");
if(imc <18.5){
        printf("Sottopeso\n");
}elseif(imc <25){
        printf("Normopeso\n");
}elseif(imc <30){
        printf("Sovrappeso\n");
}else{
        printf("Obesità\n");
}
return0;
}

Classificazione:
Normopeso
2.4 Input carattere (con problema e soluzione):
Esercizio 3: Conversioni di Tipo (20 min)
3.1 Divisione intera vs reale:
#include <stdio.h>
int main(){
int numero;
char lettera;
    printf("Inserisci un numero: ");
    scanf("%d", &numero);
// PROBLEMA: scanf lascia '\n' nel buffer
    printf("Inserisci una lettera: ");
    scanf(" %c", &lettera); // SOLUZIONE: spazio prima di %c
    printf("\nHai inserito:\n");
    printf("Numero: %d\n", numero);
    printf("Lettera: %c\n", lettera);
return0;
}
#include <stdio.h>
int main(){
int a =7, b =2;

Output:
=== DIVISIONE ===
a = 7, b = 2
Divisione intera: 7 / 2 = 3
Divisione reale: 3.50
Resto: 7 % 2 = 1
3.2 Troncamento e arrotondamento:
    printf("=== DIVISIONE ===\n");
    printf("a = %d, b = %d\n\n", a, b);
// Divisione intera
int ris_int = a / b;
    printf("Divisione intera: %d / %d = %d\n", a, b, ris_int);
// Divisione reale (cast)
float ris_float =(float)a / b;
    printf("Divisione reale: %.2f\n", ris_float);
// Modulo (resto)
int resto = a % b;
    printf("Resto: %d%%%d = %d\n", a, b, resto);
return0;
}
#include <stdio.h>
#include <math.h>
int main(){

Output:
Valore originale: 3.14159
Cast a int: 3
Arrotondato: 3
Floor: 3
Ceil: 4
3.3 Overflow e underflow:
double pi =3.14159;
    printf("Valore originale: %.5f\n", pi);
// Conversione diretta (troncamento)
int pi_int =(int)pi;
    printf("Cast a int: %d\n", pi_int);
// Arrotondamento
int pi_round =(int)round(pi);
    printf("Arrotondato: %d\n", pi_round);
// Floor (arrotonda per difetto)
int pi_floor =(int)floor(pi);
    printf("Floor: %d\n", pi_floor);
// Ceil (arrotonda per eccesso)
int pi_ceil =(int)ceil(pi);
    printf("Ceil: %d\n", pi_ceil);
return0;
}

Output:
=== LIMITI INT ===
INT_MAX = 2147483647
INT_MIN = -2147483648
Overflow:
max = 2147483647
max + 1 = -2147483648 (overflow!)
Underflow:
#include <stdio.h>
#include <limits.h>
int main(){
    printf("=== LIMITI INT ===\n");
    printf("INT_MAX = %d\n", INT_MAX);
    printf("INT_MIN = %d\n", INT_MIN);
// Overflow
int max = INT_MAX;
    printf("\nOverflow:\n");
    printf("max = %d\n", max);
    printf("max + 1 = %d (overflow!)\n", max +1);
// Underflow
int min = INT_MIN;
    printf("\nUnderflow:\n");
    printf("min = %d\n", min);
    printf("min - 1 = %d (underflow!)\n", min -1);
return0;
}

min = -2147483648
min - 1 = 2147483647 (underflow!)
3.4 Conversione carattere-numero:
Output:
Carattere: '7'
Codice ASCII: 55
Valore numerico: 7
#include <stdio.h>
int main(){
char cifra ='7';
int numero = cifra -'0';
    printf("Carattere: '%c'\n", cifra);
    printf("Codice ASCII: %d\n", cifra);
    printf("Valore numerico: %d\n", numero);
    printf("\n");
// Viceversa
int val =5;
char car = val +'0';
    printf("Numero: %d\n", val);
    printf("Carattere: '%c'\n", car);
    printf("Codice ASCII: %d\n", car);
return0;
}

Numero: 5
Carattere: '5'
Codice ASCII: 53
Esercizio 4: Progetti Completi (45 min)
4.1 Calcolatrice interattiva:
#include <stdio.h>
int main(){
float num1, num2;
char operatore;
float risultato;
    printf("====== CALCOLATRICE ======\n");
    printf("Inserisci primo numero: ");
    scanf("%f", &num1);
    printf("Inserisci operatore (+, -, *, /): ");
    scanf(" %c", &operatore);
    printf("Inserisci secondo numero: ");
    scanf("%f", &num2);
    printf("\n====== CALCOLO ======\n");
if(operatore =='+'){
        risultato = num1 + num2;
        printf("%.2f + %.2f = %.2f\n", num1, num2, risultato);
}elseif(operatore =='-'){
        risultato = num1 - num2;
        printf("%.2f - %.2f = %.2f\n", num1, num2, risultato);
}elseif(operatore =='*'){

4.2 Convertitore temperature:
        risultato = num1 * num2;
        printf("%.2f × %.2f = %.2f\n", num1, num2, risultato);
}elseif(operatore =='/'){
if(num2 !=0){
            risultato = num1 / num2;
            printf("%.2f ÷ %.2f = %.2f\n", num1, num2, risultato);
}else{
            printf("ERRORE: Divisione per zero!\n");
}
}else{
        printf("ERRORE: Operatore non valido!\n");
}
return0;
}
#include <stdio.h>
int main(){
float temperatura;
int scelta;
float celsius, fahrenheit, kelvin;
    printf("====== CONVERTITORE TEMPERATURE ======\n");
    printf("1. Celsius → Fahrenheit e Kelvin\n");
    printf("2. Fahrenheit → Celsius e Kelvin\n");
    printf("3. Kelvin → Celsius e Fahrenheit\n");
    printf("\nScegli opzione (1-3): ");
    scanf("%d", &scelta);
    printf("Inserisci temperatura: ");
    scanf("%f", &temperatura);

4.3 Calcolo scontrino con sconto:
    printf("\n====== RISULTATI ======\n");
if(scelta ==1){
        celsius = temperatura;
        fahrenheit =(celsius *9.0f/5.0f)+32.0f;
        kelvin = celsius +273.15f;
        printf("%.2f°C = %.2f°F = %.2fK\n", celsius, fahrenheit, kelvin);
}elseif(scelta ==2){
        fahrenheit = temperatura;
        celsius =(fahrenheit -32.0f)*5.0f/9.0f;
        kelvin = celsius +273.15f;
        printf("%.2f°F = %.2f°C = %.2fK\n", fahrenheit, celsius, kelvin);
}elseif(scelta ==3){
        kelvin = temperatura;
        celsius = kelvin -273.15f;
        fahrenheit =(celsius *9.0f/5.0f)+32.0f;
        printf("%.2fK = %.2f°C = %.2f°F\n", kelvin, celsius, fahrenheit);
}else{
        printf("Opzione non valida!\n");
}
return0;
}

#include <stdio.h>
int main(){
float prezzo1, prezzo2, prezzo3;
float subtotale, sconto_percentuale, sconto_importo, totale;
    printf("====== CALCOLO SCONTRINO ======\n");
    printf("Prezzo articolo 1: ");
    scanf("%f", &prezzo1);
    printf("Prezzo articolo 2: ");
    scanf("%f", &prezzo2);
    printf("Prezzo articolo 3: ");
    scanf("%f", &prezzo3);
    printf("Percentuale sconto (0-100): ");
    scanf("%f", &sconto_percentuale);
// Calcoli
    subtotale = prezzo1 + prezzo2 + prezzo3;
    sconto_importo = subtotale * sconto_percentuale /100.0f;
    totale = subtotale - sconto_importo;
// Stampa scontrino
    printf("\n====== SCONTRINO ======\n");
    printf("Articolo 1:      %7.2f€\n", prezzo1);
    printf("Articolo 2:      %7.2f€\n", prezzo2);
    printf("Articolo 3:      %7.2f€\n", prezzo3);
    printf("----------------------\n");
    printf("Subtotale:       %7.2f€\n", subtotale);
    printf("Sconto (%.0f%%):   -%6.2f€\n", sconto_percentuale,
sconto_importo);
    printf("======================\n");

Esempio output:
====== CALCOLO SCONTRINO ======
Prezzo articolo 1: 15.50
Prezzo articolo 2: 23.00
Prezzo articolo 3: 8.90
Percentuale sconto (0-100): 10
====== SCONTRINO ======
Articolo 1:        15.50€
Articolo 2:        23.00€
Articolo 3:         8.90€
----------------------
Subtotale:         47.40€
Sconto (10%):      -4.74€
======================
TOTALE:            42.66€
4.4 Conversione unità di misura:
    printf("TOTALE:          %7.2f€\n", totale);
return0;
}
#include <stdio.h>
int main(){
float valore;
int tipo;
    printf("====== CONVERTITORE UNITÀ ======\n");
    printf("1. Metri ↔ Piedi\n");
    printf("2. Chilogrammi ↔ Libbre\n");

4.5 Calcolo prestito bancario:
    printf("3. Chilometri ↔ Miglia\n");
    printf("\nScegli conversione (1-3): ");
    scanf("%d", &tipo);
    printf("Inserisci valore: ");
    scanf("%f", &valore);
    printf("\n====== RISULTATO ======\n");
if(tipo ==1){
float piedi = valore *3.28084f;
        printf("%.2f metri = %.2f piedi\n", valore, piedi);
}elseif(tipo ==2){
float libbre = valore *2.20462f;
        printf("%.2f kg = %.2f libbre\n", valore, libbre);
}elseif(tipo ==3){
float miglia = valore *0.621371f;
        printf("%.2f km = %.2f miglia\n", valore, miglia);
}else{
        printf("Opzione non valida!\n");
}
return0;
}
#include <stdio.h>
#include <math.h>
int main(){

float capitale, tasso_annuo, tasso_mensile;
int durata_mesi;
float rata_mensile, totale_pagato, interessi_totali;
    printf("====== CALCOLO RATA PRESTITO ======\n");
    printf("Capitale richiesto (€): ");
    scanf("%f", &capitale);
    printf("Tasso interesse annuo (%%): ");
    scanf("%f", &tasso_annuo);
    printf("Durata (mesi): ");
    scanf("%d", &durata_mesi);
// Calcolo rata (formula ammortamento francese)
    tasso_mensile = tasso_annuo /100.0f/12.0f;
if(tasso_mensile >0){
        rata_mensile = capitale * tasso_mensile *
                       pow(1+ tasso_mensile, durata_mesi)/
(pow(1+ tasso_mensile, durata_mesi)-1);
}else{
        rata_mensile = capitale / durata_mesi;
}
    totale_pagato = rata_mensile * durata_mesi;
    interessi_totali = totale_pagato - capitale;
    printf("\n====== RIEPILOGO ======\n");
    printf("Capitale:            %10.2f€\n", capitale);
    printf("Tasso annuo:         %9.2f%%\n", tasso_annuo);
    printf("Durata:              %10d mesi\n", durata_mesi);
    printf("-----------------------------------\n");
    printf("Rata mensile:        %10.2f€\n", rata_mensile);
    printf("Totale da pagare:    %10.2f€\n", totale_pagato);

ESERCIZI AUTONOMI
Esercizio 5: Pratica Individuale
5.1 Crea un programma che chiede base e altezza di un triangolo e calcola l’area.
5.2 Scrivi un programma che converte ore, minuti, secondi in secondi totali.
5.3 Crea un programma che calcola il costo di una chiamata telefonica (€/minuto ×
durata).
5.4 Programma che converte una distanza in metri in: km, cm, mm, miglia.
5.5 Calcolo consumo carburante: chiedi km percorsi e litri consumati, calcola km/l e l/
100km.
ESERCIZI DA SVOLGERE A CASA
Homework 1: Scrivi un programma che:
Chiede nome, età, altezza, peso
Calcola IMC
Calcola anno di nascita approssimativo
Stampa un riepilogo formattato
Homework 2: Crea un convertitore valute che:
Chiede importo in Euro
Converte in: Dollari (1€ = 1.10$), Sterline (1€ = 0.85£), Yen (1€ = 160¥)
Stampa tabella con tutte le conversioni
    printf("Interessi totali:    %10.2f€\n", interessi_totali);
return0;
}
• 
• 
• 
• 
• 
• 
• 

Homework 3: Programma calcolo stipendio:
Chiede ore lavorate
Chiede paga oraria
Calcola stipendio lordo
Calcola tasse (23% fino a 1000€, 30% oltre)
Calcola stipendio netto
Stampa dettaglio completo
Homework 4: Calcolatore geometria:
Menu con 3 opzioni: cerchio, rettangolo, triangolo
Per ogni figura: chiede dimensioni necessarie
Calcola perimetro e area
Stampa risultati formattati
Homework 5: Esperimenti con limiti numerici:
Usa <limits.h> e <float.h>
Stampa limiti di tutti i tipi interi
Stampa limiti e precisione dei float
Sperimenta con overflow/underflow
Documenta risultati
Homework 6: Gioco “Indovina l’operazione”:
Programma mostra: “5 ? 3 = 15”
Utente deve indovinare l’operazione (risponde: *, +, -, /)
Programma verifica e comunica se corretto
Usa variabili per numeri e risultato
APPROFONDIMENTI
Rappresentazione Interna dei Tipi
Interi in memoria:
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

int x = 42;
Memoria (32 bit, little-endian):
Indirizzo: 0x1000 0x1001 0x1002 0x1003
Byte:      2A     00     00     00
           ↑      ↑      ↑      ↑
           LSB                  MSB
Binario: 00000000 00000000 00000000 00101010
Float in memoria (IEEE 754):
float f = 3.14f;
Binario: 01000000 01001000 11110101 11000011
         ↓        ↓        ↓          ↓
         Sign  Exponent    Mantissa
Allineamento Memoria (Alignment)
Le variabili sono allineate in memoria per efficienza.
Padding inserito per allineare int a multiplo di 4.
struct esempio {
char c; // 1 byte
// 3 byte padding
int i; // 4 byte
char c2; // 1 byte
// 3 byte padding
};
sizeof(struct esempio)=12 byte (non 6!)

Volatile e Register
volatile: Dice al compilatore di non ottimizzare.
register: Suggerisce di tenere in registro CPU (raramente usato oggi).
Tipi Fixed-Width (C99)
<stdint.h> definisce tipi con dimensione garantita:
RIEPILOGO CONCETTI CHIAVE
Dichiarazione Variabili
volatileint sensor_value;
registerint i;
#include <stdint.h>
int8_t   x;
int16_t  y;
int32_t  z;
int64_t  w;
uint8_t  a;
uint16_t b;
tipo nome;
tipo nome = valore;
const tipo nome = valore;

Tipi Fondamentali
Interi:  char, short, int, long, long long
Float:   float, double, long double
Carattere: char
Booleano: _Bool / bool (C99+)
Input/Output
Conversioni
Operatori Base
TABELLE DI RIFERIMENTO RAPIDO
Tipi Interi (tipici)
Tipo Byte Range Signed Range Unsigned
char 1 -128 a 127 0 a 255
printf("formato", args);
scanf("formato", &var);
(tipo)espressione
tipo var = espressione;
=   assegnazione
sizeof(tipo)  dimensione

Tipo Byte Range Signed Range Unsigned
short 2 -32,768 a 32,767 0 a 65,535
int 4 -2,147,483,648 a 2,147,483,6470 a 4,294,967,295
long 4/8 varia varia
long long 8 -9.2×10¹⁸ a 9.2×10¹⁸ 0 a 1.8×10¹⁹
Specificatori scanf
Tipo Printf Scanf
int %d %d
unsigned %u %u
long %ld %ld
float %f %f
double %f o %lf %lf
char %c %c
string %s %s
Header Files Utili
Header Contenuto
<stdio.h> I/O (printf, scanf)
<stdlib.h> Utility (malloc, rand, exit)
<math.h> Matematica (sqrt, pow, sin)
<string.h> Stringhe (strlen, strcpy)

Header Contenuto
<limits.h> Limiti tipi interi
<float.h> Limiti tipi float
<stdbool.h> bool, true, false
<stdint.h> Tipi fixed-width
PROBLEMI COMUNI E SOLUZIONI
Problema 1: Variabile non inizializzata
Soluzione: Inizializza sempre.
Problema 2: scanf senza &
Soluzione:
int x;
printf("%d\n", x); // Garbage!
int x =0;
int x;
scanf("%d", x); // ERRORE! Manca &
scanf("%d", &x);

Problema 3: Float con scanf
Soluzione:
Problema 4: Divisione intera
Soluzione:
Problema 5: Overflow silenzioso
Soluzione: Usa tipo più grande.
double d;
scanf("%f", &d); // ERRORE! double usa %lf
scanf("%lf", &d);
int a =5, b =2;
float r = a / b; // r = 2.0 (non 2.5!)
float r =(float)a / b;
int big =2000000000;
int bigger = big +1000000000; // Overflow!
longlong bigger =(longlong)big +1000000000;

PUNTI CHIAVE DELLA LEZIONE
✓ Variabile = contenitore per dati in memoria
✓ Tipi base: int, float, double, char
✓ Dichiarazione: tipo nome;Inizializzazione: tipo nome = valore;
✓ scanf() legge input, richiede & prima della variabile
✓ sizeof() restituisce dimensione in byte
✓ Cast(tipo)espressione converte esplicitamente
✓ Divisione intera: int / int = int (tronca decimali)
✓ const rende variabile immutabile
✓ Inizializza sempre le variabili (no garbage)
✓ %lf per double in scanf (non %f)
PREPARAZIONE PER LA PROSSIMA
LEZIONE
Nella prossima lezione studieremo:
Operatori aritmetici: +, -, *, /, %
Operatori di incremento/decremento: ++, –
Operatori relazionali: <, >, ==, !=
Operatori logici: &&, ||, !
Precedenza e associatività
Espressioni complesse
Porta con te:
Esercizi homework completati
Domande su scanf o conversioni
Calcolatrice per verificare calcoli
Esempi di espressioni matematiche complesse
Ottimo lavoro! Ora sai usare variabili e input! 🎯
• 
• 
• 
• 
• 
• 
• 
• 
• 
• 

Nelle prossime lezioni aggiungeremo operatori ed espressioni per creare calcoli
complessi, poi passeremo ai costrutti di controllo (if, while, for) per programmi
veramente potenti!


---

# lezione8 operatori

**File:** `lezione8 operatori.pdf`
**Tipo:** `.pdf`
**Dimensione:** 663.5 KB
**Ultima modifica:** 02/07/2026 09:24

---

LEZIONE 8 - Operatori ed Espressioni
Durata: 4 ore | Teoria: 2h | Esercizi: 2h
PARTE TEORICA (2 ore)
8.1 Introduzione agli Operatori (10 min)
Cos’è un Operatore?
Un 
operatore
 è un simbolo che indica un’operazione da eseguire su uno o più 
operandi
.
Esempio:
Classificazione per Numero di Operandi
1. Operatori Unari
 (1 operando)
2. Operatori Binari
 (2 operandi)
3. Operatori Ternari
 (3 operandi)
Classificazione per Tipo di Operazione
Aritmetici
: +, -, *, /, %
Relazionali
: <, >, <=, >=, ==, !=
Logici
: &&, ||, !
Bitwise
: &, |, ^, ~, <<, >>
Assegnazione
: =, +=, -=, *=, /=, %=
Incremento/Decremento
: ++, –
Altro
: sizeof, ternario (?:), virgola (,)
8.2 Operatori Aritmetici (esempi e note)
Operatori Base
1. Addizione (+)
int
 risultato 
=
 
5
 
+
 
3
;
//              ↑ ↑ ↑
//              │ │ └── operando 2
//              │ └──── operatore
//              └────── operando 1
-
x      
// negazione
++
x     
// incremento
!
x      
// NOT logico
a 
+
 b   
// addizione
a 
>
 b   
// maggiore di
a 
&&
 b  
// AND logico
condizione 
?
 valore_se_vero 
:
 valore_se_falso
int
 a 
=
 
5
 
+
 
3
;
           
// 8
float
 b 
=
 
2.5
 
+
 
1.3
;
     
// 3.8
int
 c 
=
 
-
10
 
+
 
15
;
        
// 5

2. Sottrazione (-)
**3. Moltiplicazione (*)**
4. Divisione (/)
IMPORTANTE: Divisione intera vs reale
5. Modulo (%) - Resto della Divisione
Usi pratici del modulo:
Operatori Unari
Negazione (-)
Positivo (+)
 (raramente usato)
Esempi Completi
Esempio 1: Calcolo media
int
 a 
=
 
10
 
-
 
3
;
          
// 7
float
 b 
=
 
5.5
 
-
 
2.3
;
     
// 3.2
int
 c 
=
 
0
 
-
 
5
;
           
// -5
int
 a 
=
 
4
 
*
 
3
;
           
// 12
float
 b 
=
 
2.5
 
*
 
4.0
;
     
// 10.0
int
 c 
=
 
-
3
 
*
 
5
;
          
// -15
int
 a 
=
 
10
 
/
 
3
;
          
// 3 (divisione intera!)
float
 b 
=
 
10.0
 
/
 
3.0
;
    
// 3.333...
float
 c 
=
 
10.0
 
/
 
3
;
      
// 3.333... (uno float basta)
int
 d 
=
 
10
 
/
 
0
;
          
// ERRORE! Undefined behavior
int
 x 
=
 
7
,
 y 
=
 
2
;
int
 r1 
=
 x 
/
 y
;
           
// 3 (troncamento)
float
 r2 
=
 x 
/
 y
;
         
// 3.0 (divisione intera, poi convertito)
float
 r3 
=
 
(
float
)
x 
/
 y
;
  
// 3.5 (divisione reale) 
✓
int
 a 
=
 
10
 
%
 
3
;
          
// 1 (10 = 3*3 + 1)
int
 b 
=
 
15
 
%
 
4
;
          
// 3 (15 = 4*3 + 3)
int
 c 
=
 
20
 
%
 
5
;
          
// 0 (divisione esatta)
int
 d 
=
 
7
 
%
 
2
;
           
// 1 (pari=0, dispari=1)
// float e = 10.5 % 3.2; // ERRORE! % solo per interi
// Verificare se pari/dispari
if
 
(
n 
%
 
2
 
==
 
0
)
 
{
    printf
(
"Pari
\n
"
);
}
// Ciclare array (wraparound)
int
 indice 
=
 
(
i 
+
 
1
)
 
%
 array_size
;
// Estrarre ultima cifra
int
 ultima_cifra 
=
 numero 
%
 
10
;
// Estrarre cifre
int
 centinaia 
=
 numero 
/
 
100
;
int
 decine 
=
 
(
numero 
/
 
10
)
 
%
 
10
;
int
 unita 
=
 numero 
%
 
10
;
int
 x 
=
 
5
;
int
 y 
=
 
-
x
;
      
// -5
int
 z 
=
 
-(-
x
);
   
// 5
int
 x 
=
 
+
5
;
      
// equivalente a: int x = 5;

Esempio 2: Conversione ore
Esempio 3: Scambio senza variabile temporanea
8.3 Incremento/Decremento
Incremento (++)
Post-incremento (x++)
 - Usa il valore PRIMA, poi incrementa
Pre-incremento (++x)
 - Incrementa PRIMA, poi usa il valore
Confronto:
Decremento (–)
Post-decremento (x–)
Pre-decremento (–x)
Quando Usare Pre vs Post
In espressioni semplici, sono equivalenti:
In espressioni complesse, differiscono:
int
 voto1 
=
 
8
,
 voto2 
=
 
7
,
 voto3 
=
 
9
;
float
 media 
=
 
(
voto1 
+
 voto2 
+
 voto3
)
 
/
 
3.0
;
  
// 8.0
// Nota: 3.0 per divisione reale!
int
 secondi_totali 
=
 
3665
;
int
 ore 
=
 secondi_totali 
/
 
3600
;
      
// 1
int
 minuti 
=
 
(
secondi_totali 
%
 
3600
)
 
/
 
60
;
  
// 1
int
 secondi 
=
 secondi_totali 
%
 
60
;
    
// 5
// Risultato: 1h 1m 5s
int
 a 
=
 
5
,
 b 
=
 
3
;
a 
=
 a 
+
 b
;
  
// a = 8
b 
=
 a 
-
 b
;
  
// b = 5
a 
=
 a 
-
 b
;
  
// a = 3
// Ora: a = 3, b = 5
int
 x 
=
 
5
;
int
 y 
=
 x
++;
  
// y = 5, x = 6
int
 x 
=
 
5
;
int
 y 
=
 
++
x
;
  
// y = 6, x = 6
int
 a 
=
 
5
,
 b 
=
 
5
;
printf
(
"
%d\n
"
,
 a
++);
  
// Stampa: 5, poi a diventa 6
printf
(
"
%d\n
"
,
 a
);
    
// Stampa: 6
printf
(
"
%d\n
"
,
 
++
b
);
  
// b diventa 6, poi stampa: 6
printf
(
"
%d\n
"
,
 b
);
    
// Stampa: 6
int
 x 
=
 
5
;
int
 y 
=
 x
--;
  
// y = 5, x = 4
int
 x 
=
 
5
;
int
 y 
=
 
--
x
;
  
// y = 4, x = 4
x
++;
    
// Incrementa x
++
x
;
    
// Incrementa x (stesso effetto)

Nei cicli (anticipazione):
Errori Comuni
ERRORE: Usare ++ su espressioni
ERRORE: Doppio incremento
Best Practice:
 - Usa ++ e – su righe separate quando possibile - Evita espressioni
complesse con effetti collaterali - In caso di dubbio, scrivi più chiaramente
8.4 Relazionali
Gli operatori 
relazionali
 confrontano due valori e restituiscono 
1
 (vero) o 
0
 (falso).
Operatori di Confronto
1. Uguale a (==)
ATTENZIONE:
 Non confondere 
==
 (confronto) con 
=
 (assegnazione)!
2. Diverso da (!=)
3. Maggiore di (>)
4. Minore di (<)
int
 i 
=
 
0
;
int
 array
[
10
];
array
[
i
++]
 
=
 
5
;
  
// array[0] = 5, poi i diventa 1
array
[++
i
]
 
=
 
7
;
  
// i diventa 2, poi array[2] = 7
// Equivalenti:
for
 
(
i 
=
 
0
;
 i 
<
 
10
;
 i
++)
   
// ...
for
 
(
i 
=
 
0
;
 i 
<
 
10
;
 
++
i
)
   
// ...
// Preferenza: ++i (leggermente più efficiente in C++)
int
 x 
=
 
5
,
 y 
=
 
3
;
(
x 
+
 y
)++;
     
// ERRORE! Non è un l-value
++(
x 
+
 y
);
     
// ERRORE!
int
 x 
=
 
5
;
int
 y 
=
 x
++
 
+
 
++
x
;
  
// UNDEFINED BEHAVIOR! Evitare!
int
 a 
=
 
5
,
 b 
=
 
5
,
 c 
=
 
3
;
int
 r1 
=
 
(
a 
==
 b
);
  
// 1 (vero)
int
 r2 
=
 
(
a 
==
 c
);
  
// 0 (falso)
int
 x 
=
 
5
;
if
 
(
x 
=
 
10
)
 
{
        
// 
BUG
! Assegna 10 a x, sempre vero
    printf
(
"Oops
\n
"
);
}
if
 
(
x 
==
 
10
)
 
{
       
// Corretto: confronta
    printf
(
"OK
\n
"
);
}
int
 a 
=
 
5
,
 b 
=
 
3
;
int
 r 
=
 
(
a 
!=
 b
);
    
// 1 (vero, sono diversi)
int
 a 
=
 
10
,
 b 
=
 
5
;
int
 r 
=
 
(
a 
>
 b
);
     
// 1 (vero)
int
 a 
=
 
3
,
 b 
=
 
7
;
int
 r 
=
 
(
a 
<
 b
);
     
// 1 (vero)

5. Maggiore o uguale (>=)
6. Minore o uguale (<=)
Comparazione con Float
PROBLEMA:
 Float hanno errori di arrotondamento!
Confronto Caratteri
Espressioni Relazionali
8.5 Logici
Gli operatori 
logici
 combinano espressioni booleane.
AND Logico (&&)
Vero solo se ENTRAMBI gli operandi sono veri.
int
 a 
=
 
5
,
 b 
=
 
5
;
int
 r1 
=
 
(
a 
>=
 b
);
   
// 1 (vero, sono uguali)
int
 r2 
=
 
(
a 
>=
 
3
);
   
// 1 (vero, 5 >= 3)
int
 a 
=
 
5
,
 b 
=
 
10
;
int
 r 
=
 
(
a 
<=
 b
);
    
// 1 (vero)
float
 a 
=
 
0
.1
 
+
 
0
.2
;
float
 b 
=
 
0
.3
;
if
 
(
a 
==
 b
)
 
{
                     
// Probabilmente FALSO!
    printf
(
"Uguali
\n
"
);
}
// SOLUZIONE: Usa epsilon (tolleranza)
#include 
<math.h>
#define EPSILON 
0
.00001
if
 
(
fabs
(
a 
-
 b
)
 
<
 EPSILON
)
 
{
      
// Corretto
    printf
(
"Uguali (entro tolleranza)
\n
"
);
}
char
 c1 
=
 
'A'
,
 c2 
=
 
'B'
;
if
 
(
c1 
<
 c2
)
 
{
  
// Vero (confronta codici ASCII: 65 < 66)
    printf
(
"A viene prima di B
\n
"
);
}
// Controlli utili
char
 ch 
=
 
'g'
;
if
 
(
ch 
>=
 
'a'
 
&&
 ch 
<=
 
'z'
)
 
{
    printf
(
"Lettera minuscola
\n
"
);
}
int
 eta 
=
 
25
;
char
 tessera 
=
 
'S'
;
  
// S = ha tessera, N = no
int
 prezzo_pieno 
=
 
10
;
// Sconto solo se: (età < 18 o età > 65) E ha tessera
if
 
((
eta 
<
 
18
 
||
 eta 
>
 
65
)
 
&&
 tessera 
==
 
'S'
)
 
{
    
int
 prezzo 
=
 prezzo_pieno 
/
 
2
;
    printf
(
"Prezzo ridotto: 
%d
€
\n
"
,
 prezzo
);
}
 
else
 
{
    printf
(
"Prezzo pieno: 
%d
€
\n
"
,
 prezzo_pieno
);
}

Tabella verità:
A     B     A && B
------------------------
0     0       0
0     1       0
1     0       0
1     1       1
Esempi:
Short-circuit evaluation:
OR Logico (||)
Vero se ALMENO UNO degli operandi è vero.
Tabella verità:
A     B     A || B
------------------------
0     0       0
0     1       1
1     0       1
1     1       1
Esempi:
Short-circuit:
int
 a 
=
 
5
,
 b 
=
 
10
;
if
 
(
a 
>
 
0
 
&&
 b 
>
 
0
)
 
{
            
// Vero
    printf
(
"Entrambi positivi
\n
"
);
}
if
 
(
a 
>
 
0
 
&&
 b 
<
 
5
)
 
{
            
// Falso (b < 5 è falso)
    printf
(
"Non stampato
\n
"
);
}
// Controllo range
int
 x 
=
 
50
;
if
 
(
x 
>=
 
0
 
&&
 x 
<=
 
100
)
 
{
    printf
(
"x è tra 0 e 100
\n
"
);
}
int
 x 
=
 
0
;
if
 
(
x 
!=
 
0
 
&&
 
(
10
 
/
 x
)
 
>
 
2
)
 
{
    
// Sicuro! Se x=0, non valuta 10/x
    printf
(
"OK
\n
"
);
}
char
 ch 
=
 
'A'
;
if
 
(
ch 
==
 
'a'
 
||
 ch 
==
 
'A'
)
 
{
    
// Vero
    printf
(
"È la lettera A
\n
"
);
}
// Controllo multiplo
int
 giorno 
=
 
6
;
if
 
(
giorno 
==
 
6
 
||
 giorno 
==
 
7
)
 
{
    printf
(
"È weekend!
\n
"
);
}
// Validazione
int
 voto 
=
 
110
;
if
 
(
voto 
<
 
0
 
||
 voto 
>
 
100
)
 
{
    printf
(
"Voto non valido
\n
"
);
}

NOT Logico (!)
Inverte il valore booleano.
Tabella verità:
A     !A
-----------
0      1
1      0
Esempi:
Combinazioni Complesse
Leggi di De Morgan
Equivalenze utili:
Valori di Verità in C
In C, 
qualsiasi valore diverso da 0 è considerato vero
.
if
 
(
x 
==
 
0
 
||
 
(
10
 
/
 x
)
 
>
 
2
)
 
{
    
// Se x=0, non valuta 10/x
    printf
(
"OK
\n
"
);
}
int
 x 
=
 
0
;
int
 y 
=
 
!
x
;
      
// y = 1 (NOT di 0)
int
 a 
=
 
5
;
int
 b 
=
 
!
a
;
      
// b = 0 (NOT di qualsiasi numero != 0)
// Verifica negativa
if
 
(!(
x 
>
 
10
))
 
{
    printf
(
"x NON è maggiore di 10
\n
"
);
}
// Equivalente a:
if
 
(
x 
<=
 
10
)
 
{
    printf
(
"x è minore o uguale a 10
\n
"
);
}
int
 eta 
=
 
25
;
char
 tessera 
=
 
'S'
;
  
// S = ha tessera, N = no
int
 prezzo_pieno 
=
 
10
;
// Sconto solo se: (età < 18 o età > 65) E ha tessera
if
 
((
eta 
<
 
18
 
||
 eta 
>
 
65
)
 
&&
 tessera 
==
 
'S'
)
 
{
    
int
 prezzo 
=
 prezzo_pieno 
/
 
2
;
    printf
(
"Prezzo ridotto: 
%d
€
\n
"
,
 prezzo
);
}
 
else
 
{
    printf
(
"Prezzo pieno: 
%d
€
\n
"
,
 prezzo_pieno
);
}
!(
A 
&&
 B
)
  ≡  
!
A 
||
 
!
B
!(
A 
||
 B
)
  ≡  
!
A 
&&
 
!
B
// Esempio:
// "Non è vero che piove E fa freddo"
// equivale a:
// "Non piove O non fa freddo"

8.6 Assegnazione composta
Gli operatori 
composti
 combinano operazione e assegnazione.
Operatori Disponibili
Esempi Base
Addizione composta (+=)
Sottrazione composta (-=)
**Moltiplicazione composta (*=)**
Divisione composta (/=)
Modulo composto (%=)
Confronto Forme
int
 a 
=
 
5
;
if
 
(
a
)
 
{
             
// Vero! (5 != 0)
    printf
(
"a è vero
\n
"
);
}
int
 b 
=
 
0
;
if
 
(
b
)
 
{
             
// Falso
    printf
(
"Non stampato
\n
"
);
}
if
 
(!
b
)
 
{
            
// Vero! (NOT di 0)
    printf
(
"b è falso
\n
"
);
}
+=
   
-=
   
*=
   
/=
   
%=
   
&=
   
|=
   
^=
   
<<=
   
>>=
int
 x 
=
 
10
;
x 
+=
 
5
;
      
// Equivalente a: x = x + 5;
// x = 15
int
 x 
=
 
20
;
x 
-=
 
3
;
      
// Equivalente a: x = x - 3;
// x = 17
int
 x 
=
 
4
;
x 
*=
 
3
;
      
// Equivalente a: x = x * 3;
// x = 12
int
 x 
=
 
20
;
x 
/=
 
4
;
      
// Equivalente a: x = x / 4;
// x = 5
int
 x 
=
 
17
;
x 
%=
 
5
;
      
// Equivalente a: x = x % 5;
// x = 2
// Forma lunga
x 
=
 x 
+
 
10
;
y 
=
 y 
*
 
2
;
z 
=
 z 
/
 
3
;
// Forma compatta (preferita)
x 
+=
 
10
;
y 
*=
 
2
;
z 
/=
 
3
;

Vantaggi
1. Più conciso
2. Più efficiente (teoricamente)
3. Meno errori
Esempi Pratici
Contatore:
Accumulo:
Moltiplicazione per potenze di 2:
8.7 Ternario
L’
operatore ternario
 (?:) è l’unico operatore con 3 operandi.
Sintassi
Esempi Base
Assegnazione condizionale:
In printf:
Calcolo assoluto:
lunghissimo_nome_variabile 
=
 lunghissimo_nome_variabile 
+
 
5
;
lunghissimo_nome_variabile 
+=
 
5
;
  
// Più leggibile
array
[
funzione_complessa
(
x
)]
 
=
 array
[
funzione_complessa
(
x
)]
 
+
 
1
;
array
[
funzione_complessa
(
x
)]
 
+=
 
1
;
  
// Valuta indice una sola volta
x 
=
 y 
+
 
1
;
    
// Intendevi x = x + 1? Errore comune
x 
+=
 
1
;
       
// Chiaro!
int
 contatore 
=
 
0
;
contatore 
+=
 
1
;
  
// oppure: contatore++
float
 totale 
=
 
0
.0
;
for
 
(
int
 i 
=
 
0
;
 i 
<
 n
;
 i
++)
 
{
    totale 
+=
 array
[
i
];
}
x 
=
 x 
<<
 
3
;
  
// x = x * 8  (più veloce di x *= 8)
x 
=
 x 
>>
 
2
;
  
// x = x / 4  (più veloce di x /= 4)
condizione 
?
 valore_se_vero 
:
 valore_se_falso
int
 a 
=
 
10
,
 b 
=
 
20
;
int
 max 
=
 
(
a 
>
 b
)
 
?
 a 
:
 b
;
   
// max = 20
// Equivalente a:
int
 max
;
if
 
(
a 
>
 b
)
 
{
    max 
=
 a
;
}
 
else
 
{
    max 
=
 b
;
}
int
 eta 
=
 
17
;
printf
(
"Sei 
%s\n
"
,
 
(
eta 
>=
 
18
)
 
?
 
"maggiorenne"
 
:
 
"minorenne"
);

Ternario Annidato
Possibile ma sconsigliato:
Meglio usare if-else per chiarezza:
Quando Usare il Ternario
✓
✓
 BUONO (semplice, leggibile):
✗
✗
 CATTIVO (complesso, illeggibile):
8.8 Precedenza e Associatività
La 
precedenza
 determina l’ordine di valutazione degli operatori.
Tabella Precedenza (dal più alto al più basso)
Livello
Operatori
Descrizione
Associatività
1
() [] . ->
Parentesi, accesso
L→R
2
! ~ ++ – + - * & (cast)
sizeof
Unari
R→L
3
* / %
Moltiplicazione, divisione,
modulo
L→R
4
+ -
Addizione, sottrazione
L→R
5
<< >>
Shift bit
L→R
6
< <= > >=
Relazionali
L→R
7
== !=
Uguaglianza
L→R
8
&
AND bitwise
L→R
9
^
XOR bitwise
L→R
10
|
OR bitwise
L→R
11
&&
AND logico
L→R
12
||
OR logico
L→R
13
?:
Ternario
R→L
14
= += -= *= /= %= etc.
Assegnazione
R→L
15
,
Virgola
L→R
Esempi Precedenza
int
 x 
=
 
-
5
;
int
 abs_x 
=
 
(
x 
<
 
0
)
 
?
 
-
x 
:
 x
;
  
// abs_x = 5
int
 voto 
=
 
85
;
char
 
*
valutazione 
=
 
(
voto 
>=
 
90
)
 
?
 
"Ottimo"
 
:
                    
(
voto 
>=
 
80
)
 
?
 
"Buono"
 
:
                    
(
voto 
>=
 
70
)
 
?
 
"Discreto"
 
:
                    
(
voto 
>=
 
60
)
 
?
 
"Sufficiente"
 
:
 
"Insufficiente"
;
if
 
(
voto 
>=
 
90
)
 
{
    valutazione 
=
 
"Ottimo"
;
}
 
else
 
if
 
(
voto 
>=
 
80
)
 
{
    valutazione 
=
 
"Buono"
;
}
 
// ...
int
 max 
=
 
(
a 
>
 b
)
 
?
 a 
:
 b
;
int
 segno 
=
 
(
x 
<
 
0
)
 
?
 
-
1
 
:
 
1
;
printf
(
"
%d\n
"
,
 
(
n 
%
 
2
 
==
 
0
)
 
?
 
0
 
:
 
1
);
int
 x 
=
 
(
a 
>
 b
)
 
?
 
(
c 
>
 d
)
 
?
 
(
e 
>
 f
)
 
?
 
1
 
:
 
2
 
:
 
3
 
:
 
4
;
  
// Confuso!

Aritmetica:
Con parentesi (override precedenza):
Relazionali e logici:
Assegnazione:
Associatività
Left-to-Right (L→R):
Right-to-Left (R→L):
Best Practices
1. Usa parentesi quando in dubbio:
2. Non affidarti troppo alla precedenza:
3. Una operazione per riga (quando complesso):
int
 x 
=
 
2
 
+
 
3
 
*
 
4
;
       
// x = 14 (non 20!)
// Equivalente a: 2 + (3 * 4)
int
 y 
=
 
10
 
-
 
4
 
/
 
2
;
      
// y = 8 (non 3!)
// Equivalente a: 10 - (4 / 2)
int
 x 
=
 
(
2
 
+
 
3
)
 
*
 
4
;
     
// x = 20
int
 y 
=
 
(
10
 
-
 
4
)
 
/
 
2
;
    
// y = 3
int
 a 
=
 
5
,
 b 
=
 
10
,
 c 
=
 
3
;
if
 
(
a 
<
 b 
&&
 b 
>
 c
)
 
{
    
// OK: relazionali prima di &&
    printf
(
"Vero
\n
"
);
}
// Senza &&, avremmo bisogno di parentesi:
int
 result 
=
 a 
<
 b 
>
 c
;
  
// Confuso! Usa parentesi
int
 result 
=
 
(
a 
<
 b
)
 
&&
 
(
b 
>
 c
);
  
// Chiaro
int
 x
,
 y
,
 z
;
x 
=
 y 
=
 z 
=
 
5
;
           
// Associatività R→L
// Equivalente a: x = (y = (z = 5));
int
 x 
=
 
10
 
-
 
5
 
-
 
2
;
      
// (10 - 5) - 2 = 3
int
 y 
=
 
20
 
/
 
4
 
/
 
2
;
      
// (20 / 4) / 2 = 2
int
 x 
=
 
5
;
x 
=
 x 
+
 
1
;
               
// R→L per =
// Non confondere con: (x = x) + 1
int
 
*
p 
=
 
&
x
;
             
// R→L per unari
// Poco chiaro
if
 
(
a 
&&
 b 
||
 c 
&&
 d
)
 
{
 
}
// Chiaro
if
 
((
a 
&&
 b
)
 
||
 
(
c 
&&
 d
))
 
{
 
}
// Funziona ma poco leggibile
int
 result 
=
 a 
*
 b 
+
 c 
/
 d 
-
 e
;
// Meglio
int
 temp 
=
 b 
*
 c
;
int
 result 
=
 a 
+
 
(
temp 
/
 d
)
 
-
 
(
e 
%
 f
);

8.9 Bitwise (panoramica)
Gli operatori 
bitwise
 lavorano sui singoli bit.
Operatori Disponibili
AND Bitwise (&)
Bit a bit: 1 solo se ENTRAMBI i bit sono 1.
OR Bitwise (|)
Bit a bit: 1 se ALMENO UNO dei bit è 1.
XOR Bitwise (^)
Bit a bit: 1 se i bit sono DIVERSI.
NOT Bitwise (~)
Inverte tutti i bit (complemento a 1).
// Difficile
int
 result 
=
 a 
*
 b 
+
 c 
/
 d 
-
 e
;
// Più chiaro
int
 prod 
=
 a 
*
 b
;
int
 quo 
=
 c 
/
 d
;
int
 result 
=
 prod 
+
 quo 
-
 e
;
&
    AND bitwise
|
    OR bitwise
^
    XOR bitwise 
(
OR esclusivo
)
~
    NOT bitwise 
(
complemento
)
<<
   Shift left
>>
   Shift right
int
 a 
=
 
12
;
  
// 1100
int
 b 
=
 
10
;
  
// 1010
int
 c 
=
 a 
&
 b
;
  
// 1000 = 8
// Uso: mascherare bit
int
 flags 
=
 
0b11010110
;
int
 bit3 
=
 
(
flags 
&
 
0b00001000
)
 
!=
 
0
;
  
// Testa bit 3
int
 a 
=
 
12
;
  
// 1100
int
 b 
=
 
10
;
  
// 1010
int
 c 
=
 a 
|
 b
;
  
// 1110 = 14
// Uso: settare bit
flags 
=
 flags 
|
 
0b00001000
;
  
// Setta bit 3
// oppure: flags |= 0b00001000;
int
 a 
=
 
12
;
  
// 1100
int
 b 
=
 
10
;
  
// 1010
int
 c 
=
 a 
^
 b
;
  
// 0110 = 6
// Uso: toggle bit
flags 
=
 flags 
^
 
0b00001000
;
  
// Inverte bit 3
// Swap senza variabile temp
a 
=
 a 
^
 b
;
b 
=
 a 
^
 b
;
a 
=
 a 
^
 b
;

Shift Left (<<)
Sposta bit a sinistra (equivale a moltiplicare per 2ⁿ).
Shift Right (>>)
Sposta bit a destra (equivale a dividere per 2ⁿ).
Nota:
 Con numeri signed negativi, >> può inserire 1 a sinistra (arithmetic shift) o 0 (logical
shift) - dipende dall’implementazione.
Applicazioni Pratiche
Moltiplicazione/divisione veloce per potenze di 2:
Maschere e flag:
PARTE PRATICA (2 ore)
ESERCIZI GUIDATI
Esercizio 1: Operatori Aritmetici (20 min)
1.1 Calcolatrice completa (programma corretto e completo)
int
 a 
=
 
12
;
   
// 00001100 (8 bit)
int
 b 
=
 
~
a
;
   
// 11110011 = -13 (complemento a 2)
int
 a 
=
 
5
;
      
// 00000101
int
 b 
=
 a 
<<
 
1
;
 
// 00001010 = 10 (5 * 2)
int
 c 
=
 a 
<<
 
2
;
 
// 00010100 = 20 (5 * 4)
int
 a 
=
 
20
;
     
// 00010100
int
 b 
=
 a 
>>
 
1
;
 
// 00001010 = 10 (20 / 2)
int
 c 
=
 a 
>>
 
2
;
 
// 00000101 = 5  (20 / 4)
x 
=
 x 
<<
 
3
;
  
// x = x * 8  (più veloce di x *= 8)
x 
=
 x 
>>
 
2
;
  
// x = x / 4  (più veloce di x /= 4)
#define FLAG_A 
0x01
  
// 00000001
#define FLAG_B 
0x02
  
// 00000010
#define FLAG_C 
0x04
  
// 00000100
int
 flags 
=
 
0
;
flags 
|=
 FLAG_A
;
     
// Setta FLAG_A
flags 
|=
 FLAG_C
;
     
// Setta FLAG_C
if
 
(
flags 
&
 FLAG_A
)
 
{
  
// Testa FLAG_A
    printf
(
"FLAG_A è settato
\n
"
);
}
flags 
&=
 
~
FLAG_A
;
    
// Cancella FLAG_A

1.2 Conversione tempo:
Esempio output:
Inserisci secondi totali: 3725
3725 secondi = 1 ore, 2 minuti, 5 secondi
1.3 Divisione intera vs reale:
#include 
<stdio.h>
int
 main
()
 
{
    
float
 a
,
 b
;
    
    printf
(
"Inserisci primo numero: "
);
    
if
 
(
scanf
(
"
%f
"
,
 
&
a
)
 
!=
 
1
)
 
return
 
1
;
    
    printf
(
"Inserisci secondo numero: "
);
    
if
 
(
scanf
(
"
%f
"
,
 
&
b
)
 
!=
 
1
)
 
return
 
1
;
    
    printf
(
"
\n
=== RISULTATI ===
\n
"
);
    printf
(
"
%.2f
 + 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 a 
+
 b
);
    printf
(
"
%.2f
 - 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 a 
-
 b
);
    printf
(
"
%.2f
 × 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 a 
*
 b
);
    
    
// Divisione con controllo per divisione per zero
    
if
 
(
b 
!=
 
0
.0f
)
 
{
        printf
(
"
%.2f
 ÷ 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 a 
/
 b
);
    
}
 
else
 
{
        printf
(
"
%.2f
 ÷ 
%.2f
 = ERRORE (divisione per zero)
\n
"
,
 a
,
 b
);
    
}
    
    
// Modulo: solo per interi (mostriamo conversione esplicita)
    
{
        
int
 ia 
=
 
(
int
)
a
;
        
int
 ib 
=
 
(
int
)
b
;
        
if
 
(
ib 
!=
 
0
)
 
{
            printf
(
"
%d
 
%%
 
%d
 = 
%d\n
"
,
 ia
,
 ib
,
 ia 
%
 ib
);
        
}
 
else
 
{
            printf
(
"
%d
 
%%
 
%d
 = ERRORE (divisione per zero)
\n
"
,
 ia
,
 ib
);
        
}
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 secondi_totali
;
    
int
 ore
,
 minuti
,
 secondi
;
    
    printf
(
"Inserisci secondi totali: "
);
    scanf
(
"
%d
"
,
 
&
secondi_totali
);
    
    ore 
=
 secondi_totali 
/
 
3600
;
    minuti 
=
 
(
secondi_totali 
%
 
3600
)
 
/
 
60
;
    secondi 
=
 secondi_totali 
%
 
60
;
    
    printf
(
"
%d
 secondi = 
%d
 ore, 
%d
 minuti, 
%d
 secondi
\n
"
,
           secondi_totali
,
 ore
,
 minuti
,
 secondi
);
    
    
return
 
0
;
}

Esercizio 2: Incremento e Decremento (20 min)
2.1
 Differenza pre/post incremento:
Output:
#include 
<stdio.h>
int
 main
()
 
{
    
int
 dividendo
,
 divisore
;
    
    printf
(
"Dividendo: "
);
    scanf
(
"
%d
"
,
 
&
dividendo
);
    
    printf
(
"Divisore: "
);
    scanf
(
"
%d
"
,
 
&
divisore
);
    
    
if
 
(
divisore 
==
 
0
)
 
{
        printf
(
"ERRORE: Divisione per zero!
\n
"
);
        
return
 
1
;
    
}
    
    
int
 quoziente 
=
 dividendo 
/
 divisore
;
    
int
 resto 
=
 dividendo 
%
 divisore
;
    
float
 risultato_reale 
=
 
(
float
)
dividendo 
/
 divisore
;
    
    printf
(
"
\n
=== DIVISIONE INTERA ===
\n
"
);
    printf
(
"
%d
 ÷ 
%d
 = 
%d
 (quoziente)
\n
"
,
 dividendo
,
 divisore
,
 quoziente
);
    printf
(
"
%d
 
%%
 
%d
 = 
%d
 (resto)
\n
"
,
 dividendo
,
 divisore
,
 resto
);
    
    printf
(
"
\n
=== DIVISIONE REALE ===
\n
"
);
    printf
(
"
%d
 ÷ 
%d
 = 
%.4f\n
"
,
 dividendo
,
 divisore
,
 risultato_reale
);
    
    
// Verifica
    printf
(
"
\n
Verifica: 
%d
 × 
%d
 + 
%d
 = 
%d\n
"
,
           quoziente
,
 divisore
,
 resto
,
 quoziente 
*
 divisore 
+
 resto
);
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 x 
=
 
5
,
 y 
=
 
5
;
    
    printf
(
"Valori iniziali: x = 
%d
, y = 
%d\n\n
"
,
 x
,
 y
);
    
    
// Post-incremento
    printf
(
"Post-incremento (x++):
\n
"
);
    printf
(
"Valore di x++: 
%d\n
"
,
 x
++);
  
// Stampa 5
    printf
(
"Valore di x dopo: 
%d\n\n
"
,
 x
);
  
// Ora è 6
    
    
// Pre-incremento
    printf
(
"Pre-incremento (++y):
\n
"
);
    printf
(
"Valore di ++y: 
%d\n
"
,
 
++
y
);
  
// Stampa 6
    printf
(
"Valore di y dopo: 
%d\n
"
,
 y
);
  
// Ancora 6
    
    
return
 
0
;
}

Valori iniziali: x = 5, y = 5
Post-incremento (x++):
Valore di x++: 5
Valore di x dopo: 6
Pre-incremento (++y):
Valore di ++y: 6
Valore di y dopo: 6
2.2
 Contatore con incremento:
2.3
 Esercizio pratico - conto alla rovescia:
Esercizio 3: Operatori Relazionali e Logici (25 min)
3.1
 Controllo età per cinema:
#include 
<stdio.h>
int
 main
()
 
{
    
int
 contatore 
=
 
0
;
    
    printf
(
"Contatore iniziale: 
%d\n
"
,
 contatore
);
    
    contatore
++;
    printf
(
"Dopo contatore++: 
%d\n
"
,
 contatore
);
    
    
++
contatore
;
    printf
(
"Dopo ++contatore: 
%d\n
"
,
 contatore
);
    
    contatore 
+=
 
5
;
    printf
(
"Dopo contatore += 5: 
%d\n
"
,
 contatore
);
    
    contatore
--;
    printf
(
"Dopo contatore--: 
%d\n
"
,
 contatore
);
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 n
;
    
    printf
(
"Inserisci numero per conto alla rovescia: "
);
    scanf
(
"
%d
"
,
 
&
n
);
    
    printf
(
"
\n
Conto alla rovescia:
\n
"
);
    
while
 
(
n 
>
 
0
)
 
{
        printf
(
"
%d
...
\n
"
,
 n
);
        n
--;
  
// o --n, stesso effetto qui
    
}
    printf
(
"ZERO!
\n
"
);
    
    
return
 
0
;
}

3.2
 Validazione password (semplice):
#include 
<stdio.h>
int
 main
()
 
{
    
int
 eta
;
    
char
 tessera
;
    
    printf
(
"Inserisci età: "
);
    scanf
(
"
%d
"
,
 
&
eta
);
    
    printf
(
"Hai tessera fedeltà? (S/N): "
);
    scanf
(
" 
%c
"
,
 
&
tessera
);
    
    
float
 prezzo 
=
 
10.0
;
  
// Prezzo base
    
    printf
(
"
\n
=== CALCOLO BIGLIETTO ===
\n
"
);
    
    
// Bambini (< 12) e anziani (> 65): sconto 50%
    
if
 
(
eta 
<
 
12
 
||
 eta 
>
 
65
)
 
{
        prezzo 
=
 prezzo 
*
 
0
.5
;
        printf
(
"Sconto età: -50
%%\n
"
);
    
}
    
    
// Sconto tessera: ulteriore 10%
    
if
 
(
tessera 
==
 
'S'
 
||
 tessera 
==
 
's'
)
 
{
        prezzo 
=
 prezzo 
*
 
0
.9
;
        printf
(
"Sconto tessera: -10
%%\n
"
);
    
}
    
    printf
(
"Prezzo finale: 
%.2f
€
\n
"
,
 prezzo
);
    
    
return
 
0
;
}

3.3
 Controllo triangolo (dati 3 lati):
#include 
<stdio.h>
int
 main
()
 
{
    
int
 lunghezza
;
    
char
 ha_maiuscola
,
 ha_numero
;
    
    printf
(
"=== VERIFICA PASSWORD ===
\n
"
);
    printf
(
"Lunghezza password: "
);
    scanf
(
"
%d
"
,
 
&
lunghezza
);
    
    printf
(
"Contiene almeno una maiuscola? (S/N): "
);
    scanf
(
" 
%c
"
,
 
&
ha_maiuscola
);
    
    printf
(
"Contiene almeno un numero? (S/N): "
);
    scanf
(
" 
%c
"
,
 
&
ha_numero
);
    
    
// Password valida se:
    
// - Lunghezza >= 8 E
    
// - Ha maiuscola E
    
// - Ha numero
    
int
 valida 
=
 
(
lunghezza 
>=
 
8
)
 
&&
 
                 
(
ha_maiuscola 
==
 
'S'
 
||
 ha_maiuscola 
==
 
's'
)
 
&&
                 
(
ha_numero 
==
 
'S'
 
||
 ha_numero 
==
 
's'
);
    
    printf
(
"
\n
"
);
    
if
 
(
valida
)
 
{
        printf
(
"
✓
 Password VALIDA
\n
"
);
    
}
 
else
 
{
        printf
(
"
✗
 Password NON VALIDA
\n
"
);
        
        
if
 
(
lunghezza 
<
 
8
)
 
{
            printf
(
"  - Deve essere almeno 8 caratteri
\n
"
);
        
}
        
if
 
(
ha_maiuscola 
!=
 
'S'
 
&&
 ha_maiuscola 
!=
 
's'
)
 
{
            printf
(
"  - Deve contenere una maiuscola
\n
"
);
        
}
        
if
 
(
ha_numero 
!=
 
'S'
 
&&
 ha_numero 
!=
 
's'
)
 
{
            printf
(
"  - Deve contenere un numero
\n
"
);
        
}
    
}
    
    
return
 
0
;
}

3.4
 Anno bisestile:
Esercizio 4: Operatori Composti e Ternario (20 min)
4.1
 Uso operatori composti:
#include 
<stdio.h>
int
 main
()
 
{
    
float
 a
,
 b
,
 c
;
    
    printf
(
"Inserisci i tre lati del triangolo:
\n
"
);
    printf
(
"Lato 1: "
);
    scanf
(
"
%f
"
,
 
&
a
);
    printf
(
"Lato 2: "
);
    scanf
(
"
%f
"
,
 
&
b
);
    printf
(
"Lato 3: "
);
    scanf
(
"
%f
"
,
 
&
c
);
    
    
// Disuguaglianza triangolare:
    
// La somma di due lati deve essere > del terzo
    
int
 valido 
=
 
(
a 
+
 b 
>
 c
)
 
&&
 
(
a 
+
 c 
>
 b
)
 
&&
 
(
b 
+
 c 
>
 a
);
    
    
if
 
(
valido
)
 
{
        printf
(
"
\n
✓
 Può formare un triangolo valido
\n
"
);
        
        
// Classificazione
        
if
 
(
a 
==
 b 
&&
 b 
==
 c
)
 
{
            printf
(
"Tipo: EQUILATERO
\n
"
);
        
}
 
else
 
if
 
(
a 
==
 b 
||
 b 
==
 c 
||
 a 
==
 c
)
 
{
            printf
(
"Tipo: ISOSCELE
\n
"
);
        
}
 
else
 
{
            printf
(
"Tipo: SCALENO
\n
"
);
        
}
    
}
 
else
 
{
        printf
(
"
\n
✗
 NON può formare un triangolo valido
\n
"
);
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 anno
;
    
    printf
(
"Inserisci anno: "
);
    scanf
(
"
%d
"
,
 
&
anno
);
    
    
// Regole anno bisestile:
    
// - Divisibile per 4 E
    
// - (NON divisibile per 100 O divisibile per 400)
    
    
int
 bisestile 
=
 
(
anno 
%
 
4
 
==
 
0
)
 
&&
 
                    
((
anno 
%
 
100
 
!=
 
0
)
 
||
 
(
anno 
%
 
400
 
==
 
0
));
    
    
if
 
(
bisestile
)
 
{
        printf
(
"
%d
 è BISESTILE (366 giorni)
\n
"
,
 anno
);
    
}
 
else
 
{
        printf
(
"
%d
 NON è bisestile (365 giorni)
\n
"
,
 anno
);
    
}
    
    
return
 
0
;
}

Output:
Valore iniziale: x = 10
Dopo x += 5:  x = 15
Dopo x -= 3:  x = 12
Dopo x *= 2:  x = 24
Dopo x /= 4:  x = 6
Dopo x %= 5:  x = 1
4.2
 Operatore ternario - esempi pratici:
4.3
 Calcolo sconto con ternario:
#include 
<stdio.h>
int
 main
()
 
{
    
int
 x 
=
 
10
;
    
    printf
(
"Valore iniziale: x = 
%d\n\n
"
,
 x
);
    
    x 
+=
 
5
;
    printf
(
"Dopo x += 5:  x = 
%d\n
"
,
 x
);
    
    x 
-=
 
3
;
    printf
(
"Dopo x -= 3:  x = 
%d\n
"
,
 x
);
    
    x 
*=
 
2
;
    printf
(
"Dopo x *= 2:  x = 
%d\n
"
,
 x
);
    
    x 
/=
 
4
;
    printf
(
"Dopo x /= 4:  x = 
%d\n
"
,
 x
);
    
    x 
%=
 
5
;
    printf
(
"Dopo x 
%%
= 5:  x = 
%d\n
"
,
 x
);
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 a 
=
 
15
,
 b 
=
 
20
;
    
    
// Massimo tra due numeri
    
int
 max 
=
 
(
a 
>
 b
)
 
?
 a 
:
 b
;
    printf
(
"Massimo tra 
%d
 e 
%d
: 
%d\n
"
,
 a
,
 b
,
 max
);
    
    
// Minimo tra due numeri
    
int
 min 
=
 
(
a 
<
 b
)
 
?
 a 
:
 b
;
    printf
(
"Minimo tra 
%d
 e 
%d
: 
%d\n
"
,
 a
,
 b
,
 min
);
    
    
// Valore assoluto
    
int
 x 
=
 
-
7
;
    
int
 abs_x 
=
 
(
x 
<
 
0
)
 
?
 
-
x 
:
 x
;
    printf
(
"Valore assoluto di 
%d
: 
%d\n
"
,
 x
,
 abs_x
);
    
    
// Pari o dispari
    
int
 n 
=
 
13
;
    printf
(
"
%d
 è 
%s\n
"
,
 n
,
 
(
n 
%
 
2
 
==
 
0
)
 
?
 
"pari"
 
:
 
"dispari"
);
    
    
// Maggiorenne
    
int
 eta 
=
 
17
;
    printf
(
"Sei 
%s\n
"
,
 
(
eta 
>=
 
18
)
 
?
 
"maggiorenne"
 
:
 
"minorenne"
);
    
    
return
 
0
;
}

Esercizio 5: Progetti Completi (35 min)
5.1
 Calcolatore BMI (Body Mass Index):
#include 
<stdio.h>
int
 main
()
 
{
    
float
 importo
;
    
    printf
(
"Inserisci importo spesa: "
);
    scanf
(
"
%f
"
,
 
&
importo
);
    
    
// Sconto: 10% se >= 100€, altrimenti 5%
    
float
 percentuale_sconto 
=
 
(
importo 
>=
 
100.0
)
 
?
 
10.0
 
:
 
5.0
;
    
float
 sconto 
=
 importo 
*
 percentuale_sconto 
/
 
100.0
;
    
float
 totale 
=
 importo 
-
 sconto
;
    
    printf
(
"
\n
=== RIEPILOGO ===
\n
"
);
    printf
(
"Importo:   
%.2f
€
\n
"
,
 importo
);
    printf
(
"Sconto:    
%.0f%%
 (
%.2f
€)
\n
"
,
 percentuale_sconto
,
 sconto
);
    printf
(
"Totale:    
%.2f
€
\n
"
,
 totale
);
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
float
 peso
,
 altezza
,
 bmi
;
    
    printf
(
"=== CALCOLO BMI ===
\n
"
);
    printf
(
"Peso (kg): "
);
    scanf
(
"
%f
"
,
 
&
peso
);
    
    printf
(
"Altezza (m): "
);
    scanf
(
"
%f
"
,
 
&
altezza
);
    
    
// Validazione
    
if
 
(
peso 
<=
 
0
 
||
 altezza 
<=
 
0
)
 
{
        printf
(
"ERRORE: Valori non validi!
\n
"
);
        
return
 
1
;
    
}
    
    bmi 
=
 peso 
/
 
(
altezza 
*
 altezza
);
    
    printf
(
"
\n
=== RISULTATO ===
\n
"
);
    printf
(
"BMI: 
%.1f\n
"
,
 bmi
);
    
    
// Classificazione OMS
    printf
(
"Categoria: "
);
    
if
 
(
bmi 
<
 
16.0
)
 
{
        printf
(
"Grave magrezza
\n
"
);
    
}
 
else
 
if
 
(
bmi 
<
 
18.5
)
 
{
        printf
(
"Sottopeso
\n
"
);
    
}
 
else
 
if
 
(
bmi 
<
 
25.0
)
 
{
        printf
(
"Normopeso
\n
"
);
    
}
 
else
 
if
 
(
bmi 
<
 
30.0
)
 
{
        printf
(
"Sovrappeso
\n
"
);
    
}
 
else
 
if
 
(
bmi 
<
 
35.0
)
 
{
        printf
(
"Obesità classe 1
\n
"
);
    
}
 
else
 
if
 
(
bmi 
<
 
40.0
)
 
{
        printf
(
"Obesità classe 2
\n
"
);
    
}
 
else
 
{
        printf
(
"Obesità classe 3
\n
"
);
    
}
    
    
return
 
0
;
}

5.2
 Gioco indovina numero (con tentativi):
5.3
 Calcolatore tasse (aliquote progressive):
#include 
<stdio.h>
#include 
<stdlib.h>
#include 
<time.h>
int
 main
()
 
{
    
int
 numero_segreto
,
 tentativo
,
 contatore 
=
 
0
;
    
int
 max_tentativi 
=
 
7
;
    
    
// Genera numero casuale tra 1 e 100
    srand
(
time
(
NULL
));
    numero_segreto 
=
 rand
()
 
%
 
100
 
+
 
1
;
    
    printf
(
"=== INDOVINA IL NUMERO ===
\n
"
);
    printf
(
"Ho pensato un numero tra 1 e 100.
\n
"
);
    printf
(
"Hai 
%d
 tentativi.
\n\n
"
,
 max_tentativi
);
    
    
while
 
(
contatore 
<
 max_tentativi
)
 
{
        contatore
++;
        printf
(
"Tentativo 
%d
/
%d
: "
,
 contatore
,
 max_tentativi
);
        scanf
(
"
%d
"
,
 
&
tentativo
);
        
        
if
 
(
tentativo 
==
 numero_segreto
)
 
{
            printf
(
"
\n
  BRAVO! Hai indovinato in 
%d
 tentativi!
\n
"
,
 contatore
            
return
 
0
;
        
}
 
else
 
if
 
(
tentativo 
<
 numero_segreto
)
 
{
            printf
(
"Troppo basso!
\n
"
);
        
}
 
else
 
{
            printf
(
"Troppo alto!
\n
"
);
        
}
        
        
// Suggerimenti extra agli ultimi tentativi
        
if
 
(
contatore 
>=
 max_tentativi 
-
 
2
)
 
{
            
int
 diff 
=
 
(
tentativo 
>
 numero_segreto
)
 
?
 
                       tentativo 
-
 numero_segreto 
:
 
                       numero_segreto 
-
 tentativo
;
            
            
if
 
(
diff 
<=
 
5
)
 
{
                printf
(
"(Sei molto vicino!)
\n
"
);
            
}
 
else
 
if
 
(
diff 
<=
 
10
)
 
{
                printf
(
"(Sei vicino!)
\n
"
);
            
}
        
}
        
        printf
(
"
\n
"
);
    
}
    
    printf
(
"  Hai esaurito i tentativi!
\n
"
);
    printf
(
"Il numero era: 
%d\n
"
,
 numero_segreto
);
    
    
return
 
0
;
}

5.4
 Convertitore numeri romani (da decimale):
#include 
<stdio.h>
int
 main
()
 
{
    
float
 reddito
,
 tasse 
=
 
0
.0
;
    
    printf
(
"=== CALCOLO TASSE (sistema semplificato) ===
\n
"
);
    printf
(
"Inserisci reddito annuo (€): "
);
    scanf
(
"
%f
"
,
 
&
reddito
);
    
    
if
 
(
reddito 
<=
 
0
)
 
{
        printf
(
"Reddito non valido!
\n
"
);
        
return
 
1
;
    
}
    
    
// Aliquote progressive (esempio semplificato)
    
// 0 - 15000: 23%
    
// 15001 - 28000: 27%
    
// 28001 - 55000: 38%
    
// oltre 55000: 43%
    
    
if
 
(
reddito 
<=
 
15000
)
 
{
        tasse 
=
 reddito 
*
 
0
.23
;
    
}
 
else
 
if
 
(
reddito 
<=
 
28000
)
 
{
        tasse 
=
 
15000
 
*
 
0
.23
 
+
 
(
reddito 
-
 
15000
)
 
*
 
0
.27
;
    
}
 
else
 
if
 
(
reddito 
<=
 
55000
)
 
{
        tasse 
=
 
15000
 
*
 
0
.23
 
+
 
13000
 
*
 
0
.27
 
+
 
(
reddito 
-
 
28000
)
 
*
 
0
.38
;
    
}
 
else
 
{
        tasse 
=
 
15000
 
*
 
0
.23
 
+
 
13000
 
*
 
0
.27
 
+
 
27000
 
*
 
0
.38
 
+
 
                
(
reddito 
-
 
55000
)
 
*
 
0
.43
;
    
}
    
    
float
 netto 
=
 reddito 
-
 tasse
;
    
float
 aliquota_media 
=
 
(
tasse 
/
 reddito
)
 
*
 
100.0
;
    
    printf
(
"
\n
=== RIEPILOGO ===
\n
"
);
    printf
(
"Reddito lordo:     
%10.2f
€
\n
"
,
 reddito
);
    printf
(
"Tasse:             
%10.2f
€ (
%.1f%%
)
\n
"
,
 tasse
,
 aliquota_media
);
    printf
(
"Reddito netto:     
%10.2f
€
\n
"
,
 netto
);
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 numero
,
 originale
;
    
    printf
(
"Inserisci numero (1-3999): "
);
    scanf
(
"
%d
"
,
 
&
numero
);
    
    
if
 
(
numero 
<
 
1
 
||
 numero 
>
 
3999
)
 
{
        printf
(
"Numero fuori range!
\n
"
);
        
return
 
1
;
    
}
    
    originale 
=
 numero
;
    printf
(
"
%d
 in numeri romani: "
,
 originale
);
    
    
// Migliaia
    
while
 
(
numero 
>=
 
1000
)
 
{
        printf
(
"M"
);
        numero 
-=
 
1000
;
    
}
    
    
// Centinaia
    
if
 
(
numero 
>=
 
900
)
 
{
        printf
(
"CM"
);

Esempio output:
Inserisci numero (1-3999): 1994
1994 in numeri romani: MCMXCIV
ESERCIZI AUTONOMI
Esercizio 6: Pratica Libera
6.1
 Crea un programma che verifica se un numero è primo (usa %, ciclo anticipato).
        printf
(
"CM"
);
        numero 
-=
 
900
;
    
}
    
if
 
(
numero 
>=
 
500
)
 
{
        printf
(
"D"
);
        numero 
-=
 
500
;
    
}
    
if
 
(
numero 
>=
 
400
)
 
{
        printf
(
"CD"
);
        numero 
-=
 
400
;
    
}
    
while
 
(
numero 
>=
 
100
)
 
{
        printf
(
"C"
);
        numero 
-=
 
100
;
    
}
    
    
// Decine
    
if
 
(
numero 
>=
 
90
)
 
{
        printf
(
"XC"
);
        numero 
-=
 
90
;
    
}
    
if
 
(
numero 
>=
 
50
)
 
{
        printf
(
"L"
);
        numero 
-=
 
50
;
    
}
    
if
 
(
numero 
>=
 
40
)
 
{
        printf
(
"XL"
);
        numero 
-=
 
40
;
    
}
    
while
 
(
numero 
>=
 
10
)
 
{
        printf
(
"X"
);
        numero 
-=
 
10
;
    
}
    
    
// Unità
    
if
 
(
numero 
>=
 
9
)
 
{
        printf
(
"IX"
);
        numero 
-=
 
9
;
    
}
    
if
 
(
numero 
>=
 
5
)
 
{
        printf
(
"V"
);
        numero 
-=
 
5
;
    
}
    
if
 
(
numero 
>=
 
4
)
 
{
        printf
(
"IV"
);
        numero 
-=
 
4
;
    
}
    
while
 
(
numero 
>=
 
1
)
 
{
        printf
(
"I"
);
        numero 
-=
 
1
;
    
}
    
    printf
(
"
\n
"
);
    
    
return
 
0
;
}

6.2
 Programma che calcola il fattoriale di un numero (usa * e ciclo).
6.3
 Convertitore binario → decimale (inserisci cifre una a una).
6.4
 Calcolatore interesse composto bancario.
6.5
 Gioco “Morra cinese” (sasso, carta, forbice) contro computer.
ESERCIZI DA SVOLGERE A CASA
Homework 1:
 Crea un programma “Analisi numero” che: - Legge un numero intero - Dice
se è pari/dispari - Calcola valore assoluto - Dice se è multiplo di 3, 5, o 10 - Conta le cifre -
Calcola somma delle cifre
Homework 2:
 Sistema di voto esami: - Chiede voti di 5 esami (0-30) - Calcola media -
Verifica se tutti i voti sono >= 18 - Dice se studente è promosso - Calcola media ponderata
se forniti i crediti
Homework 3:
 Calcolatore distanza punti: - Chiede coordinate (x1, y1) e (x2, y2) - Calcola
distanza euclidea: √[(x2-x1)² + (y2-y1)²] - Usa solo operatori visti (no sqrt() direttamente,
ma x*x per quadrato)
Homework 4:
 Gioco “Divisione veloce”: - Mostra due numeri casuali - Utente deve
rispondere velocemente se primo divisibile per secondo - Conta risposte corrette/sbagliate -
10 domande
Homework 5:
 Esperimenti con operatori bitwise: - Chiedi un numero - Mostra
rappresentazione binaria (usa shift e &) - Conta bit a 1 - Testa/setta/cancella bit specifici -
Fai swap con XOR
Homework 6:
 Mini-linguaggio matematico: - Chiedi espressione tipo: “5 + 3 * 2” - Leggi
numero, operatore, numero - Valuta rispettando precedenza - Gestisci errori (divisione per
zero)
APPROFONDIMENTI
Sequence Points e Undefined Behavior
Sequence point:
 Punto dove tutte le valutazioni precedenti sono complete.
Sequence points comuni:
 - Fine istruzione (
;
) - Prima di chiamata funzione - 
&&
, 
||
, 
?:
, 
,
 (valutazione da sinistra)
Regola d’oro:
 Non modificare stessa variabile più volte tra sequence points.
Short-Circuit Evaluation
Ottimizzazione:
 
&&
 e 
||
 non valutano secondo operando se non necessario.
int
 x 
=
 
5
;
int
 y 
=
 x
++
 
+
 
++
x
;
  
// UNDEFINED BEHAVIOR!
// Non si sa quale ++ viene valutato prima
// 
✗
 MALE
i 
=
 i
++;
a
[
i
]
 
=
 i
++;
f
(
i
++,
 i
++);
// 
✓
 BENE
i
++;
a
[
i
]
 
=
 value
;
 i
++;
int
 temp1 
=
 i
++;
 
int
 temp2 
=
 i
++;
 f
(
temp1
,
 temp2
);

Attenzione effetti collaterali:
Operatori Bitwise Avanzati
Maschere comuni:
Conta bit a 1 (popcount):
Ottimizzazioni Compilatore
Il compilatore può 
ottimizzare
 espressioni:
Constant folding:
Strength reduction:
Dead code elimination:
Promozione Intera Implicita
// Se x == 0, NON valuta (y / x)
if
 
(
x 
!=
 
0
 
&&
 
(
y 
/
 x
)
 
>
 
2
)
 
{
 
}
// Se p != NULL, SOLO ALLORA deref *p
if
 
(
p 
!=
 NULL 
&&
 
*
p 
==
 
'A'
)
 
{
 
}
if
 
(
x 
>
 
0
 
||
 
++
contatore 
>
 
10
)
 
{
 
}
// Se x > 0, contatore NON viene incrementato!
// Setta bit n
x 
|=
 
(
1
 
<<
 n
);
// Cancella bit n
x 
&=
 
~(
1
 
<<
 n
);
// Toggl bit n
x 
^=
 
(
1
 
<<
 n
);
// Testa bit n
if
 
(
x 
&
 
(
1
 
<<
 n
))
 
{
 
}
// Isola bit meno significativo a 1
x 
&
 
-
x
// Cancella bit meno significativo a 1
x 
&
 
(
x 
-
 
1
)
int
 count 
=
 
0
;
while
 
(
x
)
 
{
    count
++;
    x 
&=
 
(
x 
-
 
1
);
  
// Cancella bit meno significativo
}
// Codice originale
int
 x 
=
 
2
 
+
 
3
;
// Dopo ottimizzazione
int
 x 
=
 
5
;
  
// Calcolato a compile-time
int
 y 
=
 
10
 
*
 
20
 
/
 
5
;
  
// Diventa: int y = 40;
x 
*
 
2
    → x 
<<
 
1
    
// Shift più veloce
x 
/
 
4
    → x 
>>
 
2
if
 
(
0
)
 
{
    
// Questo codice viene rimosso dal compilatore
}

Integer promotion:
 char e short promossi automaticamente a int.
Usual arithmetic conversions:
RIEPILOGO CONCETTI CHIAVE
Operatori Aritmetici
+  addizione
-  sottrazione
*  moltiplicazione
/  divisione (intera se operandi int)
%  modulo (solo interi)
Incremento/Decremento
++x  pre-incremento (prima incrementa, poi usa)
x++  post-incremento (prima usa, poi incrementa)
--x  pre-decremento
x--  post-decremento
Operatori Relazionali
==  uguale
!=  diverso
>   maggiore
<   minore
>=  maggiore o uguale
<=  minore o uguale
Operatori Logici
&&  AND (entrambi veri)
||  OR (almeno uno vero)
!   NOT (inverti)
Operatori Composti
+=  -=  *=  /=  %=
x += 5  equivale a  x = x + 5
Operatore Ternario
condizione ? se_vero : se_falso
max = (a > b) ? a : b;
TABELLE DI RIFERIMENTO RAPIDO
char
 a 
=
 
100
,
 b 
=
 
100
;
char
 c 
=
 a 
+
 b
;
  
// Overflow! a e b promossi a int, risultato 200,
                 
// poi troncato a char (overflow)
printf
(
"
%d\n
"
,
 c
);
  
// Probabilmente: -56 (256 - 200)
int
 i
;
float
 f
;
double
 d
;
i 
+
 f  
// i promosso a float
f 
+
 d  
// f promosso a double

Precedenza Operatori (Comuni)
Precedenza
Operatori
Associatività
Più alta
() [] . ->
L→R
! ~ ++ – + - (unari)
R→L
* / %
L→R
+ -
L→R
< <= > >=
L→R
== !=
L→R
&&
L→R
||
L→R
?:
R→L
= += -= *= /= %=
R→L
Più bassa
,
L→R
Tabelle Verità
AND (&&):
A  B  A&&B
0  0   0
0  1   0
1  0   0
1  1   1
OR (||):
A  B  A||B
0  0   0
0  1   1
1  0   1
1  1   1
NOT (!):
A  !A
0   1
1   0
PROBLEMI COMUNI E SOLUZIONI
Problema 1: = invece di ==
Soluzione:
Problema 2: Divisione intera inaspettata
Soluzione:
int
 x 
=
 
5
;
if
 
(
x 
=
 
10
)
 
{
  
// 
BUG
! Assegna, non confronta
    printf
(
"Sempre vero!
\n
"
);
}
if
 
(
x 
==
 
10
)
 
{
  
// Corretto: confronto
    printf
(
"OK
\n
"
);
}
int
 a 
=
 
5
,
 b 
=
 
2
;
float
 result 
=
 a 
/
 b
;
  
// result = 2.0 (non 2.5!)

Problema 3: Modulo con negativi
Soluzione:
 Usa solo con numeri positivi, o gestisci manualmente:
Problema 4: Overflow senza warning
Soluzione:
 Usa tipo più grande o controlla limiti:
Problema 5: Float comparison
Soluzione:
Problema 6: Precedenza confusa
Soluzione:
 Usa parentesi esplicite:
Problema 7: Incremento multiplo
Soluzione:
 Usa istruzioni separate:
float
 result 
=
 
(
float
)
a 
/
 b
;
  
// 2.5
// oppure
float
 result 
=
 a 
/
 
(
float
)
b
;
// oppure
float
 result 
=
 
(
float
)(
a
)
 
/
 
(
float
)(
b
);
int
 a 
=
 
-
7
 
%
 
3
;
  
// Risultato dipende da implementazione!
// Può essere -1 o 2
int
 mod
(
int
 a
,
 
int
 b
)
 
{
    
int
 r 
=
 a 
%
 b
;
    
return
 
(
r 
<
 
0
)
 
?
 r 
+
 b 
:
 r
;
}
int
 x 
=
 
2000000000
;
int
 y 
=
 x 
+
 
1000000000
;
  
// Overflow silenzioso!
printf
(
"
%d\n
"
,
 y
);
  
// Valore negativo!
#include 
<limits.h>
if
 
(
x 
>
 INT_MAX 
-
 
1000000000
)
 
{
    printf
(
"Overflow!
\n
"
);
}
 
else
 
{
    
int
 y 
=
 x 
+
 
1000000000
;
}
float
 a 
=
 
0
.1
 
+
 
0
.2
;
if
 
(
a 
==
 
0
.3
)
 
{
  
// Probabilmente falso!
    printf
(
"Uguale
\n
"
);
}
#include 
<math.h>
#define EPSILON 
0
.00001
if
 
(
fabs
(
a 
-
 
0
.3
)
 
<
 EPSILON
)
 
{
    printf
(
"Uguale (entro tolleranza)
\n
"
);
}
int
 x 
=
 
10
;
if
 
(
x 
>
 
5
 
&&
 x 
<
 
20
 
||
 x 
==
 
0
)
 
{
 
}
// Viene valutato come: (x > 5 && x < 20) || (x == 0)
// Ma potresti voler dire: x > 5 && (x < 20 || x == 0)
if
 
((
x 
>
 
5
 
&&
 x 
<
 
20
)
 
||
 x 
==
 
0
)
 
{
 
}
  
// Chiaro
int
 i 
=
 
5
;
int
 x 
=
 i
++
 
+
 i
++
 
+
 i
++;
  
// UNDEFINED BEHAVIOR!

ESERCIZI BONUS AVANZATI
Bonus 1: Swap XOR (senza temp)
Bonus 2: Controllo potenza di 2
Bonus 3: Conta bit a 1
int
 x 
=
 i
;
i
++;
x 
+=
 i
;
i
++;
x 
+=
 i
;
i
++;
#include 
<stdio.h>
int
 main
()
 
{
    
int
 a 
=
 
5
,
 b 
=
 
10
;
    
    printf
(
"Prima: a=
%d
, b=
%d\n
"
,
 a
,
 b
);
    
    
// Swap con XOR (solo per curiosità)
    a 
=
 a 
^
 b
;
    b 
=
 a 
^
 b
;
  
// b diventa a originale
    a 
=
 a 
^
 b
;
  
// a diventa b originale
    
    printf
(
"Dopo:  a=
%d
, b=
%d\n
"
,
 a
,
 b
);
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 n
;
    
    printf
(
"Inserisci numero: "
);
    scanf
(
"
%d
"
,
 
&
n
);
    
    
// Un numero è potenza di 2 se ha un solo bit a 1
    
// Trucco: n & (n-1) == 0 per potenze di 2
    
if
 
(
n 
>
 
0
 
&&
 
(
n 
&
 
(
n 
-
 
1
))
 
==
 
0
)
 
{
        printf
(
"
%d
 è una potenza di 2
\n
"
,
 n
);
    
}
 
else
 
{
        printf
(
"
%d
 NON è una potenza di 2
\n
"
,
 n
);
    
}
    
    
return
 
0
;
}

Bonus 4: Inversione cifre
Esempio:
Inserisci numero: 1234
1234 invertito è 4321
GLOSSARIO TECNICO
Operatore
: Simbolo che esegue operazione (+, -, *, /, etc.)
Operando
: Valore su cui opera un operatore
Espressione
: Combinazione di operatori e operandi che produce valore
Precedenza
: Ordine di valutazione degli operatori
Associatività
: Direzione valutazione (L→R o R→L)
Short-circuit
: Valutazione parziale (&&, ||)
L-value
: Espressione che può stare a sinistra di =
R-value
: Espressione che può stare solo a destra di =
Side effect
: Modifica stato (come ++, –)
Sequence point
: Punto dove valutazioni sono complete
Undefined behavior
: Comportamento non specificato dallo standard
Integer promotion
: Conversione automatica char/short → int
Overflow
: Risultato supera massimo rappresentabile
Underflow
: Risultato inferiore a minimo rappresentabile
#include 
<stdio.h>
int
 main
()
 
{
    
unsigned
 
int
 n
;
    
int
 count 
=
 
0
;
    
    printf
(
"Inserisci numero: "
);
    scanf
(
"
%u
"
,
 
&
n
);
    
    
unsigned
 
int
 temp 
=
 n
;
    
while
 
(
temp
)
 
{
        count 
+=
 temp 
&
 
1
;
  
// Aggiunge 1 se bit meno significativo è 1
        temp 
>>=
 
1
;
         
// Shift a destra
    
}
    
    printf
(
"Il numero 
%u
 ha 
%d
 bit a 1
\n
"
,
 n
,
 count
);
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 n
,
 invertito 
=
 
0
;
    
    printf
(
"Inserisci numero: "
);
    scanf
(
"
%d
"
,
 
&
n
);
    
    
int
 originale 
=
 n
;
    
    
while
 
(
n 
>
 
0
)
 
{
        
int
 cifra 
=
 n 
%
 
10
;
           
// Estrae ultima cifra
        invertito 
=
 invertito 
*
 
10
 
+
 cifra
;
  
// Aggiunge a sinistra
        n 
/=
 
10
;
                      
// Rimuove ultima cifra
    
}
    
    printf
(
"
%d
 invertito è 
%d\n
"
,
 originale
,
 invertito
);
    
    
return
 
0
;
}

Modulo
: Resto divisione intera (%)
Bitwise
: Operazione bit a bit (&, |, ^, ~, <<, >>)
PREPARAZIONE PER LA PROSSIMA LEZIONE
Nella prossima lezione useremo questi operatori dentro i 
costrutti di selezione
 (if, else,
switch) per creare programmi che prendono decisioni complesse. È qui che i programmi
diventano veramente intelligenti e interattivi!
Gli operatori che hai imparato oggi sono gli 
strumenti base
 che userai in ogni singolo
programma C che scriverai. Più pratichi, più diventeranno naturali come scrivere in italiano.


---

# lezione9 if selezione

**File:** `lezione9 if selezione.pdf`
**Tipo:** `.pdf`
**Dimensione:** 629.1 KB
**Ultima modifica:** 02/07/2026 09:24

---

LEZIONE 9 - Costrutto di Selezione: if-else
Durata: 4 ore | Teoria: 2h | Esercizi: 2h
PARTE TEORICA (2 ore)
9.1 Introduzione alla Selezione (10 min)
Cos’è la Selezione?
La 
selezione
 (o alternativa) permette al programma di scegliere quale blocco di codice
eseguire in base a una 
condizione
.
Analogia vita reale:
SE piove ALLORA
    prendi ombrello
ALTRIMENTI
    lascia ombrello a casa
Flusso di Controllo
Senza selezione (sequenziale):
Istruzione 1
Istruzione 2
Istruzione 3
Istruzione 4
Tutte le istruzioni vengono sempre eseguite.
Con selezione:
Istruzione 1
SE condizione ALLORA
    Istruzione 2  ← Eseguita solo se vera
ALTRIMENTI
    Istruzione 3  ← Eseguita solo se falsa
Istruzione 4
Flow Chart: Selezione

        ┌─────────┐
        │ Inizio  │
        └────┬────┘
             │
        ┌────┴────┐
        │Istruzione│
        │    1    │
        └────┬────┘
             │
          
╱
──┴──
╲
         
╱
Condiz?
╲
        
╱
____ ____
╲
       SI│        │NO
         │        │
    ┌────┴────┐ ┌┴────────┐
    │Istruzione│ │Istruzione│
    │    2    │ │    3    │
    └────┬────┘ └┬────────┘
         │        │
         └────┬───┘
              │
        ┌─────┴─────┐
        │Istruzione 4│
        └─────┬─────┘
              │
        ┌─────┴─────┐
        │   Fine    │
        └───────────┘
9.2 Istruzione if Semplice (15 min)
Sintassi Base
Componenti:
 - 
if
: parola chiave - 
condizione
: espressione booleana (vera/falsa) - 
{ }
:
blocco di codice (facoltativo se una sola istruzione)
Esempi Base
Esempio 1: Controllo età
Esempio 2: Numero positivo
Esempio 3: Verifica divisibilità
Blocco Singola vs Multipla Istruzione
if
 
(
condizione
)
 
{
    
// Codice eseguito SE condizione è vera
}
int
 eta 
=
 
20
;
if
 
(
eta 
>=
 
18
)
 
{
    printf
(
"Sei maggiorenne
\n
"
);
}
int
 x 
=
 
5
;
if
 
(
x 
>
 
0
)
 
{
    printf
(
"Il numero è positivo
\n
"
);
}
int
 n 
=
 
10
;
if
 
(
n 
%
 
2
 
==
 
0
)
 
{
    printf
(
"
%d
 è pari
\n
"
,
 n
);
}

Una istruzione (parentesi opzionali):
Più istruzioni (parentesi OBBLIGATORIE):
ERRORE comune (senza parentesi):
Best Practice:
 Usa SEMPRE le parentesi graffe, anche per singola istruzione!
Condizioni Complesse
AND logico (&&):
OR logico (||):
NOT logico (!):
Condizioni nidificate:
if
 
(
x 
>
 
0
)
    printf
(
"Positivo
\n
"
);
// Equivalente a:
if
 
(
x 
>
 
0
)
 
{
    printf
(
"Positivo
\n
"
);
}
if
 
(
x 
>
 
0
)
 
{
    printf
(
"Il numero è positivo
\n
"
);
    x 
=
 x 
*
 
2
;
    printf
(
"Raddoppiato: 
%d\n
"
,
 x
);
}
if
 
(
x 
>
 
0
)
    printf
(
"Positivo
\n
"
);
    x 
=
 x 
*
 
2
;
  
// SEMPRE eseguito! Non fa parte dell'if
// Corretto:
if
 
(
x 
>
 
0
)
 
{
    printf
(
"Positivo
\n
"
);
    x 
=
 x 
*
 
2
;
  
// Ora fa parte dell'if
}
int
 eta 
=
 
25
;
char
 patente 
=
 
'S'
;
if
 
(
eta 
>=
 
18
 
&&
 patente 
==
 
'S'
)
 
{
    printf
(
"Puoi guidare
\n
"
);
}
int
 giorno 
=
 
7
;
if
 
(
giorno 
==
 
6
 
||
 giorno 
==
 
7
)
 
{
    printf
(
"È weekend!
\n
"
);
}
int
 piove 
=
 
0
;
  
// 0 = no, 1 = sì
if
 
(!
piove
)
 
{
    printf
(
"Non serve ombrello
\n
"
);
}
int
 voto 
=
 
28
;
if
 
(
voto 
>=
 
18
)
 
{
    
if
 
(
voto 
>=
 
27
)
 
{
        printf
(
"Ottimo!
\n
"
);
    
}
}

Valori di Verità
In C, 
0 è falso
, tutto il resto è 
vero
.
9.3 Istruzione if-else (20 min)
Sintassi
Caratteristiche:
 - Esattamente UN blocco viene eseguito - Se condizione vera → esegue
primo blocco - Se condizione falsa → esegue secondo blocco
Flow Chart: if-else
          
╱
──────
╲
         
╱
Condiz? 
╲
        
╱
____ _____
╲
       SI│         │NO
         │         │
    ┌────┴────┐ ┌─┴─────┐
    │ Blocco  │ │ Blocco│
    │   if    │ │  else │
    └────┬────┘ └─┬─────┘
         │        │
         └────┬───┘
              │
         (continua)
Esempi
Esempio 1: Pari o dispari
Esempio 2: Maggiore/minore
int
 x 
=
 
5
;
if
 
(
x
)
 
{
  
// Vero perché x = 5 (≠ 0)
    printf
(
"x è vero
\n
"
);
}
int
 y 
=
 
0
;
if
 
(
y
)
 
{
  
// Falso perché y = 0
    printf
(
"Non stampato
\n
"
);
}
if
 
(!
y
)
 
{
  
// Vero perché NOT di 0
    printf
(
"y è falso
\n
"
);
}
if
 
(
condizione
)
 
{
    
// Codice SE condizione è vera
}
 
else
 
{
    
// Codice SE condizione è falsa
}
int
 n
;
printf
(
"Inserisci numero: "
);
scanf
(
"
%d
"
,
 
&
n
);
if
 
(
n 
%
 
2
 
==
 
0
)
 
{
    printf
(
"
%d
 è pari
\n
"
,
 n
);
}
 
else
 
{
    printf
(
"
%d
 è dispari
\n
"
,
 n
);
}

Esempio 3: Temperatura
Esempio 4: Login semplice
Confronto con Operatore Ternario
Quando usare ternario vs if-else:
 - Ternario: assegnazioni semplici - if-else: logica
complessa, più istruzioni
9.4 if-else if-else (Selezione Multipla) (20 min)
Sintassi
Caratteristiche:
 - Le condizioni vengono testate 
in ordine
 - Viene eseguito 
solo il primo
blocco con condizione vera - 
else
 finale è 
opzionale
 (caso di default)
int
 a 
=
 
10
,
 b 
=
 
20
;
if
 
(
a 
>
 b
)
 
{
    printf
(
"
%d
 è maggiore di 
%d\n
"
,
 a
,
 b
);
}
 
else
 
{
    printf
(
"
%d
 è minore o uguale a 
%d\n
"
,
 a
,
 b
);
}
float
 temp
;
printf
(
"Temperatura (°C): "
);
scanf
(
"
%f
"
,
 
&
temp
);
if
 
(
temp 
>=
 
25.0
)
 
{
    printf
(
"Fa caldo
\n
"
);
}
 
else
 
{
    printf
(
"Fa fresco
\n
"
);
}
int
 password_corretta 
=
 
1234
;
int
 password_inserita
;
printf
(
"Inserisci password: "
);
scanf
(
"
%d
"
,
 
&
password_inserita
);
if
 
(
password_inserita 
==
 password_corretta
)
 
{
    printf
(
"Accesso consentito
\n
"
);
}
 
else
 
{
    printf
(
"Password errata!
\n
"
);
}
// Con if-else
int
 max
;
if
 
(
a 
>
 b
)
 
{
    max 
=
 a
;
}
 
else
 
{
    max 
=
 b
;
}
// Con operatore ternario (più compatto)
int
 max 
=
 
(
a 
>
 b
)
 
?
 a 
:
 b
;
if
 
(
condizione1
)
 
{
    
// Se condizione1 è vera
}
 
else
 
if
 
(
condizione2
)
 
{
    
// Se condizione1 falsa E condizione2 vera
}
 
else
 
if
 
(
condizione3
)
 
{
    
// Se condizioni precedenti false E condizione3 vera
}
 
else
 
{
    
// Se tutte le condizioni precedenti sono false
}

Flow Chart: if-else if-else
       
╱
────────
╲
      
╱
Condizione
╲
  NO
     
╱
     1?     
╲
───────┐
    
╱
______________
╲
 SI   │
           │               │
      ┌────┴────┐          │
      │ Blocco  │          │
      │    1    │          │
      └────┬────┘          │
           │               │
           │           
╱
───┴───
╲
           │          
╱
Condizione
╲
  NO
           │         
╱
     2?     
╲
───────┐
           │        
╱
______________
╲
 SI   │
           │               │               │
           │          ┌────┴────┐          │
           │          │ Blocco  │          │
           │          │    2    │          │
           │          └────┬────┘          │
           │               │               │
           │               │          ┌────┴────┐
           │               │          │ Blocco  │
           │               │          │  else   │
           │               │          └────┬────┘
           │               │               │
           └───────────────┴───────────────┘
                           │
                      (continua)
Esempi
Esempio 1: Valutazione voto
Esempio 2: Classificazione BMI
int
 voto
;
printf
(
"Inserisci voto (0-100): "
);
scanf
(
"
%d
"
,
 
&
voto
);
if
 
(
voto 
>=
 
90
)
 
{
    printf
(
"Ottimo
\n
"
);
}
 
else
 
if
 
(
voto 
>=
 
80
)
 
{
    printf
(
"Buono
\n
"
);
}
 
else
 
if
 
(
voto 
>=
 
70
)
 
{
    printf
(
"Discreto
\n
"
);
}
 
else
 
if
 
(
voto 
>=
 
60
)
 
{
    printf
(
"Sufficiente
\n
"
);
}
 
else
 
{
    printf
(
"Insufficiente
\n
"
);
}
float
 bmi
;
printf
(
"BMI: "
);
scanf
(
"
%f
"
,
 
&
bmi
);
if
 
(
bmi 
<
 
18.5
)
 
{
    printf
(
"Sottopeso
\n
"
);
}
 
else
 
if
 
(
bmi 
<
 
25.0
)
 
{
    printf
(
"Normopeso
\n
"
);
}
 
else
 
if
 
(
bmi 
<
 
30.0
)
 
{
    printf
(
"Sovrappeso
\n
"
);
}
 
else
 
if
 
(
bmi 
<
 
35.0
)
 
{
    printf
(
"Obesità classe I
\n
"
);
}
 
else
 
if
 
(
bmi 
<
 
40.0
)
 
{
    printf
(
"Obesità classe II
\n
"
);
}
 
else
 
{
    printf
(
"Obesità classe III
\n
"
);
}

Esempio 3: Giorni del mese
Esempio 4: Classificazione temperatura
Ordine delle Condizioni
IMPORTANTE:
 L’ordine conta!
Corretto:
ERRATO:
Regola:
 Metti condizioni 
più specifiche prima
, 
più generali dopo
.
9.5 if Annidati (Nidificazione) (20 min)
Concetto
int
 mese
;
printf
(
"Inserisci mese (1-12): "
);
scanf
(
"
%d
"
,
 
&
mese
);
if
 
(
mese 
==
 
2
)
 
{
    printf
(
"28 o 29 giorni (febbraio)
\n
"
);
}
 
else
 
if
 
(
mese 
==
 
4
 
||
 mese 
==
 
6
 
||
 mese 
==
 
9
 
||
 mese 
==
 
11
)
 
{
    printf
(
"30 giorni
\n
"
);
}
 
else
 
if
 
(
mese 
>=
 
1
 
&&
 mese 
<=
 
12
)
 
{
    printf
(
"31 giorni
\n
"
);
}
 
else
 
{
    printf
(
"Mese non valido
\n
"
);
}
float
 temp
;
printf
(
"Temperatura (°C): "
);
scanf
(
"
%f
"
,
 
&
temp
);
if
 
(
temp 
<
 
0
)
 
{
    printf
(
"Sotto zero (ghiaccio)
\n
"
);
}
 
else
 
if
 
(
temp 
<
 
15
)
 
{
    printf
(
"Freddo
\n
"
);
}
 
else
 
if
 
(
temp 
<
 
25
)
 
{
    printf
(
"Mite
\n
"
);
}
 
else
 
if
 
(
temp 
<
 
35
)
 
{
    printf
(
"Caldo
\n
"
);
}
 
else
 
{
    printf
(
"Molto caldo
\n
"
);
}
if
 
(
x 
>
 
90
)
 
{
    printf
(
"A
\n
"
);
}
 
else
 
if
 
(
x 
>
 
80
)
 
{
    printf
(
"B
\n
"
);
}
 
else
 
if
 
(
x 
>
 
70
)
 
{
    printf
(
"C
\n
"
);
}
// Se x = 95, stampa "A" (primo vero)
if
 
(
x 
>
 
70
)
 
{
          
// Troppo generale!
    printf
(
"C
\n
"
);
}
 
else
 
if
 
(
x 
>
 
80
)
 
{
   
// Mai raggiunto se x > 70
    printf
(
"B
\n
"
);
}
 
else
 
if
 
(
x 
>
 
90
)
 
{
   
// Mai raggiunto
    printf
(
"A
\n
"
);
}
// Se x = 95, stampa "C" (sbagliato!)

Un 
if annidato
 è un if dentro un altro if.
Esempi
Esempio 1: Accesso con doppia verifica
Esempio 2: Classificazione numero
Esempio 3: Triangolo valido e tipo
if
 
(
condizione_esterna
)
 
{
    
// Blocco esterno
    
if
 
(
condizione_interna
)
 
{
        
// Blocco interno (eseguito solo se entrambe vere)
    
}
}
int
 eta
;
char
 patente
;
printf
(
"Età: "
);
scanf
(
"
%d
"
,
 
&
eta
);
if
 
(
eta 
>=
 
18
)
 
{
    printf
(
"Hai patente? (S/N): "
);
    scanf
(
" 
%c
"
,
 
&
patente
);
    
    
if
 
(
patente 
==
 
'S'
 
||
 patente 
==
 
's'
)
 
{
        printf
(
"Puoi noleggiare auto
\n
"
);
    
}
 
else
 
{
        printf
(
"Serve patente
\n
"
);
    
}
}
 
else
 
{
    printf
(
"Sei troppo giovane
\n
"
);
}
int
 n
;
printf
(
"Inserisci numero: "
);
scanf
(
"
%d
"
,
 
&
n
);
if
 
(
n 
==
 
0
)
 
{
    printf
(
"Il numero è zero
\n
"
);
}
 
else
 
{
    
if
 
(
n 
>
 
0
)
 
{
        printf
(
"Il numero è positivo
\n
"
);
        
if
 
(
n 
%
 
2
 
==
 
0
)
 
{
            printf
(
"ed è anche pari
\n
"
);
        
}
 
else
 
{
            printf
(
"ed è anche dispari
\n
"
);
        
}
    
}
 
else
 
{
        printf
(
"Il numero è negativo
\n
"
);
        
if
 
(
n 
%
 
2
 
==
 
0
)
 
{
            printf
(
"ed è anche pari
\n
"
);
        
}
 
else
 
{
            printf
(
"ed è anche dispari
\n
"
);
        
}
    
}
}

Problema: Nidificazione Eccessiva
Codice difficile da leggere:
Soluzione 1: Usa AND logico
Soluzione 2: Early return (in funzioni)
Soluzione 3: else-if al posto di annidati
float
 a
,
 b
,
 c
;
printf
(
"Tre lati: "
);
scanf
(
"
%f
 
%f
 
%f
"
,
 
&
a
,
 
&
b
,
 
&
c
);
if
 
(
a 
+
 b 
>
 c 
&&
 a 
+
 c 
>
 b 
&&
 b 
+
 c 
>
 a
)
 
{
    printf
(
"Triangolo valido
\n
"
);
    
    
if
 
(
a 
==
 b 
&&
 b 
==
 c
)
 
{
        printf
(
"Tipo: EQUILATERO
\n
"
);
    
}
 
else
 
if
 
(
a 
==
 b 
||
 b 
==
 c 
||
 a 
==
 c
)
 
{
        printf
(
"Tipo: ISOSCELE
\n
"
);
    
}
 
else
 
{
        printf
(
"Tipo: SCALENO
\n
"
);
    
}
}
 
else
 
{
    printf
(
"Non è un triangolo valido
\n
"
);
}
if
 
(
condizione1
)
 
{
    
if
 
(
condizione2
)
 
{
        
if
 
(
condizione3
)
 
{
            
if
 
(
condizione4
)
 
{
                
if
 
(
condizione5
)
 
{
                    
// Troppo annidato!
                
}
            
}
        
}
    
}
}
if
 
(
condizione1 
&&
 condizione2 
&&
 condizione3 
&&
 condizione4 
&&
 condizione5
    
// Più chiaro!
}
if
 
(!
condizione1
)
 
return
;
if
 
(!
condizione2
)
 
return
;
if
 
(!
condizione3
)
 
return
;
// Continua...

9.6 Dangling Else (Problema) (10 min)
Il Problema
Quando ci sono più 
if
 senza parentesi graffe, a quale 
if
 appartiene l’
else
?
Regola in C
L’
else
 si associa 
sempre
 all’
if
 più vicino.
Interpretazione corretta:
Come Evitare Ambiguità
Usa SEMPRE le parentesi graffe:
// Invece di:
if
 
(
x 
>
 
90
)
 
{
    
// ...
}
 
else
 
{
    
if
 
(
x 
>
 
80
)
 
{
        
// ...
    
}
 
else
 
{
        
if
 
(
x 
>
 
70
)
 
{
            
// ...
        
}
    
}
}
// Usa:
if
 
(
x 
>
 
90
)
 
{
    
// ...
}
 
else
 
if
 
(
x 
>
 
80
)
 
{
    
// ...
}
 
else
 
if
 
(
x 
>
 
70
)
 
{
    
// ...
}
if
 
(
condizione1
)
    
if
 
(
condizione2
)
        istruzione1
;
else
              
// A quale if appartiene questo else?
    istruzione2
;
if
 
(
condizione1
)
    
if
 
(
condizione2
)
        istruzione1
;
    
else
          
// Appartiene al secondo if!
        istruzione2
;
if
 
(
condizione1
)
 
{
    
if
 
(
condizione2
)
 
{
        istruzione1
;
    
}
 
else
 
{
        istruzione2
;
  
// Eseguito se condizione2 falsa
    
}
}

Esempio Pratico
Ambiguo (senza graffe):
Chiaro (con graffe):
9.7 Best Practices e Stile (15 min)
1. Usa Sempre le Graffe
2. Indentazione Consistente
// Vuoi else per il primo if?
if
 
(
condizione1
)
 
{
    
if
 
(
condizione2
)
 
{
        istruzione1
;
    
}
}
 
else
 
{
  
// Chiaramente associato al primo if
    istruzione2
;
}
// Oppure vuoi else per il secondo if?
if
 
(
condizione1
)
 
{
    
if
 
(
condizione2
)
 
{
        istruzione1
;
    
}
 
else
 
{
  
// Chiaramente associato al secondo if
        istruzione2
;
    
}
}
int
 x 
=
 
5
,
 y 
=
 
10
;
if
 
(
x 
>
 
0
)
    
if
 
(
y 
>
 
5
)
        printf
(
"Entrambi OK
\n
"
);
else
    printf
(
"x negativo
\n
"
);
  
// SBAGLIATO! Non fa quello che pensi
// Quando x=5, y=3: non stampa nulla!
if
 
(
x 
>
 
0
)
 
{
    
if
 
(
y 
>
 
5
)
 
{
        printf
(
"Entrambi OK
\n
"
);
    
}
 
else
 
{
        printf
(
"y troppo piccolo
\n
"
);
    
}
}
 
else
 
{
    printf
(
"x negativo
\n
"
);
}
// 
✗
 MALE (pericoloso)
if
 
(
x 
>
 
0
)
    printf
(
"OK
\n
"
);
// 
✓
 BENE (sicuro)
if
 
(
x 
>
 
0
)
 
{
    printf
(
"OK
\n
"
);
}

3. Condizioni Chiare e Leggibili
4. Evita Condizioni Complesse
5. Costanti a Sinistra (Yoda Conditions)
6. Validazione Input Prima
// 
✓
 BENE
if
 
(
condizione
)
 
{
    istruzione1
;
    istruzione2
;
}
 
else
 
{
    istruzione3
;
}
// 
✗
 MALE
if
 
(
condizione
)
 
{
istruzione1
;
    istruzione2
;
    
}
 
else
 
{
  istruzione3
;
}
// 
✗
 DIFFICILE DA LEGGERE
if
 
(!(
x 
<
 
0
 
||
 x 
>
 
100
 
||
 y 
<
 
0
 
||
 y 
>
 
100
))
 
{
    
// ...
}
// 
✓
 PIÙ CHIARO
int
 x_valido 
=
 
(
x 
>=
 
0
 
&&
 x 
<=
 
100
);
int
 y_valido 
=
 
(
y 
>=
 
0
 
&&
 y 
<=
 
100
);
if
 
(
x_valido 
&&
 y_valido
)
 
{
    
// ...
}
// 
✗
 TROPPO COMPLESSO
if
 
((
a 
>
 b 
&&
 c 
<
 d
)
 
||
 
(
e 
==
 f 
&&
 
(
g 
!=
 h 
||
 i 
<=
 j
))
 
||
 k 
>
 
0
)
 
{
    
// ...
}
// 
✓
 SPEZZA IN PARTI
int
 condizione1 
=
 
(
a 
>
 b 
&&
 c 
<
 d
);
int
 condizione2 
=
 
(
e 
==
 f 
&&
 
(
g 
!=
 h 
||
 i 
<=
 j
));
int
 condizione3 
=
 
(
k 
>
 
0
);
if
 
(
condizione1 
||
 condizione2 
||
 condizione3
)
 
{
    
// ...
}
// Previene errore = invece di ==
if
 
(
5
 
==
 x
)
 
{
  
// Se scrivi if (5 = x) → errore compilazione
    
// ...
}
// Ma rende codice meno leggibile, preferenza personale
if
 
(
x 
==
 
5
)
 
{
  
// Più naturale, ma attenzione a non scrivere =
    
// ...
}

7. Return Early (Guard Clauses)
8. Commenti per Logica Complessa
PARTE PRATICA (2 ore)
ESERCIZI GUIDATI
Esercizio 1: if Semplice (15 min)
1.1
 Controllo maggiore età:
// 
✓
 BUONO - Valida subito
int
 eta
;
scanf
(
"
%d
"
,
 
&
eta
);
if
 
(
eta 
<
 
0
 
||
 eta 
>
 
120
)
 
{
    printf
(
"Età non valida
\n
"
);
    
return
 
1
;
}
// Continua con età valida
if
 
(
eta 
>=
 
18
)
 
{
    
// ...
}
// 
✗
 NIDIFICAZIONE PROFONDA
int
 funzione
(
int
 x
)
 
{
    
if
 
(
x 
>
 
0
)
 
{
        
if
 
(
x 
<
 
100
)
 
{
            
if
 
(
x 
%
 
2
 
==
 
0
)
 
{
                
// Logica principale
                
return
 x 
*
 
2
;
            
}
        
}
    
}
    
return
 
-
1
;
}
// 
✓
 RETURN EARLY
int
 funzione
(
int
 x
)
 
{
    
if
 
(
x 
<=
 
0
)
 
return
 
-
1
;
    
if
 
(
x 
>=
 
100
)
 
return
 
-
1
;
    
if
 
(
x 
%
 
2
 
!=
 
0
)
 
return
 
-
1
;
    
    
// Logica principale (meno nidificata)
    
return
 x 
*
 
2
;
}
// Calcolo sconto in base a categorie cliente
if
 
(
cliente_vip 
&&
 acquisto 
>
 
1000
)
 
{
    sconto 
=
 
0
.20
;
  
// 20% per VIP su grandi acquisti
}
 
else
 
if
 
(
cliente_vip
)
 
{
    sconto 
=
 
0
.10
;
  
// 10% standard VIP
}
 
else
 
if
 
(
acquisto 
>
 
500
)
 
{
    sconto 
=
 
0
.05
;
  
// 5% per acquisti elevati
}
 
else
 
{
    sconto 
=
 
0
.0
;
   
// Nessuno sconto
}

1.2
 Password semplice:
1.3
 Numero positivo, negativo o zero:
Esercizio 2: if-else (20 min)
#include 
<stdio.h>
int
 main
()
 
{
    
int
 eta
;
    
    printf
(
"Inserisci la tua età: "
);
    scanf
(
"
%d
"
,
 
&
eta
);
    
    
if
 
(
eta 
>=
 
18
)
 
{
        printf
(
"Sei maggiorenne
\n
"
);
    
}
    
    
if
 
(
eta 
<
 
18
)
 
{
        printf
(
"Sei minorenne
\n
"
);
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 password 
=
 
1234
;
    
int
 input
;
    
    printf
(
"Inserisci password: "
);
    scanf
(
"
%d
"
,
 
&
input
);
    
    
if
 
(
input 
==
 password
)
 
{
        printf
(
"
✓
 Accesso consentito
\n
"
);
    
}
    
    
if
 
(
input 
!=
 password
)
 
{
        printf
(
"
✗
 Password errata
\n
"
);
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 n
;
    
    printf
(
"Inserisci numero: "
);
    scanf
(
"
%d
"
,
 
&
n
);
    
    
if
 
(
n 
>
 
0
)
 
{
        printf
(
"
%d
 è positivo
\n
"
,
 n
);
    
}
    
    
if
 
(
n 
<
 
0
)
 
{
        printf
(
"
%d
 è negativo
\n
"
,
 n
);
    
}
    
    
if
 
(
n 
==
 
0
)
 
{
        printf
(
"Il numero è zero
\n
"
);
    
}
    
    
return
 
0
;
}

2.1
 Pari o dispari:
2.2
 Massimo tra due numeri:
2.3
 Promozione/bocciatura:
2.4
 Temperatura acqua:
#include 
<stdio.h>
int
 main
()
 
{
    
int
 n
;
    
    printf
(
"Inserisci numero: "
);
    scanf
(
"
%d
"
,
 
&
n
);
    
    
if
 
(
n 
%
 
2
 
==
 
0
)
 
{
        printf
(
"
%d
 è PARI
\n
"
,
 n
);
    
}
 
else
 
{
        printf
(
"
%d
 è DISPARI
\n
"
,
 n
);
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 a
,
 b
;
    
    printf
(
"Primo numero: "
);
    scanf
(
"
%d
"
,
 
&
a
);
    
    printf
(
"Secondo numero: "
);
    scanf
(
"
%d
"
,
 
&
b
);
    
    
if
 
(
a 
>
 b
)
 
{
        printf
(
"Il massimo è 
%d\n
"
,
 a
);
    
}
 
else
 
{
        printf
(
"Il massimo è 
%d\n
"
,
 b
);
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
float
 voto
;
    
    printf
(
"Inserisci voto (0-10): "
);
    scanf
(
"
%f
"
,
 
&
voto
);
    
    
if
 
(
voto 
>=
 
6.0
)
 
{
        printf
(
"
✓
 PROMOSSO
\n
"
);
        printf
(
"Complimenti!
\n
"
);
    
}
 
else
 
{
        printf
(
"
✗
 BOCCIATO
\n
"
);
        printf
(
"Devi rifare l'esame
\n
"
);
    
}
    
    
return
 
0
;
}

Esercizio 3: if-else if-else (25 min)
3.1
 Valutazione esame:
3.2
 Calcolatore sconti:
#include 
<stdio.h>
int
 main
()
 
{
    
float
 temp
;
    
    printf
(
"Temperatura acqua (°C): "
);
    scanf
(
"
%f
"
,
 
&
temp
);
    
    
if
 
(
temp 
<=
 
0
)
 
{
        printf
(
"STATO: Ghiaccio (solido)
\n
"
);
    
}
 
else
 
if
 
(
temp 
<
 
100
)
 
{
        printf
(
"STATO: Acqua (liquido)
\n
"
);
    
}
 
else
 
{
        printf
(
"STATO: Vapore (gas)
\n
"
);
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 voto
;
    
    printf
(
"Inserisci voto (0-100): "
);
    scanf
(
"
%d
"
,
 
&
voto
);
    
    
// Validazione
    
if
 
(
voto 
<
 
0
 
||
 voto 
>
 
100
)
 
{
        printf
(
"Voto non valido!
\n
"
);
        
return
 
1
;
    
}
    
    printf
(
"Voto: 
%d
 - "
,
 voto
);
    
    
if
 
(
voto 
>=
 
90
)
 
{
        printf
(
"Ottimo (A)
\n
"
);
    
}
 
else
 
if
 
(
voto 
>=
 
80
)
 
{
        printf
(
"Buono (B)
\n
"
);
    
}
 
else
 
if
 
(
voto 
>=
 
70
)
 
{
        printf
(
"Discreto (C)
\n
"
);
    
}
 
else
 
if
 
(
voto 
>=
 
60
)
 
{
        printf
(
"Sufficiente (D)
\n
"
);
    
}
 
else
 
{
        printf
(
"Insufficiente (F)
\n
"
);
    
}
    
    
return
 
0
;
}

3.3
 Calcolatore tasse (aliquote):
3.4
 Classificatore IMC:
#include 
<stdio.h>
int
 main
()
 
{
    
float
 importo
,
 sconto_perc 
=
 
0
.0
;
    
    printf
(
"Importo spesa (€): "
);
    scanf
(
"
%f
"
,
 
&
importo
);
    
    
if
 
(
importo 
>=
 
500
)
 
{
        sconto_perc 
=
 
20.0
;
    
}
 
else
 
if
 
(
importo 
>=
 
200
)
 
{
        sconto_perc 
=
 
15.0
;
    
}
 
else
 
if
 
(
importo 
>=
 
100
)
 
{
        sconto_perc 
=
 
10.0
;
    
}
 
else
 
if
 
(
importo 
>=
 
50
)
 
{
        sconto_perc 
=
 
5.0
;
    
}
 
else
 
{
        sconto_perc 
=
 
0
.0
;
    
}
    
    
float
 sconto_importo 
=
 importo 
*
 sconto_perc 
/
 
100.0
;
    
float
 totale 
=
 importo 
-
 sconto_importo
;
    
    printf
(
"
\n
=== RIEPILOGO ===
\n
"
);
    printf
(
"Importo:    
%.2f
€
\n
"
,
 importo
);
    printf
(
"Sconto:     
%.0f%%
 (
%.2f
€)
\n
"
,
 sconto_perc
,
 sconto_importo
);
    printf
(
"Totale:     
%.2f
€
\n
"
,
 totale
);
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
float
 reddito
,
 tasse
;
    
    printf
(
"Reddito annuo (€): "
);
    scanf
(
"
%f
"
,
 
&
reddito
);
    
    
if
 
(
reddito 
<=
 
15000
)
 
{
        tasse 
=
 reddito 
*
 
0
.23
;
    
}
 
else
 
if
 
(
reddito 
<=
 
28000
)
 
{
        tasse 
=
 
15000
 
*
 
0
.23
 
+
 
(
reddito 
-
 
15000
)
 
*
 
0
.27
;
    
}
 
else
 
if
 
(
reddito 
<=
 
55000
)
 
{
        tasse 
=
 
15000
 
*
 
0
.23
 
+
 
13000
 
*
 
0
.27
 
+
 
(
reddito 
-
 
28000
)
 
*
 
0
.38
;
    
}
 
else
 
{
        tasse 
=
 
15000
 
*
 
0
.23
 
+
 
13000
 
*
 
0
.27
 
+
 
27000
 
*
 
0
.38
 
+
 
(
reddito 
-
 
55000
    
}
    
    
float
 netto 
=
 reddito 
-
 tasse
;
    
float
 aliquota_media 
=
 
(
tasse 
/
 reddito
)
 
*
 
100.0
;
    
    printf
(
"
\n
=== CALCOLO TASSE ===
\n
"
);
    printf
(
"Reddito lordo:  
%.2f
€
\n
"
,
 reddito
);
    printf
(
"Tasse:          
%.2f
€ (
%.1f%%
)
\n
"
,
 tasse
,
 aliquota_media
);
    printf
(
"Reddito netto:  
%.2f
€
\n
"
,
 netto
);
    
    
return
 
0
;
}

Esercizio 4: if Annidati (25 min)
4.1
 Accesso cinema con età e accompagnatore:
#include 
<stdio.h>
int
 main
()
 
{
    
float
 peso
,
 altezza
,
 imc
;
    
    printf
(
"Peso (kg): "
);
    scanf
(
"
%f
"
,
 
&
peso
);
    
    printf
(
"Altezza (m): "
);
    scanf
(
"
%f
"
,
 
&
altezza
);
    
    
if
 
(
peso 
<=
 
0
 
||
 altezza 
<=
 
0
)
 
{
        printf
(
"Valori non validi!
\n
"
);
        
return
 
1
;
    
}
    
    imc 
=
 peso 
/
 
(
altezza 
*
 altezza
);
    
    printf
(
"
\n
IMC: 
%.1f
 - "
,
 imc
);
    
    
if
 
(
imc 
<
 
16.0
)
 
{
        printf
(
"Grave magrezza
\n
"
);
    
}
 
else
 
if
 
(
imc 
<
 
18.5
)
 
{
        printf
(
"Sottopeso
\n
"
);
    
}
 
else
 
if
 
(
imc 
<
 
25.0
)
 
{
        printf
(
"Normopeso
\n
"
);
    
}
 
else
 
if
 
(
imc 
<
 
30.0
)
 
{
        printf
(
"Sovrappeso
\n
"
);
    
}
 
else
 
if
 
(
imc 
<
 
35.0
)
 
{
        printf
(
"Obesità classe I
\n
"
);
    
}
 
else
 
if
 
(
imc 
<
 
40.0
)
 
{
        printf
(
"Obesità classe II
\n
"
);
    
}
 
else
 
{
        printf
(
"Obesità classe III
\n
"
);
    
}
    
    
return
 
0
;
}

4.2
 Login con username e password:
4.3
 Classificazione triangolo completa:
#include 
<stdio.h>
int
 main
()
 
{
    
int
 eta
;
    
char
 accompagnato
;
    
    printf
(
"=== BIGLIETTERIA CINEMA ===
\n
"
);
    printf
(
"Film vietato ai minori di 14 anni
\n\n
"
);
    
    printf
(
"Età: "
);
    scanf
(
"
%d
"
,
 
&
eta
);
    
    
if
 
(
eta 
>=
 
14
)
 
{
        printf
(
"
✓
 Puoi entrare
\n
"
);
    
}
 
else
 
{
        printf
(
"Sei accompagnato da un adulto? (S/N): "
);
        scanf
(
" 
%c
"
,
 
&
accompagnato
);
        
        
if
 
(
accompagnato 
==
 
'S'
 
||
 accompagnato 
==
 
's'
)
 
{
            printf
(
"
✓
 Puoi entrare con accompagnatore
\n
"
);
        
}
 
else
 
{
            printf
(
"
✗
 Non puoi entrare
\n
"
);
        
}
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
#include 
<string.h>
int
 main
()
 
{
    
char
 username
[
20
],
 password
[
20
];
    
char
 username_corretto
[]
 
=
 
"admin"
;
    
char
 password_corretta
[]
 
=
 
"1234"
;
    
    printf
(
"=== LOGIN SISTEMA ===
\n
"
);
    printf
(
"Username: "
);
    scanf
(
"
%s
"
,
 username
);
    
    
if
 
(
strcmp
(
username
,
 username_corretto
)
 
==
 
0
)
 
{
        printf
(
"Password: "
);
        scanf
(
"
%s
"
,
 password
);
        
        
if
 
(
strcmp
(
password
,
 password_corretta
)
 
==
 
0
)
 
{
            printf
(
"
\n
✓
 Accesso consentito
\n
"
);
            printf
(
"Benvenuto, 
%s
!
\n
"
,
 username
);
        
}
 
else
 
{
            printf
(
"
\n
✗
 Password errata
\n
"
);
        
}
    
}
 
else
 
{
        printf
(
"
\n
✗
 Username non trovato
\n
"
);
    
}
    
    
return
 
0
;
}

4.4
 Calcolatore età con verifica data:
#include 
<stdio.h>
#include 
<math.h>
int
 main
()
 
{
    
float
 a
,
 b
,
 c
;
    
    printf
(
"Inserisci i tre lati del triangolo:
\n
"
);
    printf
(
"Lato a: "
);
    scanf
(
"
%f
"
,
 
&
a
);
    printf
(
"Lato b: "
);
    scanf
(
"
%f
"
,
 
&
b
);
    printf
(
"Lato c: "
);
    scanf
(
"
%f
"
,
 
&
c
);
    
    
// Verifica validità
    
if
 
(
a 
+
 b 
>
 c 
&&
 a 
+
 c 
>
 b 
&&
 b 
+
 c 
>
 a
)
 
{
        printf
(
"
\n
✓
 Triangolo VALIDO
\n
"
);
        
        
// Tipo per lati
        
if
 
(
a 
==
 b 
&&
 b 
==
 c
)
 
{
            printf
(
"Tipo (lati): EQUILATERO
\n
"
);
        
}
 
else
 
if
 
(
a 
==
 b 
||
 b 
==
 c 
||
 a 
==
 c
)
 
{
            printf
(
"Tipo (lati): ISOSCELE
\n
"
);
        
}
 
else
 
{
            printf
(
"Tipo (lati): SCALENO
\n
"
);
        
}
        
        
// Tipo per angoli (Teorema di Pitagora)
        
float
 aa 
=
 a 
*
 a
,
 bb 
=
 b 
*
 b
,
 cc 
=
 c 
*
 c
;
        
        
if
 
(
fabs
(
aa 
+
 bb 
-
 cc
)
 
<
 
0
.001
 
||
 
            fabs
(
aa 
+
 cc 
-
 bb
)
 
<
 
0
.001
 
||
 
            fabs
(
bb 
+
 cc 
-
 aa
)
 
<
 
0
.001
)
 
{
            printf
(
"Tipo (angoli): RETTANGOLO
\n
"
);
        
}
 
else
 
if
 
(
aa 
+
 bb 
>
 cc 
&&
 aa 
+
 cc 
>
 bb 
&&
 bb 
+
 cc 
>
 aa
)
 
{
            printf
(
"Tipo (angoli): ACUTANGOLO
\n
"
);
        
}
 
else
 
{
            printf
(
"Tipo (angoli): OTTUSANGOLO
\n
"
);
        
}
        
    
}
 
else
 
{
        printf
(
"
\n
✗
 NON è un triangolo valido
\n
"
);
    
}
    
    
return
 
0
;
}

Esercizio 5: Progetti Completi (35 min)
5.1
 Menu calcolatrice avanzata:
#include 
<stdio.h>
int
 main
()
 
{
    
int
 giorno
,
 mese
,
 anno
;
    
int
 oggi_giorno 
=
 
2
,
 oggi_mese 
=
 
10
,
 oggi_anno 
=
 
2024
;
    
    printf
(
"Inserisci data di nascita (gg mm aaaa): "
);
    scanf
(
"
%d
 
%d
 
%d
"
,
 
&
giorno
,
 
&
mese
,
 
&
anno
);
    
    
// Validazione base
    
if
 
(
anno 
<
 
1900
 
||
 anno 
>
 oggi_anno
)
 
{
        printf
(
"Anno non valido!
\n
"
);
        
return
 
1
;
    
}
    
    
if
 
(
mese 
<
 
1
 
||
 mese 
>
 
12
)
 
{
        printf
(
"Mese non valido!
\n
"
);
        
return
 
1
;
    
}
    
    
if
 
(
giorno 
<
 
1
 
||
 giorno 
>
 
31
)
 
{
        printf
(
"Giorno non valido!
\n
"
);
        
return
 
1
;
    
}
    
    
// Calcolo età
    
int
 eta 
=
 oggi_anno 
-
 anno
;
    
    
// Aggiusta se compleanno non ancora passato quest'anno
    
if
 
(
mese 
>
 oggi_mese
)
 
{
        eta
--;
    
}
 
else
 
if
 
(
mese 
==
 oggi_mese
)
 
{
        
if
 
(
giorno 
>
 oggi_giorno
)
 
{
            eta
--;
        
}
    
}
    
    printf
(
"
\n
Hai 
%d
 anni
\n
"
,
 eta
);
    
    
if
 
(
eta 
>=
 
18
)
 
{
        printf
(
"Sei maggiorenne
\n
"
);
    
}
 
else
 
{
        printf
(
"Sei minorenne
\n
"
);
        printf
(
"Diventerai maggiorenne nel 
%d\n
"
,
 anno 
+
 
18
);
    
}
    
    
return
 
0
;
}

5.2
 Sistema di valutazione studente:
#include 
<stdio.h>
#include 
<math.h>
int
 main
()
 
{
    
float
 a
,
 b
,
 risultato
;
    
int
 scelta
;
    
    printf
(
"=== CALCOLATRICE AVANZATA ===
\n
"
);
    printf
(
"1. Addizione
\n
"
);
    printf
(
"2. Sottrazione
\n
"
);
    printf
(
"3. Moltiplicazione
\n
"
);
    printf
(
"4. Divisione
\n
"
);
    printf
(
"5. Potenza
\n
"
);
    printf
(
"6. Radice quadrata
\n
"
);
    printf
(
"7. Valore assoluto
\n
"
);
    printf
(
"
\n
Scegli operazione (1-7): "
);
    scanf
(
"
%d
"
,
 
&
scelta
);
    
    
if
 
(
scelta 
>=
 
1
 
&&
 scelta 
<=
 
5
)
 
{
        printf
(
"Primo numero: "
);
        scanf
(
"
%f
"
,
 
&
a
);
        printf
(
"Secondo numero: "
);
        scanf
(
"
%f
"
,
 
&
b
);
    
}
 
else
 
if
 
(
scelta 
==
 
6
 
||
 scelta 
==
 
7
)
 
{
        printf
(
"Numero: "
);
        scanf
(
"
%f
"
,
 
&
a
);
    
}
 
else
 
{
        printf
(
"Scelta non valida!
\n
"
);
        
return
 
1
;
    
}
    
    printf
(
"
\n
=== RISULTATO ===
\n
"
);
    
    
if
 
(
scelta 
==
 
1
)
 
{
        risultato 
=
 a 
+
 b
;
        printf
(
"
%.2f
 + 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 risultato
);
    
}
 
else
 
if
 
(
scelta 
==
 
2
)
 
{
        risultato 
=
 a 
-
 b
;
        printf
(
"
%.2f
 - 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 risultato
);
    
}
 
else
 
if
 
(
scelta 
==
 
3
)
 
{
        risultato 
=
 a 
*
 b
;
        printf
(
"
%.2f
 × 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 risultato
);
    
}
 
else
 
if
 
(
scelta 
==
 
4
)
 
{
        
if
 
(
b 
!=
 
0
)
 
{
            risultato 
=
 a 
/
 b
;
            printf
(
"
%.2f
 ÷ 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 risultato
);
        
}
 
else
 
{
            printf
(
"ERRORE: Divisione per zero!
\n
"
);
        
}
    
}
 
else
 
if
 
(
scelta 
==
 
5
)
 
{
        risultato 
=
 pow
(
a
,
 b
);
        printf
(
"
%.2f
 ^ 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 risultato
);
    
}
 
else
 
if
 
(
scelta 
==
 
6
)
 
{
        
if
 
(
a 
>=
 
0
)
 
{
            risultato 
=
 sqrt
(
a
);
            printf
(
"√
%.2f
 = 
%.2f\n
"
,
 a
,
 risultato
);
        
}
 
else
 
{
            printf
(
"ERRORE: Radice di numero negativo!
\n
"
);
        
}
    
}
 
else
 
if
 
(
scelta 
==
 
7
)
 
{
        risultato 
=
 fabs
(
a
);
        printf
(
"|
%.2f
| = 
%.2f\n
"
,
 a
,
 risultato
);
    
}
    
    
return
 
0
;
}

5.3
 Gioco “Sasso, Carta, Forbice”:
#include 
<stdio.h>
int
 main
()
 
{
    
int
 voti
[
5
];
    
int
 i
,
 somma 
=
 
0
,
 min 
=
 
100
,
 max 
=
 
0
;
    
float
 media
;
    
int
 promosso 
=
 
1
;
  
// 1 = sì, 0 = no
    
    printf
(
"=== VALUTAZIONE STUDENTE ===
\n
"
);
    printf
(
"Inserisci 5 voti (0-30):
\n
"
);
    
    
for
 
(
i 
=
 
0
;
 i 
<
 
5
;
 i
++)
 
{
        printf
(
"Voto 
%d
: "
,
 i 
+
 
1
);
        scanf
(
"
%d
"
,
 
&
voti
[
i
]);
        
        
// Validazione
        
if
 
(
voti
[
i
]
 
<
 
0
 
||
 voti
[
i
]
 
>
 
30
)
 
{
            printf
(
"Voto non valido!
\n
"
);
            
return
 
1
;
        
}
        
        somma 
+=
 voti
[
i
];
        
        
// Aggiorna min e max
        
if
 
(
voti
[
i
]
 
<
 min
)
 min 
=
 voti
[
i
];
        
if
 
(
voti
[
i
]
 
>
 max
)
 max 
=
 voti
[
i
];
        
        
// Verifica promozione
        
if
 
(
voti
[
i
]
 
<
 
18
)
 
{
            promosso 
=
 
0
;
        
}
    
}
    
    media 
=
 
(
float
)
somma 
/
 
5
;
    
    printf
(
"
\n
=== RISULTATI ===
\n
"
);
    printf
(
"Media: 
%.1f\n
"
,
 media
);
    printf
(
"Voto minimo: 
%d\n
"
,
 min
);
    printf
(
"Voto massimo: 
%d\n
"
,
 max
);
    
    
if
 
(
promosso
)
 
{
        printf
(
"Esito: 
✓
 PROMOSSO
\n
"
);
        
        
if
 
(
media 
>=
 
27
)
 
{
            printf
(
"Qualifica: OTTIMO
\n
"
);
        
}
 
else
 
if
 
(
media 
>=
 
24
)
 
{
            printf
(
"Qualifica: BUONO
\n
"
);
        
}
 
else
 
{
            printf
(
"Qualifica: SUFFICIENTE
\n
"
);
        
}
    
}
 
else
 
{
        printf
(
"Esito: 
✗
 BOCCIATO
\n
"
);
        printf
(
"(Hai almeno un'insufficienza)
\n
"
);
    
}
    
    
return
 
0
;
}

5.4
 Analizzatore numero completo:
#include 
<stdio.h>
#include 
<stdlib.h>
#include 
<time.h>
int
 main
()
 
{
    
int
 giocatore
,
 computer
;
    
    
// Inizializza generatore numeri casuali
    srand
(
time
(
NULL
));
    
    printf
(
"=== SASSO, CARTA, FORBICE ===
\n
"
);
    printf
(
"1. Sasso
\n
"
);
    printf
(
"2. Carta
\n
"
);
    printf
(
"3. Forbice
\n
"
);
    printf
(
"
\n
La tua scelta (1-3): "
);
    scanf
(
"
%d
"
,
 
&
giocatore
);
    
    
if
 
(
giocatore 
<
 
1
 
||
 giocatore 
>
 
3
)
 
{
        printf
(
"Scelta non valida!
\n
"
);
        
return
 
1
;
    
}
    
    
// Computer sceglie casualmente
    computer 
=
 rand
()
 
%
 
3
 
+
 
1
;
    
    printf
(
"
\n
Tu: "
);
    
if
 
(
giocatore 
==
 
1
)
 printf
(
"Sasso
\n
"
);
    
else
 
if
 
(
giocatore 
==
 
2
)
 printf
(
"Carta
\n
"
);
    
else
 printf
(
"Forbice
\n
"
);
    
    printf
(
"Computer: "
);
    
if
 
(
computer 
==
 
1
)
 printf
(
"Sasso
\n
"
);
    
else
 
if
 
(
computer 
==
 
2
)
 printf
(
"Carta
\n
"
);
    
else
 printf
(
"Forbice
\n
"
);
    
    printf
(
"
\n
"
);
    
    
if
 
(
giocatore 
==
 computer
)
 
{
        printf
(
"PAREGGIO!
\n
"
);
    
}
 
else
 
if
 
((
giocatore 
==
 
1
 
&&
 computer 
==
 
3
)
 
||
               
(
giocatore 
==
 
2
 
&&
 computer 
==
 
1
)
 
||
               
(
giocatore 
==
 
3
 
&&
 computer 
==
 
2
))
 
{
        printf
(
"HAI VINTO!  
\n
"
);
    
}
 
else
 
{
        printf
(
"HAI PERSO!  
\n
"
);
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
#include 
<math.h>
int
 main
()
 
{
    
int
 n
,
 originale
,
 cifre 
=
 
0
,
 somma_cifre 
=
 
0
;
    
int
 temp
,
 invertito 
=
 
0
;
    
int
 is_primo 
=
 
1
;
    
    printf
(
"Inserisci un numero intero positivo: "
);
    scanf
(
"
%d
"
,
 
&
n
);
    
    
if
 
(
n 
<=
 
0
)
 
{
        printf
(
"Numero non valido!
\n
"
);
        
return
 
1
;
    
}
    
    originale 
=
 n
;
    

ESERCIZI AUTONOMI
Esercizio 6: Pratica Libera
    
    printf
(
"
\n
=== ANALISI DI 
%d
 ===
\n
"
,
 originale
);
    
    
// Pari o dispari
    
if
 
(
n 
%
 
2
 
==
 
0
)
 
{
        printf
(
"Parità: PARI
\n
"
);
    
}
 
else
 
{
        printf
(
"Parità: DISPARI
\n
"
);
    
}
    
    
// Conta cifre e somma
    temp 
=
 n
;
    
while
 
(
temp 
>
 
0
)
 
{
        cifre
++;
        somma_cifre 
+=
 temp 
%
 
10
;
        temp 
/=
 
10
;
    
}
    printf
(
"Numero di cifre: 
%d\n
"
,
 cifre
);
    printf
(
"Somma delle cifre: 
%d\n
"
,
 somma_cifre
);
    
    
// Numero invertito
    temp 
=
 n
;
    
while
 
(
temp 
>
 
0
)
 
{
        invertito 
=
 invertito 
*
 
10
 
+
 temp 
%
 
10
;
        temp 
/=
 
10
;
    
}
    printf
(
"Numero invertito: 
%d\n
"
,
 invertito
);
    
    
// Palindromo
    
if
 
(
originale 
==
 invertito
)
 
{
        printf
(
"È un PALINDROMO
\n
"
);
    
}
 
else
 
{
        printf
(
"NON è un palindromo
\n
"
);
    
}
    
    
// Primo
    
if
 
(
n 
==
 
1
)
 
{
        is_primo 
=
 
0
;
    
}
 
else
 
{
        
for
 
(
int
 i 
=
 
2
;
 i 
<=
 sqrt
(
n
);
 i
++)
 
{
            
if
 
(
n 
%
 i 
==
 
0
)
 
{
                is_primo 
=
 
0
;
                
break
;
            
}
        
}
    
}
    
    
if
 
(
is_primo
)
 
{
        printf
(
"È un numero PRIMO
\n
"
);
    
}
 
else
 
{
        printf
(
"NON è un numero primo
\n
"
);
    
}
    
    
// Multipli
    printf
(
"Multiplo di:
\n
"
);
    
if
 
(
n 
%
 
2
 
==
 
0
)
 printf
(
"  2
\n
"
);
    
if
 
(
n 
%
 
3
 
==
 
0
)
 printf
(
"  3
\n
"
);
    
if
 
(
n 
%
 
5
 
==
 
0
)
 printf
(
"  5
\n
"
);
    
if
 
(
n 
%
 
10
 
==
 
0
)
 printf
(
"  10
\n
"
);
    
    
return
 
0
;
}

6.1
 Crea un programma che determina il tipo di giorno (feriale/festivo) dato il numero del
giorno (1-7).
6.2
 Calcolo parcheggio: tariffe diverse per ore (prima ora 2€, successive 1.50€).
6.3
 Conversione voto numerico (0-30) in giudizio italiano (gravemente insufficiente,
insufficiente, sufficiente, buono, distinto, ottimo, eccellente).
6.4
 Quiz a scelta multipla con 5 domande e punteggio finale.
6.5
 Sistema di accesso con 3 tentativi di password.
ESERCIZI DA SVOLGERE A CASA
Homework 1:
 Calcolatore commissioni bancarie: - Prelievo < 100€: commissione 2€ -
100€ - 500€: commissione 1.5% - > 500€: commissione 1% - Se conto premium:
commissione dimezzata
Homework 2:
 Sistema voto laurea: - Chiedi media voti (0-30) - Chiedi se ha lodi (quante) -
Chiedi punteggio tesi (0-5) - Calcola voto base (media * 110 / 30) - Aggiungi punti lode e
tesi - Determina se lode (>= 110)
Homework 3:
 Validatore password robusto: - Lunghezza minima 8 caratteri - Almeno una
maiuscola - Almeno una minuscola - Almeno un numero - Almeno un simbolo speciale -
Valuta sicurezza (debole/media/forte)
Homework 4:
 Gioco indovina il numero con difficoltà: - Scegli difficoltà
(facile/medio/difficile) - Range diverso per difficoltà - Tentativi diversi per difficoltà -
Suggerimenti progressivi
Homework 5:
 Sistema di prenotazione ristorante: - Chiedi numero persone - Chiedi giorno
settimana - Chiedi ora - Verifica disponibilità (regole complesse) - Calcola prezzo stimato
Homework 6:
 Analizzatore anno: - Chiedi anno - Dice se bisestile - Dice secolo - Dice
millennio - Eventi storici importanti (hardcoded)
APPROFONDIMENTI
Switch vs if-else
Quando usare 
switch
 (lezione prossima) vs 
if-else
:
Usa if-else quando:
 - Condizioni complesse (range, AND, OR) - Condizioni con float -
Poche alternative (2-3)
Usa switch quando:
 - Confronto singola variabile con costanti - Molte alternative (4+) -
Valori interi/char discreti
Short-Circuit nelle Condizioni
Attenzione effetti collaterali:
// && valuta secondo operando solo se primo è vero
if
 
(
puntatore 
!=
 NULL 
&&
 
*
puntatore 
==
 
'A'
)
 
{
    
// Sicuro: se puntatore NULL, non deref
}
// || valuta secondo operando solo se primo è falso
if
 
(
x 
==
 
0
 
||
 y 
/
 x 
>
 
10
)
 
{
    
// Sicuro: se x=0, non divide
}

Ottimizzazione Condizioni
Branch prediction:
 CPU moderna “indovina” quale branch prendere.
Codice prevedibile:
Codice imprevedibile:
Branch misprediction
 costa 10-20 cicli CPU!
Espressioni Booleane Lazy
RIEPILOGO CONCETTI CHIAVE
if Semplice
if-else
if-else if-else
if Annidati
if
 
(
x 
>
 
0
 
||
 
++
contatore 
>
 
10
)
 
{
 
}
// Se x > 0, contatore NON viene incrementato!
// Condizione quasi sempre vera → CPU predice bene
if
 
(
array
[
i
]
 
!=
 
0
)
 
{
  
// Raramente 0
    
// Eseguito quasi sempre
}
// Condizione casuale → CPU sbaglia spesso
if
 
(
rand
()
 
%
 
2
)
 
{
    
// 50% vero, 50% falso
}
// Valutazione pigra (lazy) con variabili temporanee
int
 condizione_complessa 
=
 
(
a 
>
 b 
&&
 c 
<
 d
)
 
||
 
(
e 
==
 f 
&&
 g 
!=
 h
);
if
 
(
condizione_complessa
)
 
{
    
// Usa variabile, più chiaro
}
if
 
(
condizione
)
 
{
    
// Eseguito se vera
}
if
 
(
condizione
)
 
{
    
// Se vera
}
 
else
 
{
    
// Se falsa
}
if
 
(
cond1
)
 
{
    
// Prima vera
}
 
else
 
if
 
(
cond2
)
 
{
    
// Seconda vera
}
 
else
 
{
    
// Tutte false
}

PUNTI CHIAVE DELLA LEZIONE
✓
 
if
 esegue blocco solo se condizione vera
✓
 
if-else
 sceglie tra due alternative
✓
 
if-else if
 permette scelte multiple
✓
 
Usa SEMPRE graffe
 { } anche per singola istruzione
✓
 
Condizioni
 valutate in ordine (prima vera vince)
✓
 
Dangling else
 si associa all’if più vicino
✓
 
0 è falso
, tutto il resto è vero
✓
 
Valida input
 prima di usarlo
✓
 
Return early
 riduce nidificazione
✓
 
Commenta logica
 complessa
PREPARAZIONE PER LA PROSSIMA LEZIONE
Nella prossima lezione studieremo: - 
Istruzione switch-case
: selezione multipla ottimizzata
- 
Break e fall-through
: controllo flusso switch - 
Default
: caso di default - 
Switch vs if-
else
: quando usare cosa - 
Esempi pratici
: menu, stati, classificazioni
Porta con te: - Esercizi homework completati - Domande su if-else o condizioni - Esempi di
menu o scelte multiple - Idee per progetti con molte opzioni
Ottimo lavoro! Ora sai prendere decisioni nei programmi!  
Con if-else hai il potere di creare programmi 
intelligenti
 che reagiscono diversamente in
base alle situazioni. Nella prossima lezione aggiungeremo lo switch per gestire ancora
meglio scelte multiple!
if
 
(
cond_esterna
)
 
{
    
if
 
(
cond_interna
)
 
{
        
// Entrambe vere
    
}
}


---

# SVILUPPO SOSTENIBILE 25-27

**File:** `SVILUPPO SOSTENIBILE 25-27.docx`
**Tipo:** `.docx`
**Dimensione:** 162.3 KB
**Ultima modifica:** 02/07/2026 09:24

---

ISTITUTO TECNOLOGICO SUPERIORE ACADEMY

PER LE TECNOLOGIE DELLA INFORMAZIONE E DELLA COMUNICAZIONE

DEL PIEMONTE

Sede legale: Torino, Piazza Carlo Felice 18

Oggetto: SVILUPPO SOSTENIBILE

L’ITS Academy ICT Piemonte, come ente di formazione professionale valorizza e promuove cambiamenti sotto il profilo comportamentale, finalizzato a dotare tutti i cittadini delle competenze essenziali necessarie per conseguire uno sviluppo sostenibile.

Durante l’intera durata del percorso verranno trattate trasversalmente tematiche finalizzate alla consapevolezza in ambito di sostenibilità e difesa dell’ambiente. 

La programmazione comunitaria 2021/2027 collegata all’Agenda 2030 per lo sviluppo sostenibile, continua ad attribuire a quest’ultimo un ruolo centrale tra gli obiettivi da perseguire tra i cittadini, le istituzioni e le realtà economiche europee. Nelle unità formative caratterizzanti del percorso saranno trattate le tematiche generali dello sviluppo sostenibile e della green economy.  

Si affronteranno i temi della neutralità climatica, della produzione di energia tramite fonti rinnovabili, dell’uso efficiente delle risorse, del contenimento della produzione dei rifiuti, della economia circolare e dell’impatto economico e sui territori dei cambiamenti climatici. 

L’obiettivo sarà rendere gli studenti consapevoli delle ricadute sul sistema economico e sociale delle politiche ambientali e di stimolarli ad assumere comportamenti “sostenibili” sia nella gestione dei processi produttivi (anche nell’ottica di futuri profili tecnici) che nei comportamenti personali.  

Saranno affrontati da un lato la valutazione dell’impatto ambientale dei processi e delle tecnologie utilizzate dal mondo dell’information technology per svolgere le proprie attività di business; dall’altro, si analizzerà ciò che può fare l’IT per supportare le sfide della green economy (smart working, smart grid, condivisione di dati e risorse in cloud, ecc ). Inoltre, argomento centrale parlando di digitalizzazione rimane l’obsolescenza dei dispositivi elettronici e il loro smaltimento secondo le normative vigenti. In ambito IT l’obsolescenza di dispositivi e sistemi è una tema importante in quanto la non sostituzione di dispositivi datati può arrivare anche a creare vulnerabilità alle reti e ai sistemi con conseguente possibile attacco informatico e compromissione e perdita di dati. In questo contesto, la problematica dell’obsolescenza sarà trattata nell’ottica della sostenibilità ambientale cercando un punto di equilibrio tra il contenimento nella produzione dei rifiuti e le necessità che nascono dall’ evoluzione tecnologica di sistemi informatici.

La parte pratica delle lezioni dedicata all'uso del computer verrà condotta trasmettendo agli allievi i principi dello sviluppo sostenibile e della gestione ecosostenibile delle risorse. Questa modalità prevede l'attento utilizzo dei materiali e dei supporti elettronici utilizzati durante le ore di lezione. Per l’utilizzo della carta all'interno della struttura sono a disposizione cestini per i rifiuti in genere, cestini per la plastica e contenitori per il riciclo della carta. Gli allievi saranno invitati a utilizzare i fogli su entrambe le facciate, ed a utilizzare carta di riciclo per le stampe di prova di lavori, relazioni, esercitazioni. Le dispense prodotte e distribuite come fotocopia saranno sempre in formato fronte/retro. Per l’utilizzo dei computer viene sollecitato l'uso delle anteprime di stampa al posto della stampa di prova; per l’utilizzo della struttura spegnere le luci; accendere il Pc solo se necessario.

Le tematiche verranno affrontate trasversalmente in tutto il percorso per sensibilizzare gli allievi a adottare buone prassi operative e nello specifico gli argomenti trattati saranno i seguenti:

  Tematiche e orientamenti ambientali previsti a livello UE, nazionale, regionale e locale 

Rifiuti e risorse materiali, Neutralità climatica, Ambiente e salute. Idrogeno e mobilità elettrica, Il Green Deal europeo e le strategie UE ad esso correlate 

Vulnerabilità degli ambienti naturali  

Cambiamenti climatici e impatto sui territori Biodiversità  

Modalità di gestione delle risorse ambientali ed energetiche  

Efficienza energetica Sfruttamento del Suolo Utilizzo sostenibile delle risorse idriche  

Nuovi modelli di consumo e di mobilità a basso impatto ambientale  

L’economia circolare Nuove forme di mobilità per le persone e le merci  

Problematiche sociali e sanitarie  

Impatto dell’inquinamento sulla salute dei cittadini 

Legislazioni ambientali e incentivazioni economiche di settore 

La normativa RAEE 

Principali strumenti e tecniche di osservazione 

L’impronta ambientale delle organizzazioni produttive in ambito IT 

I fattori che influiscono sulla sostenibilità dei processi 

Il monitoraggio degli asset IT in ottica di consumo energetico 

Legame di causa/effetto delle azioni umane sull'ambiente 

L’efficienza energetica delle soluzioni hardware e software utilizzate  

Buone prassi per l'utilizzo eco-compatibile delle tecnologie informatiche 

Soluzioni e tecnologie per il risparmio di risorse e l'efficientamento energetico 

Smart working: tecnologie e ambiti di applicazione nel comparto IT 

Smart grid: la gestione IT delle reti di distribuzione dell’energia 

La diffusione dei sensori in rete per il monitoraggio ambientale 

Principi fondamentali della gestione dei rifiuti e di materiali da riciclo, in un'ottica di circolarità 

Estendere la vita utile di prodotti, componenti e materiali 

Gestione e smaltimento dei rifiuti e dei componenti elettrici ed elettronici (RAEE) 

 Per una maggiore completezza di informazioni qui di seguito alcuni link di approfondimento:

 TEMATICA SOSTENIBILITA’

Temi — Agenzia europea dell'ambiente (europa.eu) 

 A European Green Deal | European Commission (europa.eu) 

 Delivering the European Green Deal | European Commission (europa.eu) 

 Neutralità carbonica: cos'è e come raggiungerla | Attualità | Parlamento europeo (europa.eu) 

 Ministero della Transizione Ecologica (mite.gov.it) 

 Home - Geoportale Nazionale (minambiente.it) 

Strategia di sviluppo sostenibile | Regione Piemonte 

 Ambiente e Territorio | Regione Piemonte 

 Dettaglio ADA.14.01.04 - Sustainability Management in ambito ICT | Atlante Lavoro | INAPP 

 www.conai.org 

 Home - Greenpeace Italia - Greenpeace Italia 

 http://it.wikipedia.org/wiki/Raee 

http://it.wikipedia.org/wiki/Riciclaggio_della_carta 

www.ambiente.it/ 

www.federambiente.it/ 

Officina Ambiente - Studio di consulenza ambientale 

