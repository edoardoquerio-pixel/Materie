using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace MVC.Controllers
{
    public class ProdottiController : Controller
    {
        // GET: ProdottiController
        public ActionResult Index()
        {
            return View();
        }

        // GET: ProdottiController/Details/5
        public ActionResult Details(int id)
        {
            return View();
        }

        // GET: ProdottiController/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: ProdottiController/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create(IFormCollection collection)
        {
            try
            {
                return RedirectToAction(nameof(Index));
            }
            catch
            {
                return View();
            }
        }

        // GET: ProdottiController/Edit/5
        public ActionResult Edit(int id)
        {
            return View();
        }

        // POST: ProdottiController/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit(int id, IFormCollection collection)
        {
            try
            {
                return RedirectToAction(nameof(Index));
            }
            catch
            {
                return View();
            }
        }

        // GET: ProdottiController/Delete/5
        public ActionResult Delete(int id)
        {
            return View();
        }

        // POST: ProdottiController/Delete/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Delete(int id, IFormCollection collection)
        {
            try
            {
                return RedirectToAction(nameof(Index));
            }
            catch
            {
                return View();
            }
        }
    }
}
