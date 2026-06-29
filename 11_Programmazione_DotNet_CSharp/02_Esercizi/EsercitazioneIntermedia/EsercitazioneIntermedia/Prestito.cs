namespace EsercitazioneIntermedia
{
    internal class Prestito
    {
        //propietà
        public string Id { get; set; }
        public Studente Studente { get; set; }
        public Libro Libro { get; set; }
        public DateTime DataPrestito { get; set; }
        public DateTime? DataRestituzione { get; set; }
        public int GiorniScadenza { get; set; }

        //costruttore
        public Prestito(string id, Studente studente, Libro libro,
            DateTime dataPrestito, DateTime? dataRestituzione, int giorniScadenza)
        {
            Id = id;
            Studente = studente;
            Libro = libro;
            DataPrestito = dataPrestito;
            DataRestituzione = dataRestituzione;
            GiorniScadenza = giorniScadenza;
        }

        //metodi
        public bool IsInCorso()
        {
            return DataRestituzione == null;
        }

        public bool IsScaduto()
        {
            //se è già stato restituito non è scaduto
            if (DataRestituzione != null)
                return false;

            //verifica se la data odierna supera la data di scadenza
            return DateTime.Today > DataPrestito.AddDays(GiorniScadenza);
        }

        public override string ToString()
        {
            string stato;
            if (!IsInCorso())
                stato = "Restituito";
            else if (IsScaduto())
                stato = "SCADUTO";
            else
                stato = "In corso";

            return $"{Id}: {Studente.Nome} {Studente.Cognome} - {Libro.Titolo} " +
                $"(dal {DataPrestito:dd/MM/yyyy}, scad. {GiorniScadenza} gg) [{stato}]";
        }
    }
}
