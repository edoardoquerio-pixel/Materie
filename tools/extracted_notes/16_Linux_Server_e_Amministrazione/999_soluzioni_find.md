# soluzioni find

Fonte: `soluzioni find.pdf`

Soluzioni — find 

Ricerca base 

Es. 1 Cercare in tutto il filesystem un file di nome resolv.conf, sopprimendo gli errori. 

$ find / -name "resolv.conf" 2>/dev/null 

La ricerca parte dalla radice /. Il reindirizzamento 2>/dev/null scarta i messaggi "Permission 
denied" su stderr, lasciando l'output pulito. 

Es. 2 Trovare tutti i file con estensione .log nella directory /var/log. 

$ find /var/log -name "*.log" 

Il pattern *.log usa il glob * per qualsiasi prefisso. Le virgolette impediscono alla shell di 
espandere il glob prima di passarlo a find. 

Es. 3 Trovare tutte le directory che si chiamano backup a partire da /home. 

$ find /home -type d -name "backup" 

-type d limita la ricerca alle sole directory, escludendo file con lo stesso nome. 

Es. 4 Trovare i file di proprietà del tuo utente in /tmp. 

$ find /tmp -user $(whoami) 

La sostituzione di comando $(whoami) inserisce automaticamente il nome dell'utente corrente. 
In alternativa si può scrivere il nome esplicitamente: find /tmp -user mario. 

Ricerca per dimensione e data 

Es. 5 Trovare tutti i file regolari di dimensione superiore a 100 MiB nel filesystem. 

$ find / -type f -size +100M 2>/dev/null 

-type f esclude directory e link. +100M significa strettamente maggiore di 100 MiB. 2>/dev/null 
sopprime gli errori di accesso negato. 

Es. 6 Trovare i file in /etc modificati nelle ultime 24 ore. 

$ find /etc -mtime -1 

Il valore -1 con -mtime significa «modificati da meno di 1 giorno», ovvero nelle ultime 24 ore. Per 
ricerche più precise al minuto si può usare -mmin -60 (ultima ora). 

Permessi 

Es. 7 Trovare tutti i file nel sistema con il bit SUID attivo. 
$ find / -type f -perm /4000 2>/dev/null 

Il formato /4000 (slash) significa «almeno uno dei bit indicati è presente»: qui il bit SUID (4000). -
type f esclude le directory. 2>/dev/null rimuove i messaggi di accesso negato. 

⚠️ Sicurezza: I file SUID di proprietà di root vengono eseguiti con privilegi di 
amministratore. Censirli periodicamente è una buona pratica di hardening. 

Es. 8 Trovare le directory con lo sticky bit attivo (come /tmp). 

$ find / -type d -perm /1000 2>/dev/null 

Lo sticky bit su una directory (1000) impedisce agli utenti di eliminare i file altrui anche se hanno 
il permesso di scrittura sulla directory, come accade in /tmp. 

Es. 9 Trovare tutti i file con almeno uno dei permessi speciali attivi (SUID, SGID, Sticky). 

 
 
 
 
$ find / -perm /7000 2>/dev/null 

Il valore 7000 è la somma dei tre bit speciali: SUID (4000) + SGID (2000) + Sticky (1000). Con il 
formato / basta che sia attivo almeno uno dei tre. 

Es. 10 Trovare i file scrivibili da "others" in /home (potenziale rischio sicurezza). 

$ find /home -type f -perm -002 

Il formato -002 (trattino) significa «il bit 002 deve essere presente»: permesso di scrittura per 
others. Un file scrivibile da chiunque in /home è spesso un errore di configurazione da 
correggere. 

Azioni e pipeline 

Es. 11 Trovare i file *.conf in /etc modificati negli ultimi 7 giorni e visualizzarli con ls -lh. 

$ find /etc -name "*.conf" -mtime -7 -exec ls -lh {} \; 

Il {} viene sostituito dal percorso di ogni file trovato. Il \; termina il comando -exec: il backslash 
previene l'interpretazione del ; da parte della shell. 

Es. 12 Cercare in /etc/ tutti i file che contengono la stringa 127.0.0.1 usando find + xargs grep. 

$ find /etc/ -name '*' -type f | xargs grep "127.0.0.1" 

find produce la lista dei file; xargs la passa a grep come argomenti. È equivalente a grep -r 
"127.0.0.1" /etc/ ma il -type f di find garantisce di passare solo file regolari, evitando errori su 
directory e link. 

💡 Nomi con spazi: Se i percorsi possono contenere spazi, usare la variante sicura: find 
/etc/ -type f -print0 | xargs -0 grep "127.0.0.1" 

Es. 13 Trovare tutti i file di proprietà dell'utente mario e copiarli in /root/backup_mario/. 
$ find / -user mario -type f -exec cp {} /root/backup_mario/ \; 2>/dev/null 

Per ogni file trovato viene eseguito cp file /root/backup_mario/. La directory di destinazione 
deve esistere prima di lanciare il comando: mkdir -p /root/backup_mario/. 

Es. 14 (avanzato) Trovare file chiamati student nel filesystem, escludendo /proc e /tmp, 
sopprimendo gli errori. 

$ find / -name "student" -type f ! -path '*/proc/*' ! -path '*/tmp/*' 2>/dev/null 

Il ! è l'operatore NOT: esclude i percorsi che corrispondono al pattern. */proc/* e */tmp/* 
escludono qualsiasi path che contenga quelle directory. È buona pratica escludere /proc e 
/sys nelle ricerche di sistema perché sono filesystem virtuali, non contengono file reali e 
generano molti falsi risultati.