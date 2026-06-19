# Project Charter — Integrazione IT TP Group

| Campo | Valore |
|---|---|
| **Documento** | Project Charter |
| **Versione** | 1.0 |
| **Data** | Giugno 2026 |
| **Stato** | Bozza |
| **Redatto da** | Team di Progetto — Fornitore IT |
| **Approvato da** | [da approvare] |

---

## 1. Nome Progetto

**Integrazione IT TP Group**

---

## 2. Sponsor / Cliente

- **Azienda**: TP Group srl
- **Referente tecnico**: Andrei+ — Solution Architect
- **Ruolo nel progetto**: Committente e destinatario della soluzione

---

## 3. Ruolo del Fornitore

Il presente documento è redatto dal **Fornitore/Proponente** (azienda IT che propone e realizza la soluzione). Il fornitore si assume la responsabilità di progettazione, approvvigionamento, implementazione, test e avvio in esercizio dell'infrastruttura IT convergente per TP Group, nonché del supporto per il conseguimento della conformità ISO/IEC 27001.

---

## 4. Business Case

TP Group nasce dalla fusione tra **Thema Consulting** (realtà on-premise con sede fisica, datacenter interno e cluster HPC) e **Pro Studio** (realtà cloud-native basata su Google Workspace e GCP). La fusione genera l'esigenza improrogabile di:

- **Convergenza dei sistemi IT**: integrare le due realtà tecnologiche eterogenee in un'unica infrastruttura coerente, sicura e gestibile centralmente.
- **Adeguamento normativo ISO/IEC 27001**: certificazione necessaria per operare nei settori automotive (auto sportive) e aerospace, dove la sicurezza delle informazioni è requisito contrattuale.
- **Efficienza operativa**: razionalizzare costi IT, eliminare duplicazioni, unificare posta elettronica, identity management e backup.
- **Continuità operativa**: garantire la fruibilità dei servizi ai clienti anche in scenari di disastro, con ridondanza e delocalizzazione.
- **Vantaggio competitivo**: l'infrastruttura convergente e certificata ISO 27001 costituisce un elemento distintivo per l'acquisizione di nuovi committenti nei settori ad alta criticità.

L'investimento complessivo si colloca in un orizzonte di **3 anni**, con un ritorno atteso in termini di riduzione dei costi operativi, consolidamento infrastrutturale e abilitazione al lavoro da remoto per l'intero organico.

---

## 5. Obiettivi

### 5.1 Obiettivi primari

| # | Obiettivo | Criterio di completamento |
|---|---|---|
| O1 | Convergenza servizi IT Thema + Pro Studio in un'unica infrastruttura gestita | Tutti i servizi IT unificati sotto un unico dominio e policy di accesso |
| O2 | Allineamento alla certificazione **ISO/IEC 27001** | Gap analysis completata, policy di sicurezza redatte, evidenze documentali pronte per audit |
| O3 | Potenziamento cluster **HPC** (+8 nodi in 2 anni) | Specifica tecnica definita, nodi ordinati e installati secondo piano di espansione |
| O4 | Potenziamento applicazione **Pondus** e pubblicazione online | Nuova release distribuita con REST API, DB ottimizzato, accesso da remoto |
| O5 | **Smart working** operativo per 50 dipendenti | 40 postazioni in sede operative, 10+ collegamenti da remoto funzionanti con VPN Client-to-LAN |

### 5.2 Obiettivi secondari

- Redazione della documentazione tecnica e di progetto completa
- Migrazione graduale dei servizi Pro Studio da GCP verso l'infrastruttura convergente (hybrid cloud)
- Definizione e test delle procedure di Disaster Recovery
- Formazione del personale sui nuovi sistemi

---

## 6. Budget

### 6.1 Budget base

| Voce | Importo |
|---|---|
| Budget base infrastruttura | **520.000 € + IVA** |
| *di cui HPC on-premise* | *250.000 €* |
| *di cui HPC cloud (alternativa)* | *220.000 €* |

### 6.2 Extra manodopera (supporto triennale)

| Ruolo | Costo giornaliero | Durata |
|---|---|---|
| Sistemista senior | 500 €/gg | 3 anni |
| Project Manager | 650 €/gg | 3 anni |
| **Totale extra manodopera** | **~181.000 €** (stima su base annua) |

### 6.3 Note sul budget

- Il budget HPC prevede due scenari alternativi (on-premise 250 k€ / cloud 220 k€); la scelta verrà definitiva in fase di architettura dettagliata.
- I costi di manodopera sono stimati su una presenza media di 120 giorni/anno per sistemista e 60 giorni/anno per PM.
- L'IVA è esclusa dagli importi indicati e verrà applicata in fatturazione secondo le vigenti disposizioni fiscali.
- Eventuali variazioni superiori al ±10% dovranno essere approvate tramite richiesta di cambio formale (change request).

---

## 7. Tempistica

### 7.1 Cronoprogramma di massima

| Fase | Durata | Note |
|---|---|---|
| **Progettazione esecutiva** | 2 settimane | Architettura dettagliata, piano di migrazione |
| **Procurement HW/SW** | 8–16 settimane | Tempi di consegna critici, da avviare subito |
| **Setup infrastruttura di base** | 2 settimane | Rete, firewall, storage, virtualizzazione |
| **Migrazione servizi** | 4 settimane | Coesistenza con servizi esistenti |
| **Test e collaudo** | 1 settimana | Test funzionali, di carico, DR test |
| **Avvio in esercizio** | 1 settimana | Go-live, assistenza post-migrazione |
| **Totale attività attive** | **~12 settimane** | |
| **Ciclo di vita complessivo** | **3 anni** | Supporto, manutenzione e assistenza |

