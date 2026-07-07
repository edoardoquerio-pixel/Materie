# Specifica Cluster HPC Ibrido — On-Prem + Azure CycleCloud

> **VM burst**: Standard HB176-96rs v4 (constrained 96 vCPU) — unico SKU conforme ai requisiti ≥8 GB/core

## Architettura dual-network

Ogni nodo HPC (on-prem e Azure) ha **due reti fisiche separate**:

| Rete | Scopo | On-prem | Azure | Firewall |
|------|-------|---------|-------|----------|
| **Ethernet** (management) | SSH, API CycleCloud, NFS/Lustre, backup | VLAN 20 → Switch L3 → **FortiGate FG-100F** | Azure SmartNIC v2 → `snet-hpc-westeu` → **NSG** | ✅ FortiGate (on-prem) + NSG (Azure) |
| **InfiniBand** (calcolo) | MPI, RDMA, comunicazione tra nodi | InfiniBand switch on-prem (isolato) | ConnectX-7 NDR 400 Gbps (fabric Azure) | ❌ Nessun firewall (rete trusted, latenza <2μs) |

> **Importante**: L'InfiniBand **NON passa dal FortiGate** né dalla VPN. Le due fabbric InfiniBand (on-prem e Azure) sono separate — MPI non attraversa mai il sito remoto. Questo è voluto: la latenza VPN (~5ms) renderebbe MPI inutilizzabile cross-sito.

### Flussi di traffico e firewall

| Flusso | Percorso | Controllo |
|--------|----------|-----------|
| Front-end on-prem → CycleCloud head node | SSH su Ethernet → VLAN 20 → FortiGate → IPsec VPN → `snet-hpc-westeu` | FortiGate policy + NSG (port 22) |
| CycleCloud head node → HBv4 nodi | API interna Azure (Ethernet) | NSG `snet-hpc-westeu` |
| HBv4 nodi → Managed Lustre | Ethernet (Azure interno) | NSG `snet-lustre-westeu` |
| MPI tra HBv4 nodi | InfiniBand NDR (fabric Azure) | Nessuno (rete trusted) |
| Utente remoto → HPC on-prem | WireGuard → FortiGate → VLAN 20 | FortiGate (port 22, scheduler API) |
| Dati job on-prem → Lustre | Ethernet → FortiGate → VPN → `snet-lustre` | FortiGate policy (port TCP 988) |

## Configurazione di rete Azure

```
Sede Torino                          Azure West Europe
┌──────────────────────┐            ┌──────────────────────────────┐
│  Cluster On-Prem      │            │  CycleCloud Head Node        │
│                        │            │  (Standard_D2s_v3)           │
│ 8 nodi esistenti       │◄───IPsec──►│  └→ Slurm scheduler          │
│ (HW proprietario)      │            │  └→ HB176-96rs v4 (8 burst) │
│ InfiniBand interconnect│            │  └→ Managed Lustre 4 TB     │
│                        │            │  └→ InfiniBand SR-IOV NDR   │
│ Front-end VM (Linux)   │            │                              │
│ └→ PBS/Torque job queue│            │                              │
└──────────────────────┘            └──────────────────────────────┘
```

> **Nota**: MPI non attraversa la VPN. I job on-prem e Azure sono separati ma condividono il filesystem Lustre per i dati.

## Componenti

### On-Prem (esistenti)

| Componente | Specifica |
|---|---|
| Nodi calcolo | 8 nodi fisici con HW proprietario, schede InfiniBand |
| Front-end | 1 VM Linux con PBS/Torque job scheduler |
| Rete | InfiniBand interna al cluster |
| Storage | Storage locale + NAS QNAP (backup) |
| OS | Linux (distribuzione specifica HPC) |

### Azure CycleCloud — Nuovi nodi burst

| Parametro | Valore |
|---|---|
| Servizio | **Azure CycleCloud** (orchestrazione cluster) |
| Head node VM | **Standard_D2s_v3** (2 vCPU, 8 GB RAM, 16 GB SSD) — dedicato in Azure |
| VM burst | **Standard HB176-96rs v4** (96 vCPU, 768 GB RAM, InfiniBand NDR 400 Gbps) |
| Nodi massimi | 8 nodi (configurabile in base a budget) |
| Connettività | InfiniBand SR-IOV (NDR 400 Gbps, NVIDIA ConnectX-7) |
| Filesystem | **Azure Managed Lustre** (POSIX compliant, latenza < 5 ms) |
| Scheduler | Slurm (gestito da CycleCloud) + PBS/Torque on-prem (forward job) |
| OS | Rocky Linux 9 (Azure HPC image) |
| Regione | West Europe |

