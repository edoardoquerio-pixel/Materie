# Linux Server esercizi ripasso meta corso2

**File:** `Linux Server esercizi ripasso meta corso2.pdf`
**Tipo:** `.pdf`
**Dimensione:** 281.3 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
 
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
Esercitazioni di ripasso 

 
2 
 
 
 
Attività preliminari (facciamo un po’ di pulizia) – 
Rimozione degli utenti non necessari: 
 
Backup della macchina: 
- Con la macchina virtuale spenta, creare un’istantanea (snapshot) della 
macchina; 
 
 
Consegna esercizio 2 
 
Federica ha 45 anni e si occupa di programmazione e sistemi in un’azienda. 
Divorziata, si è poi risposata. 
La sua famiglia è composta – oltre che dall’attuale compagno (o marito) - da 
quattro figli: 
Paolo e Pietro di 3 e 6 anni; 
Giovanni e Giacomo di 12 e 14 anni. 
 
All’interno del proprio computer di casa ha creato un media server, in cui 
memorizza i film che acquista o che scarica ( legalmente con regolare utilizzo 
dei DRM). 
 
Il server di casa che utilizza come media server è una piattaforma Linux. 
 
Federica vorrebbe far sì che i figli di 6 e 3 anni abbiano accesso ai contenuti 
riservati ai bambini di 6 anni; e che i figli di 12 e 14 abbiano accesso  ai 
contenuti fino a 18 anni. Infine vorrebbe che lei e l’attuale compagno (che non 
è un utente tecnico e che non avrà un account nel sistema) abbiano accesso a 
tutti i contenuti. 
 
- Creare i seguenti utenti: 
federica, paolo, pietro, giovanni, giacomo 
- Aggiungere federica come sudo user; 
- Creare i seguenti gruppi: 
piccoli, grandi, adulti 
- Assegnare paolo e pietro al gruppo piccoli; 
- Assegnare giovanni e giacomo al gruppo grandi; 

 
3 
 
- Assegnare federica al gruppo adulti; 
- Creare una directory: 
/home/contenuti 
- All’interno della directory /home/contenuti creare due directories: 
piccoli 
grandi 
adulti 
- Fare in modo che: 
o Il gruppo piccoli abbia accesso alla sola cartella piccoli; 
o Il gruppo grandi abbia accesso alla cartella piccoli e alla cartella 
grandi; 
o federica abbia accesso a tutto. 
 
Federica vuol far sì che il figlio giovanni possa caricare i film in SFTP. 
Verificare che giovanni possa entrare sul sever in SFTP e possa 
caricare un file. 
 
Federica vuole inoltre creare un blog per la famiglia. 
Creare l’host 
famiglia.local e famiglia 
e verificare che nginx risponda su quell’host con la pagina di default. 
 
 
 
 
 
 
