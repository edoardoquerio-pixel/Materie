# Specifica Cluster HPC Ibrido — On-Prem + Azure CycleCloud

## Architettura

```
Sede Torino                          Azure West Europe
┌──────────────────────┐            ┌────────────────────────────┐
│  Cluster On-Prem      │            │  Azure CycleCloud          │
│                        │            │                            │
│ 8 nodi esistenti       │            │ HB176-48rs (16 nodi burst) │
│ (HW proprietario)      │◄───IPsec──►│ nic_hpc (10.30.100.0/24)  │
│ InfiniBand interconnect│            │ InfiniBand SR-IOV          │
│                        │            │                            │
│ Front-end VM (Linux)   │            │ Azure Managed Lustre       │
│ └→ PBS/Torque job queue│            │ (Lustre filesystem)        │
└──────────────────────┘            └────────────────────────────┘
```

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
| VM | **Standard HB176-48rs** (176 vCPU, 48 GB RAM, InfiniBand HDR100) |
| Nodi massimi | 16 nodi (configurabile in base a budget) |
| Connettività | InfiniBand SR-IOV (HDR100, 100 Gbps) |
| Filesystem | **Azure Managed Lustre** (POSIX compliant, latenza < 5 ms) |
| Scheduler | PBS/Torque (compatibile con on-prem) |
| OS | AlmaLinux 8.x HPC (immagine Azure ottimizzata) |
| Regione | West Europe |

### Azure Managed Lustre

| Parametro | Valore |
|---|---|
| Throughput | 500 MB/s per TB di storage |
| Capacità | 4 TB (sufficiente per job HPC) |
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
| HB176-48rs (16 nodi, 8 ore/giorno, 200 gg/anno) | € 3,87/h | € 61,92 | € 12.384 |
| Azure Managed Lustre (4 TB) | — | € 2,67 | € 960 |
| CycleCloud (licenza gratuita) | — | — | € 0 |
| **Totale HPC Azure/anno** | | | **~€ 13.344** |

*8 ore/giorno × 16 nodi  
**200 giorni lavorativi/anno

### Confronto costi

| Scenario | On-prem 8 nodi (esistenti) | + Azure 16 nodi (burst) | Delta |
|---|---|---|---|
| Costo capitale (HW 16 nodi acquisto) | — | ~€ 192.000 (evitato) | **€ -192.000** |
| Costo operativo annuo | ~€ 18.000 | + € 13.344 (Azure) | **€ +13.344** |

La scelta CycleCloud consente di evitare l'acquisto di 8 nuovi nodi HPC fisici (~€ 192.000), utilizzando invece risorse Azure a consumo con un costo operativo di ~€ 13.344/anno.

## Configurazione di rete Azure

| Parametro | Valore |
|---|---|
| VNet HPC | `vnet-tpgroup-westeu` — 10.30.0.0/16 |
| Subnet HPC burst | `snet-hpc-westeu` — 10.30.100.0/24 |
| Subnet Lustre | `snet-lustre-westeu` — 10.30.101.0/24 |
| NSG | Allow InfiniBand (tra nodi), Allow SSH (da front-end on-prem) |
| VPN | IPsec IKEv2 — 10.10.0.0/16 → 10.30.100.0/24 |

## Workflow job HPC ibrido

1. Utente invia job su front-end on-prem (PBS/Torque)
2. Scheduler CycleCloud (su front-end) valuta risorse necessarie
3. Se risorse on-prem insufficienti → CycleCloud provvede VM HB176-48rs in Azure
4. Dati job copiati su Azure Managed Lustre
5. Job eseguito su nodi Azure + on-prem (paritetico)
6. Risultati riscritti su Lustre
7. A job completato: nodi Azure deallocati (nessun costo idle)
