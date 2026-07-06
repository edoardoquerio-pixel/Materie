namespace StudentiGUI
{
    partial class Nuovo
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
            lblTitolo = new Label();
            pnlDettaglio = new Panel();
            btnCancella = new Button();
            btnSalva = new Button();
            txtClasse = new TextBox();
            lblClasse = new Label();
            txtEmail = new TextBox();
            lblEmail = new Label();
            txtCognome = new TextBox();
            lblCognome = new Label();
            txtNome = new TextBox();
            lblNome = new Label();
            txtMatricola = new TextBox();
            lblMatricola = new Label();
            pnlDettaglio.SuspendLayout();
            SuspendLayout();
            // 
            // lblTitolo
            // 
            lblTitolo.AutoSize = true;
            lblTitolo.Location = new Point(189, 9);
            lblTitolo.Name = "lblTitolo";
            lblTitolo.Size = new Size(93, 15);
            lblTitolo.TabIndex = 0;
            lblTitolo.Text = "Nuovo Studente";
            // 
            // pnlDettaglio
            // 
            pnlDettaglio.Controls.Add(btnCancella);
            pnlDettaglio.Controls.Add(btnSalva);
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
            pnlDettaglio.Location = new Point(12, 49);
            pnlDettaglio.Name = "pnlDettaglio";
            pnlDettaglio.Size = new Size(460, 388);
            pnlDettaglio.TabIndex = 6;
            // 
            // btnCancella
            // 
            btnCancella.Location = new Point(376, 352);
            btnCancella.Name = "btnCancella";
            btnCancella.Size = new Size(75, 23);
            btnCancella.TabIndex = 11;
            btnCancella.Text = "Cancella";
            btnCancella.UseVisualStyleBackColor = true;
            btnCancella.Click += btnCancella_Click;
            // 
            // btnSalva
            // 
            btnSalva.Location = new Point(273, 352);
            btnSalva.Name = "btnSalva";
            btnSalva.Size = new Size(75, 23);
            btnSalva.TabIndex = 10;
            btnSalva.Text = "Salva";
            btnSalva.UseVisualStyleBackColor = true;
            btnSalva.Click += btnSalva_Click;
            // 
            // txtClasse
            // 
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
            // txtEmail
            // 
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
            // txtCognome
            // 
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
            // 
            // txtNome
            // 
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
            // txtMatricola
            // 
            txtMatricola.Location = new Point(116, 26);
            txtMatricola.Name = "txtMatricola";
            txtMatricola.Size = new Size(100, 23);
            txtMatricola.TabIndex = 1;
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
            // Nuovo
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(484, 561);
            Controls.Add(pnlDettaglio);
            Controls.Add(lblTitolo);
            Name = "Nuovo";
            Text = "Nuovo";
            pnlDettaglio.ResumeLayout(false);
            pnlDettaglio.PerformLayout();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label lblTitolo;
        private Panel pnlDettaglio;
        private Button btnCancella;
        private Button btnSalva;
        private TextBox txtClasse;
        private Label lblClasse;
        private TextBox txtEmail;
        private Label lblEmail;
        private TextBox txtCognome;
        private Label lblCognome;
        private TextBox txtNome;
        private Label lblNome;
        private TextBox txtMatricola;
        private Label lblMatricola;
    }
}