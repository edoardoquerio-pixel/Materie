# Regressione logistica

## Panoramica
UNITA’ FORMATIVA | Data Analytics and Visualization

## Argomenti trattati
Data Analytics, API REST

---
## Appunti

### Slide 1
DOCENTE | Adriano Gaved
UNITA’ FORMATIVA | Data Analytics and Visualization
ARGOMENTO | Regressione logistica
### Slide 2
Prevedere un risultato Sì / No
Dataset: prestiti.xlsx
### Slide 3
Classificazione: quando l'output non è un numero
Finora abbiamo sempre previsto un valore numerico continuo.
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
### Slide 4
La curva a S — sigmoid
A differenza della retta, la logistica produce sempre un valore tra 0 e 1
Output sempre in [0, 1]
Non è mai negativa né superiore a 1 — è una probabilità.
Forma a S (sigmoid)
Sale lentamente, poi rapidamente al centro, poi si appiattisce di nuovo.
Soglia di decisione
P ≥ 0,5 → Sì. La soglia è modificabile in base al contesto.
Funziona come la multipla: ogni variabile ha il suo coefficiente.
### Slide 5
La formula logistica
z  =  a  +  b₁·reddito  +  b₂·debiti  +  b₃·età
P(Sì)  =  1 / (1 + e⁻ᶻ)
z è il punteggio lineare (come nella regressione multipla). La sigmoid lo trasforma in probabilità.
b₁ > 0: reddito più alto → z aumenta →P(Sì) aumenta
b₂ < 0: debiti più alti → z diminuisce →P(Sì) diminuisce
b₃ > 0: età maggiore → storico più lungo →P(Sì) aumenta lievemente
### Slide 6
Esempio numerico — dataset prestiti.xlsx
Supponiamo di aver ottenuto i seguenti coefficienti:
z = −2.5 + 0.00005·reddito − 0.00006·debiti + 0.02·età
### Slide 7
Valutare il modello — la matrice di confusione
Come capire se il modello funziona bene?
(VP + VN) / totale  = (38+47)/(38+47+6+9) = 85%
Quante previsioni sono corrette in totale
VP / (VP + FP)  =  38/(38+9) = 81%
Tra chi prevediamo Sì, quanti sono davvero Sì
VP / (VP + FN)  =  38/(38+6) = 86%
Tra chi è davvero Sì, quanti prevediamo Sì
### Slide 8
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
### Slide 9
Come funziona il train/test split
Il dataset viene diviso casualmente in due parti prima di fare qualsiasi cosa
Dataset completo — 100 clienti
Training set — 80 clienti (80%)
Il test set non si tocca
I dati di test devono restare nascosti fino alla valutazione finale. Usarli per scegliere i parametri del modello invalida i risultati.
Proporzione tipica: 80/20
80% training, 20% test è la proporzione più comune. Con dataset piccoli (< 100 righe) si può scendere a 70/30.
random_state — cos'è e perché serve

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_Regressione_logistica.md*
