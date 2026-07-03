# Google Colab

Fonte: `Google Colab.pptx`

### Slide 1

DOCENTE | Adriano Gaved

UNITA’ FORMATIVA | Data Analytics and Visualization

ARGOMENTO | Google Colab

---

### Slide 2

Google Colab

Scrivere ed eseguire Python nel browser, senza installare nulla

colab.research.google.com

---

### Slide 3

Cos'è Google Colab

Un ambiente di sviluppo Python gratuito che gira nel browser

🌐  Browser-based

Non installi nulla sul tuo computer. Funziona su qualsiasi PC, Mac o Chromebook con Chrome o Firefox.

☁️  Salvataggio su Drive

I notebook si salvano automaticamente su Google Drive. Puoi condividerli come un documento Google.

🆓  Gratuito

GPU e CPU gratuiti forniti da Google. Sufficienti per analisi dati e machine learning di base.

📓  Notebook interattivo

Misto di codice Python eseguibile e testo formattato. Ogni cella può essere eseguita separatamente.

📦  Librerie preinstallate

pandas, numpy, sklearn, matplotlib, seaborn sono già disponibili. Nessun pip install necessario per i casi comuni.

🔗  Collegato a Google

Accede direttamente a Google Drive, Google Sheets e altri servizi Google con una sola riga di codice.

---

### Slide 4

Anatomia di un notebook

Un notebook è composto da celle — ogni cella contiene codice o testo

▶  Cella di codice

import pandas as pd
df = pd.read_excel('prestiti.xlsx')
df.head()

Output:

id   eta   reddito_annuo   debiti_totali   prestito_approvato
0   1    38      45000           12000              Sì

T  Cella di testo (Markdown)

## Analisi esplorativa
Questa sezione calcola le statistiche descrittive
del dataset **prestiti.xlsx**.

Interazioni principali

▶  Esegui cella

Shift + Enter

+ Cella codice

Ctrl + M  B

+ Cella testo

Ctrl + M  M

Elimina cella

Ctrl + M  D

Esegui tutto

Runtime → Esegui tutto

Interrompi

Runtime → Interrompi

---

### Slide 5

Primo utilizzo — creare ed eseguire il primo notebook

1  Apri Colab

Vai su colab.research.google.com
Accedi con il tuo account Google

2  Nuovo notebook

File → Nuovo notebook
Appare un foglio vuoto con una cella di codice

3  Rinomina il file

Clic su 'Untitled0.ipynb' in alto
Scrivi un nome es. 'Analisi_Prestiti'

4  Scrivi il primo codice

Clic sulla cella → scrivi:
print('Ciao Colab!')

5  Esegui la cella

Premi Shift+Enter
L'output appare sotto la cella
Il numero [1] indica l'ordine di esecuzione

6  Salvataggio

Ctrl+S oppure File → Salva
Il file .ipynb è salvato su Google Drive
automaticamente ogni pochi minuti

---

### Slide 6

Esempio — le prime righe di ogni analisi dati

Queste 4 celle sono il punto di partenza standard per qualsiasi dataset:

1  Importa le librerie

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

2  Carica il dataset

df = pd.read_excel('prestiti.xlsx')
print(df.shape)       # (100, 5)
df.head()             # prime 5 righe

3  Statistiche di base

df.describe()         # media, std, min, max
df['prestito_approvato'].value_counts()

4  Primo grafico

df.plot.scatter(x='reddito_annuo', y='debiti_totali',
  c=df['prestito_approvato'].map({'Sì':1,'No':0}),
  colormap='RdYlGn')
plt.show()

---

### Slide 7

Shortcut — tasti utili in Colab

Imparare 8-10 shortcut rende il lavoro nel notebook molto più veloce

Windows / Linux

Mac

(sostituisci Ctrl con ⌘ Cmd)

Shift + Enter

Esegui cella e passa alla successiva

Ctrl + Enter

Esegui cella, resta sulla stessa

Alt + Enter

Esegui cella e inserisci una nuova sotto

Ctrl + M  B

Inserisci cella di codice sotto

