# Regressione logistica

**File:** `Regressione logistica.pptx`
**Tipo:** `.pptx`
**Dimensione:** 100.5 KB
**Ultima modifica:** 02/07/2026 09:24

---

Regressione
Logistica
Prevedere un risultato Sì / No
Dataset: prestiti.xlsx

---

Classificazione: quando l'output non è un numero
Finora abbiamo sempre previsto un valore numerico continuo.
Output
Esempio
Regressione lineare
Numero continuo
Prezzo di un appartamento: €245.000
Regressione logaritmica
Numero continuo
Prezzo al mq dato l'anno: €3.200
Regressione logistica
Sì / No  (0 o 1)
Il prestito viene approvato?
💡  L'idea chiave
La regressione logistica non prevede direttamente Sì o No. Calcola la probabilità (tra 0 e 1) che l'evento accada.
Es: P(approvato) = 0,82 → molto probabile che venga approvato. Sopra una soglia (es. 0,5) → Sì.

---

La curva a S — sigmoid
A differenza della retta, la logistica produce sempre un valore tra 0 e 1
soglia 0,5
P(Sì)
1,0
0,0
Reddito →
❌  Rifiutato
✅  Approvato
Output sempre in [0, 1]
Non è mai negativa né superiore a 1 — è una probabilità.
Forma a S (sigmoid)
Sale lentamente, poi rapidamente al centro, poi si appiattisce di nuovo.
Soglia di decisione
P ≥ 0,5 → Sì. La soglia è modificabile in base al contesto.
Più variabili
Funziona come la multipla: ogni variabile ha il suo coefficiente.

---

La formula logistica
z  =  a  +  b₁·reddito  +  b₂·debiti  +  b₃·età
P(Sì)  =  1 / (1 + e⁻ᶻ)
z è il punteggio lineare (come nella regressione multipla). La sigmoid lo trasforma in probabilità.
b₁
reddito
b₁ > 0: reddito più alto → z aumenta →P(Sì) aumenta
b₂
debiti
b₂ < 0: debiti più alti → z diminuisce →P(Sì) diminuisce
b₃
età
b₃ > 0: età maggiore → storico più lungo →P(Sì) aumenta lievemente

---

Esempio numerico — dataset prestiti.xlsx
Supponiamo di aver ottenuto i seguenti coefficienti:
z = −2.5 + 0.00005·reddito − 0.00006·debiti + 0.02·età
Cliente
Reddito
Debiti
Età
z
P(Sì)
Decisione
A
€65.000
€8.000
45
1.32
0.79
✅ Approvato
B
€28.000
€42.000
31
−1.08
0.25
❌ Rifiutato
C
€45.000
€15.000
38
0.51
0.62
✅ Approvato
D
€22.000
€5.000
55
0.20
0.55
✅ Approvato
E
€50.000
€48.000
29
−0.70
0.33
❌ Rifiutato

---

Valutare il modello — la matrice di confusione
Come capire se il modello funziona bene?
Previsto: Sì
Previsto: No
Reale: Sì
Reale: No
38
Vero Positivo
(VP)
6
Falso Negativo
(FN)
9
Falso Positivo
(FP)
47
Vero Negativo
(VN)
Accuratezza
(VP + VN) / totale  = (38+47)/(38+47+6+9) = 85%
Quante previsioni sono corrette in totale
Precisione
VP / (VP + FP)  =  38/(38+9) = 81%
Tra chi prevediamo Sì, quanti sono davvero Sì
Recall
VP / (VP + FN)  =  38/(38+6) = 86%
Tra chi è davvero Sì, quanti prevediamo Sì

---

Perché dividere i dati in training e test?
Non basta che il modello funzioni bene sui dati che ha già visto
📚  Analogia: l'esame scolastico
Uno studente che memorizza le domande dell'anno scorso può risponderle tutte. Ma sa davvero la materia? Solo un esame con domande nuove lo rivela.
❌  Senza split — valutazione ingannevole
Il modello viene allenato su tutti i 100 clienti.
Viene valutato sugli stessi 100 clienti.

