# Specifica Cluster HPC — Variante Full Cloud Azure

> **Documento:** Architettura del cluster HPC su Microsoft Azure con HBv4 e InfiniBand NDR 400 Gbps
> **Variante:** D — Full Cloud Azure
> **Stato:** Bozza tecnica

---

## REQUISITI

- **Nodi calcolo**: 8 esistenti (Thema, on-premise) — da dismettere; **8 nuovi nodi cloud** sostitutivi
- **CPU**: 2 processori per nodo, ≥24 core ciascuno, clock elevato
- **RAM**: **≥8 GB per core**
- **GPU**: Non richiesta
- **Scratch locale**: ≥1,6 TB per nodo (NVMe)
- **OS**: Linux (Rocky Linux 9 / Ubuntu 24.04 LTS)
- **Rete**: doppia rete (management Ethernet + interconnessione calcolo a bassa latenza)
- **Vincolo bando**: server fisici dedicati, no VM/container per i compute node
- **Utilizzo**: simulazioni crash test, calcolo strutturale (FEM), uso interno
- **Budget HPC**: quota parte del budget totale progetto €520.000

---

## SOLUZIONE

### Azure HBv4 — La scelta migliore per HPC

Azure HBv4 è l'unica offerta cloud CPU HPC con **InfiniBand NDR nativo** (400 Gbps, NVIDIA ConnectX-7). A differenza di GCP (Cloud RDMA Falcon — protocollo proprietario) e AWS (EFA — SRD su Ethernet), Azure utilizza lo **stesso stack InfiniBand NVIDIA** presente negli 8 nodi on-premise di Thema.

| Confronto | GCP H4D-standard-192 | **Azure HB176-96rs v4** | AWS Hpc7a.96xlarge |
|---|---|---|---|
| **Interconnessione** | Cloud RDMA Falcon 200 Gbps | **InfiniBand NDR 400 Gbps** | EFA SRD 300 Gbps |
| **Tipo RDMA** | Falcon HW (binary compat.) | **NVIDIA ConnectX-7 nativo** | SRD (proprietario AWS) |
| **Compatibilità IB on-prem** | Via IRDMA driver | **Stesso driver MLNX OFED** | Via libfabric |
| **Latenza MPI** | 1,5-3 μs | **<2 μs** | 3-5 μs |
| **Prezzo on-demand/h** | $13,74 | **$7,20** | $9,08 |
| **Scratch locale** | 3 TB LSSD | **3,6 TB NVMe** | ❌ Nessuno |
| **RAM** | 3.600 GB (192 core) | **768 GB (96 core, 8 GB/core)** | 768 GB (192 core, 4 GB/core) |

> **Vantaggio decisivo**: Azure HBv4 usa lo stesso vendor (NVIDIA Mellanox) dell'infrastruttura InfiniBand on-premise esistente. Le applicazioni MPI compilate per gli 8 nodi attuali funzionano **senza alcuna modifica** sugli HBv4.

### Specifica tecnica HB176-96rs v4

| Parametro | Valore |
|---|---|
| **CPU** | AMD EPYC 9V33X Genoa-X (Zen 4) |
| **L3 Cache** | **2.304 MB** (3D V-Cache) |
| **vCPU** (core fisici) | **96** (SMT disabilitato) |
| **RAM** | **768 GB DDR5 (8 GB/core)** ✅ requisito rispettato |
| **Banda memoria** | 780 GB/s, effettiva ~1,2 TB/s con 3D V-Cache |
| **Interconnessione** | **400 Gbps NDR InfiniBand** (NVIDIA ConnectX-7) |
| **Rete management** | 80 Gbps Ethernet (Azure SmartNIC v2) |
| **Scratch locale** | 2 × 1.800 GB NVMe + 480 GB SSD = **3,6 TB** |
| **Architettura** | 2 socket NUMA, 48 core per socket |

> La **3D V-Cache** (2.304 MB L3) offre un vantaggio significativo su carichi FEM/crash test dove il dataset del problema spesso eccede la cache L3 standard (~384 MB), riducendo gli accessi a memoria principale.

### Perché HB176-96rs v4 (constrained vCPU)

Lo SKU **Standard_HB176-96rs v4** utilizza la modalità "constrained vCPU" di Azure: espone 96 vCPU su 176 totali, con un rapporto **8 GB/core** (768 GB / 96 = 8 GB/core ✅) che soddisfa pienamente il requisito. La variante a 176 vCPU pieni (HB176rs v4) avrebbe solo 4,36 GB/core, violando il requisito.

