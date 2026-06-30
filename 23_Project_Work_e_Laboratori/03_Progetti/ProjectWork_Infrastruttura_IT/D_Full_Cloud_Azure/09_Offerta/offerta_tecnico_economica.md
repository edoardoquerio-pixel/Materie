# Offerta Tecnico/Economica — Variante Full Cloud Azure

## Premessa

Offerta per l'integrazione IT di TP Group (Thema Consulting + Pro Studio)
su infrastruttura interamente Microsoft Azure.

## Riepilogo Variante

| Elemento | Valore |
|---|---|
| **Architettura** | 100% su Microsoft Azure |
| **HPC** | **HB176-96rs v4 (InfiniBand NDR 400 Gbps)** — 8 nodi (3 Reserved + 5 spot) |
| **Pondus** | **AKS con Windows nodepool** + Azure SQL (Hybrid Benefit) |
| **Posta/Collab** | **Microsoft 365 Business Premium** (50 utenti) |
| **Identità** | Microsoft Entra ID Connect (da Samba4 AD) |
| **DR** | West Europe (primario) + North Europe (DR) |
| **Backup** | Azure Backup + Blob Storage GRS |
| **Durata** | 12 settimane implementazione, 3 anni ciclo vita |

## Budget Dettagliato

### Costi una tantum (implementazione)

| Voce | Importo | Note |
|---|---|---|
| Upgrade connettività sede (1 Gbps + failover 4G/5G) | €6.000 | Fibra dedicata + backup |
| Setup Azure VNet + VPN Gateway | €0 | Incluso in Azure |
| Configurazione M365 (estensione a 50 utenti) | €500 | Onboarding 20 utenti Pro Studio |
| Migrazione dati (assistenza 10 gg/uomo) | €5.000 | Trasferimento file, DB, configurazioni |
| Migrazione Profis→Odoo | €3.000 | 6 gg sistemista (€500/gg) |
| Formazione personale (2 sessioni) | €3.000 | 1 giornata in presenza |
| Project Management | €7.800 | 12 settimane × €650/gg PM |
| **Totale una tantum** | **€25.300** | |

### Costi HW/SW/Cloud (primo anno)

| Voce | Servizio | Importo | Note |
|---|---|---|---|
| **Compute HPC** | 8 HB176-96rs v4 (3 nodi 3Y Reserved + 5 spot, 12h×220gg) | ~€43.960 | 768 core, 6.144 GB RAM, 8 GB/core ✅ |
| **Front-end HPC** | Standard_D8s_v5 | ~€300 | |
| **Azure Managed Lustre** | 10 TB filesystem parallelo | ~€17.000 | Throughput >100 GB/s |
| **Egress dati HPC** | Download risultati simulazione (~300 GB/mese) | ~€1.500 | Nuovo — non preventivato in precedenza |
| **Azure SQL (Pondus)** | 16 vCPU BC + failover, Hybrid Benefit | ~€39.792 | BC tier ~2.7× GP; failover group incluso |
| **AKS Windows (Pondus)** | 1 nodo Standard_D2s_v3 + control plane | ~€6.500 | Windows nodepool per compatibilità legacy |
| **Networking** | VPN GW, NAT, WAF, Bastion, DNS | ~€5.400 | |
| **Storage/Backup** | Blob GRS 20TB Hot, Azure Backup, Site Recovery | ~€9.700 | Storage: ~€6.050 (GRS $0,037/GB); Backup+ASR: ~€3.650 |
| **Sicurezza** | Defender for Cloud, Key Vault | ~€1.800 | |
| **Microsoft 365 Business Premium** | 50 utenti (€22/utente/mese) | ~€13.200 | Upgrade Thema Basic→Premium + nuovi Pro Studio |
| **Odoo Enterprise** | 50 utenti | €14.940 | Sostituisce Profis + SugarCRM + Kimai |
| **Azure DevOps + BitBucket** | Versioning Git (Basic 5 utenti + BitBucket) | ~€2.060 | Sostituzione GiTea |
| **Totale ricorrente anno 1** | | **~€156.152** | |

### Riepilogo Budget 3 Anni

| Voce | Importo |
|---|---|---|
| Una tantum (implementazione) | €25.300 |
| Ricorrente anno 1 (cloud + SaaS) | ~€156.152 |
| Ricorrente anno 2-3 (cloud + SaaS) | ~€156.152/anno × 2 = ~€312.304 |
| **Totale 3 anni** | **~€493.756** |
| Extra manodopera (sistemista €500/gg × 46gg + PM €650/gg × 60gg + sviluppatore €450/gg × 40gg) | ~€77.000 |
| **Totale complessivo 3 anni** | **~€570.756** |

**Dettaglio extra manodopera:**

| Voce | Giorni | Costo/gg | Totale |
|---|---|---|---|
| Sistemista (setup infrastruttura, migrazioni) | 46 | €500 | €23.000 |
| Project Manager (coordinamento, reportistica) | 60 | €650 | €39.000 |
| Sviluppatore .NET (refactoring Pondus per AKS) | 40 | €450 | €18.000 |
| **Totale extra manodopera** | | | **~€77.000** |

> **Nota**: I costi di manodopera includono 6 giorni aggiuntivi di sistemista per la migrazione Profis→Odoo (€3.000) rispetto alla stima originale (40gg → 46gg). Il costo sviluppatore .NET è invariato (40gg × €450/gg).

