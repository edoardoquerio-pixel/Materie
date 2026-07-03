# Linux Server 02 Comandi Essenziali

Fonte: `Linux Server 02 Comandi Essenziali.pdf`

DOCENTE 

UNITA’ 
FORMATIVA 

ARGOMENTO 

Wolfgang Cecchin 

Linux Server 

Installazione Debian e Comandi Essenziali 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Programma odierno: 

- Leggere e scrivere files; 
- Muoversi nelle directories; 
- Creare utenti; 
- Substitute User e Sudo; 
- 
Installare pacchetti 

2 

 
 
 
 
 
 
 
 
 
La shell 

https://it.wikipedia.org/wiki/Shell_Unix 

https://en.wikipedia.org/wiki/Unix_shell 

Esistono vari tipi di shell: 
sh, zsh, bash… 

Muoversi agevolmente con la shell: 

Il tab fornisce l’autocomplete dei comandi noti; 
la freccia in su serve per scorrere la history dei comandi (vedi anche il 
comando “history”); 
CTRL + D effettua il logout; 
CTRL + C interrompe un comando; 
q serve per uscire dalla modalità lettura di alcuni programmi (man); 
~ : è la home directory. 

Il comando: 
$ clear # “pulisce” il terminale 

3 

 
 
 
 
 
 
 
 
 
 
 
 
 
Struttura dei comandi in Linux 

La struttura di un comando in Linux è: 
Comando + opzioni + parametri 

Es: 
ls = list 

ls -lah = 

list 

- l = long listening form 
- a = all 
- h = human readable 

ls -lah /home = 

list 

- l = long listening form 
- a = all 
- h = human readable 

/home = della directory home 

ls -lah /home = fai l’elenco del contenuto (ls) della directory home (/home), 
usando la modalità estesa (long listening form), mostrando tutti i file (all), in 
modo che siano comprensibile da un utente umano 

Opzioni brevi 
$ ls -lah /home 

Opzioni in forma estesa 
$ ls -l --all --human-readable /home 

4 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Manuali ed help dei comandi 

$ man ls 
$ ls --help 

5 

 
 
 
 
 
Creare file e reindirizzare l’input verso un file 

$ touch MioFile 

$ echo “ciao mondo” > mioFile 
$ echo “ciao mondo” >> mioFile 

$ ls > output_ls 

Leggere un file 

$ cat MioFile 

Scrivere un file 

$ nano MioFile 

Oppure (curiosità): 

$ vi MioFile 

(:i per scrivere 
:w per salvare 
:q per uscire 
:wq per scrivere e salvare 
:q! per forzare l’uscita) 

6 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Creare directories, Copiare, rinominare, cancellare un file 

$ mkdir miaDir #creo una directory 

$ cp source destination # copia 
$ cp -R source destination # copia una directory (copia ricorsiva) 
$ mv oldName newName # rinomino un file 
$ rm file # cancella il file 
$ rm -r directory # rimuove una directory e il suo contenuto 

L’opzione -f forza (per lo più evitare di usarla). 

7 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
Muoversi nel file system 

$ cd # change directory 

$ pwd # quale è la directory corrente? 

Simboli “speciali” 

. = è la directory stessa; 
.. = è la directory superior; 
/ = è la directory principale del sistema (la root); 
~ = è la home dell’utente (~ è la tilde; su linux usare i tasti: alt gr + ì ) 

$ cd / # vado nella directory root del sistema 

$cd - # torno alla directory precedente 

$ tree -L 1 / # vedo l’alberatura del sistema 

8 

 
 
 
 
 
 
 
 
 
 
 
 
FHS Filesystem Hierarchy Standard 

Riferimenti: 

https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard 

Attenzione nelle moderne distribuzioni alcuni directories “puntano” ad altre. 

9 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
Gli utenti 

root (individuato con #): è l’amministratore del sistema 

su = substitute user 

sudo = “substitute user do” (“super user do”); esegue il comando per un 
altro utente- 

E’ necessario aggiungere l’utente in /etc/sudoers.d 

Creare un file con il nome utente e aggiungere all’’interno: 
user ALL=(ALL:ALL) ALL 

• The first ALL is the users allowed to use the sudo command. 
• The second ALL defines the hosts (servers) on which sudo can be 

employed. 

• The third ALL is the user you are running the command as. 
• The last ALL defines the commands allowed. 

Nota: la home di root è /root 

Attenzione non confondere: 
l’utente root; 
la home di root che è /root; 
la root directory che è /. 

10 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Aggiungere utenti: 

# useradd 

# useradd -D alberto 
# useradd -d /var/marco marco 

# groupadd 

File che gestiscono gli utenti 

Il file /etc/passwd 
Il file /etc/group 
Il file /etc/shadow 
Il file /etc/shadow 

Cambiare password di un utente 

Cambiare la propria password: 
$ passwd 

Cambiare la password di un utente: 
# passwd marco 

11 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Link simbolici 

$ ln -s file nomeLink 

Comando tar (“tape archive”) 

Creazione di un archivio: 

$ tar cvf nomeMioArchivio.tar directory1 directory2 dirctory3 file1 file2… 

Estrazione di un archivio: 

$ tar xvf nomeMioArchivio.tar directory1 directory2 dirctory3 file1 file2… 

Creazione di un archivio compresso - compressore gzip – opzione z : 

$ tar czvf nomeMioArchivio.tar.gz directory1 directory2 dirctory3 file1 file2… 

Estrazione di un archivio: 

$ tar xzvf nomeMioArchivio.tar.gz directory1 directory2 dirctory3 file1 file2… 

Creazione di un archivio compresso - compressore bz2 – opzione j: 

$ tar cjvf nomeMioArchivio.tar.bz2 directory1 directory2 dirctory3 file1… 

Estrazione di un archivio: 

$ tar xjvf nomeMioArchivio.tar.bz2 directory1 directory2 dirctory3 file1… 

12 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Installazione pacchetti in Debian 

Directory di configurazione per i repositories (lo vedremo per il PHP) 

/etc/apt.d 

Per aggiornare i repositories: 

# apt update 

Per installare i pacchetti: 

# apt install 

Attenzione! 

Usare con molta cautela: 

# apt upgrade 

Effettua l’upgrade dei pacchetti disponibili 

13