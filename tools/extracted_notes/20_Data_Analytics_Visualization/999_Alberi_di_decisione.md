# Alberi di decisione

Fonte: `Alberi di decisione.pptx`

### Slide 1

DOCENTE | Adriano Gaved

UNITA’ FORMATIVA | Data Analytics and Visualization

ARGOMENTO | Albero di decisione

---

### Slide 2

Albero di
Decisione

Classificare con una sequenza di domande Sì / No

Dataset: prestiti.xlsx

---

### Slide 3

Come funziona un albero di decisione

Un albero pone una serie di domande sui dati per arrivare a una classificazione

debiti_totali > 30.000?

reddito > 40.000?

età > 50?

No

Sì

✅ Approvato

Sì

❌ Rifiutato

No

✅ Approvato

Sì

❌ Rifiutato

No

Nodo radice

Nodo interno

Foglie

---

### Slide 4

Concetti chiave dell'albero di decisione

Nodo radice

La prima domanda — la variabile che divide meglio i dati. L'algoritmo la sceglie automaticamente in base all'indice di Gini o all'entropia.

Nodi interni

Ogni domanda successiva su una variabile. Ogni nodo divide i dati in due (o più) rami finché non si raggiunge una foglia.

Foglie

Il nodo terminale: contiene la classe predetta (es. Approvato / Rifiutato). Non ci sono più domande da porre.

Profondità (depth)

Numero di livelli dell'albero. Alberi profondi imparano bene i dati di training ma rischiano l'overfitting.

Overfitting

L'albero memorizza i dati di training anziché generalizzare. Si controlla limitando la profondità massima (max_depth).

Indice di Gini

Misura l'impurità di un nodo: 0 = perfettamente puro (una sola classe), 0.5 = massima mescolanza. L'algoritmo minimizza il Gini.

---

### Slide 5

Albero di decisione vs Regressione logistica

Due approcci diversi allo stesso problema di classificazione

Albero di decisione

Regressione logistica

Output

Classe diretta (Sì/No)

Probabilità → soglia → Sì/No

Interpretabilità

Alta: si legge come flowchart

Media: coefficienti da interpretare

Relazioni

Non lineari, regole nette

Lineari nel log-odds

Overfitting

Rischio alto senza potatura

Rischio basso

Variabili categ.

Gestite nativamente

Richiedono encoding

Quando usarlo

Spiegare decisioni a non tecnici

Quando serve una probabilità calibrata

---

### Slide 6

Esempio — classificare 5 clienti con l'albero

Regole dell'albero (semplificate):

SE debiti > 30.000  →  SE età > 50  →  Approvato  |  altrimenti Rifiutato
SE debiti ≤ 30.000  →  SE reddito > 40.000  →  Approvato  |  altrimenti Rifiutato

Cliente

Reddito

Debiti

Età

Regola applicata

Previsione

A

€65.000

€8.000

45

debiti≤30k → reddito>40k → ✅

✅ Approvato

B

€28.000

€42.000

31

debiti>30k → età≤50 → ❌

❌ Rifiutato

C

€45.000

€15.000

38

debiti≤30k → reddito>40k → ✅

✅ Approvato

D

€22.000

€5.000

55

debiti≤30k → reddito≤40k → ❌

❌ Rifiutato

E

€50.000

€48.000

55

debiti>30k → età>50 → ✅

✅ Approvato

---

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

4  Valuta

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
plt.show()

6  Importanza variabili

import pandas as pd
pd.Series(
  model.feature_importances_,
  index=X.columns
).sort_values().plot.barh()
plt.title('Importanza variabili')

---

### Slide 8

Il rischio principale — overfitting

Un albero troppo profondo impara a memoria i dati di training, ma sbaglia sui nuovi dati

max_depth = 1

Accuratezza training:

65%

Accuratezza test:

63%

Underfitting: troppo semplice. Una sola domanda non basta per separare le classi.

max_depth = 3

Accuratezza training:

84%

Accuratezza test:

82%

Bilanciato: buona generalizzazione. L'albero cattura le relazioni principali senza memorizzare.

max_depth = None

Accuratezza training:

100%

Accuratezza test:

71%

Overfitting: perfetto sul training, pessimo sul test. L'albero ha memorizzato ogni esempio.

💡  Regola pratica: inizia con max_depth=3, poi aumenta di 1 finché l'accuratezza sul test smette di migliorare.

---

### Slide 9

Importanza delle variabili — cosa conta di più?

L'albero di decisione calcola automaticamente quanto ogni variabile contribuisce alle previsioni

debiti_totali

52%

reddito_annuo

34%

eta

14%

debiti_totali (52%) — La variabile più discriminante: livello di indebitamento è il fattore principale nella decisione.

reddito_annuo (34%) — Secondo fattore: il reddito determina la capacità di rimborso.

età (14%) — Contributo minore: l'età agisce come fattore di contesto, non determinante.

---

### Slide 10

Esercizio  ·  prestiti.xlsx

Usa il dataset già noto: 100 clienti, 3 variabili, esito approvazione.

1

Su Colab: carica prestiti.xlsx, prepara X e y, esegui il train/test split (80/20, random_state=42)

2

Allena un DecisionTreeClassifier con max_depth=3. Qual è l'accuratezza sul test set?

3

Visualizza l'albero con plot_tree. Quale variabile è alla radice? Corrisponde a quella con importanza più alta?

4

Allena un secondo albero senza limitare la profondità. Confronta l'accuratezza su training e test. Cosa osservi?

5

Stampa la matrice di confusione per entrambi gli alberi. Quale ha meno falsi negativi?

---

### Slide 11

Riepilogo — albero di decisione

🌳

L'albero classifica ponendo domande sequenziali sulle variabili: ogni nodo divide i dati in rami

👁️

È il classificatore più interpretabile: la logica di ogni previsione è leggibile come un diagramma di flusso

⚠️

Senza limitare la profondità (max_depth) l'albero memorizza il training set — verifica sempre l'accuratezza sul test

📊

feature_importances_ mostra quanto conta ogni variabile: utile per capire cosa guida le decisioni

Logistica: probabilità  ·  Albero: regole leggibili  ·  Entrambi: matrice di confusione per valutare