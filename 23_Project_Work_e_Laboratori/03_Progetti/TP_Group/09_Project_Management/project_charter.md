# Project Charter — TP Group

## Identificazione progetto

| Campo | Valore |
| --- | --- |
| Nome progetto | Integrazione Infrastruttura IT TP Group |
| Acronimo | TP-IT-01 |
| Sponsor | Direzione TP Group |
| Project Manager | [Da nominare] |
| Data inizio | [Da definire] |
| Data fine prevista | 9-12 mesi dalla data inizio |

## Obiettivi

1. Convergere le infrastrutture IT di Thema Consulting (on premise) e Pro Studio (cloud) in un'unica architettura coerente
2. Ottenere la conformità ai requisiti ISO/IEC 27001 (business continuity, disaster recovery, sicurezza accessi)
3. Potenziare il cluster HPC da 8 a 16 nodi con interconnessione Infiniband 200 Gbps
4. Potenziare e ridistribuire l'applicazione Pondus con architettura HA
5. Garantire la continuità operativa durante e dopo la migrazione
6. **Garantire smart working strutturale**: minimo 10 dipendenti al giorno in remoto con connettività VPN stabile
7. **Rispettare finestra manutenzione**: massimo 7 giorni consecutivi di fermo, come richiesto dal cliente

## Scope

**Incluso:**
- Progettazione e implementazione rete/VPN
- Adeguamento sicurezza ISO 27001
- Potenziamento cluster HPC
- Migrazione Pondus a VM HA
- Integrazione cloud ibrido GCP/Workspace
- Backup e disaster recovery
- Documentazione e formazione

**Escluso:**
- Certificazione formale ISO 27001 (ente esterno)
- Sviluppo nuove funzionalità Pondus
- Fornitura laptop/postazioni utente
- Infrastruttura fisica edificio (UPS, condizionamento, rack)

## Milestone

| Milestone | Data prevista | Deliverable |
| --- | --- | --- |
| M1 — Assessment completato | Mese 1-2 | Documento AS-IS + GAP analysis |
| M2 — Rete e VPN operative | Mese 2-4 | Nuova rete + VPN funzionanti |
| M3 — Sicurezza implementata | Mese 3-6 | Politiche, cifratura, MFA attivi |
| M4 — HPC potenziato | Mese 4-8 | 8 nuovi nodi operativi |
| M5 — Pondus migrato e HA | Mese 6-9 | Pondus su VM con failover |
| M6 — Cloud integrato | Mese 5-9 | AD/Workspace SSO, backup off-site |
| M7 — Backup e DR pronti | Mese 6-9 | Recovery test superato |
| M8 — Offerta consegnata | Mese 8-12 | Documento finale + quotazione |
| M9 — Smart working operativo | Mese 2 | VPN per 10+ utenti remoti, test carico |
| M10 — Chiusura progetto | Mese 9-12 | Handover, documentazione, formazione |

## Budget

| Voce | Importo |
| --- | --- |
| Budget totale progetto | € 520.000 |
| (di cui risorse extra budget) | Da rendicontare separatamente |
| Costi sistemista (€500/gg) | Da stimare (~€40.000) |
| Costi PM (€650/gg) | Da stimare (~€19.500) |
| Costi HW rete, backup, sicurezza | Da quotazione |
| Costi ricorrenti (36 mesi) | Da stimare (~€63.000) |

## Team di progetto

| Ruolo | Figura | Impegno stimato |
| --- | --- | --- |
| Project Manager | [Da nominare] | 30 giorni |
| Sistemista senior | [Da nominare] | 80 giorni |
| Security specialist | [Da nominare] | 20 giorni |
| Sviluppatore .NET (Pondus) | [Da nominare] | 15 giorni |
| Referente IT Thema | [Da nominare] | Part-time |
| Referente IT Pro Studio | [Da nominare] | Part-time |

> **Nota:** La durata di 9-12 mesi è stata confermata dal cliente in sede di intervista (18/06/2026). Il cliente ha inoltre specificato che i costi delle risorse (€500/gg sistemista, €650/gg PM) sono extra budget e coprono il personale IT interno per i 3 anni successivi.
