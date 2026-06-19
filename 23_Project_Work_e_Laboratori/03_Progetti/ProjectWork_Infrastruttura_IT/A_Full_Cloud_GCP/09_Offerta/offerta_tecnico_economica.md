# Offerta Tecnico/Economica — Variante Full Cloud GCP

## Premessa

Offerta per l'integrazione IT di TP Group (Thema Consulting + Pro Studio)
su infrastruttura interamente Google Cloud Platform (GCP).

## Riepilogo Variante

| Elemento | Valore |
|---|---|
| **Architettura** | 100% su Google Cloud |
| **HPC** | Istanze C2 su GCP (8+8 nodi) — InfiniBand non disponibile |
| **Pondus** | Cloud Run + Cloud SQL (SQL Server) |
| **Posta/Collab** | Google Workspace |
| **Identità** | GCDS sync + Workspace |
| **DR** | Multi-regione GCP (us-central1 + europe-west4) |
| **Backup** | Cloud Storage + Cloud SQL PITR |
| **Durata** | 12 settimane implementazione, 3 anni ciclo di vita |

## Budget Dettagliato

### Costi una tantum (implementazione)

| Voce | Importo | Note |
|---|---|---|
| Upgrade connettività sede (1 Gbps) | €6.000 | Fibra dedicata + failover 4G |
| Setup VPC + Cloud VPN | €0 | Incluso in GCP |
| Configurazione Google Workspace (50 utenti) | €1.000 | Onboarding + migrazione posta |
| Migrazione dati (assistenza 10 gg/uomo) | €5.000 | Trasferimento file, DB, configurazioni |
| Formazione personale (2 sessioni) | €3.000 | 1 giornata in presenza |
| Project Management | €7.800 | 12 settimane × €650/gg PM |
| **Totale una tantum** | **€22.800** | |

### Costi HW/SW/Cloud (primo anno)

| Voce | Importo | Note |
|---|---|---|
| Istanze HPC C2 (8 nodi, CUD 1 anno) | ~$86.400 | ~€82.300 |
| Front-end + storage HPC | ~$12.600 | ~€12.000 |
| Cloud SQL (Pondus) | $18.000 | ~€17.100 |
| Cloud Run (Pondus) | $3.600 | ~€3.400 |
| Cloud VPN + NAT + DNS | $3.360 | ~€3.200 |
| Cloud Storage (backup) | $4.104 | ~€3.900 |
| Cloud Armor (WAF) | $1.200 | ~€1.100 |
| Google Workspace (50 utenti Business) | €7.200 | |
| Odoo Enterprise (50 utenti) | €14.940 | Sostituzione Profis |
| BitBucket (50 utenti) | ~$1.800 | ~€1.700 |
| Sicurezza (SCC + KMS) | $6.120 | ~€5.800 |
| **Totale ricorrente primo anno** | | **~€152.640** |

### Riepilogo Budget

| Voce | Importo |
|---|---|
| Una tantum (implementazione) | €22.800 |
| Ricorrente anno 1 (cloud + SaaS) | ~€152.640 |
| Ricorrente anno 2-3 (cloud + SaaS) | ~€152.640/anno × 2 = ~€305.280 |
| **Totale 3 anni** | **~€480.720** |
| Extra manodopera (sistemista €500/gg × 60gg + PM €650/gg × 60gg) | €69.000 |
| **Totale complessivo 3 anni** | **~€549.720** |

*NB: Budget cliente: €520.000 + €181.000 extra = €701.000. Variante A ~€549.720 (rientra nel budget).*
*Costi cloud in USD convertiti a €1 = $1,05.*
*CUD (Committed Use Discount) 1 anno per istanze HPC.*
