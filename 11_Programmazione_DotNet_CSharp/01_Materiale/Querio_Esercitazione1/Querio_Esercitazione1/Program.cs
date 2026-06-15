namespace Querio_Esercitazione1
{
    public class Program
    {
        static void Main(string[] args)
        {
            QuerioEsercitazione1Biz biz = new QuerioEsercitazione1Biz();

            while (true)
            {
                Console.Clear();
                Console.WriteLine("--- GESTIONALE OFFICINA ---");
                Console.WriteLine("1) Visualizza dati responsabile venditori");
                Console.WriteLine("2) Visualizza dati capo officina");
                Console.WriteLine("3) Stampa ordine tramite codice");
                Console.WriteLine("4) Termina programma");
                Console.Write("Scegli: ");

                string scelta = Console.ReadLine();

                switch (scelta)
                {
                    case "1":
                        biz.VisualizzaResponsabile();
                        break;

                    case "2":
                        biz.VisualizzaCapoOfficina();
                        break;

                    case "3":
                        biz.StampaOrdine();
                        break;

                    case "4":
                        return;

                    default:
                        Console.WriteLine("Opzione non valida.");
                        Console.ReadKey();
                        break;
                }
            }
        }
    }
}
