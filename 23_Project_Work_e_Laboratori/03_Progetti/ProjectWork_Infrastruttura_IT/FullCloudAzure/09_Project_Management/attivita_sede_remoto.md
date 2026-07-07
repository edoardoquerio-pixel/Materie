# Attività in Sede vs Da Remoto — Check Forniture

> **Documento:** Pianificazione logistica e verifica forniture per il progetto Full Cloud Azure TP Group  
> **Data:** Luglio 2026

---

## Premessa

La sede operativa (Thema Consulting, Torino) dispone già di infrastruttura on-prem con cui lavorava prima della migrazione. Questo documento:

1. **Verifica ogni voce di budget** contro ciò che esiste già, indicando se l'acquisto è necessario o se il componente esistente è riusabile
2. **Identifica gap e sovrapposizioni** tra forniture preventivate e realtà AS-IS
3. **Pianifica** dove e come si svolgono le attività (sede vs remoto)

---

## Check forniture: budget vs. esistente

Ogni riga del budget è analizzata confrontando ciò che è previsto a progetto con ciò che è già presente in sede.

### Rete / VPN

| Voce di budget | Costo | Esistente in sede | Necessario? | Note |
|---------------|:----:|:-----------------:|:-----------:|------|
| **FortiGate FG-100F HA cluster** (×2, FortiCare 3 anni) | € 7.000 | ✅ **FG-60F** (singolo, non HA) | **SÌ** — FG-60F insufficiente | FG-60F ha throughput IPsec ~3 Gbps, insufficiente per VPN site-to-site + 50 utenti remoti + traffico HPC. FG-100F è l'entry level per HA. Il FG-60F può essere riconvertito per laboratorio/DR site |
| **Switch Core L3 48 porte PoE+** (×2) | € 2.400 | ⚠️ **Non documentati** marca/modello | **Probabile SÌ** | Se gli switch esistenti sono L2 non gestiti (tipico per SMB), vanno sostituiti. I due switch L3 coprono core + HPC (VLAN 20) + server (VLAN 30). Se invece esistono già switch L3 gestiti → risparmio €2.400 |
| **Switch accesso 24 porte PoE+** (×3) | € 1.200 | ⚠️ **Non documentati** | **Da verificare** | Se gli switch esistenti sono L2 PoE+ con porte sufficienti (40 postazioni), potrebbero essere riusati. Il budget è comunque contenuto (€1.200 per 3 switch) |
| **Access Point WiFi 6** (×4) | € 1.000 | ⚠️ **Non documentati** | **Probabile SÌ** | Se esistono AP, probabilmente non sono gestiti dal FortiGate (che richiede AP FortiGate-compatibili). Il progetto prevede AP gestiti dal FortiGate per SSID unificato su VLAN 40/50 |
| **UPS rack 1500 VA** (×2) | € 1.200 | ✅ **UPS esistente** con soli 10 min di autonomia | **SÌ** — 10 min insufficienti | L'UPS esistente ha autonomia troppo bassa per spegnimento controllato. I 2 nuovi UPS da 1500 VA garantiscono ~20-30 min per apparati di rete. Il vecchio UPS può servire apparecchiature non critiche |
| **Cablaggio strutturato cat.6A** | € 6.000 | ⚠️ **Non documentato**, probabilmente cat.5e o cat.6 base | **Da verificare** | Se il cablaggio esistente è cat.6 (non 6A) e funzionante, può bastare per 1 GbE alle postazioni. Cat.6A serve per 10 GbE tra switch core e server/HPC. **Verifica in sede necessaria** — possibile risparmio parziale |
| **2° ISP FTTH 1 Gbps** (1 anno) | € 4.200 | ✅ **1 ISP attivo** (provider non specificato) | **SÌ** — singolo ISP è rischio | La migrazione cloud richiede connettività ridondante. Se l'ISP esistente è già 1 Gbps, il 2° ISP può essere anche una linea consumer/business 100-500 Mbps per backup |
| **Subtotale Rete** | **€ 18.800 + € 4.200/anno** | | **Risparmio potenziale:** ~€ 3.000-5.000 | Se switch e cablaggio esistenti sono adeguati |

