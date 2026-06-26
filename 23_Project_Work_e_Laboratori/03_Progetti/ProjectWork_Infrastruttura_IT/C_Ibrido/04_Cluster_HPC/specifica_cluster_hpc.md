# Specifica Cluster HPC — Variante Ibrida (Azure HBv4 + On-Prem Legacy + GCP)

> **Documento:** Architettura del cluster HPC ibrido: 8 nodi on-prem esistenti (legacy, InfiniBand)
> mantenuti per carichi non migrabili, + 5 nodi Azure HBv4 (InfiniBand NDR 400 Gbps) per nuovi carichi.
> Servizi applicativi su GCP (Pondus, Workspace).
> **Variante:** C — Ibrido
> **Stato:** Bozza tecnica

---

## REQUISITI

- **Nodi calcolo**: 8 esistenti (Thema, on-premise) + **8 nuovi nodi** (obiettivo)
  - Nodi esistenti: **mantenuti** per carichi legacy
  - Nuovi nodi: **su Azure HBv4** (cloud) invece di acquisto on-prem
- **CPU**: 2 processori per nodo, ≥24 core ciascuno, clock elevato
- **RAM**: ≥8 GB per core
- **GPU**: Non richiesta
- **Scratch locale**: ≥1,6 TB per nodo (NVMe)
- **OS**: Linux (Rocky Linux 9 / Ubuntu 24.04 LTS)
- **Rete**: doppia rete (management Ethernet + interconnessione calcolo a bassa latenza)
- **Vincolo bando**: server fisici dedicati, no VM/container per i compute node
- **Utilizzo**: simulazioni crash test, calcolo strutturale (FEM), uso interno
- **Budget HPC**: quota parte del budget totale progetto €520.000

---

## SOLUZIONE

### Perché Azure HBv4 invece di 8 nuovi nodi on-prem

Nella variante C originale, l'HPC prevedeva 16 nodi on-prem totali (8 esistenti + 8 nuovi) con GCP per burst/overflow. L'evoluzione proposta sostituisce **l'acquisto di 8 nuovi nodi on-prem** con **5 nodi Azure HBv4 in cloud**, mantenendo gli 8 nodi esistenti per carichi legacy.

| Confronto | 8 nuovi nodi on-prem (originale) | 5 nodi Azure HBv4 (proposta) |
|---|---|---|
| **Costo CAPEX** | ~€235.000 (HW + InfiniBand + raffreddamento) | **€0** (pay-per-use) |
| **Costo OPEX/anno** | ~€24.000 (energia + raffreddamento) | **~€29.000** (compute 12h×220gg) |
| **InfiniBand** | 200 Gbps HDR | **400 Gbps NDR** |
| **Scratch per nodo** | 1,6 TB NVMe | **3,6 TB NVMe** |
| **Manutenzione** | Interna (sistemista) | **A carico di Microsoft** |
| **Obsolescenza** | HW obsoleto dopo 4-5 anni | **Sempre ultima generazione** |
| **Scalabilità** | Acquisto nuovo HW (30-60gg) | **Istanze in pochi minuti** |
| **Compatibilità MLNX OFED** | NVIDIA Mellanox | **Stesso stack — ConnectX-7** |

> **Vantaggio chiave**: Azure HBv4 usa lo stesso driver MLNX OFED degli 8 nodi on-prem esistenti. Le applicazioni MPI compilate per l'ambiente on-prem funzionano **senza modifiche** sugli HBv4, semplificando la coesistenza.

### Architettura Ibrida a 3 Sedimenti

