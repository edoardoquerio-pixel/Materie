namespace GuiPersona
{
    partial class Form1
    {
        /// <summary>
        /// Variabile di progettazione necessaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Pulire le risorse in uso.
        /// </summary>
        /// <param name="disposing">ha valore true se le risorse gestite devono essere eliminate, false in caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Codice generato da Progettazione Windows Form

        /// <summary>
        /// Metodo necessario per il supporto della finestra di progettazione. Non modificare
        /// il contenuto del metodo con l'editor di codice.
        /// </summary>
        private void InitializeComponent()
        {
            this.lblNuovo = new System.Windows.Forms.Label();
            this.lblCognome = new System.Windows.Forms.Label();
            this.txtCognome = new System.Windows.Forms.TextBox();
            this.txtNome = new System.Windows.Forms.TextBox();
            this.lblNome = new System.Windows.Forms.Label();
            this.txtDataNascita = new System.Windows.Forms.TextBox();
            this.lblDataNasciata = new System.Windows.Forms.Label();
            this.txtLuogoNascita = new System.Windows.Forms.TextBox();
            this.lblLuogoNascita = new System.Windows.Forms.Label();
            this.lblSesso = new System.Windows.Forms.Label();
            this.btnIvia = new System.Windows.Forms.Button();
            this.btnCancella = new System.Windows.Forms.Button();
            this.lblEta = new System.Windows.Forms.Label();
            this.txtEta = new System.Windows.Forms.TextBox();
            this.cbxSesso = new System.Windows.Forms.ComboBox();
            this.SuspendLayout();
            // 
            // lblNuovo
            // 
            this.lblNuovo.AutoSize = true;
            this.lblNuovo.Location = new System.Drawing.Point(369, 15);
            this.lblNuovo.Name = "lblNuovo";
            this.lblNuovo.Size = new System.Drawing.Size(39, 13);
            this.lblNuovo.TabIndex = 0;
            this.lblNuovo.Text = "Nuovo";
            // 
            // lblCognome
            // 
            this.lblCognome.AutoSize = true;
            this.lblCognome.Location = new System.Drawing.Point(58, 90);
            this.lblCognome.Name = "lblCognome";
            this.lblCognome.Size = new System.Drawing.Size(52, 13);
            this.lblCognome.TabIndex = 1;
            this.lblCognome.Text = "Cognome";
            // 
            // txtCognome
            // 
            this.txtCognome.Location = new System.Drawing.Point(153, 87);
            this.txtCognome.Name = "txtCognome";
            this.txtCognome.Size = new System.Drawing.Size(121, 20);
            this.txtCognome.TabIndex = 2;
            // 
            // txtNome
            // 
            this.txtNome.Location = new System.Drawing.Point(153, 140);
            this.txtNome.Name = "txtNome";
            this.txtNome.Size = new System.Drawing.Size(121, 20);
            this.txtNome.TabIndex = 4;
            // 
            // lblNome
            // 
            this.lblNome.AutoSize = true;
            this.lblNome.Location = new System.Drawing.Point(58, 143);
            this.lblNome.Name = "lblNome";
            this.lblNome.Size = new System.Drawing.Size(35, 13);
            this.lblNome.TabIndex = 3;
            this.lblNome.Text = "Nome";
            // 
            // txtDataNascita
            // 
            this.txtDataNascita.Location = new System.Drawing.Point(153, 194);
            this.txtDataNascita.Name = "txtDataNascita";
            this.txtDataNascita.Size = new System.Drawing.Size(121, 20);
            this.txtDataNascita.TabIndex = 6;
            // 
            // lblDataNasciata
            // 
            this.lblDataNasciata.AutoSize = true;
            this.lblDataNasciata.Location = new System.Drawing.Point(58, 197);
            this.lblDataNasciata.Name = "lblDataNasciata";
            this.lblDataNasciata.Size = new System.Drawing.Size(80, 13);
            this.lblDataNasciata.TabIndex = 5;
            this.lblDataNasciata.Text = "Data di Nascita";
            // 
            // txtLuogoNascita
            // 
            this.txtLuogoNascita.Location = new System.Drawing.Point(153, 249);
            this.txtLuogoNascita.Name = "txtLuogoNascita";
            this.txtLuogoNascita.Size = new System.Drawing.Size(121, 20);
            this.txtLuogoNascita.TabIndex = 8;
            // 
            // lblLuogoNascita
            // 
            this.lblLuogoNascita.AutoSize = true;
            this.lblLuogoNascita.Location = new System.Drawing.Point(58, 252);
            this.lblLuogoNascita.Name = "lblLuogoNascita";
            this.lblLuogoNascita.Size = new System.Drawing.Size(87, 13);
            this.lblLuogoNascita.TabIndex = 7;
            this.lblLuogoNascita.Text = "Luogo di Nascita";
            // 
            // lblSesso
            // 
            this.lblSesso.AutoSize = true;
            this.lblSesso.Location = new System.Drawing.Point(58, 308);
            this.lblSesso.Name = "lblSesso";
            this.lblSesso.Size = new System.Drawing.Size(36, 13);
            this.lblSesso.TabIndex = 9;
            this.lblSesso.Text = "Sesso";
            // 
            // btnIvia
            // 
            this.btnIvia.Location = new System.Drawing.Point(100, 374);
            this.btnIvia.Name = "btnIvia";
            this.btnIvia.Size = new System.Drawing.Size(75, 23);
            this.btnIvia.TabIndex = 11;
            this.btnIvia.Text = "Invia";
            this.btnIvia.UseVisualStyleBackColor = true;
            this.btnIvia.Click += new System.EventHandler(this.btnIvia_Click);
            // 
            // btnCancella
            // 
            this.btnCancella.Location = new System.Drawing.Point(239, 374);
            this.btnCancella.Name = "btnCancella";
            this.btnCancella.Size = new System.Drawing.Size(75, 23);
            this.btnCancella.TabIndex = 12;
            this.btnCancella.Text = "Cancella";
            this.btnCancella.UseVisualStyleBackColor = true;
            this.btnCancella.Click += new System.EventHandler(this.btnCancella_Click);
            // 
            // lblEta
            // 
            this.lblEta.AutoSize = true;
            this.lblEta.Location = new System.Drawing.Point(414, 379);
            this.lblEta.Name = "lblEta";
            this.lblEta.Size = new System.Drawing.Size(26, 13);
            this.lblEta.TabIndex = 13;
            this.lblEta.Text = "Età:";
            // 
            // txtEta
            // 
            this.txtEta.Enabled = false;
            this.txtEta.Location = new System.Drawing.Point(446, 376);
            this.txtEta.Name = "txtEta";
            this.txtEta.ReadOnly = true;
            this.txtEta.Size = new System.Drawing.Size(100, 20);
            this.txtEta.TabIndex = 14;
            // 
            // cbxSesso
            // 
            this.cbxSesso.FormattingEnabled = true;
            this.cbxSesso.Items.AddRange(new object[] {
            "Maschio",
            "Femmina"});
            this.cbxSesso.Location = new System.Drawing.Point(153, 305);
            this.cbxSesso.Name = "cbxSesso";
            this.cbxSesso.Size = new System.Drawing.Size(121, 21);
            this.cbxSesso.TabIndex = 15;
            this.cbxSesso.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.cbxSesso);
            this.Controls.Add(this.txtEta);
            this.Controls.Add(this.lblEta);
            this.Controls.Add(this.btnCancella);
            this.Controls.Add(this.btnIvia);
            this.Controls.Add(this.lblSesso);
            this.Controls.Add(this.txtLuogoNascita);
            this.Controls.Add(this.lblLuogoNascita);
            this.Controls.Add(this.txtDataNascita);
            this.Controls.Add(this.lblDataNasciata);
            this.Controls.Add(this.txtNome);
            this.Controls.Add(this.lblNome);
            this.Controls.Add(this.txtCognome);
            this.Controls.Add(this.lblCognome);
            this.Controls.Add(this.lblNuovo);
            this.Name = "Form1";
            this.Text = "Gui Persona";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblNuovo;
        private System.Windows.Forms.Label lblCognome;
        private System.Windows.Forms.TextBox txtCognome;
        private System.Windows.Forms.TextBox txtNome;
        private System.Windows.Forms.Label lblNome;
        private System.Windows.Forms.TextBox txtDataNascita;
        private System.Windows.Forms.Label lblDataNasciata;
        private System.Windows.Forms.TextBox txtLuogoNascita;
        private System.Windows.Forms.Label lblLuogoNascita;
        private System.Windows.Forms.Label lblSesso;
        private System.Windows.Forms.Button btnIvia;
        private System.Windows.Forms.Button btnCancella;
        private System.Windows.Forms.Label lblEta;
        private System.Windows.Forms.TextBox txtEta;
        private System.Windows.Forms.ComboBox cbxSesso;
    }
}

