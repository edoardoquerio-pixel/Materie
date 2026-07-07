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
- **Nuovi nodi**: **Azure CycleCloud** con VM **HB176-48rs** (16 nodi burst)
- **Connettività**: VPN IPsec Sede→Azure per cyclecloud
- **Storage**: Azure Managed Lustre per filesystem condiviso
- **Costi**: Nodi Azure solo a consumo (deallocazione quando non usati)
