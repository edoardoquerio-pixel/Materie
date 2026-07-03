# Benvenuto Excel

**File:** `Benvenuto Excel.xlsx`
**Tipo:** `.xlsx`
**Dimensione:** 448.1 KB
**Ultima modifica:** 02/07/2026 09:11

---

## Sheet: Inizio

Benvenuto nel tour. 
Istruzioni per le utilità per la lettura dello schermo: Bastano 10 semplici passaggi per iniziare a usare Excel, l'app per fogli di calcolo più famosa al mondo. 
Questa presentazione include altri 11 fogli. Le istruzioni per ogni foglio iniziano nella cella A1 e tutti i passaggi successivi si trovano nelle celle A2, A3 e così via. 
Le istruzioni indicano le celle a cui passare per usare una funzionalità o suggeriscono letture di approfondimento.
Per iniziare, premi CTRL+PGGIÙ.
Fai un tour
Bastano 10 semplici passaggi per iniziare a usare
l'app per fogli di calcolo più famosa al mondo.
Per tornare all'inizio, premi CTRL+HOME. Per iniziare il tour, premi CTRL+PGGIÙ.
#VALUE!

## Sheet: 1. Sommare

Sommare numeri in modo efficiente |  |  |  |  |  | 
Ecco alcuni modi per sommare i numeri in Excel: |  |  |  |  |  | 
Le celle da C3 a D7 contengono dati con due colonne: Frutta e Importo.  |  | Frutta | Importo |  | Carne | Importo
Passa a D8 premendo CTRL+D, digita D8 e quindi premi INVIO. |  | Mele | 50 |  | Manzo | 50
Digita =SOMMA(D4:D7) e quindi premi INVIO. |  | Arance | 20 |  | Pollo | 30
Il risultato è 170.  |  | Banane | 60 |  | Maiale | 10
Ecco un altro modo per sommare, usando una scelta rapida da tastiera. Le celle da F3 a G7 contengono dati con due colonne: Carne e Importo. |  | Limoni | 40 |  | Pesce | 50
Passa alla cella G8. Premi ALT+= e quindi premi INVIO. |  |  |  |  |  | 
Il risultato nella cella G8 è 140. |  |  |  |  |  | 
Ecco un altro modo per creare una somma. Le celle da C10 a D15 contengono due colonne di dati: Articolo e Importo. |  | Articolo | Importo |  | Articolo | Importo
Ora somma solo i numeri superiori a 50. Passa alla cella D16. Digita =SOMMA.SE(D11:D15;">50"), quindi premi INVIO. Il risultato è 100. |  | Pane | 50 |  | Pane | 50
CREDITO EXTRA: Le celle da F10 a G15 contengono dati con due colonne: Articolo e Importo. Passa alla cella G16. Prova ad aggiungere un'altra formula SOMMA.SE qui. Somma gli importi nella colonna G, le celle da G11 a G15, ma sommando gli importi minori di 100. Il risultato dovrebbe essere 160. |  | Ciambelle | 100 |  | Ciambelle | 100
Altri dettagli: Vai a A27. In alternativa, per procedere al passaggio successivo, premi CTRL+PGGIÙ. |  | Biscotti | 40 |  | Biscotti | 40
 |  | Torte | 50 |  | Torte | 50
 |  | Crostate | 20 |  | Crostate | 20
Altre informazioni sulla funzione SOMMA  |  |  |  |  |  | 
Alcuni dei suggerimenti forniti sopra illustrano come usare la funzione SOMMA. Ecco altri dettagli. |  |  |  |  |  | 
Le celle da C37 a D41 contengono dati con due colonne: Frutta e Quantità.  |  |  |  |  |  | 
La formula nella cella D42: =SOMMA(D38:D41). |  |  |  |  |  | 
Se la funzione SOMMA nella cella D42 potesse parlare, direbbe: Somma i valori nelle celle D38, D39, D40 e D41. |  |  |  |  |  | 
Ecco un altro modo per usarla: |  |  |  |  |  | 
Le celle da C47 a D48 contengono dati con due colonne: Articolo e Importo.  |  |  |  |  |  | 
Le celle da F47 a G51 contengono dati con due colonne: Articolo e Importo.  |  |  |  |  |  | 
Le celle da E53 a E54 contengono dati con una colonna: Totale. |  |  |  |  |  | 
La formula nella cella E54: =SOMMA(D48; G48:G51;100). |  |  |  |  |  | 
Se la formula nella cella E54 potesse parlare, direbbe: Somma quanto segue: il valore nella cella D48, i valori nelle celle G48, G49, G50 e G51 e 100. |  | Frutta | Importo |  |  | 
La formula nella cella E54 usa: |  | Mele | 50 |  |  | 
• Un riferimento di cella singola, ovvero l'"indirizzo" o il "nome" di una cella. D48 è il riferimento di cella singola nella formula precedente.  |  | Arance | 20 |  |  | 
• Un intervallo di celle, ossia una serie di celle che inizia da una cella e termina in un'altra. G48:G51 è l'intervallo di celle nella formula.  |  | Banane | 60 |  |  | 
• Una costante, ovvero il numero 100.  |  | Limoni | 40 |  |  | 
DETTAGLIO IMPORTANTE: Passa alla cella E54. Noterai il valore 100 verso la fine della formula. Anche se è possibile inserire numeri in una formula come questa, non è consigliabile farlo a meno che non sia assolutamente necessario. Si tratta di un valore costante ed è facile dimenticarsi della sua presenza. È preferibile fare riferimento a un'altra cella, come la cella D16. In questo modo sarà più visibile e non nascosto all'interno di una formula.  |  |  | 170 |  |  | 
Passa alla cella A66 per l'istruzione successiva. |  |  |  |  |  | 
 |  | Articolo | Importo |  | Articolo | Importo
 |  | Tabella | 20 |  | Automobili | 20
 |  |  |  |  | Autocarri | 10
 |  |  |  |  | Biciclette | 10

## Sheet: 2. Riempire

