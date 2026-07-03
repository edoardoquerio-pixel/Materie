# 04. Crittografia DES e AES

**File:** `04. Crittografia DES e AES.pdf`
**Tipo:** `.pdf`
**Dimensione:** 18312.9 KB
**Ultima modifica:** 02/07/2026 09:25

---

Intervento realizzato da
Docente
Unità formativa
Argomento
Prof. Marco Farina
Sicurezza Informatica
Crittografia DES e AES
v 3.1.4 ~ feb 2026
changelog

Novecento: dalle lettere ai numeri
1943
1949
Bletchley Park
Communication Theory of Secrecy 
Systems
1969
 ARPANET
1976
 DES
1977
 Crittografia a chiave pubblica
1994
 SSL
1900
2000
1989
 World Wide Web


1Data Encryption 
Standard

DES
Input (64 bit)
Initial 
permutation
Left half (32)
Right half (32) Cipher 
function
⊕
Cipher 
function
⊕
Cipher 
function
⊕
Final 
permutation
Output (64 bit)
Key (64 bit)
Key 
permutation
L half (28)
R half (28)
L shift
L shift
Permutation
L shift
L shift
Permutation
L shift
L shift
Permutation
Subkey #1 (48)
Subkey #2 (48)
Subkey #16 (48)
Round 1
 Round 2
 Round 16

Crittoanalisi
Quanto è grande lo spazio delle chiavi?
K⋆=|Σ|L=256≈7,2⋅1016
Deep Crack
Chi
: 
distributed.net
 & EFF
Anno
: 1999
CPU
: 1536
Performance
: 92 miliardi di chiavi al secondo
Te m p o
: 22 ore e 15 minuti
Costo
: 200.000 
$

Crittoanalisi
Quanto è grande lo spazio delle chiavi?
K⋆=|Σ|L=256≈7,2⋅1016
Problema:
Conseguenza:
Soluzione?
spazio delle chiavi troppo piccolo.
attacco brute force.
…cifriamo TRE volte. (sigh
!
)


2Advanced 
Encryption Standard

Costruzione di AES
1997
Il NIST emette il 
bando per la 
costruzione di 
AES
Richieste tre caratteristiche: 
Sicurezza (chiave da 128+ bit) 
Efficienza computazionale 
Semplicità di implementazione
1999
L
’
algoritmo scelto è stato sviluppato da due crittografi belgi, Joan Daemen e Vincent 
Rijmen, che lo hanno presentato con il nome di 
Rijndael
, derivato dai loro nomi. 
Rijndael
, in fiammingo, si pronuncia [
ˈ
r
ɛ
inda
ː
l] (“rèin-daal”).

Input
328831e0
435a3137
f6309807
a88da234
2b28ab09
7eaef7cf
15d2154f
16a6883c
State
 Cipher Key
32
= 0011 0010 (1 byte)
Notazione esadecimale (esempio):
Questo è un blocco di 128 
bit preso dal messaggio in 
chiaro che deve essere 
cifrato.

Input
328831e0
435a3137
f6309807
a88da234
2b28ab09
7eaef7cf
15d2154f
16a6883c
State
 Cipher Key
al processo di 
cifratura
all’espansione 
della chiave

Processo di cifratura
Il procedimento di cifratura del blocco plaintext avviene usando 4 
differenti trasformazioni nel 
round iniziale
, nei 
9 round principali
 e nel 
round finale
.
In particolare vengono usate quattro fasi, una di permutazione e tre di 
sostituzione:
๏
Substitute bytes
: usa una 
S-Box
 per svolgere una sostituzione del 
blocco byte per byte.
๏
Shift rows
: una semplice permutazione.
๏
Mix columns
: una sostituzione che utilizza l
’
aritmetica sui campi di 
Galois 
GF(2
8
)
.
๏
Add round key
: una semplice operazione di XOR bit-a-bit del blocco 
corrente con una porzione della chiave espansa.

Processo di cifratura
State
AddRoundKey
SubBytes
ShiftRows
MixColumns
AddRoundKey
SubBytes
ShiftRows
AddRoundKey
Initial 
round
9/11/13 
main  
rounds
ﬁ
nal 
round
Cipher 
key
Round 
key 1-9
Round 
key 10

Le trasformazioni di AES
SubBytes
ShiftRows
MixColumns
AddRoundKey
Vediamo ora le quattro trasformazioni di AES. Per ogni 
trasformazione vedremo come funziona intuitivamente 
l
’
algoritmo di crittografia ed infine come avviene la 
trasformazione della chiave.

SubBytes
a09ae9
3df4c6f8
e3e28d48
be2b2a08
19
La trasformazione 
Substitute byte
 è una semplice ricerca su una 
tabella. AES definisce una matrice di dimensione 16x16 chiamata 
S-Box
 che contiene una permutazione di tutti i 256 valori a 8 bit.

