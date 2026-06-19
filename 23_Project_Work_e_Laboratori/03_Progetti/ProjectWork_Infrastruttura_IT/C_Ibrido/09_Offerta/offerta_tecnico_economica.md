# Offerta Tecnico/Economica — Variante Ibrida

## Premessa

Offerta per l'integrazione IT di TP Group con architettura ibrida:
HPC on-premise + servizi su Google Cloud + DR cloud.

## Riepilogo Variante

| Elemento | Valore |
|---|---|
| **Architettura** | HPC on-prem + servizi su GCP + DR cloud |
| **HPC** | 8 nodi esistenti + 8 nuovi on-prem (InfiniBand) |
| **Pondus** | Cloud Run + Cloud SQL (GCP) |
| **Posta/Collab** | Google Workspace |
| **Identità** | Samba4 AD on-prem + GCDS sync |
| **DR** | Cloud (Pondus multi-regione) + on-prem (co-location HPC) |
| **Backup** | NAS QNAP (on-prem) + Cloud Storage (GCP) |
| **Durata** | 12 settimane implementazione, 3 anni ciclo di vita |

## Budget Dettagliato

### Costi una tantum (implementazione + HW)

| Voce | Importo | Note |
|---|---|---|
| **Rete** | | |
| FortiGate 100F + licenze | €6.200 | |
| Switch, AP, installazione | €8.800 | |
| **HPC on-prem** | | |
| 8 nodi calcolo AMD EPYC | €180.000 | |
| InfiniBand + Ethernet | €37.000 | |
| Raffreddamento + armadio | €18.000 | |
| **Co-location HPC** | | |
| Set-up co-location (22U) | €5.000 | |
| **Servizi professionali** | | |
| Migrazione cloud + setup hybrid | €20.000 | |
| Project Management | €7.800 | |
| Formazione | €3.000 | |
| **Totale una tantum** | **€285.800** | |

### Costi operativi annui

| Voce | Importo/anno |
|---|---|
| Energia HPC on-prem (16 nodi) | ~€24.000 |
| Canone co-location | €15.000 |
| Fibra + 4G | €6.960 |
| FortiGate UTM | €900 |
| GCP servizi (Pondus, backup, DR) | ~€44.000 |
| Google Workspace (50 utenti) | €7.200 |
| Odoo Enterprise (50 utenti) | €14.940 |
| BitBucket (50 utenti) | ~€1.700 |
| Manutenzione sistemista | €15.000 |
| **Totale annuo** | **~€129.700** |

### Riepilogo Budget

| Voce | Importo |
|---|---|
| Una tantum (HW + implementazione) | €285.800 |
| Ricorrente anno 1 | ~€129.700 |
| Ricorrente anno 2-3 | ~€259.400 |
| **Totale 3 anni** | **~€674.900** |
| **Budget cliente** | **€520.000 + €181.000 = €701.000** |
| **Delta** | **~€26.100 sotto budget** |

*Nota: variante ibrida ottimale per chi vuole mantenere il controllo HPC on-prem con InfiniBand e sfruttare il cloud per servizi e DR. Budget ben allineato.*
