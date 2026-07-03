# Parte 2

## Panoramica
Identity e Governance - Parte 2 (4 ore)

## Argomenti trattati
Azure, Reti, Database, Data Analytics, API REST

---
## Appunti

### Slide 1
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
Identity e Governance - Parte 2 (4 ore)
### Slide 2
Identity e Governance - Parte 2
Conditional Access, Identity Protection, PIM e governance pratica
### Slide 3
Argomenti di oggi
•  Conditional Access: regole di accesso basate su utente, rischio e dispositivo
•  Identity Protection: segnali di rischio e protezione degli account
•  PIM: ruoli privilegiati attivi solo quando servono
•  Management Groups: organizzare più subscription in modo coerente
•  Azure Policy e iniziative: applicare regole di conformità in modo centralizzato
•  Naming, tagging e locks: governance pratica delle risorse
•  B2B ed External ID: identità esterne per partner e applicazioni
### Slide 4
Conditional Access
Conditional Access è il motore Zero Trust di Microsoft Entra. Funziona con regole if-then:
“Se un utente vuole accedere a una risorsa, allora deve soddisfare una condizione.”
Esempio: "Se un utente accede da fuori rete aziendale, allora deve fare MFA."
Le policy si creano in Entra ID > Conditional Access > Policies e si applicano dopo l'autenticazione iniziale (primo fattore).
Richiedono licenza Entra ID P1 (inclusa in Microsoft 365 Business Premium).
### Slide 5
Conditional Access: segnali e decisioni
Segnali (input della policy):
•  Utente o gruppo: a chi si applica la policy
•  Indirizzo IP: posizione geografica, rete aziendale o meno
•  Dispositivo: conforme, ibrido, piattaforma (Windows, iOS...)
•  Applicazione: a quale app si sta accedendo
•  Livello di rischio: segnale da Identity Protection
Decisioni (output della policy):
•  Blocca accesso
•  Consenti con condizioni: richiedi MFA, dispositivo conforme, cambio password
### Slide 6
Identity Protection
Identity Protection rileva automaticamente comportamenti sospetti sugli accessi:
•  Login da IP anonimi (es. VPN/Tor)
•  Password spray: tentativi di indovinare password su molti account
•  Credenziali compromesse: trovate in database di leak
•  Viaggio impossibile: login da Roma e da Tokyo a 5 minuti di distanza
Genera tre report: risky users, risky sign-ins, risk detections.
Può integrarsi con Conditional Access: se il rischio è alto, blocca l'accesso o forza il cambio password. Richiede licenza Entra ID P2.
### Slide 7
PIM: Privileged Identity Management
PIM elimina i permessi privilegiati permanenti. Principio: nessuno dovrebbe essere Owner o Global Admin 24/7.
•  L'admin assegna un ruolo come eligible (idoneo), non active
•  Quando serve, l'utente attiva il ruolo dal portale PIM
•  L'attivazione richiede: MFA, una giustificazione, eventuale approvazione
•  Il ruolo resta attivo per un tempo limitato (es. 8 ore), poi scade
“È il principio del just-in-time access: i permessi esistono solo quando servono.”
Richiede licenza Entra ID P2 o Entra ID Governance.
### Slide 8
Management Groups
I Management Groups sono il livello sopra le subscription:
Management Group > Subscription > Resource Group > Resource
Servono per applicare in modo coerente policy e RBAC a più sottoscrizioni insieme.
•  Ogni directory ha un Root Management Group
•  Le assegnazioni fatte a un MG si ereditano verso il basso
•  Sono utili per separare ambienti, business unit o aree geografiche
“Esempio: il MG "Europa" può imporre policy comuni a tutte le subscription europee.”
### Slide 9
Azure Policy e iniziative
Azure Policy controlla se le risorse rispettano regole organizzative.
•  Esempi: consentire solo regioni approvate, imporre tag obbligatori, vietare SKU non autorizzate
•  Effetti tipici: audit, deny, append, deployIfNotExists
•  Si assegna a Management Group, subscription o Resource Group
Iniziativa = raccolta di più policy gestite come un unico set.
•  Utile per standard di sicurezza, compliance o cost management
•  Rende più semplice applicare e tracciare regole comuni
“I Management Groups danno la gerarchia, Azure Policy applica le regole.”
### Slide 10
Governance pratica: naming, tagging e locks
Naming convention
Dare nomi coerenti e leggibili alle risorse
Aggiungere metadati come Environment, Owner, CostCenter
Proteggere da modifiche o cancellazioni accidentali
•  I tag aiutano costi e filtri, ma non si ereditano automaticamente
•  I lock nel portale sono Delete e Read-only; in CLI/API sono CanNotDelete e ReadOnly

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 005_5_Identity_e_Governance_-_Parte_2.md*
