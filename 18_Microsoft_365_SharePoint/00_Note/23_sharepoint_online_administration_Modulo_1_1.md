# sharepoint_online_administration_Modulo 1 (1)

**File:** `sharepoint_online_administration_Modulo 1 (1).pptx`
**Tipo:** `.pptx`
**Dimensione:** 2076.9 KB
**Ultima modifica:** 26/06/2026 10:04

---

 Amministrazione
SharePoint Online
& Collaborazione M365
Un percorso completo per padroneggiare la struttura, la sicurezza e l'integrazione nell'ecosistema Microsoft 365.
 Obiettivi del Modulo 
Comprendere la gestione dei siti, le librerie documenti, i permessi avanzati e l'integrazione nativa con Teams e OneDrive.
Struttura Siti
Permessi
Teams Sync
Modulo 2
Sharepoint Online

---

Panoramica del modulo
Cosa affronteremo oggi
Agenda dettagliata
1
Struttura e Siti
Team Site vs Communication Site e architettura fondamentale.
2
Librerie Documenti
Organizzazione file, colonne, viste personalizzate e ricerca.
3
Pagine e Webpart
Creazione di contenuti moderni e visualizzazione informazioni.
4
Permessi e Sicurezza
Gestione accessi, gruppi e livelli di autorizzazione.
5
Liste e Dati
Gestione dati strutturati come alternativa a Excel.
6
Integrazione M365
Sinergia con Teams, OneDrive e altre app dell'ecosistema.

---

Elimina i Duplicati
Evita la proliferazione di copie via email e riduce la perdita di file grazie ad un archivio unico e centralizzato accessibile a tutti.
Collaborazione
Permette a più utenti di lavorare contemporaneamente sullo stesso documento (co-authoring), tracciando ogni modifica in tempo reale.
Struttura Organizzata
Organizza i documenti in modo logico tramite metadati e tassonomie, superando i limiti delle semplici cartelle nidificate.
Versioning & Sicurezza
Garantisce il recupero di versioni precedenti dei file e offre un controllo granulare sui permessi di accesso per ogni utente.
Ecosistema M365
Integrazione nativa e fluida con Teams, OneDrive, Planner e Power Platform per un ambiente di lavoro digitale completo.
Governance dei Dati
Assicura la conformità normativa, la gestione delle policy di conservazione e la protezione delle informazioni sensibili aziendali.
Valore Aziendale
Perché le aziende usano SharePoint

---

Infrastruttura Zero
Nessun server da acquistare o gestire. Manutenzione a carico di Microsoft.
Aggiornamenti Automatici
Funzionalità sempre aggiornate all'ultima versione senza downtime.
Integrazione Nativa M365
Connessione fluida con Teams, OneDrive, Power Automate e Power Apps.
Sicurezza Avanzata
Compliance enterprise e protezione dati gestita globalmente da Microsoft.
SharePoint Online
SaaS (Software as a Service)
 Scelta raccomandata per la maggior parte delle aziende
Gestione Complessa
Richiede server fisici/virtuali, backup, patching e personale IT dedicato.
Aggiornamenti Manuali
Upgrade costosi e rischiosi (es. migrazione da 2016 a 2019).
Integrazioni Limitate
Connessione ibrida complessa per usare Teams o Power Platform.
Costi CAPEX Elevati
Investimento iniziale alto in hardware e licenze perpetue.
SharePoint On-Premise
Server Farm Locale
 Solo per esigenze specifiche di compliance o legacy
Confronto Tecnologie
SharePoint Online vs On-Premise
Analisi comparativa
VS

---

Team Site
Collaborazione & Lavoro di Gruppo
Quando usarlo
"Dobbiamo lavorare insieme su questo"
Collaborazione Quotidiana
Ideale per progetti, reparti o gruppi di lavoro che creano contenuti insieme.
Connesso a M365 Group
Crea automaticamente un Team in Teams, un piano Planner e un calendario condiviso.
Gestione Permessi Semplice
Tutti i membri del team hanno accesso di modifica (Member) di default.
Communication Site
Informazione & Comunicazione
Quando usarlo
"Voglio comunicare questo a tutti"
Comunicazione "Top-Down"
Pubblicazione di news, policy, eventi o portali intranet per un vasto pubblico.
Design Visivo Impattante
Layout moderni, widescreen, senza barra laterale sinistra, focus su immagini e leggibilità.
Pochi Autori, Molti Lettori
Un piccolo gruppo crea e gestisce i contenuti, il resto dell'azienda legge (Read-only).
Architettura SharePoint
Tipi di Siti: Team Site vs Communication Site
Struttura Fondamentale
VS