### Sicurezza

| Voce di budget | Costo | Esistente in sede | Necessario? | Note |
|---------------|:----:|:-----------------:|:-----------:|------|
| **Licenze/configurazione ISO 27001** | € 8.000 | ❌ Nessuna certificazione ISO 27001 attiva | **SÌ** | Include consulenza, policy, procedure, documentazione del SGSA. Non esiste nulla di equivalente |
| **Audit iniziale sicurezza** | € 3.500 | ❌ Nessun audit formale pregresso | **SÌ** | Audit obbligatorio per certificazione |
| **Subtotale Sicurezza** | **€ 11.500** | | **Nessun risparmio** | |

### Cluster HPC

| Voce di budget | Costo | Esistente in sede | Necessario? | Note |
|---------------|:----:|:-----------------:|:-----------:|------|
| **Rinnovo licenze cluster on-prem (3 anni)** | € 10.000 | ✅ **8 nodi HPC attivi** con licenze in scadenza | **SÌ** — rinnovo necessario | Le licenze del cluster on-prem (sistema operativo, scheduler PBS/Torque, librerie MPI, compilatori) vanno rinnovate per continuare l'operatività. Se il cluster è già sotto contratto di manutenzione, verificare la scadenza |
| **Potenziamento InfiniBand** (cavi, switch) | € 6.000 | ✅ **InfiniBand HDR 200 Gbps** (presunto) | **Da verificare** | Le due fabbriche InfiniBand (on-prem HDR, Azure NDR 400 Gbps) sono separate e indipendenti. **Se la fabbrica on-prem HDR funziona correttamente** (cavi in buono stato, switch operativo), il potenziamento potrebbe non essere necessario subito. **Verifica in sede**: testare bit error rate sui cavi esistenti, temperatura switch. Se OK → risparmio €6.000 |
| **HB176-96rs v4 SPOT** (200 gg × 8h) | € 2.144/anno | ❌ Non esistente | **SÌ** | Nuovo servizio cloud, nessuna alternativa on-prem |
| **CycleCloud head node D2s_v3** (24/7) | € 360/anno | ❌ Non esistente | **SÌ** | Nuovo servizio cloud |
| **Azure Managed Lustre 4 TB** | € 960/anno | ❌ Non esistente | **SÌ** | Nuovo servizio cloud |
| **Subtotale HPC** | **€ 16.000 + € 3.464/anno** | | **Risparmio potenziale:** ~€ 6.000 | Se InfiniBand on-prem non necessita upgrade |

### Pondus su Azure

| Voce di budget | Costo | Esistente in sede | Necessario? | Note |
|---------------|:----:|:-----------------:|:-----------:|------|
| **Analisi compatibilità codice** | € 2.000 | ✅ **Server fisico** Xeon Silver 4110, 64 GB, MS SQL | **SÌ** | Va analizzato il codice C# per compatibilità con Azure App Service (container Linux?) e migrazione MS SQL → Azure SQL |
| **Adattamento codice** | € 10.000 | — | **SÌ (da confermare dopo analisi)** | Non si sa ancora se serve. Stimato €10.000 di media, ma potrebbe essere €0 o €25.000. Da verificare dopo analisi compatibilità |
| **Setup Azure App + SQL** | € 1.500 | ❌ Non esistente | **SÌ** | Manodopera per deployment |
| **Test e validazione** | € 2.000 | — | **SÌ** | Collaudo funzionale |
| **App Service P1v3** | € 1.362/anno | ❌ Non esistente | **SÌ** | Nuovo servizio cloud |
| **Azure SQL DB S2** | € 772/anno | ❌ Non esistente | **SÌ** | Nuovo servizio cloud |
| **Subtotale Pondus** | **€ 15.500 + € 2.134/anno** | | **Nessun risparmio** | Costo adattamento codice è una riserva, non una spesa certa |

