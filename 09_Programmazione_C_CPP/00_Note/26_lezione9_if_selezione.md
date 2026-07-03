# lezione9 if selezione

**File:** `lezione9 if selezione.pdf`
**Tipo:** `.pdf`
**Dimensione:** 629.1 KB
**Ultima modifica:** 02/07/2026 09:24

---

LEZIONE 9 - Costrutto di Selezione: if-else
Durata: 4 ore | Teoria: 2h | Esercizi: 2h
PARTE TEORICA (2 ore)
9.1 Introduzione alla Selezione (10 min)
Cos’è la Selezione?
La 
selezione
 (o alternativa) permette al programma di scegliere quale blocco di codice
eseguire in base a una 
condizione
.
Analogia vita reale:
SE piove ALLORA
    prendi ombrello
ALTRIMENTI
    lascia ombrello a casa
Flusso di Controllo
Senza selezione (sequenziale):
Istruzione 1
Istruzione 2
Istruzione 3
Istruzione 4
Tutte le istruzioni vengono sempre eseguite.
Con selezione:
Istruzione 1
SE condizione ALLORA
    Istruzione 2  ← Eseguita solo se vera
ALTRIMENTI
    Istruzione 3  ← Eseguita solo se falsa
Istruzione 4
Flow Chart: Selezione

        ┌─────────┐
        │ Inizio  │
        └────┬────┘
             │
        ┌────┴────┐
        │Istruzione│
        │    1    │
        └────┬────┘
             │
          
╱
──┴──
╲
         
╱
Condiz?
╲
        
╱
____ ____
╲
       SI│        │NO
         │        │
    ┌────┴────┐ ┌┴────────┐
    │Istruzione│ │Istruzione│
    │    2    │ │    3    │
    └────┬────┘ └┬────────┘
         │        │
         └────┬───┘
              │
        ┌─────┴─────┐
        │Istruzione 4│
        └─────┬─────┘
              │
        ┌─────┴─────┐
        │   Fine    │
        └───────────┘
9.2 Istruzione if Semplice (15 min)
Sintassi Base
Componenti:
 - 
if
: parola chiave - 
condizione
: espressione booleana (vera/falsa) - 
{ }
:
blocco di codice (facoltativo se una sola istruzione)
Esempi Base
Esempio 1: Controllo età
Esempio 2: Numero positivo
Esempio 3: Verifica divisibilità
Blocco Singola vs Multipla Istruzione
if
 
(
condizione
)
 
{
    
// Codice eseguito SE condizione è vera
}
int
 eta 
=
 
20
;
if
 
(
eta 
>=
 
18
)
 
{
    printf
(
"Sei maggiorenne
\n
"
);
}
int
 x 
=
 
5
;
if
 
(
x 
>
 
0
)
 
{
    printf
(
"Il numero è positivo
\n
"
);
}
int
 n 
=
 
10
;
if
 
(
n 
%
 
2
 
==
 
0
)
 
{
    printf
(
"
%d
 è pari
\n
"
,
 n
);
}

Una istruzione (parentesi opzionali):
Più istruzioni (parentesi OBBLIGATORIE):
ERRORE comune (senza parentesi):
Best Practice:
 Usa SEMPRE le parentesi graffe, anche per singola istruzione!
Condizioni Complesse
AND logico (&&):
OR logico (||):
NOT logico (!):
Condizioni nidificate:
if
 
(
x 
>
 
0
)
    printf
(
"Positivo
\n
"
);
// Equivalente a:
if
 
(
x 
>
 
0
)
 
{
    printf
(
"Positivo
\n
"
);
}
if
 
(
x 
>
 
0
)
 
{
    printf
(
"Il numero è positivo
\n
"
);
    x 
=
 x 
*
 
2
;
    printf
(
"Raddoppiato: 
%d\n
"
,
 x
);
}
if
 
(
x 
>
 
0
)
    printf
(
"Positivo
\n
"
);
    x 
=
 x 
*
 
2
;
  
// SEMPRE eseguito! Non fa parte dell'if
// Corretto:
if
 
(
x 
>
 
0
)
 
{
    printf
(
"Positivo
\n
"
);
    x 
=
 x 
*
 
2
;
  
// Ora fa parte dell'if
}
int
 eta 
=
 
25
;
char
 patente 
=
 
'S'
;
if
 
(
eta 
>=
 
18
 
&&
 patente 
==
 
'S'
)
 
{
    printf
(
"Puoi guidare
\n
"
);
}
int
 giorno 
=
 
7
;
if
 
(
giorno 
==
 
6
 
||
 giorno 
==
 
7
)
 
{
    printf
(
"È weekend!
\n
"
);
}
int
 piove 
=
 
0
;
  
// 0 = no, 1 = sì
if
 
(!
piove
)
 
{
    printf
(
"Non serve ombrello
\n
"
);
}
int
 voto 
=
 
28
;
if
 
(
voto 
>=
 
18
)
 
{
    
if
 
(
voto 
>=
 
27
)
 
{
        printf
(
"Ottimo!
\n
"
);
    
}
}

Valori di Verità
In C, 
0 è falso
, tutto il resto è 
vero
.
9.3 Istruzione if-else (20 min)
Sintassi
Caratteristiche:
 - Esattamente UN blocco viene eseguito - Se condizione vera → esegue
primo blocco - Se condizione falsa → esegue secondo blocco
Flow Chart: if-else
          
╱
──────
╲
         
╱
Condiz? 
╲
        
╱
____ _____
╲
       SI│         │NO
         │         │
    ┌────┴────┐ ┌─┴─────┐
    │ Blocco  │ │ Blocco│
    │   if    │ │  else │
    └────┬────┘ └─┬─────┘
         │        │
         └────┬───┘
              │
         (continua)
Esempi
Esempio 1: Pari o dispari
Esempio 2: Maggiore/minore
int
 x 
=
 
5
;
if
 
(
x
)
 
{
  
// Vero perché x = 5 (≠ 0)
    printf
(
"x è vero
\n
"
);
}
int
 y 
=
 
0
;
if
 
(
y
)
 
{
  
// Falso perché y = 0
    printf
(
"Non stampato
\n
"
);
}
if
 
(!
y
)
 
{
  
// Vero perché NOT di 0
    printf
(
"y è falso
\n
"
);
}
if
 
(
condizione
)
 
{
    
// Codice SE condizione è vera
}
 
else
 
{
    
// Codice SE condizione è falsa
}
int
 n
;
printf
(
"Inserisci numero: "
);
scanf
(
"
%d
"
,
 
&
n
);
if
 
(
n 
%
 
2
 
==
 
0
)
 
{
    printf
(
"
%d
 è pari
\n
"
,
 n
);
}
 
else
 
{
    printf
(
"
%d
 è dispari
\n
"
,
 n
);
}

Esempio 3: Temperatura
Esempio 4: Login semplice
Confronto con Operatore Ternario
Quando usare ternario vs if-else:
 - Ternario: assegnazioni semplici - if-else: logica
complessa, più istruzioni
9.4 if-else if-else (Selezione Multipla) (20 min)
Sintassi
Caratteristiche:
 - Le condizioni vengono testate 
in ordine
 - Viene eseguito 
solo il primo
blocco con condizione vera - 
else
 finale è 
opzionale
 (caso di default)
int
 a 
=
 
10
,
 b 
=
 
20
;
if
 
(
a 
>
 b
)
 
{
    printf
(
"
%d
 è maggiore di 
%d\n
"
,
 a
,
 b
);
}
 
else
 
