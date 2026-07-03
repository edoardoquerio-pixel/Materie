# Parte 1

Fonte: `4) Microsoft Azure - Identity e Governance (Parte 1).pptx`

### Slide 1

DOCENTE

Federico Laurianti

UNITA' FORMATIVA

Microsoft Azure (100 ore)

ARGOMENTO

Identity e Governance - Parte 1 (2 ore)

---

### Slide 2

Identity e Governance

Come Azure gestisce chi sei, cosa puoi fare e quali regole valgono

---

### Slide 3

Argomenti di oggi

•  Microsoft Entra ID: cos'è, il tenant, il dominio .onmicrosoft.com
•  Utenti e gruppi: interni vs esterni, creazione, associazione
•  App Registration: identità per le applicazioni
•  Azure Policy: assegnazioni e restrizioni (es. region consentite)
•  RBAC: cos'è, ruoli, scope, assegnazioni
•  IAM nel portale: Check Access, Add Role Assignment
•  MFA: perché è obbligatorio
Nelle prossime lezioni approfondiremo ogni tema e ne aggiungeremo altri.

---

### Slide 4

Microsoft Entra ID (ex Azure AD)

Microsoft Entra ID è il servizio di identità e accesso di Azure. Gestisce:
•  Chi sei: utenti, gruppi, applicazioni
•  Come ti autentichi: password, MFA, Authenticator
•  Cosa puoi fare: ruoli, permessi, policy
Ogni organizzazione Azure ha almeno un tenant Entra ID: è il "contenitore" di tutte le identità.
“Pensatelo come l'elenco telefonico dell'organizzazione: contiene tutti gli utenti, i gruppi e le app registrate.”

---

### Slide 5

Il tenant e il dominio .onmicrosoft.com

Quando un'organizzazione crea un tenant Entra ID, riceve un dominio di default:
nomeorganizzazione.onmicrosoft.com
•  È l'indirizzo univoco del tenant su Azure
•  Nel vostro caso: itsictpiemonte.onmicrosoft.com
•  Il vostro account istituzionale è collegato a quel tenant
Con la sottoscrizione per studenti, l'accesso a Entra ID è bloccato, ma il tenant esiste. La sottoscrizione normale permette di gestire utenti, gruppi e app.

---

### Slide 6

Utenti: interni ed esterni

In Entra ID ci sono due tipi di utenti:

Member (interno)

Guest (esterno)

Chi è

Appartiene all'organizzazione

Invitato da fuori

Account

Nel tenant (es. mario.rossi@...onmicrosoft.com)

Il suo esistente (Gmail, altro tenant)

Accesso

Completo (in base ai permessi)

Limitato a ciò che gli è condiviso

Quando crei un utente, puoi assegnargli subito uno o più gruppi esistenti.

---

### Slide 7

Gruppi

I gruppi servono a organizzare gli utenti e semplificare la gestione dei permessi.
•  Crei un gruppo (es. "Team Sviluppo", "Docenti", "Studenti Anno 1")
•  Associ uno o più utenti al gruppo
•  Assegni i permessi al gruppo invece che ai singoli utenti
Vantaggio: se entra un nuovo membro nel team, lo aggiungi al gruppo e ha subito tutti i permessi necessari. Non devi configurare nulla risorsa per risorsa.
“È lo stesso principio dei gruppi di Active Directory in azienda, ma su cloud.”

---

### Slide 8

App Registration: identità per le applicazioni

Anche le applicazioni hanno bisogno di un'identità per interagire con Azure.
App Registration crea un'identità nel tenant Entra ID. Esempio: Terraform.
•  Si registra come app nel tenant
•  Riceve credenziali (client ID + secret) per autenticarsi
•  Gli si assegnano i permessi necessari (es. creare VM, gestire rete)
Stessa cosa per: pipeline CI/CD, script di automazione, applicazioni web.
“In Enterprise Applications trovi le app già registrate e i relativi permessi.”

---

### Slide 9

Azure Policy

