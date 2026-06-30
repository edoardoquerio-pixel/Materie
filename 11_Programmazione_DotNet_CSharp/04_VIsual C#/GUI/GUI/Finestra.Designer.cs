namespace GUI
{
    partial class Finestra
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
            lblTesto = new Label();
            txtContenuto = new TextBox();
            btnInvia = new Button();
            lblRisultato = new Label();
            SuspendLayout();
            // 
            // lblTitolo
            // 
            lblTitolo.AutoSize = true;
            lblTitolo.Font = new Font("Segoe UI", 12F, FontStyle.Bold);
            lblTitolo.Location = new Point(386, 9);
            lblTitolo.Name = "lblTitolo";
            lblTitolo.Size = new Size(55, 21);
            lblTitolo.TabIndex = 0;
            lblTitolo.Text = "Titolo";
            lblTitolo.TextAlign = ContentAlignment.TopCenter;
            // 
            // lblTesto
            // 
            lblTesto.AutoSize = true;
            lblTesto.Location = new Point(51, 67);
            lblTesto.Name = "lblTesto";
            lblTesto.Size = new Size(95, 15);
            lblTesto.TabIndex = 1;
            lblTesto.Text = "Inserisci un testo";
            // 
            // txtContenuto
            // 
            txtContenuto.Location = new Point(152, 64);
            txtContenuto.Name = "txtContenuto";
            txtContenuto.Size = new Size(100, 23);
            txtContenuto.TabIndex = 2;
            // 
            // btnInvia
            // 
            btnInvia.Location = new Point(279, 63);
            btnInvia.Name = "btnInvia";
            btnInvia.Size = new Size(75, 23);
            btnInvia.TabIndex = 3;
            btnInvia.Text = "Invia";
            btnInvia.UseVisualStyleBackColor = true;
            btnInvia.Click += btnInvia_Click;
            // 
            // lblRisultato
            // 
            lblRisultato.AutoSize = true;
            lblRisultato.Location = new Point(51, 360);
            lblRisultato.Name = "lblRisultato";
            lblRisultato.Size = new Size(0, 15);
            lblRisultato.TabIndex = 4;
            // 
            // Finestra
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(784, 411);
            Controls.Add(lblRisultato);
            Controls.Add(btnInvia);
            Controls.Add(txtContenuto);
            Controls.Add(lblTesto);
            Controls.Add(lblTitolo);
            Name = "Finestra";
            Text = "Finestra";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label lblTitolo;
        private Label lblTesto;
        private TextBox txtContenuto;
        private Button btnInvia;
        private Label lblRisultato;
    }
}
