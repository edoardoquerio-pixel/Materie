namespace EsempioMVC.Models
{
    public class ContattoViewModel
    {
        //ViewModel
        public string? Cognome { get; set; }
        public string? Nome { get; set; }
        public required string Email { get; set; }
        public string? Oggetto { get; set; }
        public required string Messaggio { get; set; }
    }
}
