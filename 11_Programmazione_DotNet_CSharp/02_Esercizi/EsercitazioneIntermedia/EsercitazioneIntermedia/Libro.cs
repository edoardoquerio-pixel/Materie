namespace EsercitazioneIntermedia
{
    internal class Libro
    {
        //propietà
        public string ISBN { get; set; }
        public string Titolo { get; set; }
        public string Autore { get; set; }
        public int Anno { get; set; }

        //costruttore
        public Libro(string isbn, string titolo, string autore, int anno)
        {
            ISBN = isbn;
            Titolo = titolo;
            Autore = autore;
            Anno = anno;
        }

        public override string ToString()
        {
            return $"{Titolo} - {Autore} ({Anno})";
        }
    }
}