{
    printf
(
"
%d
 è minore o uguale a 
%d\n
"
,
 a
,
 b
);
}
float
 temp
;
printf
(
"Temperatura (°C): "
);
scanf
(
"
%f
"
,
 
&
temp
);
if
 
(
temp 
>=
 
25.0
)
 
{
    printf
(
"Fa caldo
\n
"
);
}
 
else
 
{
    printf
(
"Fa fresco
\n
"
);
}
int
 password_corretta 
=
 
1234
;
int
 password_inserita
;
printf
(
"Inserisci password: "
);
scanf
(
"
%d
"
,
 
&
password_inserita
);
if
 
(
password_inserita 
==
 password_corretta
)
 
{
    printf
(
"Accesso consentito
\n
"
);
}
 
else
 
{
    printf
(
"Password errata!
\n
"
);
}
// Con if-else
int
 max
;
if
 
(
a 
>
 b
)
 
{
    max 
=
 a
;
}
 
else
 
{
    max 
=
 b
;
}
// Con operatore ternario (più compatto)
int
 max 
=
 
(
a 
>
 b
)
 
?
 a 
:
 b
;
if
 
(
condizione1
)
 
{
    
// Se condizione1 è vera
}
 
else
 
if
 
(
condizione2
)
 
{
    
// Se condizione1 falsa E condizione2 vera
}
 
else
 
if
 
(
condizione3
)
 
{
    
// Se condizioni precedenti false E condizione3 vera
}
 
else
 
{
    
// Se tutte le condizioni precedenti sono false
}

Flow Chart: if-else if-else
       
╱
────────
╲
      
╱
Condizione
╲
  NO
     
╱
     1?     
╲
───────┐
    
╱
______________
╲
 SI   │
           │               │
      ┌────┴────┐          │
      │ Blocco  │          │
      │    1    │          │
      └────┬────┘          │
           │               │
           │           
╱
───┴───
╲
           │          
╱
Condizione
╲
  NO
           │         
╱
     2?     
╲
───────┐
           │        
╱
______________
╲
 SI   │
           │               │               │
           │          ┌────┴────┐          │
           │          │ Blocco  │          │
           │          │    2    │          │
           │          └────┬────┘          │
           │               │               │
           │               │          ┌────┴────┐
           │               │          │ Blocco  │
           │               │          │  else   │
           │               │          └────┬────┘
           │               │               │
           └───────────────┴───────────────┘
                           │
                      (continua)
Esempi
Esempio 1: Valutazione voto
Esempio 2: Classificazione BMI
int
 voto
;
printf
(
"Inserisci voto (0-100): "
);
scanf
(
"
%d
"
,
 
&
voto
);
if
 
(
voto 
>=
 
90
)
 
{
    printf
(
"Ottimo
\n
"
);
}
 
else
 
if
 
(
voto 
>=
 
80
)
 
{
    printf
(
"Buono
\n
"
);
}
 
else
 
if
 
(
voto 
>=
 
70
)
 
{
    printf
(
"Discreto
\n
"
);
}
 
else
 
if
 
(
voto 
>=
 
60
)
 
{
    printf
(
"Sufficiente
\n
"
);
}
 
else
 
{
    printf
(
"Insufficiente
\n
"
);
}
float
 bmi
;
printf
(
"BMI: "
);
scanf
(
"
%f
"
,
 
&
bmi
);
if
 
(
bmi 
<
 
18.5
)
 
{
    printf
(
"Sottopeso
\n
"
);
}
 
else
 
if
 
(
bmi 
<
 
25.0
)
 
{
    printf
(
"Normopeso
\n
"
);
}
 
else
 
if
 
(
bmi 
<
 
30.0
)
 
{
    printf
(
"Sovrappeso
\n
"
);
}
 
else
 
if
 
(
bmi 
<
 
35.0
)
 
{
    printf
(
"Obesità classe I
\n
"
);
}
 
else
 
if
 
(
bmi 
<
 
40.0
)
 
{
    printf
(
"Obesità classe II
\n
"
);
}
 
else
 
{
    printf
(
"Obesità classe III
\n
"
);
}

Esempio 3: Giorni del mese
Esempio 4: Classificazione temperatura
Ordine delle Condizioni
IMPORTANTE:
 L’ordine conta!
Corretto:
ERRATO:
Regola:
 Metti condizioni 
più specifiche prima
, 
più generali dopo
.
9.5 if Annidati (Nidificazione) (20 min)
Concetto
int
 mese
;
printf
(
"Inserisci mese (1-12): "
);
scanf
(
"
%d
"
,
 
&
mese
);
if
 
(
mese 
==
 
2
)
 
{
    printf
(
"28 o 29 giorni (febbraio)
\n
"
);
}
 
else
 
if
 
(
mese 
==
 
4
 
||
 mese 
==
 
6
 
||
 mese 
==
 
9
 
||
 mese 
==
 
11
)
 
{
    printf
(
"30 giorni
\n
"
);
}
 
else
 
if
 
(
mese 
>=
 
1
 
&&
 mese 
<=
 
12
)
 
{
    printf
(
"31 giorni
\n
"
);
}
 
else
 
{
    printf
(
"Mese non valido
\n
"
);
}
float
 temp
;
printf
(
"Temperatura (°C): "
);
scanf
(
"
%f
"
,
 
&
temp
);
if
 
(
temp 
<
 
0
)
 
{
    printf
(
"Sotto zero (ghiaccio)
\n
"
);
}
 
else
 
if
 
(
temp 
<
 
15
)
 
{
    printf
(
"Freddo
\n
"
);
}
 
else
 
if
 
(
temp 
<
 
25
)
 
{
    printf
(
"Mite
\n
"
);
}
 
else
 
if
 
(
temp 
<
 
35
)
 
{
    printf
(
"Caldo
\n
"
);
}
 
else
 
{
    printf
(
"Molto caldo
\n
"
);
}
if
 
(
x 
>
 
90
)
 
{
    printf
(
"A
\n
"
);
}
 
else
 
if
 
(
x 
>
 
80
)
 
{
    printf
(
"B
\n
"
);
}
 
else
 
if
 
(
x 
>
 
70
)
 
{
    printf
(
"C
\n
"
);
}
// Se x = 95, stampa "A" (primo vero)
if
 
(
x 
>
 
70
)
 
{
          
// Troppo generale!
    printf
(
"C
\n
"
);
}
 
else
 
if
 
(
x 
>
 
80
)
 
{
   
// Mai raggiunto se x > 70
    printf
(
"B
\n
"
);
}
 
else
 
if
 
(
x 
>
 
90
)
 
{
   
// Mai raggiunto
    printf
(
"A
\n
"
);
}
// Se x = 95, stampa "C" (sbagliato!)

Un 
if annidato
 è un if dentro un altro if.
Esempi
Esempio 1: Accesso con doppia verifica
Esempio 2: Classificazione numero
Esempio 3: Triangolo valido e tipo
if
 
(
condizione_esterna
)
 
{
    
// Blocco esterno
    
if
 
(
condizione_interna
)
 
{
        
// Blocco interno (eseguito solo se entrambe vere)
    
}
}
int
 eta
;
char
 patente
;
printf
(
"Età: "
);
scanf
(
"
%d
"
,
 
&
eta
);
if
 
(
eta 
>=
 
18
)
 
{
    printf
(
"Hai patente? (S/N): "
);
    scanf
(
" 
%c
"
,
 
&
patente
);
    
    
if
 
(
patente 
==
 
'S'
 
||
 patente 
==
 
's'
)
 
{
        printf
(
"Puoi noleggiare auto
\n
"
);
    
}
 
else
 
{
        printf
(
"Serve patente
\n
"
);
    
}
}
 
