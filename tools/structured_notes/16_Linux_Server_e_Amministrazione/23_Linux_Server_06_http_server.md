# Linux Server 06 http server

## Panoramica
Negoziazione Client-Server e status code

## Argomenti trattati
Linux, Configurazione, Installazione, API REST, Git

---
## Appunti

Wolfgang Cecchin
UNITA’ FORMATIVA
Httpd Server: nginx, Apache
Negoziazione Client-Server e status code
https://developer.mozilla.org/en-US/docs/Learn/Serverside/First_steps/Client-Server_overview
Codici si stato
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
https://it.wikipedia.org/wiki/Codici_di_stato_HTTP
Architettura statica:
Architettura dinamica:
“Configurazione” di un webserver
• Assegniamo un nome al server;
Troviamo uno spazio per mettere i files;
• Diciamo al webserver come associare il nome ai files da servire;
• Configuriamo i log.
Installazione nginx
$ sudo apt update
$ sudo apt install nginx
Far partire, riavviare, fermare, conoscere lo stato di Nginx
$ sudo systemctl start nginx
$ sudo systemctl restart nginx
$ sudo systemctl stop nginx
$ sudo systemctl status nginx
Di default Nginx è in ascolto sulla porta 80
(di default anche Apache!).
Testare e ricaricare la configurazione di nginx:
$ sudo nginx -t
$ sudo systemctl reload nginx
Configurazione di nginx
I file di configurazione si trovano in:
La configurazione dei siti si trova in:
/etc/nginx/sites-available
Esiste una configurazione di default, quindi se io digito nel browser della mia macchina
locale un sito che ho impostato in /etc/hosts, ad esempio:
http://localhost
http://mercoledi.local
mi risponde la pagina di default di Nginx.
Creiamo una directory in cui inserire i file del sito.
/var/www/mercoledi.local
/srv/www/mercoledi.local
La configurazione del sito devo inserirla in:
/etc/nginx/sites-available
ma il sito va attivato con link simbolico in:
/etc/nginx/sites-enabled
Configurazione minima del file:
/etc/nginx/sites-available/mercoledi.local.conf
listen [::]:80;
server_name mercoledi.local;
root /var/www/mercoledi.local;
index index.html;
try_files $uri $uri/ =404;
In questo modo sto dicendo che chiamando
http://mercoledi.local
mi vengono serviti i files che si trovano nella directory:
/var/www/mercoledi.local
Attenzione! Non abbiamo ancora attivato il sito!
Configuriamo i log del web server
/var/log è la directory in cui si trovano i files di log dei principali servizi su Linux.
I log sono gestiti dal servizio (detto anche “demone”) syslogd, che tra le altre cose si
occupa anche della compressione.
Aggiungiamo i log specifici per questo sito:
listen [::]:80;
server_name mercoledi.local;
root /var/www/mercoledi.local;
index index.html;
try_files $uri $uri/ =404;
access_log /var/log/nginx/mercoledi.local.log;
error_log /var/log/nginx/mercoledi.local.error.log:
Codici di stato http
All’interno dei log sono memorizzate le risposte e gli errori del web server.
Approfondimenti sui codici di risposta http:
https://it.wikipedia.org/wiki/Codici_di_stato_HTTP
Attivazione di un sito
Attiviamo il sito.
La configurazione del sito devo inserirla in:
/etc/nginx/sites-available
ma il sito va attivato con link simbolico in:
/etc/nginx/sites-enabled
Per creare un link usiamo la sintassi:
$ sudo ln -s source nomeLink

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 006_Linux_Server_06_http_server.md*
