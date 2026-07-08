# Registro Rischi — Progetto Full Cloud Azure

| # | Rischio | Probabilità | Impatto | Priorità | Azione | Responsabile |
|---|---|---|---|---|---|---|
| R01 | Incompatibilità codice Pondus legacy con App Service | Media | Alto | **Alta** | Analisi pre-migrazione. Se necessario, alternativa VM Windows (IaaS) | Sistemista + Sviluppatore |
| R02 | Resistenza utenti al cambio strumenti (GWS → M365) | Alta | Medio | **Alta** | Formazione dedicata, pilot con 5 utenti chiave, helpdesk dedicato prime 2 settimane | PM |
| R03 | Slittamento cronoprogramma per complessità migrazione ERP (Profis/BC) | Media | Alto | **Alta** | Consulente Dynamics 365 dedicato, buffer 1 settimana nel cronoprogramma | PM |
| R04 | Perdita dati durante migrazione | Bassa | Alto | **Alta** | Backup preventivo, verifica checksum, rollback plan per ogni fase | Sistemista |
| R05 | Costi Azure superiori al previsto | Media | Medio | **Media** | Budget alert, reserved instances, Azure Cost Management | PM |
| R06 | Latenza VPN Sede→Azure non adeguata per HPC | Bassa | Medio | **Bassa** | Test di latenza pre-migrazione. ExpressRoute come alternativa (costo maggiore) | Sistemista |
| R07 | Sincronizzazione AD Samba4 → Entra ID non completa | Bassa | Alto | **Media** | Test su OU pilota, Entra Connect Health monitoring | Sistemista |
| R08 | Attacco ransomware durante migrazione | Bassa | Alto | **Alta** | M365 Defender, backup preventivo, air-gapped backup | Sistemista + Security |
| R09 | Mancata disponibilità risorse (sistemista) | Media | Medio | **Media** | Pianificazione con secondo sistemista di backup | PM |
| R10 | Ritardo consegna hardware (FortiGate, switch) | Bassa | Medio | **Bassa** | Ordine con 4 settimane di anticipo, fornitore con SLA | PM |
