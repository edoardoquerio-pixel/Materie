# Linux Server 03.4 Esercizio-su-utenti-permessi - passaggi

Fonte: `Linux Server 03.4 Esercizio-su-utenti-permessi - passaggi.pdf`

DOCENTE 

Wolfgang Cecchin 

UNITA’ FORMATIVA 

Linux Server 

ARGOMENTO 

Esercizio su utenti e permessi 

1 

 
 
 
 
 
 
 
 
 
 
Consegna: 

1. Creare i seguenti utenti: 

o giulia, andrea, chiara, luca, sara 

2. Creare i seguenti gruppi: 

o scrittori, editing, grafica, amministrazione 

3. Assegnare gli utenti ai gruppi: 

o andrea e chiara al gruppo scrittori 

o 

o 

luca al gruppo editing 

luca anche al gruppo scrittori (deve 

leggere 

i 

manoscritti) 

o sara al gruppo grafica 

o giulia ai gruppi amministrazione, scrittori, editing, 

grafica 

4. Creare la struttura directory: 

 /home/casaeditrice/ 

 ├── manoscritti/ 

 ├── bozze/ 

 ├── grafica/ 

 │ ├── copertine/ 

 │ └── impaginazione/ 

 └── amministrazione/ 

5. Impostare i permessi in modalità ottale: 

2 

 
 
 
Propri

etario 

giulia 

Directory 

/home/casae

ditrice/ 

/home/casae

Gruppo 

Permessi ottali Risultato atteso 

amministrazion

e 

755 

Giulia: rwx, tutti: r-x 

ditrice/manos

giulia scrittori 

770 

critti/ 

/home/casae

ditrice/bozze/ 

/home/casae

giulia editing 

770 

ditrice/grafica

giulia grafica 

770 

/ 

/home/casae

ditrice/grafica

giulia grafica 

770 

giulia grafica 

770 

/copertine/ 

/home/casae

ditrice/grafica

/impaginazion

e/ 

/home/casae

Giulia: rwx, scrittori: 

rwx, altri: nessuno 

Giulia: rwx, editing: 

rwx, altri: nessuno 

Giulia: rwx, grafica: 

rwx, altri: nessuno 

Giulia: rwx, grafica: 

rwx, altri: nessuno 

Giulia: rwx, grafica: 

rwx, altri: nessuno 

ditrice/ammini

giulia 

strazione/ 

amministrazion

e 

700 

Solo Giulia: rwx 

6. Creare i seguenti file e impostare i permessi: 

o 

In /home/casaeditrice/manoscritti/ creare 

romanzo_capitolo1.txt: 

▪ Proprietario: giulia, Gruppo: scrittori 

▪ Permessi: 660 

3 

 
 
 
 
o 

In /home/casaeditrice/bozze/ creare 

romanzo_corretto.txt: 

▪ Proprietario: giulia, Gruppo: editing 

▪ Permessi: 660 

o 

In /home/casaeditrice/grafica/copertine/ creare 

bozza_copertina.png: 

▪ Proprietario: giulia, Gruppo: grafica 

▪ Permessi: 660 

o 

In /home/casaeditrice/amministrazione/ creare 

contratti.txt: 

▪ Proprietario: giulia, Gruppo: amministrazione 

▪ Permessi: 600 

Verifica: 

• Accedere come andrea e verificare di poter creare un file 

in /home/casaeditrice/manoscritti/ 

• Accedere come luca e verificare di poter leggere i file in 

/home/casaeditrice/manoscritti/ 

• Accedere come luca e verificare di poter scrivere in 

/home/casaeditrice/bozze/ 

• Accedere come sara e verificare di NON poter accedere a 

/home/casaeditrice/manoscritti/ 

• Accedere come sara e verificare di poter scrivere in 

/home/casaeditrice/grafica/copertine/ 

4 

 
 
 
 
• Accedere come andrea e verificare di NON poter 

accedere a /home/casaeditrice/amministrazione/ 

5