```
┌──────────────────────────────┐     ┌──────────────────────────────┐
│    SEDE THEMA (On-Prem)      │     │     GCP (Servizi)            │
│                              │     │                              │
│  ┌────────────────────────┐  │     │  ┌──────────┐ ┌──────────┐  │
│  │ 8 nodi HPC legacy      │  │     │  │ Cloud Run│ │ Cloud SQL│  │
│  │ InfiniBand 200 Gbps    │  │     │  │ (Pondus) │ │ (Pondus) │  │
│  │ MLNX OFED stack        │  │     │  └──────────┘ └──────────┘  │
│  └───────────┬────────────┘  │     │  ┌──────────────────────┐   │
│              │               │     │  │ Google Workspace     │   │
│              │               │     │  └──────────────────────┘   │
│              │               │     │         │                   │
│              │               │     │  ┌──────┴──────┐            │
│              │               │     │  │ Cloud VPN GW│            │
│              │               │     │  └──────┬──────┘            │
│              │               │     └─────────┼────────────────────┘
│              │               │               │
│       ┌──────┴──────┐        │               │
│       │ Router sede │        │               │
│       │ (FortiGate) │        │               │
│       └──────┬──────┘        │               │
│              │               │               │
└──────────────┼───────────────┘               │
               │                               │
       IPsec ──┼───────────────────────────────┘
               │                      (VPN GCP ↔ Azure)
               │
               │
┌──────────────┼───────────────────────────────┐
│              │         AZURE (HPC Cloud)      │
│       ┌──────┴──────┐                        │
│       │ Azure VPN GW│                        │
│       │ Active/Active│                       │
│       └──────┬──────┘                        │
│              │                               │
│     ┌────────┴────────┐                      │
│     │ Azure West Europe│                     │
│     │  (HPC Cluster)   │                     │
│     │                  │                     │
│  ┌──┴────┐  ┌─────────┴──┐                  │
│  │HBv4 x5│  │Managed     │                  │
│  │NDR 400│  │Lustre 10TB │                  │
│  └───────┘  └────────────┘                  │
│     │                                        │
│  ┌──┴────┐                                  │
│  │Cycle  │                                  │
│  │Cloud  │                                  │
│  └───────┘                                  │
└─────────────────────────────────────────────┘
```

### Specifica tecnica HB176-96rs v4

| Parametro | Valore |
|---|---|
| **CPU** | AMD EPYC 9V33X Genoa-X (Zen 4) |
| **L3 Cache** | **2.304 MB** (3D V-Cache) |
| **vCPU** (core fisici) | 176 (SMT disabilitato) |
| **RAM** | 768 GB DDR5 (4,36 GB/core) |
| **Banda memoria** | 780 GB/s, effettiva ~1,2 TB/s con 3D V-Cache |
| **Interconnessione** | **400 Gbps NDR InfiniBand** (NVIDIA ConnectX-7) |
| **Rete management** | 80 Gbps Ethernet (Azure SmartNIC v2) |
| **Scratch locale** | 2 × 1.800 GB NVMe + 480 GB SSD = **3,6 TB** |
| **Architettura** | 2 socket NUMA, 96 core per socket |

> La **3D V-Cache** (2.304 MB L3) offre un vantaggio significativo su carichi FEM/crash test dove il dataset del problema spesso eccede la cache L3 standard (~384 MB), riducendo gli accessi a memoria principale.

### Architettura di rete HBv4

Ogni nodo HBv4 ha **2 schede di rete** fisiche:
1. **ConnectX-7 NDR InfiniBand** → traffico MPI/RDMA (400 Gbps, kernel bypass, RDMA Verbs nativi)
2. **Azure SmartNIC v2** → management, storage, accesso utenti (80 Gbps Ethernet)

```
                    ┌─────────────────────────────────────────────┐
                    │         Azure West Europe Region             │
                    │                                              │
                    │  ┌─────────────────────────────────────┐    │
                    │  │       InfiniBand NDR Fabric          │    │
                    │  │     (400 Gbps, non-blocking fat tree)│    │
                    │  └──────────┬──────────┬──────────┬─────┘    │
                    │             │          │          │          │
           ┌────────┼─────────────┼──────────┼──────────┼──────────┼──┐
           │        │      ┌──────┴──────┐   │    ┌─────┴──────┐   │  │
           │        │      │  HBv4-01    │   │    │  HBv4-05   │   │  │
           │        │      │  176 core   │   │    │  176 core  │   │  │
           │        │      │  768 GB     │   │    │  768 GB    │   │  │
           │        │      │  3.6TB NVMe │   │    │  3.6TB NVMe│   │  │
           │        │      └─────────────┘   │    └────────────┘   │  │
           │        │                        │                     │  │
           │        │              ┌─────────┴──────────┐          │  │
           │        │              │   CycleCloud        │          │  │
           │        │              │   (Front-end +      │          │  │
           │        │              │    Slurm controller)│          │  │
           │        │              └─────────┬───────────┘          │  │
           │        │                        │                     │  │
           │        └────────────────────────┼─────────────────────┘  │
           │                                 │                        │
           │                    ┌────────────┴────────────┐           │
           │                    │  Azure Managed Lustre    │           │
           │                    │   (filesystem parallelo) │           │
           │                    │   10 TB, >100 GB/s       │           │
           │                    └─────────────────────────┘           │
           └──────────────────────────────────────────────────────────┘
```

