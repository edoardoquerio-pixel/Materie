namespace DatabaseCRUD
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Database CRUD!");


            var dal = new StudentiDAL();

            Console.WriteLine($"Elenco studenti: \n {string.Join("\n", dal.Elenco())}");

            Console.Write("Insersci la matricola dello studente da cercare: ");
            int matricola = int.Parse(Console.ReadLine());

            Studente? s = dal.Dettaglio(matricola);

            if (s != null)
                Console.WriteLine(s);
            else 
                Console.WriteLine($"Lo studente con matricola {matricola} non è presente nell'elenco.");

            Studente studente = new Studente();
            Console.WriteLine("Inserisci un nuovo studente:");
            Console.Write("Matricola: ");
            studente.Matricola = int.Parse(Console.ReadLine());
            Console.Write("Nome: ");
            studente.Nome = Console.ReadLine();
            Console.Write("Cognome: ");
            studente.Cognome = Console.ReadLine();
            Console.Write("Email: ");
            studente.Email = Console.ReadLine();
            Console.Write("Classe: ");
            studente.Classe = Console.ReadLine();

                dal.Nuovo(studente);
                Console.WriteLine("Studente inserito con successo.");

            //Studente sMod = new Studente() { Matricola = 12002, Nome ="Vito", Cognome = "Lo Presti", Email = "vito.lopresti@its.net", Classe = "5B" };
            //dal.Modifica(sMod);
            //Console.WriteLine("Studente modificato con successo.");
        }
    }
}
