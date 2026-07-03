# 07 - Version Control Git — Tutte le Sessioni


---

## Sessione 1: Quiz Version Control


Quiz – Fondamenti di Version Control e Git
1. Cos'è il Version Control?
A. Un linguaggio di programmazione
B. Un sistema che registra le modifiche ai file nel tempo
C. Un servizio cloud per salvare file
D. Un editor di testo avanzato
2. Quale problema NON viene risolto dal version control?
A. Tracciabilità delle modifiche
B. Collaborazione tra sviluppatori
C. Scrittura automatica del codice
D. Recupero di versioni precedenti
3. Il version control può essere paragonato a:
A. Un antivirus
B. Una macchina del tempo per il codice
C. Un compilatore
D. Un database remoto
4. Cosa succede senza un sistema di version control?
A. Il codice è più veloce
B. Le modifiche sono sempre chiare
C. Si crea caos tra le versioni dei file
D. I file non possono essere cancellati
5. Quale di questi è un problema reale senza version control?
A. Impossibilità di usare Internet
B. Perdita di lavoro e conflitti nel team
C. Codice troppo leggibile
D. Riduzione dello spazio su disco
6. Qual è il limite principale del Version Control Locale?
A. È troppo lento
B. Non funziona offline
C. Non permette collaborazione
D. Richiede un server
7. Quale sistema è un esempio di Version Control Centralizzato?
8. Nel Version Control Distribuito:
A. Esiste un solo server centrale
B. Ogni client ha una copia completa del repository
C. Non è possibile lavorare offline
D. Non esiste uno storico delle modifiche
9. Quale vantaggio chiave ha il Version Control Distribuito?
A. Richiede meno spazio
B. Backup automatico su ogni client
C. Funziona solo online
D. È più semplice del locale
10. In quali ambiti si usa il Version Control?
A. Solo sviluppo software
B. Solo documentazione
C. Solo progetti creativi
D. In tutti i casi sopra
11. Chi ha creato Git?
B. Guido van Rossum
C. Linus Torvalds
D. Mark Zuckerberg
12. In che anno è nato Git?
13. Perché Git è considerato molto veloce?
A. Usa solo Internet
B. Salva i file in cloud
C. Esegue operazioni localmente
D. Riduce il numero di file
14. Git e GitHub sono:
A. La stessa cosa
B. Due editor di codice
C. Uno strumento locale e una piattaforma online
D. Due linguaggi di programmazione
15. GitHub serve principalmente per:
A. Scrivere codice offline
B. Ospitare repository e collaborare
C. Compilare programmi
D. Sostituire Git
16. Quali sono le tre fasi del flusso di lavoro Git?
A. Edit – Save – Upload
B. Local – Remote – Cloud
C. Working Directory – Staging Area – Repository
D. Code – Test – Deploy
17. Quale comando aggiunge file alla staging area?
18. Cos'è un commit?
A. Un backup automatico
B. Una cartella di progetto
C. Un'istantanea dello stato del progetto
D. Un file temporaneo
19. Cosa contiene sempre un commit?
A. Solo il codice

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 2: Lezione 1


