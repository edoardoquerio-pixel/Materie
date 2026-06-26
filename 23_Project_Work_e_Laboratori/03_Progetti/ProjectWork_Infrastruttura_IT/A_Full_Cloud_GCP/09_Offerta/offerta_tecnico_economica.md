# Offerta Tecnico/Economica — Variante Full Cloud GCP (HPC su Azure)

## Premessa

Offerta per l'integrazione IT di TP Group (Thema Consulting + Pro Studio)
con architettura **multi-cloud**: servizi su Google Cloud Platform (Pondus, Workspace,
storage) + cluster HPC su Microsoft Azure (HBv4, InfiniBand NDR 400 Gbps).

## Riepilogo Variante

| Elemento | Valore |
|---|---|
| **Architettura** | Multi-cloud: GCP (servizi) + Azure (HPC) |
| **HPC** | **Azure HBv4 (InfiniBand NDR 400 Gbps)** — 5 nodi (3 Reserved + 2 spot) |
| **Pondus** | Cloud Run + Cloud SQL (GCP) |
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
| Setup VPC + Cloud VPN (GCP) | €0 | Incluso in GCP |
| Setup Azure VNet + VPN Gateway | €0 | Incluso in Azure |
| Configurazione Google Workspace (50 utenti) | €1.000 | Onboarding + migrazione posta |
| Migrazione dati (assistenza 10 gg/uomo) | €5.000 | Trasferimento file, DB, configurazioni |
| Formazione personale (2 sessioni) | €3.000 | 1 giornata in presenza |
| Project Management | €7.800 | 12 settimane × €650/gg PM |
| **Totale una tantum** | **€22.800** | |

### Costi HW/SW/Cloud (primo anno)

| Voce | Importo | Provider |
|---|---|---|
| **HPC — Azure HBv4** (3 Reserved + 2 spot, 12h×220gg) | ~€28.992 | **Azure** |
| Azure Managed Lustre (10 TB) | ~€17.100 | **Azure** |
| Azure Blob Storage Hot (20 TB) | ~€2.280 | **Azure** |
| Azure VPN Gateway Active-Active | ~€13.716 | **Azure** |
| Cloud Run (Pondus) | ~€3.400 | GCP |
| Cloud SQL (Pondus) | ~€17.100 | GCP |
| Cloud VPN (GCP side, HA VPN) | ~€1.800 | GCP |
| Cloud Storage (backup) | ~€3.900 | GCP |
| Cloud Armor (WAF) | ~€1.100 | GCP |
| Google Workspace (50 utenti Business) | €7.200 | GCP |
| Odoo Enterprise (50 utenti) | €14.940 | SaaS |
| BitBucket (50 utenti) | ~€1.700 | SaaS |
| Sicurezza GCP (SCC + KMS) | ~€5.800 | GCP |
| Sicurezza Azure (Defender for Cloud) | ~€1.800 | Azure |
| **Totale ricorrente primo anno** | **~€120.828** | |

### Riepilogo Budget

| Voce | Importo |
|---|---|
| Una tantum (implementazione) | €22.800 |
| Ricorrente anno 1 (cloud + SaaS) | ~€120.828 |
| Ricorrente anno 2-3 (cloud + SaaS) | ~€120.828/anno × 2 = ~€241.656 |
| **Totale 3 anni** | **~€385.284** |
| Extra manodopera (sistemista €500/gg × 60gg + PM €650/gg × 60gg) | €69.000 |
| **Totale complessivo 3 anni** | **~€454.284** |

*NB: Budget cliente: €520.000 + €181.000 extra = €701.000. Variante A multi-cloud ~€454.284 (rientra nel budget).*
*Costi Azure calcolati su utilizzo realistico HPC (12h×220gg).*
*Costi cloud in USD convertiti a €1 = $1,05.*

### Differenza rispetto a Variante A originale (solo GCP)

| Voce | A originale (GCP H4D) | A multi-cloud (Azure HPC + GCP) | Risparmio |
|---|---|---|---|
| HPC compute/anno | ~€82.300 (C2 con CUD) | **~€28.992 (HBv4 Reserved+Spot)** | **~€53.308/anno** |
| Networking/anno | ~€3.200 | ~€15.516 (VPN multi-cloud) | -€12.316/anno |
| **Delta annuo** | | | **~€40.992 risparmio** |
| **Delta 3 anni** | | | **~€122.976 risparmio** |