### Confronto con Budget Cliente

| Voce | Importo |
|---|---|
| **Budget cliente** | €520.000 + €181.000 extra = **€701.000** |
| **Costo Variante Full Cloud Azure** | **~€570.756** |
| **Margine residuo** | **~€130.244** ✅ |

> La Variante Full Cloud Azure rientra **comodamente** nel budget cliente, con un margine di ~€130k per imprevisti o espansioni future.

## Dettaglio modifiche rispetto a preventivo precedente

| Voce | Precedente | Attuale | Delta | Motivazione |
|---|---|---|---|---|---|
| Nodi HPC | 5 × HB176-96rs (880 core) | **8 × HB176-96rs (768 core)** | — | Constrained vCPU: 96 core, 8 GB/core ✅ |
| Compute HPC (anno) | ~€28.700 (5 HB176, 3R+2S) | **~€43.960** (8 HB176-96rs, 3R+5S) | **+€15.260** | $7,20/h on-demand (non $3,60); 3Y Rsvd $3,60/h |
| Managed Lustre | ~€8.100 | **~€17.000** | **+€8.900** | Allineamento costo reale listino |
| Egress HPC | €0 | **~€1.500** | **+€1.500** | Nuovo — dati simulazione |
| Pondus runtime | Container Apps ~€3.000 | **AKS Windows ~€8.160** | **+€5.160** | Windows container D4s_v3 (per legacy Pondus) |
| Azure SQL MI | GP Hybrid ~€14.400 | **BC Hybrid + failover ~€39.792** | **+€25.392** | Business Critical + Failover Group automatico (ISO 27001) |
| Storage/Backup | Blob GRS 20TB + Backup + ASR ~€4.600 | **~€9.700** | **+€5.100** | Prezzo GRS reale ($0,037/GB mensile) + Backup + ASR |
| Azure Cache for Redis | — | **~€900** | **+€900** | Nuovo — caching per ridurre carico DB |
| M365 (50 utenti) | ~€10.200 | **~€13.200** | **+€3.000** | Upgrade Business Premium (requisito ISO 27001) |
| Una tantum | €22.300 | **€25.300** | **+€3.000** | Migrazione Profis→Odoo |
| Extra manodopera | ~€74.000 | **~€77.000** | **+€3.000** | 6 gg sistemista per Odoo |
| **Totale 3 anni** | **~€374.520** | **~€570.756** | **+€196.236** | Budget cliente €701k; margine +€130k |

## Risparmi rispetto a Variante Full Cloud GCP

| Voce | GCP | Azure | Risparmio |
|---|---|---|---|
| **Posta/Collab** | Google Workspace €7.200/anno | **M365 già presente €0 migrazione** | **€7.200/anno** |
| **Licenza SQL** | Cloud SQL full price ~$18.000/anno | **Hybrid Benefit -55%** primario + secondario failover ~$21.780/anno | **~$3.780/anno extra** (2 istanze per DR) |
| **Compute HPC/h** | H4D $13,74/h | **HB176-96rs $7,20/h** | **-48%** |
| **InfiniBand** | Cloud RDMA 200 Gbps (giustificazione no VM) | **InfiniBand NDR 400 Gbps nativo** | **Nessuna eccezione** |
| **Sicurezza** | Security Command Center ~€6.000/anno | **Defender for Cloud ~€1.800/anno** | **~€4.200/anno** |
| **Costi migrazione posta** | Migrazione Zimbra→Workspace | **Nessuna (M365 già in uso)** | **Risparmio significativo** |

> **Differenziale Variante D vs A**: Costo totale 3 anni Variante D ~€570.756 vs Variante A (GCP) ~€549.720 = **+€21.036 (+4%)**. Azure rimane competitivo grazie a InfiniBand nativo e M365 già presente, ma il corretto prezzo HPC HB176-96rs riduce il vantaggio economico. Il differenziale è compensato da: nessuna migrazione posta (M365 già in uso), InfiniBand nativo senza eccezioni, e service level ISO 27001 nativo.

## Note

- Tutti i prezzi cloud sono espressi in EUR (cambio $1 = €0,92)
- I costi HPC sono calcolati su **utilizzo realistico** (12 ore/giorno × 220 giorni lavorativi), non 24/7/365
- Azure Hybrid Benefit applicato su Azure SQL: la licenza SQL Server on-premise esistente viene riutilizzata su entrambe le istanze Azure SQL (primaria Business Critical + secondaria failover) con sconto ~55%
- Azure Cache for Redis Standard C1 (~€75/mese) aggiunto come layer di caching per ridurre la latenza delle query e il carico sul DB
- Microsoft 365 Business Premium (€22/utente/mese) copre: Exchange, SharePoint, Teams, Defender for Office 365, Purview
- L'estensione M365 da 30 a 50 utenti include l'upgrade delle 30 licenze Thema da Business Basic a Business Premium
- Costi Odoo, BitBucket invariati rispetto a Variante GCP (Odoo €14.940, BitBucket €1.700)
- Azure DevOps Basic (~€360/anno per 5 utenti) si aggiunge a BitBucket per la migrazione GiTea
- *Budget cliente: €520.000 + €181.000 extra = €701.000. Variante D ~€570.756 (rientra con margine ~€130k).*