Fondamenti di Version Control
Lezione 1 – Corso di Version Control con Git
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Cosa imparerai in questa lezione
Comprendere il Version Control
Pratica diretta
Scopriremo cos'è il version control, perché è
Impareremo le basi di Git, lo strumento più
Creeremo il nostro primo repository e
nato e quali problemi risolve nello sviluppo
utilizzato al mondo per il controllo di
faremo il nostro primo commit, mettendo
software moderno
subito in pratica i concetti
Il version control è una competenza fondamentale per ogni sviluppatore moderno. Che tu lavori da solo o in team, padroneggiare questi strumenti ti
permetterà di gestire il codice in modo professionale, tracciare ogni modifica e collaborare eﬀicacemente con altri sviluppatori. Questa lezione getta le
fondamenta per diventare un professionista dello sviluppo software.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Cos'è il Version Control?
Il version control (o controllo di versione) è un sistema che registra nel tempo le modifiche
apportate a uno o più file, permettendoti di recuperare versioni specifiche in un secondo
momento. Pensa a un sistema di "macchina del tempo" per il tuo codice.
Ogni modifica significativa crea una nuova versione del progetto, come un'istantanea nel
Storico delle modiﬁche
Tutte le modifiche vengono registrate con data, autore e descrizione, creando una
cronologia completa
Puoi sapere chi ha modificato cosa, quando e perché, rendendo il codice completamente
Più persone possono lavorare sullo stesso progetto contemporaneamente senza
sovrascriversi a vicenda
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Il caos senza Version Control
Scenario familiare?
progetto_v2.zip
progetto_finale.zip
progetto_finale_VERO.zip
progetto_finale_definitivo.zip
progetto_finale_definitivo_v2.zip
progetto_da_consegnare_QUESTO.zip
Questo caos è il risultato di lavorare senza
un sistema di version control. Ogni
Perdita di lavoro
Sovrascrivere accidentalmente file
importanti senza possibilità di recupero
Conﬂitti nel team
Due persone modificano lo stesso file e
una delle due versioni viene persa
versione è un file separato, non c'è traccia
Nessuna tracciabilità
delle modifiche, e trovare "quella modifica di
Impossibile sapere chi ha fatto cosa,
tre settimane fa" diventa un incubo.
quando e perché una modifica è stata fatta
Backup inefﬁciente
Duplicare intere cartelle di progetto
occupa spazio e crea confusione
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Tre modelli di Version Control
Nel corso degli anni, sono emersi tre principali modelli di version control, ognuno con i propri vantaggi e limitazioni. Comprendere queste
diﬀerenze aiuta a comprendere perché Git è diventato lo standard industriale.
Version Control Locale
Version Control Centralizzato
Version Control Distribuito
Il sistema più semplice: un database locale che
Un unico server centrale contiene tutti i file
Ogni client ha una copia completa dell'intero
tiene traccia delle modifiche ai file sul tuo
versionati. I client scaricano le versioni dal
storico del repository. Esempio: Git, Mercurial.
computer. Esempio: RCS (Revision Control
server. Esempio: SVN (Subversion), CVS.
Vantaggio: lavoro oﬀline, backup naturale,
System). Limite: funziona solo su un singolo
Limite: se il server non è disponibile, nessuno
massima flessibilità nella collaborazione.
computer, nessuna collaborazione possibile.
può lavorare o salvare versioni.

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 3: Lezione 2


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

## Sessione 4: Lezione 3


Introduzione a Git Remoto e
Repository Online
Impara a gestire il tuo codice collaborativamente e in modo professionale
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Git Locale vs Git Remoto: La
Differenza Fondamentale
Repository Locale
Repository Remoto
Il tuo repository locale vive
Un repository remoto risiede su un
esclusivamente sulla tua macchina. Ogni
server esterno, accessibile da chiunque
commit, branch e modifica rimane
abbia le credenziali. È il centro di
confinato al tuo computer. È perfetto per
coordinamento dove tutti i collaboratori
lavorare oﬀline e sperimentare senza
sincronizzano il loro lavoro.
influenzare gli altri.
Accesso solo da una macchina
• Nessuna condivisione automatica
Rischio di perdita dati se il PC si
Accesso da qualsiasi dispositivo
Condivisione e collaborazione in
Backup automatico e sicurezza
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Perché Usare un Repository Remoto?
Backup Automatico
Collaborazione in Tempo Reale
Il tuo codice è al sicuro su server aﬀidabili. Anche se il tuo computer si
Lavora simultaneamente con colleghi e amici. Merge, pull requests e
rompe, la tua storia di commit e tutti i tuoi progetti sono preservati nel
code review diventano semplici. Ogni membro del team può
contribuire senza conflitti.
Integrazione CI/CD
Storia Completa
Automatizza test, build e deployment ogni volta che pushi nuove
Mantieni traccia di ogni modifica, chi l'ha fatta e quando. Ripristina
modifiche. Migliora la qualità del codice e riduci gli errori prima della
versioni precedenti in pochi secondi e analizza l'evoluzione del
progetto nel tempo.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
HTTPS vs SSH: Scegliere il Protocollo Giusto
Il protocollo più semplice e universale.
Il protocollo più sicuro e professionale. Usa
Funziona ovunque senza configurazione
coppie di chiavi crittografiche per
aggiuntiva e utilizza le tue credenziali di
l'autenticazione automatica senza password.
GitHub/GitLab per l'autenticazione.
Facile da configurare per i principianti
Autenticazione automatica con chiavi
Funziona dietro qualsiasi firewall
• Maggiore sicurezza crittografica
Non richiede chiavi SSH
Nessun inserimento credenziali
Devi inserire username e password ogni
• Menù sicuro di SSH
Configurazione iniziale più complessa
Può essere bloccato da alcuni firewall
Suggerimento: Inizia con HTTPS per semplificare, poi passa a SSH quando ti senti più
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Conﬁgurazione accesso tramite HTTPS
git config --global user.name "IlTuoNome"
git config --global user.email "latuaemail@example.com"
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Il Flusso di Lavoro Git:
Un'Immagine Vale Mille Parole
1. Il Tuo Computer
2. Il Server Remoto
3. I Collaboratori
Clona il repository remoto
Pusha le tue modifiche al
Gli altri team member
sul tuo locale. Lavora,

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 5: Lezione 4


