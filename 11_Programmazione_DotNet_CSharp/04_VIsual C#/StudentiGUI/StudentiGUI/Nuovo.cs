using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace StudentiGUI
{
    public partial class Nuovo : Form
    {
        public Nuovo()
        {
            InitializeComponent();
        }

        private void btnSalva_Click(object sender, EventArgs e)
        {
            //istanziare un oggetto dal 
            var dal = new StudentiDAL();

            int matricola = Convert.ToInt32(txtMatricola.Text);

            //cerco studente con matricola inserita
            Studente s = dal.Dettaglio(matricola);

            //verifico sua assenza nel database
            if (s != null)
            {
                MessageBox.Show($"Matricola {matricola} già presente nel database", "Cerca", MessageBoxButtons.OK, MessageBoxIcon.Information);

            }
            else
            {
                //salvo i dati nel database
                var studente = new Studente()
                {
                    Matricola = matricola,
                    Nome = txtNome.Text,
                    Cognome = txtCognome.Text,
                    Email = txtEmail.Text,
                    Classe = txtClasse.Text
                };
                dal.Nuovo(studente);
                MessageBox.Show($"Studente aggiunto con successo", "Salva", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
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


            
