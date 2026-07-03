# Lezione 1

## Panoramica
Lezione 1 – Corso di Version Control con Git

## Argomenti trattati
Git, Data Analytics, Database, Reti, Linux

---
## Appunti

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
*Fonte: 001_Lezione_1_-_Fondamenti_di_Version_Control.md*
