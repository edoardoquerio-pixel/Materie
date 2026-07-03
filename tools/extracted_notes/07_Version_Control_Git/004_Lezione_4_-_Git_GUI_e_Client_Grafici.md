# Lezione 4

Fonte: `Lezione 4 - Git GUI e Client Grafici.pdf`

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

•

Visualizzazione istantanea della cronologia dei commit

• Gestione intuitiva dei conflitti di merge

•

•

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

immediatamente 

comprensibile la struttura 

del progetto. Identificare 

dove sono avvenuti i merge 

e quali branch sono attivi 

diventa un'operazione visiva 

immediata.

Diff Visuale Avanzato

Risoluzione Conﬂitti 

Staging Selettivo 

Sempliﬁcata

Intuitivo

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

SourceTree

GitKraken

GitHub Desktop

SmartGit

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

avanzate come integrazione 

repository Git. Interfaccia 

funzionalità con curva di 

con Jira e GitHub Issues. 

pulita focalizzata sulle 

apprendimento moderata.

Versione gratuita limitata per 

operazioni essenziali.

repository privati.

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
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

Terminale vs GUI: Un Confronto Pratico

 Vantaggi del Terminale

 Vantaggi della GUI

Controllo totale: accesso a ogni comando e opzione disponibile in Git

Visualizzazione: grafico interattivo dei branch e della cronologia

Velocità: operazioni rapide tramite comandi memorizzati

Intuitività: operazioni point-and-click senza memorizzare sintassi

Automazione: facilità di scripting e integrazione in pipeline CI/CD

Produttività: staging parziale e merge visuale più veloci

Universalità: funziona ovunque, anche su server remoti via SSH

Accessibilità: ideale per chi inizia o per task occasionali

Leggerezza: nessun consumo di risorse grafiche

Sicurezza: meno possibilità di errori con operazioni distruttive

 Svantaggi del Terminale

 Svantaggi della GUI

•

•

Richiede memorizzazione dei comandi

Visualizzazione limitata della storia del progetto

•

•

Consumo di risorse di sistema

Alcune operazioni avanzate non disponibili

• Gestione conflitti più complessa

• Diﬀicile automazione di workflow

•

Curva di apprendimento iniziale ripida

• Dipendenza dall'interfaccia specifica

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

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
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

Guida Pratica a SourceTree

SourceTree è un client grafico gratuito per Git e Mercurial che semplifica la gestione dei repository attraverso un'interfaccia 

visuale intuitiva. Questa guida ti accompagnerà passo dopo passo nell'uso delle funzionalità principali, dalle operazioni 

base come commit e push, fino alla gestione avanzata di branch, merge e risoluzione dei conflitti. Che tu sia uno 

sviluppatore alle prime armi o un professionista esperto, SourceTree ti permette di visualizzare la storia del progetto, gestire 

le modifiche e collaborare con il team in modo eﬀiciente.

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

Installare SourceTree: Primi Passi

01

Download del Client

02

Esegui l'Installatore

Visita il sito uﬀiciale sourcetreeapp.com e scarica la versione per il tuo 

Avvia il file scaricato e segui la procedura guidata. Su macOS potresti dover 

sistema operativo (Windows o macOS). Il download è gratuito e non 

autorizzare l'installazione nelle preferenze di sicurezza. Su Windows, 

richiede licenza.

03

accetta le autorizzazioni richieste.

04

Registrazione Account

Veriﬁca Installazione Git

Al primo avvio, SourceTree richiederà di creare un account Atlassian 

SourceTree rileverà automaticamente se Git è già installato sul sistema. Se 

gratuito o di eﬀettuare il login. Questo account è necessario per utilizzare il 

non lo trova, ti oﬀrirà di installare una versione embedded oppure di 

software, ma non implica costi.

specificare il percorso della tua installazione esistente.

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

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
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

Clonare Repository Esistenti

1

2

3

4

Ottenere l'URL

Copia l'URL del repository da GitHub, GitLab o Bitbucket. Può essere HTTPS o 

SSH, a seconda della configurazione della tua autenticazione.

Avviare Clone

