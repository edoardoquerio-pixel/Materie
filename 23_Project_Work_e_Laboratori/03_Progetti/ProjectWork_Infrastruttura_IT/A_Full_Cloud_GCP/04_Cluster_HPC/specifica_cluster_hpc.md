# Specifica Cluster HPC — Variante Full Cloud GCP (con HPC su Azure)

> **Documento:** Architettura del cluster HPC su Microsoft Azure HBv4 con InfiniBand NDR 400 Gbps.
> GCP utilizzato per servizi applicativi (Pondus, Workspace, storage), Azure per il solo cluster HPC.
> **Variante:** A — Full Cloud GCP (Multi-Cloud: Azure HPC + GCP Servizi)
> **Stato:** Bozza tecnica

---

## REQUISITI

- **Nodi calcolo**: 8 esistenti (Thema, on-premise) + **8 nuovi nodi** (obiettivo)
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

### Perché Azure HBv4 invece di GCP H4D / C2

Il confronto tra i provider cloud per HPC ha evidenziato Azure HBv4 come **1° classificato**:

| Criterio | GCP H4D-standard-192 | **Azure HB176-96rs v4** | AWS Hpc7a.96xlarge |
|---|---|---|---|
| **Interconnessione** | Cloud RDMA Falcon 200 Gbps | **InfiniBand NDR 400 Gbps** | EFA SRD 300 Gbps |
| **Tipo RDMA** | Falcon HW (binary compat.) | **NVIDIA ConnectX-7 nativo** | SRD (proprietario AWS) |
| **Compatibilità IB on-prem** | Via IRDMA driver | **Stesso driver MLNX OFED** | Via libfabric |
| **Latenza MPI** | 1,5-3 μs | **<2 μs** | 3-5 μs |
| **Prezzo on-demand/h** | $13,74 | **$7,20** | $9,08 |
| **Scratch locale** | 3 TB LSSD | **3,6 TB NVMe** | ❌ Nessuno |
| **Vincolo "no VM"** | Giustificabile (Titanium) | **SR-IOV = bare-metal grade** | EFA via ena |

> **Scelta**: Azure HBv4 offre InfiniBand NDR 400 Gbps nativo allo stesso driver MLNX OFED degli 8 nodi on-prem esistenti, a un costo **-48% rispetto a GCP H4D** ($7,20/h vs $13,74/h).

L'architettura risultante è **multi-cloud**: il cluster HPC risiede su Azure West Europe (HBv4 + InfiniBand + Managed Lustre), mentre tutti gli altri servizi (Pondus, Google Workspace, storage legacy) restano su GCP come da variante A originale.

### Architettura Multi-Cloud

