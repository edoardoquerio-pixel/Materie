# Matrice di Confronto — Varianti A / C / D

> **Nota:** La **Variante B (On-Premise)** è stata scartata. La nuova **Variante D (Full Cloud Azure)**
> sostituisce B in quanto offre InfiniBand nativo a un costo inferiore.
>
> **HPC Provider a confronto:** Azure HBv4 (InfiniBand NDR 400 Gbps) si è classificato **1°**,
> GCP H4D (Cloud RDMA Falcon 200 Gbps) 2°, AWS Hpc7a (EFA 300 Gbps, nessun scratch locale) 3° — escluso.
>
> **La soluzione HPC Azure HBv4 è stata applicata a TUTTE le varianti:**
> - **A** → HPC su Azure HBv4 (multi-cloud), servizi su GCP
> - **C** → 8 nodi on-prem legacy + Azure HBv4 + servizi GCP
> - **D** → Full Azure (già HBv4)

## Confronto Architetturale

| Criterio | A — Full Cloud GCP | C — Ibrido | D — Full Cloud Azure ⭐ |
|---|---|---|---|
| **HPC** | **Azure HBv4 (InfiniBand NDR 400 Gbps)** multi-cloud — 5 nodi (3R+2S) + GCP servizi | **8 nodi on-prem legacy + Azure HBv4 (InfiniBand NDR 400 Gbps)** — 5 nodi (3R+2S) + GCP servizi | **HBv4 (InfiniBand NDR 400 Gbps)** — 5 nodi (3 Reserved + 2 spot) |
| **Pondus** | Cloud Run + Cloud SQL | Cloud Run + Cloud SQL | **AKS con Windows nodepool + Azure SQL (Hybrid Benefit -55%)** |
| **Posta/Collab** | Google Workspace | Google Workspace | **Microsoft 365** (già presente — €0 migrazione) |
| **Identità** | GCDS → Workspace | Samba4 AD + GCDS sync | **Microsoft Entra ID Connect** (da Samba4 AD) |
| **File server** | Google Drive + Cloud Storage | Drive (collab) + NextCloud (HPC) | **OneDrive + Azure Files** |
| **Backup** | Cloud Storage multi-regione | NAS QNAP (HPC) + Cloud Storage (servizi) | **Azure Backup + Blob Storage GRS** |
| **DR** | Failover automatico GCP multi-regione | Cloud automatico (Pondus) + manuale (HPC) | **Azure Site Recovery West Europe → North Europe, RPO≤1h** |
| **Sicurezza** | GCP compliance nativa | Mista: GCP compliance + on-prem | **Defender for Cloud + Azure Policy ISO 27001** |

## Confronto Provider HPC — GCP vs Azure vs AWS

| Criterio | GCP H4D | Azure HBv4 ⭐ | AWS Hpc7a |
|---|---|---|---|
| **vCPU** | 192 | 176 | 192 |
| **RAM** | 720 GB | 768 GB | 768 GB |
| **Interconnessione** | Cloud RDMA Falcon 200 Gbps | **InfiniBand NDR 400 Gbps nativo** (ConnectX-7) | EFA 300 Gbps |
| **Latenza MPI** | ~3-5 μs | **< 2 μs** (stesso driver MLNX OFED on-prem) | ~5-10 μs |
| **Scratch NVMe locale** | 3 TB LSSD | **3,6 TB** (2×1.800+480 GB) | ❌ **Nessuno** (solo EBS) |
| **On-demand/h** | $13,74 | **$7,20** | $9,08 |
| **3Y Reserved/h** | ~$6,87 | **~$2,88** | ~$4,54 |
| **Spot/h** | ~$4,12 | **~$1,46** | ~$2,72 |
| **Compatibilità on-prem** | Binary compat Verbs | **MLNX OFED driver** (stesso stack) | EFA driver specifico |
| **Verdetto** | 2° posto — buono ma costo +91% vs Azure | **1° posto — InfiniBand nativo, costo minimo** | 3° posto — escluso (no scratch) |

## Confronto Performance HPC