else
 
{
    printf
(
"Sei troppo giovane
\n
"
);
}
int
 n
;
printf
(
"Inserisci numero: "
);
scanf
(
"
%d
"
,
 
&
n
);
if
 
(
n 
==
 
0
)
 
{
    printf
(
"Il numero è zero
\n
"
);
}
 
else
 
{
    
if
 
(
n 
>
 
0
)
 
{
        printf
(
"Il numero è positivo
\n
"
);
        
if
 
(
n 
%
 
2
 
==
 
0
)
 
{
            printf
(
"ed è anche pari
\n
"
);
        
}
 
else
 
{
            printf
(
"ed è anche dispari
\n
"
);
        
}
    
}
 
else
 
{
        printf
(
"Il numero è negativo
\n
"
);
        
if
 
(
n 
%
 
2
 
==
 
0
)
 
{
            printf
(
"ed è anche pari
\n
"
);
        
}
 
else
 
{
            printf
(
"ed è anche dispari
\n
"
);
        
}
    
}
}

Problema: Nidificazione Eccessiva
Codice difficile da leggere:
Soluzione 1: Usa AND logico
Soluzione 2: Early return (in funzioni)
Soluzione 3: else-if al posto di annidati
float
 a
,
 b
,
 c
;
printf
(
"Tre lati: "
);
scanf
(
"
%f
 
%f
 
%f
"
,
 
&
a
,
 
&
b
,
 
&
c
);
if
 
(
a 
+
 b 
>
 c 
&&
 a 
+
 c 
>
 b 
&&
 b 
+
 c 
>
 a
)
 
{
    printf
(
"Triangolo valido
\n
"
);
    
    
if
 
(
a 
==
 b 
&&
 b 
==
 c
)
 
{
        printf
(
"Tipo: EQUILATERO
\n
"
);
    
}
 
else
 
if
 
(
a 
==
 b 
||
 b 
==
 c 
||
 a 
==
 c
)
 
{
        printf
(
"Tipo: ISOSCELE
\n
"
);
    
}
 
else
 
{
        printf
(
"Tipo: SCALENO
\n
"
);
    
}
}
 
else
 
{
    printf
(
"Non è un triangolo valido
\n
"
);
}
if
 
(
condizione1
)
 
{
    
if
 
(
condizione2
)
 
{
        
if
 
(
condizione3
)
 
{
            
if
 
(
condizione4
)
 
{
                
if
 
(
condizione5
)
 
{
                    
// Troppo annidato!
                
}
            
}
        
}
    
}
}
if
 
(
condizione1 
&&
 condizione2 
&&
 condizione3 
&&
 condizione4 
&&
 condizione5
    
// Più chiaro!
}
if
 
(!
condizione1
)
 
return
;
if
 
(!
condizione2
)
 
return
;
if
 
(!
condizione3
)
 
return
;
// Continua...

9.6 Dangling Else (Problema) (10 min)
Il Problema
Quando ci sono più 
if
 senza parentesi graffe, a quale 
if
 appartiene l’
else
?
Regola in C
L’
else
 si associa 
sempre
 all’
if
 più vicino.
Interpretazione corretta:
Come Evitare Ambiguità
Usa SEMPRE le parentesi graffe:
// Invece di:
if
 
(
x 
>
 
90
)
 
{
    
// ...
}
 
else
 
{
    
if
 
(
x 
>
 
80
)
 
{
        
// ...
    
}
 
else
 
{
        
if
 
(
x 
>
 
70
)
 
{
            
// ...
        
}
    
}
}
// Usa:
if
 
(
x 
>
 
90
)
 
{
    
// ...
}
 
else
 
if
 
(
x 
>
 
80
)
 
{
    
// ...
}
 
else
 
if
 
(
x 
>
 
70
)
 
{
    
// ...
}
if
 
(
condizione1
)
    
if
 
(
condizione2
)
        istruzione1
;
else
              
// A quale if appartiene questo else?
    istruzione2
;
if
 
(
condizione1
)
    
if
 
(
condizione2
)
        istruzione1
;
    
else
          
// Appartiene al secondo if!
        istruzione2
;
if
 
(
condizione1
)
 
{
    
if
 
(
condizione2
)
 
{
        istruzione1
;
    
}
 
else
 
{
        istruzione2
;
  
// Eseguito se condizione2 falsa
    
}
}

Esempio Pratico
Ambiguo (senza graffe):
Chiaro (con graffe):
9.7 Best Practices e Stile (15 min)
1. Usa Sempre le Graffe
2. Indentazione Consistente
// Vuoi else per il primo if?
if
 
(
condizione1
)
 
{
    
if
 
(
condizione2
)
 
{
        istruzione1
;
    
}
}
 
else
 
{
  
// Chiaramente associato al primo if
    istruzione2
;
}
// Oppure vuoi else per il secondo if?
if
 
(
condizione1
)
 
{
    
if
 
(
condizione2
)
 
{
        istruzione1
;
    
}
 
else
 
{
  
// Chiaramente associato al secondo if
        istruzione2
;
    
}
}
int
 x 
=
 
5
,
 y 
=
 
10
;
if
 
(
x 
>
 
0
)
    
if
 
(
y 
>
 
5
)
        printf
(
"Entrambi OK
\n
"
);
else
    printf
(
"x negativo
\n
"
);
  
// SBAGLIATO! Non fa quello che pensi
// Quando x=5, y=3: non stampa nulla!
if
 
(
x 
>
 
0
)
 
{
    
if
 
(
y 
>
 
5
)
 
{
        printf
(
"Entrambi OK
\n
"
);
    
}
 
else
 
{
        printf
(
"y troppo piccolo
\n
"
);
    
}
}
 
else
 
{
    printf
(
"x negativo
\n
"
);
}
// 
✗
 MALE (pericoloso)
if
 
(
x 
>
 
0
)
    printf
(
"OK
\n
"
);
// 
✓
 BENE (sicuro)
if
 
(
x 
>
 
0
)
 
{
    printf
(
"OK
\n
"
);
}

3. Condizioni Chiare e Leggibili
4. Evita Condizioni Complesse
5. Costanti a Sinistra (Yoda Conditions)
6. Validazione Input Prima
// 
✓
 BENE
if
 
(
condizione
)
 
{
    istruzione1
;
    istruzione2
;
}
 
else
 
{
    istruzione3
;
}
// 
✗
 MALE
if
 
(
condizione
)
 
{
istruzione1
;
    istruzione2
;
    
}
 
else
 
{
  istruzione3
;
}
// 
✗
 DIFFICILE DA LEGGERE
if
 
(!(
x 
<
 
0
 
||
 x 
>
 
100
 
||
 y 
<
 
0
 
||
 y 
>
 
100
))
 
{
    
// ...
}
// 
✓
 PIÙ CHIARO
int
 x_valido 
=
 
(
x 
>=
 
0
 
&&
 x 
<=
 
100
);
int
 y_valido 
=
 
(
y 
>=
 
0
 
&&
 y 
<=
 
100
);
if
 
(
x_valido 
&&
 y_valido
)
 
{
    
// ...
}
// 
✗
 TROPPO COMPLESSO
if
 
((
a 
>
 b 
&&
 c 
<
 d
)
 
||
 
(
e 
==
 f 
&&
 
(
g 
!=
 h 
||
 i 
<=
 j
))
 
||
 k 
>
 
0
)
 