Risparmiare tempo con il riempimento automatico delle celle |  |  |  |  |  |  |  | 
Ecco come usare la funzionalità di riempimento in Excel: |  |  |  |  |  |  |  | 
Le celle da C3 a G7 contengono dati con cinque colonne: la colonna "Questo:" con il numero 50 in ogni cella, la colonna "Più questo:" con i numeri 50, 60, 70 e 80, la colonna "Uguale:" con la cella E4 che contiene la somma delle celle C4 e D4, la colonna "Più questo:" con il numero 75 in ogni cella e la colonna "Uguale:" con la cella G4 che contiene la somma delle celle E4 e F4. |  | Questo: | Più questo: | Uguale: | Più questo: | Uguale: |  | 
Passa alla cella E4. Premi CTRL+D, digita E4 e premi INVIO.  |  | 50 | 50 | 100 | 75 | 175 |  | 
Seleziona le celle E4, E5, E6 e E7 tenendo premuto MAIUSC e la freccia GIÙ, quindi premi CTRL+MAIUSC+; . Excel inserirà automaticamente i totali nelle celle: 110, 120 e 130. Questa operazione è detta anche "ricopiare in basso". |  | 50 | 60 |  | 75 |  |  | 
CREDITO EXTRA: Passare alla cella G4 e ripetere la procedura per ricopiare in basso. |  | 50 | 70 |  | 75 |  |  | 
Le celle da C10 a G14 contengono dati con cinque colonne: Queste colonne contengono l'intestazione da C3 a G3 e i valori dalle celle da C4 a G7 dopo avere eseguito i passaggi nelle celle A5 e A6. |  | 50 | 80 |  | 75 |  |  | 
Passa alla cella C15. Seleziona le celle C15 D15, E15, F15 e G15. Questa volta premi CTRL+MAIUSC+: per riempire le celle. Questa operazione è detta "ricopiare a destra". |  |  |  |  |  |  |  | 
Altri dettagli: Passa alla cella A27. In alternativa, per procedere al passaggio successivo, premi CTRL+PGGIÙ. |  |  |  |  |  |  |  | 
 |  | Questo: | Più questo: | Uguale: | Più questo: | Uguale: |  | 
 |  | 50 | 50 | 100 | 75 | 175 |  | 
 |  | 50 | 60 | 110 | 75 | 185 |  | 
 |  | 50 | 70 | 120 | 75 | 195 |  | 
 |  | 50 | 80 | 130 | 75 | 205 |  | 
 |  | 200 |  |  |  |  |  | 
Usare il quadratino di riempimento per copiare le celle |  |  |  |  |  |  |  | 
A volte non è necessario che i numeri cambino con il riempimento. Può invece essere sufficiente copiare i valori in altre celle adiacenti. Ecco come fare: |  |  |  |  |  |  |  | 
Le celle da C33 a F37 contengono quattro colonne: Reparto, Categoria, Prodotto e Conteggio.  |  |  |  |  |  |  |  | 
Passa alla cella C34. Seleziona le celle C34, C35, C36 e C37 e premi CTRL+MAIUSC+; (punto e virgola). Il valore della cella C34 viene copiato nelle celle sottostanti selezionate. |  |  |  |  |  |  |  | 
Passa alla cella A64 per l'istruzione successiva. |  |  |  |  |  |  |  | 
 |  | Reparto | Categoria | Prodotto | Conteggio |  |  | 
 |  | Ortofrutta | Frutta | Mela | 100 |  |  | 
 |  |  |  | Arancia | 200 |  |  | 
 |  |  |  | Banana | 50 |  |  | 
 |  |  |  | Pere | 100 |  |  | 
 |  |  | Gen |  |  |  |  | 
 |  | Settimana 1 | 35 | 44 | 79 |  | Trim. 1 | 
 |  |  | 74 | 64 | 56 |  |  | 
 |  |  | 82 | 50 | 83 |  |  | 
 |  |  | 90 | 22 | 89 |  |  | 

## Sheet: 3. Dividere

I dati si trovano tutti in un'unica colonna? Dividili. |  |  |  |  |  |  | 
Passa alla cella D5. Premi CTRL+D, digita D5 e premi INVIO. Digita il nome presente nella colonna Posta elettronica nella cella C5: Olga. |  |  |  |  |  |  | 
Passa alla cella D6. Premi CTRL+E, una scelta rapida per Anteprima suggerimenti. |  |  |  |  |  |  | 
Anteprima suggerimenti determina se ciò che si digita segue uno schema uniforme e riempie le celle quando viene rilevato lo schema.  |  | Posta elettronica | Nome | Cognome |  |  | 
Ecco un altro modo per usare Anteprima suggerimenti: Passa alla cella E5. |  | Olga.Panicucci@contoso.com |  | Panicucci |  |  | 
Premi ALT+H per accedere alla scheda Home sopra la barra multifunzione, quindi premi FI per selezionare le opzioni Riempimento. Premi la freccia GIÙ per selezionare Anteprima suggerimenti nell'elenco oppure premi N. La colonna dei cognomi viene completata, nelle celle da E5 a E9. |  | Pio.Udinesi@fabrikam.com |  |  |  |  | 
Altri dettagli: Passa alla cella A27. In alternativa, per procedere al passaggio successivo, premi CTRL+PGGIÙ. |  | Albertino.Mazzanti@relecloud.com |  |  |  |  | 
 |  | Fiamma.Greco@contoso.com |  |  |  |  | 
 |  | Martina.Milani@fabrikam.com  |  |  |  |  | 
