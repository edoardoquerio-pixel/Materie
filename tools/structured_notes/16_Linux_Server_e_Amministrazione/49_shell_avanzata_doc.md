# shell avanzata doc

## Panoramica
Reindirizzamento, processi e operatori

## Argomenti trattati
Linux, Reti, API REST, Configurazione, Database

---
## Appunti

Wolfgang Cecchin
Reindirizzamento, processi e operatori
1. File descriptor e reindirizzamento
Cos'è un file descriptor
In Linux, tutto è un file: file di testo, directory, dispositivi hardware, socket di rete, la tastiera,
lo schermo. Il kernel gestisce tutto tramite la stessa astrazione.
Quando un processo vuole comunicare con qualcosa — leggere dalla tastiera, scrivere sullo
schermo, aprire un file — non lo fa direttamente. Chiede al kernel di aprire un canale, e il
kernel gli restituisce un numero intero che rappresenta quel canale. Quel numero è il file
descriptor (fd).
Puoi immaginarlo come il numero di un tavolo al ristorante: il cameriere (kernel) sa a quale
tavolo portare il cibo, tu (il processo) usi solo il numero — non ti preoccupi di dove si trova
fisicamente il tavolo.
processo → "voglio scrivere sul canale 1" → kernel → schermo
processo → "voglio scrivere sul canale 1" → kernel → file.txt ← dopo
reindirizzamento
Il processo scrive sempre sullo stesso numero. È il kernel che decide dove quel numero
I tre canali aperti automaticamente
Ogni processo, nel momento in cui viene avviato, riceve già tre file descriptor aperti, ereditati
Collegato a (default)
stdout e stderr puntano entrambi al terminale, ma sono canali separati. Questo è
fondamentale: permette di mandare l'output normale da una parte e gli errori da un'altra,
senza mescolarli.
Perché si chiama "descriptor" e non "file"
Il file descriptor non è il file — è solo un indice nella tabella dei file aperti del processo. Ogni
processo ha la propria tabella. Modificare dove punta l'fd 1 di un processo non cambia nulla
per gli altri processi.
Il reindirizzamento (>, 2>, &>) non fa altro che cambiare la destinazione di questi indici prima
che il processo parta. Il processo non sa nulla di questo: continua a scrivere su 1 e 2 come
Reindirizzamento di stdout (1)
# Salva l'elenco dei file di configurazione su file
ls -l /etc > elenco.txt
# Aggiunge in coda invece di sovrascrivere
ls -l /var/www >> elenco.txt
# Equivalente esplicito con fd 1
ls -l /etc 1> elenco.txt
# Caso pratico: salvare il risultato di una query MySQL su file
mysql -u root -p fotodb -e "SELECT * FROM clienti;" > clienti.txt
Reindirizzamento di stderr (2)
# find genera errori su directory senza permessi — li separiamo
find / -name "*.conf" > risultati.txt 2> errori.log
# Cerca file PHP ignorando silenziosamente le directory protette
find /var/www -name "*.php" 2> /dev/null
# grep: solo i match su stdout, eventuali errori su file separato
grep -r "password" /etc 2> /tmp/grep_errori.log
Reindirizzare entrambi con 2>&1
La sintassi si legge pezzo per pezzo:
│ │ │└─ il numero del file descriptor 1 (stdout)
│ │ └── & significa "questo è un fd, non un nome file"
│ └───── operatore di reindirizzamento
└──────── il file descriptor 2 (stderr)
Traduzione letterale: "punta fd 2 verso lo stesso posto dove punta fd 1".
Il & davanti all'1 è necessario per disambiguare: senza, 2>1 significherebbe "scrivi stderr su
un file chiamato letteralmente 1".
Perché l'ordine conta
La shell legge il reindirizzamento da sinistra a destra. 2>&1 significa "copia la destinazione
attuale di fd 1" — non "tieni fd 2 sempre sincronizzato con fd 1".
# CORRETTO: prima sposta stdout su file, poi aggancia stderr a stdout
find / -name "*.conf" > tutto.log 2>&1
# passo 1 — dopo > tutto.log: fd1 → tutto.log, fd2 → terminale
# passo 2 — dopo 2>&1: fd1 → tutto.log, fd2 → tutto.log ✓
# SBAGLIATO: 2>&1 viene letto prima, quando stdout punta ancora al terminale
find / -name "*.conf" 2>&1 > tutto.log
# passo 1 — dopo 2>&1: fd1 → terminale, fd2 → terminale ← copia fd1
# passo 2 — dopo > tutto.log: fd1 → tutto.log, fd2 → terminale ✗ stderr
rimane sul terminale
# Sintassi moderna equivalente (solo bash)
find / -name "*.conf" &> tutto.log
# Sintassi classica (funziona su sh, dash, bash — preferibile negli script)
find / -name "*.conf" > tutto.log 2>&1
# Backup MySQL: output e errori nello stesso log
mysqldump -u root -p fotodb > /var/log/backup.log 2>&1
# Aggiornamento pacchetti silenzioso, tutto su log
apt-get upgrade > /var/log/upgrade.log 2>&1
# Esecuzione silenziosa — scarta tutto
apt-get update &> /dev/null
Reindirizzamento di stdin (0)
# MySQL legge il dump da file invece che dalla tastiera
mysql -u root -p fotodb < dump.sql
# Invia il contenuto di un file come corpo di una mail

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_shell_avanzata_doc.md*
