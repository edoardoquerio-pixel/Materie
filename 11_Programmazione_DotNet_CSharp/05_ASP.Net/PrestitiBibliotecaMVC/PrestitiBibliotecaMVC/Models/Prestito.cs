using System;
using System.Collections.Generic;
using System.ComponentModel;

namespace PrestitiBibliotecaMVC.Models;

public partial class Prestito
{
    public int Id { get; set; }

    [DisplayName("Libro")]
    public int IdLibro { get; set; }

    [DisplayName("Studente")]
    public int Matricola { get; set; }

    [DisplayName("Data Prestito")]
    public DateTime DataPrestito { get; set; } = DateTime.Now;

    [DisplayName("Data Restituzione")]
    public DateTime? DataRestituzione { get; set; }

    [DisplayName("Titolo Libro")]
    public virtual Libro IdLibroNavigation { get; set; } = null!;

    [DisplayName("Studente")]
    public virtual Studente MatricolaNavigation { get; set; } = null!;
}
