# Linux Server 08 php

## Panoramica
“Configurazione” del php e del mysql

## Argomenti trattati
Linux, Configurazione, Reti, API REST, Installazione

---
## Appunti

Docente: Wolfgang Cecchin
Titolo argomento:
“Configurazione” del php e del mysql
Installiamo il PHP;
Configuriamo Nginx per far funzionare il PHP;
(Configuriamo gli errori);
Installiamo i moduli del PHP che ci occorrono;
Utilizzando un web server PHP può essere eseguito in tre modalità: CGI, FastCGI o come
modulo dedicato del web server.
CGI è l’acronimo di Common Gateway Interface; si tratta di uno standard (RFC 3875)
utilizzato dai web server per interfacciarsi con applicazioni esterne. È stato il primo
strumento utilizzato per lo sviluppo di applicazioni web in C/C++ o Perl all’inizio degli anni
’90. Per ogni richiesta del web server su pagine dinamiche, come ad esempio quelle con
estensione .php, l’interfaccia CGI si preoccupa di eseguire l’interprete del linguaggio e di
restituire la risposta. Questo approccio consente di avere un isolamento dell’esecuzione del
codice tra web server e linguaggio interpretato ma rende il sistema inefficiente dal punto di
vista delle performance, poiché l’interfaccia è riallocata a ogni richiesta HTTP. Ormai questa
tecnologia non viene più utilizzata nelle moderne applicazioni PHP perché considerata poco
efficiente in presenza di altro traffico.
FastCGI è una tecnologia più recente, basata sullo stesso principio di funzionamento del
CGI, ma con la differenza che la comunicazione tra web server e FastCGI è gestita attraverso
socket. Un modulo FastCGI rimane in ascolto di eventuali richieste HTTP in memoria e non
deve essere rieseguito continuamente. Questa soluzione garantisce performance migliori
rispetto al CGI, soprattutto per applicazioni ad altro traffico. Ad esempio, il web server nginx
e Internet Information Service (IIS) utilizzano entrambi la modalità FastCGI per
l’esecuzione di applicazioni PHP.
Un’altra alternativa per eseguire il codice PHP in ambito web è l’utilizzo di un modulo
dedicato del web server. Questa modalità è stata, ed è tuttora, molto utilizzata con il web
server Apache grazie alla sua facilità di installazione e alle sue performance. Utilizzando un
modulo dedicato, le chiamate agli script PHP vengono gestite direttamente dal web server,
senza dover utilizzare un livello ulteriore di comunicazione, come nel caso di CGI o
FastCGI. Apache rimane a tutt’oggi il web server più utilizzato, con una quota di utilizzo
intorno al 50%. Nginx sta diventando sempre più popolare, soprattutto nei casi di
applicazioni web ad altro traffico.
Enrico Zimuel, Sviluppare in PHP 7
Installiamo il PHP
Nginx utilizza il PHP in modalità FastCGI, mentre Apache lo utilizza come modulo.
Infatti per installare il PHP con Nginx si usa il php-fpm (FastCGI Process Manager):
$sudo apt install php php-fpm
Procediamo con l’installazione del PHP_FPM.
$ sudo systemctl start php8.4-fpm
$ sudo systemctl enable php8.4-fpm
$ sudo systemctl status php8.4-fpm
Configuriamo nginx
Nel file di configurazione del nostro sito aggiungiamo:
# pass PHP scripts to FastCGI server
#
location ~ \.php$ {
include snippets/fastcgi-php.conf;
#
# # With php-fpm (or other unix sockets):
fastcgi_pass unix:/var/run/php/php8.4-fpm.sock;
# # With php-cgi (or other tcp sockets):
# fastcgi_pass 127.0.0.1:9000;
Aggiungere anche:
index index.html index.php;
Solo su macchine di sviluppo, configuriamo il PHP perché si vedano gli errori
Dove si trovano i files di configurazione del PHP?
Editiamo il file :
/etc/php/8.4/fpm/php.ini
per lo sviluppo
display_errors = On
error_reporting = E_ALL
Attenzione! In produzione devono essere:
display_errors = Off
error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT

---
*Fonte: 008_Linux_Server_08_php.md*
