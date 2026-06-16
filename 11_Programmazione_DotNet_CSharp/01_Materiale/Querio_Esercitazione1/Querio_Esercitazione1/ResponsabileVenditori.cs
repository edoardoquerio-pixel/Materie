namespace Querio_Esercitazione1
{
    public class ResponsabileVenditori : Venditore
    {
        //propietà

        public List<Venditore> Venditori { get; set; }

        //metodi

        public override double Tredicesima()
        {
            double bonus = 0;

            foreach (Venditore v in this.Venditori)
            {
                double tariffaGiornaliera = v.Stipendio / 30.0;
                bonus += tariffaGiornaliera * 0.15;
            }

            return this.Stipendio * 2 + bonus;
        }
    }
}
