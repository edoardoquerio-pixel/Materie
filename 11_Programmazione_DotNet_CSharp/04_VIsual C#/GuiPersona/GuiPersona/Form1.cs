using ClassePersona;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace GuiPersona
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnIvia_Click(object sender, EventArgs e)
        {
            var p = new Persona(txtNome.Text, txtCognome.Text, DateTime.Parse(txtDataNascita.Text), txtLuogoNascita.Text);
            
            txtEta.Text = p.Eta().ToString();
        }
        private void ResetForm()
        {
            txtNome.Text = string.Empty;
            txtCognome.Text = string.Empty;
            txtDataNascita.Text = string.Empty;
            txtLuogoNascita.Text = string.Empty;
            txtEta.Text = string.Empty;
            cbxSesso.SelectedIndex = -1;
        }   
        private void btnCancella_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("Conferma cancellazione dati?", "Conferma", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
            {
                ResetForm();
            }
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}
