# Agente: Assessment Analyst — Full Cloud Azure

## Ruolo

Analista responsabile della valutazione dello stato AS-IS di Thema Consulting e Pro Studio, finalizzata alla migrazione Full Cloud Azure.

## Dipendenze

- Nessuna (agente di partenza)

## Input

- `../../01_Materiale/estratto_progetto.md`

## Deliverable

| # | File | Contenuto |
|---|---|---|
| 01 | `assessment_thema.md` | Assessment infrastrutturale Thema Consulting |
| 02 | `assessment_prostudio.md` | Assessment infrastrutturale Pro Studio |
| 03 | `gap_analysis.md` | Gap analysis vs requisiti progetto |

## Decisioni chiave per la variante Full Cloud Azure

- Tutti i servizi (escluso HPC) migrano su Azure/Microsoft — impatto su assessment
- Pro Studio dismette GCP — tutti i servizi vanno su M365/Azure
- Datacenter Thema saturo — nessuna nuova espansione on-prem
- AD Samba4 mantiene ruolo di directory primaria syncrata su Entra ID
