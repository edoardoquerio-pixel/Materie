# 10) Microsoft Azure -Compute su Azure - Dischi, scalabilità e costo delle VM

**File:** `10) Microsoft Azure -Compute su Azure - Dischi, scalabilità e costo delle VM.pptx`
**Tipo:** `.pptx`
**Dimensione:** 72.9 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Compute su Azure: dischi, scalabilità e costo delle VM (4 ore)

---

Compute su Azure
Dischi, scalabilità e costo delle VM

---

Da dove proseguiamo
•  abbiamo già visto come si sceglie una VM: immagine, size, regione, disponibilità
•  adesso guardiamo che cosa cambia davvero prestazioni e costo nel tempo
•  i punti chiave sono dischi, ridimensionamento, scale set e scelte di spesa
•  la domanda è pratica: questa VM basta, costa il giusto, cresce bene?

---

Perché il disco conta
•  il disco non è solo spazio
•  influenza velocità di avvio, risposta dell'app e costo della VM
•  un disco lento può frenare anche una VM ben dimensionata
•  per questo compute e storage si leggono insieme

---

Tipi di disco in Azure
Tipo
Uso tipico
Standard HDD
casi economici e poco intensi
Standard SSD
uso base con latenza più stabile
Premium SSD
VM applicative e workload più reattivi
Ultra Disk
casi molto esigenti su IOPS e throughput
•  non tutti i tipi servono in ogni scenario

---

Standard, Premium, Ultra
•  Standard: costa meno, va bene per test o carichi leggeri
•  Premium: è il riferimento quando conta la reattività
•  Ultra: serve solo per workload molto spinti
•  la scelta va fatta sul bisogno reale, non sul livello più alto disponibile

---

OS disk e data disk
•  il OS disk contiene sistema operativo e avvio della VM
•  i data disk ospitano dati, log o parti dell'applicazione
•  separarli aiuta a gestire meglio prestazioni e crescita
•  non tutto deve stare sul disco del sistema

---

Caching: che cosa significa
•  il caching usa memoria locale dell'host per accelerare alcuni accessi al disco
•  può essere utile in lettura o in lettura/scrittura, secondo il caso
•  non è una spunta magica: va allineato al comportamento del carico
•  prima capisco l'uso del disco, poi scelgo il caching

---

Encryption dei dischi
Opzione
Significato
SSE
cifratura dei dati a riposo
PMK
chiavi gestite dalla piattaforma Azure
CMK
chiavi gestite dal cliente, di solito via Key Vault
•  il punto comune è proteggere i dati memorizzati sui dischi

---

Ridimensionare una VM
•  una VM può cambiare size se la stima iniziale non era corretta
•  aumentare o ridurre la taglia è il primo passo di right-sizing
•  non sempre serve creare una nuova macchina
•  prima misuro il bisogno, poi cambio dimensione

---

Scale up e scale out
Se faccio...
Sto facendo...
dare più risorse a una VM
Scale up
usare più istanze simili
Scale out
•  lo scale up è più semplice
•  lo scale out richiede un'app più distribuita
•  entrambi impattano costo e disponibilità

---

Virtual Machine Scale Set
•  uno Scale Set gestisce più VM simili come un gruppo
•  serve quando più istanze fanno lo stesso lavoro
•  può crescere o ridursi con regole di autoscaling
•  è il passaggio naturale quando una sola VM non basta più

---

Costo compute: che cosa incide
•  la size della VM pesa molto sul costo orario
•  contano anche dischi, tempo di accensione e numero di istanze
•  una VM accesa ma poco usata resta comunque una spesa
•  ottimizzare vuol dire usare risorse proporzionate

---

Right-sizing, RI e Savings Plans
•  Right-sizing: scegliere o correggere la taglia giusta
•  Reserved Instances: convenienza se il carico è stabile nel tempo
•  Savings Plans: più flessibili quando l'uso cambia tra servizi compute
•  prima osservo i consumi, poi scelgo l'impegno di spesa

---

Dove guardare nel portale
•  Virtual machines -> VM -> Size: taglia e cambio dimensione
•  Virtual machines -> VM -> Disks: OS disk, data disk, tipo disco
•  Virtual machine scale sets: gruppi di VM simili
•  Cost Management + Billing: lettura dei costi complessivi
•  con account limitati alcune opzioni possono non essere disponibili

---

Chiusura del blocco
•  non basta scegliere una VM: bisogna leggere anche dischi, crescita e spesa
•  Standard, Premium e Ultra rispondono a bisogni diversi
•  Scale Set serve quando il carico chiede più istanze uguali
•  il passo successivo è passare dal compute IaaS al compute gestito