In SourceTree, clicca su "Clone" nella schermata iniziale o usa File > 

Clone/New. Si aprirà una finestra di dialogo dedicata all'operazione.

Inserire Dettagli

Incolla l'URL nel campo "Source Path" e scegli dove salvare il repository 

localmente nel campo "Destination Path". Assegna un nome al bookmark per 

riconoscerlo facilmente.

Download Completo

SourceTree scaricherà l'intera cronologia del progetto. Una volta completato, 

potrai iniziare a lavorare immediatamente sui file con accesso completo alla 

storia e ai branch.

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

Panoramica dell'Interfaccia Utente

Repository View

Branches Panel

Staging Area

La vista principale 

Il pannello laterale 

La zona centrale dove 

mostra tutti i tuoi 

elenca tutti i branch 

prepari i file da 

repository locali e 

disponibili, sia locali 

committare. Puoi 

remoti. Puoi facilmente 

che remoti, 

selezionare quali 

passare da un progetto 

permettendo una 

modifiche includere nel 

all'altro con un 

navigazione rapida tra 

prossimo commit 

semplice clic.

le diverse linee di 

trascinandole tra le 

sviluppo.

sezioni.

Commit History

Il grafico della cronologia visualizza l'intera storia del progetto con linee che 

rappresentano branch, merge e l'evoluzione del codice nel tempo.

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

Creare e Cambiare Branch

Operazioni sui Branch

I branch permettono di sviluppare funzionalità in parallelo senza interferire con il 

codice principale. In SourceTree, creare un nuovo branch è semplice: clicca sul 

pulsante "Branch" nella toolbar, assegna un nome descrittivo e seleziona da 

quale commit partire.

Per cambiare branch, basta fare doppio clic sul branch desiderato nel pannello 

laterale. SourceTree aggiornerà automaticamente i file nella working directory 

01

Clicca "Branch"

Nella toolbar superiore

02

Assegna Nome

Usa nomi descrittivi come 

"feature-login"

per riflettere lo stato del branch selezionato. Questa operazione è chiamata 

03

"checkout".

Seleziona Origine

Scegli il commit di partenza

04

Conferma Creazione

Il nuovo branch è pronto

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

Commit, Push e Pull: Il Ciclo Base

Commit

Push

Salva le modifiche localmente. 

Seleziona i file nella staging area, scrivi 

un messaggio descrittivo e clicca 

"Commit". Le modifiche sono ora parte 

della storia locale.

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
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

Risolvere Conﬂitti di Merge

I conflitti si verificano quando due branch modificano le stesse righe di codice in modo diverso. SourceTree evidenzia i file in conflitto con un'icona speciale. Quando 

tenti un merge e si verifica un conflitto, SourceTree ti avvisa immediatamente e ti permette di risolverlo in diversi modi.

Identiﬁcare il Conﬂitto

Scegliere la Strategia

Puoi usare l'editor integrato per vedere entrambe le versioni, accettare una 

I file con conflitti appaiono nella sezione "Uncommitted changes" con 

versione specifica (Mine/Theirs), o aprire un tool di merge esterno per 

un'icona di avviso. SourceTree sospende il merge fino alla risoluzione.

maggiore controllo.

Risolvere Manualmente

Completare il Merge

Dopo aver risolto tutti i conflitti, aggiungi i file alla staging area e completa il 

Modifica il file per combinare le modifiche nel modo corretto. Rimuovi i 

commit di merge. La cronologia mostrerà la confluenza dei due branch.

marker di conflitto (<<<<<<<, =======, >>>>>>>) e mantieni il codice 

desiderato.

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

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

2

Creare Stash

Visualizzare Stash

Clicca "Stash" nella toolbar. Assegna 

Il pannello "Stashes" nel sidebar 

un nome descrittivo per identificarlo 

mostra tutti gli stash salvati. Puoi 

facilmente in seguito. Le modifiche 

averne multipli 

scompaiono dalla working directory.

contemporaneamente, ognuno con il 

proprio nome.

3

Applicare Stash

Fai doppio clic sullo stash o usa "Apply Stash". Le modifiche tornano nella working 