> **Perché HB176-96rs v4**: 768 GB / 96 vCPU = **8 GB/core** ✅ requisito soddisfatto. La variante full-core (176 vCPU) avrebbe solo 4,36 GB/core ❌. Azure HBv4 è l'unico cloud che rispetta il vincolo.

### Azure Managed Lustre

| Parametro | Valore |
|---|---|
| Throughput | 500 MB/s per TB di storage |
| Capacità | 4 TB (sufficiente per job HPC burst) |
| Protocollo | POSIX/Lustre (montabile su cluster on-prem + Azure) |
| Costo | ~€ 0,20/GB/mese |

## Costi

### Una tantum (upgrade sede)

| Voce | Costo |
|---|---|
| Rinnovo licenze/supporto cluster on-prem (3 anni) | € 10.000 |
| Potenziamento rete InfiniBand on-prem (cavi, switch) | € 6.000 |
| **Totale una tantum** | **€ 16.000** |

### Ricorrenti Azure

| Voce | Costo/ora nodo | Costo/giorno* | Costo/anno** |
|---|---|---|---|
| HB176-96rs v4 (8 nodi SPOT, 8 ore/giorno, 200 gg/anno) | € 1,34/h | € 10,72 | € 2.144 |
| CycleCloud head node (Standard_D2s_v3, on-demand 24/7) | — | — | € 360 |
| Azure Managed Lustre (4 TB) | — | € 2,67 | € 960 |
| CycleCloud (licenza gratuita) | — | — | € 0 |
| ExpressRoute (opzionale, per alta latenza) | — | € 9,86 | € 3.600 |
| **Totale HPC Azure/anno (senza ER)** | | | **~€ 3.464** |
| **Totale HPC Azure/anno (con ER)** | | | **~€ 7.064** |

*\*8 ore/giorno × 8 nodi*
*\*\*200 giorni lavorativi/anno*

Nota**: Il costo è significativamente inferiore alla variante full cloud (~€44k/anno) perché i nodi Azure sono usati SOLO per overflow, non come calcolo primario. Prezzi SPOT con checkpointing obbligatorio. Il CycleCloud head node (D2s_v3) è sempre acceso (24/7, ~€30/mese).

### Confronto costi

| Scenario | On-prem 8 nodi (esistenti) | + Azure 8 nodi (burst) | Delta |
|---|---|---|---|
| Costo capitale (8 nuovi nodi fisici evitati) | — | ~€ 192.000 (evitato) | **€ -192.000** |
| Costo operativo annuo | ~€ 18.000 | + € 3.464 (Azure burst + head node) | **€ +3.464** |

La scelta CycleCloud consente di evitare l'acquisto di 8 nuovi nodi HPC fisici (~€ 192.000), utilizzando invece risorse Azure SPOT a consumo con un costo operativo di ~€ 3.464/anno (incluso head node D2s_v3). Il checkpointing è necessario per gestire la possibile revoca delle istanze SPOT.

## Configurazione di rete Azure

| Parametro | Valore |
|---|---|
| VNet HPC | `vnet-tpgroup-westeu` — 10.30.0.0/16 |
| Subnet HPC burst | `snet-hpc-westeu` — 10.30.100.0/24 |
| Subnet Lustre | `snet-lustre-westeu` — 10.30.101.0/24 |
| NSG | Allow InfiniBand (tra nodi), Allow SSH (da front-end on-prem) |
| VPN | IPsec IKEv2 — 10.10.0.0/16 → 10.30.100.0/24 |
| ExpressRoute | Opzionale — solo se la latenza VPN impatta i job HPC |

> **Rischio R06**: Latenza VPN Sede→Azure può essere inadeguata per job HPC dati-intensivi. Test di latenza pre-migrazione obbligatori. ExpressRoute come alternativa (costo +€3.600/anno).

## Workflow job HPC ibrido

1. Utente invia job su front-end on-prem (PBS/Torque)
2. Front-end on-prem forwarda job a CycleCloud head node (Standard_D2s_v3) via SSH/API
3. CycleCloud valuta risorse disponibili on-prem vs necessità job
4. Se risorse on-prem insufficienti → CycleCloud provisiona VM HB176-96rs v4 in Azure (SPOT)
5. Dati job copiati su Azure Managed Lustre (condiviso)
6. Job eseguito su nodi Azure **oppure** on-prem (mai ibrido MPI cross-sito)
7. Risultati riscritti su Lustre
8. A job completato: nodi Azure deallocati (nessun costo idle)

### Checkpointing

Poiché le istanze Azure sono SPOT, è obbligatorio il checkpoint periodico dei job:

```bash
# Esempio checkpoint con ciclo job: salva stato ogni 30 min
checkpoint_period=1800  # 30 secondi
while job_running; do
    sleep $checkpoint_period
    save_checkpoint /shared/lustre/checkpoints/$JOB_ID
done
```
