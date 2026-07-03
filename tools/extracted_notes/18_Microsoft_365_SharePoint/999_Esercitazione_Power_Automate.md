# Esercitazione Power Automate

Fonte: `Esercitazione Power Automate.docx`

Laboratorio guidato – Power Automate Cloud

Introduzione pratica a trigger, azioni, notifiche, approvazioni e integrazione tra i servizi Microsoft 365 

Informazioni Generali

Obiettivi formativi: Comprendere la logica di base di Power Automate, creare flussi cloud automatizzati, utilizzare contenuti dinamici e implementare condizioni decisionali. 

Prerequisiti: Conoscenza basilare dell'ambiente Microsoft 365. Accesso attivo a Power Automate, SharePoint, Teams, Outlook e Forms. 

Tempo stimato complessivo: 60 - 75 minuti.

Servizi Microsoft 365 utilizzati: Power Automate, SharePoint Online, Office 365 Outlook, Microsoft Teams, Microsoft Forms, Approvals. 

Convenzioni del laboratorio

Durante le esercitazioni, si prega di utilizzare le seguenti nomenclature per mantenere uniformità:

Flusso Esercizio 1: LAB_NotificaFile_NomeCognome

Flusso Esercizio 2: LAB_Approvazione_NomeCognome

Canale Teams: Canale Generale del Team di classe.

Sito SharePoint: Sito del corso creato durante la precedente esercitazione

Lista SharePoint: RichiesteCorso

Modulo Forms: Richiesta materiale didattico

ESERCIZIO 1: Notifica automatica caricamento file in SharePoint

Scenario: È necessario monitorare una specifica cartella condivisa. Quando un utente carica un nuovo documento, il sistema deve avvisare tempestivamente il team interessato e inviare una comunicazione via email al responsabile. 

Obiettivo: Creare un flusso cloud automatizzato lineare che reagisca a un evento su SharePoint e distribuisca l'informazione su più canali (Email e Teams). 

Tempo stimato: 20 minuti.

Risultato atteso:

Al caricamento di un file, il flusso si avvia automaticamente. L'utente designato riceve un'email con il nome e il link del file. Contemporaneamente, nel canale Teams specificato appare un messaggio automatico con i medesimi dettagli. 

[File creato in SharePoint] -> [Email Outlook] -> [Messaggio Teams]

Istruzioni passo-passo

Accedere al portale di Power Automate (make.powerautomate.com) con le proprie credenziali istituzionali. 

Nel menu di navigazione a sinistra, cliccare su Crea e selezionare Flusso cloud automatizzato. 

Assegnare al flusso il nome LAB_NotificaFile_NomeCognome.

Nel campo di ricerca dei trigger, digitare SharePoint e selezionare il trigger When a file is created (properties only) (Quando viene creato un file - solo proprietà). Cliccare su Crea. 

Configurare il trigger SharePoint: 

Indirizzo sito: Selezionare il sito SharePoint del corso dal menu a tendina.

Nome libreria: Selezionare Documenti condivisi (o la libreria indicata dal docente). 

Cartella (opzionale): Cliccare sull'icona della cartella per restringere il monitoraggio a una sottocartella specifica, se richiesto. 

Cliccare su + Nuovo passaggio.

Cercare il connettore Office 365 Outlook e selezionare l'azione Send an email (V2) (Invia un'email V2). 

Configurare l'azione Email: 

A (To): Inserire il proprio indirizzo email per il test.

Oggetto (Subject): Scrivere "Nuovo file caricato: " e, cliccando nel campo, selezionare Nome file con estensione dal pannello dei Contenuti dinamici. 

Corpo (Body): Scrivere un breve messaggio testuale (es. "È stato caricato un nuovo documento. Clicca sul link per aprirlo:") e inserire il contenuto dinamico Collegamento all'elemento (Link to item). 

Cliccare su + Nuovo passaggio.

Cercare il connettore Microsoft Teams e selezionare l'azione Post message in a chat or channel (Pubblica un messaggio in una chat o in un canale). 

Configurare l'azione Teams: 

Pubblica come: Flow bot.

Pubblica in: Channel (Canale).

Team: Selezionare il Team della classe.

