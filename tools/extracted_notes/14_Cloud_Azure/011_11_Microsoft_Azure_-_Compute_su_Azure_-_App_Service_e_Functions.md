# Lezione 11

Fonte: `11) Microsoft Azure - Compute su Azure - App Service e Functions.pptx`

### Slide 1

DOCENTE

Federico Laurianti

UNITÀ FORMATIVA

Microsoft Azure (100 ore)

ARGOMENTO

Compute su Azure: App Service e Functions (4 ore)

---

### Slide 2

Compute su Azure

App Service e Functions

---

### Slide 3

Dalla VM al servizio gestito

•  con una VM gestisci sistema operativo, patch, runtime e applicazione
•  con App Service porti soprattutto codice e configurazione
•  con Functions porti funzioni che si attivano a evento
•  il cambio di logica è: meno server da gestire, più focus sull'applicazione

---

### Slide 4

App Service: idea base

•  App Service pubblica web app e API senza gestire una VM
•  Azure gestisce OS, runtime, patching e integrazione con la piattaforma
•  tu gestisci codice, configurazione, dominio, scaling e osservabilità
•  è una scelta tipica quando l'app è web o HTTP API

---

### Slide 5

App Service Plan

•  il piano decide dove gira l'app e quante risorse usa
•  più app possono condividere lo stesso piano
•  cambiare piano cambia capacità, costo e funzionalità disponibili
•  l'app è il sito; il piano è la capacità che lo ospita

---

### Slide 6

Web App e API App

Caso

Servizio

sito web o backend HTTP

Web App

API consumata da app o servizi

API App

•  nella pratica entrambe stanno dentro il modello App Service
•  la distinzione aiuta a ragionare sul tipo di applicazione

---

### Slide 7

Deployment slot

•  uno slot è un ambiente parallelo alla produzione
•  esempio: production e staging
•  puoi pubblicare una versione nuova nello slot di test
•  poi fai swap per portarla in produzione con meno rischio

---

### Slide 8

Scaling in App Service

•  Scale up: cambio piano o capacità del piano
•  Scale out: aumento il numero di istanze
•  l'autoscale può reagire a metriche come CPU o richieste
•  il costo segue il piano e le istanze usate

---

### Slide 9

Quando scegliere App Service

•  applicazioni web e API
•  deploy frequenti e gestione semplice
•  integrazione con domini, certificati, log e scaling
•  quando non serve controllare direttamente il sistema operativo

---

### Slide 10

Azure Functions: idea base

•  Azure Functions esegue codice in risposta a un evento
•  una funzione non è una web app intera
•  è un pezzo di logica che parte quando succede qualcosa
•  esempi: richiesta HTTP, messaggio in coda, timer, file caricato

---

### Slide 11

Trigger e binding

Concetto

Significato

Trigger

evento che avvia la funzione

Input binding

dato letto dalla funzione

Output binding

destinazione su cui la funzione scrive

•  la funzione dichiara collegamenti che Azure gestisce per lei

---

### Slide 12

Trigger comuni

Trigger

Esempio

HTTP

API leggera o webhook

Timer

attività pianificata

Queue

elaborare messaggi

Blob

reagire a un file caricato

•  il trigger racconta perché il codice parte

---

### Slide 13

App Service o Functions?

Se devo...

Scelta naturale

tenere online un'app web o API

App Service

reagire a eventi separati

Functions

gestire OS e software specifico

VM

•  non sono livelli migliori o peggiori: rispondono a problemi diversi

---

### Slide 14

Limiti pratici in aula

•  con Azure for Students alcune opzioni possono essere limitate
•  App Service e Functions sono più adatti a demo leggere rispetto ad AKS
•  se un piano o una regione non compare, si verifica prima subscription e disponibilità
•  l'obiettivo è leggere il modello, non forzare ogni creazione

---

### Slide 15

Dove guardare nel portale

•  App Services: web app, piani, deployment slot, scaling
•  App Service plans: capacità condivisa e costo del piano
•  Function App: funzioni, trigger, configurazione
•  Application Insights: log e metriche applicative
•  Cost Management + Billing: costo dei piani e delle risorse

---

### Slide 16

Chiusura del blocco

•  App Service riduce la gestione del server per web app e API
•  Functions esegue codice a evento con trigger e binding
•  rispetto alle VM perdi controllo sull'OS, ma guadagni semplicità operativa
•  il passo successivo è capire dove entrano container e Kubernetes