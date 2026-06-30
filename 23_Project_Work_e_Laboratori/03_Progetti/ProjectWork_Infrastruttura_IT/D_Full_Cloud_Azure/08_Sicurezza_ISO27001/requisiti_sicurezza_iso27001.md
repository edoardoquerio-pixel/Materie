# Requisiti Sicurezza ISO 27001 — Variante Full Cloud Azure

## Premessa

La presente sezione documenta l'adeguamento tecnico della Variante Full Cloud Azure
ai requisiti ISO/IEC 27001 specificati dal cliente. La certificazione formale richiede
un audit esterno da parte di un ente accreditato; questo documento copre gli aspetti
tecnici propedeutici alla certificazione.

Azure è certificato ISO 27001:2013, ISO 27017, ISO 27018, SOC 2 Type II, HIPAA e oltre
100 certificazioni di conformità. L'infrastruttura eredita queste certificazioni.

## Business Continuity

### Ridondanza sistemi strategici

Azure offre ridondanza nativa a livello di infrastruttura:

| Sistema | Strategia | Dettaglio |
|---|---|---|
| **Compute (HPC, Pondus)** | Availability Zones (3 zone West Europe) + region pair (North Europe) | Failover automatico multi-regione |
| **Database (Azure SQL)** | Active Geo-Replication | Failover automatico <30 secondi |
| **Storage (Blob)** | GRS (Geo-Redundant Storage) | 3 copie locali + 3 copie in regione accoppiata |
| **Load Balancer** | Azure Front Door / Traffic Manager — multi-regione attivo | Nessun single point of failure |
| **DNS** | Azure DNS anycast | Alta disponibilità nativa |

### Ridondanza connettività

| Elemento | Configurazione |
|---|---|
| **Link sede → Azure** | Fibra 1 Gbps primario + failover 4G/5G |
| **Azure VPN Gateway** | Active-Active — 2 tunnel IPsec simultanei |
| **ExpressRoute** | Opzionale: circuito dedicato per latenza ridotta e SLA 99,95% |

## Disaster Recovery

| Requisito | Implementazione |
|---|---|
| Delocalizzazione backup | Azure Blob Storage GRS (West Europe + North Europe) |
| Fruibilità servizi clienti | Pondus multi-regione, failover automatico <5 min |
| Procedure di restore | Runbook DR documentato, test semestrale via Site Recovery drill |
| RPO servizi critici | ≤1 ora (PITR Azure SQL) o 0 (Active Geo-Replication); HPC ≤4 ore |
| RTO servizi critici | ≤30 sec (SQL failover) / ≤5 min (AKS) / ≤60 min (HPC) |

## Sicurezza Accessi

### Cifratura dati

| Stato | Dettaglio |
|---|---|
| **Dati in transito** | TLS 1.3 su tutti i servizi esposti (HTTPS, gRPC, Azure Front Door) |
| **Dati a riposo** | Azure SSE (Storage Service Encryption) AES-256 di default |
| **Chiavi** | Azure Key Vault per customer-managed keys (CMEK) e BYOK |
| **Endpoint** | Laptop dipendenti: BitLocker (Windows) — policy obbligatoria |

### Protocolli sicuri

| Servizio | Protocollo |
|---|---|
| Web application (Pondus) | HTTPS (TLS 1.3) via Application Gateway |
| API | HTTPS + OAuth 2.0 / Azure AD tokens |
| SSH (VM) | SSH key-based, porta 22 via Azure Bastion (nessun IP pubblico) |
| VPN | IPsec (IKEv2), AES-256 |
| Posta | SMTP TLS, IMAP TLS (M365) |
| DB connection | TLS 1.2+ (Azure SQL firewall + Private Endpoint) |

### VPN

| Tipo | Configurazione |
|---|---|
| **LAN-to-LAN** | Azure VPN Gateway (tunnel IPsec IKEv2) tra FortiGate e Azure |
| **Client-to-LAN** | Azure Point-to-Site VPN + Azure Bastion per accesso admin via browser |
| **Hybrid Cloud** | N/A (tutto su Azure) |

### Autenticazione Multi-Fattore (MFA)

- **Microsoft Entra ID**: Conditional Access policy — MFA obbligatorio per tutti gli utenti
- **Microsoft Authenticator**: 2FA via app, SMS o chiamata
- **Azure AD B2C**: MFA per utenti Pondus (abbonamenti esterni)
- **Samba4 AD**: non più necessario (sostituito da Entra ID Connect sync)