Dividere una colonna in base ai delimitatori. |  |  |  |  |  |  | 
Anteprima suggerimenti è molto utile. Ma se vuoi dividere i dati in più colonne contemporaneamente, non è lo strumento migliore per farlo. Prova Testo in colonne: |  |  |  |  |  |  | 
Passa alla cella C32. Seleziona tutte le celle da C32 a C39: da Olga fino a Martina.  |  |  |  |  |  |  | 
Premi ALT+A per accedere alla scheda Dati sopra la barra multifunzione, quindi premi CO per selezionare Testo in colonne nella sezione Strumenti dati. Viene visualizzata la finestra Conversione guidata testo in colonne - Passaggio 1 di 3. Verifica che sia selezionato il pulsante di opzione Delimitato, quindi premi INVIO. Premi TAB per spostarti nella finestra di dialogo. |  |  |  |  |  |  | 
Conversione guidata testo in colonne - Passaggio 2 di 3: premi TAB fino all'opzione Virgola in Delimitatori. Verifica che sia selezionata solo l'opzione Virgola, quindi premi TAB per selezionare Avanti e infine premi INVIO. |  | Dati | Nome | Cognome | Nome società |  | 
Conversione guidata testo in colonne - Passaggio 3 di 3: premi TAB e seleziona solo l'opzione Generale.  |  | Olga,Panicucci,Contoso Ltd. |  |  |  |  | 
Infine, premi TAB fino alla casella di testo Destinazione. Digita $D$32 e premi INVIO. |  | Pio,Udinesi,Fabrikam Inc. |  |  |  |  | 
CURIOSITÀ: C'è un altro modo per lavorare sui dati. Puoi eseguire una query su un'origine esterna e dividere i dati provenienti dall'origine. Questa operazione si esegue una volta sola, dopo di che i dati sono aggiornabili e pronti per l'uso. Vuoi provare? Seleziona la scheda Dati (ALT+A), quindi esplora le opzioni nell'area Recupera e trasforma premendo uno di questi tasti di scelta rapida: PN, FT, FW, PT, PR o X1. In alternativa, passa alla cella A80 per Altre informazioni sul Web. |  | Albertino,Mazzanti,Relecloud |  |  |  |  | 
Passa alla cella A49 per l'istruzione successiva. |  | Fiamma,Greco,Contoso Ltd. |  |  |  |  | 
 |  | Carmelo,Barese,Relecloud |  |  |  |  | 
 |  | Nazzareno,Romani,Fabrikam Inc. |  |  |  |  | 
 |  | Cataldo,Capon,Relecloud |  |  |  |  | 
 |  | Martina,Milani,Contoso Ltd. |  |  |  |  | 
Dividere una colonna con formule |  |  |  |  |  |  | 
Può essere utile scrivere una formula per dividere i dati. In questo modo, se vengono modificati i dati originali, vengono aggiornati anche i dati divisi. Si tratta di un'operazione più avanzata resa possibile da alcune funzioni: SINISTRA, DESTRA, TROVA e LUNGHEZZA. Per altre informazioni su ognuna di queste funzioni, vedi i collegamenti in fondo a questo foglio in Altre informazioni sul Web, a partire dalla cella A80. Se vuoi provare, ecco come dividere la cella C56. |  |  |  |  |  |  | 

## Sheet: 4. Trasporre

Spostare i dati con la trasposizione |  |  |  |  |  |  | 
Quando occorre ruotare le colonne e le righe, in Excel si può usare la trasposizione. |  |  |  |  |  |  | 
Le celle da C5 a H6 contengono due righe di articoli e importi. Seleziona le celle da C5 a H6. |  |  |  |  |  |  | 
Ora bisogna copiare le celle. Premi CTRL+C. |  |  |  |  |  |  | 
Seleziona la cella C9. |  | Articolo | Pane | Ciambelle | Biscotti | Torte | Crostate
Premi ALT+H per accedere alla scheda Home sopra la barra multifunzione, quindi premi V per selezionare Opzioni Incolla. Premi la freccia GIÙ oppure S per selezionare Incolla speciale.  |  | Importo | 50 | 100 | 40 | 50 | 20
Premi TAB fino all'opzione Trasponi. Premi la BARRA SPAZIATRICE per selezionare Trasponi, quindi premi INVIO. |  |  |  |  |  |  | 
L'ESPERTO SUGGERISCE: La scelta rapida da tastiera per Incolla speciale è CTRL+ALT+V. 
 |  |  |  |  |  |  | 
Altri dettagli: Vai a A27. In alternativa, per procedere al passaggio successivo, premi CTRL+PGGIÙ. |  per procedere al passaggio successivo |  |  |  |  |  | 
Trasporre con una formula |  |  |  |  |  |  | 
A volte è preferibile non copiare e incollare per trasporre. In questo caso si può usare una formula per trasporre le righe e le colonne. Ecco come fare: |  |  |  |  |  |  | 
Per trasporre questi dati, devi prima selezionare alcune celle vuote. Poiché i dati nelle celle da C33 a H34 a destra includono due righe e sei colonne, devi effettuare la selezione inversa, ovvero due colonne e sei righe. A questo scopo, seleziona le celle da C40 a D45.  |  |  |  |  |  |  | 
È piuttosto complicato, quindi presta attenzione. Con le celle ancora selezionate, digita =MATR.TRASPOSTA(C33:H34) senza premere INVIO. Premi invece CTRL+MAIUSC+INVIO. Se viene visualizzato un errore oppure #VALORE! come risultato, riprova a partire dall'istruzione nella cella A29. 
 |  |  |  |  |  |  | 
Seleziona una delle celle trasposte, ad esempio la cella C41. Osserva la formula nella parte superiore di Excel. La formula sarà simile alla seguente: {=MATR.TRASPOSTA(C33:H34)} |  |  |  |  |  |  | 
Seleziona un'altra cella trasposta dalle celle da C40 a D45, ad esempio la cella D43. Osserva di nuovo la barra della formula. La formula è uguale a quella presente nella cella C41. Perché? Perché è una formula di matrice.
 |  |  |  |  |  |  | 
Passa alla cella A54 per l'istruzione successiva. |  | Articolo | Pane | Ciambelle | Biscotti | Torte | Crostate
 |  | Importo | 50 | 100 | 40 | 50 | 20

## Sheet: 5. Ordinare e filtrare

