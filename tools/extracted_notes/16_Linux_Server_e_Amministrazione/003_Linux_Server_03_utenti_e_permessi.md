# Linux Server 03 utenti e permessi

Fonte: `Linux Server 03 utenti e permessi.pdf`

DOCENTE 

Wolfgang Cecchin 

UNITA’ FORMATIVA 

Linux Server 

ARGOMENTO 

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
$ passwd 

Cambiare la password di un utente: 
# passwd marco 

2 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Aggiungo un utente: 

# useradd marco 

Imposto una password per l’utente 
# passwd marco 

Che cosa è capitato? 

Lo vedo nel file: 
/etc/passwd 
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

3 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Come Marco provo a entrare nella home di Alberto e creare un 
file: 
$ touch mioFile 

Non posso. 

Perché? 

Perché non ho i permessi: 
drwxr-xr-x 2 alberto alberto 4,0K nov 13 11:17 alberto 

4 

 
 
 
 
 
 
 
 
 
 
 
I permessi sono organizzati in 3 gruppi: 

- User; 
- Group; 
- Other; 

Per ciascuno di questi gruppi viene indicato: 

- Nessun permesso: -; 
- Lettura: r; 
- Scrittura: w; 
- Esecuzione: x. 

La lettera “d” in prima posizione indica che si tratta di una 
directory. 

Per cambiare permessi: 
$ chmod permissions filename 

Ci sono due modi per cambiare permessi. 

5 

 
 
 
 
 
 
 
 
 
 
Modalità numerica: 

Number 

Permission Type 

Symbol 

0 

1 

2 

3 

4 

5 

6 

7 

No Permission 

Execute 

Write 

Execute + Write 

Read 

Read + Execute 

Read +Write 

Read + Write +Execute 

--- 

--x 

-w- 

-wx 

r-- 

r-x 

rw- 

rwx 

Esempio: 
$ chmod 764 mioFile 

- il proprietario ha tutti i permessi; 
- il gruppo cui appartiene l’utente può leggere e scrivere; 
- Tutti gli altri possono solo leggere. 

6 

 
 
 
 
 
 
 
 
 
 
Modalità simbolica: 

Operator 

Description 

Adds a permission to a file or 
directory 

Removes the permission 

Sets the permission and 
overrides the permissions set 
earlier. 

+ 

- 

= 

User Denotations 

u 

g 

o 

a 

user/owner 

group 

other 

all 

Esempi: 
$ chmod o=rwx mioFile 

Tutti gli altri possono leggere, scrivere ed eseguire. 

$ chmod g+x 

Aggiungo i permessi di esecuzione al gruppo. 

$ chmod g-r tolgo i permessi di lettura al gruppo. 

Altri comandi utili: 

7 

 
 
 
 
 
 
 
 
 
 
 
 
 
Aggiungere un gruppo: 
# groupadd mynewgroup 

Cambiare il gruppo: 
# chgroup 

Aggiungere un utente a un gruppo: 
# usermod -a -G examplegroup exampleusername 
(oppure è possibile editare il file /etc/passwd). 

Cambiare proprietario: 
# chown 

Opzione ricorsiva: 
$ chmod -R 755 miaDir 
$ chown -R user:group mioFile. 

Esercizio: 
Creare una directory e far sì che entrambi gli utenti possano 
scrivere file all’interno. 

8