Canale: Selezionare Generale.

Messaggio: Comporre un messaggio avvisando del nuovo file e inserire i contenuti dinamici Nome file con estensione e Collegamento all'elemento. 

Nota didattica:

L'uso dei Contenuti dinamici è fondamentale in Power Automate: permette di riutilizzare i dati generati dai passaggi precedenti (in questo caso, le proprietà del file lette dal trigger di SharePoint) all'interno delle azioni successive, rendendo il flusso adattabile a ogni nuovo evento. 

Cliccare su Salva in alto a destra o in basso.

Cliccare su Test (in alto a destra), selezionare Manualmente, cliccare su Test in basso. 

Aprire una nuova scheda del browser, andare nel sito SharePoint configurato al punto 5 e caricare un documento qualsiasi. 

Tornare alla scheda di Power Automate e osservare l'esecuzione del flusso. Verificare poi la ricezione dell'email e la presenza del messaggio in Teams. 

Checklist di verifica - Esercizio 1

Il flusso è stato salvato senza errori di sintassi.

Il caricamento di un file su SharePoint ha fatto partire il flusso con esito "Riuscito".

È stata ricevuta un'email contenente il nome del file e un link funzionante.

Nel canale Teams è apparso un messaggio formattato correttamente inviato dal "Flow bot".

ESERCIZIO 2: Richiesta approvazione da Microsoft Forms

Scenario: Si richiede di compilare un modulo per richiedere del materiale didattico aggiuntivo. La richiesta deve essere approvata da un docente. Se approvata, i dati vengono salvati in un registro e lo studente viene notificato. Se rifiutata, lo studente riceve le motivazioni del rifiuto. 

Obiettivo: Integrare Microsoft Forms, implementare un processo di approvazione umana (Approvals) e gestire una diramazione logica (Condition/Condizione) basata sull'esito dell'approvazione. 

Tempo stimato: 40 minuti.

Risultato atteso:

L'invio di un modulo Forms genera una richiesta di approvazione in Teams/Outlook. A seconda della scelta dell'approvatore (Approva/Rifiuta), il flusso esegue azioni diverse: registra i dati su SharePoint e notifica l'approvazione, oppure invia solo una notifica di rifiuto. 

Preparazione iniziale

Prima di creare il flusso, è necessario predisporre le origini dati:

Creare il Modulo Forms: Accedere a Microsoft Forms e creare un nuovo modulo intitolato Richiesta materiale didattico. Aggiungere le seguenti domande: 

Nome e cognome (Testo)

Email studente (Testo)

Tipo richiesta (Scelta: Slide, Esercizi, Video)

Motivazione (Testo lungo)

Creare la Lista SharePoint: Nel sito SharePoint del corso, creare una nuova Lista vuota intitolata RichiesteCorso. Oltre alla colonna predefinita Title, aggiungere le seguenti colonne (tutte di tipo 'Riga singola di testo', tranne Motivazione): 

Studente

EmailStudente

TipoRichiesta

Motivazione (Più righe di testo)

Stato

Istruzioni passo-passo

In Power Automate, creare un nuovo Flusso cloud automatizzato. Nome: LAB_Approvazione_NomeCognome. 

Cercare il trigger Microsoft Forms e selezionare When a new response is submitted (Quando viene inviata una nuova risposta). Cliccare su Crea. 

Nel trigger, selezionare l'ID modulo corrispondente a Richiesta materiale didattico.

Cliccare + Nuovo passaggio. Cercare nuovamente Microsoft Forms e selezionare Get response details (Ottieni i dettagli della risposta). 

In ID modulo, selezionare di nuovo Richiesta materiale didattico. Nel campo ID Risposta, selezionare il contenuto dinamico ID risposta proveniente dal passaggio precedente. 

Nota didattica:

Il trigger di Forms ci dice solo che qualcuno ha compilato il modulo. L'azione Get response details è obbligatoria per recuperare cosa l'utente ha scritto nelle singole domande. Senza questo passaggio, non avremmo accesso alle risposte da usare nel flusso. 

