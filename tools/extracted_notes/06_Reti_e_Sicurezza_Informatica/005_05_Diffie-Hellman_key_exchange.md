# Lezione 05

Fonte: `05. Diffie-Hellman key exchange.pdf`

Docente

Prof. Marco Farina

Unità formativa

Sicurezza Informatica

Argomento

Diffie-Hellman-Merkle key exchange

Intervento realizzato da

changelog

v 3.4.4 ~ mar 2026

crittografiche

1Le chiavi 

Proprietà delle chiavi crittografiche

Casuale

Protetta

Condivisa

La potenza di un sistema crittografico dipende 
dalla tecnica usata per condividere la chiave.

Come si può condividere la chiave?

Alice Liddell
Abingdon Road 42
Oxford

KEY
EXPRESS

A mano

Terza parte

Canale 
sicuro

I primi due metodi non sono utilizzabili in epoca informatica; il 
terzo presuppone che una chiave sia già stata scambiata.

Il metodo dei lucchetti

Il metodo dei lucchetti

Il metodo dei lucchetti

Il metodo dei lucchetti

Il metodo dei lucchetti

Il metodo dei lucchetti

Il metodo dei lucchetti

Il metodo dei lucchetti

Il metodo dei lucchetti

Il metodo dei lucchetti

Il metodo dei lucchetti

Il metodo dei lucchetti

Il metodo dei lucchetti

Perché questo metodo 
non può funzionare?

Composizione di cifrature

Chiave di Bob

abcdefghijklmnopqrstuvwxyz 
HFSUGTAKVDEOYJBPNXWCQRIMZL

Chiave di Alice

abcdefghijklmnopqrstuvwxyz 
CPMGATNOJEFWIQBURYHXSDZKLV

Messaggio
Cifrato da Bob
Cifrato da Alice
Decifrato da Bob
Decifrato da Alice

ci vediamo all una
SV RGUVHYB HOO QJH
HD YNSDOLP OBB REO
AJ MQCJLZP LOO VKL
ei cnaiywb yhh zxy

I puzzle 
di Merkle

I puzzle di Merkle

2n

 puzzle e 

Bob genera 
li pubblica.

I puzzle di Merkle

857

482739

Ogni puzzle, se risolto, 
contiene un ID e una 
chiave casuale.

2n

 puzzle e 

Bob genera 
li pubblica.

I puzzle di Merkle

2n

 puzzle e 

Bob genera 
li pubblica.

Alice sceglie 
casualmente un puzzle

I puzzle di Merkle

182374

537

2n

 puzzle e 

Bob genera 
li pubblica.

Alice sceglie 
casualmente un puzzle
…e lo risolve.

I puzzle di Merkle

537

182374

Alice invia l’ID a Bob e 
tiene copia della chiave

I puzzle di Merkle

537

182374

Bob sa quale puzzle risolvere 
per ottenere la chiave

182374

Alice invia l’ID a Bob e 
tiene copia della chiave

I puzzle di Merkle

537

2n−1
L’attaccante può intercettare l’ID, ma deve risolvere, in media, 
(ovvero la metà di quelli generati) per scoprire la chiave condivisa.

 puzzle 

Il metodo dei colori

Chiave segreta condivisa

Dati pubblici

Chiave segreta condivisa

NO.

2Fondamenti di 

matematica

Insiemi numerici

ℕ
Complessi

𝕀
Immaginari

π
2

3 + 2i

ℤ
Reali

ℚ
Razionali
ℝ
Interi

3
11

−1

ℂ
Naturali

 
 
 
 
 
 
Insiemi numerici

ℕ
Complessi

𝕀
Immaginari

π
2

3 + 2i

ℤ
Reali

ℚ
Razionali
ℝ
Interi

3
11

−1

ℂ
Naturali

 
 
 
 
 
 
DEF

Teorema della divisione
a ≥ 0 b > 0
 sono interi, esistono e sono univocamente 
 e 
Se 
determinati gli interi 

r
q ≥ 0
 ed 
a = bq + r

 tali che 
 e 

0 ≤ r < | b |

q

r
 ed 

 sono detti rispettivamente il quoziente e il resto della divisione.

a

q

q

…

q

q

r

b

r
q
 più un certo resto 
 blocchi grandi 
.

DEF

I numeri primi
 si dice primo se:
;
a ∈ ℝ a
, se 

p
Un numero intero 
p ≠ {−1, 1, 0}
๏
๏ per ogni 
In altre parole, un intero è un primo se è diverso da 
ha divisori propri.

 divide 

, allora 

p

a ∈ {−1, 1, p, − p}
.
{−1, 1, 0}

 e non 

1 2p 3p 4 5p 6 7p 8

PRIME AWARDS

9 10 11p 12 13p 14 15 16

