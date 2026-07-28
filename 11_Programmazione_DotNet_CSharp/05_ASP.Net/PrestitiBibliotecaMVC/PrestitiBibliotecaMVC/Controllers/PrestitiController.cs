using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using PrestitiBibliotecaMVC.Models;

namespace PrestitiBibliotecaMVC.Controllers
{
    public class PrestitiController : Controller
    {
        private readonly PrestitiBibliotecaMvcContext _context;

        public PrestitiController(PrestitiBibliotecaMvcContext context)
        {
            _context = context;
        }

        // GET: Prestiti
        public async Task<IActionResult> Index(string? search)
        {
            var prestitiBibliotecaMvcContext = _context.Prestiti
                .Include(p => p.IdLibroNavigation)
                .Include(p => p.MatricolaNavigation)
                .AsQueryable()
                ;

            //filtro dei dati in base al titolo del libro o al cognome o nome dello studente
            if(search!=null)
                prestitiBibliotecaMvcContext = prestitiBibliotecaMvcContext.Where(p => p.IdLibroNavigation.Titolo!.Contains(search) || p.MatricolaNavigation.Cognome!.Contains(search) || p.MatricolaNavigation.Nome!.Contains(search));

            //passo il valore di ricerca alla view per mantenere il valore nel form
            ViewBag.Search = search;
            prestitiBibliotecaMvcContext = prestitiBibliotecaMvcContext.OrderByDescending(p => p.DataPrestito);
            return View(await prestitiBibliotecaMvcContext.ToListAsync());
        }

        public async Task<IActionResult> PrestitiNonRestituiti()
        {
            var prestitiBibliotecaMvcContext = _context.Prestiti
                .Include(p => p.IdLibroNavigation)
                .Include(p => p.MatricolaNavigation)
                .Where(p=>p.DataRestituzione == null)
                .OrderByDescending(p => p.DataPrestito);
            ;
            return View("Index",await prestitiBibliotecaMvcContext.ToListAsync());
        }
        public async Task<IActionResult> ArchivioPrestiti()
        {
            var prestitiBibliotecaMvcContext = _context.Prestiti
                .Include(p => p.IdLibroNavigation)
                .Include(p => p.MatricolaNavigation)
                .Where(p => p.DataRestituzione != null)
                .OrderByDescending(p => p.DataPrestito);
            ;
            return View("Index", await prestitiBibliotecaMvcContext.ToListAsync());
        }

        public async Task<IActionResult> RestituisciPrestito(int id)
        {
            var prestito = await _context.Prestiti.FindAsync(id);
            if (prestito == null)
                return NotFound();
            try
            {
                prestito.DataRestituzione = DateTime.Now; //restituisco il prestito impostando la data di restituzione a quella odierna
                _context.Update(prestito);
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)

            {
                throw;
            }
            return RedirectToAction(nameof(Index));
        }
        // GET: Prestiti/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var prestito = await _context.Prestiti
                .Include(p => p.IdLibroNavigation)
                .Include(p => p.MatricolaNavigation)
                .FirstOrDefaultAsync(m => m.Id == id);
            if (prestito == null)
            {
                return NotFound();
            }

            return View(prestito);
        }


        
        // GET: Prestiti/Create
        public IActionResult Create()
        {
            ViewData["IdLibro"] = new SelectList(_context.Libri, "Id", "Titolo");
            ViewData["Matricola"] = new SelectList(_context.Studenti, "Id", "Nominativo");
            return View();
        }

        // POST: Prestiti/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,IdLibro,Matricola")] Prestito prestito)
        {
            try
            {
                _context.Add(prestito);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            catch (Exception)
            {
                ViewData["IdLibro"] = new SelectList(_context.Libri, "Id", "Titolo", prestito.IdLibro);
                ViewData["Matricola"] = new SelectList(_context.Studenti, "Id", "Nominativo", prestito.Matricola);
                return View(prestito);
            }
        }

        // GET: Prestiti/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var prestito = await _context.Prestiti.FindAsync(id);
            if (prestito == null)
            {
                return NotFound();
            }
            ViewData["IdLibro"] = new SelectList(_context.Libri, "Id", "Id", prestito.IdLibro);
            ViewData["Matricola"] = new SelectList(_context.Studenti, "Id", "Id", prestito.Matricola);
            return View(prestito);
        }

        // POST: Prestiti/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,IdLibro,Matricola,DataPrestito,DataRestituzione")] Prestito prestito)
        {
            if (id != prestito.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(prestito);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!PrestitoExists(prestito.Id))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction(nameof(Index));
            }
            ViewData["IdLibro"] = new SelectList(_context.Libri, "Id", "Id", prestito.IdLibro);
            ViewData["Matricola"] = new SelectList(_context.Studenti, "Id", "Id", prestito.Matricola);
            return View(prestito);
        }

        // GET: Prestiti/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var prestito = await _context.Prestiti
                .Include(p => p.IdLibroNavigation)
                .Include(p => p.MatricolaNavigation)
                .FirstOrDefaultAsync(m => m.Id == id);
            if (prestito == null)
            {
                return NotFound();
            }

            return View(prestito);
        }

        // POST: Prestiti/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var prestito = await _context.Prestiti.FindAsync(id);
            if (prestito != null)
            {
                _context.Prestiti.Remove(prestito);
            }

            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool PrestitoExists(int id)
        {
            return _context.Prestiti.Any(e => e.Id == id);
        }
    }
}