### Identity and Access Management (IAM)

- **Azure RBAC**: ruoli predefiniti e custom per ogni servizio (Contributor, Reader, SQL Contributor, HPC Admin)
- **Managed Identities**: le applicazioni (Pondus) si autenticano ad Azure SQL senza credential in codice
- **Privileged Identity Management (PIM)**: accesso Just-In-Time ai ruoli amministrativi con approvazione e audit
- **Conditional Access**: policy basate su: posizione geografica, device compliance, rischio utente, applicazione

## Microsoft Defender for Cloud

| Funzionalità | Descrizione |
|---|---|
| **Security posture management** | Punteggio di sicurezza (Secure Score) con raccomandazioni prioritarie |
| **Vulnerability assessment** | Scansione vulnerabilità su VM HBv4 e container |
| **Adaptive application controls** | Allowlist delle applicazioni eseguibili sulle VM |
| **Just-In-Time VM access** | Accesso RDP/SSH su richiesta con finestra temporale |
| **File integrity monitoring** | Monitoraggio modifiche a file di sistema critici |
| **Container security** | Scansione immagini in ACR, protezione runtime AKS |

## Azure Policy — ISO 27001 Built-in Initiative

Azure Policy offre un'iniziativa predefinita per la conformità ISO 27001 che valuta automaticamente
oltre 60 controlli, tra cui:

- Cifratura dati a riposo e in transito
- Backup configurati per tutti i servizi
- Limiti di accesso di rete (NSG, firewall)
- MFA obbligatorio per utenti amministrativi
- Audit logging abilitato
- Utilizzo di RBAC al posto di permessi classici

## Microsoft Purview (Data Governance)

Incluso in Microsoft 365 E3 (già presente per Thema):

- **Data classification**: classificazione automatica di documenti sensibili
- **Data Loss Prevention (DLP)**: blocca la condivisione di dati riservati (es. risultati crash test clienti)
- **Information Protection**: etichette di riservatezza su documenti (Confidenziale, Uso Interno, Pubblico)
- **Audit logging**: tracciamento di ogni accesso a documenti e dati

## Bozza Policy di Sicurezza (Principi)

1. **Zero Trust**: verify explicitly, least privilege, assume breach
2. **MFA obbligatorio**: per tutti gli utenti TP Group, nessuna eccezione
3. **Accesso JIT**: ruoli amministrativi concessi solo per il tempo necessario
4. **Cifratura totale**: tutti i dati a riposo e in transito sono cifrati
5. **Audit continuo**: Azure Policy valuta la conformità ISO 27001 in tempo reale
6. **Backup e DR**: test DR semestrale obbligatorio
7. **Vulnerability management**: scansione mensile e remediation entro 30 giorni
8. **Incident response**: procedura documentata con escalation a Security Operations

---

## Procedure Organizzative ISO 27001

Accanto ai controlli tecnici già documentati, la conformità ISO 27001 richiede procedure organizzative che definiscano ruoli, responsabilità e processi. Le sezioni seguenti coprono i controlli dell'Allegato A applicabili al perimetro TP Group.

### A.5 — Policy di Sicurezza

#### Information Security Policy (bozza)

**Scopo**: Definire i principi, le responsabilità e gli obiettivi di sicurezza informatica per TP Group.

**Ambito**: La policy si applica a tutti i dipendenti, collaboratori, fornitori e sistemi informativi di TP Group, inclusi:
- Sistemi on-premise (in fase di dismissione)
- Infrastruttura cloud Azure
- Servizi M365 e Google Workspace (in fase di migrazione)
- Applicazioni interne (Pondus, Odoo) ed esterne

**Principi fondamentali**:

1. **Riservatezza**: I dati di clienti, dipendenti e progetto sono accessibili solo a personale autorizzato
2. **Integrità**: I dati sono protetti da modifiche non autorizzate tramite controlli di accesso e logging
3. **Disponibilità**: I servizi critici (Pondus, HPC, posta) hanno ridondanza e DR documentati
4. **Miglioramento continuo**: Il sistema di gestione della sicurezza è rivisto annualmente

**Responsabilità**:
- **Direzione**: Approva la policy di sicurezza e assegna le risorse necessarie
- **CISO/Responsabile Sicurezza**: Mantiene la policy, coordina gli audit, gestisce gli incidenti
- **Sistemisti**: Implementano i controlli tecnici, eseguono vulnerability scanning
- **Dipendenti**: Rispettano le policy, segnalano anomalie

