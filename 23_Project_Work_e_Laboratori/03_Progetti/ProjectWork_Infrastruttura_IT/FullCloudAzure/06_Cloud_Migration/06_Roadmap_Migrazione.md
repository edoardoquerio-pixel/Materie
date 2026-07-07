# 06 — Roadmap Migrazione

> **Documento:** Fasi, attività, rollback per la migrazione Full Cloud Azure  
> **Data:** Luglio 2026

---

## Fase 0 — Foundation (Settimane 1-2)

**Obiettivo:** Creare il tenant M365, configurare Entra ID, preparare l'infrastruttura Azure di base.

| # | Attività | Responsabile | Durata |
| --- | --- | --- | --- |
| F0.1 | Creazione/consolidamento tenant M365 TP Group | Sistemista | 1 giorno |
| F0.2 | Configurazione domini personalizzati su Entra ID | Sistemista | 1 giorno |
| F0.3 | Setup Entra Connect Sync (sincronizzazione da AD Samba4) | Sistemista | 2 giorni |
| F0.4 | Creazione utenti Pro Studio in AD + Entra ID | Sistemista | 2 giorni |
| F0.5 | Assegnazione licenze M365 a tutti i 50 utenti | Sistemista | 1 giorno |
| F0.6 | Configurazione MFA tramite Conditional Access | Sistemista | 1 giorno |
| F0.7 | Creazione resource group Azure: `rg-tpgroup-migration-westeu` | Sistemista | 0,5 giorni |
| F0.8 | Provisioning VNet, subnet, VPN Gateway | Sistemista | 2 giorni |

**Dipendenze:** AD Samba4 accessibile e funzionante, credenziali amministrative tenant Microsoft.

---

## Fase 1 — Posta: Zimbra + GWS → Exchange Online (Settimane 3-5)

**Obiettivo:** Migrare tutte le 50 caselle a Exchange Online con zero perdita dati.

| # | Attività | Responsabile | Durata |
| --- | --- | --- | --- |
| F1.1 | Configurazione Exchange Online (domini, policy, alias, DKIM) | Sistemista | 1 giorno |
| F1.2 | Migrazione caselle Zimbra → Exchange Online (IMAP sync o tool) | Sistemista | 5 giorni |
| F1.3 | Migrazione caselle Google Workspace → Exchange Online | Sistemista | 5 giorni |
| F1.4 | Configurazione Outlook per tutti gli utenti (autodiscover) | Sistemista | 2 giorni |
| F1.5 | Verifica calendari, contatti, regole, firme | Sistemista + Utenti pilota | 2 giorni |
| F1.6 | Puntamento MX a Exchange Online | Sistemista | 1 ora |

**Rollback:** Mantenere Zimbra in sola lettura per 7 giorni. MX record punta ancora a Zimbra fino a verifica completata.

---

## Fase 2 — File: NextCloud + Drive → SharePoint/OneDrive (Settimane 3-4)

**Obiettivo:** Migrare tutti i dati file a SharePoint/OneDrive conservando permessi e struttura.

| # | Attività | Responsabile | Durata |
| --- | --- | --- | --- |
| F2.1 | Creazione struttura siti SharePoint (dipartimenti, progetti) | Sistemista | 2 giorni |
| F2.2 | Configurazione OneDrive per tutti i 50 utenti | Sistemista | 1 giorno |
| F2.3 | Migrazione dati Google Drive → SharePoint/OneDrive | Sistemista | 3 giorni |
| F2.4 | Migrazione dati NextCloud → SharePoint/OneDrive | Sistemista | 3 giorni |
| F2.5 | Verifica permessi, condivisioni, metadati | Sistemista + Utenti pilota | 2 giorni |

**Rollback:** Mantenere NextCloud in sola lettura per 7 giorni.

---

## Fase 3 — Dynamics 365: Sales + BC (Settimane 4-8)

**Obiettivo:** Configurare Dynamics 365 e migrare dati CRM, ERP e timesheet.

| # | Attività | Responsabile | Durata |
| --- | --- | --- | --- |
| F3.1 | Setup tenant Dynamics 365 + integrazione Entra ID | Sistemista | 1 giorno |
| F3.2 | Configurazione Dynamics Sales (pipeline, campi, automazioni) | Consulente Dynamics | 5 giorni |
| F3.3 | Configurazione Dynamics BC (piano dei conti, IVA, fatturazione) | Consulente Dynamics | 5 giorni |
| F3.4 | Migrazione CRM: Sugar CRM → Dynamics Sales | Consulente Dynamics | 3 giorni |
| F3.5 | Migrazione ERP: Profis → Dynamics BC | Consulente Dynamics | 5 giorni |
| F3.6 | Migrazione timesheet: Kimai → Dynamics BC | Consulente Dynamics | 2 giorni |
| F3.7 | Migrazione Odoo (CRM + contabilità + timesheet) → Dynamics | Consulente Dynamics | 5 giorni |
| F3.8 | Test utenti pilota (5 utenti, 1 settimana) | Sistemista + Utenti pilota | 5 giorni |
| F3.9 | Formazione utenti + roll-out completo | Consulente + PM | 3 giorni |

