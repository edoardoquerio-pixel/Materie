# Parte 2

## Panoramica
Reti su Azure - Parte 2 (3 ore)

## Argomenti trattati
Azure, Cloud, Reti, API REST, Git

---
## Appunti

### Slide 1
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
Reti su Azure - Parte 2 (3 ore)
### Slide 2
Reti su Azure - Parte 2
NSG su subnet e NIC, effective rules, HTTP/HTTPS e troubleshooting
### Slide 3
•  Ripresa dei concetti chiave della Parte 1
•  Differenza tra NSG su subnet e NSG su NIC
•  Effective security rules: dove leggere il risultato finale
•  Casi tipici: HTTP e HTTPS su una VM
•  Metodo di troubleshooting quando un accesso non funziona
•  Verifica dal portale e da Cloud Shell
### Slide 4
Ripartenza dalla Parte 1
•  Nella prima parte abbiamo visto VNet, subnet, NSG e caso RDP 3389
•  Il punto chiave era semplice: una regola di rete cambia davvero il comportamento della VM
•  Ora facciamo un passo in piu': capire dove applicare la regola e come leggere l'effetto complessivo
•  Non basta vedere un NSG nel portale: bisogna capire se e' quello che decide davvero il traffico
### Slide 5
Subnet e NIC: due livelli diversi
Quando e' utile
Un insieme di risorse nella stessa porzione di rete
Per regole comuni a piu' VM
Una singola interfaccia di rete
Per eccezioni o casi specifici
•  Azure permette di usare NSG su entrambi i livelli
•  Il punto non e' aggiungere regole ovunque, ma capire quale livello ha senso usare
### Slide 6
Quando ha senso lavorare sulla subnet
•  Quando piu' VM dello stesso livello applicativo devono seguire le stesse regole
•  Quando vuoi separare bene frontend, backend e zone amministrative
•  Quando vuoi una vista piu' ordinata della segmentazione
•  Quando la regola descrive il comportamento atteso di tutta una porzione di rete
La subnet e' il posto naturale per la policy comune.
### Slide 7
Quando ha senso lavorare sulla NIC
•  Quando una singola VM ha bisogno di un'eccezione temporanea o mirata
•  Quando vuoi differenziare una macchina senza cambiare tutta la subnet
•  Quando stai facendo verifica o isolamento di un nodo specifico
•  Se usi troppe eccezioni a livello NIC, pero', la lettura della rete diventa meno chiara
Una regola sulla NIC e' potente, ma va usata con criterio.
### Slide 8
Cosa conta davvero nel risultato finale
•  Il traffico reale dipende dalla combinazione delle regole visibili sulla subnet e sulla NIC
•  Guardare una sola regola spesso porta a conclusioni sbagliate
•  Se un livello blocca il traffico necessario, l'accesso fallisce anche se altrove vedi un allow
•  Per questo Azure offre una vista di sintesi: le effective security rules
Il problema non e' trovare una regola, ma capire l'effetto finale.
### Slide 9
Effective security rules
•  Sono la vista che aiuta a leggere il comportamento effettivo della VM
•  Riassumono regole default e regole custom che incidono sul traffico
•  Sono utili quando una VM non risponde e vuoi evitare di controllare oggetti a caso
•  Non sostituiscono il ragionamento, ma evitano errori di lettura del contesto
Se devi capire perche' una VM non e' raggiungibile, questa e' una verifica centrale.
### Slide 10
Caso tipico: pubblicare HTTP
Per raggiungere una pagina web su una VM servono almeno questi elementi:
•  Una Public IP associata al percorso corretto
•  Una regola inbound TCP 80 coerente con il livello scelto
•  Un servizio nella VM che ascolta davvero sulla porta 80
•  Nessun blocco effettivo che annulli quel traffico
La rete da sola non basta: deve esserci anche qualcosa che risponde dentro la VM.
### Slide 11
Caso tipico: pubblicare HTTPS
•  Dal punto di vista della rete, HTTPS significa soprattutto porta 443
•  Il certificato non risolve una regola mancante: se 443 non passa, il servizio resta irraggiungibile
•  In alcuni casi si lascia aperta anche la 80 per reindirizzare verso 443
•  In altri casi si espone solo 443 per ridurre la superficie visibile
La regola di rete decide il passaggio, il servizio applicativo decide la risposta corretta.
### Slide 12
Regole troppo larghe e regole troppo strette
Source = Any su porta sensibile
Espone troppo la VM
Priority non ragionata
Una regola inattesa puo' prevalere
Apertura su subnet intera senza motivo

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 007_7_Microsoft_Azure_-_Reti_su_Azure_-_Parte_2.md*