**Ciclo di revisione**: La policy è rivista annualmente o in occasione di cambiamenti significativi (migrazione, nuovo servizio, incidente maggiore).

### A.6 — Organizzazione Interna

#### Ruoli e responsabilità di sicurezza

| Ruolo | Titolare | Responsabilità |
|---|---|---|
| **CISO** | Direttore IT / Responsabile nominato | Policy, risk assessment, audit, incident response coordination |
| **Security Team** | Sistemisti senior | Implementazione controlli, vulnerability management, monitoring |
| **System Administrators** | Personale IT | Gestione operativa, backup, patch, user management |
| **Data Owner** | Responsabile di funzione (amministrazione, HPC, Pondus) | Classificazione dati, autorizzazione accessi |
| **Internal Auditor** | Ruolo indipendente (o esterno) | Audit annuale, verifica conformità ISO 27001 |

#### Comitato di Sicurezza

Riunione trimestrale con:
- CISO (presiede)
- Direzione IT
- Responsabile legale/compliance
- Referenti di funzione (amministrazione, HPC, Pondus)

Ordine del giorno:
1. Stato delle vulnerabilità e remediation
2. Incidenti di sicurezza del periodo
3. Stato avanzamento compliance ISO 27001
4. Nuovi rischi e mitigazioni proposte
5. Approvazione modifiche alle policy

### A.12 — Operations Security

#### Vulnerability Management Process

| Fase | Frequenza | Azione | Responsabile |
|---|---|---|---|
| **Scansione** | Mensile | Azure Defender vulnerability scan su tutte le VM HBv4 e container AKS | Security Team |
| **Analisi** | Entro 5 giorni | Classificazione vulnerabilità (Critical/High/Medium/Low) | Security Team |
| **Remediation Critical** | Entro 7 giorni | Patch urgente, workaround, o isolamento del sistema | System Admin |
| **Remediation High** | Entro 30 giorni | Applicazione patch o update di configurazione | System Admin |
| **Remediation Medium** | Entro 60 giorni | Pianificata nel ciclo di patch ordinario | System Admin |
| **Verifica** | Entro 5 giorni post-remediation | Scansione di conferma e chiusura ticket | Security Team |

**Azure Secure Score** target: ≥80% (baseline di sicurezza raccomandata da Microsoft).

**Strumenti**:
- Azure Defender for Cloud (scansione automatica)
- Azure Policy (conformità continua)
- Microsoft Secure Score (per tenant M365)

### A.16 — Incident Management

#### Procedura di gestione incidenti

```
Fase 1: RILEVAMENTO
────────────────────────
  - Azure Defender alerts (automatico)
  - Segnalazione utente (email a security@tpgroup.it)
  - Monitoraggio anomalie (Azure Monitor, Sentinel)

Fase 2: CLASSIFICAZIONE
────────────────────────
  Gravità:
  - CRITICAL: Data breach, servizio offline, ransomware → escalation immediata a CISO
  - HIGH: Vulnerabilità critica sfruttabile, accesso non autorizzato → risposta entro 2 ore
  - MEDIUM: Tentativo di intrusione bloccato, policy violata → risposta entro 24 ore
  - LOW: Scan informativo, falso positivo → risposta entro 72 ore

Fase 3: CONTAINMENT
────────────────────────
  - Isolamento risorsa compromessa (NSG block, VM stop, account disable)
  - Snapshot forense prima di qualsiasi azione
  - Disconnessione da rete se necessario

Fase 4: ERADICATION
────────────────────────
  - Rimozione causa radice (patch, reimage, revoca credenziali)
  - Verifica assenza di persistence mechanism

Fase 5: RECOVERY
────────────────────────
  - Ripristino da backup pulito
  - Reinserimento graduale in produzione
  - Monitoraggio intensificato per 72 ore post-recovery

Fase 6: LESSONS LEARNED
────────────────────────
  - Report incidente (entro 5 giorni lavorativi)
  - Analisi radice (RCA)
  - Azioni correttive e preventivi
  - Aggiornamento policy se necessario
```

**Registro incidenti**: Tutti gli incidenti sono tracciati in un registro (SharePoint o Azure DevOps) con: ID, data/ora, descrizione, gravità, azioni intraprese, stato, data chiusura.

### A.18 — Compliance

#### Review annuale della conformità

