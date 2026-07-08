using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace StudentiGUI
{
    public partial class Elimina : Form
    {
        public Elimina()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void btnCerca_Click(object sender, EventArgs e)
        {
            int matricola = Convert.ToInt32(txtCerca.Text);

            var dal = new StudentiDAL();

            Studente? s = dal.Dettaglio(matricola);

            if (s == null)
            {
                MessageBox.Show($"Lo studente con matricola {matricola} non esiste", "Cerca", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else
            {
                txtMatricola.Text = s.Matricola.ToString();
                txtNome.Text = s.Nome;
                txtCognome.Text = s.Cognome;
                txtEmail.Text = s.Email;
                txtClasse.Text = s.Classe;

            }
            
        }
    }
}