### 7.2 Vincoli temporali

- **Shutdown massimo consentito**: 7 giorni consecutivi
- **Coesistenza obbligatoria**: tutti i servizi devono rimanere fruibili durante la migrazione (nessuna interruzione completa)
- **Procurement**: i tempi di consegna hardware (8–16 settimane) rappresentano il percorso critico del progetto; l'ordine deve essere emesso entro la prima settimana dall'approvazione del charter

---

## 8. Team di Progetto

| Ruolo | Competenze | Impegno previsto |
|---|---|---|
| **Project Manager** | Coordinamento, pianificazione, risk management, reportistica | 650 €/gg, continuativo su 3 anni |
| **Sistemista Senior** | Reti, firewall, storage, virtualizzazione, cluster HPC, backup | 500 €/gg, continuativo su 3 anni |
| **Solution Architect** (Andrei+) | Supervisione tecnica lato cliente, validazione scelte architetturali | Ad horas |

*Eventuali figure aggiuntive (sviluppatore .NET per Pondus, specialista sicurezza per ISO 27001) verranno coinvolte secondo necessità e preventivate separatamente.*

---

## 9. Stakeholder

| Stakeholder | Interesse / Ruolo | Impatto |
|---|---|---|
| **Dirigenza TP Group** | Approvazione budget, decisioni strategiche, sponsor interno | Alto |
| **Dipendenti TP Group (50 totali)** | Utilizzatori finali dei sistemi IT, soggetti a smart working | Alto |
| **Clienti automotive / aerospace** | Fruizione servizi Pondus e collaborazione tecnica | Medio |
| **Fornitori HW/SW** | Tempi di consegna, qualità dei componenti, supporto | Medio |
| **Ente di certificazione ISO 27001** | Audit e rilascio certificazione | Alto |
| **Pro Studio (legacy)** | Continuità servizi cloud in fase di migrazione | Medio |

---

## 10. Rischi Preliminari

| # | Rischio | Probabilità | Impatto | Mitigazione proposta |
|---|---|---|---|---|
| R1 | **Datacenter saturo**: lo spazio fisico e la capacità elettrica/raffreddamento potrebbero non essere sufficienti per le nuove apparecchiature | Media | Alto | Audit preliminare del datacenter; valutare espansione rack o offload parziale su cloud |
| R2 | **Condizionamento al limite**: l'impianto di climatizzazione del datacenter potrebbe non reggere il carico termico aggiuntivo | Media | Alto | Verifica termica preventiva; predisporre soluzione di raffreddamento supplementare (in-rack cooling) |
| R3 | **Finestra di migrazione stretta (7 giorni)**: il tempo massimo di indisponibilità dei servizi è molto limitato | Alta | Alto | Pianificazione dettagliata delle attività; pre-migrazione e sync in finestra; rollback plan obbligatorio |
| R4 | **Coesistenza servizi durante migrazione**: mantenere operativi i sistemi legacy mentre si installano i nuovi | Alta | Medio | Architettura a commutazione (cut-over); bilanciamento del carico tra vecchio e nuovo per test progressivi |
| R5 | **Tempi consegna HW (8–16 settimane)**: ritardi nella fornitura di server, storage e apparati di rete | Media | Alto | Ordine anticipato (entro settimana 1); identificare fornitori alternativi; prevedere buffer di 4 settimane nel piano |
| R6 | **Complessità integrazione AD**: unificazione Active Directory Thema (Samba4) con Google Workspace Pro Studio | Media | Medio | Analisi di identity federation; soluzione ibrida con SSO (SAML/OpenID Connect) |
| R7 | **Perdita dati in migrazione**: errore umano o tecnico durante il trasferimento dati sensibili | Bassa | Molto Alto | Backup completo pre-migrazione; verifica checksum post-migrazione; test di restore |

---

## 11. Criteri di Successo

Il progetto si considera concluso con successo quando **tutte** le seguenti condizioni sono verificate:

1. **Integrazione completata entro 12 settimane** dalla data di inizio lavori (escluso procurement).
2. **Zero perdita di dati** in tutte le fasi di migrazione e cut-over.
3. **Certificazione ISO/IEC 27001 allineata**: gap analysis superata, policy di sicurezza formalizzate e implementate, evidenze documentali pronte per audit esterno.
4. **Smart working operativo**: tutti i 50 dipendenti abilitati al lavoro da remoto tramite VPN Client-to-LAN con protocolli sicuri.
5. **Cluster HPC espanso**: piano di acquisizione e installazione dei nuovi 8 nodi approvato e avviato (primo lotto).
6. **Pondus funzionante e pubblicato online**: nuova release dell'applicazione distribuita e accessibile da remoto con prestazioni adeguate.
7. **Nessuna interruzione di servizio non pianificata** durante la migrazione (shutdown massimo rispettato: 7 giorni totali).
8. **Documentazione di progetto completa**: project charter, architettura, piano di migrazione, piano di test, disaster recovery plan, manuale operativo.

---

## 12. Firma / Approvazione

Il presente Project Charter richiede l'approvazione formale del cliente per l'avvio delle attività.

| Ruolo | Nome | Firma | Data |
|---|---|---|---|
| **Project Manager** (Fornitore) | __________________________ | _________________ | ____/____/______ |
| **Solution Architect** (Cliente — Andrei+) | __________________________ | _________________ | ____/____/______ |
| **Direzione TP Group** (Cliente) | __________________________ | _________________ | ____/____/______ |

---
*Documento generato il Giugno 2026 — Versione 1.0*
