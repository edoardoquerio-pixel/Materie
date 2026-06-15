namespace Querio_Esercitazione1
{
    public class Venditore : Persona, ICloneable
    {
        //propietà

        public SettoreVendite Settore { get; set; }

        //metodi

        public override double Tredicesima()
        {
            return this.Stipendio * 1.91;
        }

        public object Clone()
        {
            return this.MemberwiseClone();
        }
    }
}
