# Linux Server tool di diagnostica

**File:** `Linux Server tool di diagnostica.pdf`
**Tipo:** `.pdf`
**Dimensione:** 240.1 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
 
 
 
  
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Tool di diagnostica 

[Digitare qui] 
 
 
uptime 
Il comando uptime fornisce in una sola riga le informazioni essenziali sullo stato del 
server: 
 
• da quanto tempo il sistema e' acceso 
• quanti utenti sono collegati 
• il load average degli ultimi 1, 5 e 15 minuti 
 
$ uptime 
 
 10:32:04 up 14 days, 3:21,  2 users,  load average: 0.12, 0.08, 0.05 
 
Lettura campo per campo: 
 
• 10:32:04 — ora corrente del sistema 
• up 14 days, 3:21 — il sistema e' acceso da 14 giorni, 3 ore e 21 minuti. Il formato e' giorni, 
poi ore:minuti 
• 2 users — numero di sessioni utente aperte (terminali, SSH...) 
• load average: 0.12, 0.08, 0.05 — carico medio nell'ultimo 1 minuto, 5 minuti e 15 minuti 
 
Il load average 
Indica quanti processi sono in attesa di essere eseguiti dalla CPU, mediato nel 
tempo. 
I tre valori rappresentano rispettivamente la media dell'ultimo 1 minuto, 5 minuti e 
15 minuti. 
 
Il valore di riferimento e' il numero di core della CPU: 
 
• load average < numero di core — il sistema e' a riposo, c'e' capacita' libera 
• load average = 1.0 su 1 core — CPU al 100%, situazione limite ma non critica 
• load average > numero di core — ci sono processi che aspettano la CPU: il sistema e' 
sovraccarico 
 
I tre valori vanno letti insieme: un picco solo nel primo (1 min) e' passeggero; se 
anche il terzo (15 min) e' alto, il problema e' strutturale. 
 
Esempio: load average 0.12, 0.08, 0.05 su un sistema a 4 core — tutto tranquillo. 
Esempio: load average 7.50, 6.20, 4.10 su un sistema a 4 core — il sistema e' sotto 
stress. 
 
Quanti core ha il mio sistema? 
 
$ nproc 
 
$ lscpu | grep 'CPU(s)' 
 
Analisi della memoria RAM: free 
Il comando free mostra la memoria totale, usata, libera e la quota di swap. 
L'opzione -h presenta i valori in formato leggibile, scegliendo automaticamente 
l'unita' piu' adatta. 
 
$ free -h 
 

[Digitare qui] 
 
 
              total        used        free      shared  buff/cache   available 
Mem:           15Gi        3,2Gi       9,1Gi      283Mi        3,0Gi       11Gi 
Swap:         2,0Gi          0B        2,0Gi 
 
Cosa significa buff/cache? 
Linux usa la RAM libera come cache disco per migliorare le prestazioni. 
La colonna available e' quella che conta davvero: indica quanta memoria puo' 
essere usata da nuovi processi. 
 
Messaggi del kernel: dmesg 
dmesg mostra i messaggi del kernel dal momento del boot. 
E' il primo strumento da consultare in caso di problemi hardware. 
 
• Rilevamento e inizializzazione dei dispositivi hardware 
• Errori di driver 
• Problemi con dischi e filesystem 
• Messaggi di errore della rete 
 
$ dmesg | tail -50 
 
$ dmesg | grep -i error 
 
$ dmesg | grep -iE "error|fail|warn|critical" 
 
$ dmesg | grep -i sda 
 
$ dmesg | grep -i nvme 
 
L'opzione -T mostra i timestamp in formato leggibile: 
 
$ dmesg -T | grep -i error 
 
Le parole chiave piu' importanti da cercare: 
 
• error, fail — errori generici di dispositivi o driver 
• I/O error, timeout — il disco non risponde o e' lento 
• EXT4-fs error — filesystem corrotto 
• Out of memory — il sistema ha esaurito la RAM 
• Hardware Error — errore segnalato direttamente dall'hardware 
 
Regola pratica: un messaggio che appare una volta puo' essere normale. Se si 
ripete molte volte, c'e' un problema reale. 
 
Log di sistema: journalctl 
journalctl e' il tool per consultare il journal di systemd. 
Raccoglie in modo centralizzato i log di tutti i servizi e del kernel. 
 
Comando Descrizione 
journalctl -xe Ultimi log con contesto esteso (errori recenti) 
journalctl -b Log del boot corrente 
journalctl -b -1 Log del boot precedente 

