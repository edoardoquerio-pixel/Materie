# presentazione grep sed find

## Panoramica
Ricerca e manipolazione di file e testo in Linux

## Argomenti trattati
Linux, Data Analytics, Sicurezza

---
## Appunti

ITS ICT — Linux Server
grep, sed, find
Ricerca e manipolazione di file e testo in Linux
$ grep -rn "error"
/var/log/ 2>/dev/null
$ sed -i 's/old/new/g'
$ find / -perm /4000 \
-type f 2>/dev/null
$ find /etc -name '*.conf'
| xargs grep '127.0.0.1'
Modifica il testo
Cerca nel filesystem
In questa lezione
Cerca righe che contengono un
Opzioni: -i -r -n -v -l -c -E
Ancore: ^ $ e regex estese
Non modifica mai i file
Modifica il testo riga per riga
Comando s/vecchio/nuovo/g
Eliminare righe con /pattern/d
Modifica in-place con -i
Cerca per nome, tipo, proprietario
Filtra per dimensione e data
Permessi: tre formati di -perm
Esegue azioni con -exec
grep — Cercare nei file
Ancore nelle espressioni regolari
$ grep [opzioni] "pattern" file
Non modifica mai i file — solo cerca e mostra.
Opzioni principali
Case-insensitive (MAIUSCOLE = minuscole)
Ricorsiva nelle sottodirectory
Mostra il numero di riga
Inverte: righe che NON corrispondono
Solo nomi file con corrispondenze
Conta le righe corrispondenti
Abilita regex estese (ERE)
Stampa solo la parte corrispondente
Riga che inizia con root
Riga che finisce con bash
Qualsiasi carattere singolo
OR logico (richiede -E)
grep -E "err|warn"
grep — Esempi pratici
Trova ERROR nel log
Righe non vuote e non commentate
$ grep "ERROR" sistema.log
$ grep -v "^#" webserver.conf | grep -v "^$"
Cerca ERROR o WARNING (OR)
Conta i login falliti
$ grep -E "ERROR|WARNING" sistema.log
$ grep -c "Failed password" sistema.log
Con numero di riga, case-insensitive
File che contengono password (ricorsivo)
$ grep -ni "error" sistema.log
$ grep -rl "password" /etc/
Righe che NON sono commenti
Estrai tutti gli IP dal log
$ grep -v "^#" webserver.conf
$ grep -oE "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" sistema.log
sed — Modificare il testo
$ sed [opzioni] 'comando' file
Il comando di sostituzione s/vecchio/nuovo/flag
$ sed 's/vecchio/nuovo/flag' file
Sostituisce la prima occorrenza per riga
Tutte le occorrenze nella riga (global)
Case-insensitive
Solo la seconda occorrenza
Opzione -i (in-place)
Senza -i → output su stdout, file intatto
Con -i → modifica diretta del file
$ sed 's/old/new/' file.txt
$ sed -i 's/old/new/g' file.txt
ATTENZIONE: -i modifica il file in modo irreversibile. Prima di usarla, verificare il risultato senza -i. Per creare una copia di backup automatica: sed -
i.bak 's/old/new/g' file
sed — Esempi pratici e workflow consigliato
Sostituire WARNING con ERROR (solo output)
Eliminare le righe vuote
$ sed 's/WARNING/ERROR/' webserver.conf
$ sed '/^$/d' file.txt

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_presentazione_grep_sed_find.md*