Ordinare e filtrare facilmente |  |  |  |  |  | 
Le celle da C5 a G13 contengono cinque colonne: Reparto, Categoria e Importi per i mesi di ottobre, novembre e dicembre. |  |  |  |  |  | 
Supponiamo di voler disporre i reparti in ordine alfabetico. Seleziona la colonna Reparto, passa alla cella C5. Premi CTRL+D, digita C5 e premi INVIO. Ora premi ALT+H per accedere alla scheda Home sopra la barra multifunzione, quindi premi OR per accedere alle opzioni Ordina e filtra. Usa i tasti di direzione per trovare l'opzione Ordina dalla A alla Z, oppure premi O, quindi premi INVIO.  |  |  |  |  |  | 
Ordina gli importi di dicembre dal più grande al più piccolo. Seleziona la colonna Dicembre, quindi passa alla cella G5 e seleziona le celle da G5 a G13. Premi ALT+H per accedere alla scheda Home sopra la barra multifunzione, quindi premi OR per le opzioni Ordina e filtra. Nota che le opzioni sono cambiate da Ordina dalla A alla Z a Ordina dal più grande al più piccolo e così via. Usa i tasti di direzione per trovare l'opzione Ordina dal più grande al più piccolo, quindi premi INVIO.  |  |  |  |  |  | 
Ora filtra i dati in modo da visualizzare solo le righe Prodotti da forno. Passa alla cella G5, Dic. Premi CTRL+A per selezionare tutte le celle, quindi premi ALT+H per accedere alla scheda Home. Premi OR per accedere alle opzioni Ordina e filtra, quindi usa i tasti di direzione per trovare l'opzione Filtro oppure premi F. |  | Reparto | Categoria | Ott | Nov | Dic
Nella prima riga, nelle celle da C5 a G5, vengono visualizzati i pulsanti filtro. Passa alla cella Reparto, C5, e premi ALT+freccia GIÙ, quindi freccia GIÙ e BARRA SPAZIATRICE per deselezionare la casella di controllo Seleziona tutto. Usa quindi i tasti di direzione per trovare Prodotti da forni e premi BARRA SPAZIATRICE, poi INVIO. |  | Carne | Manzo | 90000 | 110000 | 120000
CREDITO EXTRA: Prova l'ordinamento alfabetico in base a due colonne. Ecco come: prima di tutto disponi in ordine alfabetico la colonna Reparto (vedi la procedura descritta nella cella A3 sopra). Quindi seleziona le opzioni Ordina e filtra nella scheda Home. Trova Ordinamento personalizzato e aggiungi un secondo livello per Categoria. Quando selezioni OK, la colonna Reparto viene ordinata e, all'interno di ogni reparto, anche le righe Categoria vengono disposte in ordine alfabetico.  |  | Prodotti da forno | Dolci | 25000 | 80000 | 120000
Altri dettagli: Vai a A27. In alternativa, per procedere al passaggio successivo, premi CTRL+PGGIÙ. |  | Ortofrutta | Frutta | 10000 | 30000 | 40000
 |  | Ortofrutta | Verdura | 30000 | 80000 | 30000
 |  | Gastronomia | Insalate | 90000 | 35000 | 25000
 |  | Carne | Pollo | 75000 | 82000 | 2000000
 |  | Prodotti da forno | Pane | 30000 | 15000 | 20000
 |  | Gastronomia | Sandwich | 80000 | 40000 | 20000
Ordinare per data o addirittura per colore |  |  |  |  |  | 
In Excel è possibile ordinare i dati in molti modi. Ecco altri due modi per ordinare: |  |  |  |  |  | 
Le celle da C31 a F31 contengono dati con quattro colonne: Data spesa, Dipendente, Alimentari e Hotel. |  |  |  |  |  | 
Supponiamo di voler ordinare le date delle spese. Seleziona l'intestazione Data spesa, ovvero la cella C31, premi ALT+freccia GIÙ e usa i tasti di direzione per trovare Ordina dal meno recente al più recente. Premi INVIO. Le righe vengono disposte in ordine di data crescente in base a Data spesa. |  |  |  |  |  | 
Tre celle sono già state riempite di colore giallo. Puoi ordinare le righe in base a quel colore. Passa alla cella F31, quindi premi ALT+freccia GIÙ e usa i tasti di direzione per trovare l'opzione Ordina per colore. Premere la freccia DESTRA per selezionare il colore "giallo" RGB 255, 255, 0, quindi premi INVIO. Le celle evidenziate vengono ordinate automaticamente in alto all'interno della colonna. |  | Data spesa | Dipendente | Alimentari | Hotel | 
DETTAGLIO IMPORTANTE: Non è possibile cancellare un ordinamento come accade invece con un filtro. Quindi, se non vuoi conservare l'ordinamento impostato, dovrai annullarlo premendo CTRL+Z.
 |  | 2026-02-10 00:00:00 | Fabiola | 21 | 3820 | 
Passa alla cella A43 per l'istruzione successiva. |  | 2026-02-09 00:00:00 | Marco | 62 | 2112 | 
 |  | 2026-02-06 00:00:00 | Davide | 25 | 1611 | 
 |  | 2026-02-12 00:00:00 | Isotta | 30 | 3085 | 
 |  | 2026-02-08 00:00:00 | Gerolamo | 69 | 528 | 
 |  | 2026-02-07 00:00:00 | Laura | 45 | 5050 | 
Altri modi per filtrare i dati |  |  |  |  |  | 
Le celle da C49 a F49 contengono dati con quattro colonne: Data spesa, Dipendente, Alimentari e Hotel. |  |  |  |  |  | 
Passa alla cella F49: Hotel. Premi ALT+freccia GIÙ, quindi usa i tasti di direzione per trovare l'opzione Filtri per numeri. Premi la freccia DESTRA per entrare nell'elenco Filtri per numeri e usa i tasti di direzione per trovare l'opzione Superiori alla media, quindi premi INVIO. Excel calcola l'importo medio della colonna Hotel e quindi mostra solo le righe con importi superiori a quella media.  |  |  |  |  |  | 
Ora aggiungi un secondo filtro. Passa alla cella E49: Alimentari. Premi ALT+freccia GIÙ, quindi usa i tasti di direzione per trovare l'opzione Filtri per numeri. Premi la freccia DESTRA per entrare nell'elenco Filtri per numeri. Usa i tasti di direzione per trovare l'opzione Maggiore di, quindi digita 25 e premi INVIO. Delle tre righe filtrate in precedenza perché contenenti valori superiori alla media, Excel ne mostra due con importi superiori a 25 per gli alimentari |  |  |  |  |  | 
Passa alla cella A60 per l'istruzione successiva. |  |  |  |  |  | 
 |  | Data spesa | Dipendente | Alimentari | Hotel | 
 |  | 2026-02-10 00:00:00 | Fabiola | 21 | 3820 | 

