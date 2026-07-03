# Excel - Tutorial sulle formule

**File:** `Excel - Tutorial sulle formule.xlsx`
**Tipo:** `.xlsx`
**Dimensione:** 447.2 KB
**Ultima modifica:** 02/07/2026 09:24

---

## Sheet: Inizio

Guida introduttiva alle formule
Bastano pochi semplici passaggi per iniziare a creare formule e funzioni in Excel, l'app per fogli di calcolo 
più famosa al mondo.
Per tornare all'inizio, premi CTRL+HOME. Per iniziare il tour, premi CTRL+PGGIÙ.
#VALUE!

## Sheet: Concetti di base

Concetti di base: matematica con Excel |  |  |  |  |  |  |  |  |  |  |  |  | 
In Excel si può sommare, sottrarre, moltiplicare e dividere senza usare le funzioni predefinite. Basta usare alcuni operatori di base: +, -, *, /. Tutte le formule iniziano con un segno di uguale (=).
 |  | Numeri da usare: |  | Operazione: | Formule: | Risposte: |  |  |  |  |  |  | 
Per sommare, seleziona la cella F3, digita =C3+C4, quindi premi INVIO. 
 |  | 1 |  | Addizione (+)  |  | 3 |  |  |  |  |  |  | 
Per sottrarre, seleziona la cella F4, digita =C3-C4, quindi premi INVIO.  |  | 2 |  | Sottrazione (-)  |  | -1 |  |  |  |  |  |  | 
Per moltiplicare, seleziona la cella F5, digita =C3*C4, quindi premi INVIO.
 |  |  |  | Moltiplicazione (*)  |  | 2 |  |  |  |  |  |  | 
Per dividere, seleziona la cella F6, digita =C3/C4, quindi premi INVIO.
 |  |  |  | Divisione (/)  |  | 0.5 |  |  |  |  |  |  | 
Prova: cambia i numeri nelle celle C3 e C4 e osserva come i risultati delle formule cambiano automaticamente. |  |  |  | Potenza (^)  |  | 1 |  |  |  |  |  |  | 
CREDITO EXTRA: Per elevare un valore a una potenza, usa il simbolo dell'accento circonflesso (^), ad esempio =A1^A2. Per immetterlo, premi MAIUSC+ì. Nella cella F7 immetti =C3^C4. |  |  |  |  |  |  |  |  |  |  |  |  | 
Altri dettagli |  |  |  |  |  |  |  |  |  |  |  |  | 
Passaggio successivo |  |  |  |  |  |  |  |  |  |  |  |  | 
Altre informazioni su formule, celle e intervalli |  |  |  |  |  |  |  |  |  |  |  |  | 
Excel è costituito da singole celle raggruppate in righe e colonne. Le righe sono numerate, le colonne sono identificate da lettere. Sono presenti più di 1 milione di righe e 16.000 colonne e si possono inserire formule in qualsiasi di esse. 
 |  |  |  |  |  |  |  |  |  |  |  |  | 
Le formule possono contenere riferimenti di cella, intervalli di riferimenti di cella, operatori e costanti. Ecco alcuni esempi di formule:

=A1+B1
=10+20
=SOMMA(A1:A10)

 |  |  |  |  |  |  |  |  |  |  |  |  | 
Nel terzo esempio abbiamo usato la funzione SOMMA. Una funzione è un comando predefinito che prende uno o più valori, li calcola in un certo modo e restituisce un risultato. Ad esempio, la funzione SOMMA prende i riferimenti di cella o gli intervalli di celle specificati e ne calcola il totale. In questo esempio prende le celle da A1 a A10 e ne calcola il totale. Excel include più di 400 funzioni, disponibili nella scheda Formule.
 |  |  |  |  |  |  |  |  |  |  |  |  | 
Le formule con funzioni iniziano con un segno di uguale, seguito dal nome della funzione con i relativi argomenti (i valori usati dalla funzione per il calcolo) racchiusi tra parentesi. 
 |  |  |  |  |  |  |  |  |  |  |  |  | 
Per confermare una formula bisogna premere INVIO. A questo punto viene eseguito il calcolo della formula e nella cella viene visualizzato il risultato. Per vedere la formula vera e propria, osserva la barra della formula sotto la barra multifunzione oppure premi F2 per attivare la modalità di modifica, che consente di visualizzare la formula nella cella. Premi di nuovo INVIO per completare la formula e calcolare il risultato.

 |  |  |  |  |  |  |  |  |  |  |  |  | 
Alcune spiegazioni sulle formule |  |  |  |  |  |  |  |  |  |  |  |  | 
=10+20 è una formula in cui 10 e 20 sono costanti e il segno + è l'operatore. |  |  |  |  |  |  |  |  |  |  |  |  | 
=SOMMA(A1:A10) è una formula in cui SOMMA è il nome della funzione, le parentesi di apertura e chiusura racchiudono gli argomenti della formula e A1:A10 è l'intervallo di celle per la funzione. |  |  |  |  |  |  |  |  |  |  |  |  | 
=SOMMA(A1:A10;C1:C10) è una formula in cui SOMMA è il nome della funzione, le parentesi di apertura e chiusura racchiudono gli argomenti della formula e A1:A10;C1:C10 sono gli intervalli di celle per la funzione separati da un punto e virgola. |  |  |  |  |  |  |  |  |  |  |  |  | 
INFORMAZIONI UTILI: Le costanti sono i valori che vengono immessi nelle celle o nelle formule. Anche se =10+20 può produrre lo stesso risultato di =A1+B1, è buona norma evitare le costanti. Perché? Poiché per vedere una costante può essere necessario selezionare la cella e cercarla. Di conseguenza può risultare difficile da cambiare in un secondo momento. È molto più semplice inserire le costanti nelle celle, dove possono essere modificate facilmente e aggiunte alle formule mediante riferimento.

Ad esempio: seleziona la cella gialla con il numero 12 qui sotto. Come vedi, abbiamo usato la funzione SOMMA con un intervallo di celle. Non abbiamo digitato "4" o "8" direttamente nella formula. 
 |  |  |  |  |  |  |  |  |  |  |  |  | 
