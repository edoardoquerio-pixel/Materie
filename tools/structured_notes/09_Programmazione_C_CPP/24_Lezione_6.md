# Lezione 6

## Panoramica
LEZIONE 6 - Primo Programma in C

## Argomenti trattati
Database, Data Analytics, Linux, Reti, API REST

---
## Appunti

LEZIONE 6 - Primo Programma in C
Durata: 4 ore | Teoria: 2h | Esercizi: 2h
PARTE TEORICA (2 ore)
6.1 Introduzione al Linguaggio C (15 min)
1972: Dennis Ritchie crea il C ai Bell Labs (AT&T)
1978: Pubblicazione “The C Programming Language” (K&R)
1989: Standard ANSI C (C89)
1999: Standard C99 (nuove funzionalità)
2011: Standard C11 (thread, atomics)
2018: Standard C18 (correzioni bug)
Perché Studiare C?
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
Visual Studio Code: leggero, estensioni
Code::Blocks: IDE specifico per C/C++
CLion: professionale (JetBrains)
Dev-C++: semplice per principianti
Vim/Emacs: per puristi
GDB (GNU Debugger)
LLDB (LLVM Debugger)
Integrato nell’IDE
Processo di Compilazione
┌─────────────┐
│ Codice C │ esempio.c
└──────┬──────┘
┌─────────────┐
│PREPROCESSORE│ #include, #define
└──────┬──────┘
┌─────────────┐
│ COMPILATORE │ traduce in assembly
└──────┬──────┘
┌─────────────┐
│ ASSEMBLER │ crea codice oggetto
└──────┬──────┘
┌─────────────┐
│ LINKER │ collega librerie
└──────┬──────┘
┌─────────────┐
│ ESEGUIBILE │ esempio.exe / a.out
└─────────────┘
# Compilazione semplice
gcc programma.c -o programma
# Con warning abilitati (RACCOMANDATO!)
gcc -Wall -Wextra programma.c -o programma
# Con informazioni di debug
gcc -g programma.c -o programma
# Ottimizzazione
gcc -O2 programma.c -o programma
# Solo preprocessing
gcc -E programma.c
# Solo compilazione (no linking)
gcc -c programma.c
6.3 Struttura di un Programma C (20 min)
Il Primo Programma: Hello World
#include <stdio.h>
printf("Numero: %d\n", 42)
printf("Testo: %s\n" "Ciao");

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 006_lezione6_primo_c.md*