| Criterio | A — Full Cloud GCP (HPC su Azure) | C — Ibrido (Azure HBv4 + on-prem) | D — Full Cloud Azure ⭐ |
|---|---|---|---|---|
| **Interconnessione** | **InfiniBand NDR 400 Gbps** (Azure) | InfiniBand 200 Gbps (on-prem) + **NDR 400 Gbps (Azure)** | **InfiniBand NDR 400 Gbps** |
| **Latenza MPI** | **< 2 μs** (HBv4) | < 2 μs (on-prem) + **< 2 μs (HBv4)** | **< 2 μs** |
| **Scratch** | **3,6 TB NVMe** (HBv4) | 1,6 TB NVMe (on-prem) + **3,6 TB NVMe (HBv4)** | **3,6 TB NVMe** |
| **Burst** | Fino a 2 nodi spot extra | Fino a 2 nodi spot extra (Azure) | Fino a 5 nodi HBv4 (3R+2S) |
| **Performance crash test** | **Eccellente** (InfiniBand nativo) | **Eccellente** (doppio InfiniBand) | **Eccellente** (InfiniBand nativo) |

## Confronto DR

| Criterio | A — Full Cloud GCP | C — Ibrido | D — Full Cloud Azure ⭐ |
|---|---|---|---|
| **RPO servizi critici** | ≤1 ora | ≤1 ora (Pondus) / ≤24 ore (HPC) | **≤1 ora** |
| **RTO servizi critici** | ≤15 min | ≤15 min (Pondus) / ≤4 ore (HPC) | **≤15 min** |
| **Failover automatico** | ✅ Sì | ✅ Parziale (Pondus sì, HPC no) | **✅ Sì (completo)** |
| **Replica** | Multi-regione GCP | NAS QNAP + Cloud Storage | **West Europe → North Europe (GRS + Site Recovery)** |
| **Test DR** | Semestrale (scriptabile) | Semestrale (misto) | **Semestrale (scriptabile via Azure Chaos Studio)** |

## Confronto Costi (3 anni)

| Voce | A — Full Cloud GCP (HPC su Azure) | C — Ibrido (Azure HBv4 + on-prem) | D — Full Cloud Azure ⭐ |
|---|---|---|---|
| Una tantum (HW + setup migrazione) | €22.800 | **€41.800** | **€25.300** |
| Extra manodopera | €69.000 | Incluso | **€77.000** |
| Ricorrente anno 1 | **~€120.828** | **~€164.472** | **~€129.152** |
| Ricorrente anno 2-3 | **~€241.656** | **~€328.944** | **~€258.304** |
| **Totale 3 anni** | **~€454.284** | **~€535.216** | **~€489.756** |
| **Delta budget (€701k)** | **+€246.716** ✅ | **+€165.784** ✅ | **+€211.244** ✅ |

### Dettaglio Costi Variante D (Azure) — estratto offerta

| Voce | Costo |
|---|---|
| **Una tantum implementazione** | **€25.300** |
| Upgrade connettività sede (1 Gbps + failover) | €6.000 |
| Configurazione M365 (estensione a 50 utenti) | €500 |
| Migrazione dati (10 gg/uomo) | €5.000 |
| Migrazione Profis→Odoo | €3.000 |
| Formazione personale | €3.000 |
| Project Management (12 settimane) | €7.800 |
| **Extra manodopera** | **€77.000** |
| Sistemista (€500/gg × 46gg) | €23.000 |
| PM (€650/gg × 60gg) | €39.000 |
| Sviluppatore (€450/gg × 40gg) | €18.000 |
| **Ricorrente anno 1** | **~€129.152** |
| Compute HPC (3 Reserved + 5 Spot, 12h×220gg, 8 HB96) | ~€19.500 |
| Egress dati HPC | ~€1.500 |
| Azure Managed Lustre (10 TB) | ~€17.000 |
| Azure SQL MI (Business Critical primario + failover, Hybrid Benefit -55%) | ~€39.792 |
| Azure Cache for Redis (Standard C1) | ~€900 |
| AKS Windows nodepool D4s_v3 | ~€8.160 |
| Networking (VPN GW, WAF, Bastion, DNS) | ~€5.400 |
| Storage/Backup/DR (Blob GRS, Backup, Site Recovery) | ~€4.600 |
| Sicurezza (Defender for Cloud, Key Vault) | ~€1.920 |
| Microsoft 365 Business Premium (50 utenti) | ~€13.200 |
| Odoo Enterprise (50 utenti) | €14.940 |
| BitBucket + Azure DevOps (5 utenti) | ~€2.060 |
| **Ricorrente anno 2-3** (stesso anno 1 × 2) | **~€258.304** |
| **TOTALE 3 anni** | **~€489.756** ✅ dentro budget |