## Sheet: 6. Tabelle

Con le tabelle è tutto più facile |  |  |  |  |  |  |  | 
Una tabella offre funzionalità e vantaggi speciali. Ecco come crearne una: |  |  |  |  |  |  |  | 
Le celle da C5 a G13 contengono dati. Passa a una cella qualsiasi in quell'area, ad esempio la cella D8. Premi CTRL+D, digita D8 e premi INVIO. |  |  |  |  |  |  |  | 
Premi ALT+C per accedere alla scheda Inserisci sopra la barra multifunzione, quindi premi J e poi INVIO. In alternativa, usa la combinazione di tasti CTRL+T, quindi premi INVIO. |  |  |  |  |  |  |  | 
A questo punto hai una tabella, ossia un insieme di celle con funzionalità speciali. Per i principianti: Una tabella offre righe alternate evidenziate per semplificarne la lettura. |  | Reparto | Categoria | Ott | Nov | Dic |  | 
Puoi anche creare facilmente nuove righe. Passa alla cella vuota sotto la cella C13: Carne. Digita il testo che vuoi, quindi premi INVIO. Viene visualizzata una nuova riga per la tabella.  |  | Ortofrutta | Verdura | 30000 | 80000 | 30000 |  | 
Puoi anche creare facilmente nuove colonne: Passa a una cella qualsiasi tra H5 e H14, ad esempio H10. Digita il testo che vuoi, quindi premi INVIO. Viene visualizzata una nuova colonna per la tabella. Ripeti la procedura per aggiungere una nuova colonna nella colonna I. |  | Ortofrutta | Frutta | 10000 | 30000 | 40000 |  | 
Nota che le due colonne vengono create e formattate e viene inserito automaticamente il testo Gen e Feb nelle celle H5 e I5. |  | Prodotti da forno | Pane | 30000 | 15000 | 20000 |  | 
CREDITO EXTRA: Prova a modificare lo stile di tabella. Prima di tutto seleziona una cella nella tabella tra C5 e I14. Nella parte superiore di Excel viene visualizzata la scheda Progettazione - Strumenti tabella. Premi ALT+JN per accedere alla scheda Progettazione sopra la barra multifunzione, quindi premi S per accedere a Stili tabella. Usa i tasti di direzione per spostarti tra le opzioni e seleziona lo stile di tabella che preferisci.
 |  | Prodotti da forno | Dolci | 25000 | 80000 | 120000 |  | 
Altri dettagli: Vai a A27. In alternativa, per procedere al passaggio successivo, premi CTRL+PGGIÙ. |  | Gastronomia | Sandwich | 80000 | 40000 | 20000 |  | 
 |  | Gastronomia | Insalate | 90000 | 35000 | 25000 |  | 
 |  | Carne | Manzo | 90000 | 110000 | 200000 |  | 
 |  | Carne | Pollo | 75000 | 82000 | 150000 |  | 
Colonne calcolate nelle tabelle |  |  |  |  |  |  |  | 
Un esempio di vantaggio offerto dalle tabelle è rappresentato dalle colonne calcolate. Basta digitare una formula una sola volta e viene ricopiata automaticamente in basso. Ecco come funziona: |  |  |  |  |  |  |  | 
Le celle da C33 a H41 contengono dati con sei colonne: Reparto, Categoria, Ott, Nov, Dic e Totale. |  |  |  |  |  |  |  | 
Passa alla cella H34: Totale. |  |  |  |  |  |  |  | 
Premi ALT+= e quindi premi INVIO. |  |  |  |  |  |  |  | 
La formula SOMMA viene ricopiata automaticamente in basso, per cui non è necessario farlo manualmente.  |  |  |  |  |  |  |  | 
Passa alla cella A47 per l'istruzione successiva. |  | Reparto | Categoria | Ott | Nov | Dic | Totale | 
 |  | Ortofrutta | Verdura | 30000 | 80000 | 30000 |  | 
 |  | Ortofrutta | Frutta | 10000 | 30000 | 40000 |  | 
 |  | Prodotti da forno | Pane | 30000 | 15000 | 20000 |  | 
 |  | Prodotti da forno | Dolci | 25000 | 80000 | 120000 |  | 
 |  | Gastronomia | Sandwich | 80000 | 40000 | 20000 |  | 
 |  | Gastronomia | Insalate | 90000 | 35000 | 25000 |  | 
 |  | Carne | Manzo | 90000 | 110000 | 200000 |  | 
 |  | Carne | Pollo | 75000 | 82000 | 150000 |  | 
Righe dei totali nelle tabelle |  |  |  |  |  |  |  | 
Un altro vantaggio delle tabelle è costituito dalle righe dei totali. Invece di digitare una formula SOMMA, Excel può calcolare il totale in modo automatico. E questo vale anche per la formula MEDIA e molte altre. Ecco come funziona: |  |  |  |  |  |  |  | 
Le celle da C53 a E61 contengono dati con tre colonne: Reparto, Categoria e Vendite. |  |  |  |  |  |  |  | 
Passa a una cella qualsiasi nell'intervallo soprastante, ad esempio la cella D57. |  |  |  |  |  |  |  | 

## Sheet: 7. Elenchi a discesa