**Rollback:** Mantenere Sugar CRM, Profis, Kimai, Odoo attivi per 2 settimane. Dati contabili Profis in cold storage 30 giorni.

---

## Fase 4 — Azure DevOps: Repos + Pipelines (Settimane 5-6)

**Obiettivo:** Centralizzare il versioning e abilitare CI/CD.

| # | Attività | Responsabile | Durata |
| --- | --- | --- | --- |
| F4.1 | Creazione organizzazione Azure DevOps | Sistemista | 0,5 giorni |
| F4.2 | Migrazione repo GiTea → Azure Repos (mirror con history) | Sistemista | 1 giorno |
| F4.3 | Migrazione repo BitBucket → Azure Repos | Sistemista | 1 giorno |
| F4.4 | Setup Azure Pipelines per progetti attivi | Sistemista | 2 giorni |
| F4.5 | Configurazione self-hosted agent per accesso on-prem | Sistemista | 1 giorno |

**Rollback:** GiTea + BitBucket in sola lettura per 7 giorni.

---

## Fase 5 — Media Wiki su VM Azure (Settimana 5)

**Obiettivo:** Unificare la documentazione aziendale su Media Wiki in Azure.

| # | Attività | Responsabile | Durata |
| --- | --- | --- | --- |
| F5.1 | Provisioning VM B2s West Europe | Sistemista | 1 ora |
| F5.2 | Installazione Media Wiki (stessa versione attuale) | Sistemista | 1 giorno |
| F5.3 | Migrazione contenuti: unificare istanza on-prem + GCP | Sistemista | 2 giorni |
| F5.4 | Configurazione backup (Azure Backup + snapshot) | Sistemista | 1 giorno |
| F5.5 | Puntamento DNS wiki.tpgroup.it → IP VM Azure | Sistemista | 1 ora |

**Rollback:** Puntare DNS all'istanza on-prem originale.

---

## Fase 6 — Test e accettazione (Settimane 8-9)

**Obiettivo:** Verificare che tutti i servizi funzionino secondo i criteri di successo.

| Test | Criterio | Metodo |
| --- | --- | --- |
| Posta: invio/ricezione | &lt; 5 secondi | Test manuale 10 utenti |
| File: upload 100 MB | &lt; 10 secondi | Test SharePoint + OneDrive |
| MFA: accesso condizionale | Blocco/permesso corretto | Test policy per gruppo |
| Dynamics: creazione opportunità CRM | &lt; 3 secondi | Test funzionale |
| Dynamics: creazione fattura BC | &lt; 5 secondi | Test funzionale |
| Azure DevOps: clone + push | &lt; 30 secondi | Test repo mirror |
| Media Wiki: lettura/scrittura | &lt; 3 secondi | Test navigazione |
| Migrazione dati posta | 100%, checksum | Verifica a campione |
| Migrazione dati file | 100%, checksum | Verifica a campione |

---

## Fase 7 — Dismissione (Settimana 10)

**Obiettivo:** Spegnere le piattaforme legacy e completare la migrazione.

| # | Attività | Responsabile | Durata |
| --- | --- | --- | --- |
| F7.1 | Verifica che nessun servizio punti a piattaforme vecchie | Sistemista | 1 giorno |
| F7.2 | Migrazione Google Workspace → dismissione account | Sistemista | 1 giorno |
| F7.3 | Spegnimento VM Zimbra | Sistemista | 1 ora |
| F7.4 | Spegnimento VM NextCloud | Sistemista | 1 ora |
| F7.5 | Spegnimento VM Sugar CRM | Sistemista | 1 ora |
| F7.6 | Spegnimento VM Kimai | Sistemista | 1 ora |
| F7.7 | Spegnimento VM GiTea | Sistemista | 1 ora |
| F7.8 | Backup finale VM Profis → cold storage 30 giorni | Sistemista | 1 giorno |
| F7.9 | Backup finale AD Samba4 | Sistemista | 1 ora |
| F7.10 | Report finale di migrazione | PM | 2 giorni |

---

## Diagramma di Gantt (sintetico)

```
Settimana:   1  2  3  4  5  6  7  8  9  10
F0: Foundation       ████████
F1: Posta                        ██████████████
F2: File                          ██████████
F3: Dynamics                                 ████████████████████
F4: DevOps                                      ██████████
F5: Media Wiki                                     ██████
F6: Test                                                      ████████
F7: Dismissione                                                       ████
```
