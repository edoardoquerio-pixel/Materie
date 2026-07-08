namespace StudentiGUI
{
    partial class Elenco
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            lblTitolo = new Label();
            lblElementiTrovati = new Label();
            txtElencoStudenti = new TextBox();
            SuspendLayout();
            // 
            // lblTitolo
            // 
            lblTitolo.AutoSize = true;
            lblTitolo.Location = new Point(347, 9);
            lblTitolo.Name = "lblTitolo";
            lblTitolo.Size = new Size(89, 15);
            lblTitolo.TabIndex = 0;
            lblTitolo.Text = "Elenco Studenti";
            // 
            // lblElementiTrovati
            // 
            lblElementiTrovati.AutoSize = true;
            lblElementiTrovati.Location = new Point(33, 52);
            lblElementiTrovati.Name = "lblElementiTrovati";
            lblElementiTrovati.Size = new Size(98, 15);
            lblElementiTrovati.TabIndex = 1;
            lblElementiTrovati.Text = "Elementi Trovati: ";
            // 
            // txtElencoStudenti
            // 
            txtElencoStudenti.Enabled = false;
            txtElencoStudenti.Location = new Point(33, 70);
            txtElencoStudenti.Multiline = true;
            txtElencoStudenti.Name = "txtElencoStudenti";
            txtElencoStudenti.Size = new Size(600, 300);
            txtElencoStudenti.TabIndex = 2;
            // 
            // Elenco
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(784, 461);
            Controls.Add(txtElencoStudenti);
            Controls.Add(lblElementiTrovati);
            Controls.Add(lblTitolo);
            Name = "Elenco";
            Text = "Elenco";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label lblTitolo;
        private Label lblElementiTrovati;
        private TextBox txtElencoStudenti;
    }
}