[Digitare qui] 
 
 
journalctl -b -2 Due boot fa (utile dopo un crash) 
journalctl -u ssh Log di un servizio specifico 
journalctl -f Segue i log in tempo reale (come tail -f) 
journalctl -p err Solo messaggi di errore 
journalctl -p warning Messaggi di warning e superiori 
journalctl --since '1 hour ago' Ultimi 60 minuti 
journalctl --since 'today' Log di oggi 
 
# journalctl -b -1 -p err 
 
Cosa cercare in journalctl: 
 
• failed, error — servizi che non si avviano o vanno in errore 
• un servizio che si ripete in loop — segnale di un crash ripetuto 
• kernel: Hardware Error — errore hardware segnalato dal kernel 
 
Analisi dei dischi 
I dispositivi in /dev/ 
In Linux tutti i dispositivi hardware sono rappresentati come file nella cartella /dev/. 
I dischi non fanno eccezione. 
 
• /dev/hda, /dev/hdb... — dischi IDE (vecchio standard, ormai obsoleto). La lettera indica il 
disco: hda e' il primo, hdb il secondo. 
 
• /dev/sda, /dev/sdb... — dischi SATA, SAS o USB. SATA e' il collegamento standard per 
hard disk e SSD nei PC moderni. SAS e' la versione enterprise, piu' veloce e affidabile, usata nei 
server. La lettera indica il disco: sda e' il primo, sdb il secondo. Le partizioni si indicano con un 
numero: sda1, sda2... 
 
• /dev/nvme0n1, /dev/nvme1n1... — dischi NVMe, collegati direttamente al bus PCIe. Sono 
molto piu' veloci di SATA. Il nome segue il formato nvmeXnY: X e' il numero del controller (0, 1, 2...), 
Y e' il numero del namespace (quasi sempre 1). Le partizioni si indicano con p: nvme0n1p1, 
nvme0n1p2... 
 
Struttura dispositivi: lsblk 
lsblk elenca tutti i dispositivi a blocchi (dischi, partizioni, LVM) con struttura ad 
albero. 
E' il primo comando da usare per conoscere il nome dei dispositivi, che servira' poi 
in df, smartctl e altri strumenti. 
 
$ lsblk 
 
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT 
sda           8:0    0   500G  0 disk 
├─sda1        8:1    0   499G  0 part / 
└─sda2        8:2    0     1G  0 part [SWAP] 
nvme0n1     259:0    0   1,8T  0 disk 
├─nvme0n1p1 259:1    0   512M  0 part /boot/efi 
└─nvme0n1p2 259:2    0   1,8T  0 part /data 

[Digitare qui] 
 
 
 
$ lsblk -o NAME,SIZE,TYPE,MOUNTPOINT,FSTYPE 
 
Spazio sui filesystem: df 
df -h mostra lo spazio usato e libero su ogni filesystem montato. 
 
$ df -h 
 
Filesystem      Size  Used Avail Use% Mounted on 
/dev/sda1        20G   12G  6,8G  64% / 
/dev/sdb1       500G  230G  245G  49% /data 
 
Attenzione alla colonna Use%: sopra il 90% il filesystem e' quasi pieno. 
 
Spazio per directory: du 
$ du -sh /var/log 
 
$ du -h /var | sort -rh | head -20 
 
Mostrare lo spazio occupato da ogni directory di primo livello sotto /: 
 
$ sudo du --max-depth=1 -hx / 
 
L'opzione --max-depth=1 limita la profondita' a un solo livello, senza scendere 
nelle sottodirectory. 
L'opzione -x rimane sullo stesso filesystem, escludendo /proc, /sys, /dev che 
contengono file virtuali del kernel e non dati reali. 
 
Mostrare il totale per ogni directory con somma finale: 
 
$ sudo du -sxhc --exclude=proc * 
 
L'opzione -s mostra solo il totale per ogni argomento. L'opzione -c aggiunge una 
riga finale con il totale complessivo. 
 
Disco pieno — come diagnosticare 
Prima si verifica quale filesystem ha esaurito lo spazio: 
 
$ df -h 
 
Se una riga mostra Use% al 100% (o vicino), quella e' la partizione piena. 
A quel punto si scende nelle directory per trovare il colpevole: 
 
$ sudo du --max-depth=1 -hx / 
 
Si individua la directory piu' grande, poi si scende di un livello: 
 
