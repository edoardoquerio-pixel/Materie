# sharepoint_online_administration_Modulo 3 (1)

**File:** `sharepoint_online_administration_Modulo 3 (1).pptx`
**Tipo:** `.pptx`
**Dimensione:** 1387.0 KB
**Ultima modifica:** 26/06/2026 10:04

---

Identifica Contenuti
Individua le cartelle o le librerie specifiche che contengono dati sensibili e richiedono protezione o restrizioni di accesso speciali.
1
Gestione Gruppi
Utilizza i gruppi standard (Visitatori, Membri, Proprietari) per mappare i livelli di accesso: Lettura, Modifica, Controllo completo.
2
Interrompi Ereditarietà
Nelle impostazioni avanzate dei permessi, interrompi l'ereditarietà dal sito padre solo per gli elementi che necessitano eccezioni.
3
Verifica Accesso
Usa la funzione "Controlla autorizzazioni" o accedi con un utente di test per garantire il rispetto del principio del privilegio minimo.
4
Esercitazione Guidata 5
Configurare Permessi e Gruppi
Tempo Stimato: 15 Minuti

---

Apri/Crea Team
Apri Microsoft Teams e seleziona un Team esistente o creane uno nuovo assicurandoti che sia collegato al tuo sito SharePoint.
1
Aggiungi Scheda
Nel canale Generale, clicca su "+" e aggiungi una scheda "Document Library" (SharePoint). Seleziona la libreria del sito.
2
Sposta File
Prendi un file dalla tua chat privata o OneDrive e spostalo (o copialo) nella scheda File del canale appena configurato.
3
Verifica & Test
Apri il file contemporaneamente con un collega per testare il co-authoring in tempo reale e controlla la cronologia versioni.
4
ESERCITAZIONE GUIDATA 6
Collegare SharePoint a Teams
Tempo stimato: 15 min

---

Per continuare a studiare
Risorse e Approfondimenti
Link utili
Microsoft Learn
Percorsi di apprendimento guidati gratuiti su SharePoint, Teams e OneDrive per ogni livello.
Documentazione Ufficiale
Guide tecniche dettagliate su governance, permessi, sicurezza e configurazione avanzata.
Community PnP
Esempi di codice, webpart open-source e best practices dalla community Patterns & Practices.
Video Tutorial
Canale YouTube Microsoft 365 e sessioni registrate dalle conferenze Ignite e Build.
Strumenti PnP
Risorse pratiche come l'Adoption Kit e script di automazione per amministratori.
Roadmap M365
Resta aggiornato sulle nuove funzionalità in arrivo e sugli sviluppi futuri della piattaforma.

---

File dei Canali
Quando carichi un file nella tab "File" di un canale Teams, in realtà lo stai salvando in una Cartella della Libreria Documenti del sito SharePoint collegato.
Permessi Unificati
Aggiungi un membro al Team? Accesso automatico al sito SharePoint. Rimuovi un membro? Accesso revocato. I Gruppi M365 gestiscono tutto.
 1 Team = 1 Sito 
Teams
 Interfaccia di chat
 Canali & Tab
 Meeting & Call
SharePoint
 Storage dei File
 Motore Permessi
 Pagine & Liste
Architecture Overview
Teams & SharePoint: Come Lavorano Insieme
Integrazione Profonda

---

Proprietà del Mittente
Il file risiede fisicamente nel OneDrive for Business della persona che lo ha caricato.
Cartella Automatica
Viene creato automaticamente nella cartella Microsoft Teams Chat Files.
Accesso Privato
Non visibile all'intera organizzazione, ma solo agli utenti specifici della chat.
Dove vengono salvati?
Spazio personale del mittente
 Ideale per bozze rapide e file non definitivi
Solo i Partecipanti
I permessi vengono concessi automaticamente solo ai membri presenti nella conversazione.
Rischio "Utente Uscente"
Se il mittente lascia l'azienda e il suo OneDrive viene chiuso, il file diventa inaccessibile.
Spostamento Necessario
Per documenti ufficiali del progetto, il file va spostato manualmente in SharePoint.
Chi può accedere?
Gestione permessi e rischi
 Attenzione: Evitare per documenti a lungo termine
Collaborazione in Teams
File Inviati in Chat (Privata e Gruppo)
Architettura 1:1

---

Un Canale = Una Cartella
Ogni canale creato in Microsoft Teams genera automaticamente una cartella corrispondente nella libreria "Documenti" del sito SharePoint.
Permessi Sincronizzati
I permessi sono allineati automaticamente ai membri del Team. Chi viene aggiunto al Team accede immediatamente a tutti i file dei canali.
Accesso Flessibile
Accedi ai file dalla tab "File" in Teams per velocità o dal sito SharePoint per funzionalità avanzate di gestione documentale.
Integrazione Teams & SharePoint
File dei Canali
Struttura Automatica
Team Marketing - Documenti
 Nuovo
 Carica
 Sincronizza
 Apri in SharePoint
Nome
Stato
Modificato da
General
Attivo
Sistema
Campagna Estiva 2024
2 ore fa
M
Analisi Mercato
Ieri
L
Social Media Planning
3 giorni fa
G
Linee Guida Team.pdf
Settimana scorsa
Admin

---

Modifica nel Browser
Apri e modifica documenti Word, Excel e PowerPoint direttamente dal browser senza installare software desktop.
Salvataggio & Versioni
Salvataggio automatico istantaneo. Accedi alla cronologia per ripristinare versioni precedenti in caso di errori.
Co-authoring Fluido
Collabora con il team sullo stesso file in tempo reale senza blocchi. Vedi chi sta modificando e dove.
Produttività nel Browser
Lavorare con Office Online
Web Apps