Indietro |  |  |  |  |  |  |  |  |  |  |  |  | 
Avanti |  |  |  |  |  |  |  |  |  |  |  |  | 
Altre informazioni sul Web |  |  |  |  |  |  |  |  |  |  |  |  | 
Usare Excel come calcolatrice |  |  |  |  |  |  |  |  |  |  |  |  | 
Panoramica delle formule in Excel |  |  |  |  |  |  |  |  |  |  |  |  | 
Funzioni di Excel (in base alla categoria)  |  |  |  |  |  |  |  |  |  |  |  |  | 
Funzioni di Excel (in ordine alfabetico)  |  |  |  |  |  |  |  |  |  |  |  |  | 
Formazione gratuita su Excel disponibile online |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  | Valori |  |  |  | 
 |  |  |  |  |  |  |  |  | 4 |  |  |  | 
 |  |  |  |  |  |  |  |  | 8 |  |  |  | 
 |  |  |  |  |  |  |  |  | 12 |  |  |  | 

## Sheet: Introduzione alle funzioni

Introduzione alle funzioni |  |  |  |  |  |  |  |  |  |  |  | 
Con le funzioni si possono svolgere molte azioni, ad esempio eseguire operazioni matematiche, cercare valori o persino calcolare date e ore. Proviamo a sommare valori in diversi modi con la funzione SOMMA. |  | Frutta | Quantità |  | Carne | Quantità |  |  |  |  |  | 
Nella colonna Quantità per Frutta (cella D7), immetti =SOMMA(D3:D6) oppure digita =SOMMA( e seleziona l'intervallo con il mouse, quindi premi INVIO. Vengono sommati i valori presenti nelle D3, D4, D5 e D6. La risposta dovrebbe essere 170.
 |  | Mele | 50 |  | Manzo | 50 |  |  |  |  |  | 
Ora proviamo Somma automatica. Seleziona la cella sotto la colonna relativa a Carne (cella G7), quindi passa a Formule > Somma automatica e seleziona SOMMA. La formula verrà inserita automaticamente. Premi INVIO per confermarla. La funzionalità Somma automatica ha tutte le funzioni più comuni.
 |  | Arance | 20 |  | Pollo | 30 |  |  |  |  |  | 
Ecco una scelta rapida da tastiera specifica. Seleziona la cella D15, premi ALT= e quindi INVIO. La funzione SOMMA viene immessa automaticamente. |  | Banane | 60 |  | Maiale | 10 |  |  |  |  |  | 
Altri dettagli |  | Limoni | 40 |  | Pesce | 50 |  |  |  |  |  | 
CREDITO EXTRA
Prova a usare la funzione CONTA.NUMERI con uno dei metodi già sperimentati. La funzione CONTA.NUMERI conta il numero di celle che contengono numeri all'interno di un intervallo. |  | SOMMA >  | 170 |  | SOMMA >  |  |  |  |  |  |  | 
Passaggio successivo |  |  |  |  |  |  |  |  |  |  |  | 
Altre informazioni sulle funzioni |  | Articolo | Quantità |  | Articolo | Quantità |  |  |  |  |  | 
Passa alla scheda Formule e scorri la Libreria di funzioni, in cui le funzioni sono elencate per categoria, ad esempio Testo, Data e ora e così via. Inserisci funzione consente di cercare le funzioni per nome e avviare una procedura guidata per creare la formula. 

Quando inizi a digitare il nome di una funzione dopo aver premuto =, Excel avvia Intellisense, che elenca tutte le funzioni che iniziano con le lettere digitate. Quando trovi quella che vuoi, premi TAB. Excel completa automaticamente il nome della funzione e inserisce la parentesi di apertura. Mostra anche gli argomenti facoltativi e obbligatori. 



Esaminiamo in dettaglio alcune funzioni. La funzione SOMMA è strutturata in questo modo: |  | Pane | 50 |  | Pane | 50 |  |  |  |  |  | 
Se la funzione SOMMA potesse parlare, direbbe: "Restituisci la somma di tutti i valori nelle celle da D35 a D38 e tutta la colonna H". SOMMA è il nome della funzione, D35:D38 è il primo argomento intervallo, che in genere è necessario, e H:H è il secondo argomento intervallo; i due sono separati da una virgola. Ora proviamone una che non richiede argomenti.
 |  | Ciambelle | 100 |  | Ciambelle | 100 |  |  |  |  |  | 
La funzione OGGI restituisce la data corrente. Viene aggiornata automaticamente quando Excel ricalcola. |  | Biscotti | 40 |  | Biscotti | 40 |  |  |  |  |  | 
GUARDA QUI
Seleziona queste celle. Nell'angolo in basso a destra della finestra di Excel troverai SOMMA: 170 nella barra inferiore. Si chiama Barra di stato e rappresenta semplicemente un altro modo per trovare rapidamente un totale e altri dettagli su una cella o un intervallo.  |  | Torte | 50 |  | Torte | 50 |  |  |  |  |  | 
DETTAGLIO IMPORTANTE
Fai doppio clic in questa cella. Noterai il valore 100 verso la fine. Anche se è possibile inserire numeri in una formula come questa, non è consigliabile farlo a meno che non sia assolutamente necessario. Si tratta di un valore costante ed è facile dimenticarsi della sua presenza. È preferibile fare riferimento a un'altra cella, come la cella F51. In questo modo sarà più visibile e non nascosto all'interno di una formula.  |  | Crostate | 20 |  | Crostate | 20 |  |  |  |  |  | 
Altre informazioni sul Web |  | SOMMA >  |  |  | CONTA.NUMERI > |  |  |  |  |  |  | 
Informazioni complete sulla funzione SOMMA |  |  |  |  |  |  |  |  |  |  |  | 
Usare Somma automatica per sommare numeri |  |  |  |  |  |  |  |  |  |  |  | 
Informazioni complete sulla funzione CONTA.NUMERI |  |  |  |  |  |  |  |  |  |  |  | 
Formazione gratuita su Excel disponibile online |  |  |  |  |  |  |  |  |  |  |  | 
Torna all'inizio |  |  |  |  |  |  |  |  |  |  |  | 
Passaggio successivo |  |  |  |  |  |  |  |  |  |  |  | 
 |  | Frutta | Quantità |  |  |  |  |  |  |  |  | 
 |  | Mele | 50 |  |  |  |  |  |  |  |  | 
 |  | Arance | 20 |  |  |  |  |  |  |  |  | 
 |  | Banane | 60 |  |  |  |  |  |  |  |  | 
 |  | Limoni | 40 |  |  |  |  |  |  |  |  | 
 |  | SOMMA >  | 170 |  |  |  |  |  |  |  |  | 
 |  | Articolo | Quantità |  |  |  |  |  |  |  |  | 
 |  | Automobili | 20 |  |  |  |  |  |  |  |  | 
 |  | Autocarri | 10 |  |  |  |  |  |  |  |  | 
 |  | Biciclette | 10 |  |  |  |  |  |  |  |  | 
 |  | Pattini | 40 |  |  |  |  |  |  |  |  | 
 |  |  | Totale: |  | Valore aggiuntivo | Nuovo totale |  |  |  |  |  | 

## Sheet: MEDIA

Funzione MEDIA |  |  |  |  |  |  |  |  | 
La funzione MEDIA consente di ottenere la media dei numeri in un intervallo di celle. |  | Frutta | Quantità |  | Carne | Quantità |  |  | 
Seleziona la cella D7, quindi usa Somma automatica per aggiungere una funzione MEDIA. |  | Mele | 50 |  | Manzo | 50 |  |  | 
Ora seleziona la cella G7 e immetti una funzione MEDIA digitando =MEDIA(G3:G6).  |  | Arance | 20 |  | Pollo | 30 |  |  | 
Nella cella D15 puoi usare la creazione guidata Somma automatica oppure immettere manualmente una funzione MEDIA.  |  | Banane | 60 |  | Maiale | 10 |  |  | 
GUARDA QUI
Seleziona un intervallo di numeri, quindi osserva la media immediata riportata sulla barra di stato.
 |  | Limoni | 40 |  | Pesce | 50 |  |  | 
Attiva il foglio precedente |  | MEDIA > |  |  | MEDIA > |  |  |  | 
Vai al foglio successivo |  |  |  |  |  |  |  |  | 
CREDITO EXTRA
Prova a usare MEDIANA o MODA qui. 

MEDIANA fornisce il valore mediano del set di dati, mentre 
MODA fornisce quello con più occorrenze.
 |  | Articolo | Quantità |  | Articolo | Quantità |  |  | 
Collegamenti ad altre informazioni sul Web |  | Pane | 50 |  | Pane | 50 |  |  | 
Seleziona per ottenere informazioni complete dal Web sulla funzione MEDIA |  | Ciambelle | 100 |  | Ciambelle | 100 |  |  | 
Seleziona per ottenere informazioni complete dal Web sulla funzione MEDIANA |  | Biscotti | 40 |  | Biscotti | 40 |  |  | 
Seleziona per ottenere informazioni complete dal Web sulla funzione MODA |  | Torte | 50 |  | Torte | 50 |  |  | 
Seleziona per ottenere informazioni sulle risorse di formazione gratuita su Excel sul Web |  | Crostate | 20 |  | Crostate | 20 |  |  | 
 |  | MEDIA > |  |  |  |  |  |  | 

## Sheet: MIN e MAX

Funzioni MIN e MAX |  |  |  |  |  |  | 
La funzione MIN consente di ottenere il numero minimo in un intervallo di celle. |  | Frutta | Quantità |  | Carne | Quantità | 
La funzione MAX consente di ottenere il numero massimo in un intervallo di celle. |  | Mele | 50 |  | Manzo | 50 | 
Seleziona la cella D7, quindi usa la procedura guidata Somma automatica per aggiungere una funzione MIN.
 |  | Arance | 20 |  | Pollo | 30 | 
Ora seleziona la cella G7 e immetti una funzione MAX digitando =MAX(G3:G6).
 |  | Banane | 60 |  | Maiale | 10 | 
Nella cella D15 puoi usare la creazione guidata Somma automatica oppure immettere manualmente una funzione MIN o MAX. 
 |  | Limoni | 40 |  | Pesce | 50 | 
Altre informazioni sul Web
 |  | MIN > |  |  | MAX > |  | 
Informazioni complete sulla funzione MIN |  |  |  |  |  |  | 
Informazioni complete sulla funzione MAX |  | Articolo | Quantità |  | Articolo | Quantità | 
Formazione gratuita su Excel disponibile online |  | Pane | 50 |  | Pane | 50 | 
INFORMAZIONI UTILI
È possibile usare MIN o MAX con più intervalli o valori per visualizzare il maggiore o il minore di tali valori, ad esempio =MIN(A1:A10;B1:B10) oppure =MAX(A1:A10;B1), dove B1 contiene un valore soglia, come 10, nel qual caso la formula non restituirebbe mai un risultato inferiore a 10.
 |  | Ciambelle | 100 |  | Ciambelle | 100 | 
 |  | Biscotti | 40 |  | Biscotti | 40 | 
 |  | Torte | 50 |  | Torte | 50 | 
 |  | Crostate | 20 |  | Crostate | 20 | 
 |  | MIN o MAX > |  |  |  | 10 | 
È possibile usare MIN o MAX con più intervalli o valori per visualizzare il maggiore o il minore di tali valori, ad esempio =MIN(A1:A10;B1:B10) oppure =MAX(A1:A10;10). |  |  |  |  |  |  | 

## Sheet: Data e ora

Funzioni di data |  |  |  |  | 
Excel può fornire la data corrente, in base alle impostazioni internazionali del computer. È anche possibile sommare e sottrarre le date. |  |  |  |  | 
Osserviamo la funzione OGGI, che visualizza la data corrente. Si tratta di funzioni attive, o volatili, per cui se la cartella di lavoro viene aperta domani, sarà visualizzata la data di domani. Immetti =OGGI() nella cella D6. 
 |  |  |  |  | 
Sottrarre date: immetti il tuo prossimo compleanno nel formato GG/MM/AA nella cella D7 e osserva come Excel ti indica il numero di giorni rimanenti usando =D7-D6 nella cella D8.
 |  |  |  |  | 
Sommare date: supponiamo di voler sapere la data di scadenza di una bolletta o quando devi restituire un libro alla biblioteca. Per scoprirlo, puoi aggiungere giorni a una data. Nella cella D10 immetti un numero casuale di giorni. Nella cella D11 abbiamo sommato =D6+D10 per calcolare la data di scadenza a partire da oggi.
 |  | Funzioni di data |  |  | 
INFORMAZIONI UTILI
Excel mantiene le date e le ore in base al numero di giorni a partire dal 1 gennaio 1900. Le ore vengono mantenute in parti frazionarie della giornata in base ai minuti. Quindi, 01/01/2017 12:30 in realtà è memorizzata come 42736,5208. Se la data o l'ora viene visualizzata sotto forma di numeri di questo tipo, premi CTRL+1 > Numero e seleziona un formato Data o Ora.  |  | Data odierna: |  |  | 
DETTAGLIO IMPORTANTE
Se non vuoi visualizzare un numero negativo perché non hai ancora immesso il tuo compleanno, puoi usare la funzione SE in questo modo: =SE(D7="";"";D7-D6), che indica "SE D7 è uguale a niente, non mostrare niente, altrimenti mostra D7 meno D6".
 |  | Tuo compleanno: |  |  | 
Funzioni di ora |  | Giorni mancanti al compleanno: | 0 |  | 
Excel può fornire l'ora corrente, in base alle impostazioni internazionali del computer. È anche possibile sommare e sottrarre le ore. Ad esempio, può essere necessario tenere traccia del numero di ore lavorate da un dipendente ogni settimana e calcolare la retribuzione e lo straordinario.
 |  |  |  |  | 
Nella cella D28 immetti =ADESSO(), che visualizza l'ora corrente e viene aggiornata ogni volta che Excel la calcola. Per cambiare il formato dell'ora, scegli CTRL+1 > Numero > Ora e seleziona il formato che preferisci.
 |  | Giorni di tolleranza: |  |  | 
Sommare le ore di diversi orari: nella cella D36 abbiamo immesso =((D35-D32)-(D34-D33))*24, che calcola le ore di inizio e fine di un dipendente e quindi sottrae il tempo trascorso a pranzo. La parte *24 alla fine della formula converte in ore la parte frazionaria della giornata usata da Excel. Sarà però necessario formattare la cella come Numero. A questo scopo, passa a Home > Formato > Celle (CTRL+1) > Numero > Numero > 2 decimali.

 |  | Scadenza fattura: | 00:00:00 |  | 
Se questa formula potesse parlare, direbbe: "sottrai Ora uscita da Ora entrata, quindi sottrai le ore Uscita/Rientro pranzo e moltiplica per 24 per convertire il tempo frazionario di Excel in ore" oppure =((Ora uscita - Ora entrata)-(Uscita pranzo - Rientro pranzo))*24. |  |  |  |  | 
Indietro |  |  |  |  | 
Avanti |  |  |  |  | 
Altre informazioni sul Web |  |  |  |  | 
Informazioni complete sulla funzione OGGI |  |  |  |  | 
Informazioni complete sulla funzione ADESSO |  |  |  |  | 
Informazioni complete sulla funzione DATA |  |  |  |  | 
Formazione gratuita su Excel disponibile online |  |  |  |  | 
 |  | Funzioni di ora |  |  | 
 |  | Ora corrente: |  |  | 
 |  | Ore giornaliere lavorate |  |  | 
 |  | Ora entrata: | 08:00:00 |  | 
 |  | Uscita pranzo: | 12:00:00 |  | 
 |  | Rientro pranzo: | 13:00:00 |  | 
 |  | Ora uscita: | 17:00:00 |  | 
 |  | Totale ore: | 8.000000000000002 |  | 
 |  | Data e ora statiche |  |  | 
 |  | Data: | 2017-09-27 00:00:00 |  | 
 |  | Ora: | 08:52:00 |  | 

## Sheet: Unire testo e numeri

Unione del testo contenuto in celle diverse |  |  |  |  | 
In Excel capita spesso di dover unire il testo presente in celle diverse. Un esempio molto comune è un elenco di nomi e cognomi da combinare sotto forma di nome, cognome oppure nome completo. In Excel si può fare usando il simbolo della e commerciale (&), che puoi inserire con MAIUSC+6.
 |  | Nome | Cognome | Cognome, Nome | Nome completo
Nella cella E3 immetti =D3&C3 per unire i cognomi e i nomi. 
 |  | Olga | Panicucci | Panicucci, Olga | Olga Panicucci
PanicucciOlga non è il risultato ideale. Dobbiamo aggiungere una virgola e uno spazio. A questo scopo usiamo le virgolette per creare una nuova stringa di testo. Questa volta immetti =D3&", "&C3. La parte &", "& consente di unire una virgola e uno spazio al testo nelle celle.
 |  | Pio | Udinesi |  | 
Per creare il nome completo, uniamo prima di tutto il nome e il cognome, ma usando uno spazio senza virgola. In F3 immetti =C3&" "&D3.
 |  | Albertino | Mazzanti |  | 
Altri dettagli |  | Fiamma | Greco |  | 
Avanti |  | Carmelo | Barese |  | 
Uso di testo e numeri insieme |  | Nazzareno | Romani |  | 
Ora usiamo il simbolo & per unire testo e numeri, non solo testo e testo

Osserva le celle C28:D29. Vedi che la data e le ore si trovano in celle separate? Puoi unirle con il simbolo & come vedrai nelle celle C32:C33, ma il risultato non è ideale. Non sapendo come vuoi formattare i numeri, Excel usa il formato più basilare, che in questo caso è la data seriale. Dobbiamo indicare esplicitamente a Excel come formattare la parte numerica della formula, in modo che venga visualizzata come vuoi nella stringa di testo risultante. Per farlo, puoi usare la funzione TESTO e un codice di formato. |  | Cataldo | Capon |  | 
Nella cella C36 immetti =C28&" "&TESTO(D28;"GG/MM/AAAA"). GG/MM/AAAA è il codice di formato italiano per giorno/mese/anno, ad esempio 25/09/2017.
 |  | Martina | Milani |  | 
Nella cella C37 immetti =C29&" "&TESTO(D29;"H:MM"). H:MM è il codice di formato italiano per ore:minuti, ad esempio 13:30.

 |  |  |  |  | 
GUARDA QUI
Le formule, soprattutto quelle di grandi dimensioni, possono risultare difficile da leggere, ma è possibile separare le parti con spazi, come in questo esempio:

=C28 & " " & TESTO(D28;"GG/MM/AAAA") |  |  |  |  | 
CURIOSITÀ
Se non sai quale codice di formato usare, puoi scegliere CTRL+1 > Numero per formattare le celle come preferisci. Seleziona l'opzione Personalizzato. Puoi copiare nella formula il codice di formato visualizzato. |  |  |  |  | 
Altre informazioni sul Web |  |  |  |  | 
Informazioni complete sulla funzione TESTO |  |  |  |  | 
Combinare testo e numeri |  |  |  |  | 
Formazione gratuita su Excel disponibile online |  |  |  |  | 
 |  | Usare testo e numeri |  |  | 
 |  | Data odierna: | 2026-02-12 00:00:00 |  | 
 |  | Ora corrente: | 2026-02-12 16:13:14.580000 |  | 
 |  | Unione di testo e numeri |  |  | 
 |  | Data odierna: 46065 |  |  | 
 |  | Ora corrente: 46065,6758631944 |  |  | 
 |  | Formattazione di testo e numeri |  |  | 
 |  | Data odierna: 12/02/2026 |  |  | 
 |  | Ora corrente: 16:13 |  |  | 

## Sheet: Istruzioni SE

Istruzioni SE |  |  |  |  |  |  |  |  |  |  |  | 
Le istruzioni SE permettono di eseguire confronti logici tra condizioni. Un'istruzione SE in genere indica di eseguire una determinata operazione se una condizione è vera e di eseguire un'altra operazione in caso contrario. Le formule possono restituire testo, valori o altri calcoli. |  |  |  |  |  |  |  |  |  |  |  | 
Nella cella D9 immetti =SE(C9="Mela";VERO;FALSO). La risposta corretta è VERO. 
 |  |  |  |  |  |  |  |  |  |  |  | 
Copia D9 in D10. Qui la risposta dovrebbe essere FALSO perché un'arancia non è una mela.
 |  |  |  |  |  |  |  |  |  |  |  | 
Prova un altro esempio osservando la formula nella cella D12. Abbiamo già inserito =SE(C12<100;"Minore di 100";"Maggiore di o uguale a 100"). Cosa succede se si immette un numero maggiore di 100 nella cella C12?
 |  |  |  |  |  |  |  |  |  |  |  | 
DETTAGLIO IMPORTANTE
VERO e FALSO sono diverse dalle altre parole usate nelle formule di Excel in quanto non è necessario racchiuderle tra virgolette e vengono formattate automaticamente in maiuscolo. Anche i numeri non devono necessariamente essere racchiusi tra virgolette. Il testo normale come Sì o No, invece, deve essere racchiuso tra virgolette in questo modo: 
=SE(C9="Mela";"Sì";"No") |  |  |  |  |  |  |  |  |  |  |  | 
Altri dettagli |  |  |  |  |  |  |  |  |  |  |  | 
Avanti |  | Istruzioni SE |  |  |  |  |  |  |  |  |  | 
Istruzione SE con un'altra funzione |  | Mela |  |  |  |  |  |  |  |  |  | 
Le istruzioni SE possono anche forzare l'esecuzione di altri calcoli se è soddisfatta una determinata condizione. Qui valuteremo una cella per stabilire se deve essere addebitata l'IVA e per calcolarla, se la condizione è vera.
 |  | Arancia |  |  |  |  |  |  |  |  |  | 
Nella cella F33 abbiamo inserito =SE(E33="Sì";F31*IVA;0), con l'IVA configurata come intervallo denominato con il valore 0,0825. La formula indica: se la cella E33 equivale a Sì, moltiplica la cella F31 per l'IVA, altrimenti restituisci il valore 0.

Prova a specificare No al posto di Sì nella cella E33 per vedere come cambia il calcolo. |  |  |  |  |  |  |  |  |  |  |  | 
Abbiamo quindi aggiunto un'istruzione SE per calcolare le spese di spedizione, se necessarie. Nella cella F35 vedrai =SE(E35="Sì";SOMMA(D28:D29)*1,25;0). Questo significa: "se la cella E35 contiene Sì, moltiplica per 1,25 la somma della colonna Quantità nella tabella soprastante, altrimenti restituisci il valore 0".
 |  | 50 | Minore di 100 |  |  |  |  |  |  |  |  | 
Quindi, sostituisci il valore 1,25 nella formula nella cella F35 con "Spedizione". Quando inizi a digitare, la funzione di correzione automatica di Excel dovrebbe trovare automaticamente la voce. Quando accade, premi TAB per immetterla. Questo è un intervallo denominato che è stato immesso da Formule > Definisci nome. A questo punto, se è necessario modificare le spese di spedizione, sarà sufficiente farlo in un unico posto e usare il nome Spedizione ovunque nella cartella di lavoro.

 |  |  |  |  |  |  |  |  |  |  |  | 
INFORMAZIONI UTILI
Quando si crea una formula, Excel inserisce automaticamente bordi colorati intorno a tutti gli intervalli a cui viene fatto riferimento nella formula e gli intervalli corrispondenti nella formula saranno dello stesso colore. Per osservare questo effetto, seleziona la cella F33 e premi F2 per modificare la formula. |  |  |  |  |  |  |  |  |  |  |  | 
L'ESPERTO SUGGERISCE
Gli intervalli denominati consentono di definire i termini o i valori in un'unica posizione per poterli riutilizzare in una cartella di lavoro. Per vedere tutti gli intervalli denominati usati in questa cartella di lavoro, scegli Formule > Gestione nomi. Fai clic qui per altre informazioni.
 |  |  |  |  |  |  |  |  |  |  |  | 
Indietro |  |  |  |  |  |  |  |  |  |  |  | 
Avanti |  |  |  |  |  |  |  |  |  |  |  | 
Altre informazioni sul Web |  |  |  |  |  |  |  |  |  |  |  | 
Informazioni complete sulla funzione SE |  |  |  |  |  |  |  |  |  |  |  | 
Informazioni complete sulla funzione PIÙ.SE |  |  |  |  |  |  |  |  |  |  |  | 
Istruzioni SE avanzate |  |  |  |  |  |  |  |  |  |  |  | 
Formazione gratuita su Excel disponibile online |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  |  | https://support.office.com/en-us/article/IF-function-69AED7C9-4E8A-4755-A9BC-AA8BBFF73BE2
 |  | Articolo | Quantità | Costo | Totale |  |  |  |  |  |  | 
 |  | Widget | 2 | 9.760711585683554 | 19.521423171367108 |  |  |  |  |  |  | 
 |  | Oggetto | 3 | 3.4189202461080024 | 10.256760738324008 |  |  |  |  |  |  | 
 |  |  | Subtotale | 13.179631831791557 | 29.778183909691116 |  |  |  |  |  |  | 
 |  |  | IVA? | Sì | 2.456700172549517 |  |  |  |  |  |  | 
 |  |  | Spedizione? | Sì | 6.25 |  |  |  |  |  |  | 
 |  |  | Totale |  | 38.48488408224063 |  |  |  |  |  |  | 

## Sheet: CERCA.VERT

CERCA.VERT |  |  |  |  |  |  |  |  |  |  | 
CERCA.VERT è una delle funzioni più usate in Excel. CERCA.VERT consente di cercare un valore in una colonna a sinistra, quindi restituisce le informazioni in un'altra colonna a destra se trova una corrispondenza. CERCA.VERT dice:
 |  |  |  |  |  |  |  |  |  |  | 
=CERCA.VERT(A1;B:C;2;FALSO) |  |  |  |  |  |  |  |  |  |  | 
Cosa vuoi cercare? |  |  |  |  |  |  |  |  |  |  | 
Se lo trovi, quante colonne a destra vuoi ottenere un valore? |  |  |  |  |  |  |  |  |  |  | 
Dove lo vuoi cercare? |  |  |  |  |  |  |  |  |  |  | 
Vuoi una corrispondenza esatta o approssimativa? |  |  |  |  |  |  |  |  |  |  | 
Nella cella D22 immetti =CERCA.VERT(C22;C17:D20;2;FALSO). La risposta corretta per Mele è 50. CERCA.VERT ha cercato il valore Mele, l'ha trovato e quindi ha restituito la quantità una colonna più a destra.

 |  |  |  |  |  |  |  |  |  |  | 
Ora prova autonomamente nella sezione Carne, nella cella G22. Dovresti ottenere =CERCA.VERT(F22;F17:G20;2;FALSO).

 |  |  |  |  |  |  |  |  |  |  | 
ESPERIMENTO
Prova a selezionare altri articoli negli elenchi a discesa. Noterai che i valori nelle celle dei risultati vengono aggiornati immediatamente. |  |  |  |  |  |  |  |  |  |  | 
Altri dettagli |  |  |  |  |  |  |  |  |  |  | 
Avanti |  |  |  |  |  |  |  |  |  |  | 
CERCA.VERT e #N/D |  |  |  |  |  |  |  |  |  |  | 
Presto o tardi ti capiterà che CERCA.VERT non riesca a trovare ciò che hai chiesto e restituisca un errore (#N/D). Questo può succedere, ad esempio, se il valore di ricerca non esiste oppure se la cella di riferimento non contiene ancora un valore.
 |  |  |  |  |  |  |  |  |  |  | 
Se sai che il valore di ricerca esiste, ma vuoi nascondere l'errore se la cella di ricerca è vuota, puoi usare l'istruzione SE. In questo caso, integriamo la formula CERCA.VERT esistente nella cella D43 in questo modo:

=SE(C43="";"";CERCA.VERT(C43;C37:D41;2;FALSO))

Questo significa: se la cella C43 equivale a niente (""), non restituire niente, altrimenti restituisci i risultati di CERCA.VERT. Nota la seconda parentesi di chiusura alla fine della formula, che conclude l'istruzione SE.
 |  |  |  |  |  |  |  |  |  |  | 
Se non sei certo che il valore di ricerca esista ma vuoi comunque nascondere l'errore #N/D, puoi usare una funzione di gestione degli errori denominata SE.ERRORE nella cella G43: =SE.ERRORE(CERCA.VERT(F43;F37:G41;2;FALSO);""). SE.ERRORE indica: se CERCA.VERT restituisce un risultato valido, visualizzalo, altrimenti non visualizzare niente (""). In questo caso non viene visualizzato niente (""), ma si possono anche usare numeri (0,1, 2 e così via) o un testo, ad esempio "La formula non è corretta".
 |  | Frutta | Quantità |  | Carne | Quantità |  |  |  |  | 
DETTAGLIO IMPORTANTE
SE.ERRORE è un gestore di errori che rimuove la visualizzazione di tutti gli errori che possono essere generati dalla formula. Questo può causare problemi se Excel notifica che nella formula è presente un errore effettivo che deve essere risolto.

In generale è preferibile non aggiungere gestori di errori alle formule se non si è assolutamente certi che funzionino correttamente. |  | Mele | 50 |  | Manzo | 50 |  |  |  |  | 
Indietro |  | Arance | 20 |  | Pollo | 30 |  |  |  |  | 
Avanti |  | Banane | 60 |  | Maiale | 10 |  |  |  |  | 
Altre informazioni sul Web |  | Limoni | 40 |  | Pesce | 50 |  |  |  |  | 
Informazioni complete sulla funzione CERCA.VERT |  |  |  |  |  |  |  |  |  |  | 
Informazioni complete sulle funzioni INDICE/CONFRONTA |  | Mele |  |  | Maiale |  |  |  |  |  | 
Informazioni complete sulla funzione SE.ERRORE |  |  |  |  |  |  |  |  |  |  | 
Usare le tabelle pivot per analizzare i dati di un foglio di lavoro |  |  |  |  |  |  |  |  |  |  | 
Formazione gratuita su Excel disponibile online |  |  |  |  |  |  |  |  |  |  | 
 |  | Se la funzione SOMMA nella cella D42 potesse parlare, direbbe: Somma i valori nelle celle D38, D39, D40 e D41. |  |  |  |  |  |  |  |  | 
 |  | Articolo | Quantità |  | Articolo | Quantità |  |  |  |  | 
 |  | Pane | 50 |  | Pane | 50 |  |  |  |  | 
 |  | Ciambelle | 100 |  | Ciambelle | 100 |  |  |  |  | 
 |  | Biscotti | 40 |  | Biscotti | 40 |  |  |  |  | 
 |  | Torte | 50 |  | Torte | 50 |  |  |  |  | 
 |  | Crostate | 20 |  | Crostate | 20 |  |  |  |  | 
 |  |  | #N/A |  | Pasticceria |  |  |  |  |  | 

## Sheet: Funzioni condizionali

Funzioni condizionali: SOMMA.SE |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Le funzioni condizionali consentono di calcolare la somma, la media e il conteggio o di ottenere il valore minimo o massimo di un intervallo in base a una condizione o a un criterio specificato. Ad esempio, si può calcolare quante mele ci sono tra tutti i frutti inclusi nell'elenco. Oppure il numero di arance di tipo Florida. |  | Frutta | Quantità |  | Frutta | Tipo | Quantità |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Frutta |  | Mele |  | Arance |  | Banane |  | Limoni
SOMMA.SE consente di sommare in un intervallo sulla base di un criterio specifico cercato in un altro intervallo, come il numero di mele. Seleziona la cella D17 e digita =SOMMA.SE(C3:C14;C17;D3:D14). La funzione SOMMA.SE è strutturata in questo modo: |  | Mele | 50 |  | Mele | Fuji | 50 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Mele |  | Fuji |  | Florida |  | Cavendish |  | Rough
150 |  | Arance | 20 |  | Arance | Florida | 20 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Arance |  | Honeycrisp |  | Navel |  | Lady Finger |  | Eureka
Quale intervallo vuoi esaminare? |  | Banane | 60 |  | Banane | Cavendish | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Banane |  |  |  |  |  |  |  | 
Quale valore (testo o numero) vuoi cercare? |  | Limoni | 40 |  | Limoni | Rough | 40 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Limoni |  |  |  |  |  |  |  | 
Per ogni corrispondenza trovata, quale intervallo vuoi sommare? |  | Mele | 50 |  | Mele | Honeycrisp | 50 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
SOMMA.PIÙ.SE equivale a SOMMA.SE, ma consente di usare più criteri. Quindi, in questo esempio, è possibile cercare frutta e tipo, anziché solo frutta. Seleziona la cella H17 e digita =SOMMA.PIÙ.SE(H3:H14;F3:F14;F17;G3:G14;G17). La funzione SOMMA.PIÙ.SE è strutturata in questo modo:
 |  | Arance | 20 |  | Arance | Navel | 20 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
=SOMMA.PIÙ.SE(H3:H14;F3:F14;F17;G3:G14;G17) |  | Banane | 60 |  | Banane | Lady Finger | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Quale intervallo vuoi sommare? |  | Limoni | 40 |  | Limoni | Eureka | 40 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Questo è il primo intervallo in cui cercare corrispondenze |  | Mele | 50 |  | Mele | Honeycrisp | 50 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Questo è il criterio per la prima corrispondenza |  | Arance | 20 |  | Arance | Navel | 20 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Questo è il secondo intervallo in cui cercare corrispondenze |  | Banane | 60 |  | Banane | Cavendish | 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Questo è il criterio per la seconda corrispondenza |  | Limoni | 40 |  | Limoni | Eureka | 40 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
L'ESPERTO SUGGERISCE
Ognuna delle celle Frutta e Tipo include un elenco a discesa in cui è possibile selezionare diversi frutti. Prova e osserva come le formule vengono aggiornate automaticamente. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Altri dettagli |  | Frutta | SOMMA.SE |  | Frutta | Tipo | SOMMA.PIÙ.SE |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Passaggio successivo |  | Mele |  |  | Arance | Florida |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Funzioni condizionali: CONTA.SE |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
CONTA.SE e CONTA.PIÙ.SE consentono di contare i valori in un intervallo in base a un determinato criterio. Sono un po' diverse dalle altre funzioni SE e PIÙ.SE in quanto hanno solo un intervallo di criteri e criteri. Non valutano un intervallo per poi cercare in un altro per riepilogare. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Seleziona la cella D64 e digita =CONTA.SE(C50:C61;C64). La funzione CONTA.SE è strutturata in questo modo: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
=CONTA.SE(C50:C61;C64) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Quale intervallo vuoi esaminare? |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Quale valore (testo o numero) vuoi cercare? |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
CONTA.PIÙ.SE equivale a SOMMA.SE, ma consente di usare più criteri. Pertanto, in questo esempio, è possibile cercare frutta e tipo, anziché solo frutta. Seleziona la cella H64 e digita =CONTA.PIÙ.SE(F50:F61;F64;G50:G61;G64). La funzione CONTA.PIÙ.SE è strutturata in questo modo:
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
=CONTA.PIÙ.SE(F50:F61;F64;G50:G61;G64) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Questo è il primo intervallo da contare |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Questo è il criterio per la prima corrispondenza |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Questo è il secondo intervallo da contare |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Questo è il criterio per la seconda corrispondenza |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Altri dettagli |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Avanti |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Altre funzioni condizionali |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Finora abbiamo visto le funzioni SOMMA.SE, SOMMA.PIÙ.SE, CONTA.SE e CONTA.PIÙ.SE. Ora puoi provare autonomamente con altre funzioni, come MEDIA.SE/MEDIA.PIÙ.SE, MAX.PIÙ.SE, MIN.PIÙ.SE. Sono tutte strutturate nello stesso modo, quindi una volta scritta una formula puoi semplicemente sostituire il nome della funzione con quello che vuoi usare. Abbiamo scritto tutte le funzioni necessarie per la cella E106, pronte da copiare/incollare. In alternativa, puoi provare a digitarle manualmente per esercitarti.

SOMMA.SE 	=SOMMA.SE(C92:C103;C106;E92:E103) 
SOMMA.PIÙ.SE 	=SOMMA.PIÙ.SE(E92:E103;C92:C103;C106;D92:D103;D106) 
MEDIA.SE 	=MEDIA.SE(C92:C103;C106;E92:E103) 
MEDIA.PIÙ.SE	=MEDIA.PIÙ.SE(E92:E103;C92:C103;C106;D92:D103;D106)
CONTA.SE 	=CONTA.SE(C92:C103;C106)
CONTA.PIÙ.SE 	=CONTA.PIÙ.SE(C92:C103;C106;D92:D103;D106) 
MAX.PIÙ.SE 	=MAX.PIÙ.SE(E92:E103;C92:C103;C106;D92:D103;D106)
MIN.PIÙ.SE 	=MIN.PIÙ.SE(E92:E103;C92:C103;C106;D92:D103;D106) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Altri dettagli |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Avanti |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
SOMMA.SE con un argomento valore |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Ecco un esempio di funzione SOMMA.SE usando "maggiore di" (>) per trovare tutti i valori che superano una determinata quantità: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
200 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Somma alcuni valori in base a questo criterio: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
...Esamina queste celle...
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
...e, se il valore è maggiore di 50, sommalo.
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
NOTA: se ti ritrovi a creare molte formule condizionali, tieni presente che una tabella pivot è una soluzione migliore. Per saperne di più, leggi questo articolo sulle tabelle pivot. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Altre informazioni sul Web |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Informazioni complete sulla funzione SOMMA.SE |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Informazioni complete sulla funzione SOMMA.PIÙ.SE |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Informazioni complete sulla funzione CONTA.SE |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Informazioni complete sulla funzione CONTA.PIÙ.SE |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Informazioni complete sulla funzione MEDIA.SE |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Informazioni complete sulla funzione MEDIA.PIÙ.SE |  | Frutta | Quantità |  | Frutta | Tipo | Quantità |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Informazioni complete sulla funzione MIN.PIÙ.SE |  | Mele | 50 |  | Mele | Fuji | 50 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

## Sheet: Creazione guidata Funzione

Creazione guidata Funzione |  |  | 
Se conosci il nome della formula che vuoi usare, ma non sai con certezza come costruirla, puoi usare la Creazione guidata Funzione.
 |  |  | 
Seleziona la cella D10 e passa a Formule > Inserisci funzione > digita CERCA.VERT nella casella Cerca una funzione e scegli Vai. Quando viene evidenziato CERCA.VERT, fai clic su OK nella parte inferiore. Quando selezioni una funzione nell'elenco, Excel ne visualizza la sintassi.
 |  |  | 
Immetti quindi gli argomenti della funzione nelle caselle di testo corrispondenti. Ogni volta che ne immetti uno, Excel lo valuta e mostra il relativo risultato, con il risultato finale nella parte inferiore. Man mano che accedi alle singole sezioni, i criteri per ogni argomento vengono elencati nella parte inferiore del modulo. Al termine scegli OK. Excel immette automaticamente la formula.


 |  | Frutta | Quantità
GUARDA QUI
Dovresti ottenere =CERCA.VERT(C10;C5:D8;2;FALSO) |  | Mele | 50
INFORMAZIONI UTILI
Puoi digitare riferimenti di cella e intervallo oppure selezionarli con il mouse. |  | Arance | 20
INFORMAZIONI UTILI
Quando accedi alla sezione dei singoli argomenti, la descrizione dell'argomento viene visualizzata nella parte inferiore del modulo, sopra il risultato della formula.
 |  | Banane | 60
Indietro |  | Limoni | 40
Avanti |  |  | 
Altre informazioni sul Web |  | Mele | 50
Panoramica delle formule in Excel |  |  | 
Funzioni di Excel (in base alla categoria) |  |  | 
Funzioni di Excel (in ordine alfabetico) |  |  | 
Formazione gratuita su Excel disponibile online |  |  | 

## Sheet: Errori nelle formule

Correzione degli errori nelle formule |  |  | 
Se una formula contiene un errore, Excel mostra #NomeErrore. Gli errori possono essere utili perché indicano che qualcosa non funziona correttamente, ma possono essere difficili da risolvere. Per fortuna ci sono diverse opzioni che facilitano l'individuazione dell'origine dell'errore e la relativa correzione.
 |  |  | 
Controllo errori: vai a Formule > Controllo errori. Viene visualizzata una finestra di dialogo che indica la causa generale dell'errore specifico. L'errore #N/D cella D9 è causato dal fatto che non esiste un valore corrispondente a "Mela". Puoi risolvere l'errore usando un valore esistente, eliminare l'errore con SE.ERRORE oppure ignorarlo, contando sul fatto scomparirà quando userai un valore effettivamente esistente.
 |  | Frutta | Quantità
Se fai clic su Informazioni sull'errore, viene visualizzato un argomento della Guida relativo al messaggio di errore. Se fai clic su Mostra passaggi del calcolo, viene visualizzata la finestra di dialogo Valuta formula.
 |  | Mele | 50
Ogni volta che fai clic su Valuta, Excel valuta la formula una sezione alla volta. Non specifica necessariamente perché si verifica un errore, ma indica dove. A quel punto, esamina l'argomento della Guida per capire qual è il problema presente nella formula.
 |  | Arance | 20
ESPERIMENTO
Qual è il problema qui? Suggerimento: vogliamo calcolare la SOMMA di tutti gli articoli. |  | Banane | 60
INFORMAZIONI UTILI
Fai clic su Opzioni per impostare le regole per i casi in cui gli errori in Excel vengono visualizzati o ignorati.
 |  | Limoni | 40
Indietro |  |  | 
Avanti |  | Mela | #N/A
Altre informazioni sul Web |  |  | 
Rilevare gli errori nelle formule |  |  | 
Come evitare errori nelle formule |  |  | 
Valutare un formula annidata un passaggio alla volta |  |  | 
Formazione gratuita su Excel disponibile online |  |  | 
 |  | Frutta | Quantità
 |  | Mele | 50
 |  | Arance | 20
 |  | Banane | 60
 |  | Limoni | 40
 |  | Totale | #NAME?

## Sheet: Altre informazioni

Altre domande su Excel? | 
Premi ALT+X e digita cosa che vuoi sapere. | 
Vai avanti. Sono disponibili altre risorse su Excel: | 
Community: Invia domande e mettiti in contatto con altri appassionati di Excel.
 | 
Altre novità?
Gli abbonati a Office 365 ricevono costantemente aggiornamenti e nuove funzionalità.

 | 
