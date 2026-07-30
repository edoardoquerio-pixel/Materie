using System;
using System.Collections.Generic;

namespace PrestitiVideotecaMVC.Models;

public partial class Film
{
    public int Codice { get; set; }

    public string? Titolo { get; set; }

    public string? Supporto { get; set; }

    public string? Regista { get; set; }

    public string? Attori { get; set; }

    public string? Genere { get; set; }

    public virtual ICollection<Prestito> Prestitos { get; set; } = new List<Prestito>();
}
