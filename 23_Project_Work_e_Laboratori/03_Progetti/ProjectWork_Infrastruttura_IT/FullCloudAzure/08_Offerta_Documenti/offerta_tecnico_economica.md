# Offerta Tecnico-Economica — Variante Full Cloud Azure

> **Progetto:** Integrazione IT TP Group (Thema Consulting + Pro Studio)
> **Variante:** Full Cloud Azure + Ecosistema Microsoft
> **Budget:** € 520.000 + IVA
> **Data:** Luglio 2026

---

## 1. Sintesi della variante

La presente offerta descrive la variante **Full Cloud Azure** per il progetto di integrazione IT tra Thema Consulting srl e Pro Studio srl. Tutti i servizi IT (escluso cluster HPC on-prem) vengono migrati sull'ecosistema Microsoft: M365 Business Premium, Dynamics 365 e Azure.

## 2. Perimetro

| Incluso | Escluso |
|---|---|
| M1-M12: tutti i 12 servizi mappati | Cluster HPC on-prem (8 nodi esistenti) |
| Connettività VPN Sede→Azure | Laptop e postazioni utente |
| Backup e DR cloud-native | Arredi e infrastruttura fisica sede |
| Sicurezza ISO 27001 (strumenti Azure) | — |
| Formazione utenti e affiancamento | — |

## 3. Soluzione tecnica

### 3.1 Produttività e identità (M365 Business Premium)

| Servizio | Destinazione | Utenti |
|---|---|---|
| Posta / Calendario | Exchange Online | 50 |
| Suite Office | Office 365 desktop + web | 50 |
| Videoconferenza | MS Teams | 50 |
| Identità / MFA | Entra ID P1 + Conditional Access | 50 |
| File server | SharePoint Online + OneDrive | 50 |
| Protezione | Defender for Office 365 | 50 |

### 3.2 Applicazioni gestionali (Dynamics 365)

| Applicazione | Prodotto | Utenti |
|---|---|---|
| CRM | Dynamics 365 Sales Professional | 20 |
| ERP / Contabilità | Dynamics 365 Business Central Essentials | 10 |
| Timesheet | Dynamics 365 Business Central (incluso) | 10 |

### 3.3 Cloud (Azure)

| Servizio | SKU | Scopo |
|---|---|---|
| App Service P1v3 | Linux/Windows, 2 vCPU, 8 GB RAM | Pondus Web App |
| Azure SQL DB S2 | 50 DTU, 250 GB | Pondus Database |
| VM B2s | 2 vCPU, 4 GB RAM, 30 GB disk | Media Wiki |
| VPN Gateway | VpnGw1AZ (active-standby) | Connettività Sede→Azure |
| Azure DevOps | 50 utenti | Repos + Pipelines |

### 3.4 Cluster HPC ibrido

| Componente | Specifica |
|---|---|
| On-prem | 8 nodi esistenti (mantenuti) |
| Azure burst | CycleCloud + HB176-96rs v4 (8 nodi SPOT) |
| Filesystem | Azure Managed Lustre (4 TB) |

### 3.5 Backup e DR

| Servizio | Strumento |
|---|---|
| Backup VM | Azure Backup (RA-GRS) |
| DB SQL | PITR + long-term retention |
| DR cross-regione | Azure Site Recovery (West EU → North EU) |

### 3.6 Rete e sicurezza

| Componente | Specifica |
|---|---|
| Firewall | FortiGate FG-100F HA cluster |
| Switch L3 | 48 porte PoE+ stackable |
| VPN Sede→Azure | IPsec IKEv2 — 250 Mbps |
| VPN Client | WireGuard + Azure VPN Client |
| 2° ISP | FTTH 1 Gbps ridondante |
| SIEM (opzionale) | Microsoft Sentinel (add-on) |

## 4. Quadro economico

### 4.1 Investimento iniziale (una tantum)

| Area | Voce | Importo |
|---|---|---|
| **Rete/VPN** | FortiGate FG-100F HA, switch, AP, cablaggio, 2° ISP (1 anno) | € 23.000 |
| **Sicurezza** | Licenze, configurazione ISO 27001, audit iniziale | € 11.500 |
| **Cluster HPC** | Rinnovo licenze, potenziamento InfiniBand | € 16.000 |
| **Pondus** | Analisi compatibilità, setup iniziale Azure | € 8.500 |
| **Cloud Migration** | Migrazione servizi (M1-M11) — una tantum | € 12.000 |
| **Backup/DR** | Configurazione iniziale Azure Backup + Site Recovery | € 7.200 |
| **Costi migrazione totali** | | **€ 78.200** |

### 4.2 Servizi cloud Microsoft/ Azure (ricorrenti)

| Voce | Costo/mese | Costo/anno |
|---|---|---|
| M365 Business Premium (50 utenti × €20,60) | € 1.030 | € 12.360 |
| Dynamics 365 Sales Pro (20 utenti × €56,30) | € 1.126 | € 13.512 |
| Dynamics 365 BC Essentials (10 utenti × €69,30) | € 693 | € 8.316 |
| Azure App Service P1v3 | € 113,50 | € 1.362 |
| Azure SQL DB S2 | € 64 | € 772 |
| Azure DevOps (45 utenti × €5,25) | € 236,25 | € 2.835 |
| VM B2s Media Wiki | € 30,60 | € 367 |
| Azure VPN Gateway | € 97,50 | € 1.170 |
| Backup + DR (Azure) | € 115 | € 1.380 |
| HPC CycleCloud + Lustre + head node (8 nodi SPOT × 200 gg × 8h) | ~€ 1.768 | € 21.219 |
| **Totale ricorrente/anno** | **~€ 4.174** | **~€ 63.293** |

### 4.3 Budget complessivo

| Voce | Importo |
|---|---|
| Budget totale progetto | € 520.000 |
| **Investimento iniziale (una tantum)** | **€ 78.200** |
| **Servizi cloud anno 1** | **€ 63.293** |
| **Totale anno 1** | **€ 141.493** |
| Costi risorse (extra budget) | — |
| **Margine residuo** | **~€ 396.262** |
| Costi risorse (sistemista 55gg + PM 17gg) — extra budget | € 38.550 |

### 4.4 Costi su 3 anni (ciclo vita progetto)

| Anno | Una tantum | Ricorrenti | Totale |
|---|---|---|---|
| Anno 1 | € 78.200 | € 45.538 | € 123.738 |
| Anno 2 | € 0 | € 45.538 | € 45.538 |
| Anno 3 | € 0 | € 45.538 | € 45.538 |
| **Cumulato 3 anni** | **€ 78.200** | **€ 136.614** | **€ 214.814** |
| Risparmio dismissione servizi legacy (3 anni) | | | ~€ 60.000 |
| **Costo netto 3 anni** | | | **~€ 154.814** |

### 4.5 Costi evitati

| Servizio dismesso | Costo evitato/anno |
|---|---|
| Google Workspace (20 utenti) | ~€ 2.400 |
| Odoo SaaS (20 utenti) | ~€ 4.800 |
| BitBucket (20 utenti) | ~€ 660 |
| Manutenzione NAS QNAP + SAN NetApp | ~€ 4.500 |
| Elettricità datacenter (VM dismesse) | ~€ 1.320 |
| Licenze MS SQL Server | ~€ 2.000 |
| **Totale risparmio/anno** | **~€ 15.680** |
| **Risparmio in 3 anni** | **~€ 47.040** |