Teorema fondamentale dell’aritmetica

DEF

Fattorizzazione
{−1, 0, 1}

 un intero diverso da 

. Allora esistono numeri 

z ∈ ℝ

Sia 
primi 

p1, p2, … , pn

 tali che

 z = p1 ⋅ p2 ⋅ … ⋅ pn
Inoltre tale fattorizzazione è unica, a meno del segno dei numeri primi 
e del loro ordine nel prodotto.

180

160

140

120

100

80

60

Euclide (Grecia, -III/-V sec.), negli Elementi, insieme all’esistenza 
della fattorizzazione, aveva dimostrato una proposizione, oggi nota 
come lemma di Euclide, dalla quale si ricava la proprietà di 
fattorizzazione unica. 
Il teorema fu poi dimostrato esplicitamente per la prima volta da 
Gauss nelle Disquisitiones Arithmeticae.

MATH DEPARTMENT
EUCLIDE

Aritmetica dell’orologio

Siamo a Londra e sono le 9 del mattino. Abbiamo un 
appuntamento tra 8 ore. A che ora abbiamo l’appuntamento?

11

10
9
8

7

12

1

5

6

2
3
4

Aritmetica dell’orologio

12

1

5

6

2
3
4

11

10
9
8

7

Aritmetica dell’orologio

Siamo a Londra e sono le 9 del mattino. Abbiamo un 
appuntamento tra 8 ore. A che ora abbiamo 
l’appuntamento?

5
Qual è il rapporto tra il 
 e il 

17
?

12

1

5

6

2
3
4

11

10
9
8

7

Aritmetica dell’orologio

Siamo a Londra e sono le 9 del mattino. Abbiamo un 
appuntamento tra 8 ore. A che ora abbiamo 
l’appuntamento?

5

12

1

5

6

2
3
4

5
Qual è il rapporto tra il 
 e il 
17 12
 e 

 è il resto della divisione intera tra 

!

17
?

Possiamo definire tutte le operazioni aritmetiche nel 
“mondo dell’orologio”.

n
Possiamo astrarre l’idea di orologio e immaginarlo con 
ore sul quadrante.

11

10
9
8

7

 
DEF

Relazioni di congruenza

n ≥ 2
n
Fissiamo un intero 
, con 
n | (b − a)
n
 se 
congruenti modulo 
a ≡ b mod n
a mod n = b
.

o, equivalentemente, 

. I due numeri 

a, b ∈ ℝ

 sono detti 

. In questo caso si scrive

Esempio (orologio).

Fissiamo 

n = 12

 e scegliamo 

a = 3 b = 15
 e 

.

Questi numeri sono congruenti in modulo 
vero. Dunque:

12

 se 

12 | (15 − 3)

, che è 

3 ≡ 15 mod 12

DEF

Invertibilità di una funzione
 è sia iniettiva che suriettiva, allora esiste 

f : X → Y
Se una funzione 
una corrispondenza biunivoca tra i due insiemi 
Si può in questo caso definire la funzione inversa

X Y
 e 

.

f −1(y) ⟺ f(x) = y

Una funzione viene detta unidirezionale (one-way function) se è 
computazionalmente difficile da invertire.

Merkle Key Exchange

3Diffie-Hellman-

Diffie, Hellman e Merkle
Ralph Merkle

Martin Hellman

Whitfield Diffie

Dopo due millenni di buio il problema 
dello scambio delle chiavi viene risolto 
nel 1976. 

È il primo metodo pratico per scambiare 
chiavi crittografiche in un canale insicuro 
ed è tutt’oggi comunemente usato.

A caccia di funzioni unidirezionali

an = b

an ≡ b mod c

n volte
a ⋅ a ⋅ … ⋅ a

b =

Quante volte?
a ⋅ a ⋅ … ⋅ a

b =

Non esiste un modo facile per calcolarlo! 
Bisogna provare tutti i numeri!

Problema:

3x mod 7 = 1

Soluzione: x = 6n, n ∈ ℝ, n ≥ 0

Esempio

31 mod 7 = 1
32 mod 7 = 1
33 mod 7 = 1
34 mod 7 = 1
35 mod 7 = 1
36 mod 7 = 1

3 = 7 ⋅ 0 + 3

9 = 7 ⋅ 1 + 2

27 = 7 ⋅ 3 + 6

81 = 7 ⋅ 11 + 4

243 = 7 ⋅ 34 + 5

Nope.

Nope.

Nope.

Nope.

Nope.

729 = 7 ⋅ 104 + 1

F**k yeah!

La funzione “logaritmo discreto”
ax = b mod n

gi = b mod p

Il modulo è un numero primo 

p

 e la base dell’esponente è un generatore del 

mod p
.

Ma… cosa diavolo è un generatore?