### Cloud Migration (M1-M11)

| Voce di budget | Costo | Esistente in sede | Necessario? | Note |
|---------------|:----:|:-----------------:|:-----------:|------|
| **Migrazione posta** (Zimbra + GWS → Exchange) | € 1.500 | ✅ **Zimbra (VM)** + **GWS** attivi | **SÌ** | Manodopera sistemista. Include IMAP sync per 50 caselle Thema + Migration API per 20 utenti Pro Studio |
| **Migrazione file** (NextCloud + Drive → SharePoint) | € 2.500 | ✅ **NextCloud (VM)** + **Google Drive** attivi | **SÌ** | Manodopera sistemista con Migration Manager |
| **Setup Entra ID + MFA** | € 1.500 | ✅ **AD Samba4 (VM)** attivo | **SÌ** | Configurazione Entra Connect Sync, Conditional Access, MFA. AD Samba4 esistente è un punto di partenza |
| **Setup Azure DevOps** | € 1.000 | ✅ **GiTea (VM)** + **BitBucket SaaS** attivi | **SÌ** | Migrazione repo con history |
| **Migrazione MediaWiki** | € 500 | ✅ **MediaWiki on-prem** + **GCP** | **SÌ** | Unificazione su VM Azure B2s |
| **Configurazione Dynamics 365** | € 5.000 | ❌ Non esistente | **SÌ** | Consulente Dynamics per Sales + BC |
| **M365 Business Premium** (50 utenti) | € 12.360/anno | ✅ **30 licenze M365 Business Basic** Thema esistenti | **SÌ** ma upgrade | Thema ha già 30 licenze Basic → vanno upgrade a Premium (delta €16/utente/mese × 30). Pro Studio 20 utenti → nuove licenze Premium. Costo totale nel budget è corretto |
| **Dynamics 365 Sales Pro** (20 utenti) | € 13.512/anno | ❌ Non esistente | **SÌ** | Nuovo servizio cloud |
| **Dynamics 365 BC Essentials** (10 utenti) | € 8.316/anno | ❌ Non esistente | **SÌ** | Nuovo servizio cloud |
| **Azure DevOps** (45 utenti) | € 2.835/anno | ❌ Non esistente (BitBucket sì, ma va sostituito) | **SÌ** | Nuovo servizio cloud (5 free + 45 paid) |
| **VM B2s MediaWiki** | € 367/anno | ❌ Non esistente in Azure | **SÌ** | Nuova VM Azure. MediaWiki on-prem verrà spento |
| **Azure VPN Gateway** | € 1.170/anno | ❌ Non esistente | **SÌ** | Nuovo servizio cloud per VPN site-to-site |
| **Subtotale Migration** | **€ 12.000 + € 38.560/anno** | | **Nessun risparmio** (upgrade M365 da Basic a Premium è già scontato) | |

### Backup / DR

| Voce di budget | Costo | Esistente in sede | Necessario? | Note |
|---------------|:----:|:-----------------:|:-----------:|------|
| **Configurazione Azure Backup** | € 3.500 | ✅ **NAS QNAP 32 TB** usato per backup locali | **SÌ** | Configurazione iniziale Azure Backup. Il NAS QNAP resta come buffer temporaneo durante la migrazione, poi verrà dismesso |
| **Configurazione Azure Site Recovery** | € 2.000 | ❌ Nessun DR attivo | **SÌ** | Configurazione replica VM Azure in paired region |
| **Test DR** | € 1.700 | ❌ Nessun test DR pregresso | **SÌ** | Esercitazione annuale DR obbligatoria per ISO 27001 |
| **Azure Backup (VM + SQL + files)** | € 480/anno | — | **SÌ** | Servizio cloud |
| **Blob Storage RA-GRS (HPC, AD)** | € 180/anno | — | **SÌ** | Servizio cloud |
| **M365 Backup** (opzionale) | € 720/anno | ❌ Non esistente | **Da decidere** | Opzionale: M365 ha già retention nativa. Se policy richiede backup esterno per conformità ISO 27001 → necessario |
| **Azure Site Recovery** | € 360/anno | — | **SÌ** | Servizio cloud |
| **Subtotale Backup/DR** | **€ 7.200 + € 1.740/anno** | | **Risparmio potenziale:** ~€ 720/anno | Se M365 Backup opzionale non viene attivato |

