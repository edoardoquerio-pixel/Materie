# Version Control Git — Quaderno di Appunti

> **Materia:** 07_Version_Control_Git
> **Data generazione:** Febbraio 2026
> **Corso:** ITS ICT Cloud Specialist 2025-2027

---

## Indice delle Sessioni

1. [Lezione 1 - Fondamenti di Version Control](#lezione-1---fondamenti-di-version-control)
2. [Lezione 2 - Git Locale e Branch](#lezione-2---git-locale-e-branch)
3. [Lezione 3 - Introduzione a Git Remoto e Repository Online](#lezione-3---introduzione-a-git-remoto-e-repository-online)
4. [Lezione 4 - Git GUI e Client Grafici](#lezione-4---git-gui-e-client-grafici)
5. [Quiz Version Control](#quiz-version-control)

---

# Lezione 1 - Fondamenti di Version Control

**File:** `Lezione 1 - Fondamenti di Version Control.pdf`
**Tipo:** `.pdf`
**Dimensione:** 2561.1 KB
**Ultima modifica:** 02/07/2026 09:24

---

Fondamenti di Version Control
Lezione 1 – Corso di Version Control con Git
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

OBIETTIVI
Cosa imparerai in questa lezione
Comprendere il Version Control
Scopriremo cos'è il version control, perché è 
nato e quali problemi risolve nello sviluppo 
software moderno
Conoscere Git
Impareremo le basi di Git, lo strumento più 
utilizzato al mondo per il controllo di 
versione
Pratica diretta
Creeremo il nostro primo repository e 
faremo il nostro primo commit, mettendo 
subito in pratica i concetti
Il version control è una competenza fondamentale per ogni sviluppatore moderno. Che tu lavori da solo o in team, padroneggiare questi strumenti ti 
permetterà di gestire il codice in modo professionale, tracciare ogni modifica e collaborare eﬀicacemente con altri sviluppatori. Questa lezione getta le 
fondamenta per diventare un professionista dello sviluppo software.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Cos'è il Version Control?
Il version control (o controllo di versione) è un sistema che registra nel tempo le modifiche 
apportate a uno o più file, permettendoti di recuperare versioni specifiche in un secondo 
momento. Pensa a un sistema di "macchina del tempo" per il tuo codice.
1
Versioni
Ogni modifica significativa crea una nuova versione del progetto, come un'istantanea nel 
tempo
2
Storico delle modiﬁche
Tutte le modifiche vengono registrate con data, autore e descrizione, creando una 
cronologia completa
3
Tracciabilità
Puoi sapere chi ha modificato cosa, quando e perché, rendendo il codice completamente 
trasparente
4
Collaborazione
Più persone possono lavorare sullo stesso progetto contemporaneamente senza 
sovrascriversi a vicenda
 © 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Il caos senza Version Control
Scenario familiare?
• progetto.zip
• progetto_v2.zip
• progetto_finale.zip
• progetto_finale_VERO.zip
• progetto_finale_definitivo.zip
• progetto_finale_definitivo_v2.zip
Questo caos è il risultato di lavorare senza 
un sistema di version control. Ogni 
versione è un file separato, non c'è traccia 
delle modifiche, e trovare "quella modifica di 
tre settimane fa" diventa un incubo.
Problemi reali
Perdita di lavoro
Sovrascrivere accidentalmente file 
importanti senza possibilità di recupero
Conﬂitti nel team
Due persone modificano lo stesso file e 
una delle due versioni viene persa
Nessuna tracciabilità
Impossibile sapere chi ha fatto cosa, 
quando e perché una modifica è stata fatta
Backup inefﬁciente
Duplicare intere cartelle di progetto 
occupa spazio e crea confusione
• progetto_da_consegnare_QUESTO.zip 
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Tre modelli di Version Control
Nel corso degli anni, sono emersi tre principali modelli di version control, ognuno con i propri vantaggi e limitazioni. Comprendere queste 
diﬀerenze aiuta a comprendere perché Git è diventato lo standard industriale.
01
Version Control Locale
Il sistema più semplice: un database locale che 
tiene traccia delle modifiche ai file sul tuo 
computer. Esempio: RCS (Revision Control 
System). Limite: funziona solo su un singolo 
computer, nessuna collaborazione possibile.
02
Version Control Centralizzato
Un unico server centrale contiene tutti i file 
versionati. I client scaricano le versioni dal 
server. Esempio: SVN (Subversion), CVS. 
Limite: se il server non è disponibile, nessuno 
può lavorare o salvare versioni.
03
Version Control Distribuito
Ogni client ha una copia completa dell'intero 
storico del repository. Esempio: Git, Mercurial. 
Vantaggio: lavoro oﬀline, backup naturale, 
massima flessibilità nella collaborazione.
Caratteristica Locale Centralizzato Distribuito
Collaborazione ❌
 No ✅
 Sì ✅✅
 Eccellente
Lavoro oﬀline ✅
 Sì ❌
 Limitato ✅
 Completo
Velocità ⚡
 Veloce 🐌
 Dipende dalla rete ⚡
 Velocissimo
Backup ❌
 Nessuno ⚠
 Solo sul server ✅
 Automatico ovunque
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Dove si usa il Version Control?
Sviluppo Software
L'uso principale: gestire codice 
sorgente, coordinate feature, 
risolvere bug e mantenere più 
versioni del software 
simultaneamente
Documentazione
Mantenere versioni di manuali, 
guide utente, documentazione 
tecnica e specifiche di progetto 
con tracciabilità completa
Progetti Creativi
Gestire configurazioni di 
sistema, script di automazione, 
file di design e qualsiasi 
progetto che evolve nel tempo
Esempi concreti nel mondo reale
Linux Kernel: migliaia di sviluppatori coordinati via Git
Open Source: progetti come React, Vue.js, TensorFlow su GitHub
Aziende: Google gestisce miliardi di righe di codice con version control
Startup: ogni team di sviluppo moderno usa Git quotidianamente
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Introduzione a Git
Git è un sistema di version control distribuito creato nel 2005 da Linus Torvalds (lo stesso creatore di Linux). È diventato lo standard de facto nell'industria 
del software grazie alla sua velocità, flessibilità e potenza.
100M+
Repository su GitHub
Oltre 100 milioni di repository ospitati 
sulla piattaforma più popolare
94%
Adozione professionale
Percentuale di sviluppatori 
professionisti che usano Git
2005
Anno di nascita
Git è nato per gestire lo sviluppo del 
kernel Linux
Perché Git è così 
popolare?
Velocità
Operazioni locali istantanee, nessuna dipendenza dalla 
rete per la maggior parte delle operazioni
Branching potente
Creare, unire ed eliminare branch è velocissimo e 
incoraggia la sperimentazione
Completamente distribuito
Ogni clone è un backup completo, puoi lavorare 
ovunque, anche oﬀline
Integrità dei dati
Ogni file è verificato tramite checksum, impossibile 
corrompere i dati senza che Git lo sappia
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

CONCETTO CHIAVE
Git non è GitHub
Git: lo strumento locale
Git è un software di version control che vive sul tuo computer. Funziona 
completamente oﬀline e gestisce la storia delle modifiche del tuo codice 
in modo autonomo.
• Installato localmente sul tuo PC
• Funziona senza connessione Internet
• Gestisce repository in locale
• Strumento a riga di comando
GitHub: la piattaforma online
GitHub è una piattaforma cloud che ospita repository Git remoti. Serve 
per collaborare e condividere il codice con altri sviluppatori.
• Servizio online (richiede Internet)
• Backup remoto dei progetti
• Collaborazione in team
• Interfaccia web visuale
Analogia utile: Git è come Microsoft Word installato sul tuo computer, mentre GitHub è come Google Drive dove salvi e condividi i documenti 
con altri.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Come funziona Git: il ﬂusso di lavoro
Git non salva automaticamente le modifiche come fa un editor di testo. Segue invece un 
processo in tre fasi che ti permette di controllare esattamente cosa salvare e quando. 
Comprendere questo flusso è fondamentale per usare Git eﬀicacemente.
Working Directory
I file su cui stai lavorando attivamente. Le modifiche non sono ancora tracciate da Git.
Staging Area
Area di preparazione dove selezioni le modifiche da includere nel prossimo commit.
git add nomefile
Repository
Archivio permanente con la storia completa delle modifiche salvate.
git commit -m "messaggio"
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Il commit: un istantanea del progetto
Cos'è davvero un commit?
Un commit è una fotografia dello stato del tuo progetto in un 
momento specifico. Non è solo un salvataggio: è un punto nella storia 
del tuo codice a cui puoi sempre tornare.
"Pensa al commit come a un checkpoint in un videogioco: puoi 
sempre ricaricare da quel punto se qualcosa va storto. "
Messaggio descrittivo
Spiega cosa è stato modificato e perché
Autore e data
Chi ha fatto la modifica e quando
Codice hash univoco
Identificatore unico del commit (es: a3f2b1c)
Snapshot completo
Stato coerente di tutti i file tracciati
Ogni commit ti permette di viaggiare nel tempo: puoi vedere com'era il codice in passato, confrontare versioni diverse e 
capire l'evoluzione del progetto.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Buone pratiche sui commit
Imparare a fare commit eﬀicaci è una competenza fondamentale. Commit ben strutturati rendono la storia del progetto leggibile e facilitano la 
collaborazione con altri sviluppatori.
Un'idea = un commit
Ogni commit dovrebbe rappresentare una 
singola modifica logica e completa
Commit frequenti
Meglio tanti commit piccoli che uno grande 
alla fine della giornata
Messaggi chiari
Descrivi cosa hai fatto in modo che tu (e altri) 
possiate capirlo tra sei mesi
❌
 Esempi da evitare
• update
• fix
• modifiche varie
• asdasd
• funziona!!!
✅
 Esempi corretti
• Aggiunta validazione form login
• Correzione bug nel calcolo totale carrello
• Implementato sistema di cache per query
• Aggiornata documentazione API utenti
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Anatomia di un buon messaggio di commit
01
Usa l'imperativo presente
"Aggiunge" , "Corregge" , "Implementa" - come se stessi dando un ordine a Git
02
Sii speciﬁco ma conciso
Massimo 50-70 caratteri per la prima riga. Vai dritto al punto.
03
Spiega il "perché", non il "cosa"
Il codice mostra cosa hai fatto. Il messaggio spiega perché l'hai fatto.
04
Aggiungi dettagli se necessario
Dopo una riga vuota, puoi aggiungere una descrizione più lunga con contesto addizionale
Regola d'oro: Il tuo messaggio di commit dovrebbe completare la frase "Se 
applicato, questo commit ________" . Esempio: "Se applicato, questo commit 
aggiunge validazione form login" .
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Errori comuni quando si inizia con Git
Tutti fanno errori all'inizio. Riconoscere questi pattern ti aiuterà a evitarli e a sviluppare buone abitudini fin da subito.
1
Dimenticare git add
Modifichi i file ma ti dimentichi di aggiungerli alla staging area prima 
del commit. Risultato: il commit è vuoto o incompleto.
Soluzione: Usa git status frequentemente per verificare cosa 
stai per committare.
2
Fare un solo commit gigante
Lavori tutto il giorno e alla fine fai un unico commit con "modifiche 
di oggi" . Impossibile poi capire cosa è stato fatto.
Soluzione: Committa ogni volta che completi una piccola 
funzionalità o correzione.
3
Messaggi di commit inutili
Scrivi "fix" , "update" , "stuﬀ" senza spiegare cosa hai realmente 
modificato.
Soluzione: Dedica 10 secondi in più per scrivere un messaggio 
descrittivo significativo.
4
Paura di "rompere tutto"
Hai timore di usare Git perché pensi di poter distruggere il progetto. 
Questa paura ti blocca.
Soluzione: Git è progettato per essere sicuro. È quasi impossibile 
perdere davvero del lavoro committato.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Git è fatto per sperimentare in sicurezza
Perché non devi avere paura
Una delle cose più diﬀicili da capire per i principianti è che Git è 
progettato proprio per permetterti di sbagliare. È un sistema 
di sicurezza, non un campo minato.
Ogni commit è permanente
Una volta committato qualcosa, è quasi impossibile perderlo 
davvero
Puoi sempre tornare indietro
Git ti permette di annullare, modificare o ripristinare 
qualsiasi cambiamento
Gli esperimenti sono protetti
I branch (che vedrai nelle prossime lezioni) ti permettono di 
provare cose nuove senza rischi
Mentalità corretta
"Sbagliare è parte del processo di apprendimento. Git è la tua 
rete di sicurezza. "
Consiglio pratico: Crea una cartella di test e sperimenta liberamente con Git. Prova a fare commit, a modificare 
file, a vedere la history. Non c'è modo migliore per imparare che provare direttamente.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Installazione e conﬁgurazione di Git
Installazione per sistema operativo
🪟
 Windows
Scarica Git per Windows da git-scm.com e segui l'installer. Verrà installato 
anche Git Bash, un terminale Unix-like per Windows.
🍎
 macOS
Installa tramite Homebrew con brew install git oppure scarica l'installer 
dal sito uﬀiciale. Git è già incluso negli Xcode Command Line Tools.
🐧
 Linux
Usa il package manager della tua distribuzione: apt-get install git 
(Debian/Ubuntu) o yum install git (Red Hat/Fedora).
Conﬁgurazione iniziale
Dopo l'installazione, è fondamentale configurare la tua identità. 
Queste informazioni verranno associate ad ogni commit che farai.
git config --global user.name "Mario Rossi"
git config --global user.email 
"mario.rossi@example.com"
Per verificare la configurazione:
git config --list
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Il nostro primo repository Git
È arrivato il momento di mettere in pratica ciò che abbiamo imparato. Creeremo insieme il nostro primo 
repository Git e faremo il nostro primo commit. Segui attentamente i passaggi.
Crea una cartella di progetto
Apri il terminale e crea una nuova cartella: mkdir mio-primo-progetto poi spostati al suo interno: cd mio-primo-progetto
Inizializza il repository
Esegui il comando git init per inizializzare un nuovo repository Git nella cartella corrente. Vedrai il messaggio "Initialized empty Git repository"
Crea un ﬁle
Crea un file di testo: echo "Il mio primo progetto Git" > README.md oppure usa il tuo editor preferito per creare il file
Aggiungi alla staging area
Prepara il file per il commit: git add README.md. Questo sposta il file nell'area di staging, pronto per essere salvato
Fai il primo commit
Salva la modifica nello storico: git commit -m "Primo commit: aggiunto README". Congratulazioni, hai creato il tuo primo commit! 
Obiettivi dell'esercitazione
• Familiarizzare con i comandi base di Git
• Comprendere il flusso: working directory → staging area → repository
• Vedere concretamente come Git traccia le modifiche
• Acquisire confidenza con il terminale
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Esercizio in autonomia
Istruzioni Passo dopo Passo
1. Preparazione:
○ Apri il terminale del tuo computer.
○ Crea una cartella chiamata diario-git e spostati al suo interno.
○ Suggerimento: Usa i comandi mkdir e cd.
2. Inizializzazione:
○ Trasforma questa semplice cartella in un repository Git.
○ Veriﬁca: Se esegui git status, dovresti vedere che Git è attivo (anche se non ci sono ancora ﬁle).
3. Creazione del Contenuto:
○ Crea un ﬁle chiamato appunti.txt.
○ Scrivi all'interno del ﬁle una frase che descriva il comando Git che ti sembra più utile (es: "Il comando git init serve a 
iniziare tutto!"). Puoi usare un editor di testo o il comando echo.
4. Tracciamento (Staging Area):
○ Aggiungi il ﬁle appunti.txt alla "Staging Area".
○ Veriﬁca: Controlla di nuovo con git status. Il ﬁle dovrebbe apparire in verde (pronto per il commit).
5. Il Primo "Salvataggio" (Commit):
○ Esegui il commit del ﬁle con un messaggio chiaro, ad esempio: "Aggiunto il primo appunto sul diario".
6. La Modiﬁca:
○ Modiﬁca il ﬁle appunti.txt aggiungendo una seconda riga con la data di oggi.
○ Esegui di nuovo i passaggi di Add e Commit per salvare questa seconda versione.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Comandi fondamentali
Prima di passare alla prossima lezione, assicurati di aver compreso e memorizzato questi comandi essenziali. Li userai costantemente nel tuo lavoro 
quotidiano con Git.
git status
Mostra lo stato attuale: quali file sono modificati, in staging, o non 
tracciati
Quando usarlo: Sempre, prima di ogni operazione. È il tuo migliore 
amico.
git add nomefile
Aggiunge un file specifico alla staging area, pronto per essere 
committato
Variante: git add . aggiunge tutti i file modificati (usa con 
cautela)
git commit -m "messaggio"
Crea un commit con i file in staging, salvando un'istantanea del 
progetto
Ricorda: Il messaggio deve essere chiaro e descrittivo
git log
Visualizza la cronologia dei commit del repository con autori, date e 
messaggi
Variante: git log --oneline per una vista compatta
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Via Schiaparelli 14 - 10148 Torino
https://www.tc-web.it
Mail: franco.grivet@tc-web.it
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it
GRAZIE A TUTTI…..



---

# Lezione 2 - Git Locale e Branch

**File:** `Lezione 2 - Git Locale e Branch.pdf`
**Tipo:** `.pdf`
**Dimensione:** 3819.7 KB
**Ultima modifica:** 02/07/2026 09:24

---

Annullare Modiﬁche in Git
Una guida pratica per recuperare il controllo delle tue modifiche
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Programma della Lezione
01
Annullare Modiﬁche Locali
Impareremo come ripristinare file modificati utilizzando diversi comandi 
Git
02
Lavorare con i Branch
Scopriremo come creare, navigare e gestire branch nel tuo repository
03
Merge dei Branch
Uniremo le modifiche da branch diversi in modo sicuro ed eﬀicace
04
Esercitazioni Pratiche
Metteremo in pratica tutto ciò che abbiamo imparato con esercizi guidati 
passo-passo
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Annullare Modiﬁche Locali
Capita a tutti di fare modifiche che poi vogliamo annullare. Git oﬀre diversi strumenti 
potenti per ripristinare i file allo stato precedente. Capire quando e come usare questi 
comandi è fondamentale per lavorare con sicurezza e fiducia.
Esploriamo i metodi principali per annullare le modifiche locali prima che vengano 
committate nel repository.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it


Metodi per Annullare Modiﬁche
git checkout -- <ﬁle>
Comando classico (pre Git 2.23)
Ripristina un file specifico all'ultimo commit, scartando tutte le modifiche 
non salvate.
git checkout -- nome-file.txt
Attenzione: Questa operazione è irreversibile. Le modifiche 
non salvate verranno perse definitivamente.
git restore <ﬁle>
Comando moderno (Git 2.23+)
Più intuitivo e chiaro nel suo scopo. Funziona esattamente come 
checkout ma con sintassi più comprensibile.
git restore nome-file.txt
Best Practice: Usa git restore per progetti nuovi. È il metodo 
raccomandato dalla comunità Git.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Git Restore --staged: Tornare Indietro 
dallo Staging
Quando hai usato git add per preparare i file ma ti rendi conto di aver commesso un errore, git 
restore --staged è la soluzione. Questo comando rimuove i file dallo staging area riportandoli nel 
working directory, mantenendo le modifiche ma senza prepararle per il commit.
File modiﬁcato
Il tuo file ha modifiche nel working directory
Git add
Il file entra nello staging area
Git restore --staged
Ritorna al working directory con modifiche intatte
Attenzione: Questo comando non cancella le modifiche, le riporta semplicemente nel 
working directory dove puoi modificarle o ripristinarle.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Esempi Pratici di Ripristino
Situazione Iniziale
Hai modificato nome-file.txt  ma le modifiche hanno causato problemi
git status
modified: nome-file.txt
Ripristino
Annulli le modifiche con restore
git restore nome-file.txt
Risultato
Il file torna allo stato dell'ultimo commit
git status
nothing to commit
Questo flusso mostra come ripristinare rapidamente un file problematico. Puoi applicare lo stesso processo a più 
file contemporaneamente usando git restore . per ripristinare tutti i file modificati nella directory corrente.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Git Revert: Annullare un Commit Pubblicato
Quando usarlo
git revert crea un nuovo commit che 
annulla le modifiche di un commit 
precedente. È la scelta migliore quando hai 
già condiviso il commit con altri 
collaboratori.
A diﬀerenza di altri comandi, git revert 
non cancella la cronologia, ma la arricchisce 
con un nuovo commit che contiene l'inverso 
delle modifiche.
Sintassi
git revert HEAD
git revert abc1234
1Commit A
Feature implementata
2 Commit B
Modifiche problematiche
3Git revert
Nuovo commit che annulla B
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Git Reset: Soft vs Mixed
git reset è un comando potente ma pericoloso. Esistono diverse modalità, ognuna con eﬀetti diversi sulla cronologia del progetto.
Git reset --soft
Rimuove il commit dalla cronologia ma mantiene le modifiche nello 
staging area. Perfetto quando vuoi modificare il messaggio del 
commit o aggiungere ulteriori file.
git reset --soft HEAD~1
Git reset --mixed (default)
Rimuove il commit e sposta le modifiche dallo staging al working 
directory. Le modifiche sono ancora presenti ma non pronte per il 
commit.
git reset --mixed HEAD~1
# Oppure semplicemente:
git reset HEAD~1
⚠
 Importante: Non usare git reset su commit condivisi pubblicamente, può causare problemi ai tuoi collaboratori.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Confronto Comandi di Undo
Questa tabella riassume quando usare ogni comando in base alla situazione in cui ti trovi.
Comando Quando usarlo Eﬀetto sulla cronologia
git restore Modifiche non aggiunte allo staging Nessun eﬀetto - ripristina file
git restore --staged File nello staging da rimuovere Nessun eﬀetto - sposta indietro
git revert Commit già condivisi con altri Crea nuovo commit di annullamento
git reset --soft Commit locale da modificare Rimuove commit, mantiene staging
git reset --mixed Commit locale da rifare Rimuove commit, mantiene modifiche
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Errori Comuni da Evitare
1
Usare reset su commit condivisi
Non modificare mai la cronologia di commit già pushati su un repository condiviso. Usa git revert invece di git reset.
2
Dimenticare di speciﬁcare i ﬁle
Sii sempre specifico su quali file vuoi ripristinare. Usare . o * senza attenzione può cancellare modifiche importanti.
3
Confondere restore e reset
restore è per modifiche locali, reset è per la cronologia. Non usare reset come sostituto di restore.
4
Non veriﬁcare lo stato prima
Sempre eseguire git status e git log prima di annullare modifiche per capire esattamente dove sei.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Esercizio Guidato Pratico
Seguiamo insieme un esercizio per applicare quanto abbiamo imparato. Apri il terminale e crea una cartella di prova.
1. Preparazione
mkdir git-practice
cd git-practice
git init
echo "Ciao mondo" > file.txt
git add file.txt
git commit -m "Primo commit"
2. Modiﬁche al ﬁle
echo "Nuova riga" >> file.txt
git status
3. Esercizio A: Ripristinare
git restore file.txt
git status
Il file è tornato allo stato del commit!
4. Esercizio B: Staging e reset
echo "Testo modificato" > file.txt
git add file.txt
git reset HEAD~1
💡
 Prova tu: Dopo ogni comando, usa git status per vedere come cambia lo stato dei file. Questo ti aiuterà a capire meglio il flusso di lavoro.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Git Branch: L'Arte di Creare 
Percorsi Separati
Impara a gestire il tuo codice con la potenza dei branch in Git
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Cos'è un Branch? Una Metafora Visiva
Immagina il tuo progetto come un albero. Il ramo 
principale, chiamato main, è il tronco centrale. I 
branch sono i rami che si diramano da questo 
tronco, permettendoti di crescere nuove 
funzionalità senza danneggiare la pianta 
principale.
Ogni branch è un percorso separato della storia 
del tuo progetto. Puoi lavorare su nuove idee, 
correggere bug o sperimentare senza 
preoccuparti di rovinare il lavoro stabile nel ramo 
principale.
È come avere più copie del tuo progetto dove 
testare liberamente, ma con l'intelligenza di Git 
per unire tutto insieme quando sei pronto!
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

I Comandi Fondamentali per i Branch
Git fornisce alcuni comandi essenziali per gestire i tuoi branch. Impararli è facile!
git branch
Mostra tutti i branch del tuo progetto. Il 
branch attivo è segnato con un asterisco (*).
git switch
Cambia il branch attivo. Passa da un ramo 
all'altro in un secondo!
git switch -c
Crea un nuovo branch e ci si sposta 
immediatamente. La scorciatoia perfetta!
Suggerimento: In versioni più vecchie di Git, usa git checkout invece di git switch. Il comando git switch è più chiaro e moderno!
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Creare e Navigare tra Branch
Creazione di un Branch
Per creare un nuovo branch usa il comando git 
branch seguito dal nome che vuoi dare al branch.
git branch lezione-2
Questo crea un nuovo branch ma non ci sposta 
automaticamente. Per vedere tutti i branch 
disponibili:
git branch -a
• Il branch corrente sarà evidenziato con un 
asterisco (*)
• Verde indica il branch attivo
• Bianco indica gli altri branch
Cambiare Branch
Metodo moderno:
git switch lezione-2
Metodo classico:
git checkout lezione-2
Scorciatoia utile - crea e passa subito al nuovo 
branch:
git switch -c lezione-2
Git switch è più chiaro e specifico per 
cambiare branch. Usa sempre questo 
comando per i nuovi progetti.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Visualizzare la Storia: git log --graph
Il Comando Magico
Usa git log --graph per vedere la storia visiva del 
tuo progetto con tutte le diramazioni:
git log --graph --oneline
Questa comando ti mostra un bellissimo grafico ASCII 
che illustra come i branch si dividono e si uniscono nel 
tempo.
È come avere una mappa del tesoro del tuo progetto!
--graph
Aggiunge il diagramma visivo delle diramazioni
--oneline
Rende l'output più compatto e leggibile
--all
Mostra tutti i branch, non solo quello corrente
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Workﬂow Base: main + Feature Branch
Il pattern più comune e fondamentale per il lavoro con i branch.
Trunk stabile
Feature branch
Revisione & Test
Merge in main
Il Ramo Main
Rappresenta il codice stabile e funzionante
• È la versione che va in produzione
• Non si fa mai lavoro diretto qui
• Ogni commit dovrebbe essere testato e verificato
I Branch di Feature
Si creano da main per ogni nuova funzionalità
• Il lavoro avviene in isolamento
• Si possono fare molti commit sperimentali
Quando pronti, si uniscono a mainQuesto workflow ti permette di lavorare su più funzionalità contemporaneamente senza conflitti!
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Best Practice: Come Chiamare i Tuoi 
Branch
Un nome ben scelto per i branch rende tutto più chiaro per te e i tuoi colleghi!
Usa nomi descrittivi e brevi
Evita nomi generici come "nuovo" o "prova" . Scegli qualcosa che descriva esattamente cosa fa: 
aggiungi-login, fix-header-bug, nuova-pagina-prodotti
Usa trattini per separare le parole
Git preferisce trattini (-) invece di spazi o underscore: carrello-acquisto è meglio di 
carrello_acquisto o carrello acquisto
Evita caratteri speciali
Attieniti a lettere minuscole, numeri e trattini. Evita spazi, accenti, e caratteri come @, #, $ che 
possono causare problemi
Includi l'ID del ticket (se usi un sistema)
Se lavori con Jira o simili: PROJ-123-fix-login-error collega il branch direttamente al ticket di 
lavoro
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Esercizio Guidato Pratico
Ora è il momento di mettere in pratica quello che hai imparato. Segui questi passi:
Apri il TerminaleNaviga nella cartella del tuo progetto Git
Lista i BranchEsegui git branch per vedere i branch esistenti
Crea un Nuovo BranchUsa git switch -c per creare un branch chiamato prova-branch
Veriﬁca la PosizioneRiesegui git branch per confermare che sei su prova-branch
Fai una ModiﬁcaCrea un file di testo o modifica un file esistente nel tuo progetto
Commit delle ModiﬁcheAggiungi e commit il file: git add . e git commit -m "Test"
Visualizza la StoriaEsegui git log --graph --oneline per vedere la diramazione
Torna a mainCompleta con git switch main per tornare al branch principale
Bravo! Hai completato il tuo primo workflow con i branch. Continua a praticare questi comandi finché 
non diventano naturali!
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Git Merge e Gestione dei 
Conﬂitti
Una guida completa per principianti che hanno appena imparato i branch e vogliono 
padroneggiare l'unione delle modifiche nel loro workflow di sviluppo.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Cos'è il Merge in Git
Il merge è l'operazione fondamentale che 
permette di unire le modifiche da un branch a 
un altro. È come prendere tutti i cambiamenti 
sviluppati in una linea parallela di lavoro e 
incorporarli nella tua linea principale.
Pensa al merge come a un ponte che collega due 
strade separate, permettendo a tutti di passare 
da una strada all'altra senza perdere il percorso.
In Git, quando crei un branch, lavori su una copia 
isolata del tuo progetto. Il merge è il momento in 
cui integri quei cambiamenti nel branch 
principale (o in un altro branch).
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Fast-Forward Merge vs Merge Commit
Fast-Forward Merge
Quando si verifica: Il branch di destinazione non ha nuove modifiche dall'ultimo commit
Come funziona: Git sposta semplicemente il puntatore del branch principale avanti lungo la 
cronologia
Risultato: Nessun commit di merge viene creato, la cronologia rimane lineare
Merge Commit
Quando si verifica: Entrambi i branch hanno modifiche divergenti
Come funziona: Git crea un nuovo commit speciale che unisce le modifiche di entrambi i branch
Risultato: Viene creato un commit di merge, la cronologia mostra la biforcazione
Nota: Il fast-forward merge è più pulito visivamente, ma il merge commit preserva la storia 
completa di come i branch si sono uniti.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Il Comando Git Merge
Sintassi di Base
git merge <nome-branch>
Questo comando unisce il branch specificato con il branch corrente. Prima di eseguire il merge, assicurati di essere 
sul branch destinazione.
Passi Pratici
Passa al branch destinazione: git checkout main
Assicurati di essere aggiornato: git pull origin main
Esegui il merge: git merge feature/login
4. Risolvi eventuali conflitti
5. Commit delle modifiche unite
Opzioni Utili
--no-ff: Forza la creazione di un commit di merge
--abort: Annulla un merge in corso
-m: Aggiungi un messaggio personalizzato
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Simulazione Passo-Passo del Merge
Vediamo un esempio pratico di come si svolge un merge. Immaginiamo di avere un branch main e un branch feature/news con modifiche divergenti.
01
Conﬁgurazione Iniziale
Branch main a commit A, branch feature/news creato da A
02
Sviluppo Parallelo
Main: commit A → B → C | Feature: commit A → D → E
03
Checkout Main
git checkout main - Passiamo al branch principale
04
Esecuzione Merge
git merge feature/news - Git cerca di unire le modifiche
05
Creazione Commit
Git crea un commit di merge F che unisce C ed E
06
Risultato Finale
Branch main ora contiene tutte le modifiche da entrambi i branch
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

I Merge Conﬂict: Cosa Sono
Un merge conflict si verifica quando Git non può 
automaticamente unire le modifiche perché due branch 
hanno modificato la stessa parte di un file in modo 
diverso.
È come se due persone avessero modificato la stessa frase 
in un documento contemporaneamente. Git non sa quale 
versione sia corretta, quindi ti chiede di decidere 
manualmente.
Quando Si Veriﬁcano
• Modifiche alla stessa riga di codice
• Rinomina di file in un branch e modifiche nell'altro
• Eliminazione di file modificati nell'altro branch
• Struttura diversa del codice
Attenzione: I conflitti non sono errori! Sono normali nel lavoro di team e richiedono solo un po' di attenzione per risolverli correttamente.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Esempio Reale di Conﬂitto
Ecco come appare un file con marker di conflitto. Git inserisce marker speciali per indicare le diverse versioni del codice.
<<<<<<< HEAD
function saluta() {
  console.log("Ciao, mondo!");
}
=======
function saluta() {
  console.log("Hello, world!");
}
>>>>>>> feature/inglese
<<<<<<< HEAD
Inizio della tua versione corrente (branch 
principale). Quello che c'è tra questa e ======= è il 
codice presente nel tuo branch.
=======
Separatore centrale che divide le due versioni del 
codice. Aiuta a distinguere chiaramente le 
modifiche.
>>>>>>> feature/inglese
Inizio della versione del branch che stai mergiando. 
Il codice fino a >>>>>>> è quello del branch di 
origine.
Dopo aver risolto il conflitto, devi rimuovere tutti i marker e lasciare solo il codice scelto, poi fare commit delle modifiche.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Procedura Completa di Risoluzione
Identiﬁca i Conﬂitti
Git ti avvisa che ci sono conflitti. Usa git status per vedere quali file sono in conflitto. I file saranno marcati come "unmerged" .
Apri i File
Apri ogni file con conflitto in un editor di testo. Cerca i marker <<<<<<<, ======= e >>>>>>> per trovare le sezioni problematiche.
Risolvi Manualmente
Scegli quale versione mantenere o crea una soluzione che combini entrambe. Elimina tutti i marker di conflitto. Assicurati che il codice funzioni!
Aggiungi e Commit
git add <file> per segnalare che il conflitto è risolto. Poi git commit per completare il merge. Git suggerisce automaticamente il messaggio.
Veriﬁca
Testa il codice per assicurarti che funzioni correttamente. Esegui i test e verifica che tutto sia a posto prima di pushare le modifiche.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Best Practice per Evitare Conﬂitti
Branch Breve
Crea branch specifici e lavoraci per periodi brevi. Più lungo è il 
tempo tra la creazione del branch e il merge, maggiori sono le 
possibilità di conflitti.
Modiﬁca File Minimi
Quando possibile, limita le modifiche a pochi file. Più file 
modifichi, più probabilità hai di entrare in conflitto con altri 
sviluppatori che modificano gli stessi file.
Usa un Editor Diff
Strumenti come VS Code, IntelliJ o editor diﬀ dedicati rendono la 
risoluzione dei conflitti molto più semplice con highlight e 
suggerimenti automatici.
Test Prima del Merge
Assicurati che il tuo codice funzioni prima di fare merge. Questo 
evita di introdurre bug nel branch principale e semplifica il 
debugging se qualcosa va storto.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Esercizio Pratico Guidato
È il momento di mettere in pratica quanto hai imparato! Segui questi passi per un'esperienza hands-on con i merge e i conflitti.
Prepara l'Ambiente
Crea una nuova cartella, inizializza Git e crea un file 
hello.txt con "Hello, World!"
Crea i Branch
git branch feature/italian e git branch 
feature/spanish. Passa su ciascuno e modifica il 
file in "Ciao, Mondo!" e "Hola, Mundo!"
Esegui il Merge
Checkout su main, fai merge di feature/italian, poi 
prova a fare merge di feature/spanish. Vedrai il 
conflitto!
Risolvi il Conﬂitto
Apri il file, trova i marker, scegli una versione o crea "Hello, Ciao, Hola World!" , 
rimuovi i marker e fai commit
Veriﬁca
Usa git log --oneline --graph per vedere la cronologia. Assicurati che tutto 
sia corretto e che il merge sia completato
Bravo! Ora hai padroneggiato i merge e la gestione dei conflitti. Continua a praticare e questi concetti diventeranno naturali nel tuo workflow quotidiano.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Esercizio 2: Branch e Merge Completo
1
Crea Branch Feature
git switch -c aggiungi-contatti
echo "Email: info@esempio.it" > contatti.txt
git add contatti.txt
git commit -m "Aggiunti contatti"
2
Torna a Main e Modiﬁca
git switch main
echo "Versione 1.0" > versione.txt
git add versione.txt
git commit -m "Aggiunta versione"
3
Fai il Merge
git merge aggiungi-contatti
git log --oneline --graph --all
4
Veriﬁca Risultato
ls -la
cat contatti.txt
cat versione.txt
Soluzione completa: Dovresti vedere entrambi i file (contatti.txt e versione.txt) nel branch main. Il grafico dei log 
mostrerà due linee che si uniscono, rappresentando il merge del branch aggiungi-contatti nel main.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Via Schiaparelli 14 - 10148 Torino
https://www.tc-web.it
Mail: franco.grivet@tc-web.it
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it
GRAZIE A TUTTI…..



---

# Lezione 3 - Introduzione a Git Remoto e Repository Online

**File:** `Lezione 3 - Introduzione a Git Remoto e Repository Online.pdf`
**Tipo:** `.pdf`
**Dimensione:** 4716.1 KB
**Ultima modifica:** 02/07/2026 09:24

---

Introduzione a Git Remoto e 
Repository Online
Impara a gestire il tuo codice collaborativamente e in modo professionale
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Git Locale vs Git Remoto: La 
Differenza Fondamentale
Repository Locale
Il tuo repository locale vive 
esclusivamente sulla tua macchina. Ogni 
commit, branch e modifica rimane 
confinato al tuo computer. È perfetto per 
lavorare oﬀline e sperimentare senza 
influenzare gli altri.
• Accesso solo da una macchina
• Nessuna condivisione automatica
• Rischio di perdita dati se il PC si 
rompe
Repository Remoto
Un repository remoto risiede su un 
server esterno, accessibile da chiunque 
abbia le credenziali. È il centro di 
coordinamento dove tutti i collaboratori 
sincronizzano il loro lavoro.
• Accesso da qualsiasi dispositivo
• Condivisione e collaborazione in 
tempo reale
• Backup automatico e sicurezza
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Perché Usare un Repository Remoto?
Backup Automatico
Il tuo codice è al sicuro su server aﬀidabili. Anche se il tuo computer si 
rompe, la tua storia di commit e tutti i tuoi progetti sono preservati nel 
cloud.
Collaborazione in Tempo Reale
Lavora simultaneamente con colleghi e amici. Merge, pull requests e 
code review diventano semplici. Ogni membro del team può 
contribuire senza conflitti.
Integrazione CI/CD
Automatizza test, build e deployment ogni volta che pushi nuove 
modifiche. Migliora la qualità del codice e riduci gli errori prima della 
produzione.
Storia Completa
Mantieni traccia di ogni modifica, chi l'ha fatta e quando. Ripristina 
versioni precedenti in pochi secondi e analizza l'evoluzione del 
progetto nel tempo.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

HTTPS vs SSH: Scegliere il Protocollo Giusto
HTTPS
Il protocollo più semplice e universale. 
Funziona ovunque senza configurazione 
aggiuntiva e utilizza le tue credenziali di 
GitHub/GitLab per l'autenticazione.
Vantaggi
• Facile da configurare per i principianti
• Funziona dietro qualsiasi firewall
• Non richiede chiavi SSH
Contro
• Devi inserire username e password ogni 
volta
• Menù sicuro di SSH
SSH
Il protocollo più sicuro e professionale. Usa 
coppie di chiavi crittografiche per 
l'autenticazione automatica senza password.
Vantaggi
• Autenticazione automatica con chiavi
• Maggiore sicurezza crittografica
• Nessun inserimento credenziali
Contro
• Configurazione iniziale più complessa
• Può essere bloccato da alcuni firewall
Suggerimento: Inizia con HTTPS per semplificare, poi passa a SSH quando ti senti più 
sicuro!
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Conﬁgurazione accesso tramite HTTPS
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it
git config --global user.name "IlTuoNome"
git config --global user.email "latuaemail@example.com"


Il Flusso di Lavoro Git: 
Un'Immagine Vale Mille Parole
Distribuzione
Push al Server
Commit Locale
1. Il Tuo Computer
Clona il repository remoto 
sul tuo locale. Lavora, 
committa le modifiche e 
testa in totale sicurezza 
prima di condividere.
2. Il Server Remoto
Pusha le tue modifiche al 
repository centrale. Qui il 
codice viene salvato, 
versionato e reso 
disponibile a tutti.
3. I Collaboratori
Gli altri team member 
pullano le tue modifiche e 
contribuiscono con le loro. 
La sincronizzazione 
avviene continuamente.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Git in Azione: GitHub e GitLab
GitHub
La piattaforma più popolare per progetti open source. Oltre 100 milioni di 
utenti collaborano su milioni di repository. Oﬀre Issues, Pull Requests, 
Actions per CI/CD, e una community enorme.
• Interfaccia intuitiva e moderna
• Actions per automazione
• Pages per hosting statico
• Community e documentazione
GitLab
Una soluzione completa che include CI/CD integrato, issue tracking e 
DevOps tools. Perfetto per team che vogliono tutto in un'unica 
piattaforma.
• CI/CD integrato nativamente
• Funzionalità DevOps complete
• Versione self-hosted disponibile
• Strumenti di sicurezza avanzati
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Branch Remoti: Collaborare Senza Conﬂitti
Crea Branch Remoto
Quando lavori su una nuova funzionalità, crea un 
branch dedicato. Pushalo sul remoto per condividerlo 
con il team.
Collabora Separatamente
I tuoi colleghi possono lavorare sui loro branch mentre 
tu sviluppi la tua feature. Nessun conflitto con il codice 
principale.
Merge Quando Sei Pronto
Una volta completata la feature, apri una Pull Request 
per revisionare il codice e mergiare nel main branch in 
modo controllato.
Comandi Utili
git checkout -b feature/new-ui
git push origin feature/new-ui
git branch -r
Best Practices
• Nome chiari e descrittivi per i branch
• Pull regolarmente da main
• Delete branch dopo il merge
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Conﬁgurazione Iniziale: I Passi Fondamentali
Conﬁgura Git Globalmente
Imposta il tuo nome e email una volta per tutte. Queste informazioni verranno 
associate a ogni commit che farai.
git config --global user.name "Il Tuo Nome"
git config --global user.email "email@example.com"
Clona il Repository
Scarica il repository remoto sul tuo computer. Usa l'URL HTTPS o SSH fornito dalla 
piattaforma (GitHub, GitLab, Bitbucket).
git clone https://github.com/utente/progetto.git
cd progetto
Salvataggio credenziali HTTPS (Opzionale)
Automatizza l’inserimento delle credenziali. 
git config --global credential.helper manager-core
Fai il Tuo Primo Commit
Modifica i file, aggiungili con add e crea il primo commit. Poi pusha sul remoto per 
condividere il tuo lavoro con il mondo!
git add .
git commit -m "Primo commit"
git push origin main
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Push, Pull e Fetch in Git
Comprendere i comandi fondamentali per la sincronizzazione tra repository locale e 
remoto
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Terminologia Chiave di Git
1
Push
Invia le tue modifiche locali al repository 
remoto. È come dire: "Ho fatto del lavoro, 
condividiamolo con il team!"
git push origin main
Questo comando invia i tuoi commit al 
branch main del repository remoto 
chiamato origin.
2
Pull
Scarica le modifiche dal repository remoto 
e le integra nel tuo locale. Rimani sempre 
aggiornato con il lavoro degli altri.
git pull origin main
Combina fetch e merge in un solo comando 
per semplificare la sincronizzazione.
3
Fetch
Scarica le informazioni sui cambiamenti 
remoti senza modificarlo ancora il tuo 
codice locale. Permette di vedere cosa è 
cambiato.
git fetch origin
Dopo il fetch, puoi decidere quando e come 
integrare le modifiche con merge o rebase.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

git push: Caricare le Tue Modiﬁche
Il comando git push è il tuo strumento per condividere il lavoro completato con il team. 
Quando hai finito di lavorare su una funzionalità o hai corretto un bug, usa push per inviare i 
tuoi commit al repository remoto.
Sintassi di Base
git push <remote> <branch>
Esempi comuni:
git push origin main
git push origin develop
git push origin feature/new-login
Quando Usare Push
• Completamento di una feature o bug fix
• Al termine di una sessione di lavoro
• Dopo aver risolto i conflitti
• Per backup automatico del tuo lavoro
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Flusso di git push
Repository Remoto
Esegui git push
Repository Locale
Quando esegui git push, Git confronta la cronologia dei commit locali con quella remota. Se la tua cronologia è più recente, Git carica i nuovi commit sul repository remoto. 
Se invece il remoto ha commit più recenti, Git rifiuterà il push per evitare perdita di lavoro.
Attenzione: Se qualcun altro ha pushato modifiche dopo che hai clonato il repository, il tuo push verrà rifiutato. In questo caso, devi prima eseguire git pull per 
integrare le modifiche remote.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

git pull: Aggiornare il Lavoro Locale
Il comando git pull è una scorciatoia conveniente che combina due operazioni: git fetch (scarica le modifiche) e git merge (applica le modifiche). È il 
modo più comune per mantenere il tuo repository locale sincronizzato.
01
Scaricamento
Git scarica tutti i nuovi commit dal repository 
remoto
02
Integrazione
Git automaticamente unisce (merge) le modifiche 
remote con il tuo branch locale
03
Risultato
Il tuo repository locale è ora aggiornato con tutte 
le modifiche remote
Esempio di Terminale
git pull origin main
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0)
Unpacking objects: 100% (3/3), done.
From github.com:user/project
 * branch main -> FETCH_HEAD
 1a2b3c4..5d6e7f8 main -> origin/main
Updating 1a2b3c4..5d6e7f8
Fast-forward
 README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

git fetch: Esplorare le Modiﬁche Remote
Come Funziona
Il comando git fetch scarica le informazioni sulle modifiche remote senza 
modificarne il tuo repository locale. I commit vengono memorizzati in 
una branch remota (es. origin/main) ma non vengono automaticamente 
applicati alla tua branch corrente.
Sintassi
git fetch origin
git fetch origin main
git fetch --all
Quando Usare Fetch
• Vuoi vedere cosa hanno fatto gli altri senza modificare il tuo lavoro
• Devi esaminare le modifiche prima di applicarle
• Vuoi evitare merge automatici che potrebbero causare conflitti
• Stai lavorando in un ambiente dove la cautela è essenziale
Consiglio Pratico: Usa git fetch seguito da git diﬀ origin/main per vedere le diﬀerenze prima di decidere se fare merge. Poi esegui git merge 
origin/main per applicare le modifiche.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Push vs Pull vs Fetch
git push
Direzione: Locale → Remoto
Eﬀetto: Carica i tuoi commit
Rischi: Può essere rifiutato se il remoto è 
avanti
git pull
Direzione: Remoto → Locale
Eﬀetto: Fetch + Merge automatico
Rischi: Può creare conflitti durante il merge
git fetch
Direzione: Remoto → Locale (copia remota)
Eﬀetto: Solo download, nessuna modifica
Rischi: Nessuno, completamente sicuro
La scelta tra questi comandi dipende dal tuo workflow e dal livello di controllo che desideri. git pull è conveniente per la maggior parte dei casi, mentre 
git fetch oﬀre maggiore controllo e consapevolezza.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Esercizio Guidato: Workﬂow Completo
Seguiamo un esempio pratico che simula una situazione reale di collaborazione. Questo esercizio ti aiuterà a comprendere come i tre comandi lavorano insieme nel flusso di lavoro 
quotidiano.
Creare Repository Locale
mkdir my-project
cd my-project
git init
echo "Hello World" > README.md
git add README.md
git commit -m "Initial commit"
Collegare Repository Remoto
git remote add origin https://github.com/user/my-project.git
git remote -v
git pull origin main --allow-unrelated-histories
Primo Push
git branch -M main
git push -u origin main
# -u imposta il tracking upstream
Simulare Modiﬁche Remote
(Apri il repository su GitHub web e modifica README.md aggiungendo una riga)
Eseguire Pull Locale
git pull origin main
# Git scarica e merge le modifiche
# Potrebbe creare un commit di merge
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Best Practices e Consigli Pratici
Fai Sempre Pull All'Inizio
Prima di iniziare una nuova sessione di 
lavoro, esegui git pull per assicurarti di 
partire dalla versione più recente del 
codice. Questo riduce drasticamente la 
probabilità di conflitti.
Usa Fetch per Esaminare le 
Modiﬁche
Se sei in dubbio su cosa è cambiato, usa 
git fetch seguito da git log origin/main o 
git diﬀ origin/main per vedere le 
modifiche prima di applicarle.
Commit Piccoli e Frequenti
Commits più piccoli rendono i conflitti più 
facili da risolvere. Invece di un grande 
commit, fai più commit mirati. Questo 
semplifica anche il debugging.
Comunica con il Team
Quando lavori su file che altri stanno 
modificando, comunicalo nel tuo team. 
Strumenti come pull request e code review 
aiutano a coordinare le modifiche.
Risolvi i Conﬂitti Attivamente
Quando Git segnala un conflitto, apri il file, 
cerca le sezioni contrassegnate con 
<<<<<<<, ======= e >>>>>>>, risolvi 
manualmente e poi esegui git add e git 
commit.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it
GitHub Essentials: .gitignore, 
Pull Request e Issues
Ora è il momento di fare il salto verso i workflow professionali su 
GitHub. Impareremo a proteggere il repository con .gitignore, a 
collaborare in team tramite Pull Request e a gestire il lavoro con le 
Issues.


© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it
Cos'è il File .gitignore e Perché è Fondamentale
Il problema
Quando lavori su un progetto, la tua cartella è piena di file che non 
devono mai finire su GitHub: credenziali segrete, dipendenze 
installate localmente, file generati automaticamente. Senza 
controllo, questi file vengono inclusi nei commit per errore.
Chiavi API e password nel file .env
Cartella node_modules con migliaia di file
File di build come /dist o /out
File di configurazione IDE (.idea/, .vscode/)
La soluzione
Il file .gitignore è un file di testo che dice a Git quali file e cartelle 
ignorare completamente. Va creato nella root del progetto e 
committato nel repository, così tutti i collaboratori applicano le stesse 
regole.
Regola d'oro: Se un file può essere generato 
automaticamente o contiene segreti, non deve mai essere 
tracciato da Git.

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it
Esempio Pratico di .gitignore per un Progetto Web
Ecco un esempio commentato e realistico per un progetto Node.js/React. Ogni sezione copre una categoria diversa di file da escludere.
# ========================
# Dipendenze
# ========================
node_modules/
.pnp
.pnp.js
# ========================
# File di ambiente (SEGRETI)
# ========================
.env
.env.local
.env.production
# ========================
# Build e output
# ========================
/build
/dist
/.next
/out
# ========================
# File di sistema e IDE
# ========================
.DS_Store
Thumbs.db
.idea/
.vscode/
*.log
File già tracciati
Se aggiungi un file al .gitignore ma Git lo sta già 
tracciando, il file continuerà ad apparire nei 
commit. Devi rimuoverlo dalla cache con:
git rm --cached nomefile

Collaborazione su Branch e 
Gestione dei Conﬂitti in Git 
Remoto
Lavorare in team con Git: dalla creazione di branch alla risoluzione di conflitti e best 
practice collaborative.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Creare e Pubblicare Branch su Remoto
I branch sono essenziali per lo sviluppo parallelo: permettono a più persone di lavorare su 
funzionalità diverse senza interferire tra loro. Creare un branch locale è solo il primo passo 
— devi anche pubblicarlo sul repository remoto per condividerlo con il team.
Comandi Fondamentali
git branch nome-branch — Crea un nuovo branch
git switch -c nome-branch — Crea e passa al branch (forma compatta)
git push origin nome-branch — Pubblica il branch remoto
git push -u origin nome-branch — Imposta upstream automatico
Attenzione: Il flag -u (o --set-upstream) collega il branch locale a quello remoto, permettendo di usare semplicemente git push e git pull senza specificare ogni 
volta il nome del branch.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Aggiornare un Branch con le 
Modiﬁche di Main
Durante lo sviluppo, il branch main può ricevere nuove modifiche da altri collaboratori. Per mantenere il 
tuo branch aggiornato e ridurre i conflitti futuri, devi periodicamente integrare le ultime modifiche di 
main nel tuo branch di lavoro.
Passo 1: Cambia Branch
git switch nome-branch
Assicurati di essere nel branch corretto
Passo 2: Fetch e Merge
git pull origin main
Scarica e integra le modifiche
Passo 3: Risolvi Conﬂitti
Se necessario, risolvi eventuali conflitti prima di procedere
Questo processo mantiene il tuo branch sincronizzato con lo stato più recente del progetto, facilitando il 
merge finale.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Pull Request e Merge Request: Collaborazione Controllata
Cos'è una Pull Request?
Una Pull Request (PR) o Merge Request (MR) è una proposta 
formale di integrare le modifiche di un branch in un altro 
(solitamente main). Non è un comando Git, ma una funzionalità 
delle piattaforme di hosting come GitHub, GitLab o Bitbucket.
Flusso Tipico
1. Sviluppa la feature in un branch dedicato
2. Pubblica il branch remoto
3. Crea una PR sulla piattaforma
4. Altri sviluppatori revisionano il codice
5. Si discutono eventuali modifiche
6. Si approva e si merge la PR
Benefici: Le PR permettono revisione del codice (code review), discussioni su modifiche, test automatici prima del merge, e una 
tracciabilità completa di ogni cambiamento.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Best Practice per la Collaborazione Efﬁcace
Nomi Chiari e Descrittivi
Usa convenzioni come feature/descriptive-name, bugfix/issue-description, o 
docs/update-guide. Evita nomi generici come new-feature o fix.
Commit Piccoli e Focalizzati
Fai commit frequenti con modifiche limitate e coerenti. Ogni commit dovrebbe rappresentare una 
modifica logica completa. Scrivi messaggi chiari e descrittivi.
Aggiorna Sempre Prima di Push
Esegui git pull origin main (o git merge main) nel tuo branch prima di pushare modifiche. 
Riduce drasticamente i conflitti e mantiene il branch sincronizzato.
Testa Prima di Push
Assicurati che il codice compili e passi i test prima di pubblicare le modifiche. Non pushare codice rotto su 
branch condivisi.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Cosa Sono le Issues e Perché Si Usano
Le Issues sono lo strumento di GitHub per tracciare tutto ciò che deve essere fatto in un progetto: bug da correggere, nuove funzionalità da 
aggiungere, domande, migliorie. Sono il punto di partenza di ogni attività di sviluppo professionale.
Bug Report
Qualcosa non funziona come dovrebbe. La Issue descrive il 
comportamento attuale, quello atteso e i passi per riprodurre il 
problema.
Feature Request
Una nuova funzionalità da sviluppare. La Issue descrive l'obiettivo, il 
valore per l'utente e i criteri di accettazione.
Label e Milestone
Le etichette categorizzano le Issues (bug, enhancement, 
documentation). Le milestone raggruppano Issues in sprint o versioni 
del prodotto.
Assegnazione
Ogni Issue può essere assegnata a uno o più sviluppatori. Chi è 
assegnato è responsabile di quella attività.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Collegare Issues e Pull Request: la Magia di "Closes #7"
GitHub permette di collegare automaticamente una Issue a una Pull Request usando parole chiave speciali nel messaggio di commit o nella 
descrizione della PR. Quando la PR viene mergiata, la Issue si chiude da sola.
Parole chiave supportate
Inseriscile nel messaggio di commit o nella descrizione della PR:
fixes #3
closes #7
resolves #12
Funzionano anche in inglese e italiano. GitHub riconosce 
automaticamente il numero della Issue e crea il collegamento.
Esempi concreti
# In un messaggio di commit:
git commit -m "Aggiunge validazione form
login - fixes #14"
# Nella descrizione della PR:
"Questa PR implementa il
reset password.
closes #22, closes #23"
💡
 Collegare Issue e PR rende la storia del progetto tracciabile: 
sai sempre perché è stato scritto quel codice.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Rebase vs Merge: Scegliere la 
Strategia Giusta
Due approcci, una sola domanda: come integrare il lavoro del tuo team in modo pulito 
ed eﬀicace? In questa presentazione esploriamo le diﬀerenze fondamentali tra git 
merge e git rebase, quando usare ciascuno, e le regole d'oro per non rovinare la storia 
del tuo repository.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Il Ciclo di Vita di un Branch
Prima di scegliere tra merge e rebase, è fondamentale capire perché questi comandi esistono. Quando più sviluppatori lavorano sullo stesso progetto, i 
branch divergono inevitabilmente. Git oﬀre due strategie distinte per ricongiungerli, ognuna con implicazioni diverse sulla storia del repository e sulla 
collaborazione.
Branch Divergono
Ogni sviluppatore lavora sul proprio branch, 
aggiungendo commit indipendenti.
Necessità di Integrare
Arriva il momento di unire il lavoro: feature 
completata, bugfix pronto, sprint finito.
Scelta della Strategia
Merge o Rebase? La risposta dipende dal 
contesto, dal team e dalle policy adottate.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Git Merge: Unire Preservando la Storia
git merge integra due branch creando un merge commit — un commit speciale con due genitori che registra esattamente quando e come le due linee di 
sviluppo si sono ricongiunte. La storia rimane intatta e autentica.
 Vantaggi
• Preserva la storia cronologica completa
• Sicuro su branch condivisi e pubblici
• Facile da capire e da annullare
• Mostra chiaramente quando avviene l'integrazione
 Svantaggi
• Genera merge commit aggiuntivi
• La storia può diventare intricata con molti branch
• Il log git appare meno lineare
• Più diﬀicile leggere la progressione del progetto
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Git Rebase: Riscrivere la Storia
git rebase sposta i commit del branch corrente sopra la punta del branch di destinazione, come se il lavoro fosse stato fatto partendo da lì. Il risultato 
è una storia perfettamente lineare, senza merge commit — ma attenzione: la storia viene riscritta.
Storia lineare
Rebase su 
main
Branch 
originario
 Vantaggi
• Storia lineare e leggibile
• Nessun merge commit superfluo
• git log più pulito e navigabile
• Facilita code review e bisect
 Svantaggi
• Riscrive gli hash dei commit
• Pericoloso su branch condivisi
• Conflitti da risolvere più volte
• Richiede maggiore esperienza
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Merge vs Rebase: Confronto Diretto
La scelta tra merge e rebase non è mai assoluta — dipende dal contesto. Questa tabella riassume i criteri principali per orientare la decisione nei casi più 
comuni durante lo sviluppo quotidiano.
Criterio 🔀
 git merge 🔁
 git rebase
Storia del repository Preserva tutto, con merge commit Riscrive, storia lineare
Branch condivisi (main, develop)  Sempre sicuro  Mai usare
Feature branch privati Accettabile Preferibile
Pull Request / Code Review Comune e consigliato Ottimo per pulire prima del merge
Risoluzione conflitti Una sola volta al merge Potenzialmente per ogni commit
Leggibilità del log Storia fedele ma complessa Log pulito e lineare
Quando usarlo Integrazione finale, hotfix, PR Aggiornare feature branch, squash
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Comandi Pratici Essenziali
Ecco i comandi fondamentali da conoscere. Ogni riga ha un caso d'uso preciso — padroneggiarli significa avere pieno controllo sul proprio flusso di lavoro Git.
Merge classico
git checkout main
git merge feature/login
Integra il branch feature/login in main, 
creando un merge commit che conserva la storia 
completa.
Rebase su main
git checkout feature/login
git rebase main
Riposiziona i commit del tuo branch sopra 
l'ultimo commit di main, ottenendo una storia 
lineare.
Rebase interattivo
git rebase -i HEAD~3
Apre un editor per modificare, unire (squash), 
rinominare o eliminare gli ultimi 3 commit prima 
di condividerli.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Non fare rebase su branch 
condivisi.
Il rebase riscrive la storia dei commit, cambiando i loro hash identificativi. Se altri sviluppatori hanno già 
scaricato quei commit sul loro repository locale, si troveranno con una storia divergente e incompatibile 
— causando confusione, perdita di lavoro e conflitti diﬀicili da risolvere.
 Rebase OK su...
• Feature branch locali non condivisi
• Branch personali prima di aprire una PR
• Commit non ancora pubblicati su remoto
 Rebase MAI su...
main, develop, release
• Branch già condivisi con il team
• Commit già presenti su origin/remoto
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Takeaway: La Strategia Giusta per Ogni Situazione
Non esiste una risposta universale tra merge e rebase — esistono buone pratiche da applicare con consapevolezza. Porta 
questi principi nel tuo workflow quotidiano.
Usa Merge per...
Integrazioni finali, Pull Request, branch condivisi. La storia resterà autentica e tracciabile.
Usa Rebase per...
Aggiornare branch locali, pulire commit prima di una PR, mantenere una storia leggibile.
Ricorda sempre...
Mai rebase su branch condivisi. Comunica con il team le policy adottate nel progetto.
Prossimi passi
Pratica in un repository sandbox, sperimenta entrambe le strategie, leggi la documentazione uﬀiciale di Git.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Esercizio in Coppia – Git 
Remoto Completo
Dal Repository alla Collaborazione Reale: un percorso guidato attraverso push, pull, 
fetch, branch, merge, conflitti e rebase. Git come si usa davvero, lavorando insieme su 
un repository condiviso.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Prerequisiti e Setup Iniziale
Prima di iniziare, verificate che entrambi abbiate tutto il necessario. Questo laboratorio funziona solo se la coppia è sincronizzata fin dal primo momento.
🖥
 Git Installato
Git deve essere installato e configurato con 
user.name e user.email validi su 
entrambe le macchine.
🐙
 Account GitHub
Entrambi devono avere un account GitHub 
attivo. Annotatevi il vostro username: vi 
servirà per l'invito come collaboratore.
Studente A — Owner
Crea il repository, invita il collaboratore, gestisce il merge finale su main.
Studente B — Collaboratore
Accetta l'invito, lavora sui branch, simula il conflitto e gestisce il rebase 
interattivo.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Creazione e Conﬁgurazione del Repository
Il primo passo: mettere in piedi il campo di lavoro condiviso. 
01
Solo Studente A
Crea un repository pubblico su GitHub chiamato 
git-lab-coppia, inizializzalo con README.md, poi vai 
in Settings › Collaborators e invita Studente B tramite 
il suo username GitHub.
02
Solo Studente B
Accetta l'invito ricevuto via email o notifica GitHub. Da 
questo momento sei uﬀicialmente collaboratore con 
accesso in scrittura al repository.
03
Entrambi
Clonate il repo: git clone https://github.com/studenteA/git-lab-coppia.git. Poi verificate con git 
remote -v e git config --list.
Verifica: Entrambi vedete la stessa cartella locale con il file README.md? 
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Push e Pull Base
Il ciclo fondamentale di Git: modificare, committare, condividere. Imparate a coordinarvi senza calpestare il lavoro dell'altro. 
Studente A — Prima
Crea studente-a.txt con il testo: "Ciao, sono lo Studente A. Sto 
imparando Git. "
Poi esegui:
• git add studente-a.txt
• git commit -m "feat: aggiunto profilo studente A"
• git push origin main
Studente B — Risponde
Esegui git pull origin main e verifica che studente-a.txt sia 
comparso. Poi crea studente-b.txt con testo analogo, committalo e 
pushalo.
Infine Studente A esegue di nuovo git pull per ricevere il file di B.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Fetch vs Pull: Capire la Differenza
Molti usano git pull senza sapere cosa fa davvero. Questa fase svela il meccanismo interno. Durata stimata: 10 minuti.
Studente A modifica il README.md aggiungendo la riga "Progetto creato durante il corso ITS Git", poi fa commit e push.
Studente B — invece di fare subito git pull — esplora passo dopo passo:
git fetch origin
Scarica le informazioni remote senza modificare i file locali. Puoi vedere 
cos'è cambiato senza ancora applicarlo.
git log origin/main --oneline
Osserva il nuovo commit di A nel log remoto. I tuoi file locali sono ancora 
invariati!
git diff HEAD origin/main
Visualizza esattamente le diﬀerenze tra il tuo stato locale e il remoto, riga per 
riga.
git merge origin/main
Applica le modifiche scaricate. fetch + merge = pull. Ora lo sai!
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Branch Remoti e Collaborazione Parallela
I branch sono il cuore del lavoro in team. Permettono di sviluppare funzionalità in isolamento senza rischiare di rompere main. 
Studente A — Crea il Branch
• git switch -c 
feature/lista-spesa
Crea lista-spesa.txt con 3 elementi
Commit: "feat: aggiunta lista 
della spesa"
• git push -u origin 
feature/lista-spesa
• Comunica il nome del branch a B
Studente B — Contribuisce
git fetch origin poi git branch -r
• git switch 
feature/lista-spesa
• Aggiunge 2 elementi alla lista, commit 
e push
Studente A — Merge su Main
• git pull origin 
feature/lista-spesa
• git switch main
• git merge feature/lista-spesa
• git push origin main
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Merge Conﬂict Intenzionale
Questa è la fase più realistica del laboratorio: simulate il conflitto più comune nei team reali. La regola: entrambi modificate la stessa riga dello stesso file.
Risoluzione
B riceve errore
A pusha
Setup
Studente B dovrà aprire descrizione-progetto.txt, trovare i marcatori <<<<<<< HEAD / ======= / >>>>>>>, decidere insieme la versione unificata, rimuovere i marcatori e poi 
eseguire git add → git commit → git push.
⚠
 Attenzione: I marcatori <<<<<<< non devono MAI finire in produzione. Verificate sempre i file prima del push!
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Rebase Interattivo: Una History Pulita
Un buon progetto ha una storia leggibile. Il rebase interattivo vi permette di trasformare commit "sporchi" in un unico commit significativo.
Studente B — Squash dei Commit
Crea il branch feature/note-personali e fai 4 commit disordinati su 
note.txt: "wip", "fix", "ancora fix", "ok ora va". Poi:
• git rebase -i HEAD~4
Lascia pick sul primo, cambia gli altri 3 in squash
Scrivi il messaggio finale: "feat: aggiunte note personali dello studente B"
git rebase origin/main per aggiornare il branch
• git push --force-with-lease origin 
feature/note-personali
Studente A — Nel Frattempo
Aggiungi una modifica qualsiasi a main e pushala. Questo simula 
l'avanzamento del progetto mentre B lavora sul suo branch.
Poi, dopo il push di B:
• git fetch origin
Esamina il log del branch di B con git log --oneline
• Commentate insieme: come appare la history prima e dopo lo squash?
 Attenzione: Usa --force-with-lease — mai --force semplice su 
branch condivisi. E il rebase va usato solo su branch personali!
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Ce l'avete Fatta! 
Avete completato un percorso completo di collaborazione Git reale. Ecco tutto quello che avete imparato e praticato insieme.
Push & Pull
Il ciclo base per sincronizzare il lavoro in team 
senza sovrascrivere le modifiche altrui.
Fetch vs Pull
Capire la diﬀerenza vi rende sviluppatori più 
consapevoli e meno soggetti a sorprese.
Branch Remoti
Lavorare in parallelo su feature separate è la base 
del flusso professionale con Git.
Merge Conﬂict
I conflitti fanno paura solo la prima volta. Ora 
sapete riconoscerli e risolverli con metodo.
Rebase Interattivo
Una history pulita è un regalo per il vostro futuro 
team. Squash dei commit sporchi in messaggi 
significativi.
 Prossimi passi: Esplorate le Pull Request su GitHub, i workflow Git Flow e la CI/CD. Il laboratorio di oggi è la base di tutto!
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Via Schiaparelli 14 - 10148 Torino
https://www.tc-web.it
Mail: franco.grivet@tc-web.it
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it
GRAZIE A TUTTI…..



---

# Lezione 4 - Git GUI e Client Grafici

**File:** `Lezione 4 - Git GUI e Client Grafici.pdf`
**Tipo:** `.pdf`
**Dimensione:** 1228.4 KB
**Ultima modifica:** 02/07/2026 09:28

---

Git GUI e Client Graﬁci
Una guida completa per sviluppatori che vogliono esplorare le interfacce grafiche per Git
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it


Perché Usare un Client Graﬁco?
Il Terminale Resta Potente
Se conosci già Git da terminale, hai una base solida. I comandi 
Git oﬀrono controllo totale e precisione, permettendoti di 
gestire ogni aspetto del version control con flessibilità massima.
Ma le GUI Aggiungono Valore
I client grafici non sostituiscono il terminale, ma lo integrano. Oﬀrono una 
visualizzazione immediata dello stato del repository, semplificano operazioni 
complesse e riducono la possibilità di errori nelle operazioni quotidiane.
• Visualizzazione istantanea della cronologia dei commit
• Gestione intuitiva dei conflitti di merge
• Produttività aumentata per task ripetitivi
• Curva di apprendimento ridotta per operazioni avanzate
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

I Vantaggi Principali delle GUI
Visualizzazione 
Graﬁca dei Branch
Vedere l'albero dei branch, i 
merge e le divergenze in 
formato grafico rende 
immediatamente 
comprensibile la struttura 
del progetto. Identificare 
dove sono avvenuti i merge 
e quali branch sono attivi 
diventa un'operazione visiva 
immediata.
Diff Visuale Avanzato
Le GUI mostrano le 
diﬀerenze tra versioni con 
evidenziazione del codice, 
rendering aﬀiancato e 
navigazione semplificata. 
Puoi vedere esattamente 
cosa è cambiato in ogni file 
senza dover interpretare 
output testuali complessi.
Risoluzione Conﬂitti 
Sempliﬁcata
Quando si verificano 
conflitti durante un merge, 
le GUI oﬀrono strumenti 
visivi per confrontare le 
versioni e scegliere quale 
codice mantenere. Il 
processo diventa più 
intuitivo rispetto alla 
modifica manuale dei file 
con marcatori di conflitto.
Staging Selettivo 
Intuitivo
Puoi facilmente scegliere 
quali modifiche includere 
nel prossimo commit, anche 
a livello di singole righe. La 
selezione visiva con 
checkbox e anteprime rende 
l'operazione di staging 
molto più veloce e precisa.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

I Principali Client Graﬁci Git
Esistono diversi client grafici per Git, ognuno con caratteristiche distintive. Ecco i quattro più popolari e utilizzati dalla comunità di sviluppatori.
SourceTree
Gratuito · Atlassian
Potente e completo, perfetto 
per utenti Windows e Mac. 
Oﬀre supporto nativo per Git 
Flow e integrazione con 
Bitbucket. Interfaccia ricca di 
funzionalità con curva di 
apprendimento moderata.
GitKraken
Freemium · Multi-piattaforma
Interfaccia moderna e 
accattivante con 
visualizzazione grafica 
eccellente. Include funzionalità 
avanzate come integrazione 
con Jira e GitHub Issues. 
Versione gratuita limitata per 
repository privati.
GitHub Desktop
Gratuito · GitHub
Semplice e minimalista, ideale 
per principianti. Integrazione 
perfetta con GitHub ma 
funziona con qualsiasi 
repository Git. Interfaccia 
pulita focalizzata sulle 
operazioni essenziali.
SmartGit
Commerciale · 
Multi-piattaforma
Client professionale con 
funzionalità avanzate per team 
enterprise. Include strumenti 
per code review, confronto file 
e gestione complessa di 
branch. Licenza gratuita per 
uso non commerciale.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Terminale vs GUI: Un Confronto Pratico
 Vantaggi del Terminale
Controllo totale: accesso a ogni comando e opzione disponibile in Git
Velocità: operazioni rapide tramite comandi memorizzati
Automazione: facilità di scripting e integrazione in pipeline CI/CD
Universalità: funziona ovunque, anche su server remoti via SSH
Leggerezza: nessun consumo di risorse grafiche
  Svantaggi del Terminale
• Richiede memorizzazione dei comandi
• Visualizzazione limitata della storia del progetto
• Gestione conflitti più complessa
• Curva di apprendimento iniziale ripida
 Vantaggi della GUI
Visualizzazione: grafico interattivo dei branch e della cronologia
Intuitività: operazioni point-and-click senza memorizzare sintassi
Produttività: staging parziale e merge visuale più veloci
Accessibilità: ideale per chi inizia o per task occasionali
Sicurezza: meno possibilità di errori con operazioni distruttive
  Svantaggi della GUI
• Consumo di risorse di sistema
• Alcune operazioni avanzate non disponibili
• Diﬀicile automazione di workflow
• Dipendenza dall'interfaccia specifica
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Conﬁgurazione Globale di Git
Prima di iniziare a usare SourceTree per i tuoi progetti, è fondamentale configurare correttamente le impostazioni globali di Git. 
Questi parametri identificano l'autore dei commit e sono visibili nella cronologia del progetto.
Nome Utente ed Email
Nelle preferenze di SourceTree, vai alla sezione Generale o Git. Inserisci il tuo nome completo e l'indirizzo email associato al tuo 
account GitHub o GitLab. Questi dati appariranno in ogni commit che eﬀettuerai.
git config --global user.name "Tuo Nome"
git config --global user.email "tua@email.com"
Puoi anche impostare questi valori direttamente da terminale con i comandi mostrati sopra.
Editor di Testo Predeﬁnito
SourceTree può aprire automaticamente un editor quando necessario (per esempio, durante rebase interattivi o merge con conflitti). Configura il tuo 
editor preferito nelle impostazioni, scegliendo tra opzioni come Visual Studio Code, Sublime Text o Atom.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Guida Pratica a SourceTree
SourceTree è un client grafico gratuito per Git e Mercurial che semplifica la gestione dei repository attraverso un'interfaccia 
visuale intuitiva. Questa guida ti accompagnerà passo dopo passo nell'uso delle funzionalità principali, dalle operazioni 
base come commit e push, fino alla gestione avanzata di branch, merge e risoluzione dei conflitti. Che tu sia uno 
sviluppatore alle prime armi o un professionista esperto, SourceTree ti permette di visualizzare la storia del progetto, gestire 
le modifiche e collaborare con il team in modo eﬀiciente.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Installare SourceTree: Primi Passi
01
Download del Client
Visita il sito uﬀiciale sourcetreeapp.com e scarica la versione per il tuo 
sistema operativo (Windows o macOS). Il download è gratuito e non 
richiede licenza.
02
Esegui l'Installatore
Avvia il file scaricato e segui la procedura guidata. Su macOS potresti dover 
autorizzare l'installazione nelle preferenze di sicurezza. Su Windows, 
accetta le autorizzazioni richieste.
03
Registrazione Account
Al primo avvio, SourceTree richiederà di creare un account Atlassian 
gratuito o di eﬀettuare il login. Questo account è necessario per utilizzare il 
software, ma non implica costi.
04
Veriﬁca Installazione Git
SourceTree rileverà automaticamente se Git è già installato sul sistema. Se 
non lo trova, ti oﬀrirà di installare una versione embedded oppure di 
specificare il percorso della tua installazione esistente.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Collegare Account GitHub
Per lavorare con repository remoti, è utile collegare i tuoi account delle piattaforme di hosting 
direttamente in SourceTree. Questo semplifica le operazioni di clone, push e pull.
Apri le Preferenze
Vai su Strumenti → Opzioni (Windows) o SourceTree → Preferenze (macOS) e seleziona 
la scheda Account.
Aggiungi Account
Clicca Aggiungi e scegli il servizio (GitHub, GitLab, Bitbucket). Seleziona il protocollo di 
autenticazione preferito: OAuth o Personal Access Token.
Autorizza
Segui il flusso di autenticazione nel browser. Dovrai autorizzare SourceTree ad accedere 
ai tuoi repository. Completa il processo e torna all'applicazione.
Suggerimento: Per GitLab, potrebbe essere necessario generare un Personal Access Token 
manualmente dal sito di GitLab con permessi appropriati (api, read_repository, 
write_repository).
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Clonare Repository Esistenti
1 Ottenere l'URL
Copia l'URL del repository da GitHub, GitLab o Bitbucket. Può essere HTTPS o 
SSH, a seconda della configurazione della tua autenticazione.
2 Avviare Clone
In SourceTree, clicca su "Clone" nella schermata iniziale o usa File > 
Clone/New. Si aprirà una finestra di dialogo dedicata all'operazione.
3 Inserire Dettagli
Incolla l'URL nel campo "Source Path" e scegli dove salvare il repository 
localmente nel campo "Destination Path" . Assegna un nome al bookmark per 
riconoscerlo facilmente.
4 Download Completo
SourceTree scaricherà l'intera cronologia del progetto. Una volta completato, 
potrai iniziare a lavorare immediatamente sui file con accesso completo alla 
storia e ai branch.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Panoramica dell'Interfaccia Utente
Repository View
La vista principale 
mostra tutti i tuoi 
repository locali e 
remoti. Puoi facilmente 
passare da un progetto 
all'altro con un 
semplice clic.
Branches Panel
Il pannello laterale 
elenca tutti i branch 
disponibili, sia locali 
che remoti, 
permettendo una 
navigazione rapida tra 
le diverse linee di 
sviluppo.
Staging Area
La zona centrale dove 
prepari i file da 
committare. Puoi 
selezionare quali 
modifiche includere nel 
prossimo commit 
trascinandole tra le 
sezioni.
Commit History
Il grafico della cronologia visualizza l'intera storia del progetto con linee che 
rappresentano branch, merge e l'evoluzione del codice nel tempo.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Creare e Cambiare Branch
Operazioni sui Branch
I branch permettono di sviluppare funzionalità in parallelo senza interferire con il 
codice principale. In SourceTree, creare un nuovo branch è semplice: clicca sul 
pulsante "Branch" nella toolbar, assegna un nome descrittivo e seleziona da 
quale commit partire.
Per cambiare branch, basta fare doppio clic sul branch desiderato nel pannello 
laterale. SourceTree aggiornerà automaticamente i file nella working directory 
per riflettere lo stato del branch selezionato. Questa operazione è chiamata 
"checkout" .
01
Clicca "Branch"
Nella toolbar superiore
02
Assegna Nome
Usa nomi descrittivi come 
"feature-login"
03
Seleziona Origine
Scegli il commit di partenza
04
Conferma Creazione
Il nuovo branch è pronto
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Commit, Push e Pull: Il Ciclo Base
Commit
Salva le modifiche localmente. 
Seleziona i file nella staging area, scrivi 
un messaggio descrittivo e clicca 
"Commit" . Le modifiche sono ora parte 
della storia locale.
Push
Carica i commit locali sul server 
remoto. Clicca "Push" nella toolbar, 
seleziona il branch e conferma. I tuoi 
colleghi potranno ora vedere le tue 
modifiche.
Pull
Scarica le modifiche dal server. Clicca "Pull" per sincronizzare il tuo repository 
locale con quello remoto, integrando il lavoro degli altri membri del team.
Consiglio pratico: Esegui sempre un pull prima di iniziare a lavorare per evitare conflitti. Commita frequentemente con messaggi chiari e 
descrittivi che spiegano cosa è stato modificato e perché.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Risolvere Conﬂitti di Merge
I conflitti si verificano quando due branch modificano le stesse righe di codice in modo diverso. SourceTree evidenzia i file in conflitto con un'icona speciale. Quando 
tenti un merge e si verifica un conflitto, SourceTree ti avvisa immediatamente e ti permette di risolverlo in diversi modi.
Identiﬁcare il Conﬂitto
I file con conflitti appaiono nella sezione "Uncommitted changes" con 
un'icona di avviso. SourceTree sospende il merge fino alla risoluzione.
Scegliere la Strategia
Puoi usare l'editor integrato per vedere entrambe le versioni, accettare una 
versione specifica (Mine/Theirs), o aprire un tool di merge esterno per 
maggiore controllo.
Risolvere Manualmente
Modifica il file per combinare le modifiche nel modo corretto. Rimuovi i 
marker di conflitto (<<<<<<<, =======, >>>>>>>) e mantieni il codice 
desiderato.
Completare il Merge
Dopo aver risolto tutti i conflitti, aggiungi i file alla staging area e completa il 
commit di merge. La cronologia mostrerà la confluenza dei due branch.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Usare Stash per Salvare Modiﬁche Temporanee
Cos'è lo Stash?
Lo stash è come un cassetto temporaneo dove 
"parcheggi" le modifiche in corso quando devi cambiare 
branch urgentemente o fare un pull senza committare. Le 
modifiche vengono salvate in modo sicuro e possono 
essere riapplicate in qualsiasi momento.
È particolarmente utile quando stai lavorando su 
qualcosa di incompleto e hai bisogno di switchare 
contesto rapidamente per risolvere un bug urgente o 
revisionare il codice di un collega.
1
Creare Stash
Clicca "Stash" nella toolbar. Assegna 
un nome descrittivo per identificarlo 
facilmente in seguito. Le modifiche 
scompaiono dalla working directory.
2
Visualizzare Stash
Il pannello "Stashes" nel sidebar 
mostra tutti gli stash salvati. Puoi 
averne multipli 
contemporaneamente, ognuno con il 
proprio nome.
3
Applicare Stash
Fai doppio clic sullo stash o usa "Apply Stash" . Le modifiche tornano nella working 
directory. Puoi scegliere se mantenere o eliminare lo stash dopo l'applicazione.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Tagging: Marcare Versioni Importanti
I tag sono etichette permanenti assegnate a commit specifici, ideali per marcare release, versioni stabili o milestone importanti del progetto. A diﬀerenza dei 
branch che evolvono, i tag rimangono fissi a un punto specifico della storia. In SourceTree, puoi crearli facilmente selezionando un commit e cliccando "Tag" 
nella toolbar.
Creare Tag Annotati
I tag annotati includono nome, messaggio, data e 
autore. Sono ideali per release uﬀiciali. Esempio: 
v1.0.0 con note di rilascio.
Convenzioni di Naming
Usa il Semantic Versioning (MAJOR.MINOR.PATCH) 
per chiarezza. v2.1.3 indica versione major 2, minor 
1, patch 3. Facilita la comunicazione nel team.
Condividere Tag
I tag locali non vengono automaticamente pushati. 
Usa "Push" e seleziona "Push all tags" per 
condividerli con il team sul repository remoto.
Best practice: Crea tag per ogni release in produzione. Facilita il rollback in caso di problemi e permette di ricostruire esattamente lo stato del codice 
in un momento specifico. I tag sono immutabili e aﬀidabili.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Cherry-Pick: Selezionare i Commit Perfetti
Il cherry-pick è una delle funzionalità più potenti di Git: permette 
di copiare commit specifici da un branch all'altro senza dover fare 
un merge completo. È come scegliere le ciliegie migliori da un 
albero!
Quando utilizzarlo:
• Correggere bug urgenti su production
• Portare feature specifiche tra branch
• Recuperare commit da branch eliminati
• Applicare hotfix selettivi
Come Fare Cherry-Pick in SourceTree
1. Seleziona il branch di destinazione
2. Trova il commit da copiare nella cronologia
3. Click destro sul commit → Cherry-Pick
4. SourceTree applica le modifiche automaticamente
Nota: Potrebbero verificarsi conflitti se le modifiche toccano le stesse righe di 
codice.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Diff Graﬁco: Analizzare le Modiﬁche Visivamente
SourceTree oﬀre uno strumento di diﬀ grafico potentissimo che rende la revisione del codice intuitiva e veloce. Ogni modifica viene evidenziata con colori 
diversi, permettendo di capire immediatamente cosa è cambiato tra versioni diverse del codice.
1
Aprire il Diff
Seleziona un commit nella cronologia e clicca su "File Status" nel pannello inferiore
2
Navigare le Modiﬁche
Doppio click su un file modificato apre la vista diﬀ side-by-side con evidenziazione delle righe cambiate
3
Confrontare Branch
Usa la funzione "Compare" per vedere tutte le diﬀerenze tra due branch prima di un merge
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Esercizio in Coppia — Workﬂow Collaborativo Completo
Prerequisiti
● Entrambi: account GitHub, SourceTree installato, Git configurato con nome e email
● Studente B comunica il proprio username GitHub a Studente A
FASE 1 — Setup del Repository — Solo Studente A
1. Crea un repository su GitHub chiamato progetto-squadra con README.md e licenza MIT
2. Vai in Settings → Collaborators → aggiungi Studente B come collaboratore
3. Clona il repository in SourceTree
4. Crea un file sito.txt con questo contenuto:
  Titolo: Il Mio Sito Web
   Autore: [nome di A]
   Versione: 0.1
   Descrizione: progetto di test
5. Crea un file .gitignore con: *.log, *.tmp, temp/, .DS_Store
6. Stage entrambi i file → commit con messaggio Initial commit: add sito.txt and .gitignore → Push
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Esercizio in Coppia — Workﬂow Collaborativo Completo
FASE 2 — Lavoro Parallelo su Branch Separati — Entrambi in contemporanea
Studente B: Clona il repository in SourceTree
Studente A:
1. Crea branch feature/sezione-servizi da main
2. Aggiunge in fondo a sito.txt:
  --- SERVIZI ---
   - Web Design
   - Sviluppo App
   - Consulenza IT
3. Commit con messaggio feat: add sezione servizi → Push del branch
Studente B:
1. Crea branch feature/sezione-contatti da main
2. Aggiunge in fondo a sito.txt:
  --- CONTATTI ---
   Email: info@sito.it
   Tel: 011-0000000
   Indirizzo: Torino
3. Commit con messaggio feat: add sezione contatti → Push del branch
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Esercizio in Coppia — Workﬂow Collaborativo Completo
FASE 3 — Merge e Generazione del Conflitto — Leggete l'ordine con attenzione
Studente A:
1. Checkout su main
2. Click destro su feature/sezione-servizi → Merge into current branch → Push
3. Rimane su main → modifica la prima riga di sito.txt da Titolo: Il Mio Sito Web a Titolo: Sito Web Ufficiale → 
Commit (non pushare ancora)
Studente B:
1. Fa Pull di main → ha ora la sezione servizi di A
2. Sul branch feature/sezione-contatti → modifica la stessa prima riga a Titolo: Portale dei Servizi (diverso da 
quello di A!)
3. Commit con messaggio feat: add sezione contatti e aggiorna titolo
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Esercizio in Coppia — Workﬂow Collaborativo Completo
FASE 4 — Risoluzione del Conflitto — Studente A esegue, B osserva e consiglia
1. Studente A fa Push del proprio commit su main
2. Studente B: checkout su main → Pull → torna su feature/sezione-contatti → click destro su main → Merge 
into current branch → appare il conflitto!
3. In SourceTree, sito.txt mostra l'icona  nella sezione Uncommitted changes
4. Aprite sito.txt con l'editor: vedrete i marcatori <<<<<<<, =======, >>>>>>>
5. Decidete insieme il titolo definitivo → rimuovete tutti i marcatori → salvate
6. Stage del file → commit con messaggio merge: resolve conflict on titolo, integrate sezione 
contatti → Push del branch
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Esercizio in Coppia — Workﬂow Collaborativo Completo
FASE 5 — Stash, Hotfix e Cherry-Pick — Entrambi
Studente A:
1. Aggiunge a sito.txt la riga Copyright: 2026 — non fa commit
2. Pulsante Stash → nome: wip: aggiunta copyright → Conferma. Il file torna pulito
3. Crea branch hotfix/typo-autore da main → corregge il campo Autore con il nome completo → commit fix: correggi 
nome autore → Push
Studente B:
1. Nel log di hotfix/typo-autore, click destro sul commit dell'hotfix → Cherry-Pick
2. Verifica che la correzione sia apparsa nel suo branch senza fare un merge completo
Studente A:
1. Pannello Stashes → doppio clic su wip: aggiunta copyright → Apply Stash
2. Stage → commit chore: add copyright info → Push su main
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Esercizio in Coppia — Workﬂow Collaborativo Completo
FASE 6 — Merge Finale, Tag e Pulizia — Insieme
1. Checkout main → Pull → click destro su feature/sezione-contatti → Merge into current branch
2. Merge di hotfix/typo-autore su main nello stesso modo → Push
3. Pulsante Tag → nome: v1.0 → messaggio: Prima release completa → Push all tags
4. Cancellate tutti i branch feature e hotfix (click destro → Delete)
5. Entrambi fanno Pull su main e verificano che la cronologia sia identica su entrambe le macchine
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Riepilogo: Le Operazioni Fondamentali
Facciamo un recap completo di tutto quello che abbiamo imparato in questo corso. Queste sono le competenze che userai quotidianamente nel tuo 
lavoro di sviluppo.
Branching
Creare, cambiare e gestire 
branch per lavorare su feature 
isolate
Commit
Salvare snapshot del codice 
con messaggi chiari e 
descrittivi
Merge
Integrare modifiche da branch 
diversi, risolvendo eventuali 
conflitti
Push/Pull
Sincronizzare il lavoro locale 
con il repository remoto del 
team
Cherry-Pick
Selezionare commit specifici da applicare ad altri branch
Revert/Reset
Annullare modifiche in modo sicuro o riscrivere la cronologia locale
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

BEST PRACTICES
Combinare Terminale e GUI: Il Meglio di Due Mondi
Non devi scegliere tra GUI e terminale: i professionisti usano entrambi strategicamente! Ogni strumento ha i suoi punti di forza e sapere quando usare 
l'uno o l'altro ti renderà molto più eﬀiciente.
Quando Usare SourceTree (GUI)
Visualizzare la cronologia: vedere il grafico dei branch è molto più 
chiaro
Gestire conflitti di merge: l'interfaccia grafica semplifica la risoluzione
Cherry-pick e operazioni complesse: meno errori con l'interfaccia 
visuale
Revieware modifiche: il diﬀ side-by-side è imbattibile
Gestire staging selettivo: scegliere singole righe da committare
Quando Usare il Terminale
Operazioni ripetitive: script e alias accelerano il lavoro
Comandi veloci: git status o git pull sono più rapidi da terminale
Automazione: integrare Git in pipeline CI/CD
Operazioni avanzate: alcuni comandi Git non hanno equivalente GUI
Troubleshooting: messaggi di errore più dettagliati
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Consigli Pratici per il Successo
Commit Atomici e 
Messaggi Chiari
Ogni commit dovrebbe 
rappresentare una singola 
modifica logica. Scrivi messaggi 
descrittivi che spiegano il 
"perché" , non solo il "cosa" . Usa il 
tempo presente imperativo: "Add 
feature" non "Added feature" .
Pull Frequente, Push 
Regolare
Fai pull almeno una volta al 
giorno per rimanere 
sincronizzato con il team. 
Pusha il tuo lavoro 
frequentemente per evitare di 
perdere modifiche e 
permettere ai colleghi di 
vedere i tuoi progressi.
Strategia di Branching 
Coerente
Adotta una convenzione per i 
nomi dei branch (es: 
feature/, bugfix/, 
hotfix/) e rispettala. 
Cancella i branch dopo il 
merge per mantenere il 
repository pulito e 
organizzato.
Test Prima di Pushare
Verifica sempre che il codice 
compili e i test passino prima 
di fare push. Un commit 
rotto sul branch condiviso 
blocca tutto il team. Usa git 
stash per salvare 
temporaneamente 
modifiche incomplete.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Congratulazioni! Siete Pronti per il Mondo Reale
Avete completato il vostro percorso formativo su SourceTree e Git! Ora possedete tutte le competenze necessarie per collaborare eﬀicacemente in 
progetti reali, gestire branch complessi e risolvere conflitti con sicurezza.
Continua a Praticare
La vera padronanza arriva con l'esperienza 
quotidiana. Sperimenta con repository di 
test e non aver paura di sbagliare.
Risorse Utili
Consulta la documentazione uﬀiciale di Git 
e SourceTree quando hai dubbi. La 
community è sempre pronta ad aiutare.
Prossimi Passi
Esplora Git Flow, rebasing avanzato e hook 
personalizzati per portare le tue skill al 
livello successivo.
Ricorda: Git è uno strumento potente che diventa sempre più intuitivo con l'uso. Buon coding e buon versionamento!
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it

Via Schiaparelli 14 - 10148 Torino
https://www.tc-web.it
Mail: franco.grivet@tc-web.it
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl -  Via Schiaparelli 14 - Torino     https://www.tc-web.it
GRAZIE A TUTTI…..



---

# Quiz Version Control

**File:** `Quiz Version Control.docx`
**Tipo:** `.docx`
**Dimensione:** 9.5 KB
**Ultima modifica:** 02/07/2026 09:24

---

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

A. Git

B. Mercurial

C. SVN

D. Dropbox

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

A. Bill Gates

B. Guido van Rossum

C. Linus Torvalds

D. Mark Zuckerberg

12. In che anno è nato Git?

A. 1995

B. 2000

C. 2005

D. 2010

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

A. git commit

B. git status

C. git add

D. git log

18. Cos'è un commit?

A. Un backup automatico

B. Una cartella di progetto

C. Un'istantanea dello stato del progetto

D. Un file temporaneo

19. Cosa contiene sempre un commit?

A. Solo il codice

B. Un messaggio, autore e data

C. Una connessione Internet

D. Un branch

20. Qual è una buona pratica sui commit?

A. Fare un solo commit al giorno

B. Usare messaggi generici

C. Un'idea = un commit

D. Evitare commit frequenti

21. Quale messaggio di commit è corretto?

A. fix

B. update

C. Aggiunta validazione form login

D. funziona!!!

22. Nella prima riga del messaggio di commit è consigliato:

A. Usare il passato

B. Usare l'imperativo presente

C. Scrivere più di 100 caratteri

D. Non scrivere nulla

23. Qual è un errore comune dei principianti?

A. Usare git status

B. Committare spesso

C. Dimenticare git add

D. Scrivere messaggi chiari

24. Perché non bisogna avere paura di Git?

A. Perché cancella i file automaticamente

B. Perché è impossibile sbagliare

C. Perché protegge il lavoro committato

D. Perché funziona solo online

25. Quale comando mostra la cronologia dei commit?

A. git add

B. git status

C. git log

D. git init

