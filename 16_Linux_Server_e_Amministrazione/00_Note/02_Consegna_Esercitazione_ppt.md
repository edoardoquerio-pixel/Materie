# Consegna Esercitazione ppt

**File:** `Consegna Esercitazione ppt.pdf`
**Tipo:** `.pdf`
**Dimensione:** 111.1 KB
**Ultima modifica:** 02/07/2026 09:22

---

ESERCITAZIONE
Diagnostica e messa in sicurezza
di un'infrastruttura WordPress
Docente: Wolfgang Cecchin

Scenario
L'azienda Acme S.r.l. ha commissionato a un fornitore esterno un sito WordPress su due VM 
Debian. Alla consegna, il sito non funziona.
Macchina Ruolo Rete
debian3 Frontend — nginx + WordPress + PHP-FPM Solo Host + rete interna
debian4 Backend — MariaDB Solo rete interna
Comunicazione via rete interna privata intnet (10.0.0.0/24)
debian3 (frontend) debian4 (backend)
intnet 10.0.0.0/24

Informazioni di accesso
Dettagli
debian3 SSH dalla macchina Windows, porta 2222
Autenticazione con username e password
debian4 Non raggiungibile via SSH
Accesso dalla console VirtualBox
Username its-usr
Password Its2026

Fase 1 — Report diagnostico
Acme chiede un report scritto da presentare al fornitore. Per ogni problema:
Cosa non funziona
Il sintomo osservato
Dove si trova
File, regola o servizio
Perché non funziona
La causa tecnica
Suggerimento: procedete per livelli — rete → firewall → servizi — su ciascuna macchina.

Fase 2 — Ripristino e messa in sicurezza
Correggere i guasti e rendere il sito raggiungibile come acme.local
192.168.56.111  acme.local
→ aggiungere in C:\Windows\System32\drivers\etc\hosts
Il sito deve rispondere al nome acme.local — sia nella configurazione di nginx (server_name) che 
in WordPress (tabella wp_options nel database).

Requisiti di sicurezza
Firewall su entrambe le macchine
iptables attivo, policy DROP su INPUT.
debian3: SSH (2222), HTTP (80)
debian4: SSH (2222) + MariaDB (3306) solo da 
rete interna
SSH a debian4 solo da debian3
Nessun accesso diretto dall'esterno.
Passare per la rete interna.
MariaDB non esposto
In ascolto solo su 10.0.0.2,
non su tutte le interfacce.
Persistenza
Tutte le configurazioni devono
sopravvivere a un riavvio.

Consegna
1  Report diagnostico
Formato libero, chiaro e strutturato
2  Descrizione degli interventi
Comandi utilizzati e motivazione