SubBytes
a09ae9
3df4c6f8
e3e28d48
be2b2a08
19

SubBytes
a09ae9
3df4c6f8
e3e28d48
be2b2a08
19

SubBytes
a09ae9
3df4c6f8
e3e28d48
be2b2a08
19

SubBytes
a09ae9
3df4c6f8
e3e28d48
be2b2a08
19D4

SubBytes
a09ae9
3df4c6f8
e3e28d48
be2b2a08
D4


SubBytes
a09ae9
3df4c6f8
e3e28d48
be2b2a08
D4e0b81e
27bfb441
11985d52
aef1e530


ShiftRows
D4e0b81e
bfb441
11985d52
aef1e530
27

ShiftRows
D4e0b81e
bfb441
11985d52
aef1e530
Shift su 1 byte27

ShiftRows
D4e0b81e
bfb441
11985d52
aef1e530
27
Shift su 2 byte

ShiftRows
D4e0b81e
bfb441
11985d52
aef1e530
27
Shift su 3 byte

MixColumns
e0b81e
b44127
521198
D4
bf
5d
30aef1e5

MixColumns
e0b81e
b44127
521198
D4
bf
5d
30
aef1e5
02
03
01
01
01
02
03
01
01
01
02
03
03
01
01
02
×
Questa trasformazione opera su una singola colonna. 
Ciascun byte di una colonna viene mappato in un 
nuovo valore che è una funzione dei quattro byte 
presenti nella colonna. La trasformazione può essere 
definita dalla moltiplicazione in figura.

MixColumns
e0b81e
b44127
521198
D4
bf
5d
30
aef1e5
02
03
01
01
01
02
03
01
01
01
02
03
03
01
01
02
×
Nello standard la trasformazione viene definita considerando 
ciascuna colonna come un polinomio di quattro termini con 
coefficienti nel campo finito 
GF(2
8
)
. Ciascuna colonna viene 
moltiplicata modulo (
x
4
+1) per il polinomio fisso 
a
(
x
) dato da:
=
04
66
81
e5
a ( x )=3 x
3
+ x
2
+ x +2

MixColumns
e0b81e
b44127
521198
D4
bf
5d
30
aef1e5
02
03
01
01
01
02
03
01
01
01
02
03
03
01
01
02
×
Nello standard la trasformazione viene definita considerando 
ciascuna colonna come un polinomio di quattro termini con 
coefficienti nel campo finito 
GF(2
8
)
. Ciascuna colonna viene 
moltiplicata modulo (
x
4
+1) per il polinomio fisso 
a
(
x
) dato da:
=04
66
81
e5
a ( x )=3 x
3
+ x
2
+ x +2

MixColumns
e0b81e
b44127
521198
aef1e5
04
66
81
e5

MixColumns
e0b81e
b44127
521198
aef1e5
04
66
81
e5
e0
cb
19
9a
48
f8
d3
7a
28
06
26
4c

AddRoundKey
04
66
81
e5
e0
cb
19
9a
48
f8
d3
7a
28
06
26
4c
a0
fa
fe
17
88
54
2c
b1
23
a3
39
39
2a
6c
76
05
Round key
Prodotta nel primo 
passo di generazione 
delle chiavi

AddRoundKey
04
66
81
e5
e0
cb
19
9a
48
f8
d3
7a
28
06
26
4c
a0
fa
fe
17
Round key
⊕
a4
9c
7f
f2
=
88
54
2c
b1
23
a3
39
39
2a
6c
76
05
Prodotta nel primo 
passo di generazione 
delle chiavi

AddRoundKey
e0
cb
19
9a
48
f8
d3
7a
28
06
26
4c
Round key
a4
9c
7f
f2
88
54
2c
b1
23
a3
39
39
2a
6c
76
05
Prodotta nel primo 
passo di generazione 
delle chiavi

AddRoundKey
e0
cb
19
9a
48
f8
d3
7a
28
06
26
4c
a4
9c
7f
f2

AddRoundKey
e0
cb
19
9a
48
f8
d3
7a
28
06
26
4c
a4
9c
7f
f2
68
9f
35
2b
6b
5b
ea
43
02
6a
50
49

Rounds
I passi visti fin ora vengono applicati alla parola in input altre 9 
volte. Il round finale non include la trasformazione MixColumns.
Nel nostro esempio, il plaintext produce il seguente ciphertext:
39
02
dc
19
25
dc
11
6a
84
09
85
0b
1d
fb
97
32
328831e0
435a3137
f6309807
a88da234

Key schedule
La chiave di cifratura subisce un procedimento di 
espansione
 per 