Cliccare + Nuovo passaggio. Cercare il connettore Approvals e selezionare Start and wait for an approval (Avvia e attendi un'approvazione). 

Configurare l'approvazione: 

Tipo di approvazione: Approve/Reject - First to respond (Approva/Rifiuta - Primo a rispondere). 

Titolo: "Nuova richiesta da " + contenuto dinamico Nome e cognome.

Assegnato a: Inserire il proprio indirizzo email (per testare il ruolo del docente).

Dettagli: Inserire i contenuti dinamici Tipo richiesta e Motivazione per fornire contesto all'approvatore. 

Cliccare + Nuovo passaggio. Selezionare il controllo Condition (Condizione). 

Configurare la condizione logica: 

Nel primo campo a sinistra, inserire il contenuto dinamico Outcome (Esito) proveniente dal passaggio Approvals. 

Selezionare l'operatore is equal to (è uguale a).

Nel campo di destra, digitare esattamente: Approve.

Nel ramo "Se sì" (If yes): 

Aggiungere un'azione SharePoint - Create item (Crea elemento). Selezionare il sito e la lista RichiesteCorso. 

Mappare i campi della lista con i contenuti dinamici di Forms. Nel campo Stato, scrivere manualmente "Approvata". 

Aggiungere un'azione Office 365 Outlook - Send an email (V2). Destinatario: contenuto dinamico Email studente. Oggetto: "Richiesta approvata". 

Aggiungere un'azione Microsoft Teams - Post message in a chat or channel per avvisare il Team dell'avvenuta approvazione. 

Nel ramo "Se no" (If no): 

Aggiungere un'azione Office 365 Outlook - Send an email (V2) per informare lo studente del rifiuto (Destinatario: Email studente). Nel corpo della mail, è possibile includere il contenuto dinamico Responses Comments (Commenti risposta) di Approvals. 

Aggiungere un'azione Microsoft Teams per notificare il rifiuto nel canale.

Salvare e testare il flusso manualmente compilando il modulo Forms due volte: la prima volta approvando la richiesta, la seconda volta rifiutandola, per verificare entrambi i rami della condizione. 

Checklist di verifica - Esercizio 2

Il flusso recupera correttamente le risposte scritte nel modulo Forms.

La richiesta di approvazione viene recapitata correttamente via Teams/Outlook.

Il blocco Condizione instrada correttamente il flusso in base alla scelta (Approve/Reject).

In caso di approvazione, viene creata una nuova riga completa nella lista SharePoint.

Le email di notifica (sia positive che negative) vengono inviate al corretto indirizzo dinamico.

Competenze consolidate al termine del laboratorio

Creazione di workflow cloud automatizzati partendo da zero.

Comprensione del paradigma Trigger/Action.

Utilizzo dei Contenuti Dinamici per passare variabili tra le diverse fasi del processo.

Integrazione nativa tra SharePoint (gestione file/dati), Outlook/Teams (comunicazioni) e Forms (input dati). 

Gestione dei processi di approvazione umana (Human-in-the-loop).

Implementazione di logica condizionale (IF/THEN/ELSE).

Suggerimenti per il test e la risoluzione dei problemi

Verificare le connessioni: Se un'azione non mostra i siti SharePoint o i Team disponibili, verificare che la connessione al servizio (Connections) sia autenticata col proprio account scolastico/aziendale. 

Attenzione ai contenuti dinamici: Assicurarsi di selezionare il contenuto dinamico dal passaggio corretto (ad es., l'email dell'utente di Forms e non l'email di chi ha caricato un file in un passaggio precedente). 

Controllare la cronologia esecuzioni (Run history): Se un flusso fallisce, la cronologia mostra esattamente in quale blocco si è verificato l'errore e fornisce dettagli sul problema (es. campi obbligatori mancanti, permessi negati). 

Stringhe esatte nelle condizioni: Il sistema è sensibile al testo. Se si digita "Approvato" invece di "Approve" nella Condizione (in un ambiente in lingua inglese), il flusso andrà sempre nel ramo 'Se no'. 

Testare ogni scenario: Quando si usano diramazioni (Condizioni), è fondamentale eseguire test multipli per assicurarsi che tutti i percorsi (positivo e negativo) funzionino come previsto. 