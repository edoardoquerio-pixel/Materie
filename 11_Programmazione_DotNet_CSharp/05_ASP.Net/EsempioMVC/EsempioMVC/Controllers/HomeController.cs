using EsempioMVC.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace EsempioMVC.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
        public IActionResult SintassiRazor()
        {
            return View(); 
        }
        //GET
        public IActionResult Contatto()
        {
            var contatto = new ContattoViewModel() { Email = string.Empty, Messaggio = string.Empty };
            return View(contatto);
        }
        //POST - Contatto


        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