directory. Puoi scegliere se mantenere o eliminare lo stash dopo l'applicazione.

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

Tagging: Marcare Versioni Importanti

I tag sono etichette permanenti assegnate a commit specifici, ideali per marcare release, versioni stabili o milestone importanti del progetto. A diﬀerenza dei 

branch che evolvono, i tag rimangono fissi a un punto specifico della storia. In SourceTree, puoi crearli facilmente selezionando un commit e cliccando "Tag" 

nella toolbar.

Creare Tag Annotati

Convenzioni di Naming

Condividere Tag

I tag annotati includono nome, messaggio, data e 

Usa il Semantic Versioning (MAJOR.MINOR.PATCH) 

I tag locali non vengono automaticamente pushati. 

autore. Sono ideali per release uﬀiciali. Esempio: 

per chiarezza. v2.1.3 indica versione major 2, minor 

Usa "Push" e seleziona "Push all tags" per 

v1.0.0 con note di rilascio.

1, patch 3. Facilita la comunicazione nel team.

condividerli con il team sul repository remoto.

Best practice: Crea tag per ogni release in produzione. Facilita il rollback in caso di problemi e permette di ricostruire esattamente lo stato del codice 

in un momento specifico. I tag sono immutabili e aﬀidabili.

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

Cherry-Pick: Selezionare i Commit Perfetti

Il cherry-pick è una delle funzionalità più potenti di Git: permette 

Come Fare Cherry-Pick in SourceTree

di copiare commit specifici da un branch all'altro senza dover fare 

un merge completo. È come scegliere le ciliegie migliori da un 

albero!

Quando utilizzarlo:
•

Correggere bug urgenti su production

•

•

•

Portare feature specifiche tra branch

Recuperare commit da branch eliminati

Applicare hotfix selettivi

1.

2.

3.

4.

Seleziona il branch di destinazione

Trova il commit da copiare nella cronologia

Click destro sul commit → Cherry-Pick

SourceTree applica le modifiche automaticamente

Nota: Potrebbero verificarsi conflitti se le modifiche toccano le stesse righe di 

codice.

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

Diff Graﬁco: Analizzare le Modiﬁche Visivamente

SourceTree oﬀre uno strumento di diﬀ grafico potentissimo che rende la revisione del codice intuitiva e veloce. Ogni modifica viene evidenziata con colori 

diversi, permettendo di capire immediatamente cosa è cambiato tra versioni diverse del codice.

1

2

3

Aprire il Diff

Seleziona un commit nella cronologia e clicca su "File Status" nel pannello inferiore

Navigare le Modiﬁche

Doppio click su un file modificato apre la vista diﬀ side-by-side con evidenziazione delle righe cambiate

Confrontare Branch

Usa la funzione "Compare" per vedere tutte le diﬀerenze tra due branch prima di un merge

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

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
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

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
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

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
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

Esercizio in Coppia — Workﬂow Collaborativo Completo

FASE 4 — Risoluzione del Conflitto — Studente A esegue, B osserva e consiglia

1. Studente A fa Push del proprio commit su main
2. Studente B: checkout su main → Pull → torna su feature/sezione-contatti → click destro su main → Merge 

into current branch → appare il conflitto!
3.
In SourceTree, sito.txt mostra l'icona nella sezione Uncommitted changes
4. Aprite sito.txt con l'editor: vedrete i marcatori <<<<<<<, =======, >>>>>>>
5. Decidete insieme il titolo definitivo → rimuovete tutti i marcatori → salvate
6. Stage del file → commit con messaggio merge: resolve conflict on titolo, integrate sezione 

contatti → Push del branch

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

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
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

Esercizio in Coppia — Workﬂow Collaborativo Completo

FASE 6 — Merge Finale, Tag e Pulizia — Insieme

1. Checkout main → Pull → click destro su feature/sezione-contatti → Merge into current branch
2. Merge di hotfix/typo-autore su main nello stesso modo → Push
3. Pulsante Tag → nome: v1.0 → messaggio: Prima release completa → Push all tags
4. Cancellate tutti i branch feature e hotfix (click destro → Delete)
5. Entrambi fanno Pull su main e verificano che la cronologia sia identica su entrambe le macchine

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

