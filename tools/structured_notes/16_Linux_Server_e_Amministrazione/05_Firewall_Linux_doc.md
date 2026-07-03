# Firewall Linux doc

## Panoramica
Un firewall è un sistema che controlla il traffico di rete in entrata e in uscita sulla base di un

## Argomenti trattati
Linux, Reti, API REST, Installazione, Configurazione

---
## Appunti

Wolfgang Cecchin
UNITA’ FORMATIVA
Firewall: iptables, ufw
Firewall in Linux
Cos'è un firewall
Un firewall è un sistema che controlla il traffico di rete in entrata e in uscita sulla base di un
insieme di regole. Su un server Linux, il firewall è fondamentale per proteggere i servizi
esposti: si decide esplicitamente cosa è permesso, e tutto il resto viene bloccato.
Il kernel Linux gestisce il filtraggio dei pacchetti attraverso un sottosistema chiamato
Netfilter. Gli strumenti iptables e ufw sono semplicemente interfacce per scrivere
regole che Netfilter applica.
Nota: Il successore moderno di iptables è nftables, diventato predefinito a partire da Debian 10.
Su sistemi recenti, il comando iptables è in realtà un wrapper che traduce i comandi in regole
nftables sottostanti. Per i server applicativi standard, iptables e ufw restano comunque lo
strumento pratico di riferimento.
Parte 1 — iptables
Come funziona iptables
iptables organizza le regole in tabelle e catene.
La tabella più usata è filter, che contiene tre catene predefinite:
• INPUT — traffico diretto al server stesso
• OUTPUT — traffico generato dal server
• FORWARD — traffico che transita attraverso il server (usato nei router)
Ogni pacchetto viene confrontato con le regole della catena, dall'alto verso il basso. Alla
prima regola che corrisponde viene applicata l'azione (chiamata target):
• ACCEPT — il pacchetto viene accettato
• DROP — il pacchetto viene scartato silenziosamente
• REJECT — il pacchetto viene rifiutato con un messaggio di errore
Se nessuna regola corrisponde, si applica la policy di default della catena.
Su Debian è disponibile nei repository ufficiali:
sudo apt install iptables
Visualizzare le regole correnti
sudo iptables -L -v -n
• -L — elenca le regole
• -v — output verboso (mostra contatori, interfacce)
• -n — mostra IP e porte in formato numerico (non fa lookup DNS)
La sintassi di base
sudo iptables -A CATENA -p protocollo --dport porta -j TARGET
• -A — appende la regola in fondo alla catena (append)
• -I — inserisce la regola in cima (o in una posizione specifica)
• -p — protocollo (tcp, udp, icmp)
• --dport — porta di destinazione
• -j — azione da eseguire (jump)
Accettare le connessioni SSH (porta 22)
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
Accettare il traffico HTTP e HTTPS
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
Accettare traffico sulla loopback
Indispensabile — senza questa regola molti servizi locali smettono di funzionare:
sudo iptables -A INPUT -i lo -j ACCEPT
Accettare connessioni già stabilite
Fondamentale: senza questa regola il server non riceve le risposte alle proprie richieste
(aggiornamenti apt, query DNS, ecc.):
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
Bloccare un indirizzo IP specifico
sudo iptables -A INPUT -s 192.168.1.50 -j DROP
Permettere o bloccare il ping in entrata
# Permettere
sudo iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
# Bloccare
sudo iptables -A INPUT -p icmp --icmp-type echo-request -j DROP
Se la policy di default è già DROP, la regola di blocco è ridondante — il ping verrebbe
ignorato comunque. Diventa necessaria solo se la policy è ACCEPT e si vuole bloccare
esplicitamente il ping lasciando aperto il resto.
Impostare la policy di default a DROP
Supponiamo di avere un server nginx con le regole precedenti già configurate. Si imposta la
policy di default per bloccare tutto il resto:
sudo iptables -P INPUT DROP
Da questo momento il server accetta solo SSH, HTTP, HTTPS e le connessioni già stabilite.
Tutto il resto viene silenziosamente ignorato.
Eliminare regole
Per eliminare una regola, si usa -D con la stessa sintassi usata per aggiungerla:
sudo iptables -D INPUT -p tcp --dport 80 -j ACCEPT
Oppure si elencano le regole con i numeri di riga e si elimina per numero:
sudo iptables -L INPUT --line-numbers
sudo iptables -D INPUT 3
Svuotare tutte le regole (flush)
Durante le prove in laboratorio, per ripartire da zero:
sudo iptables -F
sudo iptables -P INPUT ACCEPT

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_Firewall_Linux_doc.md*
