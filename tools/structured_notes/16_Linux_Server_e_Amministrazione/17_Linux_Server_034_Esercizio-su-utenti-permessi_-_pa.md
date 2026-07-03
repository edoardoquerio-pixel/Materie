# Linux Server 03.4 Esercizio-su-utenti-permessi - passaggi

## Panoramica
o giulia, andrea, chiara, luca, sara

## Argomenti trattati
Linux

---
## Appunti

Wolfgang Cecchin
UNITA’ FORMATIVA
Esercizio su utenti e permessi
1. Creare i seguenti utenti:
o giulia, andrea, chiara, luca, sara
2. Creare i seguenti gruppi:
o scrittori, editing, grafica, amministrazione
3. Assegnare gli utenti ai gruppi:
o andrea e chiara al gruppo scrittori
luca al gruppo editing
luca anche al gruppo scrittori (deve
o sara al gruppo grafica
o giulia ai gruppi amministrazione, scrittori, editing,
4. Creare la struttura directory:
/home/casaeditrice/
├── manoscritti/
│ ├── copertine/
│ └── impaginazione/
└── amministrazione/
5. Impostare i permessi in modalità ottale:
Permessi ottali Risultato atteso
Giulia: rwx, tutti: r-x
giulia scrittori
ditrice/grafica
ditrice/grafica
ditrice/grafica
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
Solo Giulia: rwx
6. Creare i seguenti file e impostare i permessi:
In /home/casaeditrice/manoscritti/ creare
romanzo_capitolo1.txt:
▪ Proprietario: giulia, Gruppo: scrittori
▪ Permessi: 660
In /home/casaeditrice/bozze/ creare
romanzo_corretto.txt:
▪ Proprietario: giulia, Gruppo: editing
▪ Permessi: 660
In /home/casaeditrice/grafica/copertine/ creare
bozza_copertina.png:
▪ Proprietario: giulia, Gruppo: grafica
▪ Permessi: 660
In /home/casaeditrice/amministrazione/ creare
▪ Proprietario: giulia, Gruppo: amministrazione
▪ Permessi: 600
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
• Accedere come andrea e verificare di NON poter
accedere a /home/casaeditrice/amministrazione/

---
*Fonte: 003_Linux_Server_03_4_Esercizio-su-utenti-permessi_-_passaggi.md*
