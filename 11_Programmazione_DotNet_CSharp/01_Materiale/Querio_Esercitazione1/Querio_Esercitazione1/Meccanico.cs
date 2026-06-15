namespace Querio_Esercitazione1
{
    public class Meccanico : Persona
    {
        //propietà

        public TipologiaMeccanico Tipologia { get; set; }

        //metodi

        public override double Tredicesima()
        {
            return this.Stipendio * 1.93;
        }

        public bool Equals(Meccanico altro)
        {
            return this.Nome == altro.Nome &&
                   this.Cognome == altro.Cognome &&
                   this.Stipendio == altro.Stipendio &&
                   this.Tipologia == altro.Tipologia;
        }
    }
}
