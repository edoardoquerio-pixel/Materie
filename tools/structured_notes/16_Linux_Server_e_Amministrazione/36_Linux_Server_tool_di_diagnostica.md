# Linux Server tool di diagnostica

## Panoramica
Il comando uptime fornisce in una sola riga le informazioni essenziali sullo stato del

## Argomenti trattati
Linux, Git, API REST, Reti, Data Analytics

---
## Appunti

Wolfgang Cecchin
UNITA’ FORMATIVA
Tool di diagnostica
Il comando uptime fornisce in una sola riga le informazioni essenziali sullo stato del
da quanto tempo il sistema e' acceso
quanti utenti sono collegati
il load average degli ultimi 1, 5 e 15 minuti
10:32:04 up 14 days, 3:21, 2 users, load average: 0.12, 0.08, 0.05
Lettura campo per campo:
10:32:04 — ora corrente del sistema
up 14 days, 3:21 — il sistema e' acceso da 14 giorni, 3 ore e 21 minuti. Il formato e' giorni,
2 users — numero di sessioni utente aperte (terminali, SSH...)
load average: 0.12, 0.08, 0.05 — carico medio nell'ultimo 1 minuto, 5 minuti e 15 minuti
Il load average
Indica quanti processi sono in attesa di essere eseguiti dalla CPU, mediato nel
I tre valori rappresentano rispettivamente la media dell'ultimo 1 minuto, 5 minuti e
Il valore di riferimento e' il numero di core della CPU:
load average < numero di core — il sistema e' a riposo, c'e' capacita' libera
load average = 1.0 su 1 core — CPU al 100%, situazione limite ma non critica
load average > numero di core — ci sono processi che aspettano la CPU: il sistema e'
I tre valori vanno letti insieme: un picco solo nel primo (1 min) e' passeggero; se
anche il terzo (15 min) e' alto, il problema e' strutturale.
Esempio: load average 0.12, 0.08, 0.05 su un sistema a 4 core — tutto tranquillo.
Esempio: load average 7.50, 6.20, 4.10 su un sistema a 4 core — il sistema e' sotto
Quanti core ha il mio sistema?
$ lscpu | grep 'CPU(s)'
Analisi della memoria RAM: free
Il comando free mostra la memoria totale, usata, libera e la quota di swap.
L'opzione -h presenta i valori in formato leggibile, scegliendo automaticamente
l'unita' piu' adatta.
total used free shared buff/cache available
Mem: 15Gi 3,2Gi 9,1Gi 283Mi 3,0Gi 11Gi
Swap: 2,0Gi 0B 2,0Gi
Cosa significa buff/cache?
Linux usa la RAM libera come cache disco per migliorare le prestazioni.
La colonna available e' quella che conta davvero: indica quanta memoria puo'
essere usata da nuovi processi.
Messaggi del kernel: dmesg
dmesg mostra i messaggi del kernel dal momento del boot.
E' il primo strumento da consultare in caso di problemi hardware.
Rilevamento e inizializzazione dei dispositivi hardware
Errori di driver
Problemi con dischi e filesystem
Messaggi di errore della rete
$ dmesg | tail -50
$ dmesg | grep -i error
$ dmesg | grep -iE "error|fail|warn|critical"
$ dmesg | grep -i sda
$ dmesg | grep -i nvme
L'opzione -T mostra i timestamp in formato leggibile:
$ dmesg -T | grep -i error
Le parole chiave piu' importanti da cercare:
error, fail — errori generici di dispositivi o driver
I/O error, timeout — il disco non risponde o e' lento
EXT4-fs error — filesystem corrotto
Out of memory — il sistema ha esaurito la RAM
Hardware Error — errore segnalato direttamente dall'hardware
Regola pratica: un messaggio che appare una volta puo' essere normale. Se si
ripete molte volte, c'e' un problema reale.
Log di sistema: journalctl
journalctl e' il tool per consultare il journal di systemd.
Raccoglie in modo centralizzato i log di tutti i servizi e del kernel.
journalctl -b -1
Ultimi log con contesto esteso (errori recenti)
Log del boot corrente
Log del boot precedente
journalctl -b -2
journalctl -u ssh
journalctl -p err
Due boot fa (utile dopo un crash)
Log di un servizio specifico
Segue i log in tempo reale (come tail -f)
Solo messaggi di errore
journalctl -p warning
Messaggi di warning e superiori
journalctl --since '1 hour ago'
Ultimi 60 minuti
journalctl --since 'today'
# journalctl -b -1 -p err
Cosa cercare in journalctl:

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_Linux_Server_tool_di_diagnostica.md*
