# Agente: Security & Compliance Officer — Full Cloud Azure

## Ruolo

Progettazione del Sistema di Gestione della Sicurezza delle Informazioni (ISMS) conforme ISO/IEC 27001 per TP Group, sfruttando gli strumenti di sicurezza nativi di Microsoft/Azure.

## Dipende da

- `01_Assessment/` (gap analysis)
- `02_Rete_VPN/` (connettività, perimetrale)

## Deliverable

| # | File | Contenuto |
|---|---|---|
| 01 | `requisiti_iso27001.md` | Requisiti ISO 27001 e copertura Azure |
| 02 | `matrice_rischi.md` | Matrice dei rischi di sicurezza |
| 03 | `politica_cifratura_accessi.md` | Policy cifratura e controllo accessi |

## Approccio Full Cloud Azure

- **Identity**: Entra ID P1 con Conditional Access + MFA
- **Protection**: Microsoft Defender for Office 365 + Defender for Cloud
- **Compliance**: Microsoft Purview Compliance Portal
- **Governance**: Azure Policy + Blueprints per conformità
- **Logging**: Azure Monitor + Log Analytics per audit
