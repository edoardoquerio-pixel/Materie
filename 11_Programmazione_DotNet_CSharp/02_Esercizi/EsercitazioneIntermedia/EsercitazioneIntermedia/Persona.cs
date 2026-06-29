namespace EsercitazioneIntermedia
{
    internal class Persona
    {
        //propietà
        public string Nome { get; set; }
        public string Cognome { get; set; }

        //costruttore
        public Persona(string nome, string cognome)
        {
            Nome = nome;
            Cognome = cognome;
        }

        //metodo virtuale per il polimorfismo
        public virtual string GetDescrizione()
        {
            return $"{Nome} {Cognome}";
        }

        public override string ToString()
        {
            return $"{Nome} {Cognome}";
        }
    }
}
