# Politica di Cifratura e Controllo Accessi

## 1. Cifratura Dati

### 1.1 Dati a riposo (at-rest)

| Servizio | Metodo | Standard |
|---|---|---|
| Azure SQL Database | Transparent Data Encryption (TDE) con chiave gestita Microsoft | AES-256 |
| Azure Managed Disks (VM MediaWiki) | Server-Side Encryption (SSE) con chiave gestita Microsoft | AES-256 |
| Azure Blob Storage (Backup) | Storage Service Encryption con chiave gestita Microsoft | AES-256 |
| Exchange Online | Cifratura lato Microsoft (BitLocker + per-file encryption) | AES-256 |
| SharePoint Online / OneDrive | Cifratura lato Microsoft (BitLocker + per-file encryption) | AES-256 |
| Dynamics 365 | Cifratura lato Microsoft con chiavi gestite | AES-256 |
| Azure DevOps | Cifratura a riposo su database e artefatti | AES-256 |

### 1.2 Dati in transito (in-transit)

| Servizio | Protocollo |
|---|---|
| Tutti gli endpoint Azure | HTTPS / TLS 1.2+ |
| M365 (Exchange, SharePoint, Teams) | TLS 1.2+ (MAPI/HTTPS) |
| VPN Sede → Azure | IPsec IKEv2 (AES-256-GCM) |
| VPN client remoto | WireGuard (ChaCha20) |
| Azure DevOps | HTTPS / TLS 1.2+ |

## 2. Controllo Accessi

### 2.1 Principi guida

- **Least privilege**: ogni utente ha solo i permessi necessari
- **Zero Trust**: verificare sempre, non fidarsi mai di nessuna richiesta
- **JIT (Just-In-Time)**: accesso amministrativo concesso solo quando necessario e per durata limitata
- **MFA obbligatorio**: per tutti gli accessi a risorse cloud

### 2.2 Ruoli e permessi

| Ruolo | Permessi | MFA | PIM |
|---|---|---|---|
| Utente standard | Posta, file, Teams, Dynamics | ✅ | — |
| Sviluppatore | Azure DevOps, ambienti di test | ✅ | — |
| Sistemista | Amministrazione Azure, M365, Entra ID | ✅ | ✅ (JIT) |
| Amministratore Dynamics | Configurazione Dynamics 365 | ✅ | ✅ (JIT) |
| Project Manager | Dashboard costi Azure, report | ✅ | — |

### 2.3 Conditional Access (Entra ID P1)

| Policy | Dettaglio |
|---|---|
| **MFA globale** | Richiedi MFA per tutte le app cloud |
| **Device compliance** | Solo dispositivi gestiti e conformi (Intune) |
| **Blocco geografico** | Blocca accessi da paesi non autorizzati |
| **Rischio utente** | Blocca o richiedi cambio password per utenti a rischio |
| **Accesso admin** | Richiedi dispositivo conforme + MFA + posizione nota |

## 3. Logging e Audit

| Fonte | Strumento | Retention |
|---|---|---|
| Entra ID audit log | Azure Monitor / Log Analytics | 30 giorni (gratuito) / 1 anno (pagamento) |
| Azure Activity Log | Azure Monitor | 90 giorni |
| M365 audit log | Microsoft Purview | 180 giorni (incluso) / 1 anno (add-on) |
| Dynamics 365 audit | Dynamics 365 auditing | 180 giorni |
| Azure SQL audit | SQL auditing / Log Analytics | 1 anno |
| Defender for Cloud alerts | Azure Sentinel (opzionale) | 90 giorni |

## 4. Piano di risposta agli incidenti

| Fase | Azione | Tempo |
|---|---|---|
| Rilevamento | Defender for Cloud alert / M365 incident alert | Tempo reale |
| Analisi | Indagine su Microsoft 365 Defender / Azure Sentinel | < 1 ora |
| Contenimento | Blocco account (Entra ID Conditional Access) / Isolamento dispositivo | < 30 min |
| Eradicazione | Rimozione minaccia (Defender) / restore da backup pulito | < 4 ore |
| Ripristino | Restore dati da backup / riattivazione account | < 8 ore |
| Post-mortem | Report incidente + azioni correttive | < 5 giorni |
