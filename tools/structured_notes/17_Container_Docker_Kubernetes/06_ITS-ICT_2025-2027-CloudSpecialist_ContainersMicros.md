# ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless introduzione

## Panoramica
Unità Formativa (UF): Containers Microservizi

## Argomenti trattati
Cloud, Docker, Git, Virtualizzazione, Sicurezza

---
## Appunti

Cloud Specialist
Unità Formativa (UF): Containers Microservizi
Docente: Denis Maggiorotto
Titolo argomento: Introduzione a Docker
Denis Maggiorotto
Denis Maggiorotto
• Managing Director and shareholder @ Sunnyvale S.r.l.
20 years of experience in ICT consulting
Senior Software / Enterprise Architect @ Major companies in public
utility, telco, TV broadcasting and banking sector
• Oracle University Principal Instructor regarding Java technologies
(Micro Edition, Standard Edition and Enterprise Edition) and Oracle's
middleware products.
Independent IT professional trainer and public speaker
Sistemi virtuali
Denis Maggiorotto
denis.maggiorotto@its-ictpiemonte.it
https://www.linkedin.com/in/denismaggiorotto/
https://github.com/denismaggior8
Introduzione a Docker
…partendo dalla virtualizzazione del SO
Tipologie di virtualizzazione
Permette l’esecuzione di un SO su una CPU completamente differente
Virtualizzazione piena (VirtualBox, Qemu)
Esegue copie di SO completi
Poco efficiente
Para-virtualizzazione (UML, Xen)
Esegue SO completi su architetture particolari (es: XEN/x86)
Segregazione delle risorse
Vantaggi della virtualizzazione
Multi SO: Piu` SO sulla stessa macchina ﬁsica, più ambienti di esecuzione (eterogenei).
Sicurezza: eventuali attacchi da parte di malware o spyware sono conﬁnati alla singola macchina
In ambito didattico: invece di assegnare ad ogni studente un account su una macchina ﬁsica, si assegna
una macchina virtuale.
Risorse: Segregazione delle risorse della macchina ﬁsica (Host) su ciascuna macchina virtuale
Difetti della virtualizzazione
Spreco di risorse: le macchine virtuali possono occupare un bel po’ di risorse hardware: ogni macchina
virtuale non esegue solo una copia di un certo sistema operativo ma sfrutta una copia virtuale di tutto
l'hardware di cui lo stesso sistema operativo necessita per funzionare correttamente.
Un approccio che necessita di RAM e che occupa parecchi cicli di CPU. Sempre più economico se
paragonato all'utilizzo di più macchine a sé stanti ma gravoso dal punto di vista dell'occupazione delle
risorse in alcuni frangenti.
Portabilità: Le tecnologie di virtualizzazione oggi presenti sul mercato non sono del tutto interoperabili,
rendendo così le VM poco portabili tra prodotti di virtualizzazione differenti
Perché virtualizzare un’intera macchina, quando sarebbe possibile virtualizzare
solamente una piccola parte di essa?
I container sono una sorta di sistema operativo sempliﬁcato e virtualizzato su
quello ospitante, insieme a tutti i dati di cui necessita un’applicazione per essere
eseguita: librerie, altri eseguibili, rami del ﬁle system, ﬁle di conﬁgurazione e script.
Ogni container vive in un contesto di esecuzione isolato, con un alto livello di
astrazione e segregazione rispetto agli altri container e al sistema operativo
Storia dei container qui: https://www.internetpost.it/container-linux-storiatecnologia/
I containers Docker
Docker è un progetto open-source che semplifica
l'esecuzione di applicazioni all'interno di container,
utilizzando le funzionalità di isolamento delle risorse offerte
dal kernel Linux, come ad esempio cgroup e namespace, per
consentire a container indipendenti di coesistere sulla stessa
istanza di Linux, evitando però l'installazione e la
manutenzione di una macchina virtuale.
Virtual machines vs containers
Virtual machines vs containers
libcontainer: fornisce un'implementazione per la creazione di container con snamespaces,
cgroups, controllo di accesso al ﬁlesystem. Consente di gestire il ciclo di vita del containers
libvirt: libvirt è un'API open source, un demone e uno strumento di gestione di piattaforme
di virtualizzazione (KVM, Xen, VMware ESXi, QEMU)
LXC: è un ambiente di virtualizzazione a container, che opera a livello del sistema operativo
e permette di eseguire diversi ambienti Linux virtuali isolati tra loro (container).
systemd-nspawn: viene utilizzato per eseguire comandi o un SO in un namespace.
Virtualizza completamente la gerarchia del ﬁle system, nonché l'albero dei processi, i vari
sottosistemi IPC e il nome host e dominio.
cgroups: sono una caratteristica del kernel che consente di controllare e limitare l'utilizzo
delle risorse (CPU, memoria, network I/O, disk I/O) da parte di un processo o gruppo di
namespaces: il compito di namespace è quello di permettere l’astrazione delle risorse (IPC,
rete, punto di mount di /, l’albero dei processi, gli utenti e i gruppi, risoluzione del nomi di
rete) e isolarle dal resto del sistema
Vantaggi dei container Docker
Gli stessi di una macchina virtuale, con l’aggiunta di:
▪ Portabilità delle immagini
▪ Dimensioni più contenute

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 2025_ITS-ICT_2025-2027-CloudSpecialist_ContainersMicroservicesServlerless_introduzion.md*
