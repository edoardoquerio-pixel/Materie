# lezione grep sed awk

## Panoramica
DOCENTE: _______________________________

## Argomenti trattati
Linux, Configurazione, Sicurezza, Data Analytics

---
## Appunti

DOCENTE: _______________________________
UNITÀ FORMATIVA: Strumenti Linux per la gestione dei file
ARGOMENTO: Ricerca nei file: grep, sed, awk
Linux mette a disposizione tre strumenti fondamentali per cercare e manipolare il testo nei file:
• grep — cerca righe che contengono un pattern
sed — trasforma il testo (cerca e sostituisce)
• awk — elabora testo strutturato a colonne
I file di esempio utilizzati in questa lezione si trovano nella cartella ~/esercizi/.
1. grep — Cercare nei file
Il comando grep (Global Regular Expression Print) cerca le righe di un file che corrispondono a un
pattern e le stampa sullo standard output. Non modifica mai i file.
$ grep [opzioni] "pattern" file
Opzioni principali
Ricerca case-insensitive (maiuscole = minuscole)
Ricerca ricorsiva in tutte le sottodirectory
Mostra il numero di riga prima di ogni risultato
Inverte la ricerca: mostra le righe che NON corrispondono
Mostra solo i nomi dei file con almeno una corrispondenza
Conta il numero di righe corrispondenti
Abilita le espressioni regolari estese (ERE)
Cerca solo parole intere (word match)
Ricerca semplice
$ grep "ERROR" sistema.log
Cerca tutte le righe che contengono la parola ERROR nel file sistema.log.
Ricerca case-insensitive con numero di riga
$ grep -n -i "error" sistema.log
Trova sia ERROR sia error sia Error, mostrando il numero di riga per ogni risultato.
Ricerca invertita
$ grep -v "^#" webserver.conf
Mostra tutte le righe del file di configurazione che non iniziano con # (cioè esclude i commenti).
Ricerca ricorsiva
$ grep -rl "password" /etc/
Cerca la parola password in tutti i file dentro /etc/ e mostra solo i nomi dei file trovati.
Uso di espressioni regolari
$ grep -E "ERROR|WARNING" sistema.log
Cerca le righe che contengono ERROR oppure WARNING (operatore | = OR).
NOTA: grep non modifica mai i file. Serve solo per trovare e visualizzare righe. Per
modificare il testo si usa sed.
Ancore nelle espressioni regolari
grep "^root" utenti.txt
Righe che iniziano con "root"
grep "bash$" utenti.txt
Righe che terminano con "bash"
grep "er.ore" file.txt
Il punto sostituisce un qualsiasi carattere
2. sed — Modificare il testo
Il comando sed (Stream EDitor) legge un file riga per riga, applica una trasformazione e stampa il
risultato. Di default non modifica il file originale: l'output va sullo standard output. Con l'opzione -i
la modifica avviene direttamente sul file.
$ sed [opzioni] 'comando' file
Il comando di sostituzione: s///
Il comando più usato di sed è s (substitute):
$ sed 's/testo_vecchio/testo_nuovo/flag' file
Sostituisce solo la prima occorrenza per ogni riga
Sostituisce tutte le occorrenze nella riga (global)
Sostituzione case-insensitive
Sostituisce solo la seconda occorrenza
Sostituzione semplice (output su terminale)
$ sed 's/WARNING/ATTENZIONE/' sistema.log
Mostra il file con WARNING sostituito da ATTENZIONE nella prima occorrenza di ogni riga. Il file originale
non viene modificato.
Sostituzione con modifica in-place
$ sed -i 's/porta = 80/porta = 8080/' webserver.conf
Modifica direttamente il file webserver.conf, cambiando il valore della porta.
ATTENZIONE: L'opzione -i modifica il file in modo irreversibile. Prima di usarla, verificare il
risultato senza -i per accertarsi che la sostituzione sia corretta.
Copia di sicurezza automatica con -i
$ sed -i.bak 's/WARNING/ATTENZIONE/g' sistema.log
Crea automaticamente una copia di backup sistema.log.bak prima di modificare il file.
Eliminare righe che corrispondono a un pattern
$ sed '/^#/d' webserver.conf
Il comando d (delete) elimina le righe che corrispondono al pattern. In questo caso elimina tutti i
commenti dall'output.
Visualizzare solo un intervallo di righe
$ sed -n '1,5p' sistema.log
Con -n (no print) e il comando p mostra solo le righe dalla 1 alla 5.
Workflow consigliato: grep + sed
Passo 1 — verificare cosa verrà modificato con grep:
$ grep "livello = WARNING" webserver.conf
Passo 2 — eseguire la sostituzione con sed (senza -i prima):

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_lezione_grep_sed_awk.md*
