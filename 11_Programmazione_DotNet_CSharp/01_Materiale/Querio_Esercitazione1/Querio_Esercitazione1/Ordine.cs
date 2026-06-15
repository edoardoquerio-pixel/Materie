namespace Querio_Esercitazione1
{
    public sealed class Ordine
    {
        //propietà

        public string Codice { get; set; } = "";
        public DateTime Data { get; set; }
        public List<Prodotto> ElencoProdotti { get; set; }
        public Venditore Venditore { get; set; }

        //metodi pubblici

        public int NumeroPezzi()
        {
            return this.ElencoProdotti.Count;
        }

        public double Totale()
        {
            double totale = 0;

            foreach (Prodotto p in this.ElencoProdotti)
                totale += p.Prezzo;

            return totale;
        }

        public void Stampa()
        {
            string path = @"..\..\..\file\" + this.Codice + ".txt";

            using (StreamWriter sw = new StreamWriter(path))
            {
                sw.WriteLine("ORDINE: " + this.Codice);
                sw.WriteLine("Data: " + this.Data.ToString("dd/MM/yyyy"));
                sw.WriteLine("Venditore: " + this.Venditore.Nome + " " + this.Venditore.Cognome);
                sw.WriteLine("----------------------------------------");

                //raggruppo i prodotti per calcolare le quantita'
                List<string> codiciStampati = new List<string>();

                foreach (Prodotto p in this.ElencoProdotti)
                {
                    bool giaStampato = false;

                    foreach (string c in codiciStampati)
                    {
                        if (c == p.Codice)
                        {
                            giaStampato = true;
                            break;
                        }
                    }

                    if (!giaStampato)
                    {
                        codiciStampati.Add(p.Codice);

                        int qta = 0;

                        foreach (Prodotto inner in this.ElencoProdotti)
                        {
                            if (inner.Codice == p.Codice)
                                qta++;
                        }

                        double subtotale = p.Prezzo * qta;

                        sw.WriteLine(p.Codice + " | " +
                                     p.Denominazione + " | " +
                                     "Qta: " + qta + " | " +
                                     "Prezzo: " + p.Prezzo.ToString("C") + " | " +
                                     "Subtotale: " + subtotale.ToString("C"));
                    }
                }

                sw.WriteLine("----------------------------------------");
                sw.WriteLine("TOTALE ORDINE: " + this.Totale().ToString("C"));
            }
        }

        public static string GeneraCodiceOrdine()
        {
            string caratteri = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
            char[] chars = new char[8];
            Random random = new Random();

            chars[0] = caratteri[random.Next(26)];

            for (int i = 1; i < 8; i++)
                chars[i] = caratteri[random.Next(36)];

            return new string(chars);
        }
    }
}
