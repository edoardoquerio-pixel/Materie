# presentazione grep sed find

**File:** `presentazione grep sed find.pdf`
**Tipo:** `.pdf`
**Dimensione:** 425.2 KB
**Ultima modifica:** 02/07/2026 09:27

---

$ grep -rn "error"
/var/log/ 2>/dev/null
$ sed -i 's/old/new/g'
server.conf
$ find / -perm /4000 \
-type f 2>/dev/null
$ find /etc -name '*.conf'
| xargs grep '127.0.0.1'
ITS ICT — Linux Server
grep, sed, find
Ricerca e manipolazione di file e testo in Linux
grep
Cerca nei file
sed
Modifica il testo
find
Cerca nel filesystem

In questa lezione
grep
• Cerca righe che contengono un 
pattern
• Opzioni: -i -r -n -v -l -c -E
• Ancore: ^ $ e regex estese
• Non modifica mai i file
sed
• Modifica il testo riga per riga
• Comando s/vecchio/nuovo/g
• Eliminare righe con /pattern/d
• Modifica in-place con -i
find
• Cerca per nome, tipo, proprietario
• Filtra per dimensione e data
• Permessi: tre formati di -perm
• Esegue azioni con -exec

grep — Cercare nei file
Sintassi
$ grep [opzioni] "pattern" file
Non modifica mai i file — solo cerca e mostra.
Opzioni principali
-i Case-insensitive (MAIUSCOLE = minuscole)
-r Ricorsiva nelle sottodirectory
-n Mostra il numero di riga
-v Inverte: righe che NON corrispondono
-l Solo nomi file con corrispondenze
-c Conta le righe corrispondenti
-E Abilita regex estese (ERE)
-o Stampa solo la parte corrispondente
Ancore nelle espressioni regolari
^
Riga che inizia con root
grep "^root"
$
Riga che finisce con bash
grep "bash$"
.
Qualsiasi carattere singolo
grep "er.ore"
|
OR logico (richiede -E)
grep -E "err|warn"

grep — Esempi pratici
Trova ERROR nel log
$ grep "ERROR" sistema.log
Cerca ERROR o WARNING (OR)
$ grep -E "ERROR|WARNING" sistema.log
Con numero di riga, case-insensitive
$ grep -ni "error" sistema.log
Righe che NON sono commenti
$ grep -v "^#" webserver.conf
Righe non vuote e non commentate
$ grep -v "^#" webserver.conf | grep -v "^$"
Conta i login falliti
$ grep -c "Failed password" sistema.log
File che contengono password (ricorsivo)
$ grep -rl "password" /etc/
Estrai tutti gli IP dal log
$ grep -oE "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" sistema.log

sed — Modificare il testo
Sintassi
$ sed [opzioni] 'comando' file
Il comando di sostituzione  s/vecchio/nuovo/flag
$ sed 's/vecchio/nuovo/flag' file
(nessuno)
Sostituisce la prima occorrenza per riga
g
Tutte le occorrenze nella riga (global)
i
Case-insensitive
2
Solo la seconda occorrenza
Opzione  -i  (in-place)
Senza  -i  → output su stdout, file intatto
$ sed 's/old/new/' file.txt
Con  -i  → modifica diretta del file
$ sed -i 's/old/new/g' file.txt
ATTENZIONE: -i  modifica il file in modo irreversibile. Prima di usarla, verificare il risultato senza  -i.  Per creare una copia di backup automatica: sed -
i.bak 's/old/new/g' file

sed — Esempi pratici e workflow consigliato
Sostituire WARNING con ERROR (solo output)
$ sed 's/WARNING/ERROR/' webserver.conf
Tutte le occorrenze nella riga (flag g)
$ sed 's/server01/webserver.lan/g' sistema.log > 
mod.log
Eliminare le righe di commento dall'output
$ sed '/^#/d' webserver.conf
Eliminare le righe vuote
$ sed '/^$/d' file.txt
Mostrare solo le righe 1-10
$ sed -n '1,10p' sistema.log
Modifica in-place con backup
$ sed -i.bak 's/vecchio/nuovo/g' file.txt
Workflow consigliato: grep → sed
$ grep "old" file          # 1. verifico cosa troverò
$ sed 's/old/new/' file   # 2. controllo l'output senza -i
$ sed -i 's/old/new/' file # 3. applico la modifica

