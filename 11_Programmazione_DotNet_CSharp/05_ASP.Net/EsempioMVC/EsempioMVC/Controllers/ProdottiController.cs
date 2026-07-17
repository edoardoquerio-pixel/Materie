using EsempioMVC.Models;
using Microsoft.AspNetCore.Mvc;

namespace EsempioMVC.Controllers
{
    public class ProdottiController : Controller
    {
        private List<Prodotto> lista = new List<Prodotto> {
        new Prodotto
        {
            Codice = 1,
            Denominazione = "Prodotto 1",
            Descrizione = "Descrizione Prodotto 1",
            Prezzo = 10.15,
            Giacenza = 100
        },

        new Prodotto
        {
            Codice = 2,
            Denominazione = "Prodotto 2",
            Descrizione = "Descrizione Prodotto 2",
            Prezzo = 10.50,
            Giacenza = 10
        }};

        public IActionResult Index()
        {
            return View(lista);
        }
        //GET
        //POST
        public IActionResult Details(int codice)
        {
            // sintassi lambda expression per filtrare la lista dei prodotti in base al codice
            var p = lista.Where(x => x.Codice == codice).FirstOrDefault();

            return View(p);
        }
        //modifica 

        //eliminazione 
    }
}
