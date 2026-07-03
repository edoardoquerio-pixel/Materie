# Linux Server 03 utenti e permessi

## Panoramica
In Debian è possibile utilizzare:

## Argomenti trattati
Linux

---
## Appunti

Wolfgang Cecchin
UNITA’ FORMATIVA
Utenti e permessi
In Debian è possibile utilizzare:
# useradd
O meglio ancora:
# adduser
Per aggiungere utenti.
# useradd
# useradd -D alberto
# useradd -d /var/marco marco
# groupadd
File che gestiscono gli utenti
Il file /etc/passwd
Il file /etc/group
Il file /etc/shadow
Il file /etc/gshadow
Aggiungere un utente a un gruppo:
sudo usermod -a -G groupname username
groups utente → vedo a quali gruppi appartiene l’utente
Cambiare password di un utente
Cambiare la propria password:
Cambiare la password di un utente:
# passwd marco
Aggiungo un utente:
# useradd marco
Imposto una password per l’utente
# passwd marco
Che cosa è capitato?
Lo vedo nel file:
La cartella /home/marco e /home/alberto non è stata creata,
infatti c’è bisogno
di un parametro.
Cancello l’utente e lo ricreo:
# userdel marco
# useradd -m marco
Creare utenti senza home:
# useradd -M
Creo un secondo utente:
# useradd -m alberto
Imposto una password per l’utente
# passwd alberto
Faccio il login come Alberto.
Che shell sto usando?
$ echo "$SHELL"
Vado a vedere le home directories.
Come Marco provo a entrare nella home di Alberto e creare un
$ touch mioFile
Perché non ho i permessi:
drwxr-xr-x 2 alberto alberto 4,0K nov 13 11:17 alberto
I permessi sono organizzati in 3 gruppi:
Per ciascuno di questi gruppi viene indicato:
- Nessun permesso: -;
- Scrittura: w;
- Esecuzione: x.
La lettera “d” in prima posizione indica che si tratta di una
Per cambiare permessi:
$ chmod permissions filename
Ci sono due modi per cambiare permessi.
Modalità numerica:
Permission Type
Execute + Write
Read + Write +Execute
$ chmod 764 mioFile
- il proprietario ha tutti i permessi;
- il gruppo cui appartiene l’utente può leggere e scrivere;
- Tutti gli altri possono solo leggere.
Modalità simbolica:
Adds a permission to a file or
Removes the permission
Sets the permission and
overrides the permissions set
User Denotations
$ chmod o=rwx mioFile
Tutti gli altri possono leggere, scrivere ed eseguire.
Aggiungo i permessi di esecuzione al gruppo.
$ chmod g-r tolgo i permessi di lettura al gruppo.
Altri comandi utili:
Aggiungere un gruppo:
# groupadd mynewgroup

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 003_Linux_Server_03_utenti_e_permessi.md*
