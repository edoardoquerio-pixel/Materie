# Cloud Azure — Appunti Strutturati per Sessione

> **Corso:** ITS ICT Cloud Specialist 2025-2027  
> **Materia:** 14_Cloud_Azure

---

## Indice delle Sessioni

1. [Introduzione e Architettura](#introduzione-e-architettura)
2. [Identity e Governance](#identity-e-governance)
3. [Reti su Azure](#reti-su-azure)
4. [Compute — VM e Scalabilità](#compute-vm-e-scalabilit)
5. [Compute — App Service e Functions](#compute-app-service-e-functions)
6. [Container e AKS](#container-e-aks)
7. [Storage e Sicurezza](#storage-e-sicurezza)
8. [AI su Azure e Copilot](#ai-su-azure-e-copilot)
9. [Database e Data Integration](#database-e-data-integration)
10. [Security e Business Continuity](#security-e-business-continuity)

---

## Introduzione e Architettura

### Materiali

- [`01_1_Microsoft_Azure_-_Introduzione.md`](00_Note/01_1_Microsoft_Azure_-_Introduzione.md)
- [`11_2_Microsoft_Azure_-_Architettura_e_Strumenti_di_Accesso_Parte_1.md`](00_Note/11_2_Microsoft_Azure_-_Architettura_e_Strumenti_di_Accesso_Parte_1.md)
- [`12_3_Microsoft_Azure_-_Architettura_e_Strumenti_di_Accesso_Parte_2.md`](00_Note/12_3_Microsoft_Azure_-_Architettura_e_Strumenti_di_Accesso_Parte_2.md)

### Contenuti

DOCENTE
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Introduzione (4 ore)

---

Microsoft Azure — Introduzione
Corso Cloud Specialist · ITS ICT
Cosa faremo in 100 ore
•  Sostenibilità e IT — smart working, smart grid, sensori, RAEE, economia circolare
•  Fondamenti di Azure — regioni, responsabilità condivisa, ARM, strumenti di accesso
•  Identity & Governance — Entra ID

*[Contenuto troncato — vedi file completo]*

---

DOCENTE
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Architettura e strumenti di accesso - Parte 1 (4 ore)

---

Architettura e strumenti di accesso
Corso Cloud Specialist - ITS ICT
Agenda (4 ore)
•  Tenant, subscription e piano gratuito
•  Risorse, wizard di creazione, resource group
•  Regioni e zone di disponibilità
•  Azure Resource Manager (ARM)
•  Portale e Azure C

*[Contenuto troncato — vedi file completo]*

---

DOCENTE
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Architettura e strumenti di accesso - Parte 2 (4 ore)

---

Architettura e strumenti di accesso - Parte 2
Corso Cloud Specialist - ITS ICT
Agenda (4 ore)
•  Paired regions e edge locations
•  Modello di responsabilità condivisa e SLA
•  Best practice di separazione (resource group)
•  ARM: scope e idempotenza
•  Cloud 

*[Contenuto troncato — vedi file completo]*

---


## Identity e Governance

### Materiali

- [`13_4_Microsoft_Azure_-_Identity_e_Governance_Parte_1.md`](00_Note/13_4_Microsoft_Azure_-_Identity_e_Governance_Parte_1.md)
- [`14_5_Identity_e_Governance_-_Parte_2.md`](00_Note/14_5_Identity_e_Governance_-_Parte_2.md)

### Contenuti

DOCENTE
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Identity e Governance - Parte 1 (2 ore)

---

Identity e Governance
Come Azure gestisce chi sei, cosa puoi fare e quali regole valgono

---

Argomenti di oggi
•  Microsoft Entra ID: cos'è, il tenant, il dominio .onmicrosoft.com
•  Utenti e gruppi: interni vs esterni, creazione, associazione
•  App Registration: identit

*[Contenuto troncato — vedi file completo]*

---

DOCENTE
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Identity e Governance - Parte 2 (4 ore)

---

Identity e Governance - Parte 2
Conditional Access, Identity Protection, PIM e governance pratica

---

Argomenti di oggi
•  Conditional Access: regole di accesso basate su utente, rischio e dispositivo
•  Identity Protection: segnali di rischio e protezione degli account
•

*[Contenuto troncato — vedi file completo]*

---


## Reti su Azure

### Materiali

- [`15_6_Reti_su_Azure_-_Parte_1.md`](00_Note/15_6_Reti_su_Azure_-_Parte_1.md)
- [`16_7_Microsoft_Azure_-_Reti_su_Azure_-_Parte_2.md`](00_Note/16_7_Microsoft_Azure_-_Reti_su_Azure_-_Parte_2.md)
- [`17_8_Microsoft_Azure_-_Reti_su_Azure_-_Parte_3.md`](00_Note/17_8_Microsoft_Azure_-_Reti_su_Azure_-_Parte_3.md)

### Contenuti

DOCENTE
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Reti su Azure - Parte 1 (2 ore)

---

Reti su Azure - Parte 1
VNet, subnet, NSG e accesso RDP come caso guida

---

Argomenti
•  Perche' la rete conta in Azure
•  VNet e Subnet: i blocchi base
•  NSG: regole allow/deny sul traffico
•  RDP su una VM Windows: cosa deve esserci per collegarsi
•  Caso guida: relazione tra 

*[Contenuto troncato — vedi file completo]*

---

DOCENTE
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Reti su Azure - Parte 2 (3 ore)

---

Reti su Azure - Parte 2
NSG su subnet e NIC, effective rules, HTTP/HTTPS e troubleshooting

---

Argomenti
•  Ripresa dei concetti chiave della Parte 1
•  Differenza tra NSG su subnet e NSG su NIC
•  Effective security rules: dove leggere il risultato finale
•  Casi tipici: HTTP e 

*[Contenuto troncato — vedi file completo]*

---

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Reti su Azure - Parte 3 (4 ore)

---

Reti su Azure - Parte 3
Routing, peering, pubblicazione e accessi

---

Cosa chiudiamo oggi
•  completiamo il quadro rispetto alla Parte 2 con routing, peering e accessi più strutturati
•  colleghiamo ogni esigenza al servizio giusto: cambiare percorso, collegare reti, pubblicare, t

*[Contenuto troncato — vedi file completo]*

---


## Compute — VM e Scalabilità

### Materiali

- [`18_9_Microsoft_Azure_-_Compute_su_Azure_-_VM_immagini_e_dimensionamento.md`](00_Note/18_9_Microsoft_Azure_-_Compute_su_Azure_-_VM_immagini_e_dimensionamento.md)

### Contenuti

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Compute su Azure: VM, immagini e dimensionamento (4 ore)

---

Compute su Azure
Virtual Machine, immagini e dimensionamento

---

Da dove ripartiamo
•  abbiamo già letto una VM dal lato rete: NIC, Public IP, NSG, RDP
•  abbiamo già aperto il wizard di creazione fino a Review + create
•  oggi cambiamo domanda: non solo c

*[Contenuto troncato — vedi file completo]*

---


## Compute — App Service e Functions

### Materiali

- [`03_11_Microsoft_Azure_-_Compute_su_Azure_-_App_Service_e_Functions.md`](00_Note/03_11_Microsoft_Azure_-_Compute_su_Azure_-_App_Service_e_Functions.md)

### Contenuti

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Compute su Azure: App Service e Functions (4 ore)

---

Compute su Azure
App Service e Functions

---

Dalla VM al servizio gestito
•  con una VM gestisci sistema operativo, patch, runtime e applicazione
•  con App Service porti soprattutto codice e configurazione
•  con Functions porti funzioni che si attivano a evento

*[Contenuto troncato — vedi file completo]*

---


## Container e AKS

### Materiali

- [`04_12_Microsoft_Azure_-_Compute_su_Azure_-_Container_AKS_e_ottimizzazione.md`](00_Note/04_12_Microsoft_Azure_-_Compute_su_Azure_-_Container_AKS_e_ottimizzazione.md)

### Contenuti

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Compute su Azure: container, AKS e ottimizzazione (4 ore)

---

Compute su Azure
Container, AKS e ottimizzazione

---

Perché arriviamo ai container
•  una VM porta con sé sistema operativo e gestione completa
•  App Service riduce la gestione del server
•  il container impacchetta applicazione e dipendenze in modo ripe

*[Contenuto troncato — vedi file completo]*

---


## Storage e Sicurezza

### Materiali

- [`05_13_Microsoft_Azure_-_Storage_Data_Integration_-_Storage_e_Sicurezza.md`](00_Note/05_13_Microsoft_Azure_-_Storage_Data_Integration_-_Storage_e_Sicurezza.md)
- [`06_14_Microsoft_Azure_-_Storage_Data_Integration_-_Protezione_dati_e_file_service.md`](00_Note/06_14_Microsoft_Azure_-_Storage_Data_Integration_-_Protezione_dati_e_file_service.md)

### Contenuti

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Storage, Data & Integration - PT1: Storage account, servizi dati, sicurezza e accesso storage (4 ore)

---

Storage account e servizi dati
•  Storage account: General Purpose v2 e Premium
•  Servizi disponibili: Blob, File, Queue, Table
•  Casi d'uso principali dei servizi dati e quando scegliere Azure Files
•  Criteri 

*[Contenuto troncato — vedi file completo]*

---

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Storage, Data & Integration: protezione dati, file service e backup (4 ore)

---

Storage, protezione dati e file service (4 ore)
•  Lifecycle, tiering e retention per governare costo e ciclo di vita del dato
•  Versioning, soft delete e immutabilita per protezione operativa e compliance
•  Azure Files con identita cent

*[Contenuto troncato — vedi file completo]*

---


## AI su Azure e Copilot

### Materiali

- [`07_15_Microsoft_Azure_-_AI_su_Azure_-_Foundry_modelli_e_GitHub_Copilot.md`](00_Note/07_15_Microsoft_Azure_-_AI_su_Azure_-_Foundry_modelli_e_GitHub_Copilot.md)

### Contenuti

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
AI su Azure: Foundry, modelli e GitHub Copilot (in preparazione all'evento Microsoft Build //localhost Torino) (4 ore)

---

AI su Azure
Foundry, modelli e GitHub Copilot: cosa c'è sotto le demo del Microsoft Build //localhost Torino

---

Argomenti
•  Dove sta l'AI nel catalogo Azure (AI Services, Azure OpenAI, Foundry

*[Contenuto troncato — vedi file completo]*

---


## Database e Data Integration

### Materiali


### Contenuti


## Security e Business Continuity

### Materiali


### Contenuti