$ sudo du --max-depth=1 -hx /var 
 
$ sudo du --max-depth=1 -hx /var/log 
 

[Digitare qui] 
 
 
Si continua a scendere finche' non si trova il file o la directory che occupa lo 
spazio inaspettato. 
I soliti sospettati sono: /var/log (log cresciuti troppo), /var/cache, /tmp, /home. 
 
Salute dei dischi: smartctl 
smartctl legge i dati S.M.A.R.T. direttamente dal disco per valutarne lo stato di 
salute. 
Il nome del device da usare si ricava con lsblk. 
Attenzione: il percorso completo /dev/ e' obbligatorio, altrimenti il sistema non 
trova il dispositivo. 
 
# apt install smartmontools 
 
# smartctl -H /dev/sda 
 
# smartctl -H /dev/nvme0n1 
 
Se il risultato e' PASSED: il disco e' sano. 
Se il risultato e' FAILED: fare subito un backup! Il disco puo' smettere di funzionare in 
qualsiasi momento. 
 
Dopo un FAILED, per capire qual e' il problema ispezionare tutti gli attributi: 
 
# smartctl -a /dev/sda 
 
Cercare nella colonna WHEN_FAILED i valori FAILING_NOW o In_the_past. 
Gli attributi piu' importanti da controllare: 
 
Attributo SMART Significato 
Reallocated_Sector_Ct Settori danneggiati rimappati. Idealmente 0 
Current_Pending_Sector Settori instabili in attesa di rimappatura 
Uncorrectable_Sector Errori non correggibili. Se > 0 il disco e' a rischio 
Power_On_Hours Ore totali di utilizzo del disco 
Temperature_Celsius Temperatura attuale del disco 
 
Memoria RAM danneggiata 
Con un settore di RAM danneggiato, free -h di solito non mostra nulla di anomalo. 
Il kernel esclude automaticamente le pagine difettose durante il boot — la RAM 
totale mostrata puo' essere leggermente inferiore a quella installata fisicamente, 
ma non appare un errore esplicito. 
 
I sintomi reali di RAM danneggiata sono: 
 
• crash casuali e imprevedibili del sistema, spesso senza un pattern chiaro 
• kernel panic — il sistema si blocca con un messaggio di errore e si riavvia o si spegne 
• processi che terminano in modo anomalo con errori di segmentation fault 
• dati corrotti in modo apparentemente casuale 
 

[Digitare qui] 
 
 
In casi gravi il server si spegne improvvisamente perche' il kernel scrive dati in una 
zona di memoria corrotta e il risultato e' imprevedibile. 
 
Per diagnosticare RAM difettosa il tool dedicato e' memtest86+, che gira fuori dal 
sistema operativo, dal menu di GRUB, e testa tutta la RAM in modo sistematico. 
 
Riepilogo degli strumenti 
 
Comando Categoria Cosa fa 
uptime Sistema Carico, uptime, load average 
free -h Memoria RAM e swap usata/libera 
dmesg Kernel Messaggi hardware dal boot 
journalctl Log Log centralizzati di tutto il sistema 
lsblk Disco Struttura dischi, partizioni e nomi dei device 
df -h Disco Spazio usato su ogni filesystem 
du -sh Disco Spazio occupato da una directory 
du --max-depth=1 -hx Disco Spazio per directory di primo livello, stesso 
filesystem 
smartctl -H Disco Salute S.M.A.R.T. del disco 
smartctl -a Disco Dettaglio completo degli attributi S.M.A.R.T. 
memtest86+ Memoria Test della RAM (si avvia da GRUB, fuori dal 
sistema operativo) 
 
 
Esercizio 
1. Verificare il carico del sistema con uptime. 
   Quanti core ha la VM? Il load average e' alto o basso rispetto al numero di core? 
 
2. Con free -h verificare quanta RAM e' disponibile. 
   Quanto usa il sistema al minimo? Quanto c'e' in buff/cache? 
 
3. Con dmesg | grep -iE "error|fail|warn" cercare problemi hardware. 
   Con journalctl -b -p err cercare errori nel boot corrente. 
 
4. Con lsblk identificare i dischi presenti nella VM e i loro nomi. 
   Quali partizioni ci sono? Dove sono montate? 
 
5. Con df -h trovare il filesystem piu' pieno. 
   Con du -sh /* trovare le directory piu' grandi. 
 
6. Installare smartmontools e verificare la salute del disco della VM. 
   Usare il nome del device trovato con lsblk. 
 
