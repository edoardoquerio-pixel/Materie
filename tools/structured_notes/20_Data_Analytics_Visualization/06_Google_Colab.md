# Google Colab

## Panoramica
UNITA’ FORMATIVA | Data Analytics and Visualization

## Argomenti trattati
Data Analytics, API REST, Linux

---
## Appunti

### Slide 1
DOCENTE | Adriano Gaved
UNITA’ FORMATIVA | Data Analytics and Visualization
ARGOMENTO | Google Colab
### Slide 2
Scrivere ed eseguire Python nel browser, senza installare nulla
colab.research.google.com
### Slide 3
Cos'è Google Colab
Un ambiente di sviluppo Python gratuito che gira nel browser
🌐  Browser-based
Non installi nulla sul tuo computer. Funziona su qualsiasi PC, Mac o Chromebook con Chrome o Firefox.
☁️  Salvataggio su Drive
I notebook si salvano automaticamente su Google Drive. Puoi condividerli come un documento Google.
GPU e CPU gratuiti forniti da Google. Sufficienti per analisi dati e machine learning di base.
📓  Notebook interattivo
Misto di codice Python eseguibile e testo formattato. Ogni cella può essere eseguita separatamente.
📦  Librerie preinstallate
pandas, numpy, sklearn, matplotlib, seaborn sono già disponibili. Nessun pip install necessario per i casi comuni.
🔗  Collegato a Google
Accede direttamente a Google Drive, Google Sheets e altri servizi Google con una sola riga di codice.
### Slide 4
Anatomia di un notebook
Un notebook è composto da celle — ogni cella contiene codice o testo
▶  Cella di codice
import pandas as pd
df = pd.read_excel('prestiti.xlsx')
id   eta   reddito_annuo   debiti_totali   prestito_approvato
0   1    38      45000           12000              Sì
T  Cella di testo (Markdown)
## Analisi esplorativa
Questa sezione calcola le statistiche descrittive
del dataset **prestiti.xlsx**.
Interazioni principali
▶  Esegui cella
Runtime → Esegui tutto
Runtime → Interrompi
### Slide 5
Primo utilizzo — creare ed eseguire il primo notebook
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
Ctrl+S oppure File → Salva
Il file .ipynb è salvato su Google Drive
automaticamente ogni pochi minuti
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
### Slide 7
Shortcut — tasti utili in Colab
Imparare 8-10 shortcut rende il lavoro nel notebook molto più veloce
Windows / Linux
(sostituisci Ctrl con ⌘ Cmd)

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_Google_Colab.md*
