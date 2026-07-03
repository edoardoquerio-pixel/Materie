# README

**File:** `README.md`
**Tipo:** `.md`
**Dimensione:** 0.8 KB
**Ultima modifica:** 15/06/2026 12:46

---

Viene allestito un ambiente per arrivare a provare una versione didattica semplificata di IaC, usando OpenTofu e Docker.

## Ambiente
Installare/verificare il SW necessario.  

'OpenTofu'  

Da PowerShell:  
~$ winget install --exact --id=OpenTofu.Tofu  

Chiudere e riaprire PowerShell:  
~$ tofu version  

'Docker' gia installato  

## Esecuzione
Clonare il repository in locale.

Struttura del progetto:  

WSA-lab/  
│  
├─ app/  
│  ├─ main.py  
│  └─ requirements.txt  
│  
├─ Dockerfile  
├─ main.tf  
└─ outputs.tf  

In questa fase si lancia l’app main.py con OpenTofu.  
Spostarsi nella cartella WSA-lab, eseguire i comandi:  
~$ tofu init  
~$ tofu plan  
~$ tofu apply  

Per terminare l'infrastruttura:  
~$ tofu destroy

