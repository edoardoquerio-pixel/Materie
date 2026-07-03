# lezione find

## Panoramica
Il comando find è lo strumento principale di Linux per cercare file e directory nel filesystem in base

## Argomenti trattati
Linux, Data Analytics, Sicurezza, API REST, Configurazione

---
## Appunti

Wolfgang Cecchin
UNITA’ FORMATIVA
Il comando find è lo strumento principale di Linux per cercare file e directory nel filesystem in base
a criteri molto diversi: nome, tipo, dimensione, proprietario, permessi, data di modifica e altro
A differenza di ls, che elenca i contenuti di una directory, find esplora ricorsivamente l'albero del
filesystem a partire da un punto di inizio specificato.
1. Sintassi generale
$ find [percorso] [criteri] [azione]
Punto di partenza della ricerca. Si usa / per tutto il filesystem, . per la
directory corrente, /etc per limitare la ricerca
Uno o più filtri: nome, tipo, proprietario, permessi, dimensione, data...
Cosa fare con i file trovati. Se omessa, il default è -print (stampa il
percorso). Si può usare -exec per eseguire comandi
2. Criteri di ricerca principali
2.1 Nome del file (-name, -iname)
find / -name "hosts"
Cerca un file chiamato esattamente "hosts"
find / -name "hosts*"
Cerca file il cui nome inizia con "hosts" (* = qualsiasi
find / -name "*.conf"
Cerca tutti i file con estensione .conf
find / -iname "hosts"
Come -name, ma case-insensitive (HOSTS, Hosts,
📘 NOTA: Il carattere * è un glob (wildcard), non un'espressione regolare. Deve essere
racchiuso tra virgolette per evitare che la shell lo espanda prima di passarlo a find.
2.2 Tipo di file (-type)
2.3 Proprietario (-user, -group)
L'opzione -user filtra i file appartenenti a un utente specifico:
$ find / -user linda
Trova tutti i file nel filesystem il cui proprietario è l'utente linda.
$ find /home -group sviluppo -type f
Trova tutti i file regolari in /home appartenenti al gruppo sviluppo.
2.4 Dimensione (-size)
L'opzione -size accetta un valore con unità e un prefisso che indica il confronto:
find / -size +2G
+ = maggiore di 2 GiB
find / -size -100M
- = minore di 100 MiB
find / -size 4k
find / -type f -
Esattamente 4 KiB (raro in pratica)
Solo file regolari con dimensione superiore a 100 MiB
2.5 Data di modifica (-mtime, -mmin)
find /etc -mtime -1
File modificati nelle ultime 24 ore
find /etc -mtime +7
File non modificati da più di 7 giorni
find /tmp -mmin -30
File modificati negli ultimi 30 minuti
3. Ricerca per permessi (-perm)
L'opzione -perm permette di cercare file in base ai loro permessi in notazione ottale. Esistono tre
formati con significati distinti:
3.1 Tre formati di -perm a confronto
find . -perm 755
find . -perm -111
find . -perm /4000
Corrispondenza esatta: il file deve avere
esattamente quei permessi e nessun altro
Tutti i bit devono essere presenti, ma il file
può averne anche altri (sottoinsieme)
Almeno uno dei bit indicati deve essere
presente (OR logico)
3.2 I permessi speciali: SUID, SGID, Sticky bit
I bit speciali si specificano come quarta cifra ottale (la più significativa). Sono fondamentali per la
sicurezza del sistema.
Su file eseguibile: viene eseguito con i permessi del
proprietario del file (es. passwd esegue come root)
Su file: esegue con i permessi del gruppo. Su directory: i
nuovi file ereditano il gruppo della directory
Su directory (es. /tmp): solo il proprietario può eliminare o
rinominare i propri file, anche se la directory è scrivibile
3.3 Esempi pratici con -perm
find / -perm /4000
find / -perm /2000
File con il bit SUID attivo (formato /)
File con il bit SGID attivo
find / -type d -perm /1000
Directory con sticky bit attivo
find / -perm /7000
find . -perm -111

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_lezione_find.md*
