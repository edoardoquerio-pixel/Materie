namespace StudentiGUI
{
    partial class Dettaglio
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            lblDettaglioStudente = new Label();
            lblCercaPerMatricola = new Label();
            txtCerca = new TextBox();
            btnCerca = new Button();
            pnlCerca = new Panel();
            pnlDettaglio = new Panel();
            lblMatricola = new Label();
            txtMatricola = new TextBox();
            txtNome = new TextBox();
            lblNome = new Label();
            txtCognome = new TextBox();
            lblCognome = new Label();
            txtEmail = new TextBox();
            lblEmail = new Label();
            txtClasse = new TextBox();
            lblClasse = new Label();
            pnlCerca.SuspendLayout();
            pnlDettaglio.SuspendLayout();
            SuspendLayout();
            // 
            // lblDettaglioStudente
            // 
            lblDettaglioStudente.AutoSize = true;
            lblDettaglioStudente.Location = new Point(183, 17);
            lblDettaglioStudente.Name = "lblDettaglioStudente";
            lblDettaglioStudente.Size = new Size(105, 15);
            lblDettaglioStudente.TabIndex = 0;
            lblDettaglioStudente.Text = "Dettaglio Studente";
            // 
            // lblCercaPerMatricola
            // 
            lblCercaPerMatricola.AutoSize = true;
            lblCercaPerMatricola.Location = new Point(55, 40);
            lblCercaPerMatricola.Name = "lblCercaPerMatricola";
            lblCercaPerMatricola.Size = new Size(110, 15);
            lblCercaPerMatricola.TabIndex = 1;
            lblCercaPerMatricola.Text = "Cerca per Matricola";
            // 
            // txtCerca
            // 
            txtCerca.Location = new Point(171, 37);
            txtCerca.Name = "txtCerca";
            txtCerca.Size = new Size(100, 23);
            txtCerca.TabIndex = 2;
            // 
            // btnCerca
            // 
            btnCerca.Location = new Point(286, 36);
            btnCerca.Name = "btnCerca";
            btnCerca.Size = new Size(75, 23);
            btnCerca.TabIndex = 3;
            btnCerca.Text = "Cerca";
            btnCerca.UseVisualStyleBackColor = true;
            btnCerca.Click += btnCerca_Click;
            // 
            // pnlCerca
            // 
            pnlCerca.Controls.Add(btnCerca);
            pnlCerca.Controls.Add(lblCercaPerMatricola);
            pnlCerca.Controls.Add(txtCerca);
            pnlCerca.Location = new Point(12, 35);
            pnlCerca.Name = "pnlCerca";
            pnlCerca.Size = new Size(460, 100);
            pnlCerca.TabIndex = 4;
            // 
            // pnlDettaglio
            // 
            pnlDettaglio.Controls.Add(txtClasse);
            pnlDettaglio.Controls.Add(lblClasse);
            pnlDettaglio.Controls.Add(txtEmail);
            pnlDettaglio.Controls.Add(lblEmail);
            pnlDettaglio.Controls.Add(txtCognome);
            pnlDettaglio.Controls.Add(lblCognome);
            pnlDettaglio.Controls.Add(txtNome);
            pnlDettaglio.Controls.Add(lblNome);
            pnlDettaglio.Controls.Add(txtMatricola);
            pnlDettaglio.Controls.Add(lblMatricola);
            pnlDettaglio.Location = new Point(12, 161);
            pnlDettaglio.Name = "pnlDettaglio";
            pnlDettaglio.Size = new Size(460, 388);
            pnlDettaglio.TabIndex = 5;
            // 
            // lblMatricola
            // 
            lblMatricola.AutoSize = true;
            lblMatricola.Location = new Point(43, 29);
            lblMatricola.Name = "lblMatricola";
            lblMatricola.Size = new Size(57, 15);
            lblMatricola.TabIndex = 0;
            lblMatricola.Text = "Matricola";
            // 
            // txtMatricola
            // 
            txtMatricola.Enabled = false;
            txtMatricola.Location = new Point(116, 26);
            txtMatricola.Name = "txtMatricola";
            txtMatricola.Size = new Size(100, 23);
            txtMatricola.TabIndex = 1;
            // 
            // txtNome
            // 
            txtNome.Enabled = false;
            txtNome.Location = new Point(116, 87);
            txtNome.Name = "txtNome";
            txtNome.Size = new Size(100, 23);
            txtNome.TabIndex = 3;
            // 
            // lblNome
            // 
            lblNome.AutoSize = true;
            lblNome.Location = new Point(43, 90);
            lblNome.Name = "lblNome";
            lblNome.Size = new Size(40, 15);
            lblNome.TabIndex = 2;
            lblNome.Text = "Nome";
            // 
            // txtCognome
            // 
            txtCognome.Enabled = false;
            txtCognome.Location = new Point(116, 161);
            txtCognome.Name = "txtCognome";
            txtCognome.Size = new Size(100, 23);
            txtCognome.TabIndex = 5;
            // 
            // lblCognome
            // 
            lblCognome.AutoSize = true;
            lblCognome.Location = new Point(43, 164);
            lblCognome.Name = "lblCognome";
            lblCognome.Size = new Size(60, 15);
            lblCognome.TabIndex = 4;
            lblCognome.Text = "Cognome";
            lblCognome.Click += label1_Click;
            // 
            // txtEmail
            // 
            txtEmail.Enabled = false;
            txtEmail.Location = new Point(116, 236);
            txtEmail.Name = "txtEmail";
            txtEmail.Size = new Size(100, 23);
            txtEmail.TabIndex = 7;
            // 
            // lblEmail
            // 
            lblEmail.AutoSize = true;
            lblEmail.Location = new Point(43, 239);
            lblEmail.Name = "lblEmail";
            lblEmail.Size = new Size(36, 15);
            lblEmail.TabIndex = 6;
            lblEmail.Text = "Email";
            // 
            // txtClasse
            // 
            txtClasse.Enabled = false;
            txtClasse.Location = new Point(116, 308);
            txtClasse.Name = "txtClasse";
            txtClasse.Size = new Size(100, 23);
            txtClasse.TabIndex = 9;
            // 
            // lblClasse
            // 
            lblClasse.AutoSize = true;
            lblClasse.Location = new Point(43, 311);
            lblClasse.Name = "lblClasse";
            lblClasse.Size = new Size(40, 15);
            lblClasse.TabIndex = 8;
            lblClasse.Text = "Classe";
            // 
            // Dettaglio
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(484, 561);
            Controls.Add(pnlDettaglio);
            Controls.Add(pnlCerca);
            Controls.Add(lblDettaglioStudente);
            Name = "Dettaglio";
            Text = "Dettaglio";
            pnlCerca.ResumeLayout(false);
            pnlCerca.PerformLayout();
            pnlDettaglio.ResumeLayout(false);
            pnlDettaglio.PerformLayout();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label lblDettaglioStudente;
        private Label lblCercaPerMatricola;
        private TextBox txtCerca;
        private Button btnCerca;
        private Panel pnlCerca;
        private Panel pnlDettaglio;
        private TextBox txtNome;
        private Label lblNome;
        private TextBox txtMatricola;
        private Label lblMatricola;
        private TextBox txtEmail;
        private Label lblEmail;
        private TextBox txtCognome;
        private Label lblCognome;
        private TextBox txtClasse;
        private Label lblClasse;
    }
}