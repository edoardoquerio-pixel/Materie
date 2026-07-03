# Consegna Esercitazione ppt

## Panoramica
Diagnostica e messa in sicurezza

## Argomenti trattati
Sicurezza, Reti, Configurazione, Database, Data Analytics

---
## Appunti

Diagnostica e messa in sicurezza
di un'infrastruttura WordPress
Docente: Wolfgang Cecchin
L'azienda Acme S.r.l. ha commissionato a un fornitore esterno un sito WordPress su due VM
Debian. Alla consegna, il sito non funziona.
Frontend — nginx + WordPress + PHP-FPM
Solo Host + rete interna
Backend — MariaDB
Solo rete interna
Comunicazione via rete interna privata intnet (10.0.0.0/24)
debian3 (frontend)
debian4 (backend)
intnet 10.0.0.0/24
Informazioni di accesso
SSH dalla macchina Windows, porta 2222
Autenticazione con username e password
Non raggiungibile via SSH
Accesso dalla console VirtualBox
Fase 1 — Report diagnostico
Acme chiede un report scritto da presentare al fornitore. Per ogni problema:
Cosa non funziona
Perché non funziona
Il sintomo osservato
File, regola o servizio
La causa tecnica
Suggerimento: procedete per livelli — rete → firewall → servizi — su ciascuna macchina.
Fase 2 — Ripristino e messa in sicurezza
Correggere i guasti e rendere il sito raggiungibile come acme.local
192.168.56.111 acme.local
→ aggiungere in C:\Windows\System32\drivers\etc\hosts
Il sito deve rispondere al nome acme.local — sia nella configurazione di nginx (server_name) che
in WordPress (tabella wp_options nel database).
Requisiti di sicurezza
Firewall su entrambe le macchine
SSH a debian4 solo da debian3
iptables attivo, policy DROP su INPUT.
debian3: SSH (2222), HTTP (80)
debian4: SSH (2222) + MariaDB (3306) solo da
Nessun accesso diretto dall'esterno.
Passare per la rete interna.
MariaDB non esposto
In ascolto solo su 10.0.0.2,
non su tutte le interfacce.
Tutte le configurazioni devono
sopravvivere a un riavvio.
1 Report diagnostico
Formato libero, chiaro e strutturato
2 Descrizione degli interventi
Comandi utilizzati e motivazione

---
*Fonte: 999_Consegna_Esercitazione_ppt.md*