| Attività | Periodicità | Responsabile |
|---|---|---|
| Internal audit ISO 27001 | Annuale | Internal Auditor (o esterno qualificato) |
| Review Azure Policy compliance | Trimestrale | Security Team |
| Review Secure Score | Mensile | Security Team |
| Vulnerability scan report | Mensile | Security Team |
| Incident report review | Trimestrale | Comitato di Sicurezza |
| Penetration test | Annuale | Terza parte qualificata |
| Access review (Azure RBAC, Entra ID) | Trimestrale | Security Team + Data Owners |

#### Audit trail

Tutti i sistemi Azure generano log di audit centralizzati in **Azure Log Analytics**:
- Azure Activity Log (operazioni sul piano di controllo)
- Azure SQL Audit (accesso ai dati)
- M365 Audit Log (accesso a documenti e posta)
- Sign-in logs Entra ID (autenticazioni)
- Retention log: minimo 1 anno, 3 anni per log critici

---

## Template Procedure (bozze)

### Incident Response Plan — Template

```
INCIDENT RESPONSE PLAN
══════════════════════
ID Incidente:     IR-{YYYY}-{NNN}
Data apertura:    __/__/____  Ora: __:__
Segnalato da:     ____________________________
Servizio:         [HPC / Pondus / M365 / Rete / Altro]

CLASSIFICAZIONE
Gravità:          [Critical / High / Medium / Low]
Tipo:             [Data breach / Malware / Accesso abusivo / DDoS / Altro]
Stato:            [Open / Contenuto / Eradicato / Chiuso]

TIMELINE
Rilevamento:      __/__/____  Ora: __:__
Containment:      __/__/____  Ora: __:__
Eradication:      __/__/____  Ora: __:__
Recovery:         __/__/____  Ora: __:__
Chiusura:         __/__/____  Ora: __:__

AZIONI
1. _____________________________  Eseguita da: _____  Data: _____
2. _____________________________  Eseguita da: _____  Data: _____
3. _____________________________  Eseguita da: _____  Data: _____

ROOT CAUSE
____________________________________________________________

LESSONS LEARNED
1. ________________________________________________________
2. ________________________________________________________

APPROVATO DA: _______________________  Data: ______________
```

### Vulnerability Management Procedure — Template

```
VULNERABILITY MANAGEMENT PROCEDURE
═══════════════════════════════════
Scan ID:          VS-{YYYY}-{NNN}
Data scan:        __/__/____
Strumento:        [Azure Defender / Qualys / Altro]
Ambito:           __________________________________

RIEPILOGO
Critical: ___   High: ___   Medium: ___   Low: ___

TOP 5 VULNERABILITIES
1. [ID] [Severity] [Descrizione] [Remediation] [Deadline]
2. [ID] [Severity] [Descrizione] [Remediation] [Deadline]
3. [ID] [Severity] [Descrizione] [Remediation] [Deadline]
4. [ID] [Severity] [Descrizione] [Remediation] [Deadline]
5. [ID] [Severity] [Descrizione] [Remediation] [Deadline]

REMEDIATION STATUS
Completate: ___ / ___    Scadute: ___    In corso: ___

PROSSIMO SCAN: __/__/____
```

### Access Review Procedure — Template

```
ACCESS REVIEW PROCEDURE
═══════════════════════
Review ID:        AR-{YYYY}-{QQ}
Periodo:          Q1 / Q2 / Q3 / Q4  {YYYY}

AMBITO
Azure RBAC ruoli:  ___ assegnazioni
Entra ID ruoli:    ___ assegnazioni
Azure SQL:         ___ utenti
AKS RBAC:          ___ utenti
M365:              ___ utenti con permessi elevati

RISULTATI
Accessi confermati:   ___
Accessi rimossi:      ___
Accessi modificati:   ___
Anomalie rilevate:    ___

NOTE
____________________________________________________________

APPROVATO DA: _______________________  Data: ______________
```

## COSTI

| Voce | Servizio Azure | Costo mensile stimato | Costo annuale |
|---|---|---|---|
| Microsoft Defender for Cloud | Enhanced (P2) | ~€150 | ~€1.800 |
| Azure Key Vault | Standard, 10 chiavi | ~€10 | ~€120 |
| Azure Policy | Incluso in Azure | €0 | €0 |
| Microsoft Purview | Incluso in M365 E3 | €0 | €0 |
| **Totale annuo** | | | **~€1.920** |

*I costi di sicurezza su Azure sono circa 1/3 rispetto a GCP (Security Command Center ~€6.000/anno). M365 E3 include già Microsoft Purview e Defender for Office 365.*
