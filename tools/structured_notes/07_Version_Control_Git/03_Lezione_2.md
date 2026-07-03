# Lezione 2

## Panoramica
Una guida pratica per recuperare il controllo delle tue modifiche

## Argomenti trattati
Git, Sicurezza, API REST, Inglese

---
## Appunti

Annullare Modiﬁche in Git
Una guida pratica per recuperare il controllo delle tue modifiche
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Programma della Lezione
Annullare Modiﬁche Locali
Lavorare con i Branch
Impareremo come ripristinare file modificati utilizzando diversi comandi
Scopriremo come creare, navigare e gestire branch nel tuo repository
Merge dei Branch
Esercitazioni Pratiche
Uniremo le modifiche da branch diversi in modo sicuro ed eﬀicace
Metteremo in pratica tutto ciò che abbiamo imparato con esercizi guidati
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Annullare Modiﬁche Locali
Capita a tutti di fare modifiche che poi vogliamo annullare. Git oﬀre diversi strumenti
potenti per ripristinare i file allo stato precedente. Capire quando e come usare questi
comandi è fondamentale per lavorare con sicurezza e fiducia.
Esploriamo i metodi principali per annullare le modifiche locali prima che vengano
committate nel repository.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Metodi per Annullare Modiﬁche
git checkout -- <ﬁle>
git restore <ﬁle>
Comando classico (pre Git 2.23)
Comando moderno (Git 2.23+)
Ripristina un file specifico all'ultimo commit, scartando tutte le modifiche
Più intuitivo e chiaro nel suo scopo. Funziona esattamente come
checkout ma con sintassi più comprensibile.
git checkout -- nome-file.txt
git restore nome-file.txt
Attenzione: Questa operazione è irreversibile. Le modifiche
Best Practice: Usa git restore per progetti nuovi. È il metodo
non salvate verranno perse definitivamente.
raccomandato dalla comunità Git.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Git Restore --staged: Tornare Indietro
Quando hai usato git add per preparare i file ma ti rendi conto di aver commesso un errore, git
restore --staged è la soluzione. Questo comando rimuove i file dallo staging area riportandoli nel
working directory, mantenendo le modifiche ma senza prepararle per il commit.
Il tuo file ha modifiche nel working directory
Il file entra nello staging area
Git restore --staged
Ritorna al working directory con modifiche intatte
Attenzione: Questo comando non cancella le modifiche, le riporta semplicemente nel
working directory dove puoi modificarle o ripristinarle.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Esempi Pratici di Ripristino
Situazione Iniziale
Hai modificato nome-file.txt ma le modifiche hanno causato problemi
modified: nome-file.txt
Annulli le modifiche con restore
git restore nome-file.txt
Il file torna allo stato dell'ultimo commit
nothing to commit
Questo flusso mostra come ripristinare rapidamente un file problematico. Puoi applicare lo stesso processo a più
file contemporaneamente usando git restore . per ripristinare tutti i file modificati nella directory corrente.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Git Revert: Annullare un Commit Pubblicato
git revert crea un nuovo commit che
annulla le modifiche di un commit
precedente. È la scelta migliore quando hai
già condiviso il commit con altri
A diﬀerenza di altri comandi, git revert
non cancella la cronologia, ma la arricchisce
con un nuovo commit che contiene l'inverso
delle modifiche.
git revert HEAD
git revert abc1234
Feature implementata
Nuovo commit che annulla B
Modifiche problematiche
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Git Reset: Soft vs Mixed

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 002_Lezione_2_-_Git_Locale_e_Branch.md*
