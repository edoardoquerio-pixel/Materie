# Requisiti ISO 27001 — Copertura Full Cloud Azure

## Perimetro di certificazione

ISO/IEC 27001 per TP Group — tre macro-aree prioritarie:
1. **Business continuity**
2. **Disaster recovery**
3. **Sicurezza degli accessi ai dati**

## Mappatura requisiti → strumenti Azure

| # | Requisito ISO 27001 | Strumento Azure/Microsoft | Copertura |
|---|---|---|---|
| A.9.1.1 | Policy controllo accessi | **Entra ID P1** + Conditional Access | ✅ Completa |
| A.9.2.1 | Registrazione e cancellazione utenti | **Entra ID** + Lifecycle workflows | ✅ Completa |
| A.9.2.3 | Gestione privilegi | **Privileged Identity Management (PIM)** — JIT access | ✅ Completa |
| A.9.2.6 | Rimozione diritti accesso | **Entra ID** + access reviews | ✅ Completa |
| A.9.3.1 | Gestione password | **Entra ID** — password protection + self-service | ✅ Completa |
| A.9.4.2 | Autenticazione MFA | **Entra ID P1** — MFA + Conditional Access | ✅ Completa |
| A.10.1.1 | Cifratura dati a riposo | **Azure SSE AES-256** + **M365** cifratura lato server | ✅ Completa |
| A.10.1.2 | Cifratura dati in transito | **TLS 1.2+** di default su Azure/M365 | ✅ Completa |
| A.12.1.1 | Procedure operative documentate | **Azure Policy** + **Runbook** automazione | ✅ Completa |
| A.12.3.1 | Backup dei dati | **Azure Backup** + **M365 Backup** | ✅ Completa |
| A.12.4.1 | Log e monitoraggio | **Azure Monitor** + **Log Analytics** + **Sentinel** (opzionale) | ✅ Completa |
| A.12.6.1 | Gestione vulnerabilità | **Defender for Cloud** + **Defender Vulnerability Management** | ✅ Completa |
| A.13.1.1 | Controlli di rete | **NSG**, **Azure Firewall**, **VPN Gateway** | ✅ Completa |
| A.13.2.1 | Trasferimento informazioni | **TLS**, **IPsec**, **Azure Private Link** | ✅ Completa |
| A.14.1.1 | Sicurezza nei cicli di sviluppo | **Azure DevOps** + **Defender for DevOps** | ✅ Completa |
| A.16.1.1 | Gestione incidenti | **Microsoft Sentinel** + **Defender XDR** | ✅ Completa |
| A.17.1.1 | Continuità operativa | **Azure Site Recovery** + **Availability Zones** | ✅ Completa |
| A.17.1.2 | Disaster recovery | **Azure Site Recovery** — RPO 15 min, RTO < 4h | ✅ Completa |
| A.18.1.1 | Conformità normativa | **Microsoft Purview Compliance Portal** | ✅ Completa |

## Policy di sicurezza cloud

### Conditional Access (Entra ID P1)

| Policy | Effetto | Assegnazione |
|---|---|---|
| MFA per tutte le app cloud | Richiedi MFA | Tutti gli utenti |
| Accesso condizionale geografico | Blocca accesso da paesi non autorizzati | Tutti gli utenti |
| Device compliance | Blocca dispositivi non conformi | Tutti gli utenti |
| Rischi di accesso | Blocca o richiedi cambio password | Tutti gli utenti |
| Accesso admin con PIM | Accesso JIT con approvazione | Ruoli amministrativi |

### Defender for Office 365

| Protezione | Descrizione |
|---|---|
| Anti-phishing | Protezione da attacchi phishing e spoofing |
| Attachment sicuri | Sandboxing allegati in tempo reale |
| Link sicuri | Scansione URL al click |
| Anti-malware | Protezione da malware in posta e file |

## Audit e conformità

| Strumento | Frequenza |
|---|---|
| Azure Policy compliance scan | Giornaliera |
| Defender for Cloud secure score | Continua |
| Purview compliance assessment | Mensile |
| Entra ID access reviews | Trimestrale |
| Penetration test | Annuale |
