# Linux Server 02 Comandi Essenziali

## Panoramica
Installazione Debian e Comandi Essenziali

## Argomenti trattati
Linux, Installazione, Configurazione

---
## Appunti

Wolfgang Cecchin
Installazione Debian e Comandi Essenziali
Programma odierno:
- Leggere e scrivere files;
- Muoversi nelle directories;
- Creare utenti;
- Substitute User e Sudo;
Installare pacchetti
https://it.wikipedia.org/wiki/Shell_Unix
https://en.wikipedia.org/wiki/Unix_shell
Esistono vari tipi di shell:
Muoversi agevolmente con la shell:
Il tab fornisce l’autocomplete dei comandi noti;
la freccia in su serve per scorrere la history dei comandi (vedi anche il
comando “history”);
CTRL + D effettua il logout;
CTRL + C interrompe un comando;
q serve per uscire dalla modalità lettura di alcuni programmi (man);
~ : è la home directory.
$ clear # “pulisce” il terminale
Struttura dei comandi in Linux
La struttura di un comando in Linux è:
Comando + opzioni + parametri
- l = long listening form
- h = human readable
ls -lah /home =
- l = long listening form
- h = human readable
/home = della directory home
ls -lah /home = fai l’elenco del contenuto (ls) della directory home (/home),
usando la modalità estesa (long listening form), mostrando tutti i file (all), in
modo che siano comprensibile da un utente umano
$ ls -lah /home
Opzioni in forma estesa
$ ls -l --all --human-readable /home
Manuali ed help dei comandi
Creare file e reindirizzare l’input verso un file
$ touch MioFile
$ echo “ciao mondo” > mioFile
$ echo “ciao mondo” >> mioFile
$ ls > output_ls
Leggere un file
Scrivere un file
Oppure (curiosità):
(:i per scrivere
:wq per scrivere e salvare
:q! per forzare l’uscita)
Creare directories, Copiare, rinominare, cancellare un file
$ mkdir miaDir #creo una directory
$ cp source destination # copia
$ cp -R source destination # copia una directory (copia ricorsiva)
$ mv oldName newName # rinomino un file
$ rm file # cancella il file
$ rm -r directory # rimuove una directory e il suo contenuto
L’opzione -f forza (per lo più evitare di usarla).
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
FHS Filesystem Hierarchy Standard
https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard
Attenzione nelle moderne distribuzioni alcuni directories “puntano” ad altre.
root (individuato con #): è l’amministratore del sistema
su = substitute user
sudo = “substitute user do” (“super user do”); esegue il comando per un
E’ necessario aggiungere l’utente in /etc/sudoers.d
Creare un file con il nome utente e aggiungere all’’interno:
user ALL=(ALL:ALL) ALL
• The first ALL is the users allowed to use the sudo command.
• The second ALL defines the hosts (servers) on which sudo can be
• The third ALL is the user you are running the command as.
• The last ALL defines the commands allowed.
Nota: la home di root è /root

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 002_Linux_Server_02_Comandi_Essenziali.md*
