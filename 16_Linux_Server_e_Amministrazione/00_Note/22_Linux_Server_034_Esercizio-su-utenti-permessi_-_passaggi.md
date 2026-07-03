# Linux Server 03.4 Esercizio-su-utenti-permessi - passaggi

**File:** `Linux Server 03.4 Esercizio-su-utenti-permessi - passaggi.pdf`
**Tipo:** `.pdf`
**Dimensione:** 146.0 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
1 
 
 
 
 
  
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Esercizio su utenti e permessi 

 
  2 
Consegna: 
1. Creare i seguenti utenti:  
o giulia, andrea, chiara, luca, sara 
2. Creare i seguenti gruppi:  
o scrittori, editing, grafica, amministrazione 
3. Assegnare gli utenti ai gruppi:  
o andrea e chiara al gruppo scrittori 
o luca al gruppo editing 
o luca anche al gruppo scrittori (deve leggere i 
manoscritti) 
o sara al gruppo grafica 
o giulia ai gruppi amministrazione, scrittori, editing, 
grafica 
4. Creare la struttura directory: 
   /home/casaeditrice/ 
   ├── manoscritti/ 
   ├── bozze/ 
   ├── grafica/ 
   │   ├── copertine/ 
   │   └── impaginazione/ 
   └── amministrazione/ 
5. Impostare i permessi in modalità ottale:  

 
  3 
 
6. Creare i seguenti file e impostare i permessi:  
o In /home/casaeditrice/manoscritti/ creare 
romanzo_capitolo1.txt:  
▪ Proprietario: giulia, Gruppo: scrittori 
▪ Permessi: 660 
Directory 
Propri
etario 
Gruppo Permessi ottali Risultato atteso 
/home/casae
ditrice/ 
giulia 
amministrazion
e 
755 Giulia: rwx, tutti: r-x 
/home/casae
ditrice/manos
critti/ 
giulia scrittori 770 
Giulia: rwx, scrittori: 
rwx, altri: nessuno 
/home/casae
ditrice/bozze/ 
giulia editing 770 
Giulia: rwx, editing: 
rwx, altri: nessuno 
/home/casae
ditrice/grafica
/ 
giulia grafica 770 
Giulia: rwx, grafica: 
rwx, altri: nessuno 
/home/casae
ditrice/grafica
/copertine/ 
giulia grafica 770 
Giulia: rwx, grafica: 
rwx, altri: nessuno 
/home/casae
ditrice/grafica
/impaginazion
e/ 
giulia grafica 770 
Giulia: rwx, grafica: 
rwx, altri: nessuno 
/home/casae
ditrice/ammini
strazione/ 
giulia 
amministrazion
e 
700 Solo Giulia: rwx 

 
  4 
o In /home/casaeditrice/bozze/ creare 
romanzo_corretto.txt:  
▪ Proprietario: giulia, Gruppo: editing 
▪ Permessi: 660 
o In /home/casaeditrice/grafica/copertine/ creare 
bozza_copertina.png:  
▪ Proprietario: giulia, Gruppo: grafica 
▪ Permessi: 660 
o In /home/casaeditrice/amministrazione/ creare 
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

 
  5 
• Accedere come andrea e verificare di NON poter 
accedere a /home/casaeditrice/amministrazione/ 
 
