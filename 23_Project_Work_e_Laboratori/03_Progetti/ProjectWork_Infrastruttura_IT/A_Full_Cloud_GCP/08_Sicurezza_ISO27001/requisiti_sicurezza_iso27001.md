# Requisiti Sicurezza ISO 27001 — Variante Full Cloud GCP

## Premessa

La presente sezione documenta l'adeguamento tecnico della Variante Full Cloud GCP
ai requisiti ISO/IEC 27001 specificati dal cliente. La certificazione formale richiede
un audit esterno da parte di un ente accreditato; questo documento copre gli aspetti
tecnici propedeutici alla certificazione.

## Business Continuity

### Ridondanza sistemi strategici

GCP offre ridondanza nativa a livello di infrastruttura:

| Sistema | Strategia | Dettaglio |
|---|---|---|
| **Compute (HPC, Pondus)** | Multi-regione attivo/passivo | us-central1 (primario) + europe-west4 (DR) |
| **Database (Cloud SQL)** | Replica sincrona intra-regione + asincrona cross-regione | Failover automatico < 1 minuto |
| **Storage (Cloud Storage)** | Replica multi-regione (dual-region) | Dati disponibili anche in caso di disastro regione |
| **Load Balancer** | Global HTTPS LB — multi-regione attivo | Nessun single point of failure |
| **DNS** | Cloud DNS anycast | Alta disponibilità nativa |

### Ridondanza connettività

| Elemento | Configurazione |
|---|---|
| **Link sede → GCP** | Fibra 1 Gbps primario + failover 4G/5G |
| **Cloud VPN** | HA VPN con 2 tunnel IPsec attivi |
| **Cloud Interconnect** | Opzionale: Partner Interconnect per latenza ridotta |

## Disaster Recovery

| Requisito | Implementazione |
|---|---|
| Delocalizzazione backup | Cloud Storage multi-regione (us-central1 + europe-west4) |
| Fruibilità servizi clienti | Pondus multi-regione, failover automatico < 15 min |
| Procedure di restore | Runbook DR documentato, test semestrale |
| RPO servizi critici | ≤1 ora (PITR Cloud SQL) |
| RTO servizi critici | ≤15 min (Cloud SQL failover + Cloud Run) |

## Sicurezza Accessi

### Cifratura dati

| Stato | Dettaglio |
|---|---|
| **Dati in transito** | TLS 1.3 su tutti i servizi esposti (HTTPS, gRPC) |
| **Dati a riposo** | Cifratura lato server AES-256 (default GCP) |
| **Chiavi** | Cloud KMS per gestione chiavi (customer-managed encryption keys — CMEK) |
| **Endpoint** | Laptop dipendenti: BitLocker (Windows) o LUKS (Linux) — policy obbligatoria |

### Protocolli sicuri

| Servizio | Protocollo |
|---|---|
| Web application (Pondus) | HTTPS (TLS 1.3) |
| API | HTTPS + API key / OAuth 2.0 |
| SSH (VM) | SSH key-based, porta 22 |
| VPN | IPsec (IKEv2), AES-256 |
| Posta | SMTP TLS, IMAP TLS |
| DB connection | TLS 1.2+ (Cloud SQL proxy) |

### VPN

| Tipo | Configurazione |
|---|---|
| **LAN-to-LAN** | Cloud VPN (tunnel IPsec) tra FortiGate e GCP |
| **Client-to-LAN** | IAP (Identity-Aware Proxy) + VPN client per accesso completo |
| **Hybrid Cloud** | N/A (tutto su GCP) |

### Autenticazione Multi-Fattore (MFA)

- Google Workspace: Google Authenticator/Google Prompt (2FA obbligatorio per tutti)
- Cloud Console: Google 2FA obbligatorio per accesso amministrativo
- Applicazioni (Pondus): MFA basato su Firebase Auth + Google Identity Platform
- Samba4 AD: non più necessario (sostituito da Google Cloud Directory Sync + Workspace)

### Identity and Access Management (IAM)

| Principio | Implementazione |
|---|---|
| **Minimo privilegio** | Ruoli IAM predefiniti GCP, nessun ruolo primitive |
| **Separazione ruoli** | Admin infrastruttura ≠ Admin applicazione ≠ Utente |
| **Resource hierarchy** | Organization → Folder (Production/Staging/Dev) → Project |
| **Audit logging** | Cloud Audit Logs (Admin activity + Data access) |
| **Revisione periodica** | Cloud Asset Inventory + Policy Analyzer (trimestrale) |

