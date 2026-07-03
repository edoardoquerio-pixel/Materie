# 10_Programmazione_Python

## 📋 Panoramica

Programmazione Python per applicazioni cloud e automazione. Il linguaggio è usato trasversalmente nel corso per scripting, analisi dati (pandas, matplotlib), automazione cloud, e project work.

> ⚠️ **Nessuna cartella `01_Materiale/` presente** — il materiale didattico non è incluso nel repository. La struttura comprende solo `02_Esercizi/` e `03_Progetti/`.

## 📚 Indice degli argomenti (attesi dal syllabus)

### 1. Fondamenti di Python
- Tipi di dato, variabili, operatori
- Strutture di controllo (if, for, while)
- Funzioni, parametri, return, scope
- Type hints (`list[int]`, `-> None`)

### 2. Strutture Dati
- Liste, tuple, dict, set
- List comprehension, slicing
- Iterazione e enumerazione

### 3. File e I/O
- Lettura/scrittura file con `open()` e context manager
- `pathlib.Path` per gestione percorsi

### 4. Moduli e Package
- Organizzazione progetto, `__init__.py`, `if __name__ == "__main__":`
- `pip` e requirements.txt

### 5. Librerie per Cloud/DevOps
- `boto3` (AWS SDK), `azure-*` (Azure SDK), `google-cloud-*` (GCP SDK)
- `docker-py` per container
- `kubernetes` client per K8s
- `paramiko` per SSH automation
- `requests` per API REST

## ⚡ Punti Chiave

- Python è usato **trasversalmente** — scripting, automazione cloud, data analysis
- **Type hints** migliorano manutenibilità e permettono type checking statico
- Preferire **pathlib.Path** a `os.path` per manipolazione path
- Usare **context manager** (`with`) per file e connessioni
- I file di esercizi e progetti sono in `02_Esercizi/` e `03_Progetti/`

## 📎 Risorse Collegate

- **02_Esercizi/**: Esercizi Python
- **03_Progetti/**: Progetti Python
- **Materie collegate**: `20_Data_Analytics_Visualization`, `14_Cloud_Azure`, `17_Container_Docker_Kubernetes`