---

Ecosistema Connesso
Integrazione con Microsoft 365 Apps
Productivity Suite

---

Un file condiviso in chat serve ora a tutto il team. Cosa fai?
 Scenario Pratico
A
Lo lasci in chat
Lo sposti in SharePoint (canale)
C
Lo invii per email a tutti
B

---

Caso Studio Pratico
Scenario Reale: Team Marketing
Marketing & Comunicazione

---

Scenario Reale Aziendale
Team HR & People Operations
Human Resources

---

1. Team Site
Crea un nuovo Team Site moderno.
Assegna un titolo e una descrizione chiara.
Aggiungi almeno un altro studente come membro.
Base Struttura
2. Libreria Documenti
Crea una nuova libreria (non usare quella di default).
Aggiungi 3 colonne metadati (es. Stato, Tipo, Cliente).
Crea 2 viste pubbliche personalizzate.
Gestione File
3. Lista con Form
Crea una lista per tracciare attività o inventario.
Configura il form di inserimento (ordine campi, campi obbligatori).
Inserisci almeno 5 elementi di prova.
Dati Strutturati
4. Home Page
Personalizza la pagina Home del sito.
Usa Webpart: Notizie, Link Rapidi e la Libreria creata.
Rendi il layout visivamente accattivante.
Presentazione
5. Permessi
Verifica i gruppi di default (Owners, Members, Visitors).
Crea una cartella o lista con permessi unici (interrompi ereditarietà).
Sicurezza
6. Teams
Collega il sito a un Team Microsoft Teams.
Aggiungi una Tab nel canale Generale che punta alla tua Lista o Pagina Home.
Integrazione
Mettiamo in pratica
Mini Progetto Finale
Checklist Deliverable

---

Verifica delle Competenze
Quiz Finale: Mettiti alla Prova
10 Domande
1
Qual è lo scopo principale di un Team Site?
2
Perché usare i Metadati invece delle Cartelle?
3
A cosa servono le Viste Personalizzate in una libreria?
4
Cosa comporta l'interruzione dell'ereditarietà dei permessi?
5
Qual è la funzione principale del Versioning?
6
Quando è preferibile usare una Lista invece di Excel?
7
Dove vengono salvati i file condivisi in una Chat di Teams?
8
E i file condivisi in un Canale di Teams?
9
Quali sono le Webpart più utili per una Home Page?
10
Qual è la regola d'oro per la gestione dei permessi?
Siti
Documenti
Documenti
Permessi
Sicurezza
Liste
Integrazione
Integrazione
Pagine
Best Practice
Favorire la collaborazione del team tramite condivisione di file, liste, attività e comunicazioni in un unico spazio
Per classificare, filtrare e ricercare i documenti in modo più efficace, evitando strutture di cartelle troppo profonde.
A mostrare i documenti in modi diversi (filtri, raggruppamenti, ordinamenti) in base alle esigenze dell’utente o del team.
La libreria/cartella/documento ottiene permessi propri, separati dal sito padre; vanno gestiti manualmente.
Tenere traccia delle versioni dei documenti, permettendo ripristini e controllo delle modifiche.
Quando serve collaborazione in tempo reale, gestione di campi strutturati, permessi, automazioni e integrazione con SharePoint/Power Automate.
Nella libreria “Documenti” del Team SharePoint, nella cartella del relativo canale.
Concedere l’accesso al livello più alto possibile e creare eccezioni solo quando strettamente necessario.
Pronti a rispondere?
Analizziamo le risposte insieme
Hero, Notizie, Documenti, Link veloci, Agenda/Calendario, Attività, People, Elenchi.
Nel OneDrive della persona che li invia, in una cartella dedicata alla chat.

---

Riepilogo Modulo
Cosa hai imparato
Competenze Acquisite
Obiettivi Raggiunti
Pronto per amministrare SharePoint.
Hai acquisito le competenze fondamentali per creare, organizzare e gestire spazi di lavoro digitali moderni, migliorando la collaborazione del tuo team.
Gestione Siti
Creare Team Site e Communication Site, comprendendo la differenza e quando usarli.
Architettura Documentale
Sostituire le cartelle profonde con metadati, colonne personalizzate e viste dinamiche.
Pagine & Webpart
Costruire pagine moderne e dashboard informative utilizzando webpart senza codice.
Sicurezza & Permessi
Gestire accessi granulari, ereditarietà, gruppi e condivisione sicura.
Collaborazione M365
Integrare SharePoint con Teams, usare il co-authoring e sincronizzare con OneDrive.
Dati Strutturati
Utilizzare le Liste per gestire processi, inventari e form di inserimento dati.

---

Grazie per l'attenzione! • Corso Amministrazione SharePoint Online & M365
Fine del Modulo 1
Chiusura e Prossimi Passi
Completato
 Concetti Chiave Acquisiti 
 Creazione e gestione Siti e Librerie
 Strutturazione dati con Liste e Metadati
 Gestione Permessi e Sicurezza
 Integrazione Teams e OneDrive
 Nel Prossimo Modulo... 
Automazione: Power Automate & Workflow
Security Avanzata: Compliance & DLP
Best Practices: Governance M365
Domande?
Apriamo il confronto! Dubbi, curiosità o scenari specifici che vorreste approfondire.
 Condivisione Esperienze
 Consigli Pratici
 Troubleshooting
