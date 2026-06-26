# Project Work — Offerta Infrastruttura IT TP Group

## Panoramica

Progetto di offerta tecnico/economica per l'integrazione IT di **TP Group**,
nata dalla fusione di **Thema Consulting** (on-premise) e **Pro Studio** (cloud-native).

Il progetto sviluppa **3 varianti architetturali** complete e confrontabili per
presentare al cliente TP Group la soluzione più adatta alle proprie esigenze.

> **Nota:** La **Variante B (On-Premise)** è stata scartata in fase di valutazione.  
> Al suo posto è stata introdotta la **Variante D (Full Cloud Azure)** a seguito di un confronto
> approfondito tra provider cloud (GCP H4D vs Azure HBv4 vs AWS Hpc7a), con Azure risultato 1° classificato.

## Scenario

- **Thema Consulting**: 30 dipendenti, sede Torino, datacenter on-premise saturo,
  cluster HPC (8 nodi), servizi self-hosted (Zimbra, NextCloud, Samba4 AD, Pondus, ecc.)
- **Pro Studio**: 20 dipendenti, infrastruttura 100% cloud (Google Workspace, Odoo, BitBucket, GCP)
- **Obiettivo**: Convergenza IT, certificazione ISO/IEC 27001, potenziamento HPC (+8 nodi),
  potenziamento Pondus, smart working per 50 dipendenti
- **Budget**: 520.000 € + IVA (+ 181.000 € extra manodopera)
- **Tempistica**: 12 settimane attive, shutdown massimo 7 giorni, ciclo di vita 3 anni

## Struttura del Progetto

```
ProjectWork_Infrastruttura_IT/
├── README.md
├── Condivisi/
│   ├── 01_Assessment/           # Assessment AS-IS (Thema + Pro Studio + Gap Analysis)
│   └── 02_Project_Management/   # PM docs (Charter, WBS, Gantt, RASCI, Risk, Report)
├── A_Full_Cloud_GCP/            # Variante A — tutto su Google Cloud
│   ├── 03_Rete_VPN/
│   ├── 04_Cluster_HPC/
│   ├── 05_Pondus_App/
│   ├── 06_Cloud_Migration/
│   ├── 07_Backup_DR/
│   ├── 08_Sicurezza_ISO27001/
│   └── 09_Offerta/
├── C_Ibrido/                    # Variante C — architettura ibrida on-prem + cloud
│   └── ... stessa struttura ...
└── D_Full_Cloud_Azure/          # Variante D — tutto su Microsoft Azure (✔ consigliata)
    ├── 03_Rete_VPN/
    ├── 04_Cluster_HPC/
    ├── 05_Pondus_App/
    ├── 06_Cloud_Migration/
    ├── 07_Backup_DR/
    ├── 08_Sicurezza_ISO27001/
    └── 09_Offerta/
```

## Varianti Architetturali

| Variante | Descrizione | Budget 3 anni |
|----------|-------------|---------------|
| **A — Full Cloud GCP** | Tutta l'infrastruttura su Google Cloud | ~€454.284 |
| **C — Ibrido** | On-premise (HPC esistente) + Cloud (servizi, DR) | ~€535.216 |
| **D — Full Cloud Azure** ⭐ | Tutta l'infrastruttura su Microsoft Azure (HBv4 InfiniBand) | **~€489.756** |

> ⭐ **Variante D consigliata**: InfiniBand NDR 400 Gbps nativo, DR enterprise-grade (Failover Group automatico), SQL Business Critical, Redis Cache, M365 già presente (€0 migrazione posta). Budget residuo ~€211k.

## Come Navigare

1. **Assessment**: Inizia da `Condivisi/01_Assessment/` per capire lo stato attuale
2. **PM Docs**: `Condivisi/02_Project_Management/` per piano, tempi, costi e rischi
3. **Varianti**: Scegli una variante (A, C, o D) e naviga i documenti tecnici per area
4. **Offerta**: `09_Offerta/offerta_tecnico_economica.md` per il documento finale completo
5. **Confronto**: `Condivisi/02_Project_Management/matrice_confronto.md` per confronto diretto

## Formato dei Documenti

Tutti i documenti sono in **Markdown (.md)** e seguono lo schema:
**REQUISITI** → **SOLUZIONE** → **DIMENSIONAMENTO** → **COSTI**

## Note

- Progetto sviluppato interamente da zero (non basato su file TP_Group/ preesistenti)
- Le domande "da chiedere al cliente" (HPC definitivo, connettività sede, retention dati)
  sono lasciate come assunzioni da validare
- Documentazione in italiano, terminologia tecnica in inglese per protocolli/tecnologie