Risultato: accuratezza 95%

Ma il modello ha già visto ogni esempio durante il training. Non sappiamo se generalizza a nuovi clienti reali.

È come interrogare uno studente sulle stesse domande che ha studiato.
✅  Con split — valutazione onesta
80 clienti → training (il modello impara)
20 clienti → test (il modello non li ha mai visti)

Risultato: accuratezza 85% sul test

Questo 85% è una stima realistica di come il modello si comporterà su nuovi clienti in produzione.

È come un esame con domande nuove.

---

Come funziona il train/test split
Il dataset viene diviso casualmente in due parti prima di fare qualsiasi cosa
Dataset completo — 100 clienti
split casuale
Training set — 80 clienti (80%)
Test 20%
Il test set non si tocca
I dati di test devono restare nascosti fino alla valutazione finale. Usarli per scegliere i parametri del modello invalida i risultati.
Proporzione tipica: 80/20
80% training, 20% test è la proporzione più comune. Con dataset piccoli (< 100 righe) si può scendere a 70/30.
random_state — cos'è e perché serve
Lo split è casuale: ogni esecuzione sceglie 20 clienti diversi per il test.

random_state=42 blocca il generatore casuale su un valore fisso → il risultato è sempre lo stesso per tutti.

Il valore 42 non ha significato speciale: qualsiasi intero funziona. È una convenzione della comunità Python.

---

Regressione logistica in Python — Google Colab
1  Carica il dataset
import pandas as pd
df = pd.read_excel('prestiti.xlsx')
df.head()
2  Prepara le variabili
X = df[['eta','reddito_annuo',
        'debiti_totali']]
y = (df['prestito_approvato']=='Sì')
    .astype(int)
3  Split train / test
from sklearn.model_selection import
  train_test_split
X_tr,X_te,y_tr,y_te = train_test_split(
  X, y, test_size=0.2,
  random_state=42)
4  Allena il modello
from sklearn.linear_model import
  LogisticRegression
model = LogisticRegression()
model.fit(X_tr, y_tr)
5  Valuta le performance
from sklearn.metrics import
  accuracy_score, confusion_matrix
print(accuracy_score(y_te, model.predict(X_te)))
print(confusion_matrix(y_te, model.predict(X_te)))
6  Fai una previsione
nuovo = pd.DataFrame([[38, 45000, 15000]], columns=['eta', 'reddito_annuo', 'debiti_totali’])

prob = model.predict_proba(nuovo)[0][1]
print(f'P(approvato) = {prob:.2f}')

---

Esercizio  ·  prestiti.xlsx
100 clienti: età, reddito annuo, debiti totali, esito della richiesta di prestito.
1
Esplora il dataset: quanti prestiti sono stati approvati? Qual è il reddito medio degli approvati vs rifiutati?
2
Su Google Colab: carica il file, prepara X e y, esegui il train/test split (80/20)
3
Allena un modello LogisticRegression. Qual è l'accuratezza sul test set?
4
Stampa la matrice di confusione. Quanti falsi positivi e falsi negativi ci sono?
5
Stima la probabilità di approvazione per un cliente di 40 anni, reddito €50.000, debiti €12.000

---

Riepilogo — regressione logistica
🎯
La regressione logistica prevede la probabilità di un evento binario (Sì/No, 0/1)
📐
z è calcolato come nella regressione multipla; la sigmoid trasforma z in una probabilità tra 0 e 1
⚖️
La soglia di decisione (es. 0,5) converte la probabilità in una classe: sopra → Sì, sotto → No
📊
La matrice di confusione mostra VP, VN, FP, FN — accuratezza da sola non basta
Lineare: prevede un numero  ·  Logaritmica: relazione curva  ·  Multipla: più variabili  ·  Logistica: prevede Sì/No
