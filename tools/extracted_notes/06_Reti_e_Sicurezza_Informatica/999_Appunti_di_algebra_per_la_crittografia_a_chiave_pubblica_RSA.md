# Appunti di algebra per la crittografia a chiave pubblica RSA

Fonte: `Appunti di algebra per la crittografia a chiave pubblica RSA.pdf`

ITS ICT Piemonte

Corso di Sicurezza Informatica

Appunti di Algebra
per la crittograﬁa a chiave
pubblica RSA.

Prof. Marco Farina

marco.farina@its-ictpiemonte.it

Ultima revisione: 18 gennaio 2017.

Indice

1 Insiemi di numeri

Introduzione . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.1
1.2 Naturali, interi, razionali . . . . . . . . . . . . . . . . . . . . .

2 L’algoritmo di Euclide

3 I numeri primi

4 Relazioni di congruenza

5 Il teorema di Euler-Fermat

6 I sistemi di crittograﬁa

7 L’algoritmo RSA

2
2
2

3

5

6

7

11

13

Il presente testo `e tratto alle lezioni del prof. Alberto Albano presso il
Dipartimento di Informatica dell’Universit`a di Torino.
Questo testo `e stato scritto usando LATEX, sistema originariamente sviluppato da
Leslie Lamport, basato su TEX creato da Donald Knuth.

1 Insiemi di numeri

ITS ICT Piemonte

1

Insiemi di numeri

1.1

Introduzione

I numeri sono cos`ı pervasivi del nostro mondo che se ne comincia a fare
conoscenza nei primi anni di vita e se ne continua a fare un uso via via pi`u
approfondito nella vita quotidiana e nel percorso scolastico ﬁno alle scuole
superiori. Resta tuttavia indispensabile per gli studenti che hanno deciso
di intraprendere studi di carattere scientiﬁco o tecnico ritornarci di nuovo
nei corsi che utilizzano concetti matematici di base. L’esigenza nasce dalla
necessit`a di fare alcuni chiarimenti su alcuni aspetti delicati e profondi dei
numeri, che giocano poi un ruolo fondamentale in tutta quanta la matematica in generale e la crittologia in particolare. Non si tratta tanto di questioni
fondazionali sul concetto di numero, che in questa sede non verranno aﬀrontate, quanto di questioni concrete da tenere ben presenti da chiunque voglia
utilizzare lo strumento matematico con perizia e sicurezza.

1.2 Naturali, interi, razionali

I primi numeri che si incontrano sono gli interi positivi, detti anche
numeri naturali: 1, 2, 3, . . . . L’insieme dei numeri naturali si indica con
il simbolo N. Sono i numeri che servono a contare e che hanno fatto la
prima comparsa nelle societ`a umane svariate migliaia di anni fa. Per fare
misure di quantit`a ﬁsiche come lunghezze, aree, tempi, temperature, ecc.,
`e tuttavia necessario poter disporre di sottoparti dell’unit`a e considerare
quindi numeri frazionari m/n dove m, n ∈ N con n (cid:54)= 0. `E poi conveniente
anche introdurre i numeri con il segno per poter trattare grandezze negative
come possono essere la temperatura, la velocit`a e molte altre grandezze
ﬁsiche. Si ottengono cos`ı i seguenti insiemi numerici:

Z =

Q =

(cid:110)

0, ±1, ±2, . . .

(cid:111)

| m, n ∈ Z, n (cid:54)= 0

(cid:111)

(cid:110) m
n

numeri interi relativi,

numeri razionali.

Si hanno le evidenti inclusioni N ⊆ Z ⊆ Q. Talvolta `e anche utile considerare
gli insiemi

Z+ =

Q+ =

(cid:110)

(cid:110)

m ∈ Z | m ≥ 0
(cid:111)

q ∈ Q | q ≥ 0

(cid:111)

numeri interi non negativi,

numeri razionali non negativi.

pagina 2

2 L’algoritmo di Euclide

ITS ICT Piemonte

2 L’algoritmo di Euclide

Da bambini abbiamo imparato che quando si divide 27 per 6 il quoziente

`e 4 ed il resto `e 3, cio`e che

27 = 6 · 4 + 3.

La cosa importante da notare `e che il resto deve essere un intero maggiore
o uguale a 0 e minore in senso stretto di 6. Anche se `e vero che, ad esempio

27 = 6 · 3 + 9,

si prende come resto 3 e non 9 perch´e 3 `e il pi`u piccolo intero positivo per
cui vale l’identit`a.

La propriet`a fondamentale di cui ci stiamo occupando si pu`o enunciare

in modo preciso con il seguente teorema.

