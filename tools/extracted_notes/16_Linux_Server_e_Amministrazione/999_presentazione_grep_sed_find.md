# presentazione grep sed find

Fonte: `presentazione grep sed find.pdf`

ITS ICT — Linux Server

grep, sed, find

Ricerca e manipolazione di file e testo in Linux

$ grep -rn "error"

/var/log/ 2>/dev/null

$ sed -i 's/old/new/g'

server.conf

$ find / -perm /4000 \
-type f 2>/dev/null

$ find /etc -name '*.conf'
| xargs grep '127.0.0.1'

grep
Cerca nei file

sed
Modifica il testo

find
Cerca nel filesystem

In questa lezione

grep

sed

find

•

•

•

•

Cerca righe che contengono un 
pattern

Opzioni: -i -r -n -v -l -c -E

Ancore: ^ $ e regex estese

Non modifica mai i file

•

•

•

•

Modifica il testo riga per riga

Comando s/vecchio/nuovo/g

Eliminare righe con /pattern/d

Modifica in-place con -i

•

•

•

•

Cerca per nome, tipo, proprietario

Filtra per dimensione e data

Permessi: tre formati di -perm

Esegue azioni con -exec

grep — Cercare nei file

Sintassi

Ancore nelle espressioni regolari

$ grep [opzioni] "pattern" file

Non modifica mai i file — solo cerca e mostra.

Opzioni principali

-i

-r

-n

-v

-l

-c

-E

-o

Case-insensitive (MAIUSCOLE = minuscole)

Ricorsiva nelle sottodirectory

Mostra il numero di riga

Inverte: righe che NON corrispondono

Solo nomi file con corrispondenze

Conta le righe corrispondenti

Abilita regex estese (ERE)

Stampa solo la parte corrispondente

^

$

.

|

Riga che inizia con root

grep "^root"

Riga che finisce con bash

grep "bash$"

Qualsiasi carattere singolo

grep "er.ore"

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

Sintassi

$ sed [opzioni] 'comando' file

Il comando di sostituzione s/vecchio/nuovo/flag

$ sed 's/vecchio/nuovo/flag' file

(nessuno)

g

i

2

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

Tutte le occorrenze nella riga (flag g)

Mostrare solo le righe 1-10

$ sed 's/server01/webserver.lan/g' sistema.log > 
mod.log

$ sed -n '1,10p' sistema.log

Eliminare le righe di commento dall'output

Modifica in-place con backup

$ sed '/^#/d' webserver.conf

$ sed -i.bak 's/vecchio/nuovo/g' file.txt

Workflow consigliato: grep → sed

$ grep "old" file # 1. verifico cosa troverò
$ sed 's/old/new/' file # 2. controllo l'output senza -i
$ sed -i 's/old/new/' file # 3. applico la modifica

find — Cercare nel filesystem

Sintassi

$ find [percorso] [criteri] [azione]

-name "*.conf"

-iname "hosts"

-type f / d / l

Nome (glob, case-sensitive)

Nome case-insensitive

File, directory, link simbolico

-user mario

-size +100M

-mtime -1

Proprietario dell'utente

Dimensione > 100 MiB

Modificato nelle ultime 24 h

Esempi

$ find / -name "hosts" 2>/dev/null
$ find /var/log -type f -name "*.log"
$ find /home -type d -name "backup"
$ find /etc -mtime -1

find — Permessi: i tre formati di -perm

-perm NNNN

find . -perm 755

-perm -NNNN

find . -perm -111

-perm /NNNN

find . -perm /4000

Corrispondenza esatta

Il file deve avere esattamente quei permessi e nessun altro. Raramente usato in pratica.

Tutti i bit presenti

Tutti i bit indicati devono essere attivi, ma il file può averne anche altri.

Almeno un bit presente

Basta che sia attivo almeno uno dei bit indicati (OR logico). Il più usato per i permessi speciali.

Il formato /NNNN è quello più usato per cercare permessi speciali (SUID, SGID, Sticky bit).

find — Permessi speciali: SUID, SGID, Sticky bit

SUID

4000

Il file eseguibile viene eseguito con i permessi del proprietario (es. passwd → root).

SGID

2000

Su file: esegue con i permessi del gruppo. Su directory: i file creati ereditano il gruppo.

Sticky

1000

Su directory (es. /tmp): solo il proprietario può eliminare i propri file.

Esempi pratici

File con SUID (eseguiti come root)

Qualsiasi permesso speciale attivo

$ find / -perm /4000 -type f 2>/dev/null

$ find / -perm /7000 2>/dev/null

File con SGID

Eseguibili da tutti (user + group + others)

$ find / -perm /2000 -type f 2>/dev/null

$ find . -perm -111

Directory con sticky bit

Scrivibili da others (rischio sicurezza)

$ find / -type d -perm /1000 2>/dev/null

$ find /home -perm -002 -type f

find — Azioni: -exec, xargs e 2>/dev/null

-exec — eseguire un comando su ogni file trovato

$ find [percorso] [criteri] -exec comando {} \;

{}

Segnaposto sostituito dal percorso di ogni file trovato

\;

Termina -exec. Il \ impedisce alla shell di interpretare il ;

Copiare i file di mario in /root/backup_mario/

$ find / -user mario -type f -exec cp {} /root/backup_mario/ \;

Listare i file SUID con dettagli

$ find / -perm /4000 -type f -exec ls -lh {} \; 2>/dev/null

Pipeline con xargs — alternativa più efficiente

$ find /etc/ -name '*' -type f | xargs grep "127.0.0.1"
$ find /etc/ -type f -print0 | xargs -0 grep "pattern" # nomi con spazi

2>/dev/null scarta i messaggi "Permission denied" (stderr). Da aggiungere sempre con find / o su directory di sistema.

Riepilogo — Cheat Sheet

grep

sed

find

grep "pat" file → cerca pat nel file
grep -i "pat" file → case-insensitive
grep -r "pat" dir/ → ricorsivo
grep -v "pat" file → righe che NON corrispondono
grep -E "err|warn" file → OR logico
grep -c "pat" file → conta le righe

sed 's/old/new/' file → sostituzione (prima occ.)
sed 's/old/new/g' file → sostituzione (tutte)
sed -i 's/old/new/g' file → modifica in-place
sed '/^#/d' file → elimina commenti
sed '/^$/d' file → elimina righe vuote
sed -n '1,10p' file → mostra righe 1-10

find / -name "file" 2>/dev/null → cerca per nome
find / -type f -size +100M → file > 100 MiB
find / -user mario -type f → file di mario
find / -perm /4000 -type f → file con SUID
find / -perm /7000 2>/dev/null → tutti i perm. speciali
find /etc -exec grep -l "pat" {} \; → -exec

Esercizi

grep

sed

find

•

•

•

•

•

Mostrare le righe di sistema.log che 
contengono ERROR

Cercare ERROR o WARNING con -E

Contare i "Failed password" nel log

Mostrare gli utenti con shell /bin/bash da 
utenti.txt

Righe non vuote e non commentate da 
webserver.conf

•

•

•

Sostituire WARNING con ERROR solo a 
video

Eliminare le righe di commento 
dall'output

Sostituire server01 con webserver.lan → 
sistema_mod.log

•

•

•

•

Cercare resolv.conf nel filesystem (con 
2>/dev/null)

Trovare file SUID nel sistema

Copiare i file di mario in 
/root/backup_mario/

Trovare file > 100 MiB nel filesystem