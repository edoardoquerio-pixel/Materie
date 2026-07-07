# Matrice dei Rischi — Sicurezza Full Cloud Azure

## Matrice

| # | Rischio | Probabilità | Impatto | Priorità | Mitigazione |
|---|---|---|---|---|---|
| R01 | Compromissione credenziali utente M365 | Media | Alto | **Alta** | MFA + Conditional Access + Identity Protection. Blocco accesso da paesi non autorizzati. |
| R02 | Attacco ransomware su SharePoint/OneDrive | Bassa | Alto | **Alta** | Defender for Office 365 + retention policy + backup M365 + versioning file |
| R03 | Data leak da configurazione errata Azure | Bassa | Alto | **Alta** | Azure Policy + Defender for Cloud + NSG + Private Link per servizi critici |
| R04 | Perdita chiavi/certificati Entra ID | Bassa | Alto | **Alta** | Key Vault + backup certificati + HSM managed keys |
| R05 | Accesso non autorizzato a Dynamics 365 | Bassa | Alto | **Media** | Conditional Access + RBAC + PIM per accessi privilegiati + audit log |
| R06 | Violazione conformità ISO 27001 | Bassa | Medio | **Media** | Azure Policy compliance + Purview assessment trimestrale + penetration test annuale |
| R07 | Attacco DDoS su endpoint pubblici (Pondus, Wiki) | Media | Medio | **Media** | Azure DDoS Protection Basic (incluso) + WAF su Azure Front Door (opzionale) |
| R08 | Insider threat (dipendente con accesso eccessivo) | Bassa | Medio | **Media** | PIM (accesso JIT) + access reviews trimestrali + logging Azure Monitor |
| R09 | Phishing mirato su utenti M365 | Alta | Medio | **Alta** | Defender for Office 365 (Anti-phishing, Safe Links, Safe Attachments) + training utenti |
| R10 | Sincronizzazione AD Samba4 → Entra ID interrotta | Media | Medio | **Media** | Entra Connect Health alerting + monitoring + replica AD Samba4 |
| R11 | Malware su VM MediaWiki | Bassa | Basso | **Bassa** | Defender for Cloud + antimalware VM + backup giornaliero + snapshot |
| R12 | Costi Azure superiori al previsto per traffico egress | Media | Medio | **Media** | Budget alert Azure + Azure Cost Management + reserved instances |

## Mappa calore

```
Probabilità
    ↑
Alta    │         │         │         │
        │         │         │         │
Media   │  R09    │  R01    │         │
        │         │  R12    │         │
Bassa   │  R11    │  R06,R08│ R02,R03,│
        │         │  R10    │ R04,R05 │
        │         │         │  R07    │
        └────────┴─────────┴─────────┴──→ Impatto
          Basso     Medio      Alto
```

## Rischi eliminati dalla migrazione cloud

| Rischio on-prem | Motivo eliminazione |
|---|---|
| Guasto hardware server/VM | Azure HA nativa (SLA 99.95%) |
| Surriscaldamento datacenter | Non applicabile (nessun datacenter on-prem) |
| Furto/server room fisico | Dati in cloud, cifrati |
| Guasto UPS/batterie | Azure garantisce alimentazione ridondata |
