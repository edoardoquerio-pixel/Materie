# panoramica guasti

Fonte: `panoramica guasti.pdf`

Panoramica dei guasti

#

1

2

3

4

5

6

7

Macchina

Livello

Guasto

Causa

debian3

Rete

IP rete interna errato

10.0.0.11 → 10.0.0.1

debian3

Firewall

HTTP bloccato

No regola porta 80

debian3

Servizio

nginx root sbagliata

/var/www/html → /wordpress

debian3

Applicazione

Nome sito errato

server_name + wp_options

debian4

Rete

Interfaccia spenta

enp0s8 DOWN

debian4

Firewall

MariaDB bloccato

No regola porta 3306

debian4

Servizio

bind-address errato

127.0.0.1 → 10.0.0.2