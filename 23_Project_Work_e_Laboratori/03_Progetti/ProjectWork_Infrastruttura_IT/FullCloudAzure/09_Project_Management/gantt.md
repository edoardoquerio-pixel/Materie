# Gantt — Full Cloud Azure

## Diagramma

```
Attività                    | Set 1 | Set 2 | Set 3 | Set 4 | Ott 1 | Ott 2 | Ott 3 | Ott 4 | Nov 1 | Nov 2 | Nov 3 | Nov 4
                            |───────|───────|───────|───────|───────|───────|───────|───────|───────|───────|───────|───────|
1  Assessment               |███████|       |       |       |       |       |       |       |       |       |       |       |
2  Rete/VPN                 |       |███████|███████|       |       |       |       |       |       |       |       |       |
3  Sicurezza                |       |███████|███████|       |       |       |       |       |       |       |       |       |
4  HPC                      |       |       |███████|       |       |       |       |       |       |       |       |       |
5  Pondus                   |       |       |███████|███████|       |       |       |       |       |       |       |       |
6  Cloud Migration          |       |       |       |       |       |       |       |       |       |       |       |       |
  6.0 Foundation            |       |       |███████|███████|       |       |       |       |       |       |       |       |
  6.1 Posta                 |       |       |       |       |███████|███████|       |       |       |       |       |       |
  6.2 File                  |       |       |       |       |███████|███████|       |       |       |       |       |       |
  6.3 Dynamics 365          |       |       |       |       |       |███████|███████|███████|       |       |       |       |
  6.4 DevOps                |       |       |       |       |       |       |███████|███████|       |       |       |       |
  6.5 MediaWiki             |       |       |       |       |       |       |███████|       |       |       |       |       |
  6.6 Test                  |       |       |       |       |       |       |       |       |███████|███████|       |       |
  6.7 Dismissione           |       |       |       |       |       |       |       |       |       |       |███████|       |
7  Backup/DR                |       |       |       |       |       |       |███████|       |       |       |       |       |
8  Offerta                  |       |       |       |       |       |       |       |       |       |       |███████|       |
9  Formazione/Chiusura      |       |       |       |       |       |       |       |       |       |       |       |███████|
9  Affiancamento post       |       |       |       |       |       |       |       |       |       |       |       |███████|
```

## Milestone

| Milestone | Data | Criterio |
|---|---|---|
| M0 — Assessment completato | 12/09/2026 | Documenti consegnati |
| M1 — Rete attiva | 26/09/2026 | Switch, FortiGate, VLAN funzionanti |
| M2 — VPN Sede→Azure attiva | 03/10/2026 | Tunnel IPsec stabile |
| M3 — Foundation M365 | 10/10/2026 | Tenant, utenti, Entra ID pronti |
| M4 — Posta migrata | 24/10/2026 | 50 caselle su Exchange Online |
| M5 — File migrati | 24/10/2026 | SharePoint/OneDrive popolati |
| M6 — Dynamics attivo | 14/11/2026 | Sales + BC funzionanti |
| M7 — Pondus su Azure | 17/10/2026 | App Service + SQL attivi |
| M8 — DevOps attivo | 24/10/2026 | Repos migrati, pipelines CI/CD |
| M9 — Test superati | 14/11/2026 | Tutti i test OK |
| M10 — Dismissione legacy | 22/11/2026 | Piattaforme vecchie spente |
| M11 — Go-live + formazione | 05/12/2026 | Formazione completata |

## Risorse

| Ruolo | Impegno | Periodo |
|---|---|---|
| Sistemista senior | Full-time (55 giorni) | Settimane 1-12 |
| PM | Part-time (17 giorni) | Settimane 1-12 |
| Consulente Dynamics | Part-time (10 giorni) | Settimane 5-9 |
| Sviluppatore .NET | Part-time (5-15 giorni) | Settimane 3-6 (Pondus) |