Teorema 2.1 (della divisione). Se a ≥ 0 e b > 0 sono interi, esistono e
sono univocamente determinati gli interi q ≥ 0 ed r tali che

a = bq + r

e

0 ≤ r < b.

q ed r sono detti rispettivamente il quoziente e il resto della divisione.

La determinazione del quoziente e del resto si pu`o fare utilizzando l’algoritmo della divisione che abbiamo imparato nella scuola elementare. Ad
esempio, si provi ad applicare l’algoritmo per ottenere quoziente e resto della
divisione di 2731 diviso 43.

Deﬁnizione 2.1. Dati due interi a e b diciamo che b `e un divisore di a,
e scriviamo b|a se, dividendo a per b si ottiene resto 0, cio`e se a = qb.
Equivalentemente si dice che b divide a, oppure che a `e divisibile per b,
oppure ancora che a `e un multiplo di b.

Deﬁnizione 2.2. Dati due interi a e b, il numero positivo d tale che

1. d | a e d | b,

2. se c | a e c | b allora c | d

`e detto il massimo comun divisore di a e b e denotato con

d = (a, b).

pagina 3

2 L’algoritmo di Euclide

ITS ICT Piemonte

La condizione 1 dice che d `e un divisore comune di a e b, e la condizione 2
dice che ogni divisore comune di a e b `e anche un divisore di d. Per esempio,
6 `e un divisore comune di 60 ed 84, ma non `e il massimo comun divisore,
dato che 12 | 60 e 12 | 84, ma 12 (cid:45) 6 (il simbolo (cid:45) signiﬁca “non divide”).

Deﬁnizione 2.3. Due numeri a, b sono detti coprimi se (a, b) = 1.

Esiste un famoso metodo per calcolare il massimo comun divisore di due

interi, basato sull’uso del quoziente e del resto.

Teorema 2.2 (Algoritmo di Euclide). Il massimo comun divisore di due
interi a, b si ottiene con il metodo delle divisioni successive seguenti:

a = bq + r0
b = r0q0 + r1
r0 = r1q1 + r2

...

rn−2 = rn−1qn−1 + rn
rn−1 = rnqn + 0

Poich´e i resti ri, con 0 ≤ i ≤ n, sono positivi e decrescenti, dopo un
numero ﬁnito di passi la divisione d`a resto 0. L’ultimo resto non nullo rn `e
il massimo comun divisore di a, b.

Se gi`a il primo resto `e uguale a zero, b divide a e quindi (a, b) = b.

Esempio. Determinare il massimo comun divisore di 1776 e 1492.
Soluzione. Si ha:

(1776, 1492) = (1492, 284),

(1492, 284) = (284, 72),

(284, 72) = (72, 68),

(72, 68) = (68, 4),

(68, 4) = 4,

essendo

essendo

essendo

essendo

essendo

1776 = 1 · 1492 + 284

1492 = 5 · 284 + 72

284 = 3 · 72 + 68

72 = 1 · 68 + 4

68 = 17 · 4.

Teorema 2.3 (Identit`a di Bezout). Se d = (a, b) `e il massimo comun
divisore di a e b, allora esistono due interi m ed n tali che

d = ma + nb.

ma + nb `e detta una combinazione lineare di a e b con coeﬃcienti m ed
n.

pagina 4

3 I numeri primi

ITS ICT Piemonte

3

I numeri primi

Un concetto di fondamentale importanza nella storia e nella pratica della
matematica `e quello di numero primo. Un numero intero p si dice primo
se

• p (cid:54)= 0, 1, −1;

• per ogni a ∈ Z se a divide p allora a ∈ {1, −1, p, −p}.

In altre parole, un intero `e un primo se `e diverso da 0, 1,-1, e non ha

divisori propri.

Il Lemma seguente descrive un’importante propriet`a dei numeri primi.

Lemma 3.1. Siano a, b, p ∈ Z con p primo:

se

p | ab allora p | a o

p | b.

Dimostrazione. supponiamo che p|ab. Se p|a la dimostrazione `e banale;
assumiamo quindi anche che p (cid:45) a. Allora (a, p) = 1, quindi esistono x, y ∈ Z
tali che xa + yp = 1, da cui si ottiene

b = 1 · b = xab + ypb;

poich´e p|ab, segue che p divide b.

Dimostriamo ora il cosiddetto Teorema Fondamentale dell’Aritmetica.

Teorema 3.1. Sia z ∈ Z un intero diverso da 0,1,-1. Allora esistono numeri
primi p1, p2, . . . , pn tali che

z = p1 · p2 · p3 · . . . · pn.

Inoltre tale fattorizzazione `e unica a meno del segno dei numeri primi e del
loro ordine nel prodotto.

Dimostrazione. (esistenza) Supponiamo prima z > 0 (quindi z ≥ 2) e
applichiamo il principio di induzione nella seconda forma.

Se z = 2 allora la dimostrazione `e banale. Supponiamo ora che z ≥ 3
e che, per ipotesi induttiva, una fattorizzazione in prodotto di primi esista
per ogni 2 ≤ k ≤ z − 1.

Se z `e primo, allora `e gi`a fattorizzato (con un solo fattore). Supponiamo
quindi che z non sia primo. Allora z ha almeno un divisore proprio k; quindi

pagina 5

4 Relazioni di congruenza

ITS ICT Piemonte

z = kb con 2 ≤ k, b ≤ z −1. Ma, per ipotesi induttiva, k e b sono un prodotto
di numeri primi, e quindi anche z `e tale.

Sia ora z < 0; allora −z > 0 e quindi, per quanto appena visto, −z = p1 ·
p2· p3· . . .· pn, con p1· p2· . . .· pn numeri primi; quindi z = (−p1)· p2· p3· . . .· pn.
La prova di esistenza `e completata.

Dimostrazione. (unicit`a) Supponiamo che p1, p2, . . . , pn e q1, q2, . . . , qs siano
primi tali che