---

01
Navigazione
Menu e Quick Launch che guidano l'utente nell'esplorazione dei contenuti.
02
Pagine
Interfaccia visiva con webpart, testo e media per presentare le informazioni.
03
Librerie
Archivi centralizzati per file con versioning, metadati e co-authoring.
04
Liste
Tabelle strutturate per gestire dati come task, scadenze e inventari.
05
Impostazioni
Configurazione di permessi, look & feel e parametri regionali del sito.
Architettura Fondamentale
Struttura di un sito SharePoint
5 Componenti Chiave
Ogni sito è un'entità autonoma nell'ecosistema M365

---

User Experience
Navigazione Efficace
Best Practices
Nomi Chiari e Intuitivi
Usa etichette brevi e comprensibili (es. "Fatture" invece di "Documenti Amministrativi Contabili 2024").
Struttura Poco Profonda
Mantieni la navigazione entro 2-3 livelli al massimo. Gli utenti devono trovare i contenuti in pochi clic.
Link Rapidi in Evidenza
Usa la webpart "Collegamenti rapidi" per risorse frequenti, posizionandoli nella parte alta della pagina.
Evita Duplicazioni
Non creare link ridondanti che portano allo stesso posto. Crea confusione e disorientamento.
Usa Hub Sites
Collega siti correlati sotto un Hub Site per condividere navigazione, branding e ricerca globale.
 Evita Menù Complessi
Struttura profonda = Caos
 Usa Mega Menù
HUB
Contenuto rilevante

---

A cosa serve un Team Site?
 Quiz Time
A
Pubblicare annunci aziendali per tutti i dipendenti
Collaborare con il team sui documenti e gestire attività
C
Archiviazione personale di file privati
B

---

Struttura di un Sito SharePoint
Siti, Sottositi e Hub Sites
Architettura Moderna
Sottositi
Approccio Legacy
⚠  Sconsigliato da Microsoft
Struttura Gerarchica Rigida
I sottositi sono figli di un sito padre con URL annidati (/sites/marketing/uk). La navigazione è rigida e i contenuti difficili da spostare.
Permessi Complicati
Ereditano i permessi del padre, ma eccezioni frequenti frammentano la sicurezza e aumentano il carico amministrativo.
Evoluzione Bloccata
Microsoft non sviluppa nuove funzionalità per i sottositi. Supportati ma non aggiornati: adatti solo a SharePoint 2016 e precedenti.
Hub Sites
Approccio Moderno
✓  Raccomandato da Microsoft
Struttura Piatta e Flessibile
Siti indipendenti collegati tramite un Hub Site. Nessuna gerarchia rigida: ogni sito ha URL pulito e può essere spostato liberamente.
Navigazione Condivisa
L'Hub site distribuisce la barra di navigazione e il branding a tutti i siti associati, mantenendo coerenza visiva.
Ricerca Globale e Governance
La ricerca di un Hub Site restituisce risultati da tutti i siti associati. Permessi indipendenti per ogni sito figlio.
VS

---

Layout Responsive
Struttura flessibile a sezioni e colonne che si adatta automaticamente a desktop, tablet e dispositivi mobili.
Contenuti Ricchi
Integra facilmente testo formattato, immagini, video, collegamenti rapidi ed elenchi dinamici.
Versatilità d'Uso
Ideali per costruire portali intranet aziendali, manuali di procedure, dashboard di progetto e landing page.
Pubblicazione Rapida
Crea, modifica e pubblica notizie e pagine in pochi clic, con controlli di versione e approvazione.
Comunicare con Impatto
Pagine Moderne
Web Content

---

Le Webpart sono i componenti modulari di SharePoint. 
Permettono di costruire pagine ricche e interattive semplicemente trascinando i blocchi.
Building Blocks
Webpart: i blocchi della pagina
No Code Required

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

Scegli Layout
Definisci la struttura della pagina scegliendo sezioni a una, due o tre colonne per organizzare i contenuti.
1
Aggiungi Webpart
Inserisci gli elementi necessari come testo, immagini, liste, video o pulsanti per arricchire la pagina.
2
Salva & Pubblica
Salva una bozza per continuare dopo o clicca "Pubblica" per rendere la pagina immediatamente visibile a tutti.
3
Condividi
Invia il link ai colleghi tramite Teams o email e raccogli feedback o commenti direttamente sulla pagina.
4
Processo di Creazione
Creare una Pagina: Passo-Passo
Flusso Operativo

---

Pagine Approfondite
Esempio: Pagina Progetto
Project Hub
