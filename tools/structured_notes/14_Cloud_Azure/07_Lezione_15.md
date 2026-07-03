# Lezione 15

## Panoramica
AI su Azure: Foundry, modelli e GitHub Copilot (in preparazione all'evento Microsoft Build //localhost Torino) (4 ore)

## Argomenti trattati
Azure, Git, Reti, API REST

---
## Appunti

### Slide 1
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
AI su Azure: Foundry, modelli e GitHub Copilot (in preparazione all'evento Microsoft Build //localhost Torino) (4 ore)
### Slide 2
Foundry, modelli e GitHub Copilot: cosa c'è sotto le demo del Microsoft Build //localhost Torino
### Slide 3
•  Dove sta l'AI nel catalogo Azure (AI Services, Azure OpenAI, Foundry)
•  Azure AI Foundry: risorsa, progetto, hub — cosa sono davvero
•  Deployare un modello (gpt-4o-mini) e usarlo dal playground
•  Chiamare il modello via endpoint + key (il ponte verso il codice)
•  GitHub Copilot e i modelli di Foundry
•  Agenti: il loop "ragiona → usa strumento → risponde" (cenni)
•  Responsible AI e costi a token
•  Filo conduttore: è tutta infrastruttura Azure che già conoscete
### Slide 4
Dove sta l'AI nel catalogo Azure
•  Azure AI Services — modelli pronti via API: Vision, Language, Speech, Translator
•  Azure OpenAI — i modelli GenAI (GPT, ecc.) ospitati su Azure, con endpoint e key
•  Azure AI Foundry — l'hub di lavoro sopra i modelli: deploy, playground, agenti, RAG
“Stessa logica di sempre: una risorsa dentro un resource group, in una regione, con identità e accesso che già sapete gestire. L'AI non è un mondo a parte.”
### Slide 5
Azure AI Foundry: i pezzi
•  Risorsa di Foundry — l'account (tipo AIServices) che contiene tutto
•  Progetto — l'area di lavoro dentro la risorsa: modelli, agenti, dati, valutazioni
•  Hub (versione classica) — workspace condiviso, costruito sopra Machine Learning
“Due esperienze convivono: la "Nuova fonderia" (risorsa + progetto) e l'hub classico. Stesso obiettivo, organizzazione diversa.”
### Slide 6
Deployare un modello e provarlo
•  Dal catalogo (oltre 100 modelli: OpenAI, Llama, Mistral, Cohere…) si sceglie e si fa deploy.
•  Il deployment è il "modello pubblicato": ha un nome e si chiama da playground e API.
•  Per la demo: `gpt-4o-mini` — economico, veloce, multimodale.
•  Nel playground / Chat si prova subito: prompt → risposta.
•  Concetti da mostrare lì: system prompt (istruzioni), temperature, token.
### Slide 7
Dal playground al codice
•  Il playground è comodo, ma in produzione si chiama il modello via API.
•  Servono due cose: l'endpoint della risorsa e una key (oppure Managed Identity).
curl "$ENDPOINT/openai/deployments/gpt-4o-mini/chat/completions?api-version=2024-08-01-preview" \
-H "api-key: $KEY" -H "Content-Type: application/json" \
-d '{"messages":[{"role":"user","content":"Ciao!"}]}'
“Stesso modello, stessa risposta del playground: cambia solo che ora lo chiama il tuo codice.”
### Slide 8
GitHub Copilot e i modelli di Foundry
•  GitHub Copilot = assistente AI dentro l'editor (scrive, spiega, refattorizza codice).
•  Non è "un altro modello": dietro usa modelli (OpenAI e altri) e oggi può collegarsi a modelli ospitati su Azure / Foundry.
•  Vantaggio per l'azienda: stessi modelli, governance, billing e dati sotto il proprio tenant Azure.
•  Due usi complementari:
○  Copilot → produttività dello sviluppatore
○  modello via API/Foundry → AI dentro l'applicazione che costruisci
### Slide 9
Agenti: oltre la singola risposta
•  Un agente non si limita a rispondere: ragiona → usa uno strumento → risponde.
•  Strumenti tipici: Code Interpreter (esegue codice), ricerca su dati/RAG, funzioni custom.
•  Esempio: "somma dei primi 50 numeri primi" → l'agente scrive ed esegue codice e poi spiega.
•  Agenti, routine e workflow: dal singolo agente a più passi orchestrati (routine ricorrenti, workflow multi-step e multi-agente).
•  È il loop "agentico" che vedremo all'evento (Foundry Agents).
•  Nota reale: creare agenti richiede il ruolo dati Foundry User sulla risorsa (RBAC).
### Slide 10
Responsible AI e costi
•  Allucinazioni: il modello può affermare cose false con tono sicuro → serve verifica umana.
•  Bias e content filter: Azure applica filtri sui contenuti; l'AI Act UE classifica per rischio.
•  Dati: con Azure i prompt restano nel tuo tenant (governance, compliance).
•  Costi a token: i modelli Standard/GlobalStandard sono pay-per-token → da fermi non costano.
○  eccezione: i deployment Provisioned (PTU) riservano capacità e si pagano a ore.
### Slide 11
Da portare a casa (e all'evento)
•  L'AI su Azure è una risorsa + un modello deployato: ci parli con endpoint e key, come ogni servizio.
•  Foundry è lo studio di lavoro attorno ai modelli: deploy, playground, agenti, RAG.
•  GitHub Copilot porta gli stessi modelli nell'editor, sotto la governance del tuo tenant.
•  Gli agenti aggiungono il loop ragiona→strumento→risponde.
•  Tutto poggia su ciò che già sappiamo: resource group, identità, RBAC, costi.
“All'evento (Build //localhost Torino) vedrete Foundry e Copilot costruire applicazioni AI: ora sapete cosa c'è sotto.”

---
*Fonte: 015_15_Microsoft_Azure_-_AI_su_Azure_-_Foundry_modelli_e_GitHub_Copilot.md*