Inserire un elenco a discesa |  |  |  |  | 
Gli elenchi a discesa semplificano l'immissione dei dati. Ecco come crearne uno:  |  |  |  |  | 
Le celle da C3 a D15 contengono dati con due colonne: Alimentari e Reparto. |  | Alimentari | Reparto |  | 
Per ognuno degli alimentari a destra devono essere validi solo tre nomi di reparto. I reparti sono Ortofrutta, Carne e Prodotti da forno. |  | Mele |  |  | 
Passa alla cella D4. Premi CTRL+D, digita D4 e premi INVIO. Seleziona tutte le celle da D4 a D15. |  | Manzo |  |  | 
Nella scheda Dati seleziona Convalida dati oppure premi ALT+DL per aprire la finestra di dialogo Convalida dati. Premi TAB fino a Consenti e seleziona Elenco. Premi di nuovo TAB. |  | Banane |  |  | 
Nella casella di testo Origine digita Ortofrutta, Carne, Prodotti da forno. Verifica che i nomi siano separati da una virgola. Al termine, premi INVIO. |  | Limoni |  |  | 
Ora seleziona la cella D4, ovvero la cella accanto a Mele in C4. Premi ALT+freccia GIÙ. Viene visualizzato un menu a discesa con le tre voci appena aggiunte: Ortofrutta, Carne e Prodotti da forno. |  | Broccoli |  |  | 
INFORMAZIONI UTILI: Gli elenchi a discesa contribuiscono a garantire che vengano immessi dati validi. Per questo motivo fanno parte di un gruppo più ampio di funzionalità noto come convalida dei dati. 
Esistono altri metodi di convalida dei dati. Ad esempio, è possibile limitare l'immissione a numeri interi, date o persino importi minimi e massimi. Le opzioni a disposizione sono molte. Per saperne di più, seleziona il collegamento nella cella A61. |  | Verza |  |  | 
Altri dettagli: Vai a A27. In alternativa, per procedere al passaggio successivo, premi CTRL+PGGIÙ. |  | Prosciutto |  |  | 
 |  | Pane |  |  | 
 |  | Pollo |  |  | 
 |  | Biscotti |  |  | 
 |  | Torte |  |  | 
 |  | Crostate |  |  | 
Procedura consigliata per gli elenchi a discesa: usare una tabella. |  |  |  |  | 
Fin qui hai imparato a inserire un menu a discesa per l'elenco dei reparti. Ma cosa succede se l'elenco cambia? Ad esempio, cosa accadrebbe se venisse aggiunto un nuovo reparto chiamato Latticini? In questo caso occorrerebbe aggiornare la finestra di dialogo Convalida dati. Esiste però un modo più efficiente, creando prima una tabella: |  |  |  |  | 
Le celle da C31 a D43 contengono dati con due colonne: Alimentari e Reparto. Le celle da F31 a F34 contengono dati con una colonna: Reparto. |  |  |  |  | 
Nell'intervallo tra F31 e F34 seleziona una cella con un reparto. Ad esempio, seleziona la cella F33: Carne.  |  |  |  |  | 
Per creare una tabella, premi CTRL+T, quindi INVIO. |  | Alimentari | Reparto |  | Reparto
Ora occorre configurare di nuovo la convalida dei dati. Sotto la cella D31, Reparto, seleziona tutte le celle vuote da D32 a D43. |  | Mele |  |  | Ortofrutta
Nella scheda Dati seleziona Convalida dati oppure premi ALT+DL per aprire la finestra di dialogo Convalida dati. Premi TAB fino a Consenti e premi la freccia GIÙ per selezionare Elenco. Premi di nuovo TAB. |  | Manzo |  |  | Carne
Nella casella di testo Origine digita =$F$32:$F$34, quindi premi INVIO. |  | Banane |  |  | Prodotti da forno
Sono stati selezionati i valori nella colonna singola a partire dalla cella F31: Reparto. |  | Limoni |  |  | 
Passa alla cella D32 e premi ALT+freccia GIÙ. L'elenco a discesa include solo tre reparti: Ortofrutta, Carne e Prodotti da forno. Se però aggiungi un nuovo reparto nella colonna F sotto la cella F35, Prodotti da forno, questo elenco verrà aggiornato con la nuova categoria. Prova. |  | Broccoli |  |  | 
L'ESPERTO SUGGERISCE: Spesso gli elenchi di convalida come questo vengono collocati in una scheda separata. In questo modo si evita che gli altri utenti abbiano la tentazione di modificare un elenco.
 |  | Verza |  |  | 
Passa alla cella A60 per l'istruzione successiva. |  | Prosciutto |  |  | 
 |  | Pane |  |  | 
 |  | Pollo |  |  | 
 |  | Biscotti |  |  | 
 |  | Torte |  |  | 
 |  | Crostate |  |  | 

## Sheet: 8. Analizzare

Analizzare rapidamente i dati |  |  |  |  |  | 
Ecco come analizzare i dati in modo da individuare rapidamente schemi e tendenze: |  |  |  |  |  | 
Le celle da C5 a G13 contengono dati in cinque colonne: Reparto, Categoria, Ott, Nov e Dic. |  |  |  |  |  | 
Passa a una cella nella tabella tra le celle C5 e G13, ad esempio la cella E9, quindi premi CTRL+Q. Viene visualizzato un riquadro Analisi rapida. |  |  |  |  |  | 
Premi TAB per accedere alle opzioni Formattazione, quindi premi INVIO per selezionare Barre dei dati. |  | Reparto | Categoria | Ott | Nov | Dic
Nelle celle delle colonne Ott, Nov e Dic, ovvero le celle da E6 a G13, vengono inserite speciali barre dei dati che visualizzano i relativi importi. |  | Ortofrutta | Verdura | 30000 | 80000 | 30000
Supponiamo di voler eliminare le barre dei dati. Seleziona l'intero intervallo di celle da C5 a G13, quindi premi CTRL+Q per visualizzare nuovamente il riquadro Analisi rapida. |  | Ortofrutta | Frutta | 10000 | 30000 | 40000
Premi TAB per accedere alle opzioni Formattazione, premi la freccia DESTRA per trovare Cancella, quindi premi INVIO. |  | Prodotti da forno | Pane | 30000 | 15000 | 20000
INFORMAZIONI UTILI: Quando si selezionano celle, viene visualizzato questo pulsante Analisi rapida. Nome perfetto, non credi? Puoi accedere a questo pulsante in qualsiasi momento usando la combinazione di tasti CTRL+Q. Se hai una domanda sui dati selezionati, seleziona questa opzione e vedi se ti offre qualche risposta.  |  | Prodotti da forno | Dolci | 25000 | 80000 | 120000
Altri dettagli: Vai a A27. In alternativa, per procedere al passaggio successivo, premi CTRL+PGGIÙ. |  | Gastronomia | Sandwich | 80000 | 40000 | 20000
 |  | Gastronomia | Insalate | 90000 | 35000 | 25000
 |  | Carne | Manzo | 90000 | 110000 | 200000
 |  | Carne | Pollo | 75000 | 82000 | 150000
