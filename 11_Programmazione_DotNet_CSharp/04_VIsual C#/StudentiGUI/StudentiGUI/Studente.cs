using System;
using System.Collections.Generic;
using System.Text;

namespace StudentiGUI
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
        public override string ToString()
        {
            return $"{{{nameof(Matricola)}={Matricola.ToString()}" +
             $"{nameof(Nome)}={Nome}" +
             $"{nameof(Cognome)}={Cognome}" +
             $"{nameof(Email)}={Email}" +
             $"{nameof(Classe)}={Classe}}}";
        }
    }
}