---

## Riepilogo risparmi potenziali

| Voce | Risparmio potenziale | Condizione |
|------|:-------------------:|-----------|
| Switch core L3 (×2) | € 2.400 | Se esistono già switch L3 gestiti |
| Switch accesso (×3) | € 1.200 | Se esistono già switch PoE+ sufficienti |
| Cablaggio cat.6A | € 6.000 | Se cablaggio esistente è adeguato (cat.6 o superiore) |
| Potenziamento InfiniBand | € 6.000 | Se fabbrica InfiniBand on-prem HDR funziona correttamente |
| M365 Backup | € 720/anno | Se retention nativa M365 è sufficiente per ISO 27001 |
| **Totale risparmio una tantum** | **~€ 15.600** | |
| **Totale risparmio ricorrente** | **~€ 720/anno** | |

### Scenario peggiore (tutto da comprare)

| Budget | Costo |
|-------|:-----:|
| Una tantum | € 86.000 |
| Ricorrente/anno | € 40.914 |
| **Anno 1** | **€ 126.914** |

### Scenario migliore (con risparmi)

| Budget | Costo |
|-------|:-----:|
| Una tantum | € 70.400 (-€ 15.600) |
| Ricorrente/anno | € 40.194 (-€ 720) |
| **Anno 1** | **€ 110.594** |

**Delta tra scenario peggiore e migliore:** ~€ 16.320 (3,1% del budget totale €520.000)

---

## Azioni da fare prima di ordinare

| Priorità | Azione | Chi | Entro | Impatto |
|:--------:|--------|-----|:-----:|---------|
| 🔴 | **Ispezione switch esistenti**: marca, modello, numero porte, PoE, L2/L3 | Sistemista in sede | Settimana -1 | Se compatibili → risparmio €3.600 |
| 🔴 | **Test InfiniBand on-prem**: bit error rate, temperatura switch, stato cavi | Sistemista in sede | Settimana -1 | Se OK → risparmio €6.000 |
| 🟡 | **Verifica cablaggio esistente**: categoria (cat.5e/6/6A), lunghezza tratte, stato connettori | Sistemista in sede | Settimana -1 | Se cat.6+ funzionante → risparmio €6.000 |
| 🟡 | **Analisi compatibilità Pondus**: codice C# .NET Framework vs .NET 8/10, dipendenze MS SQL | Sistemista + sviluppatore | Settimana 1 | Determina se il budget €10.000 per adattamento verrà speso o meno |
| 🟢 | **Verifica licenze M365 esistenti**: 30 Basic → confermare upgrade a Premium, data rinnovo | Sistemista | Settimana 0 | Impatto sulla finestra di attivazione |
| 🟢 | **Verifica scadenza licenze cluster HPC on-prem** | Sistemista | Settimana 0 | Se già rinnovate di recente → possibile risparmio €10.000 |

---

## Attività in sede vs da remoto

### 1. Da eseguire obbligatoriamente in sede