Riepilogo: Le Operazioni Fondamentali

Facciamo un recap completo di tutto quello che abbiamo imparato in questo corso. Queste sono le competenze che userai quotidianamente nel tuo 

lavoro di sviluppo.

Branching

Commit

Merge

Push/Pull

Creare, cambiare e gestire 

Salvare snapshot del codice 

Integrare modifiche da branch 

Sincronizzare il lavoro locale 

branch per lavorare su feature 

con messaggi chiari e 

diversi, risolvendo eventuali 

con il repository remoto del 

isolate

descrittivi

conflitti

team

Cherry-Pick

Revert/Reset

Selezionare commit specifici da applicare ad altri branch

Annullare modifiche in modo sicuro o riscrivere la cronologia locale

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

BEST PRACTICES

Combinare Terminale e GUI: Il Meglio di Due Mondi

Non devi scegliere tra GUI e terminale: i professionisti usano entrambi strategicamente! Ogni strumento ha i suoi punti di forza e sapere quando usare 

l'uno o l'altro ti renderà molto più eﬀiciente.

Quando Usare SourceTree (GUI)

Quando Usare il Terminale

Visualizzare la cronologia: vedere il grafico dei branch è molto più 

Operazioni ripetitive: script e alias accelerano il lavoro

chiaro

Comandi veloci: git status o git pull sono più rapidi da terminale

Gestire conflitti di merge: l'interfaccia grafica semplifica la risoluzione

Automazione: integrare Git in pipeline CI/CD

Cherry-pick e operazioni complesse: meno errori con l'interfaccia 

Operazioni avanzate: alcuni comandi Git non hanno equivalente GUI

visuale

Troubleshooting: messaggi di errore più dettagliati

Revieware modifiche: il diﬀ side-by-side è imbattibile

Gestire staging selettivo: scegliere singole righe da committare

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

Consigli Pratici per il Successo

Commit Atomici e 

Messaggi Chiari

Ogni commit dovrebbe 

rappresentare una singola 

modifica logica. Scrivi messaggi 

descrittivi che spiegano il 

"perché", non solo il "cosa". Usa il 

tempo presente imperativo: "Add 

feature" non "Added feature".

Pull Frequente, Push 

Strategia di Branching 

Test Prima di Pushare

Regolare

Coerente

Fai pull almeno una volta al 

giorno per rimanere 

sincronizzato con il team. 

Pusha il tuo lavoro 

frequentemente per evitare di 

perdere modifiche e 

permettere ai colleghi di 

vedere i tuoi progressi.

Adotta una convenzione per i 

nomi dei branch (es: 

feature/, bugfix/, 

hotfix/) e rispettala. 

Cancella i branch dopo il 

merge per mantenere il 

repository pulito e 

organizzato.

Verifica sempre che il codice 

compili e i test passino prima 

di fare push. Un commit 

rotto sul branch condiviso 

blocca tutto il team. Usa git 

stash per salvare 

temporaneamente 

modifiche incomplete.

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

Congratulazioni! Siete Pronti per il Mondo Reale

Avete completato il vostro percorso formativo su SourceTree e Git! Ora possedete tutte le competenze necessarie per collaborare eﬀicacemente in 

progetti reali, gestire branch complessi e risolvere conflitti con sicurezza.

Continua a Praticare

Risorse Utili

Prossimi Passi

La vera padronanza arriva con l'esperienza 

Consulta la documentazione uﬀiciale di Git 

Esplora Git Flow, rebasing avanzato e hook 

quotidiana. Sperimenta con repository di 

e SourceTree quando hai dubbi. La 

personalizzati per portare le tue skill al 

test e non aver paura di sbagliare.

community è sempre pronta ad aiutare.

livello successivo.

Ricorda: Git è uno strumento potente che diventa sempre più intuitivo con l'uso. Buon coding e buon versionamento!

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it

GRAZIE A TUTTI…..

Via Schiaparelli 14 - 10148 Torino
https://www.tc-web.it
Mail: franco.grivet@tc-web.it

© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it