namespace EsempioMVC.Models
{
    public class Prodotto
    {
        //propietà
        public int Codice { get; set; }
        public string Denominazione { get; set; }
        public string Descrizione { get; set; }
        public double Prezzo { get; set; }
        public int Giacenza { get; set; }

        public override string ToString()
        {
            return $"Codice={Codice}" +
                $", Denominazione={Denominazione}" +
                $", Descrizione={Descrizione}" +
                $", Prezzo={Prezzo}" +
                $", Giacenza={Giacenza}";
        }
    }
}