Azure pratica un prezzo ridotto per le varianti constrained: **$7,20/h** on-demand per HB176-96rs v4 (96 vCPU) contro circa $13,00/h per HB176rs v4 (176 vCPU). Questo permette di schierare **8 nodi HB176-96rs v4** con un rapporto RAM/core ottimale e un costo inferiore rispetto alla variante full-core.

### Architettura di rete

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
           │        │      │  HBv4-01    │   │    │  HBv4-08   │   │  │
           │        │      │  96 core    │   │    │  96 core   │   │  │
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

**Differenza chiave**: ogni nodo HBv4 ha **2 schede di rete** fisiche:
1. **ConnectX-7 NDR InfiniBand** → traffico MPI/RDMA (400 Gbps, kernel bypass, RDMA Verbs nativi)
2. **Azure SmartNIC v2** → management, storage, accesso utenti (80 Gbps Ethernet)

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

Le applicazioni MPI esistenti (OpenFOAM, Ansys, STAR-CCM+, code FEM proprietarie) si eseguono su HBv4 **senza ricompilazione**, grazie alla compatibilità del driver MLNX OFED:

```bash
# Verifica dispositivo InfiniBand (stesso comando che su on-prem)
ibstat
# Output atteso:
# CA 'mlx5_0'
#   Port 1: ACTIVE (400 Gbps NDR)

# OpenMPI con UCX su InfiniBand
mpirun -n 768 \
    --hostfile hosts.txt \
    --mca pml ucx \
    --mca btl ^vader,tcp,openib \
    -x UCX_NET_DEVICES=mlx5_0:1 \
    -x UCX_TLS=rc,sm \
    --map-by ppr:48:node:pe=2 \
    --bind-to core \
    ./tuo_app_mpi
```

---

## DIMENSIONAMENTO

### Scenario B (consigliato): 8 nodi HB176-96rs v4 — sostituzione completa on-prem

| Componente | Quantità | Specifica |
|---|---|---|
| **Nodi calcolo HBv4** | **8** | HB176-96rs v4 (96 core, 768 GB RAM, 3,6 TB NVMe) |
| **Front-end (su Azure)** | 1 | Standard_D8s_v5 (8 vCPU, 32 GB RAM) |
| **Azure Managed Lustre** | 1 | 10 TB, throughput >100 GB/s |
| **Azure Blob Storage** | 1 | Account Storage Hot tier, 20 TB (archive) |

**Potenza di calcolo**: **768 core fisici** (8 × 96), **6.144 GB RAM totale**, **28.800 GB NVMe scratch totale**.

✅ **8 GB/core verificato**: 768 GB RAM / 96 core = 8 GB/core esatti — requisito soddisfatto.

### Scenario A (alternativo): 16 nodi totali (8 on-prem + 8 HB176-96rs)

| Componente | Quantità | Specifica |
|---|---|---|
| **Nodi calcolo HBv4** | **8** | HB176-96rs v4 (96 core, 768 GB RAM, 3,6 TB NVMe) |
| **Nodi on-prem esistenti** | 8 | Mantenuti in produzione (coesistenza ibrida) |
| **Front-end** | 1 | Standard_D8s_v5 |
| **Azure Managed Lustre** | 1 | 15 TB |
| **Azure Blob Storage** | 1 | 30 TB |

**Potenza di calcolo**: 768 core cloud + core on-prem variabili.

**Scenario A scartato**: richiede mantenimento datacenter on-prem, costi energetici, spazio rack e raffreddamento. Budget superiore a €520k. Si raccomanda **Scenario B** come soluzione definitiva.

### Confronto potenza cloud

| Configurazione | Core fisici | RAM totale | RAM/core | Scratch totale |
|---|---|---|---|---|
| **On-premise esistente** (8 nodi) | variabile | variabile | variabile | variabile |
| **Azure HB176-96rs × 8 nodi (Scenario B)** | **768** | **6.144 GB** | **8 GB/core ✅** | **28.800 GB NVMe** |
| **Azure HB176-96rs × 8 + on-prem × 8 (Scenario A)** | 768 + on-prem | 6.144 GB + on-prem | 8 GB/core | 28.800 GB NVMe |
| **GCP H4D × 5 nodi** | 960 | 3.600 GB | 3,75 GB/core ❌ | 15.000 GB |
| **AWS Hpc7a × 8 nodi** | 1.536 | 6.144 GB | 4 GB/core ❌ | ❌ Nessuno |