generare 11 
chiavi parziali
, usate nel
’
initial round
, nei 9 
main round 
e nel 
final round
.
…
Cipher key
La chiave espansa può essere vista come un array di parole di 32 
bit, numerate da 0 a 43. La prima colonna è riempita con la chiave 
crittografica.
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
…

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
…
Le parole in posizione 
multiplo di 4 (
w
4
, 
w
8
, …, 
w
40
) 
vengono calcolate:
1.
applicare le trasformazioni 
RotWord
 e 
SubBytes
 alla 
precedente parola 
w
i-1
w
i

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
…
Le parole in posizione 
multiplo di 4 (
w
4
, 
w
8
, …, 
w
40
) 
vengono calcolate:
1.
applicare le trasformazioni 
RotWord
 e 
SubBytes
 alla 
precedente parola 
w
i-1
w
i
w
i-1
cf
4f
3c
09
RotWord

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
…
Le parole in posizione 
multiplo di 4 (
w
4
, 
w
8
, …, 
w
40
) 
vengono calcolate:
w
i
w
i-1
8a
84
eb
01
SubByte 
con S-Box

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
…
Le parole in posizione 
multiplo di 4 (
w
4
, 
w
8
, …, 
w
40
) 
vengono calcolate:
2.
Si somma (XOR) il risultato 
con la parola di 4 posizioni 
prima w
i-4
 più una 
costante 
Rcon
w
i
w
i-1
8a
84
eb
01
SubByte 
con S-Box

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
…
Le parole in posizione 
multiplo di 4 (
w
4
, 
w
8
, …, 
w
40
) 
vengono calcolate:
2.
Si somma (XOR) il risultato 
con la parola di 4 posizioni 
prima w
i-4
 più una 
costante 
Rcon
w
i
w
i-1
w
i-4
8a
84
eb
01
SubByte 
con S-Box
2b
7e
15
16
⊕

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
…
Le parole in posizione 
multiplo di 4 (
w
4
, 
w
8
, …, 
w
40
) 
vengono calcolate:
2.
Si somma (XOR) il risultato 
con la parola di 4 posizioni 
prima w
i-4
 più una 
costante 
Rcon
w
i
w
i-1
w
i-4
8a
84
eb
01
SubByte 
con S-Box
2b
7e
15
16
⊕
 ⊕
01
00
00
00
=
a0
fa
fe
17

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
…
a0
fa
fe
17
Cipher key
Round key 1

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
…
a0
fa
fe
17
Cipher key
Round key 1

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
a0
88
23
2a
fa
54
a3
6c
fe
2c
39
76
17
b1
39
05
f2
7a
59
73
c2
96
35
59
95
b9
80
f6
f2
43
7a
7f
d0
c9
e1
b6
14
ee
3f
63
f9
25
0c
0c
a8
89
c8
a6
…
Cipher key
Round key 1
Round key 2
 Round key 10
Riassumendo, il procedimento di 
key schedule
 è: 
๏
l’input è una parola di 32 bit e un numero di iterazione 
i
. L’output è 
una parola di 32 bit; 
๏
la parola in input viene copiata nell’output; 
๏
si applica la funzione 
Rotate
 de
ﬁ
nita precedentemente per ruotare 
l’output di otto bit verso sinistra; 
๏
si applica la 
S-box di R
ĳ
ndael
 su tutti e quattro i singoli byte della 
parola di output; 
๏
solo sul primo byte della parola di output, si applica l’or esclusivo tra 
il byte e 
Rcon(
i
)
.

Sicurezza di AES
AES per garantire la sua sicurezza effettua:
๏
10 round per la chiave a 128 bit,
๏
12 round per la chiave a 192 bit,
๏
14 round per la chiave a 256 bit.
I migliori attacchi sono riusciti a forzare l’AES con:
๏
7 round e chiave di 128 bit,
๏
8 round e chiave di 192 bit,
๏
9 round e chiave di 256 bit.
Attualmente, secondo i documenti segreti trafugati da 
Edward Snowden, l’NSA sta facendo ricerche per capire se 
un attacco basato sulla 
statistica tau
 possa aiutare a 
rompere AES.
 Non chiedetemi cosa 
essa sia, non lo so. 
!

Prestazioni
AES funziona su una grande varietà di dispositivi: dalle 
smart card a 8 bit 
ﬁ
no ai super-computer.
Attualmente, sui processori Intel Core i3/i5/i7, AMD APU e le 
cpu che supportano il set di istruzioni AES-NI, la cifratura 
AES arriva ad avere un throughput di 
700 MB/s per thread
.
AESDELIVERY
700 MB/s!

Learn by doing
La libreria openssl fornisce un’implementazione sicura 
dei principali cifrari. È bene provare a familiarizzare 
con alcuni dei comandi possibili.
Manuale eBook gratuito: 
https://www.feistyduck.com/books/
openssl-cookbook/
Approfondimento ed esercizi: 
https://rainbow-bits.notion.site/
openssl-aes-salt

