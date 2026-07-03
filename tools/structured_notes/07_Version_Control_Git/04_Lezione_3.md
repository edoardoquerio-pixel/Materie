# Lezione 3

## Panoramica
Impara a gestire il tuo codice collaborativamente e in modo professionale

## Argomenti trattati
Git, Sicurezza, Cloud, Configurazione, Reti

---
## Appunti

Introduzione a Git Remoto e
Repository Online
Impara a gestire il tuo codice collaborativamente e in modo professionale
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Git Locale vs Git Remoto: La
Differenza Fondamentale
Repository Locale
Repository Remoto
Il tuo repository locale vive
Un repository remoto risiede su un
esclusivamente sulla tua macchina. Ogni
server esterno, accessibile da chiunque
commit, branch e modifica rimane
abbia le credenziali. È il centro di
confinato al tuo computer. È perfetto per
coordinamento dove tutti i collaboratori
lavorare oﬀline e sperimentare senza
sincronizzano il loro lavoro.
influenzare gli altri.
Accesso solo da una macchina
• Nessuna condivisione automatica
Rischio di perdita dati se il PC si
Accesso da qualsiasi dispositivo
Condivisione e collaborazione in
Backup automatico e sicurezza
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Perché Usare un Repository Remoto?
Backup Automatico
Collaborazione in Tempo Reale
Il tuo codice è al sicuro su server aﬀidabili. Anche se il tuo computer si
Lavora simultaneamente con colleghi e amici. Merge, pull requests e
rompe, la tua storia di commit e tutti i tuoi progetti sono preservati nel
code review diventano semplici. Ogni membro del team può
contribuire senza conflitti.
Integrazione CI/CD
Storia Completa
Automatizza test, build e deployment ogni volta che pushi nuove
Mantieni traccia di ogni modifica, chi l'ha fatta e quando. Ripristina
modifiche. Migliora la qualità del codice e riduci gli errori prima della
versioni precedenti in pochi secondi e analizza l'evoluzione del
progetto nel tempo.
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
HTTPS vs SSH: Scegliere il Protocollo Giusto
Il protocollo più semplice e universale.
Il protocollo più sicuro e professionale. Usa
Funziona ovunque senza configurazione
coppie di chiavi crittografiche per
aggiuntiva e utilizza le tue credenziali di
l'autenticazione automatica senza password.
GitHub/GitLab per l'autenticazione.
Facile da configurare per i principianti
Autenticazione automatica con chiavi
Funziona dietro qualsiasi firewall
• Maggiore sicurezza crittografica
Non richiede chiavi SSH
Nessun inserimento credenziali
Devi inserire username e password ogni
• Menù sicuro di SSH
Configurazione iniziale più complessa
Può essere bloccato da alcuni firewall
Suggerimento: Inizia con HTTPS per semplificare, poi passa a SSH quando ti senti più
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Conﬁgurazione accesso tramite HTTPS
git config --global user.name "IlTuoNome"
git config --global user.email "latuaemail@example.com"
© 2026 Mattia Nardulli – Tutti i diritti riservati.
TC-Web srl - Via Schiaparelli 14 - Torino https://www.tc-web.it
Il Flusso di Lavoro Git:
Un'Immagine Vale Mille Parole
1. Il Tuo Computer
2. Il Server Remoto
3. I Collaboratori
Clona il repository remoto
Pusha le tue modifiche al
Gli altri team member
sul tuo locale. Lavora,

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 003_Lezione_3_-_Introduzione_a_Git_Remoto_e_Repository_Online.md*
