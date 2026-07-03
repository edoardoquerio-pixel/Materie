# Linux Server 03.4 Esercizio-su-utenti-permessi - soluzione

**File:** `Linux Server 03.4 Esercizio-su-utenti-permessi - soluzione.pdf`
**Tipo:** `.pdf`
**Dimensione:** 110.3 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
1 
 
 
 
 
  
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Esercizio su utenti e permessi 

 
  2 
Soluzione - Comandi 
 
1. Creazione degli utenti 
bash 
sudo adduser giulia 
sudo adduser andrea 
sudo adduser chiara 
sudo adduser luca 
sudo adduser sara 
Per ogni utente, adduser chiederà la password e le informazioni opzionali (premi Invio per 
saltarle). 
 
2. Creazione dei gruppi 
bash 
sudo addgroup scrittori 
sudo addgroup editing 
sudo addgroup grafica 
sudo addgroup amministrazione 
 
3. Assegnazione utenti ai gruppi 
bash 
sudo usermod -aG scrittori andrea 
sudo usermod -aG scrittori chiara 
sudo usermod -aG editing luca 
sudo usermod -aG scrittori luca 
sudo usermod -aG grafica sara 
sudo usermod -aG amministrazione giulia 
sudo usermod -aG scrittori giulia 
sudo usermod -aG editing giulia 
sudo usermod -aG grafica giulia 
 
4. Creazione della struttura directory 
bash 
sudo mkdir -p /home/casaeditrice/manoscritti 

 
  3 
sudo mkdir -p /home/casaeditrice/bozze 
sudo mkdir -p /home/casaeditrice/grafica/copertine 
sudo mkdir -p /home/casaeditrice/grafica/impaginazione 
sudo mkdir -p /home/casaeditrice/amministrazione 
 
5. Impostazione proprietari e gruppi delle directory 
bash 
sudo chown giulia:amministrazione /home/casaeditrice 
sudo chown giulia:scrittori /home/casaeditrice/manoscritti 
sudo chown giulia:editing /home/casaeditrice/bozze 
sudo chown giulia:grafica /home/casaeditrice/grafica 
sudo chown giulia:grafica /home/casaeditrice/grafica/copertine 
sudo chown giulia:grafica /home/casaeditrice/grafica/impaginazione  
sudo chown giulia:amministrazione /home/casaeditrice/amministrazione  
 
6. Impostazione permessi in modalità ottale 
bash 
sudo chmod 755 /home/casaeditrice 
sudo chmod 770 /home/casaeditrice/manoscritti 
sudo chmod 770 /home/casaeditrice/bozze 
sudo chmod 770 /home/casaeditrice/grafica 
sudo chmod 770 /home/casaeditrice/grafica/copertine 
sudo chmod 770 /home/casaeditrice/grafica/impaginazione 
sudo chmod 700 /home/casaeditrice/amministrazione 
 
7. Creazione dei file 
bash 
sudo touch /home/casaeditrice/manoscritti/romanzo_capitolo1.txt  
sudo touch /home/casaeditrice/bozze/romanzo_corretto.txt 
sudo touch /home/casaeditrice/grafica/copertine/bozza_copertina.png  
sudo touch /home/casaeditrice/amministrazione/contratti.txt 
Impostare proprietari dei file: 
bash 
sudo chown giulia:scrittori /home/casaeditrice/manoscritti/romanzo_capitolo1.txt  

 
  4 
sudo chown giulia:editing /home/casaeditrice/bozze/romanzo_corretto.txt  
sudo chown giulia:grafica /home/casaeditrice/grafica/copertine/bozza_copertina.png  
sudo chown giulia:amministrazione /home/casaeditrice/amministrazione/contratti.txt  
Impostare permessi dei file: 
bash 
sudo chmod 660 /home/casaeditrice/manoscritti/romanzo_capitolo1.txt  
sudo chmod 660 /home/casaeditrice/bozze/romanzo_corretto.txt 
sudo chmod 660 /home/casaeditrice/grafica/copertine/bozza_copertina.png  
sudo chmod 600 /home/casaeditrice/amministrazione/contratti.txt  
 
8. Comandi di verifica 
Verificare la struttura creata: 
bash 
ls -la /home/casaeditrice/ 
ls -la /home/casaeditrice/manoscritti/ 
ls -la /home/casaeditrice/bozze/ 
ls -la /home/casaeditrice/grafica/ 
ls -la /home/casaeditrice/grafica/copertine/ 
ls -la /home/casaeditrice/amministrazione/ 
Verificare i gruppi degli utenti: 
bash 
groups giulia 
groups andrea 
groups chiara 
groups luca 
groups sara 
 
Test accesso come andrea (scrittore): 
bash 
su - andrea 
touch /home/casaeditrice/manoscritti/nuovo_capitolo.txt    # Deve funzionare  
ls /home/casaeditrice/bozze/    # Permission denied 
ls /home/casaeditrice/amministrazione/    # Permission denied 
exit 

 
  5 
 
Test accesso come luca (editor): 
bash 
su - luca 
cat /home/casaeditrice/manoscritti/romanzo_capitolo1.txt    # Deve funzionare (è nel 
gruppo scrittori) 
touch /home/casaeditrice/bozze/nuova_correzione.txt    # Deve funzionare  
ls /home/casaeditrice/grafica/    # Permission denied 
exit 
 
Test accesso come sara (grafica): 
bash 
su - sara 
touch /home/casaeditrice/grafica/copertine/nuova_copertina.png    # Deve funzionare 
ls /home/casaeditrice/manoscritti/    # Permission denied 
ls /home/casaeditrice/bozze/    # Permission denied 
ls /home/casaeditrice/amministrazione/    # Permission denied 
exit 
 
Test accesso come giulia (amministrazione - accesso totale): 
bash 
su - giulia 
ls /home/casaeditrice/manoscritti/    # Deve funzionare 
ls /home/casaeditrice/bozze/    # Deve funzionare 
ls /home/casaeditrice/grafica/    # Deve funzionare 
cat /home/casaeditrice/amministrazione/contratti.txt    # Deve funzionare  
exit 
 
Riepilogo permessi ottali usati 
Ottale Simbolico Significato 
700 rwx------ Solo proprietario ha accesso completo 
755 rwxr-xr-x Proprietario: tutto; altri: lettura ed esecuzione 
770 rwxrwx--- Proprietario e gruppo: tutto; altri: nessuno 

 
  6 
Ottale Simbolico Significato 
660 rw-rw---- Proprietario e gruppo: lettura/scrittura 
600 rw------- Solo proprietario: lettura/scrittura 
 
