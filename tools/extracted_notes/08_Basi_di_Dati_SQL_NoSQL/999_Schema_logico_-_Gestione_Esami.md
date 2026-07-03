# Schema logico - Gestione Esami

Fonte: `Schema logico - Gestione Esami.docx`

Sede-Corso: 1:N

Corso-Materia 1:N

Corso-Studente 1:N

Studente-Materia N:N (Esame)

E/R => Modello Logico

Corso(Codice,Titolo,Descrizione,BiennioFormativo,IdSede*)

Sede(Id,Indirizzo,Cap,Citta,Provincia)

Materia(Id,Denominazione,Descrizione,NumeroOre,IdCorso*)

Studente(Matricola,Cognome,Nome,DataNascita,LuogoNascita

	,IndirizzoResidenza,CapResidenza,CittaResidenza,ProvinciaResidenza,TitoloStudio,Email,Cellulare,IdCorso*)

Esame(IdMateria*,Matricola*,Data,Voto)