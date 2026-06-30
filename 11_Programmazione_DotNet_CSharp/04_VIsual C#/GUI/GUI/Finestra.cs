namespace GUI
{
    public partial class Finestra : Form
    {
        public Finestra()
        {
            InitializeComponent();
        }

        private void btnInvia_Click(object sender, EventArgs e)
        {
            string testo = txtContenuto.Text;

            MessageBox.Show("Hai fatto click sul pulsante Invia", "Finestra modale", MessageBoxButtons.OK, MessageBoxIcon.Information);

            lblRisultato.Text = "Hai inserito il testo: " + testo;
        }
    }
}