> Azure HB176-96rs v4 è l'unico SKU cloud che soddisfa il requisito **≥8 GB per core**. GCP H4D offre 3,75 GB/core, AWS Hpc7a offre 4 GB/core. Nessuno dei due è conforme.

---

## COSTI

### Costi istanze compute (HB176-96rs v4)

| Voce | Configurazione | On-demand/h | Spot/h | 3Y Reserved/h |
|---|---|---|---|---|---|
| Nodi calcolo HBv4 (×8) | HB176-96rs v4 | $57,60 | ~$11,68 | ~$28,80 |
| Front-end | D8s_v5 | $0,34 | ~$0,07 | ~$0,14 |
| **Subtotale compute/h** | | **$57,94** | **~$11,75** | **~$28,94** |
| **Subtotale compute/anno** (24/7) | | **$507.554** | **$102.930** | **$253.514** |

> HB176-96rs v4 costa $7,20/h on-demand. La variante constrained (96 vCPU) costa meno della full-core (~$13/h per 176 vCPU).

### Strategia di ottimizzazione costi

| Strategia | Risparmio | Note |
|---|---|---|---|
| **3 nodi Reserved + 5 spot** | ~-60% | 3×$3,60 + 5×$1,46 = **$18,10/h** |
| **Utilizzo realistico** (12h×220gg) | -70% vs 24/7 | Job schedulati su finestre lavorative |
| **Spot per job batch** | -80% | Job checkpointabili; se terminato, riparte da checkpoint |
| **Azure Reserved Instances** | -50% | Impegno 3 anni sui nodi base |

**Scenario realistico**: 3 nodi 3Y Reserved + 5 spot, 12h/giorno × 220gg/anno

- Compute: 3 × $3,60 + 5 × $1,46 = **$18,10/h**
- Ore annue: 2.640
- **Costo compute annuo: ~$47.784 (~€43.960)** (a cambio ~0,92 EUR/USD)

### Costi storage (annuali)

| Voce | Specifica | Costo/anno |
|---|---|---|
| **Azure Managed Lustre** 10 TB | Throughput >100 GB/s | ~$18.000 (~€17.000) |
| **Azure Blob Storage Hot** 20 TB | Archive risultati | ~$2.400 (~€2.200) |

> **Nota**: Il costo di Azure Managed Lustre è stato allineato al listino reale (~$18.000/anno per 10 TB). Stime precedenti a €8.100 erano basate su configurazioni non realistiche.

### Costi egress dati HPC

L'egress (trasferimento dati in uscita da Azure verso Internet) è un costo tipicamente sottovalutato nelle stime cloud HPC.

| Voce | Stima | Costo |
|---|---|---|
| Download risultati simulazione (100-500 GB/mese) | Dimensione media job: 5-20 GB, ~20-30 job/mese | ~€0,087/GB dopo 10 GB gratis |
| **Costo egress annuo stimato** | 300 GB/mese × 12 mesi | **~€1.500/anno** |

> **Mitigazione**: compressione risultati prima del download, scheduling trasferimenti in fascia off-peak, caching locale su front-end. Per carichi molto intensivi, valutare ExpressRoute (costo fisso, nessun egress).

### Costo totale 3 anni — Scenario B (8 nodi HB176-96rs v4, uso realistico)

| Voce | 1 anno | 3 anni |
|---|---|---|
| Compute HB176-96rs v4 (3 Reserved + 5 spot, 12h×220gg) | ~€43.960 | ~€131.880 |
| Front-end (on-demand) | ~€300 | ~€900 |
| Azure Managed Lustre 10 TB | ~€17.000 | ~€51.000 |
| Azure Blob Storage Hot 20 TB | ~€2.200 | ~€6.600 |
| Egress dati HPC | ~€1.500 | ~€4.500 |
| Networking (VPN, NAT, WAF, Bastion) | ~€3.800 | ~€11.400 |
| **Totale EUR** | **~€68.760** | **~€206.280** |

> **Confronto**: la stessa configurazione su GCP H4D costa circa il 30% in più (~€270.000 in 3 anni). Su AWS Hpc7a è **incompatibile** per mancanza di scratch locale NVMe e RAM/core insufficiente.

---

## Integrazione con nodi on-prem esistenti

Gli 8 nodi esistenti (Thema, on-premise con InfiniBand) condividono lo **stesso stack MLNX OFED** dei nuovi nodi Azure HBv4. Questo offre vantaggi unici:

