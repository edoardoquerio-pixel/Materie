# Piano Economico e Pagamenti

> **Documento:** Revisione costi, trasferte, margini e piano di pagamento per Full Cloud Azure TP Group  
> **Data:** Luglio 2026  
> **IVA:** Esclusa (tutti i prezzi)

---

## 1. Revisione costi di progetto

I costi sono suddivisi in quattro macrocategorie:

- **A — Forniture HW/SW/cloud** (costo d'acquisto, pass-through al cliente)
- **B — Manodopera** (tariffa giornaliera fatturata al cliente — già include margine azienda)
- **C — Trasferta** (maggiorazione per giorni in sede)
- **D — Margine azienda** (ricarico su forniture e gestione)

---

### A — Forniture HW/SW/cloud (costo d'acquisto)

| Area | Voce | Una tantum | Ric./anno |
|------|------|:----------:|:---------:|
| **Rete** | FortiGate FG-100F HA cluster (×2, FortiCare 3 anni) | € 7.000 | — |
| | Switch Core L3 48p PoE+ (×2) | € 2.400 | — |
| | Switch accesso 24p PoE+ (×3) | € 1.200 | — |
| | AP WiFi 6 triband (×4) | € 1.000 | — |
| | UPS rack 1500 VA (×2) | € 1.200 | — |
| | Cablaggio strutturato cat.6A | € 6.000 | — |
| | Accessori (SFP+ ×20, PDU rack, passacavi, console) | € 1.200 | — |
| | Smaltimento RAEE apparati obsoleti | € 300 | — |
| | 2° ISP FTTH 1 Gbps | — | € 4.200 |
| | *Subtotale Rete* | *€ 19.300* | *€ 4.200* |
| **Sicurezza** | Licenze/configurazione ISO 27001 | € 8.000 | — |
| | Audit iniziale sicurezza | € 3.500 | — |
| | *Subtotale Sicurezza* | *€ 11.500* | *€ 0* |
| **HPC** | Rinnovo licenze cluster on-prem (3 anni) | € 10.000 | — |
| | Potenziamento InfiniBand (cavi, switch) | € 6.000 | — |
| | Azure HB176-96rs v4 SPOT (8 nodi × 200gg × 8h) | — | € 19.341 |
| | CycleCloud head node D2s_v3 (24/7 PAYG) | — | € 918 |
| | Azure Managed Lustre 4 TB | — | € 960 |
| | *Subtotale HPC* | *€ 16.000* | *€ 21.219* |
| **Pondus** | Analisi compatibilità codice | € 2.000 | — |
| | Adattamento codice (se necessario, media stimata) | € 10.000 | — |
| | Setup Azure App + SQL | € 1.500 | — |
| | Test e validazione | € 2.000 | — |
| | Azure App Service P1v3 | — | € 1.362 |
| | Azure SQL DB S2 | — | € 772 |
| | *Subtotale Pondus* | *€ 15.500* | *€ 2.134* |
| **Migration** | Migrazione posta (Zimbra + GWS → Exchange) | € 1.500 | — |
| | Migrazione file (NextCloud + Drive → SharePoint) | € 2.500 | — |
| | Setup Entra ID + MFA | € 1.500 | — |
| | Setup Azure DevOps | € 1.000 | — |
| | Migrazione MediaWiki | € 500 | — |
| | M365 Business Premium (50 utenti) | — | € 12.360 |
| | Dynamics 365 Sales Pro (20 utenti) | — | € 13.512 |
| | Dynamics 365 BC Essentials (10 utenti) | — | € 8.316 |
| | Azure DevOps (45 utenti) | — | € 2.835 |
| | VM B2s MediaWiki | — | € 367 |
| | Azure VPN Gateway VpnGw1AZ | — | € 1.170 |
| | *Subtotale Migration* | *€ 7.000* | *€ 38.560* |
| **Backup/DR** | Configurazione Azure Backup | € 3.500 | — |
| | Configurazione Azure Site Recovery | € 2.000 | — |
| | Test DR | € 1.700 | — |
| | Azure Backup (VM + SQL + files) | — | € 480 |
| | Blob Storage RA-GRS (HPC, AD) | — | € 180 |
| | M365 Backup (opzionale) | — | € 720 |
| | Azure Site Recovery | — | € 360 |
| | *Subtotale Backup/DR* | *€ 7.200* | *€ 1.740* |
| **Formazione** | Formazione utenti base (M365, Dynamics, Teams, amministratori) | € 3.000 | — |
| | Formazione nuova infrastruttura TP_Group (7 moduli: rete, Azure, DevOps, HPC, backup, sicurezza) | € 4.000 | — |
| | Documentazione progetto | € 2.000 | — |
| | *Subtotale Formazione* | *€ 9.000* | *€ 0* |
| | **Totale A — Forniture (costo acquisto)** | **€ 85.500** | **€ 67.853** |

> **Nota:** La voce "Configurazione Dynamics 365" (€ 5.000) è stata spostata in B — Manodopera perché è il forfait del consulente Dynamics. Questo evita la duplicazione.

---

### B — Manodopera (tariffa fatturata al cliente)

Le tariffe giornaliere sono **prezzi di vendita** — includono già il margine dell'azienda (salario + contributi + spese generali + profitto).

| Ruolo | Giorni | Tariffa/gg | Subtotale | Di cui in sede | Di cui da remoto |
|-------|:-----:|:----------:|:---------:|:--------------:|:----------------:|
| Sistemista senior | 55 gg | € 500 | € 27.500 | 15 gg (€ 7.500) | 40 gg (€ 20.000) |
| Project Manager | 17 gg | € 650 | € 11.050 | 0 gg | 17 gg (€ 11.050) |
| Consulente Dynamics | 10 gg | € 600 | € 6.000 | 0 gg | 10 gg (€ 6.000) |
| **Totale B** | | | **€ 44.550** | **€ 7.500** | **€ 37.050** |

**Costo del lavoro per l'azienda** (stima):
| Ruolo | Costo gg (salario + contributi + spese) | Tariffa gg | Margine/gg |
|-------|:--------------------------------------:|:----------:|:----------:|
| Sistemista senior | ~€ 280 | € 500 | **€ 220 (44%)** |
| Project Manager | ~€ 350 | € 650 | **€ 300 (46%)** |
| Consulente Dynamics | ~€ 320 | € 600 | **€ 280 (47%)** |

---

### C — Trasferta

Maggiorazione del **25% sulla tariffa giornaliera** per i giorni in sede, a copertura di indennità pasto, viaggio e disagio.

| Voce | Calcolo | Importo |
|------|---------|:------:|
| Sistemista in sede (15 gg × €500 × 25%) | € 7.500 × 25% | **€ 1.875** |
| Attrezzatura trasferta (crimpatore, etichettatrice, continuity tester) | Una tantum | **€ 300** |
| **Totale C** | | **€ 2.175** |

*Se il sistemista non risiede a Torino, aggiungere € 120/notte × 15 notti = € 1.800 (da verificare).*

---

### D — Margine azienda su forniture

L'azienda esecutrice applica un **ricarico del 15%** sull'acquisto delle forniture HW/SW a copertura di: procurement, gestione fornitori, garanzia sui materiali, coordinamento logistico.

| Voce | Costo acquisto | Ricarico 15% | Prezzo vendita al cliente | Margine |
|------|:-------------:|:------------:|:-------------------------:|:------:|
| Forniture rete | € 19.300 | € 2.895 | € 22.195 | € 2.895 |
| Sicurezza (licenze + audit) | € 11.500 | € 1.725 | € 13.225 | € 1.725 |
| HPC on-prem (licenze + InfiniBand) | € 16.000 | € 2.400 | € 18.400 | € 2.400 |
| Pondus setup (analisi, setup, test) | € 5.500 | € 825 | € 6.325 | € 825 |
| Migration (forfait attività) | € 7.000 | € 1.050 | € 8.050 | € 1.050 |
| Backup/DR setup | € 7.200 | € 1.080 | € 8.280 | € 1.080 |
| Formazione (Fase 1 + Fase 2 TP_Group) | € 9.000 | € 1.350 | € 10.350 | € 1.350 |
| Adattamento codice Pondus (*se necessario*) | € 10.000 | € 1.500 | € 11.500 | € 1.500 |
| **Totale D** | **€ 75.500** | **€ 11.325** | **€ 86.825** | **€ 11.325** |

*Cloud ricorrenti (M365, Dynamics, Azure): pass-through senza margine, fatturati al costo.*

---

## 2. Conto economico di progetto

### Costi azienda (quanto spende l'esecutore)

| Voce | Anno 1 |
|------|:------:|
| A — Forniture (costo acquisto) | € 81.500 |
| B1 — Costo del lavoro sistemista (55 gg × € 280) | € 15.400 |
| B2 — Costo del lavoro PM (17 gg × € 350) | € 5.950 |
| B3 — Costo del lavoro consulente Dynamics (10 gg × € 320) | € 3.200 |
| C — Trasferta sistemista | € 2.175 |
| **Costi totali azienda** | **€ 112.225** |

### Ricavi azienda (quanto incassa dal cliente)

| Voce | Anno 1 |
|------|:------:|
| D — Forniture (prezzo vendita con ricarico 15%) | € 86.825 |
| B — Manodopera (tariffa fatturata) | € 44.550 |
| C — Trasferta fatturata | € 2.175 |
| **Ricavi totali anno 1** | **€ 133.550** |

### Margine

| Voce | Importo | % su ricavi |
|------|:------:|:-----------:|
| **Ricavi anno 1** | **€ 133.550** | 100% |
| **Costi anno 1** | **€ 112.225** | 84,0% |
| **Margine lordo anno 1** | **€ 21.325** | **16,0%** |
| Cloud ricorrenti (pass-through, senza margine) | € 67.853 | — |

**Scomposizione del margine € 21.325:**

| Componente | Importo |
|------------|:------:|
| Ricarico 15% su forniture (D) | € 11.325 |
| Margine su manodopera (sistemista 55gg × €220 + PM 17gg × €300 + cons. 10gg × €280) | € 20.100 |
| Costo trasferta (pari al fatturato, margine zero) | € 0 |
| **Margine complessivo** | **~€ 31.425** |

*Il margine complessivo è superiore al margine lordo perché una parte dei costi del lavoro (B1) è già nei costi azienda. Il calcolo corretto: Ricavi totali (€133.550) - Costi totali azienda (€112.225) = €21.325.*

---

## 3. Budget cliente e flussi

| Voce | Anno 1 | Anno 2 | Anno 3 |
|------|:------:|:------:|:------:|
| **Uscite cliente** | | | |
| A — Forniture HW/SW (prezzo vendita) | € 86.825 | € 0 | € 0 |
| B — Manodopera | € 44.550 | € 0 | € 0 |
| C — Trasferta | € 2.175 | € 0 | € 0 |
| Cloud ricorrenti (pass-through) | € 67.853 | € 67.853 | € 67.853 |
| **Totale uscite cliente** | **€ 201.403** | **€ 67.853** | **€ 67.853** |
| | | | |
| Budget totale progetto | € 520.000 | | |
| **Cumulato 3 anni** | | | **€ 337.109** |
| **Margine residuo su budget** | | | **~€ 182.891 (35,2%)** |

---

## 4. Piano di pagamento

Il piano regola i pagamenti che il cliente (**TP Group**) versa all'azienda esecutrice.

### 4.1 Importo soggetto a pagamento

| Componente | Importo |
|------------|:------:|
| A — Forniture HW/SW (prezzo vendita) | € 86.825 |
| B — Manodopera | € 44.550 |
| C — Trasferta | € 2.175 |
| **Totale** | **€ 133.550** |
| Cloud ricorrenti | € 67.853/anno (pass-through, pagamento diretto o rimborso) |

### 4.2 Milestone

| # | Milestone | Condizione | Importo | % |
|:-:|-----------|-----------|:------:|:-:|
| M0 | **Acconto avvio progetto** | Firma contratto + ordine apparati di rete (FortiGate, switch, UPS, AP, cablaggio) | **€ 25.000** | 19,4% |
| M1 | **Foundation completata** | VNet, VPN site-to-site attiva, FortiGate HA operativo, Entra ID configurato, tenant M365 pronto | **€ 20.000** | 15,5% |
| M2 | **Infrastruttura on-prem pronta** | Cablaggio completato, apparati montati, VLAN funzionanti, WiFi attivo, 2° ISP collegato | **€ 20.000** | 15,5% |
| M3 | **Posta + File migrati** | 50 caselle su Exchange Online, MX puntato, SharePoint/OneDrive popolati, NextCloud in lettura | **€ 14.000** | 10,9% |
| M4 | **Dynamics 365 attivo** | Sales + BC funzionanti, dati CRM/ERP/timesheet migrati, test pilota superati | **€ 17.000** | 13,2% |
| M5 | **DevOps + MediaWiki + HPC burst** | Repos migrati, MediaWiki su Azure, CycleCloud attivo, Lustre montato, test burst 2 nodi HBv4 OK | **€ 17.000** | 13,2% |
| M6 | **Test e accettazione** | Test di accettazione superati, formazione utenti Fase 1 + Fase 2 completata, documentazione consegnata | **€ 14.600** | 10,9% |
| M7 | **Saldo finale** | Dismissione VM legacy completata, report finale consegnato, collaudo firmato | **€ 5.950** | 4,5% |
| | **Totale** | | **€ 133.550** | **100%** |

### 4.3 Cloud ricorrenti

I servizi cloud decorrono dall'attivazione e sono **pass-through** al costo:

| Servizio | Decorrenza | Canone/mese |
|----------|-----------|:-----------:|
| M365 Business Premium (50 utenti) | Dal M1 | € 1.030 |
| Dynamics 365 Sales Pro (20 utenti) | Dal M4 | € 1.126 |
| Dynamics 365 BC Essentials (10 utenti) | Dal M4 | € 693 |
| Azure servizi (App Service, SQL, VPN, VM, backup, HPC, Lustre) | Dal M1 | ~€ 2.095 |
| **Totale cloud/mese** | | **~€ 4.944** |

**Opzioni:**
- **A)** Il cliente attiva direttamente le subscription → nessun passaggio sull'esecutore
- **B)** L'esecutore rivende → applicare margine 5-10% (da concordare)