{
    
// ...
}
// 
✓
 SPEZZA IN PARTI
int
 condizione1 
=
 
(
a 
>
 b 
&&
 c 
<
 d
);
int
 condizione2 
=
 
(
e 
==
 f 
&&
 
(
g 
!=
 h 
||
 i 
<=
 j
));
int
 condizione3 
=
 
(
k 
>
 
0
);
if
 
(
condizione1 
||
 condizione2 
||
 condizione3
)
 
{
    
// ...
}
// Previene errore = invece di ==
if
 
(
5
 
==
 x
)
 
{
  
// Se scrivi if (5 = x) → errore compilazione
    
// ...
}
// Ma rende codice meno leggibile, preferenza personale
if
 
(
x 
==
 
5
)
 
{
  
// Più naturale, ma attenzione a non scrivere =
    
// ...
}

7. Return Early (Guard Clauses)
8. Commenti per Logica Complessa
PARTE PRATICA (2 ore)
ESERCIZI GUIDATI
Esercizio 1: if Semplice (15 min)
1.1
 Controllo maggiore età:
// 
✓
 BUONO - Valida subito
int
 eta
;
scanf
(
"
%d
"
,
 
&
eta
);
if
 
(
eta 
<
 
0
 
||
 eta 
>
 
120
)
 
{
    printf
(
"Età non valida
\n
"
);
    
return
 
1
;
}
// Continua con età valida
if
 
(
eta 
>=
 
18
)
 
{
    
// ...
}
// 
✗
 NIDIFICAZIONE PROFONDA
int
 funzione
(
int
 x
)
 
{
    
if
 
(
x 
>
 
0
)
 
{
        
if
 
(
x 
<
 
100
)
 
{
            
if
 
(
x 
%
 
2
 
==
 
0
)
 
{
                
// Logica principale
                
return
 x 
*
 
2
;
            
}
        
}
    
}
    
return
 
-
1
;
}
// 
✓
 RETURN EARLY
int
 funzione
(
int
 x
)
 
{
    
if
 
(
x 
<=
 
0
)
 
return
 
-
1
;
    
if
 
(
x 
>=
 
100
)
 
return
 
-
1
;
    
if
 
(
x 
%
 
2
 
!=
 
0
)
 
return
 
-
1
;
    
    
// Logica principale (meno nidificata)
    
return
 x 
*
 
2
;
}
// Calcolo sconto in base a categorie cliente
if
 
(
cliente_vip 
&&
 acquisto 
>
 
1000
)
 
{
    sconto 
=
 
0
.20
;
  
// 20% per VIP su grandi acquisti
}
 
else
 
if
 
(
cliente_vip
)
 
{
    sconto 
=
 
0
.10
;
  
// 10% standard VIP
}
 
else
 
if
 
(
acquisto 
>
 
500
)
 
{
    sconto 
=
 
0
.05
;
  
// 5% per acquisti elevati
}
 
else
 
{
    sconto 
=
 
0
.0
;
   
// Nessuno sconto
}

1.2
 Password semplice:
1.3
 Numero positivo, negativo o zero:
Esercizio 2: if-else (20 min)
#include 
<stdio.h>
int
 main
()
 
