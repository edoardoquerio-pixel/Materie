# shell avanzata

## Panoramica
Reindirizzamento, processi e operatori

## Argomenti trattati
Linux, Reti, API REST

---
## Appunti

Wolfgang Cecchin
UNITA’ FORMATIVA
Reindirizzamento, processi e operatori
ITS Academy — Linux Server
Cos'è un file descriptor
In Linux tutto è un file:
tastiera, schermo, rete, dispositivi
Un processo non comunica direttamente
Chiede al kernel di aprire un canale →
riceve un numero intero: il fd
Il reindirizzamento cambia dove
punta quel numero, non il processo
I tre file descriptor standard
stdout e stderr puntano entrambi al terminale, ma sono canali separati — questo permette di
separare output normale ed errori.
Reindirizzamento: stdout e stderr
# sovrascrive
ls -l /etc > elenco.txt
# aggiunge in coda
ls -l /var/www >> elenco.txt
# equivalente esplicito
ls -l /etc 1> elenco.txt
# separa errori dall'output
find / -name '*.conf' \
> risultati.txt 2> errori.log
# scarta gli errori
find /var/www -name '*.php' \
# grep: errori su file separato
grep -r 'password' /etc \
2> /tmp/errori.log
> sovrascrive >> aggiunge 2> stderr /dev/null cestino
Reindirizzare entrambi: 2>&1
"Punta fd 2 verso lo stesso posto dove punta fd 1"
Senza & davanti all'1: il comando 2>1 scriverebbe stderr su un file chiamato
letteralmente "1"
# Backup MySQL: tutto nello
mysqldump -u root -p fotodb \
> /var/log/backup.log 2>&1
# Scarta tutto (silenzioso)
apt-get update &> /dev/null
# &> equivale a > ... 2>&1
# ma funziona solo in bash
2>&1 — l'ordine conta
La shell legge il reindirizzamento da sinistra a destra.
find / -name '*.conf' > tutto.log 2>&1
find / -name '*.conf' 2>&1 > tutto.log
# passo 1 — > tutto.log:
# fd1 → tutto.log
# fd2 → terminale
# passo 2 — 2>&1:
# fd2 → tutto.log ✓
# passo 1 — 2>&1:
# fd2 → terminale ← copia fd1 ora!
# passo 2 — > tutto.log:
# fd1 → tutto.log
# fd2 → terminale ✗
Regola: prima sposta stdout con > poi aggancia stderr con 2>&1
Sintassi moderna (solo bash): find / -name '*.conf' &> tutto.log
stdin (fd 0) e /dev/null
stdin (fd 0) — leggere da file
/dev/null — il cestino
# MySQL legge da file
# invece che dalla tastiera
mysql -u root -p fotodb < dump.sql
# Invia file come corpo mail
mail -s 'Report' \
admin@studio.it \
< /var/log/backup.log
# Scarta solo stdout
apt-get update > /dev/null
# Scarta solo stderr
find / -name '*.conf' 2> /dev/null
# Scarta tutto
apt-get update &> /dev/null
Tutto quello che viene scritto in /dev/null scompare — nessun output, nessun errore visibile.
Operatori di controllo
Sempre in sequenza
Il secondo comando gira sempre,
indipendentemente dall'esito del primo.
apt-get update ; apt-get upgrade

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_shell_avanzata.md*
