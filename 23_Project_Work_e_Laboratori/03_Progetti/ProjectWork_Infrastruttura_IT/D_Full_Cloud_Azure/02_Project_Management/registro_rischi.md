# Registro Rischi — TP Group Infrastructure Integration

| # | Rischio | Categoria | Probabilità | Impatto | Punteggio | Mitigazione | Contingenza | Owner |
|---|---|---|---|---|---|---|---|---|
| R1 | **Datacenter saturo**: impossibile espandere on-prem senza co-location | Infrastruttura | Alta (4) | Alto (4) | **16** | Preventivo co-location in fase di assessment; pianificare espansione con armadio esterno | Co-location già budgettata in varianti B/C | PM |
| R2 | **Condizionamento al limite**: rischio surriscaldamento con espansione HPC | Infrastruttura | Alta (4) | Alto (4) | **16** | InRow DX dedicato o co-location per nodi aggiuntivi | Riduzione carico HPC o spostamento in co-location | System Admin |
| R3 | **Downtime migrazione > 7gg**: cut-over non completato nella finestra consentita | Migrazione | Media (3) | Molto Alto (5) | **15** | Pianificazione dettagliata, rollback plan, test pre-cut-over | Estensione finestra con approvazione cliente, rollback a stato pre-migrazione | PM |
| R4 | **Incompatibilità applicazioni legacy con cloud** (Profis, Kimai, SugarCRM) | Tecnologico | Alta (4) | Alto (4) | **16** | Assessment preliminare compatibilità, alternativa Odoo SaaS già prevista | Mantenimento temporeaneo VM on-prem per app non migrabili | System Admin |
| R5 | **Perdita dati durante migrazione** | Dati | Bassa (2) | Molto Alto (5) | **10** | Backup completo pre-migrazione, CDC per DB, verifica checksum | Restore da backup, comunicazione cliente | System Admin |
| R6 | **Tempi consegna HW > 16 settimane**: lead time HPC e rete | Fornitura | Media (3) | Alto (4) | **12** | Ordine anticipato (1° mese), valutazione fornitori alternativi | Noleggio temporaneo o cloud burst in attesa | Procurement |
| R7 | **Resistenza utenti al cambiamento** (Zimbra→Workspace, Profis→Odoo) | Organizzativo | Alta (4) | Medio (3) | **12** | Formazione anticipata, periodo coesistenza, ambasciatori interni | Supporto dedicato prime 2 settimane post-migrazione | PM |
| R8 | **MFA deployment bloccato da utenti** | Organizzativo | Media (3) | Medio (3) | **9** | Comunicazione obbligatorietà da direzione, roll-out graduale | Esclusioni temporanee con approvazione Security Officer | Security Officer |
| R9 | **Vincoli edificio storico**: impossibilità modifiche strutturali | Infrastruttura | Alta (4) | Alto (4) | **16** | Co-location o cloud per espansione (già previsto in varianti) | Ridimensionamento progetto on-prem | PM |
| R10 | **Budget insufficiente per variante scelta** | Economico | Bassa (2) | Alto (4) | **8** | Preventivazione accurata, varianti con fasce di costo alternative | Riduzione ambito (es. HPC posticipato) | PM |
| R11 | **Attacco ransomware o breach durante transizione** | Sicurezza | Media (3) | Molto Alto (5) | **15** | Antimalware, backup isolati, MFA obbligatorio prima della migrazione | Isolamento immediato, restore da backup isolato, incident response | Security Officer |
| R12 | **Vendor lock-in GCP** (varianti A/C) | Strategico | Bassa (2) | Alto (4) | **8** | Architettura containerizzata (Pondus su Cloud Run), DB SQL standard | Migrazione a provider alternativo con minimo refactoring | Architect |

## Matrice dei rischi

```
Impatto
  5 │ R3  R5                R11
  4 │      R1 R2 R4 R9     R6 R10 R12
  3 │      R7
  2 │
  1 │
    └────────────────────────── Probabilità
       1   2   3   4    5

  Rosso  (15-25): Azione immediata
  Giallo (8-14): Monitorare
  Verde  (1-7):  Accettare
```

## Top 5 rischi critici (priorità)

1. **R1 — Datacenter saturo** (16): impatta tutte le varianti
2. **R2 — Condizionamento** (16): blocca espansione HPC on-prem
3. **R4 — Incompatibilità legacy** (16): rischio migrazione
4. **R9 — Vincoli edificio** (16): limitazione strutturale
5. **R3 — Downtime > 7gg** (15): finestra migrazione critica
