# Schema Rete — Full Cloud Azure

```
                 ┌──────────────────────────────────────────────────────────────────┐
                 │                        SEDE TORINO                               │
                 │                                                                  │
                 │    ┌──────────────────────┐     ┌──────────────────────┐         │
                 │    │   FortiGate FG-100F   │─────│   FortiGate FG-100F  │         │
                 │    │      (MASTER)         │     │      (SLAVE)         │         │
                 │    └──────────┬───────────┘     └──────────────────────┘         │
                 │               │     HA Cluster (A-P)                             │
                 │         ┌─────┴──────┐                                           │
                 │         │ Switch L3  │─────── Internet (ISP1 + ISP2)             │
                 │         │   Core     │                                           │
                 │         └─────┬──────┘                                           │
                 │               │                                                  │
                 │    ┌──────────┼──────────────┐                                  │
                 │    │          │              │                                   │
                 │ ┌──┴───┐  ┌──┴───┐     ┌────┴────┐   ┌───────────────────┐     │
                 │ │VLAN10│  │VLAN20│     │VLAN30   │   │  InfiniBand Switch │     │
                 │ │  LAN │  │  HPC │     │ Server  │   │  (on-prem cluster) │     │
                 │ │40 pz │  │8 nodi│     │ AD/Samba│   │  MPI/RDMA only     │     │
                 │ └──────┘  └──┬───┘     └─────────┘   │  <2μs latenza       │     │
                 │              │    Ethernet (mgmt)     └─────────┬───────────┘     │
                 │              │    SSH, Lustre, API              │ InfiniBand      │
                 │              │    ──── FortiGate ────►          │ (isolata)       │
                 │              │    (controllato)                 │ (non controll.) │
                 │              └──────────┼───────────────────────┘                 │
                 └─────────────────────────┼─────────────────────────────────────────┘
                                           │ IPsec IKEv2 (solo Ethernet)
                                           │
                 ┌─────────────────────────┴─────────────────────────────────────────┐
                 │                    AZURE WEST EUROPE                              │
                 │                                                                  │
                 │    ┌────────────────────────────────────────────────────────┐    │
                 │    │                  VNet 10.30.0.0/16                     │    │
                 │    │                                                         │    │
                 │    │  ┌─────────────────┐  ┌─────────────────────────────┐  │    │
                 │    │  │ snet-hpc        │  │ snet-cyclecloud (10.30.99.0) │  │    │
                 │    │  │ 10.30.100.0/24  │  │ ┌───────────────────────┐   │  │    │
                 │    │  │ HB176-96rs v4   │  │ │ CycleCloud Head Node  │   │  │    │
                 │    │  │ InfiniBand NDR  │  │ │ (Standard_D2s_v3)     │   │  │    │
                 │    │  │ 400 Gbps fabric │  │ └───────────────────────┘   │  │    │
                 │    │  └─────────────────┘  └─────────────────────────────┘  │    │
                 │    │                                                         │    │
                 │    │  ┌─────────────────┐  ┌─────────────────────────────┐  │    │
                 │    │  │ snet-lustre     │  │ snet-mediawiki (10.30.1.0)  │  │    │
                 │    │  │ 10.30.101.0/24  │  │ ┌──────────────────┐       │  │    │
                 │    │  │ Managed Lustre  │  │ │  VM B2s          │       │  │    │
                 │    │  │ 4 TB POSIX      │  │ │  MediaWiki       │       │  │    │
                 │    │  └─────────────────┘  │ └──────────────────┘       │  │    │
                 │    │                        │                              │  │    │
                 │    │  ┌─────────────────┐  │ ┌────────────────────────┐ │  │    │
                 │    │  │ snet-appsvc     │  │ │ snet-vpn              │ │  │    │
                 │    │  │ 10.30.2.0/24    │  │ │ 10.30.254.0/24        │ │  │    │
                 │    │  │ App Service     │  │ │ VPN Gateway VpnGw1AZ  │ │  │    │
                 │    │  │ Pondus          │  │ └────────────────────────┘ │  │    │
                 │    │  └─────────────────┘  └─────────────────────────────┘  │    │
                 │    └────────────────────────────────────────────────────────┘    │
                 │                                                                  │
                 │    ┌────────────────────────────────────────────────────────┐    │
                 │    │              Servizi Microsoft                          │    │
                 │    │                                                         │    │
                 │    │  ┌──────────┐  ┌────────┐  ┌──────────────────┐       │    │
                 │    │  │Exchange  │  │ Teams  │  │ SharePoint       │       │    │
                 │    │  │ Online   │  │        │  │ Online + OneDrive│       │    │
                 │    │  └──────────┘  └────────┘  └──────────────────┘       │    │
                 │    │  ┌──────────────┐  ┌───────────────────────────┐      │    │
                 │    │  │ Dynamics 365 │  │ Azure DevOps              │      │    │
                 │    │  │ Sales + BC   │  │ Repos + Pipelines         │      │    │
                 │    │  └──────────────┘  └───────────────────────────┘      │    │
                 │    └────────────────────────────────────────────────────────┘    │
                 │                                                                  │
                 │    ┌─────────────────────────────┐                              │
                 │    │     Azure Backup + DR        │                              │
                 │    │  Backup Vault (RA-GRS)       │                              │
                 │    │  Site Recovery (N. Europe)   │                              │
                 │    └─────────────────────────────┘                              │
                 └──────────────────────────────────────────────────────────────────┘

Legenda:
────► Traffico VPN IPsec (Ethernet/management) — controllato da FortiGate + NSG
-.- ► Traffico InfiniBand (MPI/RDMA) — NON passa da FortiGate, rete trusted
```

## Dual-network HPC

| Rete | On-prem | Azure | Controllo |
|------|---------|-------|-----------|
| **Ethernet** (management) | VLAN 20 → Switch L3 → FortiGate | Azure SmartNIC v2 → snet-hpc → NSG | ✅ FortiGate + NSG |
| **InfiniBand** (calcolo) | InfiniBand Switch (cluster) | ConnectX-7 NDR 400 Gbps (fabric Azure) | ❌ Nessuno (rete trusted, <2μs) |

> L'InfiniBand non attraversa mai il FortiGate né la VPN. Le due fabric (on-prem e Azure) sono separate. MPI job non cross-sito.

## Resource Group e naming

| Risorsa | Nome |
|---|---|
| Resource Group | `rg-tpgroup-westeu` |
| VNet | `vnet-tpgroup-westeu` — 10.30.0.0/16 |
| Subnet HPC burst | `snet-hpc-westeu` — 10.30.100.0/24 |
| Subnet Lustre | `snet-lustre-westeu` — 10.30.101.0/24 |
| Subnet CycleCloud | `snet-cyclecloud-westeu` — 10.30.99.0/24 |
| VPN Gateway | `vpngw-tpgroup-westeu` |
| VM Media Wiki | `vm-tpgroup-mediawiki-westeu` |
| App Service | `app-tpgroup-pondus-westeu` |
| SQL Server | `sql-tpgroup-pondus-westeu` |
| Backup Vault | `bvault-tpgroup-westeu` |
| Recovery Vault | `rvault-tpgroup-westeu` |