| # | Attività | Perché in sede | Fase | Durata |
|---|----------|---------------|------|--------|
| 0 | **Verifica infrastruttura esistente** (switch, cablaggio, InfiniBand) | Ispezione fisica: modello, marca, stato cavi | Pre-F0 | 1 gg |
| 1 | **Cablaggio strutturato cat.6A** (solo se assente) | Posa cavi, patch panel, canaline | Pre-F0 | 3-5 gg |
| 2 | **Dismissione FortiGate FG-60F** | Scollegamento fisico, rimozione rack | Pre-F0 | 1 h |
| 3 | **Montaggio rack e nuovi apparati** | FortiGate ×2, switch ×2-5, AP ×4, UPS ×2 | Pre-F0 | 1 gg |
| 4 | **Collegamento 2° ISP FTTH** | Presa fibra, modem | Pre-F0 | 1 gg |
| 5 | **Prima accensione FortiGate FG-100F HA** | Console seriale (irraggiungibile via rete) | F0 | 4 h |
| 6 | **Prima accensione switch L3** | Console, VLAN, stacking | F0 | 4 h |
| 7 | **Assegnazione VLAN su patch panel** | Collegamento fisico porte → VLAN | F0 | 2 h |
| 8 | **Potenziamento InfiniBand HPC** (solo se necessario) | Ricabling, verifica link fisici | F5b | 2 gg |
| 9 | **Montaggio AP WiFi 6** | Installazione a soffitto, PoE | F0 | 4 h |
| 10 | **Etichettatura fisica apparati** | Nomi host, patch panel | F0 | 2 h |
| 11 | **Verifica connettività post-cablaggio** | Test continuity, speed test | F0 | 1 gg |

### 2. Da eseguire da remoto

Accesso: VPN admin (dopo setup FortiGate) + Azure Portal + M365 Admin Center + SSH/RDP.

| # | Attività | Accesso | Fase | Durata |
|---|----------|---------|------|--------|
| 1 | Provisioning VNet, subnet, VPN Gateway | Azure Portal | F0 | 1 gg |
| 2 | Configurazione IPsec IKEv2 tunnel | Azure Portal + FortiGate GUI (via VPN) | F0 | 4 h |
| 3 | Creazione tenant M365 + Entra ID | M365 Admin Center | F0 | 1 gg |
| 4 | Entra Connect Sync (Samba4 → Entra ID) | RDP/SSH server on-prem via VPN | F0 | 2 gg |
| 5 | Utenti, licenze, MFA, Conditional Access | M365 Admin Center | F0 | 1 gg |
| 6 | Configurazione Exchange Online | M365 Admin Center | F1 | 1 gg |
| 7 | Migrazione Zimbra → Exchange (50 utenti) | IMAP sync tool | F1 | 5 gg |
| 8 | Migrazione GWS → Exchange (20 utenti) | Google Takeout / API | F1 | 5 gg |
| 9 | Creazione siti SharePoint | M365 Admin Center | F2 | 2 gg |
| 10 | Migrazione NextCloud + Drive → SharePoint | Migration Manager | F2 | 3 gg |
| 11 | Setup Dynamics 365 Sales + BC | Dynamics Admin Center | F3 | 2 gg |
| 12 | Migrazione CRM (Sugar → Dynamics) | API + import tool | F3 | 3 gg |
| 13 | Migrazione ERP (Profis → Dynamics BC) | Export/import tool | F3 | 5 gg |
| 14 | Migrazione timesheet (Kimai → Dynamics BC) | Export/import tool | F3 | 2 gg |
| 15 | Migrazione Odoo → Dynamics | API | F3 | 5 gg |
| 16 | Setup Azure DevOps + migrazione repo | Azure DevOps Portal | F4 | 2 gg |
| 17 | Migrazione MediaWiki → VM Azure | SSH + rsync via VPN | F5 | 2 gg |
| 18 | Deploy VM CycleCloud head node (D2s_v3) | Azure Portal | F5b | 1 gg |
| 19 | Configurazione CycleCloud + Slurm | SSH su head node via VPN | F5b | 2 gg |
| 20 | Provisioning Azure Managed Lustre (4 TB) | Azure Portal + CLI | F5b | 1 gg |
| 21 | Montaggio Lustre su nodi on-prem + Azure | SSH via VPN | F5b | 1 gg |
| 22 | Forwarder PBS → Slurm su front-end HPC | SSH front-end via VPN | F5b | 1 gg |
| 23 | Test burst: 2 nodi HBv4 SPOT + job MPI | SSH su CycleCloud | F5b | 1 gg |
| 24 | Azure Backup + Site Recovery | Azure Portal | F6 | 2 gg |
| 25 | Dismissione VM legacy (Zimbra, NextCloud, ecc.) | Console hypervisor via VPN | F7 | 4 h |
| 26 | Formazione utenti (3 sessioni × 2 h) | Microsoft Teams | F6 | 3 gg |
| 27 | Backup finale AD Samba4 + Profis | SSH/RDP via VPN | F7 | 1 gg |
| 28 | Report finale di migrazione | — | F7 | 2 gg |

