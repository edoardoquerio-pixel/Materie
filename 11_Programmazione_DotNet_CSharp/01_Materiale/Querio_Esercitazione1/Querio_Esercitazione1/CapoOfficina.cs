namespace Querio_Esercitazione1
{
    public class CapoOfficina : Meccanico
    {
        //propietà

        public List<Ordine> Ordini { get; set; }

        //metodi

        public override double Tredicesima()
        {
            double importoOrdini = 0;

            foreach (Ordine o in this.Ordini)
            {
                importoOrdini += o.Totale();
            }

            return this.Stipendio * 2 + importoOrdini * 0.05;
        }
    }
}
