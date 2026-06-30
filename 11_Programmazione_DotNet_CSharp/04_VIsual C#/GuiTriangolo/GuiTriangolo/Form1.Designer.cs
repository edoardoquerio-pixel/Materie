namespace GuiTriangolo
{
    partial class Triangolo
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
            this.lblLato1 = new System.Windows.Forms.Label();
            this.lblLato2 = new System.Windows.Forms.Label();
            this.lblLato3 = new System.Windows.Forms.Label();
            this.txtLato1 = new System.Windows.Forms.TextBox();
            this.txtLato2 = new System.Windows.Forms.TextBox();
            this.txtLato3 = new System.Windows.Forms.TextBox();
            this.textBox4 = new System.Windows.Forms.TextBox();
            this.lblRisultato = new System.Windows.Forms.Label();
            this.lblTriangolo = new System.Windows.Forms.Label();
            this.btnInvio = new System.Windows.Forms.Button();
            this.btnCancella = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // lblLato1
            // 
            this.lblLato1.AutoSize = true;
            this.lblLato1.Location = new System.Drawing.Point(57, 121);
            this.lblLato1.Name = "lblLato1";
            this.lblLato1.Size = new System.Drawing.Size(57, 13);
            this.lblLato1.TabIndex = 0;
            this.lblLato1.Text = "Primo Lato";
            // 
            // lblLato2
            // 
            this.lblLato2.AutoSize = true;
            this.lblLato2.Location = new System.Drawing.Point(57, 181);
            this.lblLato2.Name = "lblLato2";
            this.lblLato2.Size = new System.Drawing.Size(74, 13);
            this.lblLato2.TabIndex = 1;
            this.lblLato2.Text = "Secondo Lato";
            // 
            // lblLato3
            // 
            this.lblLato3.AutoSize = true;
            this.lblLato3.Location = new System.Drawing.Point(57, 238);
            this.lblLato3.Name = "lblLato3";
            this.lblLato3.Size = new System.Drawing.Size(58, 13);
            this.lblLato3.TabIndex = 2;
            this.lblLato3.Text = "Terzo Lato";
            // 
            // txtLato1
            // 
            this.txtLato1.Location = new System.Drawing.Point(184, 118);
            this.txtLato1.Name = "txtLato1";
            this.txtLato1.Size = new System.Drawing.Size(100, 20);
            this.txtLato1.TabIndex = 3;
            this.txtLato1.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // txtLato2
            // 
            this.txtLato2.Location = new System.Drawing.Point(184, 178);
            this.txtLato2.Name = "txtLato2";
            this.txtLato2.Size = new System.Drawing.Size(100, 20);
            this.txtLato2.TabIndex = 4;
            this.txtLato2.TextChanged += new System.EventHandler(this.textBox2_TextChanged);
            // 
            // txtLato3
            // 
            this.txtLato3.Location = new System.Drawing.Point(184, 235);
            this.txtLato3.Name = "txtLato3";
            this.txtLato3.Size = new System.Drawing.Size(100, 20);
            this.txtLato3.TabIndex = 5;
            // 
            // textBox4
            // 
            this.textBox4.Location = new System.Drawing.Point(439, 344);
            this.textBox4.Name = "textBox4";
            this.textBox4.Size = new System.Drawing.Size(100, 20);
            this.textBox4.TabIndex = 6;
            // 
            // lblRisultato
            // 
            this.lblRisultato.AutoSize = true;
            this.lblRisultato.Location = new System.Drawing.Point(349, 350);
            this.lblRisultato.Name = "lblRisultato";
            this.lblRisultato.Size = new System.Drawing.Size(82, 13);
            this.lblRisultato.TabIndex = 7;
            this.lblRisultato.Text = "Tipo di triangolo";
            // 
            // lblTriangolo
            // 
            this.lblTriangolo.AutoSize = true;
            this.lblTriangolo.Location = new System.Drawing.Point(393, 27);
            this.lblTriangolo.Name = "lblTriangolo";
            this.lblTriangolo.Size = new System.Drawing.Size(51, 13);
            this.lblTriangolo.TabIndex = 8;
            this.lblTriangolo.Text = "Triangolo";
            this.lblTriangolo.Click += new System.EventHandler(this.label5_Click);
            // 
            // btnInvio
            // 
            this.btnInvio.Location = new System.Drawing.Point(114, 342);
            this.btnInvio.Name = "btnInvio";
            this.btnInvio.Size = new System.Drawing.Size(75, 23);
            this.btnInvio.TabIndex = 9;
            this.btnInvio.Text = "Invio";
            this.btnInvio.UseVisualStyleBackColor = true;
            this.btnInvio.Click += new System.EventHandler(this.button1_Click);
            // 
            // btnCancella
            // 
            this.btnCancella.Location = new System.Drawing.Point(231, 342);
            this.btnCancella.Name = "btnCancella";
            this.btnCancella.Size = new System.Drawing.Size(75, 23);
            this.btnCancella.TabIndex = 10;
            this.btnCancella.Text = "Cancella";
            this.btnCancella.UseVisualStyleBackColor = true;
            // 
            // Triangolo
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.btnCancella);
            this.Controls.Add(this.btnInvio);
            this.Controls.Add(this.lblTriangolo);
            this.Controls.Add(this.lblRisultato);
            this.Controls.Add(this.textBox4);
            this.Controls.Add(this.txtLato3);
            this.Controls.Add(this.txtLato2);
            this.Controls.Add(this.txtLato1);
            this.Controls.Add(this.lblLato3);
            this.Controls.Add(this.lblLato2);
            this.Controls.Add(this.lblLato1);
            this.Name = "Triangolo";
            this.Text = "Triangolo";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblLato1;
        private System.Windows.Forms.Label lblLato2;
        private System.Windows.Forms.Label lblLato3;
        private System.Windows.Forms.TextBox txtLato1;
        private System.Windows.Forms.TextBox txtLato2;
        private System.Windows.Forms.TextBox txtLato3;
        private System.Windows.Forms.TextBox textBox4;
        private System.Windows.Forms.Label lblRisultato;
        private System.Windows.Forms.Label lblTriangolo;
        private System.Windows.Forms.Button btnInvio;
        private System.Windows.Forms.Button btnCancella;
    }
}

