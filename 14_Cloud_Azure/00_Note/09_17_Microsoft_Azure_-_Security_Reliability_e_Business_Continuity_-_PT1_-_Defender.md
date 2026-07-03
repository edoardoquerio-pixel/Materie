# 17) Microsoft Azure - Security, Reliability e Business Continuity - PT1 - Defender e Key Vault

**File:** `17) Microsoft Azure - Security, Reliability e Business Continuity - PT1 - Defender e Key Vault.pptx`
**Tipo:** `.pptx`
**Dimensione:** 72.6 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Security, Reliability e Business Continuity - PT1: Defender for Cloud e Key Vault (4 ore)

---

Vedere il rischio e proteggere i segreti
Defender for Cloud per la postura, Key Vault per chiavi e credenziali

---

Argomenti (4 ore)
•  Defender for Cloud: posture management, workload protection, recommendations
•  Priorità del rischio: cosa guardare prima (esposizione, identity, patching)
•  Guest Configuration e vulnerability assessment come controllo continuo
•  Ridurre la superficie esposta: WAF, segmentazione, log ed evidenze
•  Key Vault: centralizzare segreti, chiavi e certificati
•  Accesso applicativo con Managed Identity e permessi minimi
•  Rotazione, scadenza, HSM e fiducia tra servizi (TLS/mTLS)

---

Perché partire da Defender for Cloud
•  La sicurezza cloud non si legge solo dal firewall o da una singola VM.
•  Serve una vista trasversale su configurazioni, rischi e priorità operative.
•  Defender for Cloud legge lo stato di sicurezza di subscription e risorse.
•  Il valore: vedere i problemi ricorrenti prima che diventino incidente.
•  La sicurezza diventa controllo continuo, non verifica occasionale.

---

Posture management e workload protection
Livello
Cosa guarda
Posture management
configurazioni, policy, esposizioni e hardening
Workload protection
minacce, vulnerabilità e segnali operativi
•  Il primo livello misura quanto l'ambiente è impostato bene.
•  Il secondo guarda cosa sta succedendo ai workload reali.
•  Le due letture servono insieme, non una al posto dell'altra.

---

Recommendations e priorità
•  Le recommendations mostrano configurazioni deboli o mancanti.
•  Non tutte pesano uguale: alcune riducono il rischio molto più di altre.
•  Leggere prima: esposizione pubblica, identity, patching, crittografia.
•  Il punto non è chiudere ticket, ma abbassare il rischio reale.
•  Serve sempre un ordine di priorità, non una lista piatta.

---

Guest Configuration e vulnerability assessment
•  Guest Configuration verifica che le VM rispettino le impostazioni attese.
•  Il vulnerability assessment evidenzia software e componenti deboli.
•  Servono a ridurre deriva configurativa e superfici note.
•  La sicurezza del workload non finisce al bordo della subnet.
•  Anche dentro la macchina vanno letti stato e conformità tecnica.

---

Ridurre la superficie e raccogliere evidenze
•  Meno porte aperte e meno endpoint pubblici = meno rischio.
•  WAF, segmentazione e regole mirate filtrano il traffico utile.
•  Principio guida: esporre solo ciò che serve davvero.
•  Activity Log e log diagnostici raccontano cosa è successo e dove.
•  Senza evidenze un incidente resta un sospetto: la sicurezza è anche lettura dei segnali.

---

Dal vedere il rischio al proteggere i segreti
•  Defender ci dice dove siamo esposti; ora vediamo come custodire ciò che è sensibile.
•  Una delle esposizioni più comuni: credenziali e chiavi sparse nel codice o nei file.
•  Il passo naturale è centralizzarle in un servizio dedicato: Azure Key Vault.
“Stesso obiettivo (ridurre il rischio), ma ora a livello di segreti e crittografia.”

---

Perché centralizzare segreti e chiavi
•  Segreti e chiavi sparsi nel codice o nei config aumentano il rischio.
•  Un servizio centrale rende chiari controllo accessi, rotazione e audit.
•  Azure Key Vault nasce per togliere le credenziali dai punti sbagliati.
•  L'obiettivo non è solo custodire il valore, ma governarne il ciclo di vita.

---

Segreti, chiavi e certificati
Oggetto
Uso tipico
Secret
password, connection string, token
Key
crittografia, firma, protezione dati
Certificate
TLS, identità del servizio, trust
•  Hanno tutti valore sensibile, ma scopi diversi.
•  Separarli bene aiuta a scegliere permessi e processo corretti.

---

Come un'app accede al vault
•  Il modello migliore su Azure è spesso la Managed Identity.
•  Così l'app non porta con sé credenziali da salvare altrove.
•  I permessi devono essere minimi e mirati all'oggetto richiesto.
•  L'accesso degli amministratori va separato da quello applicativo.
•  Un vault sicuro dipende tanto dal permesso quanto dal contenuto.

---

Rotazione e scadenza
•  Un segreto statico per anni è un debito, non una soluzione.
•  Rotazione e scadenza obbligano a rinnovare i valori sensibili.
•  L'app va progettata per leggere credenziali aggiornate.
•  Se la rotazione rompe il servizio, il problema è anche architetturale.
•  Qui si vede se la sicurezza è stata pensata davvero.

---

HSM e fiducia tra servizi
•  Non tutte le chiavi richiedono lo stesso livello di protezione.
•  Gli scenari più sensibili possono richiedere HSM dedicati o gestiti.
•  L'HSM aumenta garanzie e isolamento del materiale crittografico (compliance, rischio alto).
•  I certificati proteggono le connessioni e dichiarano identità: entrano in TLS e basi di mTLS.
•  Anche qui conta la gestione: rinnovo, scadenza, revoca. Domanda finale: chi si fida di chi, e con quale prova?

---

Da portare a casa
•  Defender for Cloud = vedere il rischio in modo continuo e per priorità.
•  Posture (come sei impostato) e workload protection (cosa accade) vanno letti insieme.
•  Key Vault = togliere segreti e chiavi dai punti sbagliati e governarne il ciclo di vita.
•  Managed Identity + permessi minimi = accesso applicativo senza credenziali sparse.
•  Filo unico: prima vedo dove sono esposto, poi proteggo ciò che è sensibile.