find — Cercare nel filesystem
Sintassi
$ find [percorso] [criteri] [azione]
-name "*.conf"
Nome (glob, case-sensitive)
-iname "hosts"
Nome case-insensitive
-type f / d / l
File, directory, link simbolico
-user mario
Proprietario dell'utente
-size +100M
Dimensione > 100 MiB
-mtime -1
Modificato nelle ultime 24 h
Esempi
$ find / -name "hosts" 2>/dev/null
$ find /var/log -type f -name "*.log"
$ find /home -type d -name "backup"
$ find /etc -mtime -1

find — Permessi: i tre formati di -perm
-perm NNNN
find . -perm 755
Corrispondenza esatta
Il file deve avere esattamente quei permessi e nessun altro. Raramente usato in pratica.
-perm -NNNN
find . -perm -111
Tutti i bit presenti
Tutti i bit indicati devono essere attivi, ma il file può averne anche altri.
-perm /NNNN
find . -perm /4000
Almeno un bit presente
Basta che sia attivo almeno uno dei bit indicati (OR logico). Il più usato per i permessi speciali.
Il formato  /NNNN  è quello più usato per cercare permessi speciali (SUID, SGID, Sticky bit).

find — Permessi speciali: SUID, SGID, Sticky bit
SUID 4000 Il file eseguibile viene eseguito con i permessi del proprietario (es. passwd → root).
SGID 2000 Su file: esegue con i permessi del gruppo. Su directory: i file creati ereditano il gruppo.
Sticky 1000 Su directory (es. /tmp): solo il proprietario può eliminare i propri file.
Esempi pratici
File con SUID (eseguiti come root)
$ find / -perm /4000 -type f 2>/dev/null
File con SGID
$ find / -perm /2000 -type f 2>/dev/null
Directory con sticky bit
$ find / -type d -perm /1000 2>/dev/null
Qualsiasi permesso speciale attivo
$ find / -perm /7000 2>/dev/null
Eseguibili da tutti (user + group + others)
$ find . -perm -111
Scrivibili da others (rischio sicurezza)
$ find /home -perm -002 -type f

find — Azioni: -exec, xargs e 2>/dev/null
-exec — eseguire un comando su ogni file trovato
$ find [percorso] [criteri] -exec comando {} \;
{} Segnaposto sostituito dal percorso di ogni file trovato \; Termina -exec. Il \ impedisce alla shell di interpretare il ;
Copiare i file di mario in /root/backup_mario/
$ find / -user mario -type f -exec cp {} /root/backup_mario/ \;
Listare i file SUID con dettagli
$ find / -perm /4000 -type f -exec ls -lh {} \; 2>/dev/null
Pipeline con xargs — alternativa più efficiente
$ find /etc/ -name '*' -type f | xargs grep "127.0.0.1"
$ find /etc/ -type f -print0 | xargs -0 grep "pattern"  # nomi con spazi
2>/dev/null  scarta i messaggi "Permission denied" (stderr). Da aggiungere sempre con find / o su directory di sistema.

Riepilogo — Cheat Sheet
grep
grep "pat" file               → cerca pat nel file
grep -i "pat" file            → case-insensitive
grep -r "pat" dir/            → ricorsivo
grep -v "pat" file            → righe che NON corrispondono
grep -E "err|warn" file       → OR logico
grep -c "pat" file            → conta le righe
sed
sed 's/old/new/' file         → sostituzione (prima occ.)
sed 's/old/new/g' file        → sostituzione (tutte)
sed -i 's/old/new/g' file     → modifica in-place
sed '/^#/d' file              → elimina commenti
sed '/^$/d' file              → elimina righe vuote
sed -n '1,10p' file           → mostra righe 1-10
find
find / -name "file" 2>/dev/null   → cerca per nome
find / -type f -size +100M         → file > 100 MiB
find / -user mario -type f         → file di mario
find / -perm /4000 -type f         → file con SUID
find / -perm /7000 2>/dev/null     → tutti i perm. speciali
find /etc -exec grep -l "pat" {} \; → -exec

Esercizi
grep
• Mostrare le righe di sistema.log che 
contengono ERROR
• Cercare ERROR o WARNING con -E
• Contare i "Failed password" nel log
• Mostrare gli utenti con shell /bin/bash da 
utenti.txt
• Righe non vuote e non commentate da 
webserver.conf
sed
• Sostituire WARNING con ERROR solo a 
video
• Eliminare le righe di commento 
dall'output
• Sostituire server01 con webserver.lan → 
sistema_mod.log
find
• Cercare resolv.conf nel filesystem (con 
2>/dev/null)
• Trovare file SUID nel sistema
• Copiare i file di mario in 
/root/backup_mario/
• Trovare file > 100 MiB nel filesystem
