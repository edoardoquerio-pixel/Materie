# Lezione 04

## Panoramica
Novecento: dalle lettere ai numeri

## Argomenti trattati
Sicurezza, Crittografia, Data Analytics, API REST

---
## Appunti

Prof. Marco Farina
Unità formativa
Sicurezza Informatica
Crittografia DES e AES
Intervento realizzato da
v 3.1.4 ~ feb 2026
Novecento: dalle lettere ai numeri
Communication Theory of Secrecy
Crittografia a chiave pubblica
1Data Encryption
Right half (32)
#
#
Output (64 bit)
#
Quanto è grande lo spazio delle chiavi?
= 256 ≈ 7,2 ⋅ 1016
Chi: distributed.net & EFF
Performance: 92 miliardi di chiavi al secondo
Tempo: 22 ore e 15 minuti
Costo: 200.000 $
Quanto è grande lo spazio delle chiavi?
= 256 ≈ 7,2 ⋅ 1016
…cifriamo TRE volte. (sigh!)
attacco brute force.
spazio delle chiavi troppo piccolo.
Encryption Standard
Costruzione di AES
Il NIST emette il
Richieste tre caratteristiche:
Sicurezza (chiave da 128+ bit)
Efficienza computazionale
Semplicità di implementazione
L’algoritmo scelto è stato sviluppato da due crittografi belgi, Joan Daemen e Vincent
Rijmen, che lo hanno presentato con il nome di Rijndael, derivato dai loro nomi.
Rijndael, in fiammingo, si pronuncia [ˈrɛindaːl] (“rèin-daal”).
Questo è un blocco di 128
bit preso dal messaggio in
chiaro che deve essere
Notazione esadecimale (esempio):
32 = 0011 0010 (1 byte)
Processo di cifratura
Il procedimento di cifratura del blocco plaintext avviene usando 4
differenti trasformazioni nel round iniziale, nei 9 round principali e nel
In particolare vengono usate quattro fasi, una di permutazione e tre di
๏ Substitute bytes: usa una S-Box per svolgere una sostituzione del
blocco byte per byte.
๏ Shift rows: una semplice permutazione.
๏ Mix columns: una sostituzione che utilizza l’aritmetica sui campi di
๏ Add round key: una semplice operazione di XOR bit-a-bit del blocco
corrente con una porzione della chiave espansa.
Processo di cifratura
Le trasformazioni di AES
Vediamo ora le quattro trasformazioni di AES. Per ogni
trasformazione vedremo come funziona intuitivamente
l’algoritmo di crittografia ed infine come avviene la
trasformazione della chiave.
La trasformazione Substitute byte è una semplice ricerca su una
tabella. AES definisce una matrice di dimensione 16x16 chiamata
S-Box che contiene una permutazione di tutti i 256 valori a 8 bit.
Shift su 1 byte
Shift su 2 byte
Shift su 3 byte
Questa trasformazione opera su una singola colonna.
Ciascun byte di una colonna viene mappato in un
nuovo valore che è una funzione dei quattro byte
presenti nella colonna. La trasformazione può essere
definita dalla moltiplicazione in figura.
Nello standard la trasformazione viene definita considerando
ciascuna colonna come un polinomio di quattro termini con
coefficienti nel campo finito GF(28). Ciascuna colonna viene
moltiplicata modulo (x4+1) per il polinomio fisso a(x) dato da:
a(x) = 3x3 + x2 + x + 2
Nello standard la trasformazione viene definita considerando
ciascuna colonna come un polinomio di quattro termini con
coefficienti nel campo finito GF(28). Ciascuna colonna viene
moltiplicata modulo (x4+1) per il polinomio fisso a(x) dato da:
a(x) = 3x3 + x2 + x + 2
Prodotta nel primo
passo di generazione

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 004_04_Crittografia_DES_e_AES.md*