```
                     ┌─────────────────────────────────────────────────────┐
                     │                   GCP (Servizi)                      │
                     │  ┌──────────┐  ┌──────────┐  ┌──────────────────┐  │
                     │  │ Cloud Run│  │ Cloud SQL│  │ Google Workspace │  │
                     │  │ (Pondus) │  │ (Pondus) │  │ Posta/Collab     │  │
                     │  └──────────┘  └──────────┘  └──────────────────┘  │
                     │                    │                                │
                     │           ┌────────┴────────┐                      │
                     │           │  Cloud VPN GW    │                      │
                     │           └────────┬────────┘                      │
                     └────────────────────┼────────────────────────────────┘
                                          │ IPsec / HA VPN
                                          │ (400 Mbps - 1 Gbps)
                                          │
                     ┌────────────────────┼────────────────────────────────┐
                     │           ┌────────┴────────┐                      │
                     │           │  Azure VPN GW    │                      │
                     │           │  (Active-Active) │                      │
                     │           └────────┬────────┘                      │
                     │                    │                                │
                     │         ┌──────────┴──────────┐                    │
                     │         │   Azure West Europe   │                    │
                     │         │     (HPC Cluster)     │                    │
                     │         │                       │                    │
                     │  ┌──────┴──────┐  ┌─────────────┴──────┐           │
                     │  │  HBv4 x5    │  │   Managed Lustre   │           │
                     │  │  InfiniBand │  │   10 TB parallelo  │           │
                     │  │  NDR 400    │  └────────────────────┘           │
                     │  └─────────────┘                                   │
                     │         │                                          │
                     │  ┌──────┴──────┐                                   │
                     │  │  CycleCloud  │                                   │
                     │  │  + Slurm    │                                   │
                     │  └─────────────┘                                   │
                     └────────────────────────────────────────────────────┘
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

### Perché InfiniBand nativo è superiore

| Aspetto | Cloud RDMA (GCP) | InfiniBand NDR (Azure) |
|---|---|---|
| **Stack driver** | IRDMA driver Google | **MLNX OFED NVIDIA standard** |
| **Compatibilità app on-prem** | Binary compat (testata) | **Nativa — stesso driver** |
| **Banda** | 200 Gbps | **400 Gbps** |
| **Latenza porta a porta** | ~1,5 μs | **<1 μs** |
| **Adaptive Routing** | Limitato | **✅ NDR completo** |
| **Congestion Control** | Base | **✅ Avanzato (DCT)** |
| **Collective offload** | Parziale | **✅ SHARP in-net computing** |
| **Vincolo "no VM"** | Giustificabile (Titanium) | **✅ SR-IOV = bare-metal grade** |

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

### Integrazione GCP ↔ Azure (Multi-Cloud Networking)

La connettività tra il cluster HPC su Azure e i servizi su GCP è garantita da una **VPN multi-cloud**:

| Elemento | Configurazione |
|---|---|
| **Azure side** | VPN Gateway Active-Active (2 istanze) |
| **GCP side** | Cloud HA VPN (2 tunnel) |
| **Throughput** | 400 Mbps - 1 Gbps per tunnel |
| **Protocollo** | IPsec IKEv2 |
| **Latenza aggiuntiva** | ~5-10 ms (Azure West Europe → GCP europe-west) |
| **Costo** | ~€13.716/anno (Azure VPN) + ~€1.800/anno (GCP HA VPN) |

> **Nota**: Per carichi che richiedono trasferimenti intensivi tra HPC (Azure) e storage (GCP), è consigliabile uno **scambio dati via Internet** (Azure Blob → GCP Cloud Storage via API) invece che attraverso la VPN, per evitare瓶颈 sulla VPN.

---

## DIMENSIONAMENTO

### Opzione consigliata: 5 nodi HB176-96rs v4 (multi-cloud)

| Componente | Quantità | Specifica | Provider |
|---|---|---|---|
| **Nodi calcolo HBv4** | **5** | HB176-96rs v4 (176 core, 768 GB RAM, 3,6 TB NVMe) | **Azure** |
| **Front-end CycleCloud** | 1 | Standard_D8s_v5 (8 vCPU, 32 GB RAM) | **Azure** |
| **Azure Managed Lustre** | 1 | 10 TB, throughput >100 GB/s | **Azure** |
| **Azure Blob Storage** | 1 | Account Storage Hot tier, 20 TB (archive) | **Azure** |
| **Pondus** | 1 | Cloud Run + Cloud SQL | **GCP** |
| **Google Workspace** | 50 utenti | Business | **GCP** |
| **Cloud Storage** | 1 | Nearline 20 TB (backup servizi) | **GCP** |

**Potenza di calcolo**: 880 core fisici (vs 480 vCPU della precedente soluzione C2 GCP).

### Opzione massima: 8 nodi HB176-96rs v4

| Componente | Quantità | Specifica |
|---|---|---|
| **Nodi calcolo HBv4** | **8** | HB176-96rs v4 (176 core, 768 GB RAM, 3,6 TB NVMe) |
| **Front-end** | 1 | Standard_D8s_v5 |
| **Azure Managed Lustre** | 1 | 15 TB |
| **Azure Blob Storage** | 1 | 30 TB |

**Potenza di calcolo**: 1.408 core fisici.

### Confronto potenza: GCP vs Azure (multi-cloud)

| Configurazione | Core fisici | RAM totale | Scratch totale |
|---|---|---|---|
| **GCP H4D × 5** (soluzione precedente) | 960 | 3.600 GB | 15.000 GB |
| **Azure HBv4 × 5 nodi** | **880** | **3.840 GB** | **17.280 GB NVMe** |
| **Azure HBv4 × 8 nodi** | **1.408** | **6.144 GB** | **28.800 GB NVMe** |

---

## COSTI

### Costi istanze compute (HBv4 su Azure)

**Opzione 5 nodi:**

| Voce | Configurazione | On-demand/h | Spot/h | 3Y Reserved/h |
|---|---|---|---|---|
| Nodi calcolo HBv4 (×5) | HB176-96rs v4 | $36,00 | ~$7,30 | ~$14,40 |
| Front-end | D8s_v5 | $0,34 | ~$0,07 | ~$0,14 |
| **Subtotale compute/h** | | **$36,34** | **~$7,37** | **~$14,54** |
| **Subtotale compute/anno** (24/7) | | **$318.338** | **$64.561** | **$127.370** |

### Strategia di ottimizzazione costi

| Strategia | Risparmio | Note |
|---|---|---|
| **3 nodi Reserved + 2 spot** | ~-60% | 3×$2,88 + 2×$1,46 = **$11,56/h** |
| **Utilizzo realistico** (12h×220gg) | -70% vs 24/7 | Job schedulati su finestre lavorative |
| **Spot per job batch** | -80% | Job checkpointabili; se terminato, riparte da checkpoint |
| **Azure Reserved Instances** | -60% | Impegno 3 anni sui nodi base |

**Scenario realistico**: 3 nodi 3Y Reserved + 2 spot, 12h/giorno × 220gg/anno

- Compute: 3 × $2,88 + 2 × $1,46 = **$11,56/h**
- Ore annue: 2.640
- **Costo compute annuo: ~$30.518 (~€28.992)**

### Costi storage (annuali)

| Voce | Specifica | Costo/anno |
|---|---|---|
| **Azure Managed Lustre** 10 TB | Throughput 100 GB/s | ~€17.100 |
| **Azure Blob Storage Hot** 20 TB | Archive risultati | ~€2.280 |
| **Azure NetApp Files** 5 TB | Home/software condivisi (opzionale) | ~€6.840 |

### Costi networking multi-cloud (annuali)

| Voce | Costo/anno |
|---|---|
| Azure VPN Gateway Active-Active | ~€13.716 |
| GCP Cloud HA VPN | ~€1.800 |
| **Totale networking multi-cloud** | **~€15.516** |

### Costo totale 3 anni (scenario consigliato: 5 nodi, utilizzo realistico)

| Voce | 3 anni |
|---|---|
| Compute HBv4 (3 Reserved + 2 spot, 12h×220gg) | ~€86.976 |
| Front-end (on-demand) | ~€900 |
| Azure Managed Lustre 10 TB | ~€51.300 |
| Azure Blob Storage Hot 20 TB | ~€6.840 |
| Networking multi-cloud (Azure VPN + GCP VPN) | ~€46.548 |
| **Totale HPC Azure 3 anni** | **~€192.564** |
| GCP servizi (Pondus, Workspace, backup) | ~€357.156 (da offerta GCP Variante A) |
| **Totale Variante A (multi-cloud) 3 anni** | **~€549.720** |

> **Nota**: Il costo HPC su Azure (~€192.564/3a) sostituisce il costo HPC su GCP (H4D ~€300.000+/3a), generando un risparmio di ~€100.000+ pur avendo InfiniBand NDR 400 Gbps nativo. Il totale variante A rimane invariato (~€549.720) perché i costi GCP servizi restano gli stessi.

---

## Multi-Cloud: considerazioni operative

### Vantaggi dell'approccio multi-cloud Azure + GCP

- **HPC su Azure**: InfiniBand NDR 400 Gbps nativo, driver MLNX OFED compatibile con on-prem, costo -48% vs GCP
- **Servizi su GCP**: Pondus (Cloud Run + Cloud SQL), Workspace, storage già dimensionati e funzionanti
- **Nessuna migrazione forzata**: i servizi GCP esistenti non vengono toccati
- **Vincolo "no VM" rispettato**: SR-IOV su HBv4 = pass-through PCIe, equivalente a bare metal

### Svantaggi / Rischi

- **Latenza rete** (~5-10 ms) tra HPC (Azure) e storage applicativo (GCP)
- **Doppia gestione**: due cloud provider, due console, due fatturazioni
- **Trasferimento dati inter-cloud**: costi di egress tra Azure e GCP (evitabili con scambio via Internet)

### Mitigazioni

- Per job HPC che leggono/scrivono grandi volumi su GCP: utilizzare **Azure Blob Storage + Data Transfer via Internet** invece della VPN
- Per job che richiedono solo scratch locale (NVMe 3,6 TB per nodo): **nessun traffico inter-cloud**, latenza zero
- Monitoring unificato: Grafana con datasource sia Azure Monitor che GCP Cloud Monitoring

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

## Integrazione con nodi on-prem esistenti

Gli 8 nodi esistenti (Thema, on-premise con InfiniBand) condividono lo **stesso stack MLNX OFED** dei nuovi nodi Azure HBv4:

| Strategia | Descrizione |
|---|---|
| **Dismissione** | I nodi esistenti vengono dismessi; tutto il carico passa su HBv4 Azure |
| **Ibrido temporaneo** | I nodi esistenti restano on-prem per job legacy; nuovi job su Azure. MLNX OFED identico facilita la coesistenza |

**Raccomandazione**: Dismissione dei nodi esistenti al termine della migrazione. Con 5-8 HBv4 si ottiene potenza superiore senza i vincoli HW on-prem.

---

## Raccomandazioni

1. **Azure HBv4 come piattaforma HPC primaria**: InfiniBand NDR 400 Gbps nativo, latenza <2 μs, stack identico a on-prem. **Nessuna eccezione "no VM" da motivare** (SR-IOV passthrough).

2. **5 nodi HB176-96rs v4**: 880 core fissi + nodi spot per flessibilità. Costo effettivo stimato: **~€29.000/anno** con utilizzo realistico.

3. **InfiniBand nativo elimina ogni problema di compatibilità**: Le applicazioni MPI esistenti funzionano **senza modifiche** perché usano lo stesso driver MLNX OFED degli 8 nodi on-prem.

4. **Multi-cloud è la scelta giusta per questo profilo**: Il cliente ha già servizi su GCP (Workspace, Cloud Run). Spostare solo l'HPC su Azure massimizza il vantaggio InfiniBand senza stravolgere l'infrastruttura esistente.

5. **3D V-Cache**: Il cache L3 aggiuntivo (2.304 MB vs 384 MB standard) offre vantaggi misurabili su carichi FEM/crash test.

6. **Azure CycleCloud**: Orchestrazione cluster Slurm nativa, deploy automatizzato in pochi minuti.

7. **Test di benchmark**: Eseguire HPL e OSU MPI benchmarks su HBv4 prima del go-live per validare le performance attese.

8. **Reserved + spot**: La combinazione ottimale è riservare 3 nodi con 3Y Reserved (~-60%) e usare spot per il resto.

> Vedi [`09_Offerta/`](../09_Offerta/) per la configurazione economica ufficiale del progetto. Vedi [`06_Cloud_Migration/`](../06_Cloud_Migration/) per il piano di migrazione multi-cloud.
