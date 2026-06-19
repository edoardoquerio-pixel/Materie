# Specifica Cluster HPC — Variante Full Cloud GCP

## REQUISITI

- 8 nodi esistenti Thema (on-premise, HW proprietario) + 8 nuovi nodi
- 2 CPU per nodo, ≥24 core per CPU, clock rate elevato
- 8 GB RAM per core
- NO GPU
- Scratch: ≥1,6 TB per nodo (storage locale ad alta velocità)
- Sistema operativo: Linux
- NO virtualizzazione, NO container per nodi di calcolo
- Rete: Ethernet + InfiniBand (100/200 Gbps)
- Utilizzo: riservato a risorse interne (simulazioni crash test, analisi FEM)
- Budget: ~€220k (budget cloud dal capitolato)

## SOLUZIONE

### Architettura

GCP non offre InfiniBand nativo. Per cluster HPC ad alte prestazioni si utilizzano:

- **Istanze C2** (Compute Optimized) o **H3** (High Memory) con **sole tenancy**
- Rete a bassa latenza: **Google Virtual NIC (gVNIC)** + **Tier_1 networking** (100 Gbps)
- Alternative a InfiniBand: **GPUDirect-TCPX** (solo con GPU) o **MPI su TCP con tuning** di kernel

> **Nota sul requisito InfiniBand**: GCP non fornisce InfiniBand come servizio. Per carichi MPI latency-sensitive,
> si raccomanda di valutare con il cliente se le performance della rete GCP (gVNIC + placement groups)
> siano sufficienti o se sia necessario mantenere parte del cluster on-premise (soluzione ibrida).

### Tipologia Istanze

| Parametro | Valore proposto |
|---|---|
| **Tipo istanza** | `c2-standard-60` (60 vCPU, 240 GB RAM) o `c2d-highcpu` |
| **vCPU per nodo** | 60 (2× 30-core) |
| **RAM per nodo** | 240 GB (4 GB/vCPU — compromesso) |
| **vCPU totali** | 480 (8 nuovi nodi) |
| **RAM totale** | 1.920 GB |
| **Sistema operativo** | Ubuntu 24.04 LTS o Rocky Linux 9 |
| **Scheduling** | Sole tenant node (isolamento fisico) |

> Nota: il requisito 8 GB RAM/core non è direttamente soddisfacibile con le istanze GCP standard.
> Le istanze `m3-megamem-128` offrono 8 GB/vCPU ma con molte meno vCPU. Opzione alternativa:
> combinazione di istanze C2 (nodi di calcolo) + istanze M3 (nodi memory-intensive).

### Storage

| Elemento | Soluzione | Specifica |
|---|---|---|
| **Scratch** | Local SSD (NVMe) | 3 TB × 24 dischi = 3 TB per nodo |
| **Home/Software** | Persistent Disk (SSD) | 500 GB per nodo, condiviso via NFS |
| **Storage risultati** | Cloud Storage (Object store) | Bucket standard per risultati simulazioni |
| **File system** | Parallel File System | Spectrum Scale (GPFS) o BeeGFS su Persistent Disk |

### Rete

| Componente | Specifica |
|---|---|
| **Rete** | Google VPC con Tier_1 networking |
| **Banda** | 100 Gbps per VM (gVNIC + Tier_1) |
| **Placement** | Compact placement policy (riduce latenza intra-cluster) |
| **Latenza** | < 10 μs tra VM nello stesso placement group |
| **Firewall** | Cloud Firewall rules per traffico MPI (porte custom) |

### Front-end

- 1 VM (e2-standard-8, 8 vCPU, 32 GB RAM, 100 GB SSD)
- Scheduler: SLURM (controller + node)
- Accesso: SSH via IAP (Identity-Aware Proxy)

## DIMENSIONAMENTO

| Componente | Quantità | Dettaglio |
|---|---|---|
| Nodi calcolo C2 | 8 | 60 vCPU, 240 GB RAM, Local SSD 3 TB |
| Front-end | 1 | 8 vCPU, 32 GB RAM, 100 GB SSD |
| Nodi esistenti Thema | 8 | On-premise (da mantenere o dismettere) |
| Storage oggetti | 10 TB | Cloud Storage Standard |
| Parallel FS | 5 TB | Persistent Disk SSD (condiviso) |

### Confronto: Performance cluster on-premise vs GCP

| Metric | On-prem (8 nodi attuali) | GCP C2 (8 nuovi) | Differenza |
|---|---|---|---|
| Core totali | Variabile (HW proprietario) | 480 vCPU | Maggiore densità |
| RAM totale | Variabile | 1.920 GB | Maggiore capacità |
| Interconnessione | InfiniBand proprietario | 100 Gbps Ethernet (gVNIC) | Latenza maggiore |
| Storage scratch | HD locale | Local SSD NVMe | Performance superiore |
| Spazio rack | 8U | 0 (cloud) | Vantaggio significativo |

## COSTI

| Voce | Configurazione | Costo mensile (on-demand) | Costo annuale (on-demand) | Costo annuale (CUD 3 anni) |
|---|---|---|---|---|
| Istanze C2 (8 nodi) | 60 vCPU, 240 GB RAM × 8 | ~$12.000 | ~$144.000 | ~$86.400 |
| Front-end | e2-standard-8 | ~$200 | ~$2.400 | ~$1.440 |
| Local SSD | 3 TB × 8 nodi | ~$2.400 | ~$28.800 | ~$28.800 |
| Persistent Disk | 5 TB SSD condiviso | ~$850 | ~$10.200 | ~$10.200 |
| Cloud Storage | 10 TB Standard | ~$200 | ~$2.400 | ~$2.400 |
| Networking | Tier_1 egress (10 TB/mese) | ~$1.000 | ~$12.000 | ~$12.000 |
| **Totale** | | **~$16.650** | **~$199.800** | **~$141.240** |

*CUD = Committed Use Discount (1 anno: 30% sconto, 3 anni: 40% sconto).*
*Costi in USD (fatturati da GCP in $), convertiti in EUR al cambio ~1,05.*

## Raccomandazioni

1. **Valutare mantenimento on-premise**: 8 nodi esistenti potrebbero rimanere in sede per carichi legacy, con GCP per espansione (modello ibrido)
2. **Sole tenancy**: obbligatoria per prestazioni consistenti (nessun "noisy neighbor")
3. **Test di benchmark**: prima del cut-over eseguire HPL (High-Performance Linpack) su GCP per validare performance
4. **CUD 3 anni**: fortemente raccomandato per ridurre il costo del ~40%
5. **InfiniBand**: documentare al cliente che GCP non offre InfiniBand nativo. Se critical, considerare Variante C (ibrida)
