using System;
using System.Collections.Generic;
using System.Text;

namespace DatabaseCRUD
{
    internal class Studente
    {
        //proprietà
        public int Matricola { get; set; }
        public string Nome { get; set; }
        public string Cognome { get; set; }
        public string Email { get; set; }
        public string Classe { get; set; }

        public string FormatDettaglio()
        {
            return $"{{{nameof(Matricola)}={Matricola.ToString()}" +
                $"\n {nameof(Nome)}={Nome}" +
                $"\n {nameof(Cognome)}={Cognome}" +
                $"\n {nameof(Email)}={Email}" +
                $"\n {nameof(Classe)}={Classe}}}";
        }
    }
}
