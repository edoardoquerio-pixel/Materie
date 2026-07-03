# Indirizzamento IPv4

## Panoramica
Fondamenti di Reti di Calcolatori

## Argomenti trattati
Reti

---
## Appunti

Andrea Blanchietti
Fondamenti di Reti di Calcolatori
Indirizzamento IPv4
Indirizzamento con protocollo IPv4
L’indirizzo IPv4 è composto da una sequenza di 32 bit, suddivisa in quattro gruppi da 8 bit l’uno;
ogni gruppo è definito ottetto. La rappresentazione dell’indirizzo avviene convertendo i singoli
ottetti dal sistema binario al sistema decimale: si parla di notazione decimale puntata.
L’indirizzo possiede una struttura gerarchica: una parte dell’indirizzo definisce la rete nel suo
insieme e la rimanente parte individua l’host (PC, stampante, server, etc.) all’interno della rete. I
bit che definiscono la parte di rete sono individuati dalla subnet mask. Per esempio:
Anche la subnet mask ha una struttura a quattro ottetti e viene utilizzata per individuare la parte
rete all’interno dell’indirizzo. I bit di rete dell’indirizzo corrispondono ai bit con valore 1 nella
subnet mask, mentre i bit della parte host corrispondono ai bit con valore 0; nell’esempio
precedente, la rete è rappresentata dal primo, dal secondo e dal terzo ottetto, contando a partire
La parte di rete è sempre composta dai bit più significativi dell’indirizzo.
192.168.10.______________
Una seconda notazione possibile per indicare i bit di rete all’interno dell’indirizzo è utilizzare il
Prefix Length (tradotto letteralmente in lunghezza del prefisso), ovvero un numero che indica
quanti sono i bit della parte rete.
Usando l’esempio precedente, ho 24 bit di rete:
192.168.10.23/24
Nell’indirizzamento IPv4, per ogni rete vi sono due indirizzi riservati: il network address (indirizzo
di rete, ovvero l’indirizzo che rappresenta la rete nel suo complesso) e il broadcast address
(indirizzo di broadcast, ovvero l’indirizzo per le comunicazioni da un singolo host a tutti gli host
• Nell’indirizzo di rete (network address), tutti i bit della parte host sono pari a 0
• Nell’indirizzo di broadcast, tutti i bit della parte host sono pari a 1
Usando l’esempio precedente, considerando una subnet mask pari a 255.255.255.0:
Network address:
tutti I bit della parte host sono 0
Broadcast address:
tutti I bit della parte host sono 1
Tutti i rimanenti indirizzi compresi fra 192.168.10.1 e 192.168.10.254 sono utilizzabili per
indirizzare gli host all’interno della rete. Il numero di indirizzi disponibili per gli host di una rete
dipende da quanti bit abbiamo a disposizione.
Dato un network address, quanti indirizzi si hanno a disposizione per gli host?
Dati n bit nella parte host di un indirizzo, quante combinazioni si possono ottenere?
Tolgo il network address ed il broadcast e ottengo il numero di indirizzi di host per un certo
indirizzo di rete:
Numero indirizzi disponibili = 2n - 2
Esempio: 192.168.10.____________ 28 – 2 = 254 indirizzi disponibili
Classi di indirizzamento
La struttura originale dell’indirizzamento IPv4 (legacy) prevede tre classi utilizzabili per indirizzare
le reti (indicate con le lettere A, B e C) più due classi ad uso speciale, ovvero la classe D degli
indirizzi multicast e la classe E per usi sperimentali.
• La seconda colonna della tabella indica, per ogni classe, l’intervallo dei valori possibili per il
primo ottetto dell’indirizzo.
• La terza colonna della tabella indica, per ogni classe, l’intervallo dei valori possibili in binario
per il primo ottetto dell’indirizzo.
• La quarta colonna della tabella indica con la lettera N gli ottetti di rete e con la lettera H gli
ottetti della parte host.
• La quinta colonna riporta la subnet nask per le tre classi di indirizzamento A, B e C (non è
prevista per le classi D ed E)
Indirizzi privati
All’interno delle tre classi di indirizzamento (A, B e C), vi sono tre sottogruppi riservati per
indirizzare le reti private e non sono utilizzabili per indirizzare risorse su internet (in generale su
“rete pubblica”); sono definiti indirizzi privati e sono i seguenti:
• CLASSE A: Indirizzo di rete 10.0.0.0 con subnet mask 255.0.0.0, anche indicato con la
notazione 10.0.0.0/8
• CLASSE B: Indirizzi di rete dal 172.16.0.0 al 172.31.0.0 con subnet mask 255.255.0.0
• CLASSE C: Indirizzi di rete 192.168. X .0 con subnet mask 255.255.255.0, dove il terzo
ottetto X può assumere un valore compreso tra 0 e 255
TABELLA RIASSUNTIVA INDIRIZZI IPv4 PRIVATI
INDIRIZZO DI RETE
NOTAZIONE CON PREFIX
192.168.255.0/24
Dato un indirizzo IP, come possiamo risalire all’indirizzo di rete (network address) e
all’indirizzo di broadcast?
Dato un indirizzo IPv4, voglio sapere quale è la rete di appartenenza (ovvero l’indirizzo di rete), a quale
indirizzo di broadcast corrisponde e a quale intervallo degli indirizzi appartiene.
Si deve individuare la parte host e la parte rete dell’indirizzo, in base alla maschera di sottorete o al prefix
ESEMPIO 1. 192.168.10.5/24 è un indirizzo utilizzabile per indirizzare un host e corrisponde a:
192.168.10.0/24
192.168.10.255/24
da 192.168.10.1 a 192.168.10.254
ESEMPIO 2. 172.21.152.12/16 è un indirizzo utilizzabile per indirizzare un host e corrisponde a:
172.21.255.255/8
da 172.21.0.1 a 172.21.255.254
ESEMPIO 3. 10.16.42.10/8 è un indirizzo utilizzabile per indirizzare un host e corrisponde a:
10.255.255.255/8
da 10.0.0.1 a 10.255.255.254

---
*Fonte: 004_Indirizzamento_IPv4.md*
