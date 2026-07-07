# Agente: HPC Architect — Full Cloud Azure

## Ruolo

Progettazione del cluster HPC ibrido (on-prem + Azure) per simulazioni strutturali FEM e crash test di TP Group.

## Dipende da

- `01_Assessment/` (dati AS-IS Thema cluster HPC)
- `02_Rete_VPN/` (connettività a bassa latenza Sede→Azure)

## Deliverable

| # | File | Contenuto |
|---|---|---|
| 01 | `specifica_cluster_hpc.md` | Specifica tecnica cluster ibrido |

## Decisioni chiave Full Cloud Azure

- **Rimangono on-prem**: 8 nodi esistenti (HW proprietario, InfiniBand)
- **Nuovi nodi**: **Azure CycleCloud** con VM **HB176-96rs v4** (8 nodi burst SPOT)
- **Connettività**: VPN IPsec Sede→Azure per cyclecloud; ExpressRoute opzionale
- **Storage**: Azure Managed Lustre per filesystem condiviso
- **Costi**: Solo SPOT con checkpointing obbligatorio (deallocazione quando non usati)
- **Requisiti**: 8 GB/core rispettato (768 GB / 96 vCPU)
