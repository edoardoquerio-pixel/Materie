# Programmazione C/C++ — Note Complete

## 1. Fondamenti

- **Tipi**: `int`, `float`, `double`, `char`, `void`
- **Modificatori**: `short`, `long`, `unsigned`, `signed`
- **Operatori**: aritmetici, relazionali, logici, bitwise, assegnazione
- **Controllo**: `if/else`, `switch`, `while`, `do/while`, `for`
- **Funzioni**: dichiarazione (prototipo), definizione, chiamata, ricorsione

## 2. Puntatori

```c
int *p;           // Dichiarazione puntatore a int
p = &x;           // p contiene indirizzo di x
*p = 10;          // modifica valore a cui p punta
sizeof(p)         // 4 (x86) o 8 (x64)

// Puntatori e array
int arr[5] = {1,2,3,4,5};
int *q = arr;     // equivalente a &arr[0]
*(q+2) = 10;      // arr[2] = 10

// Allocazione dinamica
int *dyn = (int*)malloc(n * sizeof(int));
free(dyn);
```

## 3. Array e Matrici

```c
int arr[10];                          // Array 1D
int mat[3][4];                        // Matrice 3×4
// Per stringhe: array di char
char nome[50] = "Mario";
```

## 4. Stringhe (C-style)

```c
#include <string.h>
strlen(s), strcpy(dest, src), strcat(dest, src), strcmp(a, b)
// Confronto: strcmp == 0 significa uguali
// INPUT: fgets(buf, size, stdin) o scanf
```

## 4b. Compilazione e Toolchain

```bash
gcc -o program program.c -Wall -Wextra -std=c11   # C
g++ -o program program.cpp -Wall -Wextra -std=c++17  # C++
./program

# Debug
gdb ./program
valgrind --leak-check=full ./program

# CMake (progetti strutturati)
mkdir build && cd build
cmake ..
cmake --build .
```

## 5. Programmazione Modulare

```c
// file.h — header guard
#ifndef FILE_H
#define FILE_H
void funzione();
#endif

// file.c
#include "file.h"
void funzione() { ... }
```

## 6. Gestione Input/Output

```c
printf("Formato %d %s %f", int_val, str, float_val);
scanf("%d %s", &val, str);        // Attenzione: buffer overflow!
fgets(str, sizeof(str), stdin);   // Più sicuro

// File
FILE *f = fopen("file.txt", "r"); // r,w,a,r+,w+,a+
fscanf(f, "%d", &val);
fprintf(f, "%d", val);
fclose(f);
```

## 7. C++ (cenni)

- **Classi**: `class`, `public`/`private`, costruttori, distruttori
- **STL**: `vector`, `string`, `map`, `algorithm` (sort, find)
- **I/O stream**: `cin >>`, `cout <<`
- **New/Delete**: `int *p = new int(5); delete p;`

## 8. Esercizi Tipici

| Argomento | Esercizio |
|-----------|-----------|
| Variabili/operatori | Calcolatrice, conversione binario |
| Controllo | Indovina numero, is_primo, flowchart |
| Array | Ricerca max/min, media, ordinamento (bubble sort) |
| Matrici | Somma righe, trasposta, prodotto righe×colonne |
| Stringhe | Palindromo, conta vocali, substring |
| Puntatori | Swap, array dinamico, linked list |
| File | Lettura CSV, scrittura risultati, backup vettori |
| Ricorsione | Fattoriale, Fibonacci, torre di Hanoi |
| Strutture | Rubrica contatti, vettori con struct |
| Allocazione | Liste concatenate, vettore ridimensionabile |