Cosa sono i generatori di un numero primo?
i = [1, p − 1]
Esempio: scegliamo 
i = 1
i = 2
i = 3

61 mod 17 = 6
62 mod 17 = 2
63 mod 17 = 12

g = 6 p = 17
 e 

6i mod p

. Calcoliamo 

 con 

10

14

13

15

12

11

4

6

9

8

3

5

2

7

1

i

16

6i mod 17

6

2

12

4

7

8

14

16

11

15

5

13

10

9

3

1

…

i = (p − 1)

616 mod 17 = 1

Possiamo quindi verificare che 
generati tutti i numeri da a 

g = 6
1 p − 1
.

 è un generatore di 

p = 17

 poiché dal calcolo vengono 

In un gruppo di interi modulo n, un numero primo relativo a n genera tutti gli elementi del gruppo, infatti se si 
utilizza la moltiplicazione mod n per generare elementi da un numero primo si può generare qualsiasi 
elemento del gruppo. 

In generale, un generatore di un gruppo è un elemento che “genera” il gruppo, ovvero che 
moltiplicato per un elemento del gruppo genera un altro elemento del gruppo e cosi via.

Dati pubblici

Chiave segreta condivisa

L’algoritmo Diffie-Hellman-Merkle

Di comune accordo vengono scelti 

g p
.
 e 

XB ∈ [1, p − 1]

XA ∈ [1, p − 1]

YB = gXB (mod p)

YA = gXA (mod p)

YA

YB

K = Y XB
A

(mod p)

K è la chiave 
segreta 
condivisa

K = Y XA
B

(mod p)

L’algoritmo Diffie-Hellman-Merkle

Di comune accordo vengono scelti 

g = 6 p = 17
.
 e 

XB = 10 ∈ [1, 16]

XA = 15 ∈ [1, 16]

YB = 610 (mod 17) = 15

YA = 615 (mod 17) = 3

YA = 3

YB = 15

K = 310 (mod 17) = 8

K = 1515 (mod 17) = 8

Supponiamo per assurdo che 

Per definizione sappiamo che 

Dimostrazione
KA ≠ KB
.
YA = gXA (mod p)

 e che 

YB = gXB (mod p)
.

Sappiamo inoltre che:
KA = Y XA

(mod p)

B

KB = Y XB

A

(mod p)

Ora sostituiamo nelle equazioni precedenti le definizioni di 

KA = (gXB (mod p))

XA (mod p)

YA

 e di 

YB
:
XB (mod p)

KB = (gXA (mod p))

KB = gXAXB (mod p)

KA = gXBXA (mod p)
KA = KB

Otteniamo che 

, che contraddice l’ipotesi per assurdo rendendola falsa.

Crittoanalisi
g = 6
p = 17
, il generatore 

Eve conosce il numero primo 
.
pubblici 
A partire da questi dati può calcolare la chiave condivisa ?K

YA = 3 YB = 15
 e 

 e i valori 

i

6i mod 17

1

6

2

2

3

12

4

4

5

7

6

8

7

8

9

10

11

12

13

14

15

16

14

16

11

15

5

13

10

9

3

1

Eve deve calcolare tutte le equazioni 

gi mod p

 finché non trova 

 oppure 

YA

YB
.

A questo punto il logaritmo discreto è invertito poiché viene individuata la 
.
componente segreta 
K

 può quindi essere facilmente calcolata con la sua equazione.

 oppure 

XA

XB

Perché la procedura è sicura?
Perché nelle implementazioni reali si usano numeri di

300cifre

middle attack

4Man-in-the-

Man-in-the-middle attack

Alice e Bob devono scambiarsi l’informazione pubblica.

Eve controlla il canale di comunicazione.

Man-in-the-middle attack

Alice e Bob inviano l’informazione, ma Eve le intercetta.

Man-in-the-middle attack

Alice e Bob inviano l’informazione, ma Eve le intercetta.

Man-in-the-middle attack

Eve crea delle versioni fraudolente delle informazioni pubbliche di Bob e Alice.

Man-in-the-middle attack

Eve spedisce le versioni fraudolente ingannando entrambi.

Man-in-the-middle attack

Expectation

Reality

B-E

B-E

A-E

A-E

Comunicazione

Comunicazione

Intercettazione

cifrata

cifrata

Alice e Bob credono di aver condiviso una chiave, ma l’hanno in realtà condivisa 
con Eve, che ora sta in mezzo alla conversazione e può intercettare tutto.

Risolvere il Man-in-the-middle

Canale

Come possiamo verificare che nessuno si sia 
messo in mezzo alla comunicazione? 

Verifica manuale

Certificazione
(tra due lezioni…)

Contromisure: Telegram

@marcofarina

Contromisure: Telegram

@marcofarina

Video call

