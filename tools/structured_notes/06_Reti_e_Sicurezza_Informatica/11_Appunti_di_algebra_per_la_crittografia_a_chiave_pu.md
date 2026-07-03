# Appunti di algebra per la crittografia a chiave pubblica RSA

## Panoramica
marco.farina@its-ictpiemonte.it

## Argomenti trattati
Sicurezza, API REST, Reti

---
## Appunti

ITS ICT Piemonte
Corso di Sicurezza Informatica
Appunti di Algebra
per la crittograﬁa a chiave
Prof. Marco Farina
marco.farina@its-ictpiemonte.it
Ultima revisione: 18 gennaio 2017.
1 Insiemi di numeri
Introduzione . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2 Naturali, interi, razionali . . . . . . . . . . . . . . . . . . . . .
2 L’algoritmo di Euclide
3 I numeri primi
4 Relazioni di congruenza
5 Il teorema di Euler-Fermat
6 I sistemi di crittograﬁa
7 L’algoritmo RSA
Il presente testo `e tratto alle lezioni del prof. Alberto Albano presso il
Dipartimento di Informatica dell’Universit`a di Torino.
Questo testo `e stato scritto usando LATEX, sistema originariamente sviluppato da
Leslie Lamport, basato su TEX creato da Donald Knuth.
1 Insiemi di numeri
ITS ICT Piemonte
Insiemi di numeri
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
0, ±1, ±2, . . .
| m, n ∈ Z, n (cid:54)= 0
numeri interi relativi,
numeri razionali.
Si hanno le evidenti inclusioni N ⊆ Z ⊆ Q. Talvolta `e anche utile considerare
numeri interi non negativi,
numeri razionali non negativi.
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
2 L’algoritmo di Euclide
ITS ICT Piemonte

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_Appunti_di_algebra_per_la_crittografia_a_chiave_pubblica_RSA.md*
