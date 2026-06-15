namespace Querio_Esercitazione1
{
    public abstract class Persona
    {
        //propietà

        public string Nome { get; set; } = "";
        public string Cognome { get; set; } = "";
        public double Stipendio { get; set; }

        //metodi

        public abstract double Tredicesima();

        public override string ToString()
        {
            return $"{nameof(Nome)}={Nome}" +
                $", {nameof(Cognome)}={Cognome}" +
                $", {nameof(Stipendio)}={Stipendio}"
                ;
        }
    }
}
