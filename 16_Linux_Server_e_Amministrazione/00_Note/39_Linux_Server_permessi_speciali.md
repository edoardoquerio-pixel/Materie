# Linux Server permessi speciali

**File:** `Linux Server permessi speciali.pdf`
**Tipo:** `.pdf`
**Dimensione:** 228.9 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
  
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
Permessi speciali 

[Digitare qui] 
 
 
 
1. Sticky Bit 
Lo sticky bit e un permesso speciale in Linux/Unix che si comporta in modo diverso a seconda che 
venga applicato a una directory o a un file eseguibile. 
 
1.1 Applicazione su una directory 
Quando lo sticky bit e impostato su una directory, solo il proprietario del file puo eliminare o 
rinominare i propri file all'interno di quella directory, anche se altri utenti hanno i permessi di 
scrittura sulla directory stessa. 
L'esempio classico e la directory /tmp: 
 
$ ls -ld /tmp 
drwxrwxrwt 10 root root 4096 feb 26 10:00 /tmp 
 
La t finale nei permessi indica che lo sticky bit e attivo. Tutti gli utenti possono scrivere in /tmp, ma 
nessuno puo cancellare i file degli altri. 
 
1.2 Impostare lo sticky bit 
E possibile impostare lo sticky bit con chmod in forma simbolica o numerica (il valore 1 come 
quarto ottetto): 
 
# Con chmod simbolico 
chmod +t /percorso/directory 
 
# Con chmod numerico (il 4° ottetto) 
chmod 1777 /percorso/directory 
 
1.3 Rimuovere lo sticky bit 
 
chmod -t /percorso/directory 
 
1.4 Verifica e simboli 
Per verificare se lo sticky bit e attivo: 
 
ls -ld /percorso/directory 
 
Differenza tra t e T nella visualizzazione dei permessi: 
• t (minuscolo) — sticky bit attivo, bit di esecuzione per others attivo 
• T (maiuscolo) — sticky bit attivo, bit di esecuzione per others NON attivo 

[Digitare qui] 
 
 
1.5 Caso pratico in ambiente server 
Creazione di una directory condivisa tra piu utenti del team in cui ognuno puo scrivere ma non 
cancellare i file altrui: 
 
mkdir /srv/shared 
chmod 1777 /srv/shared 
 
1.6 Nota: comportamento legacy sui file 
Storicamente, lo sticky bit su un file eseguibile indicava al kernel di mantenere l'immagine del 
processo in swap dopo l'esecuzione. Nei sistemi moderni questo comportamento e completamente 
ignorato. 
 
 
2. SUID Bit (Set User ID) 
La s visibile su /usr/bin/passwd e il SUID bit (Set User ID). Quando impostato su un file eseguibile, 
il processo gira con i privilegi del proprietario del file al momento dell'esecuzione, 
indipendentemente da chi lo ha lanciato. 
 
$ ls -l /usr/bin/passwd 
-rwsr-xr-x 1 root root 68208 mag  4  2023 /usr/bin/passwd 
 
La s al posto della x nel gruppo dei permessi del proprietario indica il SUID attivo. 
 
2.1 Perche passwd ne ha bisogno 
Le password degli utenti sono salvate nel file /etc/shadow, accessibile solo da root: 
 
$ ls -l /etc/shadow 
-rw-r----- 1 root shadow 1234 feb 26 10:00 /etc/shadow 
 
Un utente normale non puo scrivere in /etc/shadow. Grazie al SUID, quando viene eseguito 
passwd il processo ottiene temporaneamente i privilegi di root, ma il programma e scritto in modo 
da permettere la modifica solo della propria password. 
 
2.2 Impostare il SUID 
 
# Con chmod simbolico 
chmod u+s /percorso/file 
 
# Con chmod numerico (il valore 4 come quarto ottetto) 
chmod 4755 /percorso/file 

[Digitare qui] 
 
 
2.3 Attenzione: implicazioni di sicurezza 
I file con SUID sono un vettore di attacco comune in ambito di privilege escalation. Un file SUID 
root mal scritto puo essere sfruttato per ottenere privilegi di root non autorizzati. 
E buona pratica monitorare periodicamente quali file hanno il SUID attivo: 
 
find / -perm -4000 -type f 2>/dev/null 
 
 
 
3. Riepilogo dei Bit Speciali 
 
Bit Valore Simbolo Effetto 
SUID 4 s (permessi 
owner) 
Esegue con i privilegi del proprietario del file 
SGID 2 s (permessi 
gruppo) 
Esegue con i privilegi del gruppo proprietario 
Sticky 1 t (permessi 
others) 
Solo il proprietario puo eliminare i propri file 
 
 
4. Nota sul SGID (Set Group ID) 
In modo analogo al SUID, il SGID bit (valore 2) puo essere impostato su file o directory: 
• Su file eseguibili: il processo gira con i privilegi del gruppo proprietario del file 
• Su directory: i nuovi file creati all'interno ereditano il gruppo della directory anziche quello 
del creatore — utile per cartelle condivise di gruppo 
 
# Impostare SGID su una directory 
chmod g+s /percorso/directory 
chmod 2775 /percorso/directory 
 