### 4.4 Condizioni

| Parametro | Valore |
|-----------|--------|
| Fatturazione | A stato di avanzamento (SAL) |
| Termini pagamento | 30 gg FM dalla data fattura |
| Ritenuta di garanzia | 5% trattenuto fino a collaudo finale (M7) |
| Penale ritardo | 0,5% per settimana su milestone non imputabile a cause maggiori, max 10% |
| Extra perimetro | Variazioni >10% → ordine di variazione separato |
| Foro competente | Torino |

### 4.5 Cash flow azienda esecutrice

| Mese | Evento | Entrata | Uscita prevista | Saldo |
|:----:|--------|:------:|:---------------:|:----:|
| 0 | Firma contratto | € 0 | € 0 | € 0 |
| 0 | Anticipo M0 | € 25.000 | — | +€ 25.000 |
| 0 | Ordine forniture | — | ~€ 19.300 (rete + accessori) | +€ 5.700 |
| 1-2 | SAL M1 + M2 | € 40.000 | — | +€ 45.700 |
| 1-2 | Ordine HPC + sicurezza + backup | — | ~€ 34.700 | +€ 11.000 |
| 3-4 | SAL M3 + M4 | € 31.000 | — | +€ 42.000 |
| 5-6 | SAL M5 + M6 | € 31.600 | € 0 (forniture già acquistate) | +€ 73.600 |
| 7-8 | SAL M7 | € 5.950 | — | +€ 79.550 |
| 7-10 | Pagamento stipendi/collaborazioni | — | ~€ 24.550 (costo lavoro) | +€ 55.000 |
| 7-10 | Spese trasferta | — | ~€ 2.175 | +€ 52.825 |

**Saldo finale anno 1:** **+€ 52.825** su € 133.550 fatturati. Il resto del margine è già stato assorbito nei costi generali aziendali (affitto, utenze, assicurazioni, formazione interna, ecc.).

---

## 5. Riepilogo potenziali risparmi (da verificare in sede)

| Voce | Risparmio max | Condizione |
|------|:------------:|------------|
| Switch core L3 48p (×2) + accesso 24p (×3) | € 3.600 | Se switch esistenti sufficienti |
| Cablaggio cat.6A | € 6.000 | Se cablaggio esistente adeguato |
| Potenziamento InfiniBand | € 6.000 | Se fabbrica HDR on-prem funzionante |
| **Risparmio max** | **€ 15.600** | |
| **Costo progetto scenario risparmio** (anno 1) | **€ 113.350** | |
| **Margine scenario risparmio** | **~€ 36.325 (28,2%)** | |

**Azione:** Sopralluogo tecnico in sede settimana -1. Ordini dopo verifica.
