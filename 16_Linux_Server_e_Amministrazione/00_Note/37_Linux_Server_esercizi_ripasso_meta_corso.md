# Linux Server esercizi ripasso meta corso

**File:** `Linux Server esercizi ripasso meta corso.pdf`
**Tipo:** `.pdf`
**Dimensione:** 200.3 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
 
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
Esercitazione 

 
2 
 
 
 
Attività preliminari (facciamo un po’ di pulizia) – 
Rimozione degli utenti non necessari: 
 
Backup della macchina: 
- Con la macchina virtuale spenta, creare un’istantanea (snapshot) della 
macchina; 
Rimozione utenti: 
- Accendere la macchina e cancellare gli utenti non necessari (userdel); 
- Lasciare solo l’utente principale (che si chiamerà its-usr o avrà il nome 
che avete dato voi all’utente). 
 
 
Consegna esercizio 1 
 
(Effettuare queste operazioni utilizzando la shell). 
 
Siete amministratori della macchina dell’azienda acme srl. 
 
- Come amministratore della macchina creare una cartella acme che si 
trovi in home 
- Creare due gruppi: 
dipendenti 
collaboratori 
- All’interno della cartella acme creare due cartelle: 
dipendenti 
collaboratori 
Alla cartella dei collaboratori possono accedere tutti; 
Alla cartella dei dipendenti possono accedere solo i dipendenti. 
 
  

 
3 
 
 
 
 
Davide Rossi nel gennaio 2022 incomincia a lavorare per l’azienda Acme srl. 
 
- Come amministratore della macchina di Davide Rossi creare un utente 
per Davide Rossi; 
- Assegnare Davide al gruppo dipendenti; 
- Davide all’interno della propria home crea una cartella Documenti. 
All’interno della cartella Documenti crea una cartella lavoro. 
All’interno della cartella lavoro, Davide crea una cartella con l’anno e 
poi crea una cartella per ogni mese. 
Si vuole avere la seguente struttura: 
home 
--- davide 
---- Documenti 
--------- lavoro 
------------------ 2022 
------------------------- gennaio 
------------------------- febbraio 
… 
------------------------- dicembre 
------------------ 2023 
------------------------- gennaio 
 
All’interno di ciascuna directory, creare un file che si chiama 
report.txt 
 
- Davide a un certo punto non si ricorda più la sua password. Come 
amministratore di sistema cambiargli la password. 
 
- Verificate che Davide possa entrare in SSH con user name e password. 
 
- Come Davide creare una coppia di chiavi dalla macchina Windows (o 
Mac). 
 
Suggerimento: per evitare di sovrascrivere le chiavi, create una nuova 
cartella in cui immagazzinare le nuove chiavi. 
 

 
4 
 
- Come amministratore di sistema predisponete l’accesso a SSH con 
chiave per Davide e disabilitate l’accesso con password. 
 
Suggerimento: Davide può scegliere una chiave privata  diversa da 
quella di default con cui entrare, usando il comando: 
ssh-add \percorsoWindows\chiave 
 
Nel gennaio 2023 Davide Rossi trova un altro impiego e pertanto lascia la 
Acme srl. 
 
- Prima di cancellare l’utente di Davide, l’amministratore di sistema è 
incaricato di salvare una copia della cartella lavoro nella cartella 
/home/acme/dipendenti. Predisporre una cartella con il lavoro di 
Davide; 
 
- Tale copia deve poter essere consultata in sola lettura e non modificata 
dagli altri utenti; 
 
- L’amministratore di sistema infine cancella l’utenza di Davide. 
 
Nel febbraio 2023 viene assunto l’utente CarloVerdi, che è un collaboratore in 
partita iva dell’azienda. 
 
- Creare l’utente Carlo Verdi; 
- Assegnare l’utente carlo al gruppo collaboratori; 
- Si vuole dare all’utente carlo i permessi di amministratore della 
macchina (dare la possibilità all’utente carlo di diventare 
amministratore con sudo; 
- Accertarsi che l’utente possa accedere in SSH tramite chiave; 
 
Secondo indicazioni della dirigenza, l’utente carlo deve poter modificare i 
files che furono di Davide: 
 
- Lasciare una copia dei files in sola lettura nella cartella dipendenti; 
- Creare una seconda copia dei files in lettura e scrittura nella cartella 
collaboratori, in modo che siano modificabili da carlo e dal gruppo 
collaboratori. 
 
 

 
5 
 
 
 
 
- Utilizzando un client grafico SFTP (SSH File Transfer Protocol), 
caricare dei files all’interno della cartella Documenti di carlo. 
 
 
L’azienda acme vuole creare il proprio sito aziendale. 
Incominciamo a creare l’hostname. 
 
- Creare l’hostname acme e acme.local 
- Verificare che: 
o E’ possibile effettuare il ping su acme.local; 
o E’ possibile entrare un SSH utilizzando il nome host acme.local; 
o Che la pagina di default di nginx risponde sull’host acme.local. 
 
