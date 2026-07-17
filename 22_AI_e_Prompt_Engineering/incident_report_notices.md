# Incident Report — Prompts for Teams (Italiano)

## Prompt A — Avviso per il team tecnico

**Input:** Il log dell'incidente di Task 1.

**Output:** Un riassunto tecnico in 5 punti:
- Cosa è successo
- Qual è la causa radice
- Qual è l'impatto (sui servizi/utenti)
- Come è stato risolto
- Come si può evitare (miglioramento)

**Formato:** Elenco puntato con punti elenco.

## Prompt B — Avviso per gli utenti

**Input:** Il messaggio utente per il team tecnico (copia-incollato qui da Prompt A).

**Output:** Un messaggio da pubblicare per gli utenti:
- Massimo 80 parole
- Niente gergo tecnico (ad es. container, WAL, upstream)
- Non dare colpe a nessuno, non minimizzare
- Deve dire cosa succede adesso

**Formato:** Testo semplice in modo pulito.

---

**Esempio per gli utenti (in base ai log:**

```
Il nostro sistema ha riscontrato un problema di spazio di archiviazione temporaneo che ha causato un'interruzione. Il team ha risolto il problema e tutti i servizi vengono riavviati. Si prega di riprovare tra qualche minuto: tutto dovrebbe essere di nuovo online.
```