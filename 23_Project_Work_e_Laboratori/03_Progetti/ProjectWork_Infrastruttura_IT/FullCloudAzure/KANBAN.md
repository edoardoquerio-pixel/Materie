# Personal Kanban — Full Cloud Azure (TP Group)

## 🧱 BACKLOG (Idee / Da approfondire)

| Carta | Priorità | Note |
|---|---|---|
| Valutare Azure Hybrid Benefit per licenze MS SQL esistenti | Media | Possibile risparmio su Azure SQL |
| Definire policy di governance Azure (tag, budget, RBAC) | Alta | Controllo costi e sicurezza |
| Scegliere 2° ISP per ridondanza connettività sede | Alta | Business continuity |
| Valutare Azure Front Door per Pondus multi-regione | Bassa | Scenario futuro |
| Definire piano di test funzionali per ogni area | Media | Requisito offerta |

---

## 📋 TODO (Da fare)

| # | Area | Carta | Dettaglio | Stakeholder |
|---|---|---|---|---|
| 1 | **Rete/VPN** | Progettare connettività Azure + sede unificata | VPN IPsec Sede→Azure, Client VPN, DNS | Thema → TP Group |
| 2 | **Sicurezza** | Stesura policy sicurezza cloud (ISO 27001) | Entra ID MFA, Defender, Conditional Access | Tutti |
| 3 | **Sicurezza** | Piano di disaster recovery cloud | Azure Site Recovery, RPO/RTO | Thema + Pro Studio |
| 4 | **Cloud** | Integrazione AD Samba4 → Entra ID | Entra Connect Sync, MFA, SSO | Pro Studio |
| 5 | **Cloud** | Migrazione servizi Pro Studio (GCP→Azure) | MediaWiki, identità, dismissione GCP | Pro Studio |
| 6 | **HPC** | Specifica cluster HPC ibrido (on-prem + Azure) | CycleCloud, HB176-48rs, InfiniBand | Thema |
| 7 | **Pondus** | Migrazione Pondus ad Azure App Service | C# legacy, Azure SQL, deployment | Thema |
| 8 | **Backup** | Soluzione backup cloud-native | Azure Backup, Site Recovery, retention | Thema + Pro Studio |
| 9 | **Logistica** | Piano trasloco dipendenti Pro Studio | Postazioni LAN, banchi, tempistiche | Pro Studio → Thema |
| 10 | **Offerta** | Redigere offerta tecnico-economica variante | Costi Azure, licenze, servizi | — |

---

## 🔧 IN PROGRESS (In corso)

| # | Area | Carta | Assegnatario | Stato |
|---|---|---|---|---|
| — | — | — | — | — |

---

## ✅ DONE (Completato)

| # | Carta | Note |
|---|---|---|
| 1 | Analisi documento estratto_progetto | Scenario compreso, requisiti estratti |
| 2 | Documento perimetro Full Cloud Azure | 12 servizi mappati (M1-M12) |
| 3 | Architettura TO-BE e schema connettività | Azure West Europe, VNet, VPN |

---

## 📊 Riepilogo carichi di lavoro

| Area | Backlog | Todo | In Progress | Done |
|---|---|---|---|---|
| 🌐 Rete / VPN | 1 | 1 | — | — |
| 🔒 Sicurezza ISO 27001 | — | 2 | — | — |
| 🖥️ Cluster HPC | — | 1 | — | — |
| 📱 App Pondus | 1 | 1 | — | — |
| ☁️ Cloud Migration | — | 2 | — | 3 |
| 💾 Backup / DR | — | 1 | — | — |
| 📄 Offerta documenti | — | 1 | — | — |
| 📋 Project Management | — | — | — | — |
| 🏗️ Architettura / Assessment | — | — | — | — |
| 🚚 Logistica | — | 1 | — | — |

---

> **Legenda priorità:** 🔴 Alta | 🟡 Media | 🟢 Bassa
>
> Creato il: 07/07/2026 — Revisionalo settimanalmente.
