# Linux Server comando at

Fonte: `Linux Server comando at.pdf`

DOCENTE 

Wolfgang Cecchin 

UNITA’ FORMATIVA 

Linux Server 

ARGOMENTO 

Il comando at 

 
 
 
 
 
 
 
Il comando at serve a eseguire un comando o uno script una sola volta in un momento futuro 
specifico, senza che tu debba restare loggato. Si usa quando non vuoi una schedulazione ripetitiva 
come con cron.wikipedia 

Uso base 

La forma tipica è: 

bash 

at ORARIO 

Dopo aver dato il comando, scrivi i comandi da eseguire e poi chiudi con Ctrl+D. at assegna un 
numero di job al task pianificato. 

Esempio: 

bash 

at 09:00 

echo "Ciao" > /tmp/test.txt 

Ctrl+D 

Controllare e rimuovere job 

• atq mostra i job in coda per l’utente corrente. 

atrm <numero_job> rimuove un job pianificato. 

• at -l è un alias comune per elencare i job, e at -r per rimuoverli. 

Formati dell’orario 

Puoi indicare orari semplici come 09:00, oppure parole come now + 1 hour, noon, midnight a seconda 
dell’implementazione e della manpage disponibile. In alcune versioni puoi anche usare il formato 
POSIX con -t. 

Permessi 

L’uso di at può essere controllato da /etc/at.allow e /etc/at.deny: se esiste at.allow, solo gli utenti lì 
elencati possono usarlo. Root può sempre usarlo.man+1 

Quando usarlo 

Usalo per cose come: 

• un backup che deve partire una volta sola. 

• 

l’invio di un file a una certa ora. 

• una pulizia temporanea o un riavvio programmato.