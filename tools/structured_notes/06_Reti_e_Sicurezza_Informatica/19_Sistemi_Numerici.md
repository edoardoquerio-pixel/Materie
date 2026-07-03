# Sistemi Numerici

## Panoramica
Fondamenti di Reti di Calcolatori

## Argomenti trattati
API REST

---
## Appunti

Andrea Blanchietti
Fondamenti di Reti di Calcolatori
Sistemi numerici – Conversione tra sistemi
Sistema numerico posizionale
Quando si rappresenta un numero tramite un sistema numerico posizionale, valgono alcune regole
• Si deve definire una base (per esempio, nel sistema decimale la base è 10)
• Si definisce un insieme di simboli che saranno le cifre nella rappresentazione del numero; i
simboli andranno sempre da 0 al valore della base – 1
• Le cifre di un numero avranno un peso in base alla loro posizione nel numero
I pesi sono sempre calcolati come potenze della base
Sistema decimale (numero decimale, base 10)
• Simboli: 0 1 2 3 4 5 6 7 8 9
Il valore di un numero decimale è la somma delle potenze di DIECI, ognuna moltiplicata per il
valore della cifra corrispondente:
Esempio: 5127 = 5x103 + 1x102 + 2x101 + 7x100
Sistema binario (numero binario, base 2)
• Simboli 0 e 1 (il numero è rappresentato da una sequenza di 0 e 1)
Il valore di un numero binario è dato dalla somma di potenze di DUE, ognuna moltiplicata per il
valore della cifra corrispondente
Esempio: 10010110 = 1x27+0x26+0x25+1x24+0x23+1x22+1x21+0x20
Sistema esadecimale (numero esadecimale, base 16)
• Simboli: 0 1 2 3 4 5 6 7 8 9 A B C D E F
Il valore di un numero esadecimale è la somma delle potenze di SEDICI, ognuna moltiplicata
per il valore della cifra corrispondente, dove:
– A equivale a 10
– B equivale a 11
– C equivale a 12
– D equivale a 13
– E equivale a 14
– F equivale a 15
Esempio: FE8016 = Fx163 + Ex162 + 8x161 + 0x160
Conversione da un sistema con base qualsiasi ad un sistema base 10
• Si esprime il numero come somma delle potenze della base
• Si calcolano le potenze nel sistema decimale
• Si moltiplicano per le cifre corrispondenti
• Si somma il tutto
Esempio di conversione da binario a decimale
1011001 = 1×26 + 0×25 + 1×24 + 1×23 + 0×22 + 0×21 + 1×20 = 26 + 24 + 23 + 20 = 64 + 16 + 8 + 1 = 89
Esempio di conversione da esadecimale (base 16) a decimale
7B4116 = 7×163 + B×162 + 4×161 + 1×160 = 7×4096 + 11×256 + 4×16 + 1 = 31553
Conversione da decimale ad un numero espresso in una base r qualsiasi
• Si deve dividere ripetutamente per la base r il numero espresso in base 10
I resti delle divisioni rappresentano le cifre della rappresentazione in base r; il primo resto (in
alto) sarà la cifra meno significativa mentre l’ultimo resto (in basso) sarà la cifra più
Esempio: convertire 89 da decimale a binario
Risultato: 1011001
Esempio: convertire 31553 da decimale al corrispondente valore esadecimale
Risultato: 7B4116
Conversione da numero esadecimale a binario e viceversa
• Per passare da esadecimale a binario, ogni cifra di un numero esadecimale genera quattro bit
Esempio: convertire il numero esadecimale 722416 in binario
In binario: 111001000100100
• Per passare da binario a esadecimale, raggruppo i bit a gruppi di quattro partendo da destra
(bit meno significativo) e aggiungendo zeri a sinistra se necessario
Esempio: convertire il numero binario 1010111100011 in esadecimale
Aggiungiamo tre zeri per avere gruppi da 4 bit: 0001010111100011
0001 0101 1110 0011
In esadecimale: 15E316
Tabella di conversione esadecimale/binario
Conversione da numero decimale a numero esadecimale passando per la
rappresentazione nel sistema di numerazione binario
Invece di usare la conversione diretta da un numero decimale ad un numero esadecimale,
proviamo a fare un passaggio intermedio attraverso la rappresentazione binaria.
Dividere per 2 è più semplice rispetto a dividere per 16 (soprattutto nel calcolo dei resti) e passare
da un numero binario a un numero esadecimale è immediato
Esempio: convertire 31553 da decimale al corrispondente valore esadecimale
1. Converto 31553 in binario:
111101101000001
2. Converto il numero binario in esadecimale
0111 1011 0100 0001

---
*Fonte: 999_Sistemi_Numerici.md*
