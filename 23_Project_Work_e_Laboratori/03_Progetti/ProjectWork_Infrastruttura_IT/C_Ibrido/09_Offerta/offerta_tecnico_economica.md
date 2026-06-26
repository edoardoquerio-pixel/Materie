# Offerta Tecnico/Economica — Variante Ibrida (Azure HBv4 + On-Prem Legacy + GCP)

## Premessa

Offerta per l'integrazione IT di TP Group con architettura ibrida:
8 nodi on-prem esistenti (legacy) + cluster HPC su Microsoft Azure (HBv4, InfiniBand NDR 400 Gbps)
+ servizi su Google Cloud Platform.

**Novità rispetto alla variante C originale**: gli 8 nuovi nodi on-prem precedentemente previsti
vengono sostituiti da **5 nodi Azure HBv4 in cloud**, eliminando ~€235.000 di CAPEX e
offrendo InfiniBand NDR 400 Gbps (vs 200 Gbps on-prem) a un costo operativo inferiore.

## Riepilogo Variante

| Elemento | Valore |
|---|---|
| **Architettura** | HPC ibrido: 8 nodi on-prem legacy + Azure HBv4 cloud + GCP servizi |
| **HPC (nuovi nodi)** | **Azure HBv4 (InfiniBand NDR 400 Gbps)** — 5 nodi (3 Reserved + 2 spot) |
| **HPC (legacy)** | 8 nodi on-prem esistenti (InfiniBand, MLNX OFED) |
| **Pondus** | Cloud Run + Cloud SQL (GCP) |
| **Posta/Collab** | Google Workspace |
| **Identità** | Samba4 AD on-prem + GCDS sync |
| **DR** | Cloud (Pondus multi-regione) + on-prem (co-location HPC) |
| **Backup** | NAS QNAP (on-prem) + Cloud Storage (GCP) |
| **Durata** | 12 settimane implementazione, 3 anni ciclo di vita |

## Budget Dettagliato

### Costi una tantum (implementazione + HW residuo)

| Voce | Importo | Note |
|---|---|---|
| **Rete** | | |
| FortiGate 100F + licenze | €6.200 | |
| Switch, AP, installazione | €8.800 | |
| **HPC on-prem (legacy)** | | |
| Solo manutenzione nodi esistenti | €0 | Nessun nuovo acquisto |
| **Co-location HPC** | | |
| Set-up co-location (22U) | €5.000 | Solo per nodi legacy |
| **Servizi professionali** | | |
| Setup Azure VNet + VPN Gateway | €0 | Incluso in Azure |
| Setup CycleCloud + Slurm | €3.000 | Configurazione cluster Azure |
| Migrazione job HPC on-prem → Azure | €8.000 | Re-indirizzamento carichi |
| Project Management | €7.800 | 12 settimane × €650/gg PM |
| Formazione | €3.000 | |
| **Totale una tantum** | **€41.800** | |

### Costi operativi annui

| Voce | Importo/anno | Note |
|---|---|---|
| **HPC Azure HBv4** (3 Reserved + 2 spot, 12h×220gg) | ~€28.992 | 5 nodi, utilizzo realistico |
| Azure Managed Lustre (10 TB) | ~€17.100 | Filesystem parallelo |
| Azure Blob Storage Hot (20 TB) | ~€2.280 | Archive risultati |
| Azure VPN Gateway + networking | ~€5.400 | Connettività Azure ↔ sede/GCP |
| Energia HPC on-prem (8 nodi legacy) | ~€12.000 | Solo nodi esistenti (metà) |
| Canone co-location (ridotto) | €8.000 | Solo spazio nodi legacy |
| Fibra + 4G | €6.960 | |
| FortiGate UTM | €900 | |
| GCP servizi (Pondus, backup, DR) | ~€44.000 | Cloud Run, Cloud SQL, storage |
| Google Workspace (50 utenti) | €7.200 | |
| Odoo Enterprise (50 utenti) | €14.940 | |
| BitBucket (50 utenti) | ~€1.700 | |
| Manutenzione sistemista | €15.000 | |
| **Totale annuo** | **~€164.472** | |

### Riepilogo Budget

| Voce | Importo |
|---|---|
| Una tantum (HW + implementazione) | €41.800 |
| Ricorrente anno 1 | ~€164.472 |
| Ricorrente anno 2-3 | ~€328.944 |
| **Totale 3 anni** | **~€535.216** |
| **Budget cliente** | **€520.000 + €181.000 = €701.000** |
| **Delta** | **~€165.784 sotto budget** ✅ |

### Confronto: Variante C originale vs evoluta (con Azure HBv4)

| Voce | C originale (16 on-prem + GCP) | C evoluta (8 on-prem + Azure HBv4 + GCP) | Risparmio |
|---|---|---|---|
| Una tantum | €285.800 | **€41.800** | **+€244.000** |
| Ricorrente/anno | ~€129.700 | ~€164.472 | -€34.772/anno |
| **Totale 3 anni** | **~€674.900** | **~€535.216** | **+€139.684** |
| InfiniBand | 200 Gbps HDR | **400 Gbps NDR** | **Prestazioni superiori** |
| Gestione HW | 16 nodi on-prem | **8 nodi legacy** | **-50%** |

> L'evoluzione con Azure HBv4 riduce il costo totale del 21% (~€139.684 risparmio)
> offrendo al contempo InfiniBand di fascia superiore (400 Gbps vs 200 Gbps) e
> zero CAPEX per nuovi server.

*Nota: variante ibrida ottimale per chi mantiene il controllo HPC legacy on-prem
e sfrutta Azure per potenza HPC moderna a costo variabile.*
