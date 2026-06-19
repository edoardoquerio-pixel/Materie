# Specifica Cluster HPC — Variante Ibrida

## REQUISITI

- 8 nodi esistenti Thema on-premise (da mantenere)
- 8 nuovi nodi on-premise (da acquistare)
- GCP per burst/overflow HPC (carichi non critici, picchi)
- Rete InfiniBand on-premise per nodi esistenti + nuovi
- Ethernet 25 GbE per connettività cloud
- Stessi requisiti tecnici: 2 CPU, ≥24 core, 8 GB RAM/core, NO GPU, Linux

## SOLUZIONE

### Architettura ibrida

```
[Sede Thema — On-prem]                          [GCP]
       |                                             |
[16 nodi HPC + Front-end]                    [C2 istanze burst]
       |                                             |
[InfiniBand HDR 200 Gbps]          [Cloud VPN / Interconnect]
       |                                             |
[Ethernet 25 GbE] ──────── IPsec ──────── [GCP VPC]
```

### Nodi on-premise (8 nuovi)

Stessa specifica della Variante B: AMD EPYC 9474F, 96 core, 768 GB RAM, 1,6 TB NVMe.

### HPC su GCP (burst)

| Parametro | Valore |
|---|---|
| **Tipo istanza** | C2-standard-60 (60 vCPU, 240 GB RAM) |
| **Nodi burst** | Fino a 16 (scalati su richiesta) |
| **Utilizzo** | Simulazioni non critiche, preprocessing, post-processing |
| **Storage** | Persistent Disk + object storage per dati condivisi |

## DIMENSIONAMENTO

| Elemento | On-prem | Cloud burst |
|---|---|---|
| Nodi calcolo | 16 (8 esistenti + 8 nuovi) | 0-16 (on-demand) |
| Core totali | 96 × 8 + esistenti | 960 vCPU (massimo) |
| RAM totale | 6.144 GB (nuovi) | 3.840 GB (massimo) |
| Interconnessione | InfiniBand 200 Gbps | 100 Gbps Ethernet |
| Storage scratch | NVMe 1,6 TB per nodo | Local SSD 3 TB per istanza |
| Raffreddamento | InRow DX (on-prem) | N/A (cloud) |

## COSTI

| Voce | Una tantum | Annuale |
|---|---|---|
| 8 nodi on-prem (AMD EPYC) | ~€180.000 | ~€24.000 (energia+raffreddamento) |
| InfiniBand + Ethernet | ~€37.000 | — |
| Raffreddamento + armadio | ~€18.000 | — |
| GCP burst (500 ore/mese, 8 istanze C2) | — | ~$72.000 (on-demand) / ~$43.200 (CUD) |
| **Totale** | **~€235.000** | **~€24.000 + ~$72.000 cloud** |
