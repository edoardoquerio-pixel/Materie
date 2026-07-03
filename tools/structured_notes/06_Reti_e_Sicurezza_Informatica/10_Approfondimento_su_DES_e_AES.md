# Approfondimento su DES e AES

## Panoramica
La funzione crittograﬁca di DES

## Argomenti trattati
API REST

---
## Appunti

La funzione crittograﬁca di DES
Il DES normale utilizza una funzione che si chiama Feistel (in ﬁgura), che
lavora su metà del blocco (E, in ﬁgura) e una sottochiave, che vengono
messe in XOR. Il risultato viene diviso in 8 parti da 6 bit e sostituito con
una apposita S-Box, ed inﬁne riordinati con una P-Box (permutation box),
anch’essa ﬁssa. Questa funzione viene ripetuta in ogni sottofase.
L’algoritmo di espansione della chiave in AES
L’algoritmo di espansione della chiave prende in input una word di 16 byte
e produce un array lineare di 44 word (176 byte), sufﬁcienti per fornire una
sottochiave al round iniziale e ai 10 main round.
La chiave viene copiata nella prima word della chiave espansa, mentre il
resto viene riempito quattro word per volta (i vari quadrati inizialmente
vuoti delle slide). Ogni word w[i] dipende dalla word immediatamente
precedente w[i–1] e dalla word di quattro posizioni prima w[i–4].
Per tre delle quattro word viene usato un semplice XOR (questo risponde
in parte alla tua domanda).
Per la prima word di ogni blocco (ovvero quella la cui posizione è multiplo
di 4, colorate diversamente nelle slide) viene usata una funzione più
complicata, chiamata “g”.
1. RotWord effettua uno shift a sinistra di un byte. Questo signiﬁca che
[B0,B1,B2,B3] diventa [B1,B2,B3,B0];
2. SubWord effettua una sostituzione usando la S-Box dell’algoritmo
Il risultato viene messo in XOR con una costante, chiamata
Rcon[j] (che in realtà è un vettore, per cui la costante cambia ad
ogni round–capire come funziona e perché va oltre gli scopi del
nostro corso e ha sempre a che fare con i campi di Galois).
Nella ﬁgura c’è uno schema di questi passaggi, chiamati “function g”.

---
*Fonte: 999_Approfondimento_su_DES_e_AES.md*
