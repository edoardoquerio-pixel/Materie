# Linux Server 03.4 Esercizio-su-utenti-permessi - soluzione

## Panoramica
Per ogni utente, adduser chiederà la password e le informazioni opzionali (premi Invio per

## Argomenti trattati
Linux

---
## Appunti

Wolfgang Cecchin
UNITA’ FORMATIVA
Esercizio su utenti e permessi
Soluzione - Comandi
1. Creazione degli utenti
sudo adduser giulia
sudo adduser andrea
sudo adduser chiara
sudo adduser luca
sudo adduser sara
Per ogni utente, adduser chiederà la password e le informazioni opzionali (premi Invio per
2. Creazione dei gruppi
sudo addgroup scrittori
sudo addgroup editing
sudo addgroup grafica
sudo addgroup amministrazione
3. Assegnazione utenti ai gruppi
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
sudo mkdir -p /home/casaeditrice/manoscritti
sudo mkdir -p /home/casaeditrice/bozze
sudo mkdir -p /home/casaeditrice/grafica/copertine
sudo mkdir -p /home/casaeditrice/grafica/impaginazione
sudo mkdir -p /home/casaeditrice/amministrazione
5. Impostazione proprietari e gruppi delle directory
sudo chown giulia:amministrazione /home/casaeditrice
sudo chown giulia:scrittori /home/casaeditrice/manoscritti
sudo chown giulia:editing /home/casaeditrice/bozze
sudo chown giulia:grafica /home/casaeditrice/grafica
sudo chown giulia:grafica /home/casaeditrice/grafica/copertine
sudo chown giulia:grafica /home/casaeditrice/grafica/impaginazione
sudo chown giulia:amministrazione /home/casaeditrice/amministrazione
6. Impostazione permessi in modalità ottale
sudo chmod 755 /home/casaeditrice
sudo chmod 770 /home/casaeditrice/manoscritti
sudo chmod 770 /home/casaeditrice/bozze
sudo chmod 770 /home/casaeditrice/grafica
sudo chmod 770 /home/casaeditrice/grafica/copertine
sudo chmod 770 /home/casaeditrice/grafica/impaginazione
sudo chmod 700 /home/casaeditrice/amministrazione
7. Creazione dei file
sudo touch /home/casaeditrice/manoscritti/romanzo_capitolo1.txt
sudo touch /home/casaeditrice/bozze/romanzo_corretto.txt
sudo touch /home/casaeditrice/grafica/copertine/bozza_copertina.png
sudo touch /home/casaeditrice/amministrazione/contratti.txt
Impostare proprietari dei file:
sudo chown giulia:scrittori /home/casaeditrice/manoscritti/romanzo_capitolo1.txt
sudo chown giulia:editing /home/casaeditrice/bozze/romanzo_corretto.txt
sudo chown giulia:grafica /home/casaeditrice/grafica/copertine/bozza_copertina.png
sudo chown giulia:amministrazione /home/casaeditrice/amministrazione/contratti.txt
Impostare permessi dei file:
sudo chmod 660 /home/casaeditrice/manoscritti/romanzo_capitolo1.txt
sudo chmod 660 /home/casaeditrice/bozze/romanzo_corretto.txt
sudo chmod 660 /home/casaeditrice/grafica/copertine/bozza_copertina.png
sudo chmod 600 /home/casaeditrice/amministrazione/contratti.txt
8. Comandi di verifica
Verificare la struttura creata:
ls -la /home/casaeditrice/
ls -la /home/casaeditrice/manoscritti/
ls -la /home/casaeditrice/bozze/
ls -la /home/casaeditrice/grafica/
ls -la /home/casaeditrice/grafica/copertine/
ls -la /home/casaeditrice/amministrazione/
Verificare i gruppi degli utenti:
Test accesso come andrea (scrittore):
touch /home/casaeditrice/manoscritti/nuovo_capitolo.txt # Deve funzionare
ls /home/casaeditrice/bozze/ # Permission denied
ls /home/casaeditrice/amministrazione/ # Permission denied
Test accesso come luca (editor):
cat /home/casaeditrice/manoscritti/romanzo_capitolo1.txt # Deve funzionare (è nel
gruppo scrittori)
touch /home/casaeditrice/bozze/nuova_correzione.txt # Deve funzionare

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 003_Linux_Server_03_4_Esercizio-su-utenti-permessi_-_soluzione.md*
