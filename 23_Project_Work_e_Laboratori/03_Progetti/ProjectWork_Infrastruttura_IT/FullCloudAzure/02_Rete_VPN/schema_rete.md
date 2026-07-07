# Schema Rete — Full Cloud Azure

```
                 ┌─────────────────────────────────────────────────────────────────┐
                 │                        SEDE TORINO                              │
                 │                                                                 │
                 │    ┌──────────────────────┐     ┌──────────────────────┐        │
                 │    │   FortiGate FG-100F   │─────│   FortiGate FG-100F  │        │
                 │    │      (MASTER)         │     │      (SLAVE)         │        │
                 │    └──────────┬───────────┘     └──────────────────────┘        │
                 │               │     HA Cluster (A-P)                            │
                 │         ┌─────┴──────┐                                          │
                 │         │ Switch L3  │─────── Internet (ISP1 + ISP2)            │
                 │         │   Core     │                                          │
                 │         └─────┬──────┘                                          │
                 │               │                                                 │
                 │    ┌──────────┼──────────────┐                                 │
                 │    │          │              │                                  │
                 │ ┌──┴───┐  ┌──┴───┐     ┌────┴────┐                            │
                 │ │VLAN10│  │VLAN20│     │VLAN30   │                            │
                 │ │  LAN │  │  HPC │     │ Server  │                            │
                 │ │40 pz │  │8+8   │     │ AD/Samba│                            │
                 │ └──────┘  │ nodi │     └─────────┘                            │
                 │           └──┬───┘                                            │
                 │              │   InfiniBand (on-prem cluster)                  │
                 └──────────────┼────────────────────────────────────────────────┘
                                │ IPsec IKEv2
                                │
                 ┌──────────────┴────────────────────────────────────────────────┐
                 │                    AZURE WEST EUROPE                          │
                 │                                                               │
                 │    ┌─────────────────────────────────────────────────────┐    │
                 │    │                  VNet 10.30.0.0/16                  │    │
                 │    │                                                      │    │
                 │    │  ┌─────────────┐  ┌──────────────────────────────┐  │    │
                 │    │  │ snet-vpn    │  │  snet-mediawiki (10.30.1.0/24)│  │    │
                 │    │  │ 10.30.254.0 │  │  ┌──────────────────┐       │  │    │
                 │    │  │   /24       │  │  │  VM B2s          │       │  │    │
                 │    │  │             │  │  │  MediaWiki       │       │  │    │
                 │    │  │ VPN Gateway │  │  └──────────────────┘       │  │    │
                 │    │  │ VpnGw1AZ    │  │                              │  │    │
                 │    │  └─────────────┘  │  ┌──────────────────────────┐│  │    │
                 │    │                   │  │ snet-appsvc (10.30.2.0/24)││  │    │
                 │    │                   │  │  App Service P1v3        ││  │    │
                 │    │                   │  │  (Pondus)                ││  │    │
                 │    │                   │  └──────────────────────────┘│  │    │
                 │    │                   │                              │  │    │
                 │    └───────────────────┴──────────────────────────────┘  │    │
                 │                                                               │
                 │    ┌─────────────────────────────────────────────────────┐    │
                 │    │              Servizi Microsoft                       │    │
                 │    │                                                      │    │
                 │    │  ┌──────────┐  ┌────────┐  ┌──────────────────┐    │    │
                 │    │  │Exchange  │  │ Teams  │  │ SharePoint       │    │    │
                 │    │  │ Online   │  │        │  │ Online + OneDrive│    │    │
                 │    │  └──────────┘  └────────┘  └──────────────────┘    │    │
                 │    │  ┌──────────────┐  ┌───────────────────────────┐   │    │
                 │    │  │ Dynamics 365 │  │ Azure DevOps              │   │    │
                 │    │  │ Sales + BC   │  │ Repos + Pipelines         │   │    │
                 │    │  └──────────────┘  └───────────────────────────┘   │    │
                 │    └─────────────────────────────────────────────────────┘    │
                 │                                                               │
                 │    ┌─────────────────────────────┐                           │
                 │    │     Azure Backup + DR        │                           │
                 │    │  Backup Vault (RA-GRS)       │                           │
                 │    │  Site Recovery (N. Europe)   │                           │
                 │    └─────────────────────────────┘                           │
                 └─────────────────────────────────────────────────────────────┘

Legenda:
────► Traffico VPN IPsec
- - ► Traffico Internet diretto (non VPN)
```

## Resource Group e naming

| Risorsa | Nome |
|---|---|
| Resource Group | `rg-tpgroup-westeu` |
| VNet | `vnet-tpgroup-westeu` — 10.30.0.0/16 |
| VPN Gateway | `vpngw-tpgroup-westeu` |
| VM Media Wiki | `vm-tpgroup-mediawiki-westeu` |
| App Service | `app-tpgroup-pondus-westeu` |
| SQL Server | `sql-tpgroup-pondus-westeu` |
| Backup Vault | `bvault-tpgroup-westeu` |
| Recovery Vault | `rvault-tpgroup-westeu` |