p1 · p2 . . . pn = z = q1 · q2 . . . qs.

Allora p1|z = q1 · q2 . . . qs, quindi per l’osservazione che segue il Lemma
precedente, p1 divide almeno uno dei qi A meno di riordinare q1 · q2 . . . qs
possiamo supporre che p1|q1, ma allora, essendo primi, p1 = q1 oppure
p1 = −q1.

Dividendo ora z per p1 si ottiene dunque

p2 · p3 . . . pn =

z
p1

= ±q2 · q3 . . . qs.

Procedendo in questo modo alla ﬁne si ricava n = s, ed anche l’unicit`a dei
primi nelle due fattorizzazioni, a meno dell’ordine e dei segni.

Teorema 3.2 (di Euclide). Esistono inﬁniti numeri primi positivi.

Dimostrazione. Supponiamo per assurdo che l’insieme dei numeri primi positivi sia ﬁnito, e siano allora p1, p2, . . . , pt tutti i numeri primi positivi
distinti. Consideriamo il numero intero

N = p1 · p2 · p3 . . . pt + 1.

Allora N ≥ 2 e c’`e un fattore primo q di N . Essendo primo, q deve essere
uno dei pi; ma allora q|p1 · p2 . . . pt e quindi q divide N − p1 · p2 . . . pt = 1,
che `e assurdo.

4 Relazioni di congruenza

Deﬁnizione 4.1. Fissato un intero n, (n ≥ 2), due interi a, b ∈ Z sono detti
congruenti modulo n se n | b − a. In questo caso si scrive

a ≡ b

(mod n).

Teorema 4.1. Due interi sono congruenti modulo n se e solo se divisi per
n danno lo stesso resto.

pagina 6

5 Il teorema di Euler-Fermat

ITS ICT Piemonte

Dimostrazione. Consideriamo gli interi a e b. Dividendoli per n, otteniamo

a = q1n + r1,

b = q2n + r2,

con

0 ≤ r1, r2, < n.

Se r1 = r2, allora (b − a) = (q2 − q1)n, cio`e a e b sono congruenti modulo n

Viceversa, se a ≡ b (mod n), allora b − a = kn, da cui

b = a + kn = q1n + r1 + kn = (q1 + k)n + r1.

Dal Teorema della Divisione il resto `e univocamente determinato e quindi,
confrontando b = q2n + r2 e b = (q1 + k)n + r1, si ha che r1 = r2.

Il teorema precedente assicura che si pu`o scegliere come rappresentante
di ogni classe il resto della divisione per n. Possiamo allora usare la notazione
seguente:

Zn = {0, 1, 2, . . . , n − 1},

essendo 0, 1, 2, . . . , n − 1 i possibili resti della divisione di un numero per n.

Esempio. Dato n = 3, Z3 `e formato dalle 3 classi di congruenza seguenti:

0 = {. . . , −6, −3, 0, 3, 6, 9, . . . },

1 = {. . . , −5, −2, 1, 4, 7, 10, . . . },

2 = {. . . , −4, −1, 2, 5, 8, 11, . . . }.

`E possibile deﬁnire delle operazioni di somma e prodotto in Zn.

5

Il teorema di Euler-Fermat

