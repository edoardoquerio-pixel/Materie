# Linux Server 03.3 Esercizio-su-utenti-permessi - passaggi

## Panoramica
3. Assegnare gli utenti ai gruppi:

## Argomenti trattati
Linux

---
## Appunti

Wolfgang Cecchin
UNITA’ FORMATIVA
Esercizio su utenti e permessi
1. Creare i seguenti utenti:
o marco, laura, simone, elena
2. Creare i seguenti gruppi:
fotografi, postprod, direzione
3. Assegnare gli utenti ai gruppi:
laura e simone al gruppo fotografi
o elena al gruppo postprod
o marco al gruppo direzione
o marco anche al gruppo fotografi e postprod
4. Creare la struttura directory:
5. Impostare i permessi in modalità ottale:
Proprietario Gruppo
direzione: r-x,
fotografi: rwx,
Proprietario Gruppo
direzione: r-x,
6. Creare i seguenti file e impostare i permessi:
In /home/studio/raw/ creare il file foto001.raw:
▪ Permessi: 660 (proprietario e gruppo leggono e
/home/studio/elaborati/
foto001_edit.jpg:
▪ Permessi: 640 (proprietario legge/scrive, gruppo
In /home/studio/archivio/ creare il file listino_prezzi.txt:
▪ Permessi: 600 (solo il proprietario legge e scrive)
• Accedere come simone e verificare di poter creare un file
in /home/studio/raw/
• Accedere come elena e verificare di NON poter accedere
a /home/studio/raw/
• Accedere come elena e verificare di poter modificare file
in /home/studio/elaborati/
• Accedere come laura e verificare di poter solo leggere i file
in /home/studio/elaborati/ (se aggiunta al gruppo)

---
*Fonte: 003_Linux_Server_03_3_Esercizio-su-utenti-permessi_-_passaggi.md*
