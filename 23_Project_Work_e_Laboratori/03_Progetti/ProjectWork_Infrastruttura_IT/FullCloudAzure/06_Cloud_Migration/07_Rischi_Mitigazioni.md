# 07 — Rischi e Mitigazioni

> **Documento:** Analisi rischi per la migrazione Full Cloud Azure TP Group  
> **Data:** Luglio 2026

---

## Matrice dei rischi

| # | Rischio | Probabilità | Impatto | Priorità | Mitigazione |
| --- | --- | --- | --- | --- | --- |
| R01 | Downtime posta durante migrazione caselle | Media | Alto | **Alta** | Migrazione graduale per utente (5-10/giorno). Mantenere Zimbra attivo in lettura per 7 giorni. MX puntato a Zimbra fino a verifica completa. |
| R02 | Perdita dati file (permessi, metadati, versioni) | Media | Alto | **Alta** | Backup completo pre-migrazione. Migration Manager Microsoft con verifica checksum. Test su utenti pilota prima della migrazione di massa. |
| R03 | Complessità migrazione dati contabili (Profis → BC) | Alta | Alto | **Critica** | Consulente Dynamics 365 dedicato. Affiancamento Profis + BC per 2 settimane. Profis mantenuto in cold storage 30 giorni. |
| R04 | Resistenza utenti al cambio strumenti | Media | Medio | **Media** | Formazione dedicata per ogni fase (posta, file, Dynamics). Pilot con 5 utenti chiave prima del roll-out completo. Documentazione utente chiara. |
| R05 | Sincronizzazione AD Samba4 → Entra ID non completa | Bassa | Alto | **Alta** | Entra Connect Sync con test preventivo su OU pilota. Verifica attributi utente prima della sincronizzazione completa. |
| R06 | Costi superiori al previsto | Bassa | Medio | **Bassa** | Reserved instances per App Service e VM. Budget margin ~€195K. Alert di spesa Azure configurati. |
| R07 | Incompatibilità codice Pondus legacy con App Service | Media | Alto | **Alta** | Analisi preventiva del codice C# (ASP.NET WebForms vs Core). Se necessario, percorso alternativo su VM Azure (IaaS). |
| R08 | Latenza VPN sede → Azure troppo alta | Bassa | Medio | **Bassa** | West Europe è la regione più vicina a Torino (~1000 km, latenza prevista &lt;5 ms). Test di latenza prima della migrazione. |
| R09 | Perdita dati calendar/contatti durante migrazione posta | Bassa | Medio | **Media** | Sync tool Microsoft con verifica incrociata. Esportazione .pst di backup prima della migrazione. |
| R10 | MFA blocca utenti senza smartphone | Bassa | Medio | **Media** | Conditional Access con eccezioni per device compliance. Token OATH hardware per utenti senza smartphone. |

---

## Mappa calore

```
Probabilità
    ↑
Alta    │         │         │  R03    │
        │         │         │         │
Media   │  R04    │ R01,R02 │         │
        │         │  R05    │         │
Bassa   │  R06,R08│ R09,R10 │  R07    │
        │  R09    │         │         │
        └────────┴─────────┴─────────┴──→ Impatto
          Basso     Medio      Alto
```

## Rischi chiusi (non applicabili)

| # | Rischio | Motivo esclusione |
| --- | --- | --- |
| — | Downtime infrastruttura di rete | Gestito dal piano Rete/VPN (area 02) |
| — | Superamento budget HPC | Percorso HPC separato, non incluso in questo piano |
| — | Problemi licenze software legacy | Licenze M365 e Dynamics incluse nel canone; MS SQL sostituito da Azure SQL |

---

## Piano di contingency

| Scenario | Azione | Tempo di risposta |
| --- | --- | --- |
| Migrazione posta fallisce per un utente | Ripristino manuale da backup .pst + Zimbra in lettura | 4 ore |
| Dati Dynamics corrotti | Ripristino da snapshot pre-migrazione | 8 ore |
| AD Samba4 non sincronizza | Revert a Entra Connect Sync precedente, diagnostica attributi | 4 ore |
| VM Media Wiki non raggiungibile | Puntamento DNS a VM on-prem (istanza originale) | 15 minuti |
| Attacco ransomware durante migrazione | Isolation tenant M365 + restore da backup (retention 30 giorni) | 24 ore |
