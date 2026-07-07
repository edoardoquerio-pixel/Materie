# Progetto VPN — Connettività Cloud e Remota

## 1. VPN Sede → Azure (IPsec)

| Parametro | Valore |
|---|---|
| Dispositivo on-prem | FortiGate FG-100F (HA cluster) |
| Gateway Azure | VPN Gateway VpnGw1AZ (active-standby) |
| Protocollo | IPsec IKEv2 |
| Subnet on-prem | 10.10.0.0/16 |
| Subnet Azure | 10.30.0.0/16 |
| Routing | BGP (dynamic) |
| Latenza prevista | < 5 ms (Torino → West Europe) |
| Throughput | ~250 Mbps (tunnel singolo) |
| SKU Gateway | VpnGw1AZ — € 97,50/mese |

### Schema

```
Sede Torino                    Azure West Europe
10.10.0.0/16                   10.30.0.0/16
┌──────────────┐    IPsec     ┌───────────────────┐
│ FortiGate    │◄════════════►│ VPN Gateway        │
│ FG-100F HA   │   IKEv2      │ VpnGw1AZ           │
└──────┬───────┘              └────────┬───────────┘
       │                               │
       ▼                               ▼
   HPC on-prem                    Subnet MediaWiki
   AD Samba4                      (10.30.1.0/24)
   Server                          Subnet App Service
                                   (10.30.2.0/24)
                                   Subnet Gateway
                                   (10.30.254.0/24)
```

## 2. VPN Client Remoto (WireGuard + Azure VPN)

| Tipologia | Protocollo | Destinazione | Utenti |
|---|---|---|---|
| WireGuard | UDP/51820 | Sede Torino (HPC, server) | 50 |
| Azure VPN Client | IKEv2 | Azure (VM, app) | 10 (admin) |

### Flussi di traffico

| Utente | Servizio | Percorso |
|---|---|---|
| Remoto → Posta | Exchange Online | Diretto Internet (no VPN) |
| Remoto → File | SharePoint/OneDrive | Diretto Internet (no VPN) |
| Remoto → HPC | WireGuard → FortiGate → LAN HPC | Via VPN |
| Remoto → Dynamics | Internet diretto | Diretto Internet |
| Remoto → Azure VM | Azure VPN Client | Via Azure VPN Gateway |

## 3. DNS

| Record | Target |
|---|---|
| tpgroup.it MX | `tpgroup-it.mail.protection.outlook.com` |
| autodiscover.tpgroup.it | `autodiscover.outlook.com` (CNAME) |
| pondus.tpgroup.it | `app-tpgroup-pondus-westeu.azurewebsites.net` (CNAME) |
| wiki.tpgroup.it | IP pubblico VM Media Wiki (A) o CNAME |
| dev.azure.com/tpgroup | Azure DevOps organization |

## 4. Costi VPN

| Voce | Una tantum | Ricorrente/mese |
|---|---|---|
| Azure VPN Gateway VpnGw1AZ | — | € 97,50 |
| FortiGate FG-100F (incl. nel progetto rete) | — | — |
| WireGuard (gratuito, incluso in FortiGate) | — | — |
| Azure VPN Client P2S (10 connessioni) | — | € 17,50 |
| **Totale** | **€ 0** | **€ 115,00** |
