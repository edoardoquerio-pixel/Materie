# Parte 1

## Panoramica
Identity e Governance - Parte 1 (2 ore)

## Argomenti trattati
Azure, API REST, Cloud, Reti, Data Analytics

---
## Appunti

### Slide 1
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
Identity e Governance - Parte 1 (2 ore)
### Slide 2
Identity e Governance
Come Azure gestisce chi sei, cosa puoi fare e quali regole valgono
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
### Slide 4
Microsoft Entra ID (ex Azure AD)
Microsoft Entra ID è il servizio di identità e accesso di Azure. Gestisce:
•  Chi sei: utenti, gruppi, applicazioni
•  Come ti autentichi: password, MFA, Authenticator
•  Cosa puoi fare: ruoli, permessi, policy
Ogni organizzazione Azure ha almeno un tenant Entra ID: è il "contenitore" di tutte le identità.
“Pensatelo come l'elenco telefonico dell'organizzazione: contiene tutti gli utenti, i gruppi e le app registrate.”
### Slide 5
Il tenant e il dominio .onmicrosoft.com
Quando un'organizzazione crea un tenant Entra ID, riceve un dominio di default:
nomeorganizzazione.onmicrosoft.com
•  È l'indirizzo univoco del tenant su Azure
•  Nel vostro caso: itsictpiemonte.onmicrosoft.com
•  Il vostro account istituzionale è collegato a quel tenant
Con la sottoscrizione per studenti, l'accesso a Entra ID è bloccato, ma il tenant esiste. La sottoscrizione normale permette di gestire utenti, gruppi e app.
### Slide 6
Utenti: interni ed esterni
In Entra ID ci sono due tipi di utenti:
Member (interno)
Guest (esterno)
Appartiene all'organizzazione
Invitato da fuori
Nel tenant (es. mario.rossi@...onmicrosoft.com)
Il suo esistente (Gmail, altro tenant)
Completo (in base ai permessi)
Limitato a ciò che gli è condiviso
Quando crei un utente, puoi assegnargli subito uno o più gruppi esistenti.
### Slide 7
I gruppi servono a organizzare gli utenti e semplificare la gestione dei permessi.
•  Crei un gruppo (es. "Team Sviluppo", "Docenti", "Studenti Anno 1")
•  Associ uno o più utenti al gruppo
•  Assegni i permessi al gruppo invece che ai singoli utenti
Vantaggio: se entra un nuovo membro nel team, lo aggiungi al gruppo e ha subito tutti i permessi necessari. Non devi configurare nulla risorsa per risorsa.
“È lo stesso principio dei gruppi di Active Directory in azienda, ma su cloud.”
### Slide 8
App Registration: identità per le applicazioni
Anche le applicazioni hanno bisogno di un'identità per interagire con Azure.
App Registration crea un'identità nel tenant Entra ID. Esempio: Terraform.
•  Si registra come app nel tenant
•  Riceve credenziali (client ID + secret) per autenticarsi
•  Gli si assegnano i permessi necessari (es. creare VM, gestire rete)
Stessa cosa per: pipeline CI/CD, script di automazione, applicazioni web.
“In Enterprise Applications trovi le app già registrate e i relativi permessi.”
### Slide 9
Azure Policy impone regole sull'intera sottoscrizione (o su un ambito più ristretto).
Quello che abbiamo visto: Authoring > Assignments > Allowed resource deployment regions - solo 5 region consentite. Se crei una VM in una region non in lista, Azure la blocca.
Le policy servono a:
•  Impedire errori: nessuno crea risorse dove non dovrebbe
•  Garantire conformità: regole aziendali applicate automaticamente
•  Controllare i costi: es. limitare i tipi di VM consentiti
“La policy non è un permesso: è una regola imposta dall'alto che vale per tutti, indipendentemente dal ruolo.”
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

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 004_4_Microsoft_Azure_-_Identity_e_Governance_Parte_1_.md*
