# Offerta Tecnico/Economica — Variante On-Premise

## Premessa

Offerta per l'integrazione IT di TP Group (Thema Consulting + Pro Studio)
con infrastruttura interamente on-premise e co-location per espansione.

## Riepilogo Variante

| Elemento | Valore |
|---|---|
| **Architettura** | 100% on-premise + co-location |
| **HPC** | 8 nodi esistenti + 8 nuovi in co-location |
| **Pondus** | Server dedicato on-prem (container Docker) |
| **Posta/Collab** | Zimbra (on-prem) + Google Workspace (Pro Studio) |
| **Identità** | Samba4 AD (on-prem) |
| **DR** | Sito secondario in co-location |
| **Backup** | NAS QNAP 32 TB + replica co-location |
| **Durata** | 12 settimane implementazione, 3 anni ciclo di vita |

## Budget Dettagliato

### Costi una tantum (implementazione + HW)

| Voce | Importo | Note |
|---|---|---|
| **Rete** | | |
| FortiGate 100F + licenze 3 anni | €6.200 | |
| Switch aggregazione + accesso (×4) | €3.600 | |
| AP WiFi 6 (×4) + FortiExtender | €2.200 | |
| Cablaggio + installazione | €3.000 | |
| **HPC** | | |
| 8 nodi calcolo AMD EPYC 9474F | €180.000 | |
| Switch InfiniBand QM9700 | €25.000 | |
| Switch Ethernet 25 GbE | €8.000 | |
| Storage NFS + cavi | €16.000 | |
| **Pondus** | | |
| Server 2U (dual Xeon Silver, 128 GB, SSD+HDD) | €6.000 | |
| Licenza MS SQL Server 2022 Standard | €4.000 | |
| **Co-location** | | |
| Set-up co-location (22U, cross-connect) | €5.000 | |
| **Infrastruttura** | | |
| Armadio rack + raffreddamento InRow | €18.000 | |
| UPS 5 kVA aggiuntivo | €4.000 | |
| **Servizi professionali** | | |
| Migrazione dati + setup | €15.000 | 30 gg/uomo sistemista |
| Project Management | €7.800 | 12 settimane × €650/gg |
| Formazione | €3.000 | |
| **Totale una tantum** | **€306.800** | |

### Costi operativi annui (dal secondo anno)

| Voce | Importo/anno |
|---|---|
| Energia elettrica HPC (16 nodi + raffreddamento) | ~€24.000 |
| Energia datacenter (server, storage) | ~€8.000 |
| Manutenzione HW (garanzia estesa) | ~€10.000 |
| Canone co-location (22U + 4 kW) | €15.000 |
| Fibra 1 Gbps + 4G backup | €6.960 |
| FortiGate UTM subscription | €900 |
| Licenze MS SQL assicurance | €1.000 |
| Veeam Backup maintenance | €600 |
| Odoo Enterprise (50 utenti) | €14.940 |
| BitBucket (50 utenti) | ~€1.700 |
| Manutenzione sistemista (30gg/anno) | €15.000 |
| **Totale annuo** | **~€98.100** |

### Riepilogo Budget

| Voce | Importo |
|---|---|
| Una tantum (HW + implementazione) | €306.800 |
| Ricorrente anno 1 | ~€98.100 |
| Ricorrente anno 2-3 | ~€196.200 |
| **Totale 3 anni** | **~€601.100** |
| Extra manodopera (sistemista + PM) | Già incluso |
| **Budget cliente** | **€520.000 + €181.000 = €701.000** |
| **Delta** | **~€99.900 sotto budget** |

*Nota: costi co-location potrebbero ridursi con contratti pluriennali. Budget HPC include solo 8 nuovi nodi; i nodi esistenti rimangono in uso senza costi aggiuntivi.*
