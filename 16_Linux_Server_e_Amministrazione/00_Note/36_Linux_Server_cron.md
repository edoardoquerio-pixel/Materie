# Linux Server cron

**File:** `Linux Server cron.pdf`
**Tipo:** `.pdf`
**Dimensione:** 202.3 KB
**Ultima modifica:** 02/07/2026 09:22

---

  
 
 
 
Linux Server 
 
Docente: Wolfgang Cecchin 
Titolo argomenti:  
- Archivi compressi 
- Cron 
- Processi per il monitoring 

 
2 
 
Creazione di un archivio compresso 
 
Comando tar (“tape archive”) 
 
Creazione di un archivio: 
 
$ tar cvf nomeMioArchivio.tar directory1 directory2 dirctory3 file1 file2… 
 
Estrazione di un archivio: 
 
$ tar xvf nomeMioArchivio.tar directory1 directory2 dirctory3 file1 file2… 
 
 
Creazione di un archivio compresso - compressore gzip – opzione z : 
 
$ tar czvf nomeMioArchivio.tar.gz directory1 directory2 dirctory3 file1 
file2… 
 
Estrazione di un archivio: 
 
$ tar xzvf nomeMioArchivio.tar.gz directory1 directory2 dirctory3 file1 
file2… 
 
 
Creazione di un archivio compresso - compressore bz2 – opzione j: 
 
 
$ tar cjvf nomeMioArchivio.tar.bz2 directory1 directory2 dirctory3 file1… 
 
Estrazione di un archivio: 
 
$ tar xjvf nomeMioArchivio.tar.bz2 directory1 directory2 dirctory3 file1… 
 
  

 
   3 
 
Temporizzare (“schedulare”) comandi 
 
Ogni utente al proprio crontab che permette di gestire lo scheduling dei programmi 
 
 
 
 
 
https://crontab.guru/ 
 
Es (dopo aver creato una cartella du): 
 
0 7 * * * du -shc --exclude=proc --exclude=run /* > /var/log/du/output-du-$(date '+\%Y-
\%m-\%d').log 
 
  


 
   4 
 
Programmi per il monitoring del sistema 
 
Processi attualmente in uso: 
 
# top 
 
Oppure: 
# htop 
 
Carico della macchina: 
# uptime 
 
Consumo della memoria: 
# vmstat 
O 
# free -m 
 
Utilizzo della CPU e IO: 
# iostat 
 
Processi attivi: 
# ps aux 
Trovare un processo: 
# ps aux | grep nomeProcesso 
 
Albero dei processi: 
# pstree 
 
Uccidere un processo: 
# kill -1234 
Uccidere un processo e i suoi figli: 
# kill -9 1234 
 
Spazio disco: 
# df -h 
 
Dimensione files: 
# du – shc /miaDir 
 
Spazio occupato nel disco: 
 
# du -shc --exclude=proc --exclude=run /*  
 

 
   5 
Quali porte sono utilizzate (installare net-tools): 
 
# netstat -tulp 
 
 