{
    
int
 eta
;
    
    printf
(
"Inserisci la tua età: "
);
    scanf
(
"
%d
"
,
 
&
eta
);
    
    
if
 
(
eta 
>=
 
18
)
 
{
        printf
(
"Sei maggiorenne
\n
"
);
    
}
    
    
if
 
(
eta 
<
 
18
)
 
{
        printf
(
"Sei minorenne
\n
"
);
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 password 
=
 
1234
;
    
int
 input
;
    
    printf
(
"Inserisci password: "
);
    scanf
(
"
%d
"
,
 
&
input
);
    
    
if
 
(
input 
==
 password
)
 
{
        printf
(
"
✓
 Accesso consentito
\n
"
);
    
}
    
    
if
 
(
input 
!=
 password
)
 
{
        printf
(
"
✗
 Password errata
\n
"
);
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 n
;
    
    printf
(
"Inserisci numero: "
);
    scanf
(
"
%d
"
,
 
&
n
);
    
    
if
 
(
n 
>
 
0
)
 
{
        printf
(
"
%d
 è positivo
\n
"
,
 n
);
    
}
    
    
if
 
(
n 
<
 
0
)
 
{
        printf
(
"
%d
 è negativo
\n
"
,
 n
);
    
}
    
    
if
 
(
n 
==
 
0
)
 
{
        printf
(
"Il numero è zero
\n
"
);
    
}
    
    
return
 
0
;
}

2.1
 Pari o dispari:
2.2
 Massimo tra due numeri:
2.3
 Promozione/bocciatura:
2.4
 Temperatura acqua:
#include 
<stdio.h>
int
 main
()
 
{
    
int
 n
;
    
    printf
(
"Inserisci numero: "
);
    scanf
(
"
%d
"
,
 
&
n
);
    
    
if
 
(
n 
%
 
2
 
==
 
0
)
 
{
        printf
(
"
%d
 è PARI
\n
"
,
 n
);
    
}
 
else
 
{
        printf
(
"
%d
 è DISPARI
\n
"
,
 n
);
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 a
,
 b
;
    
    printf
(
"Primo numero: "
);
    scanf
(
"
%d
"
,
 
&
a
);
    
    printf
(
"Secondo numero: "
);
    scanf
(
"
%d
"
,
 
&
b
);
    
    
if
 
(
a 
>
 b
)
 
{
        printf
(
"Il massimo è 
%d\n
"
,
 a
);
    
}
 
else
 
{
        printf
(
"Il massimo è 
%d\n
"
,
 b
);
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
float
 voto
;
    
    printf
(
"Inserisci voto (0-10): "
);
    scanf
(
"
%f
"
,
 
&
voto
);
    
    
if
 
(
voto 
>=
 
6.0
)
 
{
        printf
(
"
✓
 PROMOSSO
\n
"
);
        printf
(
"Complimenti!
\n
"
);
    
}
 
else
 
{
        printf
(
"
✗
 BOCCIATO
\n
"
);
        printf
(
"Devi rifare l'esame
\n
"
);
    
}
    
    
return
 
0
;
}

Esercizio 3: if-else if-else (25 min)
3.1
 Valutazione esame:
3.2
 Calcolatore sconti:
#include 
<stdio.h>
int
 main
()
 
{
    
float
 temp
;
    
    printf
(
"Temperatura acqua (°C): "
);
    scanf
(
"
%f
"
,
 
&
temp
);
    
    
if
 
(
temp 
<=
 
0
)
 
{
        printf
(
"STATO: Ghiaccio (solido)
\n
"
);
    
}
 
else
 
if
 
(
temp 
<
 
100
)
 
{
        printf
(
"STATO: Acqua (liquido)
\n
"
);
    
}
 
else
 
{
        printf
(
"STATO: Vapore (gas)
\n
"
);
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
int
 voto
;
    
    printf
(
"Inserisci voto (0-100): "
);
    scanf
(
"
%d
"
,
 
&
voto
);
    
    
// Validazione
    
if
 
(
voto 
<
 
0
 
||
 voto 
>
 
100
)
 
{
        printf
(
"Voto non valido!
\n
"
);
        
return
 
1
;
    
}
    
    printf
(
"Voto: 
%d
 - "
,
 voto
);
    
    
if
 
(
voto 
>=
 
90
)
 
{
        printf
(
"Ottimo (A)
\n
"
);
    
}
 
else
 
if
 
(
voto 
>=
 
80
)
 
{
        printf
(
"Buono (B)
\n
"
);
    
}
 
else
 
if
 
(
voto 
>=
 
70
)
 
{
        printf
(
"Discreto (C)
\n
"
);
    
}
 
else
 
if
 
(
voto 
>=
 
60
)
 
{
        printf
(
"Sufficiente (D)
\n
"
);
    
}
 
else
 
{
        printf
(
"Insufficiente (F)
\n
"
);
    
}
    
    
return
 
0
;
}

3.3
 Calcolatore tasse (aliquote):
3.4
 Classificatore IMC:
#include 
<stdio.h>
int
 main
()
 
{
    
float
 importo
,
 sconto_perc 
=
 
0
.0
;
    
    printf
(
"Importo spesa (€): "
);
    scanf
(
"
%f
"
,
 
&
importo
);
    
    
if
 
(
importo 
>=
 
500
)
 
{
        sconto_perc 
=
 
20.0
;
    
}
 
else
 
if
 
(
importo 
>=
 
200
)
 
{
        sconto_perc 
=
 
15.0
;
    
}
 
else
 
if
 
(
importo 
>=
 
100
)
 
{
        sconto_perc 
=
 
10.0
;
    
}
 
else
 
if
 
(
importo 
>=
 
50
)
 
{
        sconto_perc 
=
 
5.0
;
    
}
 
else
 
{
        sconto_perc 
=
 
0
.0
;
    
}
    
    
float
 sconto_importo 
=
 importo 
*
 sconto_perc 
/
 
100.0
;
    
float
 totale 
=
 importo 
-
 sconto_importo
;
    
    printf
(
"
\n
=== RIEPILOGO ===
\n
"
);
    printf
(
"Importo:    
%.2f
€
\n
"
,
 importo
);
    printf
(
"Sconto:     
%.0f%%
 (
%.2f
€)
\n
"
,
 sconto_perc
,
 sconto_importo
);
    printf
(
"Totale:     
%.2f
€
\n
"
,
 totale
);
    
    
return
 
0
;
}
#include 
<stdio.h>
int
 main
()
 
{
    
float
 reddito
,
 tasse
;
    
    printf
(
"Reddito annuo (€): "
);
    scanf
(
"
%f
"
,
 
&
reddito
);
    
    
if
 
(
reddito 
<=
 
15000
)
 
{
        tasse 
=
 reddito 
*
 
0
.23
;
    
}
 
else
 
if
 
(
reddito 
<=
 
28000
)
 
{
        tasse 
=
 
15000
 
*
 
0
.23
 
+
 
(
reddito 
-
 
15000
)
 
*
 
0
.27
;
    
}
 
else
 
if
 
(
reddito 
<=
 
55000
)
 
{
        tasse 
=
 
15000
 
*
 
0
.23
 
+
 
13000
 
*
 
0
.27
 
+
 
(
reddito 
-
 
28000
)
 
*
 
0
.38
;
    
}
 
else
 
{
        tasse 
=
 
15000
 
*
 
0
.23
 
+
 
13000
 
*
 
0
.27
 
+
 
27000
 
*
 
0
.38
 
+
 
(
reddito 
-
 
55000
    
}
    
    
float
 netto 
=
 reddito 
-
 tasse
;
    
float
 aliquota_media 
=
 
(
tasse 
/
 reddito
)
 
*
 
100.0
;
    
    printf
(
"
\n
=== CALCOLO TASSE ===
\n
"
);
    printf
(
"Reddito lordo:  
%.2f
€
\n
"
,
 reddito
);
    printf
(
"Tasse:          
%.2f
€ (
%.1f%%
)
\n
"
,
 tasse
,
 aliquota_media
);
    printf
(
"Reddito netto:  
%.2f
€
\n
"
,
 netto
);
    
    
return
 
0
;
}

Esercizio 4: if Annidati (25 min)
4.1
 Accesso cinema con età e accompagnatore:
#include 
<stdio.h>
int
 main
()
 
{
    
float
 peso
,
 altezza
,
 imc
;
    
    printf
(
"Peso (kg): "
);
    scanf
(
"
%f
"
,
 
&
peso
);
    
    printf
(
"Altezza (m): "
);
    scanf
(
"
%f
"
,
 
&
altezza
);
    
    
if
 
(
peso 
<=
 
0
 
||
 altezza 
<=
 
0
)
 
{
        printf
(
"Valori non validi!
\n
"
);
        
return
 
1
;
    
}
    
    imc 
=
 peso 
/
 
(
altezza 
*
 altezza
);
    
    printf
(
"
\n
IMC: 
%.1f
 - "
,
 imc
);
    
    
if
 
(
imc 
<
 
16.0
)
 
{
        printf
(
"Grave magrezza
\n
"
);
    
}
 
else
 
if
 
(
imc 
<
 
18.5
)
 
{
        printf
(
"Sottopeso
\n
"
);
    
}
 
else
 
if
 
(
imc 
<
 
25.0
)
 
{
        printf
(
"Normopeso
\n
"
);
    
}
 
else
 
if
 
(
imc 
<
 
30.0
)
 
{
        printf
(
"Sovrappeso
\n
"
);
    
}
 
else
 
if
 
(
imc 
<
 
35.0
)
 
{
        printf
(
"Obesità classe I
\n
"
);
    
}
 
else
 
if
 
(
imc 
<
 
40.0
)
 
{
        printf
(
"Obesità classe II
\n
"
);
    
}
 
else
 
{
        printf
(
"Obesità classe III
\n
"
);
    
}
    
    
return
 
0
;
}

4.2
 Login con username e password:
4.3
 Classificazione triangolo completa:
#include 
<stdio.h>
int
 main
()
 
{
    
int
 eta
;
    
char
 accompagnato
;
    
    printf
(
"=== BIGLIETTERIA CINEMA ===
\n
"
);
    printf
(
"Film vietato ai minori di 14 anni
\n\n
"
);
    
    printf
(
"Età: "
);
    scanf
(
"
%d
"
,
 
&
eta
);
    
    
if
 
(
eta 
>=
 
14
)
 
{
        printf
(
"
✓
 Puoi entrare
\n
"
);
    
}
 
else
 
{
        printf
(
"Sei accompagnato da un adulto? (S/N): "
);
        scanf
(
" 
%c
"
,
 
&
accompagnato
);
        
        
if
 
(
accompagnato 
==
 
'S'
 
||
 accompagnato 
==
 
's'
)
 
{
            printf
(
"
✓
 Puoi entrare con accompagnatore
\n
"
);
        
}
 
else
 
{
            printf
(
"
✗
 Non puoi entrare
\n
"
);
        
}
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
#include 
<string.h>
int
 main
()
 
{
    
char
 username
[
20
],
 password
[
20
];
    
char
 username_corretto
[]
 
=
 
"admin"
;
    
char
 password_corretta
[]
 
=
 
"1234"
;
    
    printf
(
"=== LOGIN SISTEMA ===
\n
"
);
    printf
(
"Username: "
);
    scanf
(
"
%s
"
,
 username
);
    
    
if
 
(
strcmp
(
username
,
 username_corretto
)
 
==
 
0
)
 
{
        printf
(
"Password: "
);
        scanf
(
"
%s
"
,
 password
);
        
        
if
 
(
strcmp
(
password
,
 password_corretta
)
 
==
 
0
)
 
{
            printf
(
"
\n
✓
 Accesso consentito
\n
"
);
            printf
(
"Benvenuto, 
%s
!
\n
"
,
 username
);
        
}
 
else
 
{
            printf
(
"
\n
✗
 Password errata
\n
"
);
        
}
    
}
 
else
 
{
        printf
(
"
\n
✗
 Username non trovato
\n
"
);
    
}
    
    
return
 
0
;
}

4.4
 Calcolatore età con verifica data:
#include 
<stdio.h>
#include 
<math.h>
int
 main
()
 
{
    
float
 a
,
 b
,
 c
;
    
    printf
(
"Inserisci i tre lati del triangolo:
\n
"
);
    printf
(
"Lato a: "
);
    scanf
(
"
%f
"
,
 
&
a
);
    printf
(
"Lato b: "
);
    scanf
(
"
%f
"
,
 
&
b
);
    printf
(
"Lato c: "
);
    scanf
(
"
%f
"
,
 
&
c
);
    
    
// Verifica validità
    
if
 
(
a 
+
 b 
>
 c 
&&
 a 
+
 c 
>
 b 
&&
 b 
+
 c 
>
 a
)
 
{
        printf
(
"
\n
✓
 Triangolo VALIDO
\n
"
);
        
        
// Tipo per lati
        
if
 
(
a 
==
 b 
&&
 b 
==
 c
)
 
{
            printf
(
"Tipo (lati): EQUILATERO
\n
"
);
        
}
 
else
 
if
 
(
a 
==
 b 
||
 b 
==
 c 
||
 a 
==
 c
)
 
{
            printf
(
"Tipo (lati): ISOSCELE
\n
"
);
        
}
 
else
 
{
            printf
(
"Tipo (lati): SCALENO
\n
"
);
        
}
        
        
// Tipo per angoli (Teorema di Pitagora)
        
float
 aa 
=
 a 
*
 a
,
 bb 
=
 b 
*
 b
,
 cc 
=
 c 
*
 c
;
        
        
if
 
(
fabs
(
aa 
+
 bb 
-
 cc
)
 
<
 
0
.001
 
||
 
            fabs
(
aa 
+
 cc 
-
 bb
)
 
<
 
0
.001
 
||
 
            fabs
(
bb 
+
 cc 
-
 aa
)
 
<
 
0
.001
)
 
{
            printf
(
"Tipo (angoli): RETTANGOLO
\n
"
);
        
}
 
else
 
if
 
(
aa 
+
 bb 
>
 cc 
&&
 aa 
+
 cc 
>
 bb 
&&
 bb 
+
 cc 
>
 aa
)
 
{
            printf
(
"Tipo (angoli): ACUTANGOLO
\n
"
);
        
}
 
else
 
{
            printf
(
"Tipo (angoli): OTTUSANGOLO
\n
"
);
        
}
        
    
}
 
else
 
{
        printf
(
"
\n
✗
 NON è un triangolo valido
\n
"
);
    
}
    
    
return
 
0
;
}

Esercizio 5: Progetti Completi (35 min)
5.1
 Menu calcolatrice avanzata:
#include 
<stdio.h>
int
 main
()
 
{
    
int
 giorno
,
 mese
,
 anno
;
    
int
 oggi_giorno 
=
 
2
,
 oggi_mese 
=
 
10
,
 oggi_anno 
=
 
2024
;
    
    printf
(
"Inserisci data di nascita (gg mm aaaa): "
);
    scanf
(
"
%d
 
%d
 
%d
"
,
 
&
giorno
,
 
&
mese
,
 
&
anno
);
    
    
// Validazione base
    
if
 
(
anno 
<
 
1900
 
||
 anno 
>
 oggi_anno
)
 
{
        printf
(
"Anno non valido!
\n
"
);
        
return
 
1
;
    
}
    
    
if
 
(
mese 
<
 
1
 
||
 mese 
>
 
12
)
 
{
        printf
(
"Mese non valido!
\n
"
);
        
return
 
1
;
    
}
    
    
if
 
(
giorno 
<
 
1
 
||
 giorno 
>
 
31
)
 
{
        printf
(
"Giorno non valido!
\n
"
);
        
return
 
1
;
    
}
    
    
// Calcolo età
    
int
 eta 
=
 oggi_anno 
-
 anno
;
    
    
// Aggiusta se compleanno non ancora passato quest'anno
    
if
 
(
mese 
>
 oggi_mese
)
 
{
        eta
--;
    
}
 
else
 
if
 
(
mese 
==
 oggi_mese
)
 
{
        
if
 
(
giorno 
>
 oggi_giorno
)
 
{
            eta
--;
        
}
    
}
    
    printf
(
"
\n
Hai 
%d
 anni
\n
"
,
 eta
);
    
    
if
 
(
eta 
>=
 
18
)
 
{
        printf
(
"Sei maggiorenne
\n
"
);
    
}
 
else
 
{
        printf
(
"Sei minorenne
\n
"
);
        printf
(
"Diventerai maggiorenne nel 
%d\n
"
,
 anno 
+
 
18
);
    
}
    
    
return
 
0
;
}

5.2
 Sistema di valutazione studente:
#include 
<stdio.h>
#include 
<math.h>
int
 main
()
 
{
    
float
 a
,
 b
,
 risultato
;
    
int
 scelta
;
    
    printf
(
"=== CALCOLATRICE AVANZATA ===
\n
"
);
    printf
(
"1. Addizione
\n
"
);
    printf
(
"2. Sottrazione
\n
"
);
    printf
(
"3. Moltiplicazione
\n
"
);
    printf
(
"4. Divisione
\n
"
);
    printf
(
"5. Potenza
\n
"
);
    printf
(
"6. Radice quadrata
\n
"
);
    printf
(
"7. Valore assoluto
\n
"
);
    printf
(
"
\n
Scegli operazione (1-7): "
);
    scanf
(
"
%d
"
,
 
&
scelta
);
    
    
if
 
(
scelta 
>=
 
1
 
&&
 scelta 
<=
 
5
)
 
{
        printf
(
"Primo numero: "
);
        scanf
(
"
%f
"
,
 
&
a
);
        printf
(
"Secondo numero: "
);
        scanf
(
"
%f
"
,
 
&
b
);
    
}
 
else
 
if
 
(
scelta 
==
 
6
 
||
 scelta 
==
 
7
)
 
{
        printf
(
"Numero: "
);
        scanf
(
"
%f
"
,
 
&
a
);
    
}
 
else
 
{
        printf
(
"Scelta non valida!
\n
"
);
        
return
 
1
;
    
}
    
    printf
(
"
\n
=== RISULTATO ===
\n
"
);
    
    
if
 
(
scelta 
==
 
1
)
 
{
        risultato 
=
 a 
+
 b
;
        printf
(
"
%.2f
 + 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 risultato
);
    
}
 
else
 
if
 
(
scelta 
==
 
2
)
 
{
        risultato 
=
 a 
-
 b
;
        printf
(
"
%.2f
 - 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 risultato
);
    
}
 
else
 
if
 
(
scelta 
==
 
3
)
 
{
        risultato 
=
 a 
*
 b
;
        printf
(
"
%.2f
 × 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 risultato
);
    
}
 
else
 
if
 
(
scelta 
==
 
4
)
 
{
        
if
 
(
b 
!=
 
0
)
 
{
            risultato 
=
 a 
/
 b
;
            printf
(
"
%.2f
 ÷ 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 risultato
);
        
}
 
else
 
{
            printf
(
"ERRORE: Divisione per zero!
\n
"
);
        
}
    
}
 
else
 
if
 
(
scelta 
==
 
5
)
 
{
        risultato 
=
 pow
(
a
,
 b
);
        printf
(
"
%.2f
 ^ 
%.2f
 = 
%.2f\n
"
,
 a
,
 b
,
 risultato
);
    
}
 
else
 
if
 
(
scelta 
==
 
6
)
 
{
        
if
 
(
a 
>=
 
0
)
 
{
            risultato 
=
 sqrt
(
a
);
            printf
(
"√
%.2f
 = 
%.2f\n
"
,
 a
,
 risultato
);
        
}
 
else
 
{
            printf
(
"ERRORE: Radice di numero negativo!
\n
"
);
        
}
    
}
 
else
 
if
 
(
scelta 
==
 
7
)
 
{
        risultato 
=
 fabs
(
a
);
        printf
(
"|
%.2f
| = 
%.2f\n
"
,
 a
,
 risultato
);
    
}
    
    
return
 
0
;
}

5.3
 Gioco “Sasso, Carta, Forbice”:
#include 
<stdio.h>
int
 main
()
 
{
    
int
 voti
[
5
];
    
int
 i
,
 somma 
=
 
0
,
 min 
=
 
100
,
 max 
=
 
0
;
    
float
 media
;
    
int
 promosso 
=
 
1
;
  
// 1 = sì, 0 = no
    
    printf
(
"=== VALUTAZIONE STUDENTE ===
\n
"
);
    printf
(
"Inserisci 5 voti (0-30):
\n
"
);
    
    
for
 
(
i 
=
 
0
;
 i 
<
 
5
;
 i
++)
 
{
        printf
(
"Voto 
%d
: "
,
 i 
+
 
1
);
        scanf
(
"
%d
"
,
 
&
voti
[
i
]);
        
        
// Validazione
        
if
 
(
voti
[
i
]
 
<
 
0
 
||
 voti
[
i
]
 
>
 
30
)
 
{
            printf
(
"Voto non valido!
\n
"
);
            
return
 
1
;
        
}
        
        somma 
+=
 voti
[
i
];
        
        
// Aggiorna min e max
        
if
 
(
voti
[
i
]
 
<
 min
)
 min 
=
 voti
[
i
];
        
if
 
(
voti
[
i
]
 
>
 max
)
 max 
=
 voti
[
i
];
        
        
// Verifica promozione
        
if
 
(
voti
[
i
]
 
<
 
18
)
 
{
            promosso 
=
 
0
;
        
}
    
}
    
    media 
=
 
(
float
)
somma 
/
 
5
;
    
    printf
(
"
\n
=== RISULTATI ===
\n
"
);
    printf
(
"Media: 
%.1f\n
"
,
 media
);
    printf
(
"Voto minimo: 
%d\n
"
,
 min
);
    printf
(
"Voto massimo: 
%d\n
"
,
 max
);
    
    
if
 
(
promosso
)
 
{
        printf
(
"Esito: 
✓
 PROMOSSO
\n
"
);
        
        
if
 
(
media 
>=
 
27
)
 
{
            printf
(
"Qualifica: OTTIMO
\n
"
);
        
}
 
else
 
if
 
(
media 
>=
 
24
)
 
{
            printf
(
"Qualifica: BUONO
\n
"
);
        
}
 
else
 
{
            printf
(
"Qualifica: SUFFICIENTE
\n
"
);
        
}
    
}
 
else
 
{
        printf
(
"Esito: 
✗
 BOCCIATO
\n
"
);
        printf
(
"(Hai almeno un'insufficienza)
\n
"
);
    
}
    
    
return
 
0
;
}

5.4
 Analizzatore numero completo:
#include 
<stdio.h>
#include 
<stdlib.h>
#include 
<time.h>
int
 main
()
 
{
    
int
 giocatore
,
 computer
;
    
    
// Inizializza generatore numeri casuali
    srand
(
time
(
NULL
));
    
    printf
(
"=== SASSO, CARTA, FORBICE ===
\n
"
);
    printf
(
"1. Sasso
\n
"
);
    printf
(
"2. Carta
\n
"
);
    printf
(
"3. Forbice
\n
"
);
    printf
(
"
\n
La tua scelta (1-3): "
);
    scanf
(
"
%d
"
,
 
&
giocatore
);
    
    
if
 
(
giocatore 
<
 
1
 
||
 giocatore 
>
 
3
)
 
{
        printf
(
"Scelta non valida!
\n
"
);
        
return
 
1
;
    
}
    
    
// Computer sceglie casualmente
    computer 
=
 rand
()
 
%
 
3
 
+
 
1
;
    
    printf
(
"
\n
Tu: "
);
    
if
 
(
giocatore 
==
 
1
)
 printf
(
"Sasso
\n
"
);
    
else
 
if
 
(
giocatore 
==
 
2
)
 printf
(
"Carta
\n
"
);
    
else
 printf
(
"Forbice
\n
"
);
    
    printf
(
"Computer: "
);
    
if
 
(
computer 
==
 
1
)
 printf
(
"Sasso
\n
"
);
    
else
 
if
 
(
computer 
==
 
2
)
 printf
(
"Carta
\n
"
);
    
else
 printf
(
"Forbice
\n
"
);
    
    printf
(
"
\n
"
);
    
    
if
 
(
giocatore 
==
 computer
)
 
{
        printf
(
"PAREGGIO!
\n
"
);
    
}
 
else
 
if
 
((
giocatore 
==
 
1
 
&&
 computer 
==
 
3
)
 
||
               
(
giocatore 
==
 
2
 
&&
 computer 
==
 
1
)
 
||
               
(
giocatore 
==
 
3
 
&&
 computer 
==
 
2
))
 
{
        printf
(
"HAI VINTO!  
\n
"
);
    
}
 
else
 
{
        printf
(
"HAI PERSO!  
\n
"
);
    
}
    
    
return
 
0
;
}
#include 
<stdio.h>
#include 
<math.h>
int
 main
()
 
{
    
int
 n
,
 originale
,
 cifre 
=
 
0
,
 somma_cifre 
=
 
0
;
    
int
 temp
,
 invertito 
=
 
0
;
    
int
 is_primo 
=
 
1
;
    
    printf
(
"Inserisci un numero intero positivo: "
);
    scanf
(
"
%d
"
,
 
&
n
);
    
    
if
 
(
n 
<=
 
0
)
 
{
        printf
(
"Numero non valido!
\n
"
);
        
return
 
1
;
    
}
    
    originale 
=
 n
;
    

ESERCIZI AUTONOMI
Esercizio 6: Pratica Libera
    
    printf
(
"
\n
=== ANALISI DI 
%d
 ===
\n
"
,
 originale
);
    
    
// Pari o dispari
    
if
 
(
n 
%
 
2
 
==
 
0
)
 
{
        printf
(
"Parità: PARI
\n
"
);
    
}
 
else
 
{
        printf
(
"Parità: DISPARI
\n
"
);
    
}
    
    
// Conta cifre e somma
    temp 
=
 n
;
    
while
 
(
temp 
>
 
0
)
 
{
        cifre
++;
        somma_cifre 
+=
 temp 
%
 
10
;
        temp 
/=
 
10
;
    
}
    printf
(
"Numero di cifre: 
%d\n
"
,
 cifre
);
    printf
(
"Somma delle cifre: 
%d\n
"
,
 somma_cifre
);
    
    
// Numero invertito
    temp 
=
 n
;
    
while
 
(
temp 
>
 
0
)
 
{
        invertito 
=
 invertito 
*
 
10
 
+
 temp 
%
 
10
;
        temp 
/=
 
10
;
    
}
    printf
(
"Numero invertito: 
%d\n
"
,
 invertito
);
    
    
// Palindromo
    
if
 
(
originale 
==
 invertito
)
 
{
        printf
(
"È un PALINDROMO
\n
"
);
    
}
 
else
 
{
        printf
(
"NON è un palindromo
\n
"
);
    
}
    
    
// Primo
    
if
 
(
n 
==
 
1
)
 
{
        is_primo 
=
 
0
;
    
}
 
else
 
{
        
for
 
(
int
 i 
=
 
2
;
 i 
<=
 sqrt
(
n
);
 i
++)
 
{
            
if
 
(
n 
%
 i 
==
 
0
)
 
{
                is_primo 
=
 
0
;
                
break
;
            
}
        
}
    
}
    
    
if
 
(
is_primo
)
 
{
        printf
(
"È un numero PRIMO
\n
"
);
    
}
 
else
 
{
        printf
(
"NON è un numero primo
\n
"
);
    
}
    
    
// Multipli
    printf
(
"Multiplo di:
\n
"
);
    
if
 
(
n 
%
 
2
 
==
 
0
)
 printf
(
"  2
\n
"
);
    
if
 
(
n 
%
 
3
 
==
 
0
)
 printf
(
"  3
\n
"
);
    
if
 
(
n 
%
 
5
 
==
 
0
)
 printf
(
"  5
\n
"
);
    
if
 
(
n 
%
 
10
 
==
 
0
)
 printf
(
"  10
\n
"
);
    
    
return
 
0
;
}

6.1
 Crea un programma che determina il tipo di giorno (feriale/festivo) dato il numero del
giorno (1-7).
6.2
 Calcolo parcheggio: tariffe diverse per ore (prima ora 2€, successive 1.50€).
6.3
 Conversione voto numerico (0-30) in giudizio italiano (gravemente insufficiente,
insufficiente, sufficiente, buono, distinto, ottimo, eccellente).
6.4
 Quiz a scelta multipla con 5 domande e punteggio finale.
6.5
 Sistema di accesso con 3 tentativi di password.
ESERCIZI DA SVOLGERE A CASA
Homework 1:
 Calcolatore commissioni bancarie: - Prelievo < 100€: commissione 2€ -
100€ - 500€: commissione 1.5% - > 500€: commissione 1% - Se conto premium:
commissione dimezzata
Homework 2:
 Sistema voto laurea: - Chiedi media voti (0-30) - Chiedi se ha lodi (quante) -
Chiedi punteggio tesi (0-5) - Calcola voto base (media * 110 / 30) - Aggiungi punti lode e
tesi - Determina se lode (>= 110)
Homework 3:
 Validatore password robusto: - Lunghezza minima 8 caratteri - Almeno una
maiuscola - Almeno una minuscola - Almeno un numero - Almeno un simbolo speciale -
Valuta sicurezza (debole/media/forte)
Homework 4:
 Gioco indovina il numero con difficoltà: - Scegli difficoltà
(facile/medio/difficile) - Range diverso per difficoltà - Tentativi diversi per difficoltà -
Suggerimenti progressivi
Homework 5:
 Sistema di prenotazione ristorante: - Chiedi numero persone - Chiedi giorno
settimana - Chiedi ora - Verifica disponibilità (regole complesse) - Calcola prezzo stimato
Homework 6:
 Analizzatore anno: - Chiedi anno - Dice se bisestile - Dice secolo - Dice
millennio - Eventi storici importanti (hardcoded)
APPROFONDIMENTI
Switch vs if-else
Quando usare 
switch
 (lezione prossima) vs 
if-else
:
Usa if-else quando:
 - Condizioni complesse (range, AND, OR) - Condizioni con float -
Poche alternative (2-3)
Usa switch quando:
 - Confronto singola variabile con costanti - Molte alternative (4+) -
Valori interi/char discreti
Short-Circuit nelle Condizioni
Attenzione effetti collaterali:
// && valuta secondo operando solo se primo è vero
if
 
(
puntatore 
!=
 NULL 
&&
 
*
puntatore 
==
 
'A'
)
 
{
    
// Sicuro: se puntatore NULL, non deref
}
// || valuta secondo operando solo se primo è falso
if
 
(
x 
==
 
0
 
||
 y 
/
 x 
>
 
10
)
 
{
    
// Sicuro: se x=0, non divide
}

Ottimizzazione Condizioni
Branch prediction:
 CPU moderna “indovina” quale branch prendere.
Codice prevedibile:
Codice imprevedibile:
Branch misprediction
 costa 10-20 cicli CPU!
Espressioni Booleane Lazy
RIEPILOGO CONCETTI CHIAVE
if Semplice
if-else
if-else if-else
if Annidati
if
 
(
x 
>
 
0
 
||
 
++
contatore 
>
 
10
)
 
{
 
}
// Se x > 0, contatore NON viene incrementato!
// Condizione quasi sempre vera → CPU predice bene
if
 
(
array
[
i
]
 
!=
 
0
)
 
{
  
// Raramente 0
    
// Eseguito quasi sempre
}
// Condizione casuale → CPU sbaglia spesso
if
 
(
rand
()
 
%
 
2
)
 
{
    
// 50% vero, 50% falso
}
// Valutazione pigra (lazy) con variabili temporanee
int
 condizione_complessa 
=
 
(
a 
>
 b 
&&
 c 
<
 d
)
 
||
 
(
e 
==
 f 
&&
 g 
!=
 h
);
if
 
(
condizione_complessa
)
 
{
    
// Usa variabile, più chiaro
}
if
 
(
condizione
)
 
{
    
// Eseguito se vera
}
if
 
(
condizione
)
 
{
    
// Se vera
}
 
else
 
{
    
// Se falsa
}
if
 
(
cond1
)
 
{
    
// Prima vera
}
 
else
 
if
 
(
cond2
)
 
{
    
// Seconda vera
}
 
else
 
{
    
// Tutte false
}

PUNTI CHIAVE DELLA LEZIONE
✓
 
if
 esegue blocco solo se condizione vera
✓
 
if-else
 sceglie tra due alternative
✓
 
if-else if
 permette scelte multiple
✓
 
Usa SEMPRE graffe
 { } anche per singola istruzione
✓
 
Condizioni
 valutate in ordine (prima vera vince)
✓
 
Dangling else
 si associa all’if più vicino
✓
 
0 è falso
, tutto il resto è vero
✓
 
Valida input
 prima di usarlo
✓
 
Return early
 riduce nidificazione
✓
 
Commenta logica
 complessa
PREPARAZIONE PER LA PROSSIMA LEZIONE
Nella prossima lezione studieremo: - 
Istruzione switch-case
: selezione multipla ottimizzata
- 
Break e fall-through
: controllo flusso switch - 
Default
: caso di default - 
Switch vs if-
else
: quando usare cosa - 
Esempi pratici
: menu, stati, classificazioni
Porta con te: - Esercizi homework completati - Domande su if-else o condizioni - Esempi di
menu o scelte multiple - Idee per progetti con molte opzioni
Ottimo lavoro! Ora sai prendere decisioni nei programmi!  
Con if-else hai il potere di creare programmi 
intelligenti
 che reagiscono diversamente in
base alle situazioni. Nella prossima lezione aggiungeremo lo switch per gestire ancora
meglio scelte multiple!
if
 
(
cond_esterna
)
 
{
    
if
 
(
cond_interna
)
 
{
        
// Entrambe vere
    
}
}
