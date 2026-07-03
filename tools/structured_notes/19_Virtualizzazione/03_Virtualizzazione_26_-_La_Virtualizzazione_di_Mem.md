# Virtualizzazione 26 - La Virtualizzazione di Mem

## Panoramica
Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]

## Argomenti trattati
Virtualizzazione, API REST, Data Analytics, Cloud, Git

---
## Appunti

Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]
Unità Formativa
Elementi di Virtualizzazione
La virtualizzazione della memoria
Richiami sulla memoria 1/4
• La memoria principale può agire come “cache” per la memoria di massa (dischi,
• Si parla in questo caso di memoria virtuale:
▪ I programmi sono compilati rispetto ad uno spazio di indirizzamento virtuale, diverso
da quello fisico;
▪ Il sistema di memoria virtuale traduce gli indirizzi virtuali in indirizzi fisici.
▪ illusione di avere una maggiore memoria fisica;
▪ meccanismi di protezione (gli spazi virtuali di programmi diversi mappati su spazi
fisici differrenti).
Elementi di Virtualizzazione |
Richiami sulla memoria 2/4
• La memoria e organizzata in modo
gerarchico (a livelli):
• Liv. 1: memoria più veloce(costosa).
• Liv. N: memoria più lenta (economica).
• Il processore indirizza tutta la memoria
di Liv. N, ma accede direttamente solo
• La pagine cercate si trovano al livello 1
con maggiore probabilità.
Elementi di Virtualizzazione |
Richiami sulla memoria 3/4
• Ad ogni istante solo una parte delle pagine di memoria “virtuale” è presente nella
memoria fisica.
• Quando la pagina cercata non è in memoria e deve essere letta da disco, si parla di page
• Il costo dei page fault è estremamente elevato (milioni di cicli), e questo influenza molte
scelte (dimensioni della pagina 4, 16, 32, 64 KB, gestione software).
• L’indirizzo virtuale si suddivide in Virtual Page Address + offset.
• Il Virtual Page Address indirizza le entry di una tabella, detta Page Table, che contiene
informazioni sulla presenza / validità delle pagine in memoria.
• In un sistema di memoria virtuale, ogni accesso alla memoria richiede due accessi: prima
alla Page Table e quindi alla memoria fisica.
• Per ridurre questo overhead si sfrutta un meccanismo detto TLB (Translation Lookaside
Buffer), una sorta di cache della Page Table. La TLB contiene copia delle entry della Page
Table riferite recentemente, e, come la cache, può sfruttare l’associatività per ridurre i
Elementi di Virtualizzazione |
Richiami sulla memoria 4/4
Elementi di Virtualizzazione |
La virtualizzazione della memoria 1/2
• In un ambiente non-virtualizzato:
▪ Utilizzando le page table, si passa dalla memoria virtuale alla memoria fisica.
▪ Si parla di one-level mapping.
• In un ambiente virtualizzato:
▪ Tutte le VM condividono la stessa memoria fisica e hypervisor deve ripartirla tra le
▪ Si parla di two-level mapping: dalla memoria virtuale guest alla memoria fisica guest
alla memoria fisica host.
• Terminologia:
➢Guest virtual memory: memoria visibile alle applicazioni; spazio di indirizzamento
virtuale continuo presentato dal guest OS alle applicazioni.
➢Guest physical memory: memoria visibile al guest OS.
➢Host physical memory: memoria hw reale visibile ad hypervisor.
Elementi di Virtualizzazione |
La virtualizzazione della memoria 2/2
• Two-level memory mapping:
• Per passare dalla guest virtual memory alla host physical memory serve un mapping
Guest VA (virtual address) → guest PA (physical address) → host MA (machine
• Guest physical address ≠ host machine address.
Elementi di Virtualizzazione |
Shadow Page-Table SPT 1/2
• Per evitare la riduzione delle prestazioni derivanti da extra memory mapping,
l’hypervisor utilizza delle shadow page-table (SPT) al fine di accelerare il mapping.
▪ Mapping diretto guest virtual su host physical memory address.
• SPT mappa direttamente l’indirizzo della guest virtual
memory nell’indirizzo della host physical memory.
▪ Il guest OS conserva la sua PT per memoria virtuale nello
spazio di guest physical memory assegnato.
▪ Per ogni dato in guest physical memory,
dovrebbe mapparne l’indirizzo nel dato corrispondente
di host physical memory.
▪ SPT mappa direttamente l’indirizzo della guest virtual
memory nell’indirizzo della host physical memory.
▪ L’hypervisor deve mantenere aggiornata la SPT ad ogni
cambio che il guest OS attua sulle sue PT.
Elementi di Virtualizzazione |
Shadow Page-Table SPT 2/2
• L’hypervisor utilizza l’hw di Translation Lookaside Buffer (TLB) per eseguire il
mapping diretto della memoria virtuale nella memoria di macchina fisica,

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 026_Virtualizzazione_26_-_La_Virtualizzazione_di_Mem.md*
