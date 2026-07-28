# Gantt — Full Cloud Azure

## Diagramma

```
Attività                      | Set 1 | Set 2 | Set 3 | Set 4 | Ott 1 | Ott 2 | Ott 3 | Ott 4 | Nov 1 | Nov 2
                              |───────|───────|───────|───────|───────|───────|───────|───────|───────|───────|
1  Assessment                 |███████|       |       |       |       |       |       |       |       |       |
2  Rete/VPN                   |███████|███████|       |       |       |       |       |       |       |       |
3  Sicurezza                  |███████|███████|       |       |       |       |       |       |       |       |
4  HPC (burst setup) F5b      |       |       |       |       |███████|███████|       |       |       |       |
5  Pondus (percorso separato) |       |       |███████|███████|       |       |       |       |       |       |
6  Cloud Migration            |       |       |       |       |       |       |       |       |       |       |
  6.0 Foundation (F0)         |███████|███████|       |       |       |       |       |       |       |       |
  6.1 Posta (F1)              |       |       |███████|███████|███████|       |       |       |       |       |
  6.2 File (F2)               |       |       |███████|███████|       |       |       |       |       |       |
  6.3 Dynamics 365 (F3)       |       |       |       |███████|███████|███████|███████|███████|       |       |
  6.4 DevOps (F4)             |       |       |       |       |███████|███████|       |       |       |       |
  6.5 MediaWiki (F5)          |       |       |       |       |███████|       |       |       |       |       |
  6.6 Test (F6)               |       |       |       |       |       |       |       |███████|███████|       |
  6.7 Dismissione (F7)        |       |       |       |       |       |       |       |       |       |███████|
7  Backup/DR                  |       |       |       |       |       |       |███████|███████|       |       |
8  Offerta                    |       |       |       |       |       |       |       |       |       |███████|
9  Formazione/Chiusura        |       |       |       |       |       |       |       |       |       |███████|
   Affiancamento post         |       |       |       |       |       |       |       |       |       |███████|
```

*Nota: Settimane 11-12 = Affiancamento post-migrazione (2 settimane)*

## Milestone (allineati a 08_Cronoprogramma.md)

| Milestone | Data | Criterio |
|---|---|---|
| M0 — Foundation completata | 14/09/2026 | Tenant, utenti, Entra ID, Conditional Access pronti |
| M1 — Posta migrata | 05/10/2026 | 50 caselle su Exchange Online funzionanti |
| M2 — File migrati | 28/09/2026 | SharePoint/OneDrive popolati e validati |
| M3 — Dynamics 365 attivo | 26/10/2026 | Sales + BC funzionanti, dati migrati |
| M4 — Azure DevOps attivo | 12/10/2026 | Repos migrati, pipeline CI/CD operative |
| M5 — MediaWiki attiva | 05/10/2026 | VM B2s in produzione, contenuto migrato |
| M5b — HPC burst pronto | 12/10/2026 | CycleCloud + Lustre + nodi SPOT operativi |
| M6 — Test superati | 02/11/2026 | Tutti i test di accettazione OK |
| M7 — Dismissione legacy | 09/11/2026 | Piattaforme vecchie (Zimbra, NextCloud, ecc.) spente |

## Risorse

| Ruolo | Impegno | Periodo |
|---|---|---|
| Sistemista senior | Full-time (55 giorni) | Settimane 1-12 |
| PM | Part-time (17 giorni) | Settimane 1-12 |
| Consulente Dynamics | Part-time (10 giorni) | Settimane 4-8 |
| Sviluppatore .NET | Part-time (5-15 giorni) | Settimane 3-6 (Pondus) |