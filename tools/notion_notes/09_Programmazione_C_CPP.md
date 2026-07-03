# [09] Programmazione C/CPP

## 📋 Panoramica

Materia di programmazione strutturata in C. Copre dai fondamenti (variabili, cicli, funzioni) fino a temi avanzati (puntatori, allocazione dinamica, struct, file I/O, ordinamento). Le lezioni sono progressive con guida didattica + esercizi per ogni argomento.

**Tecnologie**: C (C11/C17), GCC/Clang, CMake, compilatore da riga di comando

---

## 📚 Indice degli argomenti

### 1. Fondamenti (Lezioni 1-9)

- **Lezione 1**: Algoritmi e programmazione — flowchart, pseudocodice
- **Lezione 2**: Flowchart — diagrammi di flusso, strutture di controllo
- **Lezione 3**: Sistema binario — rappresentazione dei numeri, complemento a 2
- **Lezione 4**: Decimali e char — tipi di dato, codifica ASCII
- **Lezione 6**: Primo programma C:
  ```c
  #include <stdio.h>
  int main() {
      printf("Hello, World!\n");
      return 0;
  }
  ```
- **Lezione 7**: Variabili e input — `scanf`, `printf`, tipi (int, float, char)
- **Lezione 8**: Operatori — aritmetici, logici, relazionali, bitwise
- **Lezione 9**: if/else — selezione, operatori ternari

### 2. Controllo di Flusso (Lezioni 10-12)

- **Lezione 10**: switch — selezione multipla
- **Lezione 11**: Ciclo while/do-while — iterazione condizionata
- **Lezione 12**: Ciclo for — iterazione contata

### 3. Array e Matrici (Lezioni 13-14)

- **Array monodimensionali**: `int v[10];`
- **Array multidimensionali (matrici)**: `int m[3][4];`
- Iterazione su array, inizializzazione, ricerca lineare

### 4. Funzioni e Passaggio Parametri (Lezione 15)

```c
int somma(int a, int b) {
    return a + b;
}
```
- **Passaggio per valore** (copia) vs **per riferimento** (puntatore)
- **Prototipi**: dichiarazione prima di `main()`

### 5. Puntatori e Array Dinamici (Lezioni 16-18)

- **Puntatori**: variabili che contengono indirizzi di memoria:
  ```c
  int x = 10;
  int *p = &x;
  *p = 20;  // x ora vale 20
  ```
- **Aritmetica dei puntatori**: `p + 1` avanza di sizeof(tipo)
- **Allocazione dinamica**:
  ```c
  int *arr = malloc(n * sizeof(int));
  if (arr == NULL) { /* errore */ }
  arr = realloc(arr, new_size * sizeof(int));
  free(arr);
  ```
- **Puntatori a funzione, puntatori a struct**

### 6. Stringhe (Lezione 21)

- `char s[] = "Ciao";` — array di char terminato da `\0`
- Funzioni: `strlen()`, `strcpy()`, `strcat()`, `strcmp()`, `strtok()`
- **Stringhe dinamiche**: allocazione con `malloc` + `realloc`

### 7. Struct e Oggetti in C (Lezioni 22-23)

```c
typedef struct {
    char nome[50];
    int eta;
} Persona;
```
- **Array di struct**, puntatori a struct (`->`)
- **Struct annidate**, campi bit

### 8. File I/O (Lezione 24)

```c
FILE *f = fopen("file.txt", "r");
if (f) {
    char buffer[256];
    while (fgets(buffer, sizeof(buffer), f)) {
        printf("%s", buffer);
    }
    fclose(f);
}
```
- Modalità: r, w, a, r+, wb, rb (binario)
- `fprintf`, `fscanf`, `fread`, `fwrite`

### 9. Algoritmi di Ordinamento (Lezione 20)

- **Bubble Sort** — O(n²), semplice ma lento
- **Selection Sort** — O(n²), minimo scambio
- **Insertion Sort** — O(n²), buono per dati quasi ordinati
- **Merge Sort / Quick Sort** — O(n log n), divide-et-impera

---

## ⚡ Punti Chiave

1. **Sempre controllare il valore di ritorno di `malloc`**: può fallire → NULL
2. **`free()` ogni `malloc()`**: ogni allocazione deve essere deallocata
3. **Mai usare `gets()`**: buffer overflow sicuro; usare `fgets()`
4. **Puntatori**: l'operatore `*` dichiara/ dereferenzia, `&` prende l'indirizzo
5. **Array e puntatori sono correlati**: `arr[i] ≡ *(arr + i)`
6. **Stringhe**: sempre terminate da `\0` — lasciare spazio!
7. **CMakeLists.txt** per progetti multi-file

---

## 📎 Risorse Collegate

- **02_Esercizi/** — Esercizi graduati per ogni lezione
- **03_Progetti/** — Progetti completi (ParcheggioIntelligente, GestioneProntoSoccorso, sviluppoTemaEsame)
- **Materiale extra**: guide didattiche in markdown per puntatori, array dinamici, code/pile
