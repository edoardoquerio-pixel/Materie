# Lezione 8

## Panoramica
LEZIONE 8 - Operatori ed Espressioni

## Argomenti trattati
API REST

---
## Appunti

LEZIONE 8 - Operatori ed Espressioni
Durata: 4 ore | Teoria: 2h | Esercizi: 2h
PARTE TEORICA (2 ore)
8.1 Introduzione agli Operatori (10 min)
Cos’è un Operatore?
Un operatore è un simbolo che indica un’operazione da eseguire su uno o più operandi.
int risultato = 5 + 3;
// │ │ └── operando 2
// │ └──── operatore
// └────── operando 1
Classificazione per Numero di Operandi
1. Operatori Unari (1 operando)
-x // negazione
++x // incremento
!x // NOT logico
2. Operatori Binari (2 operandi)
a + b // addizione
a > b // maggiore di
a && b // AND logico
3. Operatori Ternari (3 operandi)
condizione ? valore_se_vero : valore_se_falso
Classificazione per Tipo di Operazione
Aritmetici: +, -, *, /, %
Relazionali: <, >, <=, >=, ==, !=
Logici: &&, ||, !
Bitwise: &, |, ^, ~, <<, >>
Assegnazione: =, +=, -=, *=, /=, %=
Incremento/Decremento: ++, –
Altro: sizeof, ternario (?:), virgola (,)
8.2 Operatori Aritmetici (esempi e note)
1. Addizione (+)
int a = 5 + 3; // 8
float b = 2.5 + 1.3; // 3.8
int c = -10 + 15; // 5
2. Sottrazione (-)
int a = 10 - 3; // 7
float b = 5.5 - 2.3; // 3.2
int c = 0 - 5; // -5
**3. Moltiplicazione (*)**
int a = 4 * 3; // 12
float b = 2.5 * 4.0; // 10.0
int c = -3 * 5; // -15
4. Divisione (/)
int a = 10 / 3; // 3 (divisione intera!)
float b = 10.0 / 3.0; // 3.333...
float c = 10.0 / 3; // 3.333... (uno float basta)
int d = 10 / 0; // ERRORE! Undefined behavior
IMPORTANTE: Divisione intera vs reale
int x = 7, y = 2;
int r1 = x / y; // 3 (troncamento)
float r2 = x / y; // 3.0 (divisione intera, poi convertito)
float r3 = (float)x / y; // 3.5 (divisione reale) ✓
5. Modulo (%) - Resto della Divisione
int a = 10 % 3; // 1 (10 = 3*3 + 1)
int b = 15 % 4; // 3 (15 = 4*3 + 3)
int c = 20 % 5; // 0 (divisione esatta)
int d = 7 % 2; // 1 (pari=0, dispari=1)
// float e = 10.5 % 3.2; // ERRORE! % solo per interi
Usi pratici del modulo:
// Verificare se pari/dispari
if (n % 2 == 0) {
printf("Pari\n");
// Ciclare array (wraparound)
int indice = (i + 1) % array_size;
// Estrarre ultima cifra
int ultima_cifra = numero % 10;
// Estrarre cifre
int centinaia = numero / 100;
int decine = (numero / 10) % 10;
int unita = numero % 10;
Operatori Unari
int y = -x; // -5
int z = -(-x); // 5
Positivo (+) (raramente usato)
int x = +5; // equivalente a: int x = 5;
Esempi Completi
Esempio 1: Calcolo media
int voto1 = 8, voto2 = 7, voto3 = 9;
float media = (voto1 + voto2 + voto3) / 3.0; // 8.0
// Nota: 3.0 per divisione reale!

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 008_lezione8_operatori.md*