In questa sezione vedremo una sorprendente applicazione della teoria
delle congruenze. Nel 1736 Euler diede una dimostrazione di una aﬀermazione di Fermat (1601-1665) che riguardava la relazione fra le potenze di un
numero e le sue classi di congruenza modulo un numero primo. Euler riusc`ı
anche a dimostrare una generalizzazione di questa aﬀermazione, valida per
ogni numero intero n, e non solo per i numeri primi. Ed `e proprio usando questo teorema (o meglio, una sua variante) che recentemente, Rivest,
Shamir e Adleman hanno inventato un metodo di crittograﬁa estremamente
eﬃciente e sicuro. Il metodo RSA `e uno dei pi`u usati oggi (per esempio,
`e implementato nel programma di pubblico dominio PGP – Pretty Good
Privacy) ed `e usato da molte autorit`a di certiﬁcazione riconosciute in rete.
Cominciamo enunciando quello che `e comunemente conosciuto come il

Piccolo Teorema di Fermat.

pagina 7

5 Il teorema di Euler-Fermat

ITS ICT Piemonte

Teorema 5.1 (Piccolo Teorema di Fermat). Sia p un numero primo, e sia
a un intero non divisibile per p. Allora

ap−1 ≡ 1 mod p.

Dimostrazione. Consideriamo i multipli di a

m1 = a, m2 = 2a, m3 = 3a,

. . . , mp−1 = (p − 1)a.

Nessuna coppia di questi numeri interi pu`o essere congrua modulo p: infatti,
in tal caso, p sarebbe un divisore di mr − ms = (r − s)a, dove r ed s
sono numeri interi 1 ≤ r < s ≤ p − 1, e poich´e r − s `e minore di p ed
inoltre p non divide a per ipotesi, questo non `e possibile. Dunque i numeri
m1, m2, . . . , mp−1 sono congrui ai numeri 1, 2, . . . , p − 1, considerati in un
ordine opportuno- Ma allora moltiplicando si ha

m1m2 . . . mp−1 = 1 · 2 · 3 · · · (p − 1)ap−1 ≡ 1 · 2 · 3 · · · (p − 1) mod p,

e se per brevit`a poniamo K = 1 · 2 · 3 · · · (p − 1) possiamo scrivere

K(ap−1 − 1) ≡ 0 mod p.

Ma K non `e divisibile per p, perch´e nessuno dei suoi fattori lo `e, e dunque
deve essere (ap−1 − 1) divisibile per p, cio`e

ap−1 ≡ 1 mod p.

Notiamo che se n non `e un numero primo, allora non si pu`o dire che
an−1 ≡ 1 mod n, in generale. Per esempio, se n = 4 e a = 3, si ha
33 = 27 ≡ 3 mod 4. Ci si pu`o dunque chiedere se ci sia una potenza di
a che sia congrua ad 1 modulo n. La risposta `e s`ı, e l’esponente corretto `e
stato trovato da Euler.

Deﬁnizione 5.1. Per un numero intero positivo n, indichiamo con ϕ(n) il
numero degli interi compresi fra 1 ed n coprimi con n.

pagina 8

5 Il teorema di Euler-Fermat

ITS ICT Piemonte

Per esempio,

ϕ(1) = 1

ϕ(2) = 1

ϕ(3) = 2

ϕ(4) = 2

ϕ(5) = 4

ϕ(6) = 2

ϕ(7) = 6

ϕ(8) = 4

ϕ(9) = 6

ϕ(10) = 4

. . .

perch´e 1 `e coprimo con 1,

1 `e coprimo con 2,

1 e 2 sono coprimi con 3,

1 e 3 sono coprimi con 4,

1, 2, 3 e 4 sono coprimi con 5,

1 e 5 sono coprimi con 6,

1, 2, 3, 4, 5 e 6 sono coprimi con 7,

1, 3, 5 e 7 sono coprimi con 8,

1, 2, 4, 5, 7 e 8 sono coprimi con 9,

1, 3, 7 e 9 sono coprimi con 10,

. . .

Una propriet`a della funzione ϕ `e evidente:

se p `e un numero primo, allora ϕ(p) = p − 1,

in quanto tutti i numeri 1, 2, . . . , p − 1 sono coprimi con p. Altrettanto
semplice `e calcolare ϕ(n) per un numero che sia potenza di un primo. La
formula `e la seguente:

se n = pa, con p numero primo, allora ϕ(n) = pa − pa−1.

Infatti, i numeri non coprimi con pa sono tutti i multipli di p, e ne ne sono
pa−1 minori di pa. Notiamo che se a = 1 (cio`e n = p `e primo) ritroviamo la
stessa formula di prima. Per esempio, ϕ(125) = ϕ(53) = 53 − 52 = 100.

L’ultima propriet`a della funzione ϕ `e quella che consente di calcolare

ϕ(n) per un numero qualsiasi. La formula `e

se m e n sono coprimi, cio`e (m, n) = 1, allora ϕ(m · n) = ϕ(m) · ϕ(n)

Per esempio, usando la tabella precedente, si ha ϕ(21) = ϕ(3 · 7) = 12,
ϕ(30) = ϕ(5 · 6) = 8, e cos`ı via. Come vediamo, `e molto semplice calcolare
ϕ(n) se si conosce la fattorizzazione di n. Questa `e la propriet`a che verr`a
sfruttata nell’algoritmo RSA.

Vediamo ora il Teorema di Euler-Fermat.

Teorema 5.2 (di Euler-Fermat). Sia n un intero positivo e a un intero
coprimo con n. Allora

aϕ(n) ≡ 1 mod n.

pagina 9

5 Il teorema di Euler-Fermat

ITS ICT Piemonte

Osserviamo che, se n `e primo, allora ϕ(n) = n − 1 e quindi ritroviamo il

Teorema di Fermat.

Ci si pu`o anche chiedere cosa capiti se (a, n) (cid:54)= 1. Per esempio, se

n = 6,a = 2, si ha

22 ≡ 4 mod 6
23 ≡ 2 mod 6
24 ≡ 2 mod 6

e cos`ı via, e vediamo che le potenze di 2 modulo 6 alternano fra 2 e 4 e non
si ottiene mai 1. Osserviamo per`o che il teorema di Euler-Fermat si pu`o
enunciare in modo equivalente come

Teorema 5.3 (di Euler-Fermat). Sia n un intero positivo ed a un intero
coprimo con n. Allora

aϕ(n)+1 ≡ a mod n.

In questa forma la conclusione del teorema vale anche per n = 6, a = 2.
Non `e per`o possibile eliminare del tutto l’ipotesi che a ed n siano coprimi
come mostra l’esempio n = 12, a = 2: si ha

22 ≡ 4 mod 12
23 ≡ 8 mod 12
24 ≡ 4 mod 12
25 ≡ 8 mod 12

e tutte le potenze successive alternano fra 4 e 8, e dunque non si riottiene
pi`u 2. Se per`o facciamo un’ipotesi su n, `e possibile eliminare la condizione
che a ed n siano coprimi.

Deﬁnizione 5.2. Un intero n si dice libero da quadrati se `e il prodotto
di numeri primi distinti, cio`e se non `e divisibile per nessun quadrato > 1.

Per esempio, 6 = 2 · 3 `e libero da quadrati, mentre 12 = 2 · 2 · 3 non lo

`e. Con questa deﬁnizione si pu`o enunciare il seguente teorema:

Teorema 5.4. Se n = p1 · p2, · · · pk `e libero da quadrati, allora

aϕ(n)+1 ≡ a mod n

per ogni intero a.

pagina 10

6 I sistemi di crittograﬁa

ITS ICT Piemonte

Osserviamo che la conclusione `e la stessa del Teorema di Euler-Fermat,
ma l’ipotesi (a, n) = 1 `e stata sostituita dall’ipotesi n libero da quadrati.
Usando il Teorema 5.4 si pu`o dimostrare facilmente per induzione che vale
il seguente risultato pi`u generale:

Deﬁnizione 5.3. Se n = p1 · p2, · · · pk `e libero da quadrati allora

ahϕ(n)+1 ≡ a mod n

per ogni intero a e per ogni intero h ≥ 1.

6

I sistemi di crittograﬁa

Il problema della crittograﬁa `e semplice da enunciare: ci sono due persone, il mittente ed il destinatario1, che chiameremo A e B, che vogliono comunicare fra loro senza che nessun altro possa leggere i loro messaggi. Dato
un messaggio M , che possiamo immaginare essere una sequenza di simboli
o numeri, A usa una funzione f (ovvero un algoritmo) che trasforma M in
un’altra sequenza C e invia questa sequenza. B usa un’altra funzione g che
trasforma C di nuovo nel messaggio originale M . Naturalmente, se qualcuno
intercetta C non deve essere in grado di usare la funzione g per decodiﬁcare
il messaggio.

L’idea di sistema crittograﬁco pu`o dunque essere resa mediante uno

schema del tipo:

M

f
−→ C

g
−→ M

dove M `e l’insieme dei messaggi, C quello dei messaggi cifrati ed f e g sono
funzioni tali che

f ◦ g = ιM

(quindi `e necessario che f sia iniettiva). f `e la procedura di cifratura e g
quella di decifratura.

Per ottenere ci`o, di solito si usa una chiave (per esempio una password).
Dunque la funzione che codiﬁca f non ha come argomento solo il messaggio
M , ma anche un altro parametro, la chiave k. In simboli

e la funzione g tale che

f (M, k) = C

g(C, k) = M

1In letteratura spesso chiamati Alice e Bob.

pagina 11

6 I sistemi di crittograﬁa

ITS ICT Piemonte

cosicch´e, conoscendo la chiave, si possa decrittare il messaggio. Questo
schema, che usa la stessa chiave k sia per la codiﬁca che per la decodiﬁca,
si chiama simmetrico.

In crittograﬁa si suppone che tutti siano a conoscenza dell’algoritmo che
usano f e g, perch´e `e sempre possibile avere questa informazione mediante
attivit`a di spionaggio o simili. Basare la segretezza delle comunicazioni sulla
segretezza dell’algoritmo non `e una buona idea. Invece la segretezza `e basata
sul fatto che solo il A e B conoscono la chiave. Infatti, l’algoritmo viene usato
sempre, mentre la chiave pu`o essere cambiata ogni volta. In questo modo,
anche se qualcuno “ruba” una chiave, la pu`o usare solo poche volte.

Questa situazione (cambiare spesso la chiave) richiede per`o un modo di
comunicare sicuro fra A e B. Un altro problema `e il seguente: se vi `e un solo
ricevente, ma molti mittenti, tutti i mittenti conoscono la chiave, e possono
leggere i messaggi l’uno dell’altro, cosa che un mittente certamente non
vuole. Questo `e il problema che il metodo a chiave pubblica vuole risolvere.
Lo schema `e il seguente:

B comunica pubblicamente una chiave e. A codiﬁca il messaggio
usando la funzione f = (M, e) = C e trasmette il messaggio.
B possiede un’altra chiave d privata. B decodiﬁca il messaggio
usando g = (C, d) = M .

Questo elimina il problema della distribuzione delle chiavi, e anche la chiave
che serve per codiﬁcare non `e quella che decodiﬁca, e quindi solo B pu`o
leggere i messaggi. Questo schema `e stato proposto per la prima volta
da Whitﬁeld Diﬃe e Martin Hellman nel 1976. Uno schema diﬀerente di
crittograﬁa a chiave pubblica `e stato proposto nello stesso anno da Ralph
Merkle.

Per fare un’analogia, un metodo simmetrico `e come una cassaforte, e
la chiave `e la combinazione per aprirla. Una persona che ha la chiave pu`o
aprire la cassaforte e depositare un documento (codiﬁcare un messaggio).
Un’altra persona con la chiave pu`o aprire la cassaforte e prendere il documento (decodiﬁcare il messaggio). Chi non ha la chiave (l’avversario, la spia,
ecc.) deve scassinare la cassaforte. Un metodo a chiave pubblica invece `e
come una buca delle lettere. Chiunque pu`o inﬁlare una lettera nella buca
(codiﬁcare il messaggio con la chiave pubblica), ma solo il proprietario della
buca ha la chiave per aprirla facilmente (decodiﬁcare il messaggio). Tutti
gli altri devono scassinare la buca delle lettere, e questo `e possibile, e anche
pi`u facile che scassinare una cassaforte, ma richiede tempo. Se il padrone
della buca ritira spesso la sua posta oppure se cambia spesso la serratura,
la sua posta `e al sicuro.

pagina 12

7 L’algoritmo RSA

ITS ICT Piemonte

Naturalmente, la domanda `e: funzioni f e g con le propriet`a richieste da
questo schema esistono? Si pu`o pensare che se si conosce la chiave e usata
per codiﬁcare il messaggio, e la funzione f che eﬀettua la codiﬁca, deve essere
possibile in qualche modo decodiﬁcare il messaggio, e cio`e un simile schema
non pu`o funzionare. L’intuizione di Rivest, Shamir e Adleman (1978) `e stata
che `e possibile costruire funzioni f e g tali che:

1. mediante la chiave privata d la decodiﬁca `e semplice e rapida, e

2. usando la conoscenza della funzione f e della chiave pubblica e, la

decodiﬁca `e possibile ma richiede troppo tempo per essere utile.

Per esempio, troppo tempo pu`o voler dire che eseguire tutti i calcoli necessari, anche usando i computer pi`u veloci a disposizione, richiede alcuni anni. `E
chiaro che leggere un messaggio segreto alcuni anni dopo che `e stato scritto
non `e di grande utilit`a.

7 L’algoritmo RSA

Descriviamo ora l’algoritmo RSA che, fra tutti gli algoritmi proposti per
la crittograﬁa a chiave pubblica che si sono rivelati sicuri, `e il pi`u semplice
sia da capire che da implementare.

B sceglie due numeri primi p e q, molto grandi, li moltiplica e forma il
numero n = pq, che `e libero da quadrati. Sappiamo che ϕ(n) = (p−1)(q−1).
Ora sceglie un numero e che sia coprimo con ϕ(n). La chiave pubblica per
codiﬁcare i messaggi `e la coppia (n, e). La funzione f per la codiﬁca `e la
seguente:

• si trasforma il messaggio in un numero M , minore di n, Se il messaggio

`e molto lungo, lo si spezza in blocchi pi`u piccoli M1, . . . , Mk;

• si calcola Ci = M e

i mod n per ogni i;

• si trasmette C1, . . . , Ck.

Per decodiﬁcare, si procede nel modo seguente: consideriamo l’equazione

ex ≡ 1 mod ϕ(n).

Poich´e e `e coprimo con ϕ(n), questa equazione ha una soluzione d, per cui
vale ed = 1 + hϕ(n). Allora la funzione g di decodiﬁca `e:

• si calcola Mi = Cd

i mod n.

pagina 13

7 L’algoritmo RSA

ITS ICT Piemonte

Infatti

Cd

i = (M e

i )d = M ed

i = M 1+hϕ(n)

i

≡ Mi mod n = Mi

dove la congruenza `e vera in virt`u della deﬁnizione 5.3 e l’ultima eguaglianza
vale in quanto Mi < n.

Facciamo qualche esempio semplice, tralasciando i calcoli. Se prendiamo

p = 47 e q = 71, allora

n = 47 · 71 = 3337

La chiave pubblica e deve essere coprima con

ϕ(3337) = (p − 1)(q − 1) = 46 · 79 = 3220

Scegliamo a caso un numero e coprimo con 3220, ad esempio e = 79, che
essendo primo `e sicuramente coprimo con 3220. In questo caso, calcolando
con l’algoritmo di Euclide si ottiene

3220 = 40 · 79 + 60

79 = 1 · 60 + 19

60 = 3 · 19 + 3

19 = 6 · 3 + 1

Calcolando con i resti si ottiene

(79, 3220) = 1 = 1019 · 79 − 25 · 3220

e dunque abbiamo la chiave privata d = 1019. Rendiamo pubblici n ed e,
teniamo segreto d ed eliminiamo p e q.

Per codiﬁcare il messaggio

M = 6882326879666683

per prima cosa lo spezziamo in blocchi pi`u piccoli. Poich´e n = 3337 ha
quattro cifre, blocchi di tre cifre vanno bene. Dunque il messaggio si spezza
in

M1 = 688
M2 = 232
M3 = 687
M4 = 966
M5 = 668
M6 = 003

pagina 14

7 L’algoritmo RSA

ITS ICT Piemonte

Il primo blocco `e codiﬁcato da

68879 mod 3337 = 1570 = C1

Notiamo che non bisogna elevare 688 alla 79-esima potenza (numero molto
grande) e poi ridurre modulo 3337. Invece, si calcola 6882 e si riduce modulo
3337, poi si moltiplica di nuovo per 688 e si riduce nuovamente modulo 3337
e cos`ı via, e in ogni passo i numeri sono piccoli. Ci sono metodi per calcolare
queste potenze in modo ancora pi`u veloce di quello descritto, rendendo cos`ı
la codiﬁca del messaggio veloce.

Ripetendo gli stessi passi su tutti gli altri blocchi otteniamo il messaggio

codiﬁcato

C = 1570 2756 2091 2276 2423 158

Decodiﬁcare il messaggio richiede le stesse operazioni usando l’esponente

d = 1019 sui blocchi di C. Si ha

15701019 mod 3337 = 688 = M1

e in modo simile per i blocchi successivi.

Perch´e questo metodo `e sicuro? In fondo, per ottenere la chiave privata
d basta conoscere ϕ(n) e tutti conoscono n. Il modo pi`u rapido di calcolare
ϕ(n) `e avere la decomposizione n = pq, cio`e dobbiamo fattorizzare n. Negli
anni recenti sono stati sviluppati molti metodi di fattorizzazione, ed il migliore di quelli attualmente noti si chiama “General Number Field Sieve”,
abbreviato in GFNS. La matematica che sta dietro questi algoritmi `e molto
complicata, e non possiamo in queste note dire niente al riguardo.

Piuttosto, `e interessante vedere alcuni risultati concreti. I dati che citeremo sono in continua evoluzione, perci`o possono diventare obsoleti anche
molto presto. Un aspetto interessante del problema della fattorizzazione `e
costituito dai cosiddetti RSA Challanges, le “sﬁde RSA”, che consistono in
una serie di numeri da fattorizzare. Iniziata negli anni ’90, questa sﬁda `e
uﬃcialmente terminata nel 2007.2 L’ultimo nuemero fattorizzato (12 dicembre 2009) `e noto come RSA 768, cio`e `e un numero che in rappresentazione

2Un archivio

`e disponibile presso

http://www.emc.com/emc-plus/rsa-labs/

historical/the-rsa-challenge-numbers.htm

pagina 15

7 L’algoritmo RSA

ITS ICT Piemonte

binaria ha 768 cifre, in notazione decimale ha 232 cifre. Il numero `e:

123018668453011775513049495838496272077285

356959533479219732245215172640050726365751

874520219978646938995647494277406384592519

255732630345373154826850791702612214291346

167042921431160222124047927473779408066535

1419597459856902143413

e i suoi due fattori primi sono

334780716989568987860441698482126908177047

949837137685689124313889828837938780022876

14711652531743087737814467999489

e

3674604366679959042824463379962795263227915

8164343087642676032283815739666511279233373

417143396810270092798736308917

Il tempo necessario per fattorizzare questi numeri `e notevole. L’algoritmo
GNFS `e composto da due parti, una preliminare per cercare una serie di
equazioni lineari da risolvere (sieving step) e una seconda in cui si risolve un
sistema di equazioni (matrix step). La prima pu`o essere eseguita in parallelo
su pi`u calcolatori, mentre la seconda deve essere fatta tutta insieme.

La fattorizzazione di RSA 768 ha richiesto l’equivalente di circa 1500
anni di lavoro di un processore AMD Opteron a 2.2 Ghz con 2GB di RAM
per il primo passo, mentre la risoluzione del sistema ha richiesto sei mesi di
lavoro ad un cluster di 80 processori AMD Opteron a 2.2 Ghz. In termini
di tempo reale, i calcoli per la fattorizzazione sono durati un paio di anni.3
In confronto RSA 663, un po’ pi`u piccolo, ha richiesto circa la met`a del
tempo. Si stima che fattorizzare RSA 1024, con 1024 cifre binarie (309 cifre
decimali) richieda circa 1000 volte il tempo occorso per fattorizzare RSA
768.

Cosa possiamo concludere: chiavi a 1024 bit sono abbastanza sicure oggi

e per ancora (forse) molti anni, mentre chiavi a 640 bits sono gi`a insicure.

3http://eprint.iacr.org/2010/006.pdf

pagina 16

7 L’algoritmo RSA

ITS ICT Piemonte

Si potrebbe osservare: non `e necessario trovare i fattori p e q, ma solo
calcolare ϕ(n). In questo caso per`o, se conosciamo p e q sappiamo calcolare
ϕ(n) semplicemente, bastano due sottrazioni e una moltiplicazione:

ϕ(n) = (p − 1)(q − 1)

Viceversa, conoscendo n e ϕ(n) `e facile trovare p e q, basta risolvere una
equazione di secondo grado. Ponendo B = pq e A = p + q si ha che
l’equazione

x2 − Ax + B = 0

ha come soluzioni esattamente p e q. Quindi, conoscendo ϕ(n) si ha un
algoritmo che in pochi passi, una somma e la risoluzione di un’equazione di
secondo grado, consente di fattorizzare il numero n. Dunque la complessit`a
di calcolo per determinare ϕ(n) `e equivalente alla complessit`a di fattorizzare
il numero n che, come abbiamo visto, `e piuttosto grande.

Questo spiega perch´e il metodo `e sicuro. `E per`o importante osservare
che nessuno ha mai dimostrato che fattorizzare il numero n `e veramente
cos`ı diﬃcile, ma solo che i migliori algoritmi conosciuti sono troppo lenti.
Potrebbe capitare che un giorno qualcuno scopra un metodo pi`u eﬃciente
per fattorizzare i numeri, ed allora il metodo RSA non sarebbe pi`u sicuro.
La crittograﬁa `e un argomento aﬀascinante, ed `e un campo in cui l’avvento dei computer ha portato grandi novit`a e possibilit`a di utilizzo. `E bene
osservare che non sempre il mittente ed il ricevente sono esseri umani, ma
potrebbero essere entrambi computer che devono comunicare fra loro, per
esempio un telefono cellulare che comunica con la rete di telefonia (non vogliamo che un telefono non autorizzato possa mettersi in contatto ed usare
le risorse della rete oppure che qualcuno possa intercettare la trasmissione
e ascoltare le nostre telefonate), oppure un computer che manda una richiesta ad un server, per esempio per fare una stampa (non vogliamo che tutti
possano usare le nostre stampanti) e cos`ı via. Quindi `e importante avere dei
metodi semplici per trasmettere in sicurezza.

La sicurezza di un sistema per`o non `e solo nella matematica che si usa,
ma anche nel protocollo. Possiamo avere il sistema pi`u sicuro del mondo, ma se riveliamo la chiave privata ad un estraneo la nostra sicurezza `e
irrimediabilmente compromessa.

pagina 17