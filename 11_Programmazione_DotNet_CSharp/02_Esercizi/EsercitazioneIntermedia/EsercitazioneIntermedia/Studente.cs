namespace EsercitazioneIntermedia
{
    internal class Studente : Persona
    {
        //propietà
        public string Matricola { get; set; }
        public string Corso { get; set; }

        //costruttore con chiamata al costruttore base
        public Studente(string matricola, string nome, string cognome, string corso)
            : base(nome, cognome)
        {
            Matricola = matricola;
            Corso = corso;
        }

        //override del metodo virtuale (polimorfismo)
        public override string GetDescrizione()
        {
            return $"{Matricola} - {base.GetDescrizione()} ({Corso})";
        }

        public override string ToString()
        {
            return GetDescrizione();
        }
    }
}
