namespace EsercitazioneIntermedia
{
    internal class Biblioteca
    {
        //propietà
        public Studente[] Studenti { get; private set; }
        public Libro[] Libri { get; private set; }
        public Prestito[] Prestiti { get; private set; }

        //costruttore: carica i dati dai file CSV
        public Biblioteca()
        {
            Studenti = CaricaStudenti("studenti.csv");
            Libri = CaricaLibri("libri.csv");
            Prestiti = CaricaPrestiti("prestiti.csv");
        }

        //metodi privati per il caricamento dei file CSV

        private Studente[] CaricaStudenti(string filePath)
        {
            //prima lettura: contare le righe
            StreamReader sr1 = new StreamReader(filePath);
            int conteggio = 0;
            string? riga = sr1.ReadLine(); //salta l'intestazione
            while ((riga = sr1.ReadLine()) != null)
                conteggio++;
            sr1.Close();

            //seconda lettura: popolare l'array
            Studente[] studenti = new Studente[conteggio];
            StreamReader sr2 = new StreamReader(filePath);
            riga = sr2.ReadLine(); //salta l'intestazione
            int i = 0;
            while ((riga = sr2.ReadLine()) != null)
            {
                string[] campi = riga.Split(';');
                //formato: Matricola;Cognome;Nome;Corso
                studenti[i] = new Studente(
                    campi[0],   //Matricola
                    campi[2],   //Nome
                    campi[1],   //Cognome
                    campi[3]    //Corso
                );
                i++;
            }
            sr2.Close();

            return studenti;
        }

        private Libro[] CaricaLibri(string filePath)
        {
            //prima lettura: contare le righe
            StreamReader sr1 = new StreamReader(filePath);
            int conteggio = 0;
            string? riga = sr1.ReadLine(); //salta l'intestazione
            while ((riga = sr1.ReadLine()) != null)
                conteggio++;
            sr1.Close();

            //seconda lettura: popolare l'array
            Libro[] libri = new Libro[conteggio];
            StreamReader sr2 = new StreamReader(filePath);
            riga = sr2.ReadLine(); //salta l'intestazione
            int i = 0;
            while ((riga = sr2.ReadLine()) != null)
            {
                string[] campi = riga.Split(';');
                //formato: ISBN;Titolo;Autore;Anno
                libri[i] = new Libro(
                    campi[0],               //ISBN
                    campi[1],               //Titolo
                    campi[2],               //Autore
                    int.Parse(campi[3])     //Anno
                );
                i++;
            }
            sr2.Close();

            return libri;
        }

        private Prestito[] CaricaPrestiti(string filePath)
        {
            //prima lettura: contare le righe
            StreamReader sr1 = new StreamReader(filePath);
            int conteggio = 0;
            string? riga = sr1.ReadLine(); //salta l'intestazione
            while ((riga = sr1.ReadLine()) != null)
                conteggio++;
            sr1.Close();

            //seconda lettura: popolare l'array
            Prestito[] prestiti = new Prestito[conteggio];
            StreamReader sr2 = new StreamReader(filePath);
            riga = sr2.ReadLine(); //salta l'intestazione
            int i = 0;
            while ((riga = sr2.ReadLine()) != null)
            {
                string[] campi = riga.Split(';');
                //formato: Id;MatricolaStudente;ISBN;DataPrestito;DataRestituzione;GiorniScadenza

                //ricerca dello studente per matricola
                Studente? studente = CercaStudente(campi[1]);

                //ricerca del libro per ISBN
                Libro? libro = CercaLibro(campi[2]);

                //conversione della data di prestito (formato dd/MM/yyyy)
                DateTime dataPrestito = DateTime.ParseExact(campi[3], "dd/MM/yyyy", null);

                //conversione della data di restituzione (può essere vuota)
                DateTime? dataRestituzione = null;
                if (campi[4] != "")
                    dataRestituzione = DateTime.ParseExact(campi[4], "dd/MM/yyyy", null);

                //conversione dei giorni di scadenza
                int giorniScadenza = int.Parse(campi[5]);

                if (studente == null || libro == null)
                    throw new Exception("Errore: studente o libro non trovato nei file CSV.");

                prestiti[i] = new Prestito(
                    campi[0],           //Id
                    studente,           //Studente
                    libro,              //Libro
                    dataPrestito,       //DataPrestito
                    dataRestituzione,   //DataRestituzione
                    giorniScadenza      //GiorniScadenza
                );
                i++;
            }
            sr2.Close();

            return prestiti;
        }

        //metodi di utilità per la ricerca

        private Studente? CercaStudente(string matricola)
        {
            foreach (Studente s in Studenti)
            {
                if (s.Matricola == matricola)
                    return s;
            }
            return null;
        }

        private Libro? CercaLibro(string isbn)
        {
            foreach (Libro l in Libri)
            {
                if (l.ISBN == isbn)
                    return l;
            }
            return null;
        }

        //servizi richiesti

        /* 1. Visualizzazione del numero di libri presi in prestito
         *    e non ancora restituiti */
        public int ContaPrestitiInCorso()
        {
            int conteggio = 0;
            foreach (Prestito p in Prestiti)
            {
                if (p.IsInCorso())
                    conteggio++;
            }
            return conteggio;
        }

        /* 2. Visualizzazione dell'elenco dei prestiti archiviati */
        public void StampaPrestiti()
        {
            Console.WriteLine("\n=== ELENCO PRESTITI ARCHIVIATI ===");
            Console.WriteLine("--------------------------------------");
            foreach (Prestito p in Prestiti)
            {
                Console.WriteLine(p);
            }
            Console.WriteLine($"\nTotale prestiti archiviati: {Prestiti.Length}");
        }

        /* 3. Visualizzazione dei prestiti non consegnati e scaduti */
        public void StampaPrestitiScaduti()
        {
            Console.WriteLine("\n=== PRESTITI NON CONSEGNATI E SCADUTI ===");
            Console.WriteLine("--------------------------------------");
            int conteggio = 0;
            foreach (Prestito p in Prestiti)
            {
                if (p.IsInCorso() && p.IsScaduto())
                {
                    Console.WriteLine(p);
                    conteggio++;
                }
            }

            if (conteggio == 0)
                Console.WriteLine("Nessun prestito scaduto.");
            else
                Console.WriteLine($"\nTotale prestiti scaduti: {conteggio}");
        }
    }
}