## Bozza Policy di Sicurezza

### Principi generali

1. **Accesso basato sul minimo privilegio**: ogni utente/servizio ha solo i permessi necessari
2. **Cifratura end-to-end**: tutti i dati cifrati in transito e a riposo
3. **Autenticazione forte**: MFA obbligatorio per tutti gli accessi
4. **Audit continuo**: logging di tutti gli accessi amministrativi e dati sensibili
5. **Patch management**: aggiornamenti di sicurezza entro 7 giorni dalla pubblicazione
6. **Incident response**: procedura documentata per gestione incidenti di sicurezza

### Ruoli e responsabilità

| Ruolo | Responsabilità |
|---|---|
| **Security Officer** | Definizione policy, audit, incident response |
| **Cloud Admin** | Configurazione IAM, networking, security groups |
| **System Admin** | Patch management, hardening VM, backup verification |
| **Application Owner** | Security delle applicazioni, gestione utenti applicativi |
| **Utenti** | Rispetto policy, uso MFA, segnalazione anomalie |

### Matrice degli accessi

| Risorsa | Security Officer | Cloud Admin | System Admin | App Owner | Utente |
|---|---|---|---|---|---|
| Cloud Console | Admin | Editor | Viewer | Viewer | None |
| VM Compute | None | Editor | Owner | None | None |
| Cloud SQL | None | Editor | Viewer | Owner | None |
| Pondus App | Viewer | None | None | Editor | User |
| Backup | Viewer | Editor | Editor | Viewer | None |
| Logs (Audit) | Owner | Viewer | Viewer | None | None |

## Adeguamento ISO 27001 — Checklist

| Controllo ISO 27001 (Annex A) | Stato Variante A | Evidenza |
|---|---|---|
| A.5.1 — Information security policy | ✅ Policy bozza inclusa | Policy nel presente documento |
| A.6.1 — Internal organization | ✅ Ruoli definiti | Matrice accessi |
| A.8.2 — Information classification | 🔶 Da dettagliare | Policy classificazione in fase di definizione |
| A.9.1 — Access control | ✅ IAM + MFA | Cloud IAM + Workspace 2FA |
| A.9.4 — System and application access control | ✅ MFA obbligatorio | Firebase Auth + Google 2FA |
| A.10.1 — Cryptographic controls | ✅ Cifratura default | AES-256, TLS 1.3, CMEK |
| A.12.1 — Operational procedures | 🟡 Runbook DR, procedure restore | Documentati |
| A.12.3 — Backup | ✅ Backup automatici | Cloud SQL, snapshot, versioning |
| A.12.6 — Technical vulnerability management | 🟡 Da formalizzare | Patch management policy |
| A.13.1 — Network security management | ✅ VPN, firewall, segmentation | Cloud VPN, Firewall Rules |
| A.14.1 — Security requirements of information systems | 🟡 Security review ciclico | Da pianificare |
| A.15.1 — Supplier relationships | ✅ GCP SOC 2/ISO 27001 certified | Compliance GCP nativa |
| A.16.1 — Incident management | 🟡 Procedura base | Da completare |
| A.17.1 — Information security continuity | ✅ DR multi-regione | RPO 1h, RTO 15 min |
| A.18.1 — Compliance with legal and contractual requirements | 🟡 GDPR compliance | DPA GCP in atto, da verificare |

✅ = Coperto / 🟡 = Parzialmente coperto / 🔶 = Da implementare

## Costi sicurezza

| Voce | Servizio GCP | Costo mensile | Costo annuale |
|---|---|---|---|
| Cloud KMS (CMEK) | Gestione chiavi | ~$10 | ~$120 |
| Cloud Armor | WAF + DDoS | ~$100 | ~$1.200 |
| Cloud Audit Logs | Logging retention (1 anno) | ~$50 | ~$600 |
| Security Command Center | Premium tier | ~$500 | ~$6.000 |
| **Totale sicurezza** | | **~$660** | **~$7.920** |

*Security Command Center Premium è opzionale per il primo anno; il tier Standard è gratuito e copre i controlli base.*
