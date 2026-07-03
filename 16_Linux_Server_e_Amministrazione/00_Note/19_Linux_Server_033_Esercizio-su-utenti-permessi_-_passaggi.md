# Linux Server 03.3 Esercizio-su-utenti-permessi - passaggi

**File:** `Linux Server 03.3 Esercizio-su-utenti-permessi - passaggi.pdf`
**Tipo:** `.pdf`
**Dimensione:** 142.3 KB
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
o marco, laura, simone, elena 
2. Creare i seguenti gruppi:  
o fotografi, postprod, direzione 
3. Assegnare gli utenti ai gruppi:  
o laura e simone al gruppo fotografi 
o elena al gruppo postprod 
o marco al gruppo direzione 
o marco anche al gruppo fotografi e postprod 
4. Creare la struttura directory: 
   /home/studio/ 
   ├── raw/ 
   ├── elaborati/ 
   └── archivio/ 
5. Impostare i permessi in modalità ottale:  
Directory Proprietario Gruppo 
Permes
si ottali 
Risultato 
atteso 
/home/studi
o/ 
marco direzione 755 
Marco: rwx, 
direzione: r -x, 
altri: r-x 
/home/studi
o/raw/ 
marco fotografi 770 
Marco: rwx, 
fotografi: rwx, 
altri: nessuno 

 
  3 
Directory Proprietario Gruppo 
Permes
si ottali 
Risultato 
atteso 
/home/studi
o/elaborati/ 
marco postprod 770 
Marco: rwx, 
postprod: 
rwx, altri: 
nessuno 
/home/studi
o/archivio/ 
marco direzione 750 
Marco: rwx, 
direzione: r -x, 
altri: nessuno 
6. Creare i seguenti file e impostare i permessi:  
o In /home/studio/raw/ creare il file foto001.raw:  
▪ Permessi: 660 (proprietario e gruppo leggono e 
scrivono) 
o In /home/studio/elaborati/ creare il file 
foto001_edit.jpg:  
▪ Permessi: 640 (proprietario legge/scrive, gruppo 
solo legge) 
o In /home/studio/archivio/ creare il file listino_prezzi.txt:  
▪ Permessi: 600 (solo il proprietario legge e scrive) 
 
Verifica: 
• Accedere come simone e verificare di poter creare un file 
in /home/studio/raw/ 

 
  4 
• Accedere come elena e verificare di NON poter accedere 
a /home/studio/raw/ 
• Accedere come elena e verificare di poter modificare file 
in /home/studio/elaborati/ 
• Accedere come laura e verificare di poter solo leggere i file 
in /home/studio/elaborati/ (se aggiunta al gruppo) 
 
 
 
 
