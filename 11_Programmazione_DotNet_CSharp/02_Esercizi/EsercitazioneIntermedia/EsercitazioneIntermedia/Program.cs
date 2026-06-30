namespace EsercitazioneIntermedia
{
    internal class Program
    {
        /*
         * Esercitazione Intermedia - Gestione Prestiti Biblioteca ITS
         * 
         * Argomenti: classi, ereditarietà, polimorfismo, collezioni di oggetti, gestione dei file
         * 
         * Il programma carica i dati dai file CSV (studenti.csv, libri.csv, prestiti.csv)
         * e offre un menu testuale per visualizzare:
         * 1. Numero di libri presi in prestito e non ancora restituiti
         * 2. Elenco completo dei prestiti archiviati
         * 3. Prestiti non consegnati e scaduti
         * 0. Uscita
         */
        static void Main(string[] args)
        {
            Console.WriteLine("=== SISTEMA GESTIONE PRESTITI BIBLIOTECA ITS ===\n");

            //caricamento dei dati dai file CSV
            Biblioteca biblioteca = new Biblioteca();
            Console.WriteLine("Dati caricati con successo!");
            Console.WriteLine($"Studenti: {biblioteca.Studenti.Length}");
            Console.WriteLine($"Libri: {biblioteca.Libri.Length}");
            Console.WriteLine($"Prestiti: {biblioteca.Prestiti.Length}");

            //menu testuale
            bool inEsecuzione = true;

            while (inEsecuzione)
            {
                Console.WriteLine("\n--- MENU PRINCIPALE ---");
                Console.WriteLine("1. Visualizza numero libri in prestito non restituiti");
                Console.WriteLine("2. Visualizza elenco prestiti archiviati");
                Console.WriteLine("3. Visualizza prestiti non consegnati e scaduti");
                Console.WriteLine("0. Esci");
                Console.Write("Scegli un'opzione: ");

                string? scelta = Console.ReadLine();

                switch (scelta)
                {
                    case "1":
                        //Servizio 1: numero di libri in prestito non restituiti
                        Console.WriteLine("\n=== LIBRI IN PRESTITO NON RESTITUITI ===");
                        int conteggio = biblioteca.ContaPrestitiInCorso();
                        Console.WriteLine($"Numero di libri attualmente in prestito: {conteggio}");
                        break;

                    case "2":
                        //Servizio 2: elenco completo dei prestiti
                        biblioteca.StampaPrestiti();
                        break;

                    case "3":
                        //Servizio 3: prestiti non consegnati e scaduti
                        biblioteca.StampaPrestitiScaduti();
                        break;

                    case "0":
                        Console.WriteLine("\nUscita dal programma. Arrivederci!");
                        inEsecuzione = false;
                        break;

                    default:
                        Console.WriteLine("Opzione non valida. Scegli 1, 2, 3 o 0.");
                        break;
                }
            }
        }
    }
}
