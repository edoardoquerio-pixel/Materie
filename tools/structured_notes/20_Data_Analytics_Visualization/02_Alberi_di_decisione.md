# Alberi di decisione

## Panoramica
UNITA’ FORMATIVA | Data Analytics and Visualization

## Argomenti trattati
Data Analytics, API REST

---
## Appunti

### Slide 1
DOCENTE | Adriano Gaved
UNITA’ FORMATIVA | Data Analytics and Visualization
ARGOMENTO | Albero di decisione
### Slide 2
Classificare con una sequenza di domande Sì / No
Dataset: prestiti.xlsx
### Slide 3
Come funziona un albero di decisione
Un albero pone una serie di domande sui dati per arrivare a una classificazione
debiti_totali > 30.000?
reddito > 40.000?
### Slide 4
Concetti chiave dell'albero di decisione
La prima domanda — la variabile che divide meglio i dati. L'algoritmo la sceglie automaticamente in base all'indice di Gini o all'entropia.
Ogni domanda successiva su una variabile. Ogni nodo divide i dati in due (o più) rami finché non si raggiunge una foglia.
Il nodo terminale: contiene la classe predetta (es. Approvato / Rifiutato). Non ci sono più domande da porre.
Profondità (depth)
Numero di livelli dell'albero. Alberi profondi imparano bene i dati di training ma rischiano l'overfitting.
L'albero memorizza i dati di training anziché generalizzare. Si controlla limitando la profondità massima (max_depth).
Misura l'impurità di un nodo: 0 = perfettamente puro (una sola classe), 0.5 = massima mescolanza. L'algoritmo minimizza il Gini.
### Slide 5
Albero di decisione vs Regressione logistica
Due approcci diversi allo stesso problema di classificazione
Albero di decisione
Regressione logistica
Classe diretta (Sì/No)
Probabilità → soglia → Sì/No
Interpretabilità
Alta: si legge come flowchart
Media: coefficienti da interpretare
Non lineari, regole nette
Lineari nel log-odds
Rischio alto senza potatura
Variabili categ.
Gestite nativamente
Richiedono encoding
Spiegare decisioni a non tecnici
Quando serve una probabilità calibrata
### Slide 6
Esempio — classificare 5 clienti con l'albero
Regole dell'albero (semplificate):
SE debiti > 30.000  →  SE età > 50  →  Approvato  |  altrimenti Rifiutato
SE debiti ≤ 30.000  →  SE reddito > 40.000  →  Approvato  |  altrimenti Rifiutato
Regola applicata
debiti≤30k → reddito>40k → ✅
debiti>30k → età≤50 → ❌
debiti≤30k → reddito>40k → ✅
debiti≤30k → reddito≤40k → ❌
debiti>30k → età>50 → ✅
### Slide 7
Albero di decisione in Python — Google Colab
1  Carica e prepara
import pandas as pd
df = pd.read_excel('prestiti.xlsx')
X = df[['eta','reddito_annuo','debiti_totali']]
y = (df['prestito_approvato']=='Sì').astype(int)
2  Split train / test
from sklearn.model_selection import train_test_split
X_tr,X_te,y_tr,y_te = train_test_split(
X, y, test_size=0.2, random_state=42)
3  Allena l'albero
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(
max_depth=3, random_state=42)
model.fit(X_tr, y_tr)
from sklearn.metrics import (
accuracy_score, confusion_matrix)
print(accuracy_score(y_te, model.predict(X_te)))
print(confusion_matrix(y_te, model.predict(X_te)))
5  Visualizza l'albero
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
fig,ax = plt.subplots(figsize=(12,5))
plot_tree(model, feature_names=X.columns,
class_names=['No','Sì'], filled=True, ax=ax)
6  Importanza variabili
import pandas as pd
model.feature_importances_,
index=X.columns

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_Alberi_di_decisione.md*
