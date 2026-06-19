# Gantt di Progetto — TP Group

## Cronoprogramma (12 mesi: lug 2026 → giu-lug 2027)

```mermaid
gantt
    title Gantt TP Group — Integrazione IT (12 mesi)
    dateFormat  YYYY-MM-DD
    axisFormat  %b %Y

    section Assessment & Planning
    Assessment & Gap analysis            :a1, 2026-07-01, 30d
    Definizione architettura TO-BE       :a2, after a1, 20d

    section Rete & VPN
    Progettazione rete                   :r1, after a1, 20d
    Acquisto HW rete                     :r2, after r1, 15d
    Installazione e cablaggio           :r3, after r2, 20d
    Configurazione Fortigate + VPN       :r4, after r3, 15d
    Test smart working (10+ utenti VPN)  :r5, after r4, 10d

    section Sicurezza ISO 27001
    Gap analysis ISO                     :s1, after a1, 20d
    Politiche e procedure                :s2, after s1, 20d
    Implementazione cifratura e MFA      :s3, after s2, 30d
    Audit interno                        :s4, after s3, 15d

    section Cluster HPC
    Dimensionamento e ordine HW          :h1, after a1, 30d
    Installazione hosting co-location    :h2, after h1, 30d
    Configurazione Infiniband + Slurm    :h3, after h2, 30d
    Benchmark e validazione              :h4, after h3, 15d

    section Pondus
    Preparazione VM e licenze            :p1, after s2, 20d
    Migrazione DB e app                  :p2, after p1, 20d
    Configurazione HA e Go-Live Online   :p3, after p2, 15d
    Dismissione server fisico            :p4, after p3, 10d

    section Cloud Migration
    VPN GCP + GCDS                       :c1, after r4, 15d
    Migrazione Workspace → MS365/Zimbra  :c2, after c1, 30d
    Migrazione Drive → NextCloud         :c3, after c1, 20d
    Migrazione CRM/TS → Odoo             :c4, after c1, 25d
    Dismissione Google Workspace         :c5, after c2, 15d

    section Backup & DR
    Acquisto e config NAS                :b1, after h1, 15d
    Configurazione backup 3-2-1          :b2, after b1 + s3, 20d
    Test DR e procedure                  :b3, after b2 + c3, 15d

    section Offerta & Documentazione
    Raccolta contributi                  :o1, after a2, 200d
    Redazione offerta finale             :o2, after b3, 15d
    Consegna documentazione              :o3, after o2, 10d

    section Project Management
    Pianificazione                       :m1, 2026-07-01, 20d
    Coordinamento e monitoraggio         :m2, after m1, 280d
    Chiusura e handover                  :m3, after o3 + b3, 15d
```

## Tabella attività

| # | Attività | Inizio | Fine | Durata | Dipendenza |
| --- | --- | --- | --- | --- | --- |
| 1 | Censimento asset | 12/06 | 15/06 | 4g | — |
| 2 | Gap analysis | 16/06 | 18/06 | 3g | #1 |
| 3 | Progettazione rete | 19/06 | 22/06 | 4g | #2 |
| 4 | Gap analysis ISO 27001 | 19/06 | 22/06 | 4g | #2 |
| 5 | Dimensionamento HPC | 19/06 | 21/06 | 3g | #2 |
| 6 | Acquisto HW rete | 23/06 | 24/06 | 2g | #3 |
| 7 | Politiche sicurezza | 23/06 | 25/06 | 3g | #4 |
| 8 | Acquisto HW HPC | 22/06 | 27/06 | 6g | #5 |
| 9 | Acquisto NAS backup | 25/06 | 26/06 | 2g | #6 |
| 10 | Installazione e cablaggio rete | 25/06 | 29/06 | 5g | #6 |
| 11 | Implementazione misure sicurezza | 26/06 | 01/07 | 6g | #7 |
| 12 | Installazione hosting HPC | 28/06 | 02/07 | 5g | #8 |
| 13 | Configurazione + test rete | 30/06 | 02/07 | 3g | #10 |
| 14 | Preparazione VM Pondus | 29/06 | 02/07 | 4g | #7 |
| 15 | Configurazione backup | 02/07 | 06/07 | 5g | #9 + #11 |
| 16 | Audit sicurezza | 02/07 | 04/07 | 3g | #11 |
| 17 | Migrazione DB e app Pondus | 03/07 | 06/07 | 4g | #14 |
| 18 | Configurazione HPC | 03/07 | 09/07 | 7g | #12 |
| 19 | VPN GCP + GCDS | 03/07 | 05/07 | 3g | #13 |
| 20 | Configurazione HA Pondus | 07/07 | 08/07 | 2g | #17 |
| 21 | Test e dismissione Pondus | 09/07 | 11/07 | 3g | #20 |
| 22 | Migrazione servizi cloud | 06/07 | 11/07 | 6g | #19 |
| 23 | Benchmark HPC | 10/07 | 11/07 | 2g | #18 |
| 24 | Integrazione cloud finale | 12/07 | 14/07 | 3g | #22 |
| 25 | Procedure DR e test | 12/07 | 15/07 | 4g | #15 + #22 |
| 26 | Raccolta contributi offerta | 19/06 | 19/07 | parallela | #2 |
| 27 | Redazione offerta | 16/07 | 20/07 | 5g | #25 |
| 28 | Consegna | 21/07 | 22/07 | 2g | #27 |
| 29 | Chiusura progetto | 22/07 | 22/07 | 1g | #28 |

**Milestone:** Consegna finale — **Giugno-Luglio 2027** (9-12 mesi dall'avvio)

> **NOTA:** Timeline aggiornata in base all'intervista cliente (durata 9-12 mesi, finestra manutenzione max 7gg, smart working strutturale).