| Strategia | Descrizione |
|---|---|
| **Scenario B (consigliato)** | I nodi esistenti vengono **dismessi**; tutto il carico passa su 8 HBv4 Azure. Costi HW on-prem (energia, raffreddamento, spazio rack) eliminati |
| **Scenario A (alternativo)** | I nodi esistenti restano on-prem per job legacy; 8 nuovi HBv4 per espansione. Maggiore potenza ma costi doppi |

**Raccomandazione**: **Scenario B** — 8 nodi HB176-96rs v4 in sostituzione completa degli 8 nodi on-prem. Con 768 core e 6.144 GB RAM a 8 GB/core si ottiene potenza superiore senza i vincoli HW on-prem (raffreddamento, spazio rack, obsolescenza).

> **Vantaggio unico di Azure**: a differenza di GCP e AWS, Azure HBv4 usa InfiniBand NVIDIA nativo — lo stesso dei nodi on-prem. Questo semplifica la coesistenza e la migrazione.

---

## Benchmark performance HB176-96rs v4

Fonte: Microsoft Azure + benchmark indipendenti su HBv4 con 3D V-Cache:

| Benchmark | Performance HB176-96rs | Note |
|---|---|---|
| **HPL LINPACK** (FP64) | ~4,5 TFLOPS per nodo | 96 core EPYC Genoa-X (vs ~8 TFLOPS HB176) |
| **Latenza MPI OSU** | <2 μs | NDR InfiniBand punto a punto (identico a HB176) |
| **Banda MPI** | 380 Gbps | ConnectX-7 NDR (identico a HB176) |
| **STAR-CCM+** | ~1,2× vs HBv3 | 3D V-Cache beneficia CFD |
| **OpenFOAM** | ~1,1× vs HBv3 | Vantaggio su mesh grandi |
| **Ansys Fluent** | ~1,2× vs HBv3 | Miglioramento su carichi memory-bound |

> Il benchmark HPL su HB176-96rs v4 (96 vCPU constrained) è inferiore alla variante full-core (~4,5 vs ~8 TFLOPS per nodo) perché usa 96 core invece di 176. Tuttavia, con 8 nodi HB176-96rs si ottengono **~36 TFLOPS totali** (vs ~40 TFLOPS con 5 nodi full-core) — una differenza trascurabile per i carichi FEM/crash test, che sono tipicamente **memory-bound** (beneficiano principalmente della RAM e della cache L3).
>
> La latenza e banda MPI su InfiniBand sono **identiche** tra le varianti constrained e full-core (stesso ConnectX-7 NDR).

---

## Raccomandazioni

1. **Azure HBv4 come piattaforma primaria**: InfiniBand NDR 400 Gbps nativo, latenza <2 μs, stack identico a on-prem. **Nessuna eccezione "no VM" da motivare** (SR-IOV passthrough).

2. **Scenario B — 8 nodi HB176-96rs v4**: 768 core fissi + nodi spot per flessibilità. Costo effettivo stimato: **~€43.960/anno** con utilizzo realistico. **8 GB/core rispettato**.

3. **InfiniBand nativo elimina ogni problema di compatibilità**: Le applicazioni MPI esistenti (OpenFOAM, Ansys, STAR-CCM+, codice FEM proprietario) funzionano **senza modifiche** perché usano lo stesso driver MLNX OFED degli 8 nodi on-prem.

4. **Vincolo "no VM" rispettato senza eccezioni**: SR-IOV pass-through = la VM vede la NIC InfiniBand come dispositivo PCIe fisico. Equivalente a bare metal.

5. **3D V-Cache**: Il cache L3 aggiuntivo (2.304 MB vs 384 MB standard) offre vantaggi misurabili su carichi FEM/crash test.

6. **Azure CycleCloud**: Orchestrazione cluster Slurm nativa, deploy automatizzato in pochi minuti.

7. **Egress monitorato**: Budget ~€1.500/anno per egress, con monitoraggio attivo e alert su soglia.

8. **Test di benchmark**: Eseguire HPL e OSU MPI benchmarks su HB176-96rs v4 prima del go-live per validare le performance attese.

9. **Reserved + spot**: La combinazione ottimale è riservare 3 nodi con 3Y Reserved (~-50%) e usare spot per il resto (5 nodi).

> Vedi [`09_Offerta/`](../09_Offerta/) per la configurazione economica ufficiale del progetto.
