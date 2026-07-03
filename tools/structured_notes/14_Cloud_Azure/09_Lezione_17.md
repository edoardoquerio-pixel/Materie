# Lezione 17

## Panoramica
Security, Reliability e Business Continuity - PT1: Defender for Cloud e Key Vault (4 ore)

## Argomenti trattati
Azure, Cloud, Sicurezza, Crittografia, API REST

---
## Appunti

### Slide 1
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
Security, Reliability e Business Continuity - PT1: Defender for Cloud e Key Vault (4 ore)
### Slide 2
Vedere il rischio e proteggere i segreti
Defender for Cloud per la postura, Key Vault per chiavi e credenziali
### Slide 3
Argomenti (4 ore)
•  Defender for Cloud: posture management, workload protection, recommendations
•  Priorità del rischio: cosa guardare prima (esposizione, identity, patching)
•  Guest Configuration e vulnerability assessment come controllo continuo
•  Ridurre la superficie esposta: WAF, segmentazione, log ed evidenze
•  Key Vault: centralizzare segreti, chiavi e certificati
•  Accesso applicativo con Managed Identity e permessi minimi
•  Rotazione, scadenza, HSM e fiducia tra servizi (TLS/mTLS)
### Slide 4
Perché partire da Defender for Cloud
•  La sicurezza cloud non si legge solo dal firewall o da una singola VM.
•  Serve una vista trasversale su configurazioni, rischi e priorità operative.
•  Defender for Cloud legge lo stato di sicurezza di subscription e risorse.
•  Il valore: vedere i problemi ricorrenti prima che diventino incidente.
•  La sicurezza diventa controllo continuo, non verifica occasionale.
### Slide 5
Posture management e workload protection
Posture management
configurazioni, policy, esposizioni e hardening
Workload protection
minacce, vulnerabilità e segnali operativi
•  Il primo livello misura quanto l'ambiente è impostato bene.
•  Il secondo guarda cosa sta succedendo ai workload reali.
•  Le due letture servono insieme, non una al posto dell'altra.
### Slide 6
Recommendations e priorità
•  Le recommendations mostrano configurazioni deboli o mancanti.
•  Non tutte pesano uguale: alcune riducono il rischio molto più di altre.
•  Leggere prima: esposizione pubblica, identity, patching, crittografia.
•  Il punto non è chiudere ticket, ma abbassare il rischio reale.
•  Serve sempre un ordine di priorità, non una lista piatta.
### Slide 7
Guest Configuration e vulnerability assessment
•  Guest Configuration verifica che le VM rispettino le impostazioni attese.
•  Il vulnerability assessment evidenzia software e componenti deboli.
•  Servono a ridurre deriva configurativa e superfici note.
•  La sicurezza del workload non finisce al bordo della subnet.
•  Anche dentro la macchina vanno letti stato e conformità tecnica.
### Slide 8
Ridurre la superficie e raccogliere evidenze
•  Meno porte aperte e meno endpoint pubblici = meno rischio.
•  WAF, segmentazione e regole mirate filtrano il traffico utile.
•  Principio guida: esporre solo ciò che serve davvero.
•  Activity Log e log diagnostici raccontano cosa è successo e dove.
•  Senza evidenze un incidente resta un sospetto: la sicurezza è anche lettura dei segnali.
### Slide 9
Dal vedere il rischio al proteggere i segreti
•  Defender ci dice dove siamo esposti; ora vediamo come custodire ciò che è sensibile.
•  Una delle esposizioni più comuni: credenziali e chiavi sparse nel codice o nei file.
•  Il passo naturale è centralizzarle in un servizio dedicato: Azure Key Vault.
“Stesso obiettivo (ridurre il rischio), ma ora a livello di segreti e crittografia.”
### Slide 10
Perché centralizzare segreti e chiavi
•  Segreti e chiavi sparsi nel codice o nei config aumentano il rischio.
•  Un servizio centrale rende chiari controllo accessi, rotazione e audit.
•  Azure Key Vault nasce per togliere le credenziali dai punti sbagliati.
•  L'obiettivo non è solo custodire il valore, ma governarne il ciclo di vita.
### Slide 11
Segreti, chiavi e certificati
password, connection string, token
crittografia, firma, protezione dati
TLS, identità del servizio, trust
•  Hanno tutti valore sensibile, ma scopi diversi.
•  Separarli bene aiuta a scegliere permessi e processo corretti.
### Slide 12
Come un'app accede al vault
•  Il modello migliore su Azure è spesso la Managed Identity.
•  Così l'app non porta con sé credenziali da salvare altrove.
•  I permessi devono essere minimi e mirati all'oggetto richiesto.
•  L'accesso degli amministratori va separato da quello applicativo.
•  Un vault sicuro dipende tanto dal permesso quanto dal contenuto.

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 017_17_Microsoft_Azure_-_Security_Reliability_e_Business_Continuity_-_PT1_-_Defender.md*