Azure Policy impone regole sull'intera sottoscrizione (o su un ambito più ristretto).
Quello che abbiamo visto: Authoring > Assignments > Allowed resource deployment regions - solo 5 region consentite. Se crei una VM in una region non in lista, Azure la blocca.
Le policy servono a:
•  Impedire errori: nessuno crea risorse dove non dovrebbe
•  Garantire conformità: regole aziendali applicate automaticamente
•  Controllare i costi: es. limitare i tipi di VM consentiti
“La policy non è un permesso: è una regola imposta dall'alto che vale per tutti, indipendentemente dal ruolo.”

---

### Slide 10

RBAC: Role-Based Access Control

RBAC è il modello con cui Azure gestisce i permessi. Tre domande:
•  Chi? - un utente, un gruppo, un'app (il principal)
•  Cosa può fare? - un insieme di azioni (il ruolo)
•  Dove? - a quale livello si applica (lo scope)
Esempio: "Mario (chi) ha il ruolo Contributor (cosa) sul Resource Group Lab-01 (dove)."
Lo scope è gerarchico (i permessi si ereditano dall'alto verso il basso):
Management Group > Subscription > Resource Group > Resource
Reader sulla Subscription = Reader su tutti i Resource Group e risorse al suo interno.

---

### Slide 11

Ruoli principali di Azure

Alcuni ruoli predefiniti (built-in) che incontrate spesso:

Ruolo

Cosa può fare

Owner

Tutto, compreso assegnare ruoli ad altri

Contributor

Tutto tranne assegnare ruoli

Reader

Solo leggere, non può modificare nulla

User Access Administrator

Gestisce solo chi ha accesso a cosa

Esistono anche ruoli specifici per servizio (es. "Virtual Machine Contributor", "Storage Blob Data Reader").
“Un permesso (role assignment) può avere una data di scadenza: dopo quella data, l'accesso viene rimosso automaticamente.”

---

### Slide 12

IAM nel portale: Check Access e Add Role Assignment

Su qualsiasi risorsa o Resource Group, c'è il pannello Access control (IAM).
Check Access: cerchi una persona e vedi che ruolo ha (anche permessi ereditati).
Add role assignment richiede 3 cose:
•  Role: Owner, Contributor, Reader, ecc.
•  Members: User/group/service principal oppure Managed identity
•  Confermi e il permesso è attivo
“Cliccando su un utente o gruppo nel pannello IAM, puoi vederne info e metadati.”

---

### Slide 13

Service Principal vs Managed Identity

Nell'Add Role Assignment avete visto due tipi di identità non-umane:

Service Principal

Managed Identity

Chi la crea

Tu (App Registration)

Azure

Credenziali

Tu le gestisci (secret)

Azure le gestisce

Uso tipico

Servizi esterni (Terraform, GitHub)

Servizi Azure (VM, App)

Rischio

Secret può essere esposto

Nessun secret da esporre

In breve: se il servizio gira dentro Azure, usa Managed Identity. Se è esterno, serve un Service Principal.

---

### Slide 14

MFA: Multi-Factor Authentication

MFA aggiunge un secondo fattore di verifica oltre alla password.
•  Qualcosa che sai: la password
•  Qualcosa che hai: il telefono con Microsoft Authenticator
Microsoft lo richiede su tutti i tenant (potete posticipare X volte, poi è obbligatorio). Nel vostro caso: login > notifica su Authenticator > approvate.
“Una password rubata non basta più per entrare. L'MFA è il singolo intervento più efficace contro accessi non autorizzati.”

---

### Slide 15

Riepilogo: i pezzi del puzzle

Livello

Servizio

Domanda

Identità

Entra ID: utenti, gruppi, app, MFA

Chi sei?

Permessi

RBAC: ruolo + scope = accesso

Cosa puoi fare?

Regole

Azure Policy: vincoli dall'alto

Cosa è consentito fare?

•  Entra ID gestisce le identità
•  RBAC assegna i permessi
•  Policy impone le regole

---

### Slide 16

Prossime lezioni

Quello che abbiamo visto oggi è una panoramica. Nelle prossime 8 ore approfondiremo:
•  Conditional Access: regole che decidono quando e come puoi accedere
•  Identity Protection: rilevamento automatico di accessi sospetti
•  PIM: attivare ruoli privilegiati solo quando servono
•  Management Groups: organizzare più sottoscrizioni
•  Policy e iniziative: creare e gestire set di regole
•  Tagging, naming convention, locks: governance pratica delle risorse
•  B2B e B2C: gestire identità esterne in scenari reali