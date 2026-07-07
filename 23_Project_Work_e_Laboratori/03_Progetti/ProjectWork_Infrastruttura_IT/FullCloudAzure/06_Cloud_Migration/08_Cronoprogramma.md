# 08 — Cronoprogramma

> **Documento:** Cronoprogramma della migrazione Full Cloud Azure TP Group  
> **Data:** Luglio 2026

---

## Fasi e tempistiche

| Fase | Descrizione | Settimane | Durata | Deliverable |
| --- | --- | --- | --- | --- |
| **F0** | Foundation | 1-2 | 2 settimane | Tenant M365 attivo, Entra ID configurato, utenti creati, VNet e VPN Gateway pronti |
| **F1** | Posta | 3-5 | 3 settimane | Exchange Online attivo per tutti i 50 utenti, MX puntato, Zimbra/GWS dismessi |
| **F2** | File | 3-4 | 2 settimane | SharePoint/OneDrive attivo, dati NextCloud + Drive migrati |
| **F3** | Dynamics 365 | 4-8 | 5 settimane | Sales + BC attivi, dati CRM/ERP/timesheet migrati |
| **F4** | Azure DevOps | 5-6 | 2 settimane | Repos migrati, pipelines funzionanti |
| **F5** | Media Wiki | 5 | 1 settimana | Media Wiki su VM Azure attivo, DNS puntato |
| **F6** | Test | 8-9 | 2 settimane | Test di accettazione superati |
| **F7** | Dismissione | 10 | 1 settimana | Piattaforme legacy spente, report finale |

---

## Gantt

```
Settimana:        1   2   3   4   5   6   7   8   9   10
                  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
F0 Foundation     │███│███│   │   │   │   │   │   │   │   │
F1 Posta          │   │   │███│███│███│   │   │   │   │   │
F2 File           │   │   │███│███│   │   │   │   │   │   │
F3 Dynamics       │   │   │   │███│███│███│███│███│   │   │
F4 Azure DevOps   │   │   │   │   │███│███│   │   │   │   │
F5 Media Wiki     │   │   │   │   │███│   │   │   │   │   │
F6 Test           │   │   │   │   │   │   │   │███│███│   │
F7 Dismissione    │   │   │   │   │   │   │   │   │   │███│
                  └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
```

---

## Tabella milestone

| Milestone | Data prevista | Criterio di completamento |
| --- | --- | --- |
| M0 — Foundation completata | Fine settimana 2 | Tenant M365 attivo, Entra ID configurato, utenti creati, VPN funzionante |
| M1 — Posta migrata | Fine settimana 5 | 50 caselle su Exchange Online, MX puntato, Zimbra in lettura |
| M2 — File migrati | Fine settimana 4 | SharePoint/OneDrive popolati, NextCloud in lettura |
| M3 — Dynamics attivo | Fine settimana 8 | Sales + BC attivi, dati migrati, test pilota superati |
| M4 — DevOps attivo | Fine settimana 6 | Repos migrati, pipeline CI/CD funzionanti |
| M5 — Documentazione migrata | Fine settimana 5 | Media Wiki su VM Azure, DNS puntato |
| M6 — Test superati | Fine settimana 9 | Tutti i test di accettazione con esito positivo |
| M7 — Dismissione completata | Fine settimana 10 | Piattaforme legacy spente, report finale consegnato |

---

## Durata totale e note

| Parametro | Valore |
|---|---|
| **Durata totale migrazione** | **10 settimane** |
| Sovrapposizione fasi | F1/F2 parallele, F3/F4/F5 parzialmente sovrapposte |
| Risorse necessarie | 1 sistemista senior (full-time), 1 consulente Dynamics (part-time settimane 4-8), 1 PM (part-time) |
| Periodo di affiancamento | 2 settimane dopo F7 per supporto post-migrazione |
| **Pondus** | Percorso separato, non incluso in questo cronoprogramma |