Secret chats

Contromisure: WhatsApp

Contromisure: WhatsApp

Contromisure: WhatsApp

Contromisure: WhatsApp

Contromisure: WhatsApp

Contromisure: WhatsApp

Contromisure: WhatsApp

Contromisure: WhatsApp

Quindi nel mondo reale si usa DHM?

Telegram Voice Call authentication

“Keys for end-to-end encrypted calls are generated using the DiffieHellman key exchange. Users who are on a call can ensure that there is no 
MitM by comparing key visualizations.”

Signal key agreement protocol

“This document describes the "X3DH" (or "Extended Triple DiffieHellman") key agreement protocol. X3DH establishes a shared secret key 
between two parties who mutually authenticate each other based on 
public keys. X3DH provides forward secrecy and cryptographic 
deniability.”

5Crittografia 

end-to-end

Instant messaging: plain text

Execute 
order 66.

Instant messaging: plain text

Execute 
order 66.

Instant messaging: plain text

Execute 
order 66.

Instant messaging: encryption

Execute 
order 66.

Instant messaging: encryption

DHKE

Execute 
order 66.

1. Diffie-Hellman Key Exchange 

Instant messaging: encryption

AES Enc

Execute 
order 66.

1. Diffie-Hellman Key Exchange 

2. AES Encryption

Instant messaging: encryption

AES Enc

akdslncshlm
Execute 
mxdksjc
order 66.

1. Diffie-Hellman Key Exchange 

2. AES Encryption

Instant messaging: encryption

akdslncshlm
mxdksjc

AES Enc

Execute 
order 66.

Instant messaging: encryption

akdslncshlm
Execute 
order 66.
mxdksjc

AES Enc

Execute 
order 66.

Instant messaging: encryption

Execute 
order 66.

AES Enc

Execute 
order 66.

Instant messaging: encryption

Execute 
order 66.

AES Enc

Execute 
order 66.

Instant messaging: encryption

Execute 
mlcch0jod8b
kcnkrhxur
order 66.

AES Enc

Execute 
order 66.

Instant messaging: encryption

mlcch0jod8b
kcnkrhxur

Execute 
order 66.

Execute 
order 66.

AES Enc

Instant messaging: encryption

mlcch0jod8b
kcnkrhxur

Execute 
order 66.

AES Enc

Execute 
order 66.

Instant messaging: encryption

mlcch0jod8b
kcnkrhxur

AES Enc

Execute 
order 66.

DHKE

Execute 
order 66.

1. Diffie-Hellman Key Exchange

Instant messaging: encryption

mlcch0jod8b
kcnkrhxur

AES Enc

dfkjsdnecri2
Execute 
undn8woue
order 66.

AES Enc

Execute 
order 66.

1. Diffie-Hellman Key Exchange

2. AES Encryption

Instant messaging: encryption

mlcch0jod8b
kcnkrhxur

AES Enc

AES Enc

Execute 
order 66.

dfkjsdnecri2
Execute 
undn8woue
order 66.

Instant messaging: encryption

mlcch0jod8b
kcnkrhxur

AES Enc

AES Enc

Execute 
order 66.

dfkjsdnecri2
Execute 
Execute 
undn8woue
order 66.
order 66.

Instant messaging: encryption

mlcch0jod8b
kcnkrhxur

AES Enc

AES Enc

Execute 
order 66.

Execute 
order 66.

Instant messaging: end-to-end encryption

Execute 
order 66.

Instant messaging: end-to-end encryption

Execute 
order 66.

1. Diffie-Hellman Key Exchange

Instant messaging: end-to-end encryption

akdslncshlm
Execute 
mxdksjc
order 66.

1. Diffie-Hellman Key Exchange

2. AES Encryption

Instant messaging: end-to-end encryption

akdslncshlm
mxdksjc

Execute 
order 66.

1. Diffie-Hellman Key Exchange 

2. AES Encryption

Instant messaging: end-to-end encryption

akdslncshlm
akdslncshlm
mxdksjc
mxdksjc

Execute 
order 66.

1. Diffie-Hellman Key Exchange 

2. AES Encryption

Instant messaging: end-to-end encryption

akdslncshlm
mxdksjc

akdslncshlm
mxdksjc

Execute 
order 66.

1. Diffie-Hellman Key Exchange 

2. AES Encryption

Instant messaging: end-to-end encryption

akdslncshlm
mxdksjc

Execute 
order 66.

akdslncshlm
mxdksjc

1. Diffie-Hellman Key Exchange 

2. AES Encryption

Instant messaging: end-to-end encryption

akdslncshlm
mxdksjc

Execute 
order 66.

akdslncshlm
Execute 
mxdksjc
order 66.

1. Diffie-Hellman Key Exchange 

2. AES Encryption