namespace StudentiGUI
{
    public partial class Elenco : Form
    {
        public Elenco()
        {
            InitializeComponent();

            //Istanziare StudentiDAL
            StudentiDAL dal = new StudentiDAL();

            lblElementiTrovati.Text=$"Studenti trovati: {dal.Elenco().Count}";

            txtElencoStudenti.Text = string.Join("\n", dal.Elenco());




        }
    }
}
