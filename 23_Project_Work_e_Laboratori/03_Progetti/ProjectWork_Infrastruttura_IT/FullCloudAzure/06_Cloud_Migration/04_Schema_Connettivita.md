# 04 — Schema Connettività

> **Documento:** Schema connettività di rete e identità per TP Group Full Cloud Azure  
> **Data:** Luglio 2026

---

## Schema generale

```
Sede Torino (Thema)                    Azure West Europe
┌──────────────────────────┐          ┌──────────────────────────────┐
│   Fortigate FG-100F      │◄──IPsec──│   VPN Gateway VpnGw1AZ       │
│   (HA cluster)           │────────► │   10.30.0.0/16               │
│   10.10.0.0/16           │          │                              │
└──────────┬───────────────┘          └──────────┬───────────────────┘
           │                                     │
           ▼                                     ▼
    ┌──────────────┐                     Subnet: 10.30.1.0/24
    │ AD Samba4  ◄─┼────IPsec────          └→ VM B2s (Media Wiki)
    │ (identità)  │                     Subnet: 10.30.2.0/24
    └──────┬───────┘                      └→ App Service VNet int.
           │ ▼                            Subnet: 10.30.99.0/24
    Entra Connect Sync                     └→ VM D2s_v3 (CycleCloud)
           ↓                            Subnet: 10.30.100.0/24
    Entra ID (cloud)                       └→ HB176-96rs v4 (burst SPOT)
                                          Subnet: 10.30.101.0/24
                                            └→ Azure Managed Lustre
                                          Subnet: 10.30.254.0/24
                                            └→ VPN Gateway

Utenti remoti                          M365 Cloud
┌──────────────┐                      ┌───────────────────┐
│ VPN client   │───IPsec──►Fortigate──► Exchange Online   │
│ WireGuard    │                      │ Teams             │
│ + Internet   │                      │ SharePoint        │
└──────────────┘                      │ OneDrive          │
                                      │ Dynamics 365      │
                                      │ Azure DevOps      │
                                      └───────────────────┘
```

---

## Dettaglio connettività

### Sede Torino → Azure (IPsec VPN)

| Parametro | Valore |
|---|---|
| Dispositivo on-prem | Fortigate FG-100F (HA cluster) |
| Gateway Azure | VPN Gateway VpnGw1AZ (active-standby) |
| Tunnel | IPsec IKEv2 |
| Subnet on-prem | 10.10.0.0/16 |
| Subnet Azure | 10.30.0.0/16 |
| Routing | BGP (dynamic) o static routes |
| Latenza prevista | &lt; 5 ms (Torino → West Europe) |

### Sede Torino → M365 / Internet

| Parametro | Valore |
|---|---|
| Autenticazione | Entra ID (via Internet, non VPN) |
| Posta | Exchange Online via MAPI/HTTPS |
| Teams | Media traffic diretto a M365 CDN |
| SharePoint | HTTPS diretto |

### Utenti remoti → Sede + Cloud

| Parametro | Valore |
|---|---|
| VPN remota | WireGuard su Fortigate |
| Lavoratori remoti | Minimo 10/giorno |
| Traffico cloud (M365, Dynamics, DevOps) | Diretto a Internet (non VPN) |
| Traffico on-prem (HPC, backup) | Via VPN WireGuard |

### Azure HPC — subnet e connettività

Il cluster HPC adotta un'architettura **dual-network**:

- **Ethernet (management):** traffico SSH, API CycleCloud, mount Lustre, backup — attraversa FortiGate (on-prem) e NSG (Azure) con policy controllate.
- **InfiniBand (compute):** traffico MPI/RDMA tra nodi HBv4 — rete trusted isolata, **nessun firewall** (necessario per latenza &lt; 2 μs). Le due fabbriche InfiniBand (on-prem e Azure) non sono interconnesse: i job MPI non attraversano mai la VPN.

| Subnet Azure | CIDR | Risorse |
| --- | --- | --- |
| `snet-cyclecloud-westeu` | 10.30.99.0/24 | VM D2s_v3 (CycleCloud head node) |
| `snet-hpc-westeu` | 10.30.100.0/24 | HB176-96rs v4 (burst SPOT, 8 nodi max) |
| `snet-lustre-westeu` | 10.30.101.0/24 | Azure Managed Lustre (4 TB, via NFS/Internal) |

---

## Flussi di identità

```
┌──────────┐     ┌─────────────────┐     ┌──────────────┐
│ AD Samba4│────►│ Entra Connect   │────►│ Entra ID     │
│ (on-prem)│     │ Sync (server    │     │ (cloud)      │
│          │     │ on-prem o VM    │     │              │
│ 50 utenti│     │ Azure)          │     │   MFA + CA   │
└──────────┘     └─────────────────┘     └──────┬───────┘
                                                │
                              ┌─────────────────┼─────────────────┐
                              ▼                 ▼                 ▼
                      ┌────────────┐   ┌──────────────┐   ┌──────────────┐
                      │ Exchange   │   │ SharePoint   │   │ Dynamics 365 │
                      │ Online     │   │ Online       │   │              │
                      └────────────┘   └──────────────┘   └──────────────┘
                              ┌──────────────────────────────┐
                              │         Azure DevOps         │
                              └──────────────────────────────┘
```

---

## Resource Group e naming convention

| Risorsa | Nome |
|---|---|
| Resource Group | `rg-tpgroup-migration-westeu` |
| VNet | `vnet-tpgroup-westeu` — 10.30.0.0/16 |
| Subnet Media Wiki | `snet-mediawiki-westeu` — 10.30.1.0/24 |
| Subnet App Service | `snet-appsvc-westeu` — 10.30.2.0/24 |
| Subnet VPN Gateway | `snet-gateway-westeu` — 10.30.254.0/24 |
| Subnet CycleCloud | `snet-cyclecloud-westeu` — 10.30.99.0/24 |
| Subnet HPC burst | `snet-hpc-westeu` — 10.30.100.0/24 |
| Subnet Lustre | `snet-lustre-westeu` — 10.30.101.0/24 |
| VPN Gateway | `vpngw-tpgroup-westeu` |
| VM Media Wiki | `vm-tpgroup-mediawiki-westeu` |
| VM CycleCloud Head Node | `vm-tpgroup-cyclecloud-westeu` |
| Azure Managed Lustre | `lustre-tpgroup-westeu` |
| App Service Plan | `asp-tpgroup-westeu` |
| App Service | `app-tpgroup-pondus-westeu` |
| Azure SQL Server | `sql-tpgroup-pondus-westeu` |
| Azure SQL DB | `sqldb-tpgroup-pondus-westeu` |

---

## DNS

| Record | Target |
|---|---|
| pondus.tpgroup.it | `app-tpgroup-pondus-westeu.azurewebsites.net` (CNAME) |
| wiki.tpgroup.it | IP pubblico VM Media Wiki (A) o CNAME |
| cyclecloud.tpgroup.it | IP privato `vm-tpgroup-cyclecloud-westeu` (DNS interno) |
| lustre.tpgroup.it | IP privato `lustre-tpgroup-westeu` (DNS interno) |
| tpgroup.it MX | exchange.protection.outlook.com |
| autodiscover.tpgroup.it | autodiscover.outlook.com (CNAME) |