Creare rapidamente un grafico |  |  |  |  |  | 
Per creare un grafico è sempre possibile usare la scheda Inserisci. In alternativa, puoi anche usare l'opzione Analisi rapida. Questa volta, però, useremo la scelta rapida da tastiera: |  |  |  |  |  | 
Le celle da C34 a G42 contengono dati con cinque colonne: Reparto, Categoria, Ott, Nov e Dic. |  |  |  |  |  | 
Passa a una cella nella tabella tra le celle C34 e G42, ad esempio la cella D38, quindi premi CTRL+Q. |  |  |  |  |  | 
Viene visualizzato il riquadro Analisi rapida. Premi la freccia DESTRA fino a Grafici. |  |  |  |  |  | 
Premi TAB per accedere alle opzioni Grafici e INVIO per selezionare il pulsante che inizia con Colonne. |  |  |  |  |  | 
Viene visualizzato e selezionato un nuovo istogramma a colonne raggruppate. Usa i tasti di direzione per spostarlo nella posizione che preferisci. Per ogni prodotto sono presenti tre colonne nel grafico, una per ogni mese di vendita: Ott, Nov e Dic. |  |  |  |  |  | 
Passa alla cella A47 per l'istruzione successiva. |  | Reparto | Categoria | Ott | Nov | Dic
 |  | Prodotti da forno | Pane | 30000 | 15000 | 20000
 |  | Prodotti da forno | Dolci | 25000 | 80000 | 120000
 |  | Gastronomia | Sandwich | 80000 | 40000 | 20000
 |  | Gastronomia | Insalate | 90000 | 35000 | 25000
 |  | Carne | Manzo | 90000 | 110000 | 200000
 |  | Carne | Pollo | 75000 | 82000 | 150000
 |  | Ortofrutta | Verdura | 30000 | 80000 | 30000
 |  | Ortofrutta | Frutta | 10000 | 30000 | 40000
Creare rapidamente grafici sparkline |  |  |  |  |  | 
Supponiamo di voler visualizzare linee di tendenza a destra dei dati per mostrare l'andamento degli importi nel corso dei tre mesi. Non è necessario creare 8 piccoli grafici a linee. Ciò che ti serve sono i grafici sparkline. |  |  |  |  |  | 
Le celle da C54 a G62 contengono dati con cinque colonne: Reparto, Categoria, Ott, Nov e Dic. |  |  |  |  |  | 
Passa a una cella all'interno della tabella tra C55 e G62 e quindi premi CTRL+Q. |  |  |  |  |  | 

## Sheet: 9. Grafici

Grafici eccellenti, consigliati per te |  |  |  |  | 
Le celle da C5 a D11 contengono dati con due colonne: Anno e Partecipazione a conferenza. |  |  |  |  | 
Passa a una cella qualsiasi della tabella tra C5 e D11, ad esempio C6. Premi CTRL+D, digita C6 e premi INVIO. |  |  |  |  | 
Premi ALT+C per accedere alla scheda Inserisci sopra la barra multifunzione. Premi K per visualizzare le opzioni Grafici consigliati. |  |  |  |  | 
Verranno visualizzati alcuni suggerimenti. Premi TAB per accedere all'elenco e usa i tasti di direzione per trovare un'opzione denominata Colonne raggruppate, quindi premi INVIO. |  | Anno | Partecipazione a conferenza |  | 
Viene visualizzato un istogramma che mostra il numero totale di partecipanti a conferenze per anno. Usa i tasti di direzione per spostare il grafico nella posizione che preferisci. |  | 2021 | 500 |  | 
Ora puoi aggiungere una linea di tendenza. Seleziona il grafico appena creato e premi ALT+JG per accedere alla scheda Progettazione - Strumenti grafico sopra la barra multifunzione.  |  | 2022 | 800 |  | 
Premi A per selezionare Aggiungi elemento grafico e quindi premi la freccia GIÙ per trovare l'opzione Linea di tendenza. Premi la freccia DESTRA per aprire le opzioni Linea di tendenza, quindi la freccia GIÙ per passare all'opzione Lineare e quindi premi INVIO. Ora hai una linea di tendenza che mostra la direzione generale delle unità vendute nel tempo. |  | 2023 | 1000 |  | 
CREDITO EXTRA: Vuoi inserire una tabella di dati direttamente sotto il grafico? Seleziona il grafico. Premi ALT+JG per accedere alla scheda Progettazione - Strumenti grafico. Premi A per selezionare Aggiungi elemento grafico. Premi la freccia GIÙ per trovare l'opzione Tabella dati, quindi premi la freccia DESTRA per aprire le opzioni Tabella dati. Premi la freccia GIÙ fino all'opzione Con chiavi legenda. Seleziona Con chiavi legenda e premi INVIO per aggiungere le chiavi della legenda al grafico.
 |  | 2024 | 900 |  | 
Altri dettagli: Vai a A27. In alternativa, per procedere al passaggio successivo, premi CTRL+PGGIÙ. |  | 2025 | 1000 |  | 
 |  | 2026 | 1200 |  | 
Assi orizzontale e asse verticale |  |  |  |  | 
A scuola ci hanno insegnato che esiste un asse X e un asse Y. Questi due assi sono presenti anche in Excel, ma hanno nomi leggermente diversi.  |  |  |  |  | 
Ecco come si chiamano in Excel: |  |  |  |  | 
• L'asse X lungo la parte inferiore è detto asse orizzontale.  |  |  |  |  | 
• L'asse Y che procede verso l'alto e verso il basso è detto asse verticale.  |  |  |  |  | 
Ogni asse può essere un asse dei valori o un asse delle categorie.  |  |  |  |  | 
• Un asse dei valori rappresenta valori numerici. Ad esempio, può rappresentare dollari, ore, durata, temperatura e così via. L'asse verticale nel grafico a destra a partire dalla cella D30 è un asse dei valori.  |  |  |  |  | 
• Un asse delle categorie rappresenta elementi come date, nomi di persone o nomi di prodotti. L'asse orizzontale nel grafico a destra a partire dalla cella D30 indica gli anni, quindi è un asse delle categorie.  |  |  |  |  | 
Passa alla cella A52 per l'istruzione successiva. |  |  |  |  | 

