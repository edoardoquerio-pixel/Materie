# Linux Server 03.3 Esercizio-su-utenti-permessi - soluzione

**File:** `Linux Server 03.3 Esercizio-su-utenti-permessi - soluzione.pdf`
**Tipo:** `.pdf`
**Dimensione:** 121.8 KB
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
 
 
Comandi: 
 
 
1. Creazione degli utenti 
bash 
sudo adduser marco 
sudo adduser laura 
sudo adduser simone 
sudo adduser elena 
Il comando adduser chiederà interattivamente la password e le informazioni aggiuntive 
(nome completo, telefono, ecc.). Per le informazioni opzionali puoi premere Invio per 
saltarle. 
 
2. Creazione dei gruppi 
bash 
sudo addgroup fotografi 
sudo addgroup postprod 
sudo addgroup direzione 
 
3. Assegnazione utenti ai gruppi 
bash 
sudo usermod -aG fotografi laura 
sudo usermod -aG fotografi simone 
sudo usermod -aG postprod elena 
sudo usermod -aG direzione marco 
sudo usermod -aG fotografi marco 
sudo usermod -aG postprod marco 
 
4. Creazione della struttura directory 
bash 
sudo mkdir -p /home/studio/raw 
sudo mkdir -p /home/studio/elaborati 

 
  3 
sudo mkdir -p /home/studio/archivio 
 
5. Impostazione proprietari e gruppi delle directory 
bash 
sudo chown marco:direzione /home/studio 
sudo chown marco:fotografi /home/studio/raw 
sudo chown marco:postprod /home/studio/elaborati 
sudo chown marco:direzione /home/studio/archivio 
 
6. Impostazione permessi in modalità ottale 
bash 
sudo chmod 755 /home/studio 
sudo chmod 770 /home/studio/raw 
sudo chmod 770 /home/studio/elaborati 
sudo chmod 750 /home/studio/archivio 
 
7. Creazione dei file 
bash 
sudo touch /home/studio/raw/foto001.raw 
sudo touch /home/studio/elaborati/foto001_edit.jpg 
sudo touch /home/studio/archivio/listino_prezzi.txt 
Impostare proprietari dei file: 
bash 
sudo chown marco:fotografi /home/studio/raw/foto001.raw 
sudo chown marco:postprod /home/studio/elaborati/foto001_edit.jpg  
sudo chown marco:direzione /home/studio/archivio/listino_prezzi.txt  
Impostare permessi dei file: 
bash 
sudo chmod 660 /home/studio/raw/foto001.raw 
sudo chmod 640 /home/studio/elaborati/foto001_edit.jpg 
sudo chmod 600 /home/studio/archivio/listino_prezzi.txt 
 
8. Verifica 
 
Verificare la struttura creata: 

 
  4 
 
bash 
ls -la /home/studio/ 
ls -la /home/studio/raw/ 
ls -la /home/studio/elaborati/ 
ls -la /home/studio/archivio/ 
 
Verificare i gruppi degli utenti: 
bash 
groups marco 
groups laura 
groups simone 
groups elena 
 
Testare l'accesso come simone (può scrivere in raw): 
bash 
su - simone 
touch /home/studio/raw/test_simone.raw 
ls -la /home/studio/raw/ 
exit 
 
Testare l'accesso come elena (NON può accedere a raw): 
bash 
su - elena 
ls /home/studio/raw/    # Dovrebbe dare "Permission denied" 
touch /home/studio/elaborati/test_elena.jpg    # Dovrebbe funzionare  
exit 
 
Testare che elena non possa accedere all'archivio: 
bash 
su - elena 
ls /home/studio/archivio/    # Dovrebbe dare "Permission denied" 
exit 
 
