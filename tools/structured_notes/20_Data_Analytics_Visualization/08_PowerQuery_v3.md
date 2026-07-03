# PowerQuery v3

## Panoramica
UNITA’ FORMATIVA | Data Analytics and Visualization

## Argomenti trattati
Data Analytics

---
## Appunti

### Slide 1
DOCENTE | Adriano Gaved
UNITA’ FORMATIVA | Data Analytics and Visualization
ARGOMENTO | Tidy Data e Power Query
### Slide 2
Ogni variabile deve formare una colonna distinta nel dataset.
Ogni singola osservazione deve formare una riga dedicata.
Ogni tipo di unità osservazionale deve formare una tabella.
Tidy data: Le 3 Regole d'Oro
### Slide 3
Tidy data: Le 3 Regole d'Oro – Regola 3
Esempio: Valori
studente_id | nome | corso_id | corso_nome
1 | Mario | C01 | Matematica
1 | Mario | C02 | Fisica
studente_id | nome
corso_id | corso_nome
C01 | Matematica
studente_id | corso_id
Ogni tipo di unità osservazionale (studenti, corsi, iscrizioni) ha la sua tabella dedicata.
### Slide 4
Efficienza Computazionale: Molti linguaggi (R, Python) sono ottimizzati per operazioni vettoriali su colonne.
Visualizzazione: Strumenti come ggplot2 o Seaborn richiedono dati in formato lungo (long format).
Integrità: Riduce drasticamente la probabilità di errori logici durante il filtraggio o l'aggregazione.
Standardizzazione: Permette di riutilizzare lo stesso codice su dataset diversi ma con la stessa struttura.
Perché la struttura conta?
### Slide 5
Messy (Compatto)
Colonna: Sesso_Età
Valori: "M_25", "F_30", "M_18"
Richiede parsing di stringhe ogni volta che si vuole filtrare per età.
Colonna A: Sesso (M, F)
Colonna B: Età (25, 30, 18)
Permette analisi statistiche dirette (es. età media per sesso).
Variabili Multiple in una Colonna
### Slide 6
Messy data: diritto da un film dell’orrore
### Slide 7
Pulizia dati strutturata e ripetibile
Dataset: 20260708_Risposte_Invito.xlsx
### Slide 8
Cosa succede se il file sorgente cambia il mese prossimo?
Come sapete quali operazioni avete fatto, e in che ordine?
Come collaborate con un collega sullo stesso processo di cleaning?
Cosa fate se vi accorgete di aver sbagliato un passo a metà lavoro?
Problemi del cleaning manuale in Excel
✗  Non ripetibile
✗  Non documentato
✗  Non reversibile
✗  Non collaborativo
### Slide 9
Interfaccia Power Query |  Demo
Come aprire Power Query
Scheda Dati → Recupera dati → Da file → Da cartella di lavoro
Seleziona il foglio 'Originale'
Clic su Trasforma dati (non Carica)
[ Screenshot: Dati → Recupera dati → Da file ]
Elementi chiave dell'interfaccia
Pannello Passaggi applicati
La lista di tutte le trasformazioni — il cuore di PQ
Mostra il risultato dopo ogni passo
Barra della formula
Codice M del passo selezionato
Lista di tutte le query nel file
### Slide 10
La reversibilità
Come funziona l'undo in Power Query
Intestazioni promosso
Tipo modificato
Duplicati rimossi
▲  Selezionato: anteprima mostra i dati a questo punto
Per eliminare un passo:
Clic destro sul passo nel pannello → Elimina
I passi successivi vengono ricalcolati automaticamente
Se i passi successivi dipendono da quello eliminato → errore segnalato chiaramente
[ Screenshot: Pannello Passaggi – clic destro Elimina ]
### Slide 11
Operazioni di cleaning
Dal cleaning manuale a Power Query
Operazione | Excel manuale | Power Query

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 003_PowerQuery_v3.md*
