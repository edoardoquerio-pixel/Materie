# Lezione 04

Fonte: `04. Crittografia DES e AES.pdf`

Docente

Prof. Marco Farina

Unità formativa

Sicurezza Informatica

Argomento

Crittografia DES e AES

Intervento realizzato da

changelog

v 3.1.4 ~ feb 2026

Novecento: dalle lettere ai numeri

1900

1943

1949

1969

1976

1977

1989

1994

Bletchley Park
Communication Theory of Secrecy 
Systems
ARPANET

DES

Crittografia a chiave pubblica

World Wide Web

SSL

2000

1Data Encryption 

Standard

Input (64 bit)

Initial 
permutation

Key (64 bit)

y
e
K

n
o
i
t
a
t
u
m
r
e
p

DES

Round 1

Round 2

Left half (32)

⊕

⊕

Right half (32)

Cipher 
function

Cipher 
function

)
8
4
(
1
#
y
e
k
b
u
S

)
8
4
(
2
#
y
e
k
b
u
S

Round 16

Output (64 bit)

Final 
permutation

⊕

Cipher 
function

)
8
4
(
6
1
#
y
e
k
b
u
S

L half (28)

L shift

L shift

L shift

Permutation

Permutation

Permutation

R half (28)

L shift

L shift

L shift

 
 
 
 
 
 
 
Crittoanalisi

Quanto è grande lo spazio delle chiavi?
K⋆ = | Σ |L
= 256 ≈ 7,2 ⋅ 1016

Deep Crack

Chi: distributed.net & EFF
Anno: 1999
CPU: 1536
Performance: 92 miliardi di chiavi al secondo
Tempo: 22 ore e 15 minuti
Costo: 200.000 $

Crittoanalisi

Quanto è grande lo spazio delle chiavi?
K⋆ = | Σ |L
= 256 ≈ 7,2 ⋅ 1016
Problema:
Conseguenza:
Soluzione?

…cifriamo TRE volte. (sigh!)

attacco brute force.

spazio delle chiavi troppo piccolo.

Encryption Standard

2Advanced 

Costruzione di AES

1997

1999

Il NIST emette il 
bando per la 
costruzione di 
AES

Richieste tre caratteristiche: 
Sicurezza (chiave da 128+ bit) 
Efficienza computazionale 
Semplicità di implementazione

L’algoritmo scelto è stato sviluppato da due crittografi belgi, Joan Daemen e Vincent 
Rijmen, che lo hanno presentato con il nome di Rijndael, derivato dai loro nomi. 
Rijndael, in fiammingo, si pronuncia [ˈrɛindaːl] (“rèin-daal”).

Input

State

Cipher Key

32 88 31 e0

2b 28 ab 09

43 5a 31 37

7e ae f7 cf

f6 30 98 07

15 d2 15 4f

a8 8d a2 34

16 a6 88 3c

Questo è un blocco di 128 
bit preso dal messaggio in 
chiaro che deve essere 
cifrato.

Notazione esadecimale (esempio):

32 = 0011 0010 (1 byte)

Input

State

Cipher Key

32 88 31 e0

2b 28 ab 09

43 5a 31 37

7e ae f7 cf

f6 30 98 07

15 d2 15 4f

a8 8d a2 34

16 a6 88 3c

al processo di 
cifratura

all’espansione 
della chiave

Processo di cifratura

Il procedimento di cifratura del blocco plaintext avviene usando 4 
differenti trasformazioni nel round iniziale, nei 9 round principali e nel 
round finale.
In particolare vengono usate quattro fasi, una di permutazione e tre di 
sostituzione:
๏ Substitute bytes: usa una S-Box per svolgere una sostituzione del 

blocco byte per byte.

๏ Shift rows: una semplice permutazione.
๏ Mix columns: una sostituzione che utilizza l’aritmetica sui campi di 

Galois GF(28).

๏ Add round key: una semplice operazione di XOR bit-a-bit del blocco 

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

Cipher 
key

Round 
key 1-9

Round 
key 10

Initial 
round

9/11/13 
main 
rounds

ﬁnal 
round

Le trasformazioni di AES

Vediamo ora le quattro trasformazioni di AES. Per ogni 
trasformazione vedremo come funziona intuitivamente 
l’algoritmo di crittografia ed infine come avviene la 
trasformazione della chiave.

SubBytes

ShiftRows

MixColumns

AddRoundKey

SubBytes

La trasformazione Substitute byte è una semplice ricerca su una 
tabella. AES definisce una matrice di dimensione 16x16 chiamata 
S-Box che contiene una permutazione di tutti i 256 valori a 8 bit.

19

a0 9a e9

3d f4 c6 f8

e3 e2 8d 48

be 2b 2a 08

SubBytes

19

a0 9a e9

3d f4 c6 f8

e3 e2 8d 48

be 2b 2a 08

SubBytes

19

a0 9a e9

3d f4 c6 f8

e3 e2 8d 48

be 2b 2a 08

SubBytes

19

a0 9a e9

3d f4 c6 f8

e3 e2 8d 48

be 2b 2a 08

SubBytes

19 D4

a0 9a e9

3d f4 c6 f8

e3 e2 8d 48

be 2b 2a 08

SubBytes

D4

a0 9a e9

3d f4 c6 f8

e3 e2 8d 48

be 2b 2a 08

SubBytes

D4 e0 b8 1e
a0 9a e9

27 bf b4 41
3d f4 c6 f8

11 98 5d 52
e3 e2 8d 48

ae f1 e5 30
be 2b 2a 08

ShiftRows

D4 e0 b8 1e

27

bf b4 41

11 98 5d 52

ae f1 e5 30

ShiftRows

D4 e0 b8 1e

bf b4 41

27

Shift su 1 byte

11 98 5d 52

ae f1 e5 30

ShiftRows

D4 e0 b8 1e

bf b4 41

27

5d 52

11 98

Shift su 2 byte

ae f1 e5 30

ShiftRows

D4 e0 b8 1e

bf b4 41

27

5d 52

11 98

30

ae f1 e5

Shift su 3 byte

MixColumns

D4

e0 b8 1e

bf

b4 41 27

5d

52 11 98

30 ae f1 e5

MixColumns

02 03 01 01

01 02 03 01

01 01 02 03

×

03 01 01 02

D4

bf

5d

30

Questa trasformazione opera su una singola colonna. 
Ciascun byte di una colonna viene mappato in un 
nuovo valore che è una funzione dei quattro byte 
presenti nella colonna. La trasformazione può essere 
definita dalla moltiplicazione in figura.

e0 b8 1e

b4 41 27

52 11 98

ae f1 e5

MixColumns

02 03 01 01

01 02 03 01

01 01 02 03

×

03 01 01 02

D4

bf

5d

30

=

04

66

81

e5

Nello standard la trasformazione viene definita considerando 
ciascuna colonna come un polinomio di quattro termini con 
coefficienti nel campo finito GF(28). Ciascuna colonna viene 
moltiplicata modulo (x4+1) per il polinomio fisso a(x) dato da:

a(x) = 3x3 + x2 + x + 2

e0 b8 1e

b4 41 27

52 11 98

ae f1 e5

MixColumns

02 03 01 01

01 02 03 01

01 01 02 03

×

03 01 01 02

D4

bf

5d

30

=

Nello standard la trasformazione viene definita considerando 
ciascuna colonna come un polinomio di quattro termini con 
coefficienti nel campo finito GF(28). Ciascuna colonna viene 
moltiplicata modulo (x4+1) per il polinomio fisso a(x) dato da:

a(x) = 3x3 + x2 + x + 2

04

e0 b8 1e

66

b4 41 27

81

52 11 98

e5

ae f1 e5

MixColumns

04

e0 b8 1e

66

b4 41 27

81

52 11 98

e5

ae f1 e5

MixColumns

04

e0 b8 1e
e0
48
28

66

b4 41 27
06
f8
cb

81

d3
19
52 11 98
26

e5

7a
9a
4c
ae f1 e5

AddRoundKey

04

e0

48

28

66

cb

f8

06

81

19

d3

26

e5

9a

7a

4c

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

Round key

Prodotta nel primo 
passo di generazione 
delle chiavi

AddRoundKey

04

66

81

e5

⊕

a0

fa

fe

17

=

a4

9c

7f

f2

e0

48

28

cb

f8

06

19

d3

26

9a

7a

4c

88

23

2a

54

a3

6c

2c

39

76

b1

39

05

Round key

Prodotta nel primo 
passo di generazione 
delle chiavi

AddRoundKey

a4

e0

48

28

9c

cb

f8

06

7f

19

d3

26

f2

9a

7a

4c

88

23

2a

54

a3

6c

2c

39

76

b1

39

05

Round key

Prodotta nel primo 
passo di generazione 
delle chiavi

AddRoundKey

a4

e0

48

28

9c

cb

f8

06

7f

19

d3

26

f2

9a

7a

4c

AddRoundKey

a4

68
e0

6b
48

02
28

9c

9f
cb

5b
f8

6a
06

7f

35
19

ea
d3

50
26

f2

2b
9a

43
7a

49
4c

Rounds

I passi visti fin ora vengono applicati alla parola in input altre 9 
volte. Il round finale non include la trasformazione MixColumns.
Nel nostro esempio, il plaintext produce il seguente ciphertext:

32 88 31 e0

39 02 dc 19

43 5a 31 37

25 dc 11 6a

f6 30 98 07

84 09 85 0b

a8 8d a2 34

1d fb 97 32

Key schedule

La chiave di cifratura subisce un procedimento di espansione per 
generare 11 chiavi parziali, usate nel’initial round, nei 9 main round 
e nel final round.

2b 28 ab 09

7e ae f7 cf

15 d2 15 4f

16 a6 88 3c

Cipher key

…

La chiave espansa può essere vista come un array di parole di 32 
bit, numerate da 0 a 43. La prima colonna è riempita con la chiave 
crittografica.

Key schedule

2b 28 ab 09

7e ae f7 cf

15 d2 15 4f

16 a6 88 3c

…

Key schedule

wi

2b 28 ab 09

7e ae f7 cf

15 d2 15 4f

16 a6 88 3c

…

Le parole in posizione 
multiplo di 4 (w4, w8, …, w40) 
vengono calcolate:

1. applicare le trasformazioni 
RotWord e SubBytes alla 
precedente parola wi-1

Key schedule

wi-1

wi

2b 28 ab 09

7e ae f7 cf

15 d2 15 4f

16 a6 88 3c

cf

4f

3c

09

RotWord

…

Le parole in posizione 
multiplo di 4 (w4, w8, …, w40) 
vengono calcolate:

1. applicare le trasformazioni 
RotWord e SubBytes alla 
precedente parola wi-1

Key schedule

wi-1

wi

2b 28 ab 09

7e ae f7 cf

15 d2 15 4f

16 a6 88 3c

8a

84

eb

01

SubByte 
con S-Box

…

Le parole in posizione 
multiplo di 4 (w4, w8, …, w40) 
vengono calcolate:

Key schedule

wi-1

wi

2b 28 ab 09

7e ae f7 cf

15 d2 15 4f

16 a6 88 3c

8a

84

eb

01

SubByte 
con S-Box

…

Le parole in posizione 
multiplo di 4 (w4, w8, …, w40) 
vengono calcolate:

2. Si somma (XOR) il risultato 
con la parola di 4 posizioni 
prima wi-4 più una 
costante Rcon

Key schedule

wi-4

wi-1

wi

2b 28 ab 09

7e ae f7 cf

15 d2 15 4f

16 a6 88 3c

2b

7e

15

16

⊕

8a

84

eb

01

SubByte 
con S-Box

…

Le parole in posizione 
multiplo di 4 (w4, w8, …, w40) 
vengono calcolate:

2. Si somma (XOR) il risultato 
con la parola di 4 posizioni 
prima wi-4 più una 
costante Rcon

Key schedule

wi-4

wi-1

wi

2b 28 ab 09

7e ae f7 cf

15 d2 15 4f

16 a6 88 3c

2b

7e

15

16

⊕

8a

84

eb

01

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

SubByte 
con S-Box

…

Le parole in posizione 
multiplo di 4 (w4, w8, …, w40) 
vengono calcolate:

2. Si somma (XOR) il risultato 
con la parola di 4 posizioni 
prima wi-4 più una 
costante Rcon

Key schedule

2b 28 ab 09

7e ae f7 cf

15 d2 15 4f

16 a6 88 3c

Cipher key Round key 1

…

a0

fa

fe

17

Key schedule

2b 28 ab 09

7e ae f7 cf

15 d2 15 4f

16 a6 88 3c

a0

fa

fe

17

Cipher key Round key 1

…

Key schedule

2b 28 ab 09

a0 88 23 2a

f2 7a 59 73

7e ae f7 cf

fa 54 a3 6c

c2 96 35 59

15 d2 15 4f

fe 2c 39 76

95 b9 80 f6

…

16 a6 88 3c

17 b1 39 05

f2 43 7a 7f

d0 c9 e1 b6

14 ee 3f 63

f9 25 0c 0c

a8 89 c8 a6

Cipher key Round key 1 Round key 2

Round key 10

Riassumendo, il procedimento di key schedule è: 
๏ l’input è una parola di 32 bit e un numero di iterazione i. L’output è 

una parola di 32 bit; 

๏ la parola in input viene copiata nell’output; 
๏ si applica la funzione Rotate deﬁnita precedentemente per ruotare 

l’output di otto bit verso sinistra; 

๏ si applica la S-box di Rĳndael su tutti e quattro i singoli byte della 

parola di output; 

๏ solo sul primo byte della parola di output, si applica l’or esclusivo tra 

il byte e Rcon(i).

Sicurezza di AES

AES per garantire la sua sicurezza effettua:

๏ 10 round per la chiave a 128 bit,

๏ 12 round per la chiave a 192 bit,

๏ 14 round per la chiave a 256 bit.

I migliori attacchi sono riusciti a forzare l’AES con:

๏ 7 round e chiave di 128 bit,

๏ 8 round e chiave di 192 bit,

๏ 9 round e chiave di 256 bit.

Attualmente, secondo i documenti segreti trafugati da 
Edward Snowden, l’NSA sta facendo ricerche per capire se 
un attacco basato sulla statistica tau possa aiutare a 
rompere AES.

Non chiedetemi cosa 
essa sia, non lo so. !

Prestazioni

AES funziona su una grande varietà di dispositivi: dalle 
smart card a 8 bit ﬁno ai super-computer.

Attualmente, sui processori Intel Core i3/i5/i7, AMD APU e le 
cpu che supportano il set di istruzioni AES-NI, la cifratura 
AES arriva ad avere un throughput di 700 MB/s per thread.

AES
DELIVERY
700 MB/s!

Learn by doing

La libreria openssl fornisce un’implementazione sicura 
dei principali cifrari. È bene provare a familiarizzare 
con alcuni dei comandi possibili.

Manuale eBook gratuito: https://www.feistyduck.com/books/
openssl-cookbook/

Approfondimento ed esercizi: https://rainbow-bits.notion.site/
openssl-aes-salt