## Sheet: 10. Tabelle pivot

Riepilogare i dati con le tabelle pivot |  |  |  |  |  | 
Le celle da C3 a F9 contengono dati con quattro colonne: Data, Venditore, Prodotto e Importo. |  |  |  |  |  | 
Esamina le colonne Data, Venditore, Prodotto e Importo. Riesci a identificare rapidamente il prodotto più redditizio? O il venditore che ha raggiunto i risultati migliori? Le tabelle pivot nelle celle da E11 a F15 servono proprio a questo. |  | Data | Venditore | Prodotto | Importo | 
Quando abbiamo creato la tabella pivot, abbiamo fatto clic su alcuni pulsanti per riepilogare i dati. Ora sappiamo qual è il prodotto più redditizio.  |  | 2025-12-17 00:00:00 | Anna | Birra | 1400 | 
A questo punto eseguirai il pivot dei dati per trovare il venditore che ha raggiunto i risultati migliori. Premi CTRL+D, digita E12 e premi INVIO. La selezione è all'interno della tabella pivot.  |  | 2025-12-22 00:00:00 | Marco | Vino | 1010 | 
Premi MAIUSC+F6 fino a entrare nel riquadro Campi tabella pivot. Se il riquadro non è aperto, premi ALT+JT, quindi N per aprire il riquadro Campi tabella pivot. Lo stato attivo passa al campo di testo Cerca: "Digitare le parole da cercare". Premi TAB fino ad arrivare al pulsante Prodotto. Premi la BARRA SPAZIATRICE per accedere al menu contestuale, quindi premi la freccia GIÙ fino a Rimuovi campo. Premi INVIO.  |  | 2026-01-08 00:00:00 | Anna | Birra | 750 | 
Ora premi TAB finché non accedi all'elenco delle categorie: Data, Venditore, Prodotto e Importo. Usare le frecce per trovare la casella di controllo Venditore. Premi BARRA SPAZIATRICE per aggiungere il campo agente Venditore. Quindi, premi MAIUSC+F6 fino ad accedere alla tabella EsempioTabellaPivot. Passa alla cella F12. Il venditore che ha raggiunto i risultati migliori è Anna, con 2.150. |  | 2026-01-12 00:00:00 | Marco | Bibite | 510 | 
Altri dettagli: Vai a A27. In alternativa, per procedere al passaggio successivo, premi CTRL+PGGIÙ. |  | 2026-02-01 00:00:00 | Fiamma | Bibite | 1600 | 
 |  | 2026-02-12 00:00:00 | Laura | Vino | 680 | 
 |  |  |  | Etichette di riga | Somma di Importo | 
 |  |  |  | Birra | 2150 | 
 |  |  |  | Bibite | 2110 | 
 |  |  |  | Vino | 1690 | 
 |  |  |  | Totale complessivo | 5950 | 
Creare una tabella pivot |  |  |  |  |  | 
Ora creerai autonomamente una tabella pivot. Così saprai farlo se ti dovesse servire in futuro per riepilogare i dati. |  |  |  |  |  | 
Le celle da C34 a F40 contengono dati con quattro colonne: Data, Venditore, Prodotto e Importo. |  |  |  |  |  | 
Seleziona una cella all'interno della tabella. Ad esempio passa alla cella E38 e quindi premi ALT+JN per accedere al menu Progettazione sopra la barra multifunzione. Premi V per inserire una tabella pivot. |  |  |  |  |  | 
Viene visualizzata una finestra di dialogo Crea tabella pivot. Lo stato attivo è su Seleziona tabella o intervallo. Lasciare selezionato questo pulsante di opzione, premi TAB per specificare dove collocare il rapporto di tabella pivot. È selezionata l'opzione predefinita: Nuovo foglio di lavoro. Premi la freccia GIÙ per selezionare Foglio di lavoro esistente. Premi TAB per entrare nella casella di testo Posizione e digita C42, quindi premi INVIO. |  |  |  |  |  | 
A destra viene visualizzato il riquadro Campi tabella pivot. Premi MAIUSC+F6 fino alla casella Cerca: Digita le parole da cercare per la modifica.  |  |  |  |  |  | 
Premi TAB per passare all'elenco delle categorie. Premi la freccia GIÙ per trovare la casella di controllo Prodotto. Premi la BARRA SPAZIATRICE per selezionare Prodotto.
In questo modo, il campo Prodotto viene aggiunto all'area Righe in fondo al riquadro. Inoltre, i dati relativi al prodotto vengono aggiunti come etichette di riga nella nuova tabella pivot. |  |  |  |  |  | 
Ora premi la freccia GIÙ per trovare la casella di controllo Importo. 
In questo modo, il campo Importo viene aggiunto all'area Valori in fondo al riquadro. Allo stesso tempo vengono calcolati i totali degli importi per ogni prodotto nella tabella pivot.
 |  | Data | Venditore | Prodotto | Importo | 
Ecco fatto. Hai creato una tabella pivot. Ci sono però molte altre cose che puoi fare. Passa alla cella A60 per saperne di più. |  | 2025-12-17 00:00:00 | Anna | Birra | 1400 | 
Passa alla cella A58 per l'istruzione successiva. |  | 2025-12-22 00:00:00 | Marco | Vino | 1010 | 
 |  | 2026-01-08 00:00:00 | Anna | Birra | 750 | 
 |  | 2026-01-12 00:00:00 | Marco | Bibite | 510 | 
 |  | 2026-02-01 00:00:00 | Fiamma | Bibite | 1600 | 
 |  | 2026-02-12 00:00:00 | Laura | Vino | 680 | 

## Sheet: Altre informazioni

Altre domande su Excel? | 
Premi ALT+Q e digita cosa che vuoi sapere. | 
Vai avanti. Sono disponibili altre risorse su Excel: | 
Community: Invia domande e mettiti in contatto con altri appassionati di Excel.
 | 
Altre novità?
Gli abbonati a Office 365 ricevono costantemente aggiornamenti e nuove funzionalità.

 | 