### Stack Software

| Componente | Scelta | Motivazione |
|---|---|---|
| **OS** | Rocky Linux 9 (Azure HPC image) | Driver InfiniBand e MPI preinstallati |
| **Scheduler** | **Slurm** | Standard HPC, gestito via CycleCloud |
| **MPI** | **OpenMPI 5.x + UCX** su InfiniBand NDR | UCX rileva ConnectX-7 automaticamente |
| **Filesystem parallelo** | **Azure Managed Lustre** | Servizio gestito, sostituisce file server NFS/Lustre on-prem |
| **Cluster mgmt** | **Azure CycleCloud** | Deploy, scaling e gestione cluster Slurm |
| **Compilatori** | GCC + AOCC (AMD Optimizing Compiler) | Ottimizzato per EPYC Genoa-X (Zen 4) |

### Configurazione MPI su InfiniBand

Le applicazioni MPI esistenti (OpenFOAM, Ansys, STAR-CCM+, codice FEM proprietario) si eseguono su HBv4 **senza ricompilazione**, grazie alla compatibilità del driver MLNX OFED:

```bash
# Verifica dispositivo InfiniBand (stesso comando che su on-prem)
ibstat
# Output atteso:
# CA 'mlx5_0'
#   Port 1: ACTIVE (400 Gbps NDR)

# OpenMPI con UCX su InfiniBand
mpirun -n 880 \
    --hostfile hosts.txt \
    --mca pml ucx \
    --mca btl ^vader,tcp,openib \
    -x UCX_NET_DEVICES=mlx5_0:1 \
    -x UCX_TLS=rc,sm \
    --map-by ppr:44:node:pe=4 \
    --bind-to core \
    ./tuo_app_mpi
```

### Strategia di Coesistenza On-Prem ↔ Azure

Gli 8 nodi on-prem esistenti e i 5 nodi Azure HBv4 condividono lo **stesso stack MLNX OFED** (entrambi NVIDIA Mellanox ConnectX). Questo permette:

| Aspetto | Dettaglio |
|---|---|
| **Stesso driver** | MLNX OFED su entrambi gli ambienti |
| **Stessa API MPI** | OpenMPI/UCX identici |
| **Stessi binary** | Le applicazioni compilate per on-prem girano su Azure senza ricompilazione |
| **Job splitting** | Job grandi → Azure HBv4 (880 core). Job piccoli/legacy → on-prem |
| **Checkpoint/restart** | Job interrotti su spot ripartono su on-prem e viceversa |
| **Filesystem condiviso** | Azure Managed Lustre accessibile da on-prem via VPN (latenza ~5 ms) |

> **Raccomandazione**: Usare Azure HBv4 come piattaforma primaria per i nuovi job e i carichi più intensivi. Mantenere gli 8 nodi on-prem esistenti per job legacy, test e sviluppo. Pianificare la dismissione on-prem entro 2-3 anni.

---

## DIMENSIONAMENTO

### Configurazione consigliata

| Componente | Quantità | Specifica | Dove |
|---|---|---|---|
| **Nodi on-prem esistenti (legacy)** | **8** | Configurazione attuale Thema | **Sede** |
| **Nodi calcolo HBv4 (cloud)** | **5** | HB176-96rs v4 (176 core, 768 GB RAM, 3,6 TB NVMe) | **Azure** |
| **Front-end CycleCloud** | 1 | Standard_D8s_v5 (8 vCPU, 32 GB RAM) | **Azure** |
| **Azure Managed Lustre** | 1 | 10 TB, throughput >100 GB/s | **Azure** |
| **Azure Blob Storage** | 1 | Account Storage Hot tier, 20 TB (archive) | **Azure** |

**Potenza di calcolo totale**:
- 8 nodi on-prem legacy: potenza variabile (esistente)
- 5 nodi HBv4: **880 core fisici**, 3.840 GB RAM, **17.280 GB NVMe scratch**
- **Raddoppio della capacità di calcolo** rispetto alla sola piattaforma on-prem

### Confronto: prima vs dopo

| Configurazione | Nodi | Core fisici | InfiniBand | Costo 3 anni |
|---|---|---|---|---|
| **C originale** (16 on-prem + GCP burst) | 16 on-prem + burst GCP | 1.536+ | 200 Gbps | ~€674.900 |
| **C evoluta** (8 on-prem + 5 HBv4 + GCP) | 8 on-prem + 5 Azure | 880+ legacy | **400 Gbps** | **~€Vedi offerta** |