## SWOT per Variante

| Variante | Punti di forza | Punti di debolezza |
|---|---|---|
| **A — Full Cloud GCP (HPC su Azure)** 🥈 | **InfiniBand NDR 400 Gbps nativo** (su Azure), servizi GCP invariati, DR automatico, costo ridotto | Multi-cloud (2 provider), latenza VPN Azure↔GCP, doppia console gestione |
| **C — Ibrido (Azure HBv4 + on-prem)** 🥉 | **Doppio InfiniBand** (on-prem legacy + Azure NDR 400), migrazione graduale, zero CAPEX nuovi nodi | 3 ambienti (on-prem + Azure + GCP), complessità operativa, costo più alto |
| **D — Full Cloud Azure ⭐** | **InfiniBand NDR 400 Gbps nativo**, DR enterprise-grade (Failover Group automatico, RPO ~5s), SQL Business Critical SSD <1ms, Redis Cache, M365 già presente, budget residuo ~€211k | Costo +7% vs GCP su 3 anni, dipendenza singolo provider, Pondus su Windows container richiede refactoring IIS→Kestrel |

## Raccomandazione

| Scenario | Variante consigliata |
|---|---|
| **Cliente vuole InfiniBand per HPC** | **D (Full Cloud Azure)** — HBv4 con InfiniBand NDR 400 Gbps |
| **Cliente vuole DR automatico e affidabilità DB** | **D (Full Cloud Azure)** — ~€489.756 vs GCP ~€549.720 (DR incluso) |
| **Cliente vuole flessibilità e migrazione graduale** | C (Ibrido) — mantiene on-prem legacy + Azure HBv4 |
| **Multi-cloud per resilienza** | A (GCP servizi + Azure HPC) — non mette tutte le uova nello stesso paniere |
| **Cliente ha vincoli edificio storico** | **D (Full Cloud Azure)** — nessun HW in sede |
| **Budget minimo** | **A — Full Cloud GCP** — ~€454.284 vs D ~€489.756 (D è premium per DR) |
| **Massima performance HPC** | **D (Full Cloud Azure)** — InfiniBand NDR 400 Gbps a $3,60/h HB96 |
| **M365 già presente (Thema)** | **D (Full Cloud Azure)** — €0 migrazione posta/collab |

**Raccomandazione finale**: Variante **D — Full Cloud Azure** è la scelta consigliata per il cliente che prioritizza **affidabilità e continuità operativa**. Offre **InfiniBand NDR 400 Gbps nativo** (requisito critico HPC),
**DR automatico completo** (RPO ~5s SQL con Failover Group automatico),
**SQL Business Critical SSD <1ms**, **Redis Cache** e **M365 già presente** senza costi di migrazione.
Budget residuo ~€211k per imprevisti/espansioni.

> **Nota sul costo**: Con Business Critical + Failover Group + Redis, D (~€489.756/3y) costa ~€35k più di A (~€454.284/3y). Il sovracosto è interamente dovuto a componenti enterprise-grade di resilienza e performance assenti in GCP: DR automatico SQL, storage SSD <1ms e caching. A parità di servizio (GP senza failover), D costerebbe circa quanto A.

**Nota**: La soluzione HPC **Azure HB96-96rs v4** (InfiniBand NDR 400 Gbps, 8 nodi 3R+5S, ~€19.500/anno)
è stata applicata come standard HPC a **tutte le varianti** (A, C, D), differenziandosi solo
per il contesto architetturale:
- **A**: HPC Azure + servizi GCP (multi-cloud, ~€454.284/3a)
- **C**: 8 nodi on-prem legacy + HPC Azure + servizi GCP (~€535.216/3a)
- **D**: Full Azure unificato (~€489.756/3a) ⭐ consigliata
