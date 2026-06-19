# Cronoprogramma TP Group — Gantt di Progetto

> **Progetto:** Integrazione infrastrutturale TP Group (Thema Consulting + Pro Studio)
> **Durata:** 12 settimane attive (84 giorni)
> **Data inizio:** 05/01/2026
> **Data fine supporto:** 12/04/2026

---

## Diagramma Gantt (Mermaid)

```mermaid
gantt
    title Cronoprogramma TP Group — Integrazione Infrastrutturale
    dateFormat  YYYY-MM-DD
    axisFormat  %d/%m

    section Assessment
        Assessment stato attuale            :a1, 2026-01-05, 14d

    section Progettazione
        Progettazione architettura          :a2, 2026-01-12, 28d

    section Approvvigionamento
        Ordine e attesa HW                  :a3, 2026-01-19, 42d

    section Infrastruttura
        Configurazione Infrastruttura       :a4, 2026-02-02, 28d

    section Migrazione
        Migrazione Dati e Servizi           :a5, 2026-03-02, 14d

    section Test
        Test e Collaudo                     :a6, 2026-03-09, 14d

    section Shutdown
        Shutdown e Cut-Over (max 7gg)       :a7, 2026-03-16, 7d

    section Formazione
        Formazione personale                :a8, 2026-03-16, 7d

    section Go-Live
        Go-Live                             :a9, 2026-03-23, 1d
        Supporto Post-Go-Live               :a10, 2026-03-23, 21d

    section Milestone
        M1 - Fine Assessment                :milestone, m1, 2026-01-18, 0d
        M2 - Fine Progettazione             :milestone, m2, 2026-02-08, 0d
        M3 - Ordine HW Effettuato           :milestone, m3, 2026-02-01, 0d
        M4 - Consegna HW                    :milestone, m4, 2026-03-01, 0d
        M5 - Inizio Migrazione              :milestone, m5, 2026-03-02, 0d
        M6 - Shutdown Completato            :milestone, m6, 2026-03-22, 0d
        M7 - Go-Live                        :milestone, m7, 2026-03-23, 0d
        M8 - Avvio Supporto Post-Go-Live    :milestone, m8, 2026-03-23, 0d
```

---

## Tabella Riepilogativa

| Attività | Inizio | Fine | Durata | Dipendenze |
|---|---|---|---|---|
| Assessment stato attuale | 05/01/2026 | 18/01/2026 | 14 gg | — |
| Progettazione architettura | 12/01/2026 | 08/02/2026 | 28 gg | Assessment |
| Ordine e attesa HW | 19/01/2026 | 01/03/2026 | 42 gg | Progettazione (parziale) |
| Configurazione Infrastruttura | 02/02/2026 | 01/03/2026 | 28 gg | Progettazione |
| Migrazione Dati e Servizi | 02/03/2026 | 15/03/2026 | 14 gg | Configurazione Infrastruttura, Consegna HW |
| Test e Collaudo | 09/03/2026 | 22/03/2026 | 14 gg | Migrazione Dati (parziale) |
| Shutdown e Cut-Over (max 7gg) | 16/03/2026 | 22/03/2026 | 7 gg | Test e Collaudo |
| Formazione personale | 16/03/2026 | 22/03/2026 | 7 gg | Configurazione Infrastruttura |
| Go-Live | 23/03/2026 | 23/03/2026 | 1 gg | Shutdown, Test e Collaudo |
| Supporto Post-Go-Live | 23/03/2026 | 12/04/2026 | 21 gg | Go-Live |

---

## Milestone

| ID | Descrizione | Settimana | Data |
|---|---|---|---|
| M1 | Fine Assessment | Settimana 2 | 18/01/2026 |
| M2 | Fine Progettazione | Settimana 5 | 08/02/2026 |
| M3 | Ordine HW Effettuato | Settimana 4 | 01/02/2026 |
| M4 | Consegna HW | Settimana 8 | 01/03/2026 |
| M5 | Inizio Migrazione | Settimana 9 | 02/03/2026 |
| M6 | Shutdown Completato (max 7gg) | Settimana 11 | 22/03/2026 |
| M7 | Go-Live | Settimana 12 | 23/03/2026 |
| M8 | Avvio Supporto Post-Go-Live | Settimane 12-14 | 23/03/2026 |

---

## Note

- **Il Gantt è indicativo e sarà dettagliato in fase di progettazione esecutiva.**
- Le attività di **Approvvigionamento HW** (Ordine e attesa HW) si svolgono in parallelo rispetto alla progettazione e configurazione, considerando lead time di 8-16 settimane per la consegna dei componenti hardware (server, storage, rete Infiniband).
- La finestra di **Shutdown** è vincolata a un massimo di **7 giorni consecutivi**, come da policy di business continuity e requisiti del capitolato.
- Le attività di **Test e Collaudo** iniziano in parziale sovrapposizione con la **Migrazione Dati e Servizi**, consentendo test incrementali sui primi moduli migrati.
- La **Formazione** del personale è schedulata in parallelo allo Shutdown per ottimizzare i tempi e non richiede indisponibilità dei sistemi.
- Il **Supporto Post-Go-Live** si estende per 3 settimane oltre il Go-Live per garantire stabilità e presidio in fase di avvio.
- Le dipendenze indicate sono da intendersi come logiche (FS — Fine-Inizio) salvo diversa indicazione.