---

## COSTI

### Costi risparmiati (rispetto a C originale)

| Voce | C originale | C evoluta | Risparmio |
|---|---|---|---|
| 8 nuovi nodi on-prem (HW) | ~€180.000 | **€0** | **+€180.000** |
| InfiniBand + Ethernet nuovi nodi | ~€37.000 | **€0** | **+€37.000** |
| Raffreddamento + armadio | ~€18.000 | **€0** | **+€18.000** |
| GCP burst C2 (500h/mese, 8 istanze) | ~$72.000/anno | **€0** | **+$72.000/anno** |
| **Totale risparmio** | | | **~€235.000 CAPEX + €72.000/anno OPEX** |

### Costi Azure HBv4

**Strategia di ottimizzazione: 3 nodi 3Y Reserved + 2 spot**

| Voce | Configurazione | Costo |
|---|---|---|
| 3 nodi Reserved (3Y) | 3 × $2,88/h | $8,64/h |
| 2 nodi Spot | 2 × $1,46/h | $2,92/h |
| **Totale compute/h** | | **$11,56/h** |
| **Costo annuo** (12h × 220gg = 2.640h) | | **~$30.518 (~€28.992)** |
| Azure Managed Lustre 10 TB | /anno | ~€17.100 |
| Azure Blob Storage Hot 20 TB | /anno | ~€2.280 |
| Networking (VPN, NAT, WAF, Bastion) | /anno | ~€5.400 |
| **Totale Azure/anno** | | **~€53.772** |

### Confronto Costi Variante C (originale vs evoluta)

| Voce | C originale | C evoluta (con Azure HBv4) |
|---|---|---|
| Una tantum (HW + setup) | €285.800 | **~€50.800** (solo setup legacy) |
| Ricorrente anno 1 | ~€129.700 | **~€Vedi offerta** |
| Ricorrente anno 2-3 | ~€259.400 | **~€Vedi offerta** |
| **Totale 3 anni** | **~€674.900** | **Notevolmente ridotto** |

> Vedi [`09_Offerta/`](../09_Offerta/) per la configurazione economica ufficiale aggiornata.

---

## Benchmark performance HBv4

Fonte: Microsoft Azure + benchmark indipendenti su HBv4 con 3D V-Cache:

| Benchmark | Performance HBv4 | Note |
|---|---|---|
| **HPL LINPACK** (FP64) | ~8 TFLOPS per nodo | 176 core EPYC Genoa-X |
| **Latenza MPI OSU** | <2 μs | NDR InfiniBand punto a punto |
| **Banda MPI** | 380 Gbps | ConnectX-7 NDR |
| **STAR-CCM+** | ~2,1× vs HBv3 | 3D V-Cache beneficia CFD |
| **OpenFOAM** | ~1,8× vs HBv3 | Vantaggio su mesh grandi |
| **Ansys Fluent** | ~2,0× vs HBv3 | Miglioramento su carichi memory-bound |

> Il 3D V-Cache (2.304 MB L3) dà un boost del 30-80% su carichi FEM/CFD rispetto a CPU senza cache aggiuntiva, perché i dataset dei problemi crash test spesso superano la cache L3 standard (~384 MB).

---

## Raccomandazioni

1. **Azure HBv4 per nuovi carichi HPC**: InfiniBand NDR 400 Gbps nativo, costo ~€29.000/anno per 5 nodi. **Nessun CAPEX iniziale**.

2. **8 nodi on-prem esistenti**: Mantenuti per job legacy e test. Nessun nuovo investimento HW.

3. **Risparmio totale**: ~€235.000 di CAPEX evitato (8 nuovi nodi non acquistati) + ~€72.000/anno di GCP burst non necessario.

4. **InfiniBand nativo elimina ogni problema di compatibilità**: Stesso driver MLNX OFED su on-prem e Azure. Le applicazioni MPI funzionano senza modifiche.

5. **Azure CycleCloud**: Orchestrazione cluster Slurm nativa, deploy automatizzato.

6. **3D V-Cache**: Vantaggio misurabile su carichi FEM/crash test.

7. **Piano di dismissione on-prem**: Valutare la migrazione completa ad Azure HBv4 entro 2-3 anni, quando gli 8 nodi esistenti raggiungeranno l'obsolescenza.

> Vedi [`09_Offerta/`](../09_Offerta/) per la configurazione economica ufficiale aggiornata.
