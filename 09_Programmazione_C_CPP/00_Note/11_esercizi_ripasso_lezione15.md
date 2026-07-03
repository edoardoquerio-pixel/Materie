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