### 3. Attività miste

| # | Attività | In sede | Da remoto | Fase |
|---|----------|---------|-----------|------|
| 1 | **Configurazione FortiGate FG-100F** | Accensione, console, IP MGMT, HA | Policy firewall, NAT, SD-WAN, VPN IPsec, BGP | F0 |
| 2 | **Setup VPN Site-to-Site** | Cavo WAN fisico (1° + 2° ISP) | IKEv2 tunnel, route, test latenza | F0 |
| 3 | **HPC — test InfiniBand** | Verifica link fisici su switch e nodi | Benchmark, MPI test, tuning | F5b |
| 4 | **Test di accettazione** | Postazioni LAN (VLAN 10), stampanti | Test cloud, utenti remoti, prestazioni | F6 |
| 5 | **Pondus su Azure** | Verifica codice C# su server fisico | Deploy Container Apps, migrazione DB | F6 |

---

## Cronologia logistica

```
Settimana:      -1      0       1       2       3       4       5       6       7       8       9       10
               │       │       │       │       │       │       │       │       │       │       │       │
VERIFICHE
  Ispezione    ██
  Decisione    ██

IN SEDE
  Cablaggio            ████████
  Apparati                      ████
  Downturn                     [██]    ← 4-6 h sostituzione FortiGate
  Accensione                    ████
  Etichettatura                 ██
  Verifica                      ██
  InfiniBand                                                    ████

DA REMOTO
  Azure foundation              ████████
  M365 setup                            ████████
  Migrazioni posta                              ██████████████
  Migrazioni file                                ██████████
  Dynamics                                                               ████████████████████
  DevOps                                                                    ██████████
  Media Wiki                                                                   ██████
  HPC burst setup                                                            ██████████
  Test                                                                                    ████████
  Dismissione                                                                                     ████
```

---

## Riepilogo risorse

| Tipo | Giorni/uomo | Profilo | Periodo |
|------|:-----------:|---------|---------|
| **Verifica preliminare** | 1 gg | Sistemista senior in sede | Settimana -1 |
| **In sede** | ~12-14 gg | 1-2 sistemisti (junior cablaggio, senior apparati) | Pre-F0 + F0 |
| **Misto** | ~5 gg | 1 sistemista senior | F0 + F5b |
| **Da remoto** | ~40-50 gg | 1 sistemista senior + consulente Dynamics part-time | Settimane 1-10 |
| **Extra** | ~12 gg | 1 PM part-time | Tutto |

### Note

1. **Prima di ordinare**: sistemista in sede 1 giorno a settimana -1 per ispezione switch, cablaggio, InfiniBand. Risultato determina ~€15.600 di possibili risparmi.
2. **Downturn rete**: 4-6 ore per sostituzione FG-60F → FG-100F HA. Pianificare serale/weekend.
3. **InfiniBand**: L'HDR 200 Gbps on-prem è sufficiente perché le due fabbriche (on-prem e Azure NDR) sono separate. Se i cavi esistenti sono in buono stato → risparmio €6.000.
4. **Dopo VPN attiva**: tutto il resto è gestibile da remoto.
5. **Cut-over F7**: VM legacy si spengono via IPMI/console, nessuna presenza fisica necessaria.
