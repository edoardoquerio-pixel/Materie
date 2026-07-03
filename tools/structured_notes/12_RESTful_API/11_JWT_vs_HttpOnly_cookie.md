# JWT vs HttpOnly cookie

## Panoramica
● Login con POST /login → il server genera un JWT (spesso firmato con HS256)

## Argomenti trattati
Database, Data Analytics, API REST

---
## Appunti

JWT vs HttpOnly cookie
1. JWT in header
Scenario tipico:
● Login con POST /login → il server genera un JWT (spesso firmato con HS256)
Il client (SPA/JS) salva il token in:
○ localStorage oppure
○ sessionStorage
● Ad ogni richiesta → header:
Authorization: Bearer <jwt>
Problema principale
Se il sito ha anche solo una vulnerabilità XSS, uno script malevolo può fare:
localStorage.getItem("token") // oppure sessionStorage
e rubarsi il JWT.
A quel punto il token è usabile ovunque, da chiunque lo possieda.
● JWT molto lunghi
● scadenza troppo ampia
troppe informazioni dentro il payload
● nessun meccanismo di rotazione / revoca
Risultato: se il token viene rubato, l’attaccante è loggato “per sempre” finché il token non
2. Cosa cambia con HttpOnly cookie
L’idea moderna è:
1. Il server, dopo il login, NON ti dà il JWT da salvare nel JS.
Invece, risponde con un Set-Cookie:
Set-Cookie: access_token=<jwt-o-id-sessione>;
SameSite=Strict;
○ salva il cookie
lo rimanda automaticamente in ogni richiesta verso quel dominio.
Tu dal frontend non fai più:
Authorization: Bearer ...
ma semplicemente chiami le API (fetch/axios) e il browser allega i cookie.
Perché è più sicuro?
Flag HttpOnly → il cookie NON è leggibile da JavaScript:
document.cookie // non mostra il cookie HttpOnly
Quindi, anche se hai XSS, l’attaccante non può rubare il token semplicemente
leggendolo dal client.
● Flag Secure → il cookie viaggia solo su HTTPS (non in chiaro).
● Flag SameSite:
○ Strict o Lax riducono i rischi di CSRF, cioè richieste da altri siti che usano
3. Ma allora JWT sono “insicuri”?
Non è che JWT siano insicuri in sé.
Problemi comuni:
1. Uso improprio:
○ Token lunghissimi, con un sacco di dati sensibili.
○ Nessuna rotazione.
○ Nessuna revoca server-side (“se ho un JWT valido posso bypassare tutto”).
2. Storage insicuro nel frontend:
○ localStorage + XSS = furto del token.
3. Assenza di controlli extra:
○ niente IP binding, niente device binding, niente controllo su user-agent.
Spesso oggi si consiglia di:
● usare JWT come access token a breve durata
tenerli nel backend o in cookie HttpOnly, non nel JS leggibile.
4. Flusso moderno tipico (semplificato) per le tue
5. Confronto didattico: Header JWT vs HttpOnly cookie
Puoi sintetizzare così ai ragazzi:
JWT in header + localStorage
JWT/Session in HttpOnly Cookie
Lettura JS ✅ sì (localStorage)
❌ no (HttpOnly)
alto (token rubabile)
più basso (token non leggibile da
Rischio CSRF basso (token in header
più alto se SameSite è None
client controlla header
browser gestisce i cookie da solo
Messaggio importante da passare:
Non è che “JWT sono il male” e “cookie sono il bene”.
Il tema è dove tieni il token e come gestisci XSS/CSRF.
1. Implementre Http CLient Only
npm install cookie-parser
3. Modifica di server.js per usare i cookie
In server.js, aggiungi cookie-parser e (se usi una SPA) abilita CORS con credenziali.
server.js aggiornato (versione semplificata)
// agganciamo le librerie che abbiamo installato con node
const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bodyParser = require('body-parser');
const cors = require('cors');
const cookieParser = require('cookie-parser'); // <--- NEW
// dichiariamo su che porta risponderà il server web

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_JWT_vs_HttpOnly_cookie.md*
