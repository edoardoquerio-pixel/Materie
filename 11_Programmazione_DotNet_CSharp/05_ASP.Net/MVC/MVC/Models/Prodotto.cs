namespace MVC.Models
{
    public class Prodotto
    {
        public int Codice { get; set; }
        public string Denominazione { get; set; }
        public string Descrizione { get; set; }
        public double Prezzo { get; set; }
        public int Giacenza { get; set; }

        public override string ToString()
        {
            return $"{{{nameof(Codice)}={Codice.ToString()}, {nameof(Denominazione)}={Denominazione}, {nameof(Descrizione)}={Descrizione}, {nameof(Prezzo)}={Prezzo.ToString()}, {nameof(Giacenza)}={Giacenza.ToString()}}}";
        }
    }
}
