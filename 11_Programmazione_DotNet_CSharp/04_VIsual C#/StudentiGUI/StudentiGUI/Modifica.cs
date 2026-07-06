using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace StudentiGUI
{
    public partial class Modifica : Form
    {
        public Modifica()
        {
            InitializeComponent();
        }

        private void btnCerca_Click(object sender, EventArgs e)
        {
           

            var dal = new StudentiDAL();
            int matricola = Convert.ToInt32(txtCerca.Text);

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

        private void btnSalva_Click(object sender, EventArgs e)
        {
            //istanziare un oggetto dal 
            var dal = new StudentiDAL();

            int matricola = Convert.ToInt32(txtMatricola.Text);

            //cerco studente con matricola inserita
            Studente s = dal.Dettaglio(matricola);

                //salvo i dati nel database
                var studente = new Studente()
                {
                    Matricola = Convert.ToInt32(txtMatricola.Text),
                    Nome = txtNome.Text,
                    Cognome = txtCognome.Text,
                    Email = txtEmail.Text,
                    Classe = txtClasse.Text
                };
                dal.Modifica(studente);
                MessageBox.Show($"Studente aggiornato con successo", "Salva", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }

        
        private void ResetForm()
        {
            txtMatricola.Text = String.Empty;
            txtNome.Text = String.Empty;
            txtCognome.Text = String.Empty;
            txtEmail.Text = String.Empty;
            txtClasse.Text = String.Empty;
        }
        private void btnCancella_Click(object sender, EventArgs e)
        {
        
                if (MessageBox.Show($"Sei sicuro di voler cancellare il studente?", "Cancella", MessageBoxButtons.OKCancel, MessageBoxIcon.Question) == DialogResult.OK)

                    ResetForm();

            
        }
    }
}
