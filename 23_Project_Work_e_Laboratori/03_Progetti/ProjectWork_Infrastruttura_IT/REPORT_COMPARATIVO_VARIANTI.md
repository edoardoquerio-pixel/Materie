# Report Comparativo — Varianti Architetturali TP Group

**Progetto:** Integrazione Infrastruttura IT TP Group (Thema Consulting + Pro Studio)  
**Data:** Giugno 2026  
**Autore:** Team di Progetto  
**Versione:** 1.0

---

## Indice

1. [Executive Summary](#1-executive-summary)
2. [Quadro Generale](#2-quadro-generale)
3. [Confronto Architetturale](#3-confronto-architetturale)
4. [Confronto HPC](#4-confronto-hpc)
5. [Confronto Pondus](#5-confronto-pondus)
6. [Confronto Rete e VPN](#6-confronto-rete-e-vpn)
7. [Confronto Backup e DR](#7-confronto-backup-e-dr)
8. [Confronto Sicurezza ISO 27001](#8-confronto-sicurezza-iso-27001)
9. [Confronto Economico](#9-confronto-economico)
10. [SWAT Analysis](#10-swot-analysis)
11. [Raccomandazione Finale](#11-raccomandazione-finale)

---

## 1. Executive Summary

| Indicatore | A — Full Cloud GCP (HPC su Azure) | C — Ibrido | D — Full Cloud Azure ⭐ |
|---|---|---|---|
| **Costo totale 3 anni** | ~€454.284 | ~€535.216 | **~€489.756** |
| **Delta budget (€701k)** | +€246.716 ✅ | +€165.784 ✅ | **+€211.244 ✅** |
| **InfiniBand** | NDR 400 Gbps (Azure) | HDR 200 Gbps legacy + NDR 400 Gbps (Azure) | **NDR 400 Gbps nativo** |
| **HW on-prem** | Nessuno | 8 nodi legacy | **Nessuno** |
| **DR** | Multi-regione GCP | Misto (Pondus auto, HPC manuale) | **Azure Site Recovery completo** |
| **Complessità** | Media (2 provider) | Alta (3 ambienti) | **Bassa (1 provider)** |
| **Voto** | 🥈 | 🥉 | **🥇** |

---

## 2. Quadro Generale

### 2.1 Situazione di Partenza

| Azienda | Dipendenti | Infrastruttura | Sede |
|---|---|---|---|
| **Thema Consulting** | 30 | On-premise (datacenter saturo, cluster HPC 8 nodi, servizi self-hosted) | Torino, edificio storico |
| **Pro Studio** | 20 | 100% Cloud (Google Workspace, Odoo, BitBucket, GCP) | Torino (contratto locazione in scadenza) |
| **TP Group (fusione)** | **50** | Obiettivo: convergenza + ISO 27001 + potenziamento HPC/Pondus + smart working | Sede unica Thema (Torino) |

### 2.2 Vincoli Critici

- **Datacenter saturo**: 2 rack saturi, impossibile espandere on-premise
- **Condizionamento al limite**: edificio storico impedisce potenziamento
- **UPS**: solo 10 minuti di autonomia
- **Budget**: €520.000 + €181.000 extra manodopera = **€701.000 totali**
- **Tempi**: 12 settimane attive, shutdown max 7 giorni, ciclo di vita 3 anni
- **HPC**: NO VM/NO container sui nodi di calcolo, InfiniBand, Linux, ≥24 core, ≥8 GB RAM/core, scratch 1,6 TB NVMe, no GPU

---

## 3. Confronto Architetturale

| Componente | A — Full Cloud GCP (HPC su Azure) | C — Ibrido | D — Full Cloud Azure ⭐ |
|---|---|---|---|
| **HPC** | **5× Azure HBv4** (cloud) — InfiniBand NDR 400 Gbps | **8 nodi on-prem legacy** (200 Gbps) + **5× Azure HBv4** (NDR 400 Gbps) | **8× Azure HB96-96rs v4** (cloud) — InfiniBand NDR 400 Gbps |
| **Pondus** | Cloud Run + Cloud SQL (GCP) | Cloud Run + Cloud SQL (GCP) | **AKS Windows + Azure SQL** (Hybrid Benefit -55%) |
| **Posta/Collab** | Google Workspace | Google Workspace | **Microsoft 365** (già presente — €0 migrazione) |
| **Identità** | GCDS → Workspace | Samba4 AD on-prem + GCDS sync | **Microsoft Entra ID Connect** (da Samba4 AD) |
| **File server** | Google Drive + Cloud Storage | Drive (collab) + NextCloud (HPC) | **OneDrive + Azure Files** |
| **Backup** | Cloud Storage multi-regione | NAS QNAP (HPC) + Cloud Storage (servizi) | **Azure Backup + Blob Storage GRS** |
| **DR** | Failover automatico GCP multi-regione | Cloud automatico (Pondus) + manuale (HPC) | **Azure Site Recovery West Europe → North Europe, RPO≤1h** |
| **Sicurezza** | GCP compliance nativa | Mista: GCP compliance + on-prem | **Defender for Cloud + Azure Policy ISO 27001** |
| **Provider cloud** | 2 (GCP + Azure) | 3 (on-prem + GCP + Azure) | **1 (Azure)** |
| **Complessità gestionale** | Media | Alta | **Bassa** |

---

## 4. Confronto HPC

### 4.1 Specifica Tecnica Nodi — Variante D (Azure HB96-96rs v4)

| Parametro | Valore |
|---|---|
| **SKU** | **HB96-96rs v4** (96 core, 768 GB, **8 GB/core ✅**) |
| **CPU** | AMD EPYC 9V33X Genoa-X (Zen 4) |
| **L3 Cache** | 2.304 MB (3D V-Cache) |
| **Core fisici** | **96 per nodo** (SMT disabilitato) — 8 GB/core esatti |
| **RAM** | 768 GB DDR5 per nodo |
| **InfiniBand** | NDR 400 Gbps — NVIDIA ConnectX-7 nativo |
| **Ethernet** | 80 Gbps (Azure SmartNIC v2) |
| **Scratch NVMe** | 3,6 TB per nodo (2×1.800 GB + 480 GB) |
| **Nodi proposti** | **8** (3 Reserved + 5 Spot) = **768 core totali** |
| **Filesystem parallelo** | Azure Managed Lustre 10 TB (>100 GB/s) |
| **Front-end** | CycleCloud su Standard_D8s_v5 |
| **OS** | Rocky Linux 9 (Azure HPC image) |
| **Scheduler** | Slurm via CycleCloud |
| **MPI** | OpenMPI 5.x + UCX |

### 4.2 Confronto Tra Varianti

| Criterio | A — Full Cloud GCP (HPC su Azure) | C — Ibrido | D — Full Cloud Azure ⭐ |
|---|---|---|---|
| **Nodi totali** | 5 (cloud puri) | 8 on-prem + 5 cloud = **13 totali** | **8** (cloud puri) |
| **Core totali** | **880** | 8 on-prem (legacy ~200 core?) + 880 = ~1.080 | **768** (8×96, 8 GB/core ✅) |
| **InfiniBand** | NDR 400 Gbps **nativo** | HDR 200 Gbps legacy + NDR 400 Gbps Azure | **NDR 400 Gbps nativo** |
| **Latenza MPI** | **<2 μs** | <2 μs on-prem + <2 μs Azure | **<2 μs** |
| **Scratch per nodo** | **3,6 TB NVMe** | 1,6 TB on-prem + 3,6 TB NVMe Azure | **3,6 TB NVMe** |
| **Vincolo "no VM"** | ✅ SR-IOV = bare-metal grade | ✅ HW fisico on-prem + SR-IOV Azure | ✅ **SR-IOV = bare-metal grade** |
| **CAPEX HW** | **€0** | HW legacy già esistente (ammortizzato) | **€0** |
| **Manutenzione HW** | **Nessuna** (cloud) | Interna (ricambi, energia, raffreddamento) | **Nessuna** (cloud) |
| **Obsolescenza** | Sempre ultima gen | HW legacy 4-5 anni | **Sempre ultima gen** |
| **Burst capacity** | Spot extra su Azure | Spot extra su Azure | **Spot extra su Azure** |

### 4.3 Confronto Provider HPC

| Criterio | GCP H4D | Azure HB96-96rs v4 ⭐ | AWS Hpc7a |
|---|---|---|---|---|
| **vCPU** | 192 | **96** | 192 |
| **RAM** | 720 GB (3,75 GB/core ❌) | **768 GB (8 GB/core ✅)** | **768 GB (4 GB/core ❌)** |
| **Interconnessione** | Cloud RDMA Falcon 200 Gbps | **InfiniBand NDR 400 Gbps** | EFA 300 Gbps |
| **Latenza MPI** | ~3-5 μs | **<2 μs** | ~5-10 μs |
| **Scratch NVMe** | 3 TB LSSD | **3,6 TB** | ❌ **Nessuno** |
| **On-demand/h** | $13,74 | **$3,60** | $9,08 |
| **3Y Reserved/h** | ~$6,87 | **~$1,44** | ~$4,54 |
| **Compat. on-prem** | Binary compat Verbs | **Stesso driver MLNX OFED** | EFA driver specifico |
| **Verdetto** | 2° posto | **1° posto 🏆** | 3° posto (escluso) |

---

## 5. Confronto Pondus

| Criterio | A — Full Cloud GCP (HPC su Azure) | C — Ibrido | D — Full Cloud Azure ⭐ |
|---|---|---|---|
| **Piattaforma** | Cloud Run (serverless) | Cloud Run (serverless) | **AKS con Windows nodepool** |
| **Database** | Cloud SQL SQL Server | Cloud SQL SQL Server | **Azure SQL Managed Instance** |
| **Licenza DB** | Full price (~$18.000/anno) | Full price (~$18.000/anno) | **Hybrid Benefit -55%** (~$8.100/anno) |
| **Load Balancer** | HTTPS LB + Cloud Armor | HTTPS LB + Cloud Armor | **Application Gateway v2 + WAF** |
| **Autenticazione** | Firebase Auth / Identity Platform | Identity Platform + Samba4 AD (LDAPS) | **Azure AD B2C + Entra ID** |
| **CDN** | Cloud CDN | Cloud CDN | **Azure CDN** |
| **API Management** | Apigee / Cloud Endpoints | Apigee / Cloud Endpoints | **Azure API Management** |
| **Runtime** | .NET 8 container Linux | .NET 8 container Linux | **.NET 8 Windows container (nanoserver)** |
| **Container Registry** | Artifact Registry | Artifact Registry | **Azure Container Registry** |
| **Costo annuo** | **~€23.700** | **~€24.000** | **~€51.000** |
| **Delta vs GCP** | — | — | **+€27.300/anno** |

> **Nota**: Il costo annuo della Variante D include Azure SQL Business Critical con **Failover Group automatico** (West Europe ↔ North Europe, RPO ~5s) e **Redis Cache** — componenti non presenti nelle varianti GCP. Il delta riflette un'architettura **enterprise-grade con DR integrato**, non un semplice upsell.

---

## 6. Confronto Rete e VPN

| Criterio | A — Full Cloud GCP (HPC su Azure) | C — Ibrido | D — Full Cloud Azure ⭐ |
|---|---|---|---|
| **Firewall** | FortiGate FG-60F (esistente) | **FortiGate 100F** (upgrade) | FortiGate FG-60F (esistente) |
| **VPN LAN-to-LAN** | Cloud VPN HA (GCP) | FortiGate 100F → GCP Cloud VPN | **Azure VPN Gateway Active-Active** |
| **VPN throughput** | 3 Gbps per tunnel | 3 Gbps | **10 Gbps aggregato** |
| **VPN Client-to-LAN** | IAP + VPN client | FortiClient SSL-VPN + IAP | **Azure P2S VPN + Bastion** |
| **Hybrid Cloud** | GCP ↔ Azure (multi-cloud) | On-prem ↔ GCP (IPsec) | **N/A (tutto su Azure)** |
| **Subnet** | VPC GCP: 4 subnet /24 | VLAN on-prem + VPC GCP: 6 subnet | **Azure VNet: 5 subnet /24** |
| **Connettività sede** | Fibra 1 Gbps + 4G/5G | Fibra 1 Gbps + 4G/5G | **Fibra 1 Gbps + 4G/5G** |
| **Costo annuo rete** | **~€11.520** | **~€10.260** | **~€13.716** |
| **Complessità** | Media (multi-cloud) | Alta (ibrida) | **Bassa (single cloud)** |

---

## 7. Confronto Backup e DR

| Criterio | A — Full Cloud GCP (HPC su Azure) | C — Ibrido | D — Full Cloud Azure ⭐ |
|---|---|---|---|
| **Strategia backup** | Cloud Storage multi-regione | NAS QNAP (on-prem) + Cloud Storage | **Azure Backup + Blob GRS** |
| **Delocalizzazione** | us-central1 ↔ europe-west4 | NAS co-location + GCP multi-regione | **West Europe ↔ North Europe (GRS)** |
| **RPO servizi critici** | ≤1 ora | ≤1 ora (Pondus) / ≤24 ore (HPC) | **≤1 ora (o 0 con Geo-Replication)** |
| **RTO servizi critici** | ≤15 min | ≤15 min (Pondus) / ≤4 ore (HPC) | **≤30 sec (SQL) / ≤5 min (Pondus)** |
| **Failover automatico** | ✅ Sì | ✅ Parziale (Pondus sì, HPC no) | **✅ Completo** |
| **Test DR** | Semestrale (scriptabile) | Semestrale (misto) | **Semestrale (Azure Site Recovery drill)** |
| **Backup VM/HPC** | Snapshot Compute Engine | Veeam → NAS QNAP | **Azure Backup Recovery Services Vault** |
| **Backup DB** | Cloud SQL PITR | Cloud SQL PITR | **Azure SQL PITR + Active Geo-Replication** |
| **Backup file** | Object versioning | Versioning GDrive + rsync NAS | **Soft delete + versioning Blob** |
| **Backup M365** | Google Vault | Google Vault | **Microsoft 365 Backup** |
| **Costo annuo backup/DR** | **~€10.104** | **~€9.200 (on-prem + cloud)** | **~€7.500 ✅** |

---

## 8. Confronto Sicurezza ISO 27001

| Controllo ISO 27001 | A — Full Cloud GCP | C — Ibrido | D — Full Cloud Azure ⭐ |
|---|---|---|---|
| **A.5 — Policy sicurezza** | ✅ Policy bozza inclusa | ✅ Unificare policy on-prem + cloud | ✅ **Azure Policy ISO 27001 built-in** |
| **A.6 — Organizzazione interna** | ✅ Ruoli definiti, IAM | ✅ Ruoli on-prem + cloud IAM | ✅ **RBAC + PIM (JIT access)** |
| **A.9 — Controllo accessi** | ✅ IAM + MFA (Google 2FA) | ✅ AD on-prem + MFA cloud | ✅ **Entra ID + MFA + Conditional Access** |
| **A.10 — Crittografia** | ✅ AES-256, TLS 1.3, CMEK | ✅ LUKS/TLS + AES-256 cloud | ✅ **SSE AES-256 + Key Vault + BYOK** |
| **A.12 — Backup** | ✅ Backup automatici PITR | ✅ NAS + Cloud (duale) | ✅ **Azure Backup + GRS + Site Recovery** |
| **A.13 — Sicurezza rete** | ✅ Cloud VPN, Firewall Rules | ✅ VLAN, VPN, VPC rules | ✅ **NSG + Azure Firewall + WAF + Bastion** |
| **A.16 — Gestione incidenti** | 🟡 Procedura base | 🟡 Da formalizzare | ✅ **Defender for Cloud + Sentinel** |
| **A.17 — Continuità operativa** | ✅ DR multi-regione RPO 1h, RTO 15min | 🟡 DR manuale HPC | ✅ **DR automatico completo** |
| **Costo sicurezza/anno** | **~€7.920** | **~€3.300** | **~€1.920 ✅** |

### 8.1 Gap Analysis — Sintesi

| Area ISO 27001 | Gap rilevati (stato AS-IS) | Priorità |
|---|---|---|
| Business continuity (ridondanza) | 4 gap (di cui 2 alta priorità) | 🔴 Alta |
| Disaster recovery (delocalizzazione) | 2 gap (entrambi alta priorità) | 🔴 Alta |
| Sicurezza accessi (cifratura, VPN, MFA, IAM) | 8 gap (di cui 4 alta priorità) | 🔴 Alta |
| **Totale** | **14 gap** | **8 Alta, 5 Media, 1 Bassa** |

**Principali vulnerabilità attuali:**
1. **Storage singolo punto di guasto** (SAN NetApp unica, NAS QNAP senza off-site)
2. **Nessuna connettività di backup** (singolo link Internet)
3. **Nessun piano DR per Pondus** (servizio clienti esposto)
4. **Cifratura assente** su storage on-prem
5. **MFA non implementato** su Samba4 AD
6. **Nessuna VPN** tra le sedi

---

## 9. Confronto Economico

### 9.1 Costi Una Tantum (Implementazione)

| Voce | A — GCP (HPC su Azure) | C — Ibrido | D — Full Azure ⭐ |
|---|---|---|---|
| Upgrade connettività sede | €6.000 | €6.000 | €6.000 |
| Nuovo firewall | — | **€3.500** (FortiGate 100F) | — |
| Setup cloud (VPN, VNet) | €0 | €0 | €0 |
| Configurazione posta/collab | €1.000 | €1.000 | **€500** (solo estensione) |
| Migrazione dati | €5.000 | €5.000 | €5.000 |
| Formazione | €3.000 | €3.000 | €3.000 |
| Project Management | €7.800 | €7.800 | €7.800 |
| Co-location setup | — | €5.000 | — |
| Configurazione cluster Azure | — | €3.000 | — |
| Migrazione job HPC | — | €8.000 | — |
| **Totale una tantum** | **€22.800** | **€41.800** | **€25.300 ✅** |

### 9.2 Costi Ricorrenti Annuali

| Voce | A — GCP (HPC su Azure) | C — Ibrido | D — Full Azure ⭐ |
|---|---|---|---|---|
| **Compute HPC** (3R+5S, 12h×220gg) | ~€28.992 | ~€28.992 | **~€19.500** (8 HB96, 768 core) |
| **Egress dati HPC** | — | — | **~€1.500** |
| **Managed Lustre** 10 TB | ~€17.100 | ~€17.100 | **~€17.000** |
| **Pondus (runtime)** | ~€3.500 | ~€3.600 | **~€8.160** (D4s_v3 nodepool) |
| **Azure SQL MI** (BC + failover) | ~€17.100 | ~€18.000 | **~€39.792** (primario + secondario, Hybrid Benefit -55%) |
| **Azure Cache for Redis** | — | — | **~€900** |
| **Networking** (VPN, NAT, WAF, Bastion) | ~€3.600 | ~€1.800 | **~€5.400** |
| **Backup/DR** | ~€10.104 | ~€9.200 | **~€4.600** |
| **Sicurezza** | ~€7.920 | ~€3.300 | **~€1.920** |
| **Google Workspace / M365 Premium** (50 utenti) | €7.200 | €7.200 | **€13.200** |
| **Connettività sede** | €6.960 | €6.960 | €6.960 |
| **Energia + raffreddamento HPC on-prem** | — | ~€12.000 | — |
| **Co-location** | — | €8.000 | — |
| **FortiGate UTM** | — | €900 | — |
| **Odoo Enterprise** (50 utenti) | €14.940 | €14.940 | €14.940 |
| **BitBucket + Azure DevOps** | ~€1.700 | ~€1.700 | **~€2.060** |
| Manutenzione sistemista | — | €15.000 | — |
| **Totale annuo** | **~€119.216** | **~€151.412** | **~€143.932** |

### 9.3 Riepilogo 3 Anni

| Voce | A — GCP (HPC su Azure) | C — Ibrido | D — Full Azure ⭐ |
|---|---|---|---|
| Una tantum | €22.800 | €41.800 | **€25.300** |
| Extra manodopera | €69.000 | Incluso in ricorrente | **€77.000** |
| Ricorrente anno 1 | ~€120.828 | ~€164.472 | **~€129.152** |
| Ricorrente anno 2-3 | ~€241.656 | ~€328.944 | **~€258.304** |
| **Totale 3 anni** | **~€454.284** | **~€535.216** | **~€489.756 ✅** |
| **Budget disponibile** | €701.000 | €701.000 | **€701.000** |
| **Margine residuo** | **+€246.716** | **+€165.784** | **+€211.244 ✅** |
| **% del budget** | **65%** | **76%** | **70% ✅** |

### 9.4 Confronto Variante D vs A

La Variante D costa ~€35.472 più della A su 3 anni (~€489.756 vs ~€454.284), ma include:

| Componente | Variante A (GCP) | Variante D (Azure) | Differenziale |
|---|---|---|---|
| **SQL** | Cloud SQL ($18k/anno, **senza DR**) | Business Critical + Failover Group WE↔NE (**DR automatico**) | +€22.692/anno |
| **Pondus** | Cloud Run serverless ($3k/anno) | AKS Windows D4s_v3 + Redis Cache | +€5.560/anno |
| **Posta/Collab** | Workspace €7.200/anno | M365 Premium €13.200/anno | +€6.000/anno |
| **HPC** | GCP H4D ($13,74/h) | Azure HB96 ($3,60/h) | **-€9.492/anno** |
| **Sicurezza** | SCC ~€6.000/anno | Defender ~€1.800/anno | **-€4.200/anno** |
| **Networking** | Multi-cloud | Single cloud | **-€6.000/anno** |

> **Raccomandazione**: Il sovracosto della Variante D è interamente giustificato da componenti **enterprise-grade assenti in GCP**: DR automatico (Failover Group), Business Critical SSD <1ms, Redis caching, InfiniBand NDR 400 Gbps nativo. A parità di servizio (GP senza failover), D costerebbe ~€1.600/anno in meno di A.

---

## 10. SWOT Analysis

### Variante A — Full Cloud GCP (HPC su Azure) 🥈

| Punti di Forza | Punti di Debolezza |
|---|---|
| ✅ InfiniBand NDR 400 Gbps nativo (su Azure) | ❌ Multi-cloud (2 provider: GCP + Azure) |
| ✅ Servizi GCP invariati (Workspace già presente Pro Studio) | ❌ Latenza VPN Azure ↔ GCP (~5-10 ms) |
| ✅ DR automatico multi-regione | ❌ Doppia console di gestione |
| ✅ Costo ridotto (~€454k, -35% vs C) | ❌ Complessità operativa |
| ✅ Nessun HW on-prem | |
| **Opportunità** | **Rischi** |
| 🌟 Multi-cloud elimina vendor lock-in | ⚠️ Costi egress tra cloud |
| 🌟 Flessibilità nella scelta del miglior provider per ogni servizio | ⚠️ Latenza inter-cloud per job HPC che accedono a storage GCP |

### Variante C — Ibrido (Azure HBv4 + On-Prem Legacy + GCP) 🥉

| Punti di Forza | Punti di Debolezza |
|---|---|
| ✅ Doppio InfiniBand (on-prem legacy + Azure NDR 400) | ❌ 3 ambienti (on-prem + Azure + GCP) |
| ✅ Migrazione graduale (mantiene nodi legacy) | ❌ **Costo più alto** (~€535k) |
| ✅ MLNX OFED identico su entrambi ambienti | ❌ Gestione HW on-prem legacy |
| ✅ Zero CAPEX nuovi nodi | ❌ Manutenzione, energia, raffreddamento |
| | ❌ DR manuale per HPC (RTO 4-10 ore) |
| **Opportunità** | **Rischi** |
| 🌟 Massima flessibilità operativa | ⚠️ Complessità gestionale molto alta |
| 🌟 Coesistenza senza migrazione forzata | ⚠️ Costi nascosti (energia, raffreddamento, sistemista) |
| 🌟 Job splitting: legacy on-prem + cloud burst | ⚠️ Obsolescenza HW legacy |

### Variante D — Full Cloud Azure ⭐

| Punti di Forza | Punti di Debolezza |
|---|---|
| ✅ **InfiniBand NDR 400 Gbps nativo** | ❌ Costo superiore vs GCP (+7% su 3 anni) |
| ✅ **DR automatico completo** (RPO ~5s SQL, ≤4h HPC) | ❌ Dipendenza singolo provider (vendor lock-in) |
| ✅ **SQL Business Critical** SSD locale <1ms | ❌ Migrazione HPC da on-prem (una tantum) |
| ✅ **Redis Cache** per performance query | |
| ✅ **M365 già presente** (€0 migrazione posta) | |
| ✅ **Zero HW on-prem** (nessun vincolo edificio storico) | |
| ✅ **Singolo provider** (complessità bassa) | |
| ✅ **Budget residuo ~€211k** per imprevisti/espansioni | |

| Opportunità | Rischi |
|---|---|
| 🌟 DR enterprise-grade già integrato (no extra) | ⚠️ Vendor lock-in Azure |
| 🌟 Budget residuo ~€211k per espansioni | ⚠️ Costi egress HPC da monitorare |
| 🌟 InfiniBand nativo senza eccezioni (nessuna giustificazione "no VM") | ⚠️ Pondus: Windows container + Redis richiede refactoring IIS→Kestrel |
| 🌟 Singolo provider = operatività semplificata | |

---

## 11. Raccomandazione Finale

### 🏆 Variante D — Full Cloud Azure è la scelta consigliata

| Motivo | Dettaglio |
|---|---|
| **Infrastruttura enterprise-grade completa** | **~€489.756/3 anni** — il 70% del budget disponibile |
| **InfiniBand NDR 400 Gbps nativo** | NVIDIA ConnectX-7, stesso driver MLNX OFED dell'on-prem |
| **DR automatico completo** | Azure Site Recovery, RPO ~5s SQL, ≤4h HPC |
| **SQL Business Critical + Failover Group** | SSD locale <1ms, replica automatica WE↔NE |
| **Redis Cache** | Layer di caching per performance query e sessioni |
| **M365 già presente** | Thema ha già Microsoft 365 — €0 migrazione posta/collab |
| **Azure Hybrid Benefit** | Risparmio ~55% sulle licenze SQL Server esistenti (su entrambe le istanze BC) |
| **8 GB/core requisito rispettato** | HB96-96rs v4: 768 GB / 96 core = 8 GB/core esatti |
| **Single provider** | 1 console, 1 fattura, 1 SLA |
| **Zero HW in sede** | Nessun vincolo di edificio storico, datacenter saturo o condizionamento |
| **Budget residuo** | ~€211k per imprevisti, espansioni o formazione aggiuntiva |

### Tabella Decisionale per Scenari Specifici

| Scenario | Variante Consigliata | Perché |
|---|---|---|
| Budget minimo assoluto | **A — Full Cloud GCP** | ~€454.284 vs D ~€490k (D premium per DR) |
| Massima affidabilità DB | **D — Full Cloud Azure** | Business Critical + Failover Group automatico |
| Massima performance HPC | **D — Full Cloud Azure** | InfiniBand NDR 400 Gbps nativo |
| DR completo e automatico | **D — Full Cloud Azure** | Azure Site Recovery + Active Geo-Replication |
| Multi-cloud per resilienza | **A — GCP + Azure** | Non mette tutte le uova nello stesso paniere |
| Migrazione graduale | **C — Ibrido** | Mantiene on-prem legacy + cloud progressivo |
| Vendor lock-in evitato | **A — Multi-cloud** | GCP servizi + Azure HPC |
| M365 già in uso (Thema) | **D — Full Cloud Azure** | €0 migrazione posta/collab |
| Vincoli edificio storico | **D — Full Cloud Azure** | Nessun HW in sede |
| Flessibilità operativa | **C — Ibrido** | Job splitting legacy/cloud |

---

*Documento redatto a scopo di offerta tecnico/economica — TP Group srl — Versione 1.0*
*Framework: REQUISITI → SOLUZIONE → DIMENSIONAMENTO → COSTI*
