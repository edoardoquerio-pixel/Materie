# Linux Server 03.3 Esercizio-su-utenti-permessi - soluzione

## Panoramica
Il comando adduser chiederà interattivamente la password e le informazioni aggiuntive

## Argomenti trattati
Linux

---
## Appunti

Wolfgang Cecchin
UNITA’ FORMATIVA
Esercizio su utenti e permessi
1. Creazione degli utenti
sudo adduser marco
sudo adduser laura
sudo adduser simone
sudo adduser elena
Il comando adduser chiederà interattivamente la password e le informazioni aggiuntive
(nome completo, telefono, ecc.). Per le informazioni opzionali puoi premere Invio per
2. Creazione dei gruppi
sudo addgroup fotografi
sudo addgroup postprod
sudo addgroup direzione
3. Assegnazione utenti ai gruppi
sudo usermod -aG fotografi laura
sudo usermod -aG fotografi simone
sudo usermod -aG postprod elena
sudo usermod -aG direzione marco
sudo usermod -aG fotografi marco
sudo usermod -aG postprod marco
4. Creazione della struttura directory
sudo mkdir -p /home/studio/raw
sudo mkdir -p /home/studio/elaborati
sudo mkdir -p /home/studio/archivio
5. Impostazione proprietari e gruppi delle directory
sudo chown marco:direzione /home/studio
sudo chown marco:fotografi /home/studio/raw
sudo chown marco:postprod /home/studio/elaborati
sudo chown marco:direzione /home/studio/archivio
6. Impostazione permessi in modalità ottale
sudo chmod 755 /home/studio
sudo chmod 770 /home/studio/raw
sudo chmod 770 /home/studio/elaborati
sudo chmod 750 /home/studio/archivio
7. Creazione dei file
sudo touch /home/studio/raw/foto001.raw
sudo touch /home/studio/elaborati/foto001_edit.jpg
sudo touch /home/studio/archivio/listino_prezzi.txt
Impostare proprietari dei file:
sudo chown marco:fotografi /home/studio/raw/foto001.raw
sudo chown marco:postprod /home/studio/elaborati/foto001_edit.jpg
sudo chown marco:direzione /home/studio/archivio/listino_prezzi.txt
Impostare permessi dei file:
sudo chmod 660 /home/studio/raw/foto001.raw
sudo chmod 640 /home/studio/elaborati/foto001_edit.jpg
sudo chmod 600 /home/studio/archivio/listino_prezzi.txt
Verificare la struttura creata:
ls -la /home/studio/
ls -la /home/studio/raw/
ls -la /home/studio/elaborati/
ls -la /home/studio/archivio/
Verificare i gruppi degli utenti:
Testare l'accesso come simone (può scrivere in raw):
touch /home/studio/raw/test_simone.raw
ls -la /home/studio/raw/
Testare l'accesso come elena (NON può accedere a raw):
ls /home/studio/raw/ # Dovrebbe dare "Permission denied"
touch /home/studio/elaborati/test_elena.jpg # Dovrebbe funzionare
Testare che elena non possa accedere all'archivio:
ls /home/studio/archivio/ # Dovrebbe dare "Permission denied"

---
*Fonte: 003_Linux_Server_03_3_Esercizio-su-utenti-permessi_-_soluzione.md*
