# 08 - Basi di Dati SQL/NoSQL — Tutte le Sessioni


---

## Sessione 1: Schema logico - Gestione Esami


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


---
*Totale: 1 sessioni generate il 02/07/2026*