Git GUI e Client Graﬁci
Una guida completa per sviluppatori che vogliono esplorare le interfacce grafiche per Git
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Perché Usare un Client Graﬁco?
Il Terminale Resta Potente
Ma le GUI Aggiungono Valore
Se conosci già Git da terminale, hai una base solida. I comandi
I client grafici non sostituiscono il terminale, ma lo integrano. Oﬀrono una
Git oﬀrono controllo totale e precisione, permettendoti di
visualizzazione immediata dello stato del repository, semplificano operazioni
gestire ogni aspetto del version control con flessibilità massima.
complesse e riducono la possibilità di errori nelle operazioni quotidiane.
Visualizzazione istantanea della cronologia dei commit
• Gestione intuitiva dei conflitti di merge
Produttività aumentata per task ripetitivi
Curva di apprendimento ridotta per operazioni avanzate
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
I Vantaggi Principali delle GUI
Visualizzazione
Graﬁca dei Branch
Vedere l'albero dei branch, i
merge e le divergenze in
formato grafico rende
comprensibile la struttura
del progetto. Identificare
dove sono avvenuti i merge
e quali branch sono attivi
diventa un'operazione visiva
Diff Visuale Avanzato
Risoluzione Conﬂitti
Staging Selettivo
Le GUI mostrano le
diﬀerenze tra versioni con
evidenziazione del codice,
rendering aﬀiancato e
navigazione semplificata.
Puoi vedere esattamente
cosa è cambiato in ogni file
senza dover interpretare
output testuali complessi.
Quando si verificano
Puoi facilmente scegliere
conflitti durante un merge,
quali modifiche includere
le GUI oﬀrono strumenti
nel prossimo commit, anche
visivi per confrontare le
a livello di singole righe. La
versioni e scegliere quale
selezione visiva con
codice mantenere. Il
checkbox e anteprime rende
processo diventa più
l'operazione di staging
intuitivo rispetto alla
molto più veloce e precisa.
modifica manuale dei file
con marcatori di conflitto.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
I Principali Client Graﬁci Git
Esistono diversi client grafici per Git, ognuno con caratteristiche distintive. Ecco i quattro più popolari e utilizzati dalla comunità di sviluppatori.
Gratuito · Atlassian
Freemium · Multi-piattaforma
Gratuito · GitHub
Potente e completo, perfetto
Interfaccia moderna e
Semplice e minimalista, ideale
per utenti Windows e Mac.
accattivante con
per principianti. Integrazione
Oﬀre supporto nativo per Git
visualizzazione grafica
perfetta con GitHub ma
Flow e integrazione con
eccellente. Include funzionalità
funziona con qualsiasi
Bitbucket. Interfaccia ricca di

*[Contenuto troncato — vedi file originale per dettagli completi]*


---
*Totale: 5 sessioni generate il 02/07/2026*