Ctrl + M  A

Inserisci cella di codice sopra

Ctrl + M  D

Elimina cella selezionata

Ctrl + M  M

Converti cella in testo (Markdown)

Ctrl + M  Y

Converti cella in codice

Ctrl + S

Salva il notebook

Ctrl + Z

Annulla ultima modifica

Ctrl + /

Commenta/decommenta riga selezionata

Tab

Autocompleta il codice

Shift + Tab

Mostra la documentazione della funzione

Ctrl + F

Cerca nel notebook

Ctrl + M  H

Mostra tutti gli shortcut disponibili

Ctrl + M  .

Interrompi l'esecuzione

---

### Slide 8

Gestione file — caricare dati su Colab

Colab non ha accesso al tuo PC. I file devono essere caricati esplicitamente.

A  Upload manuale (più semplice)

Dal pannello 📁 a sinistra → icona upload → seleziona il file.
Il file è disponibile finché la sessione è attiva.

import pandas as pd
df = pd.read_excel('prestiti.xlsx')
df.head()

⚠  Il file si cancella alla chiusura della sessione

B  Da codice (files.upload)

Fa apparire un pulsante di upload direttamente nell'output della cella.

from google.colab import files
uploaded = files.upload()
import io
df =pd.read_excel(io.BytesIO(uploaded['prestiti.xlsx']))

⚠  Richiede interazione manuale ogni volta

C  Da Google Drive (soluzione stabile)

Monta il Drive e accedi ai file come se fossero in una cartella locale.

from google.colab import drive
drive.mount('/content/drive')
df = pd.read_excel('/content/drive/MyDrive/prestiti.xlsx')

✅  Il file rimane disponibile tra sessioni diverse

---

### Slide 9

Connessione a Google Drive — flusso di lavoro consigliato

Organizza i tuoi progetti con una cartella dedicata su Drive

1  Monta il Drive

from google.colab import drive
drive.mount('/content/drive')

💡  Appare un link: clicca, accedi con Google, copia il codice di autorizzazione e incollalo nella cella.

2  Naviga nella cartella

import os
os.chdir('/content/drive/MyDrive/AnalisiDati')
os.listdir()  # elenca i file nella cartella

💡  Crea su Drive una cartella  AnalisiDati  e mettici i tuoi file .xlsx prima di iniziare.

3  Carica il dataset

import pandas as pd
df = pd.read_excel('prestiti.xlsx')
print(f'{len(df)} righe caricate')

💡  Da questo punto il percorso relativo funziona direttamente. I file rimangono tra sessioni.

4  Salva i risultati

# Salva un DataFrame come Excel su Drive
df_risultati.to_excel('risultati.xlsx', index=False)
print('Salvato su Drive')

💡  Il file appare subito nella cartella Drive e può essere aperto in Excel.

---

### Slide 10

Esercizio — primo notebook su Colab

Crea un nuovo notebook e completa i seguenti passi:

1

Vai su colab.research.google.com, crea un nuovo notebook e rinominalo con il tuo nome

2

Crea una cella di testo con un titolo ## e una breve descrizione di cosa farai

3

Carica il file prestiti.xlsx (upload manuale o da Drive) e visualizza le prime 5 righe con df.head()

4

In una nuova cella, calcola df.describe() e df['prestito_approvato'].value_counts()

5

Crea un grafico scatter: reddito_annuo sull'asse x, debiti_totali sull'asse y, colorato per esito

6

Salva il notebook su Drive e condividi il link con il docente (File → Condividi)

---

### Slide 11

Riepilogo — Google Colab

🌐

Colab è un ambiente Python nel browser: zero installazioni, accessibile da qualsiasi computer

📓

Il notebook è fatto di celle di codice e testo — esegui ogni cella con Shift+Enter

📁

I file si caricano via upload, da codice, o montando Google Drive (soluzione più stabile)

⌨️

10 shortcut base (Shift+Enter, Ctrl+M B, Ctrl+/, Tab…) rendono il lavoro molto più veloce

colab.research.google.com  —  accedi con il tuo account Google, è gratuito