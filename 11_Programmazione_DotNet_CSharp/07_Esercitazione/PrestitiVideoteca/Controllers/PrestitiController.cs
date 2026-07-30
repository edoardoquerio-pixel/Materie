using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using PrestitiVideoteca.Models;

namespace PrestitiVideoteca.Controllers
{
    public class PrestitiController : Controller
    {
        private readonly PrestitiVideotecaContext _context;

        public PrestitiController(PrestitiVideotecaContext context)
        {
            _context = context;
        }

        // GET: Prestiti
        public async Task<IActionResult> Index(string? search, int? pageNumber)
        {
            int pageSize = 100;
            var prestitiVideotecaContext = _context.Prestiti
                .Include(p => p.IdFilmNavigation)
                .Include(p => p.MatricolaNavigation)
                .AsQueryable();

            if (search != null)
                prestitiVideotecaContext = prestitiVideotecaContext.Where(p => p.IdFilmNavigation.Titolo!.Contains(search) || p.MatricolaNavigation.Cognome!.Contains(search) || p.MatricolaNavigation.Nome!.Contains(search));

            int totalRecords = await prestitiVideotecaContext.CountAsync();
            ViewBag.TotalRecords = totalRecords;
            ViewBag.Search = search;
            ViewBag.PageNumber = pageNumber ?? 1;
            ViewBag.TotalPages = totalRecords > 0 ? (int)Math.Ceiling((double)totalRecords / pageSize) : 1;

            prestitiVideotecaContext = prestitiVideotecaContext.OrderByDescending(p => p.DataPrestito);
            var result = await prestitiVideotecaContext
                .Skip(((pageNumber ?? 1) - 1) * pageSize)
                .Take(pageSize)
                .ToListAsync();

            return View(result);
        }

        // GET: Prestiti/ArchivioPrestiti
        public async Task<IActionResult> ArchivioPrestiti(string? search, int? pageNumber)
        {
            int pageSize = 100;
            var prestitiVideotecaContext = _context.Prestiti
                .Include(p => p.IdFilmNavigation)
                .Include(p => p.MatricolaNavigation)
                .Where(p => p.DataRestituzione != null)
                .AsQueryable();

            if (search != null)
                prestitiVideotecaContext = prestitiVideotecaContext.Where(p => p.IdFilmNavigation.Titolo!.Contains(search) || p.MatricolaNavigation.Cognome!.Contains(search) || p.MatricolaNavigation.Nome!.Contains(search));

            int totalRecords = await prestitiVideotecaContext.CountAsync();
            ViewBag.TotalRecords = totalRecords;
            ViewBag.Search = search;
            ViewBag.PageNumber = pageNumber ?? 1;
            ViewBag.TotalPages = totalRecords == 0 ? 1 : (int)Math.Ceiling((double)totalRecords / pageSize);

            prestitiVideotecaContext = prestitiVideotecaContext.OrderByDescending(p => p.DataPrestito);
            var result = await prestitiVideotecaContext
                .Skip(((pageNumber ?? 1) - 1) * pageSize)
                .Take(pageSize)
                .ToListAsync();

            return View(result);
        }

        // GET: Prestiti/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var prestito = await _context.Prestiti
                .Include(p => p.IdFilmNavigation)
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
            ViewData["IdFilm"] = new SelectList(_context.Film, "Codice", "Titolo");
            ViewData["Matricola"] = new SelectList(_context.Studenti, "Matricola", "Nominativo");
            return View();
        }

        // POST: Prestiti/Create
        // Per proteggere da attacchi di overposting, abilitare le proprietà specifiche a cui si vuole fare il binding.
        // Per maggiori dettagli, vedere http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,IdFilm,Matricola")] Prestito prestito)
        {
            try
            {
                _context.Add(prestito);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            catch (Exception)
            {
                ViewData["IdFilm"] = new SelectList(_context.Film, "Codice", "Titolo", prestito.IdFilm);
                ViewData["Matricola"] = new SelectList(_context.Studenti, "Matricola", "Nominativo", prestito.Matricola);
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
            ViewData["IdFilm"] = new SelectList(_context.Film, "Codice", "Titolo", prestito.IdFilm);
            ViewData["Matricola"] = new SelectList(_context.Studenti, "Matricola", "Nominativo", prestito.Matricola);
            return View(prestito);
        }

        // POST: Prestiti/Edit/5
        // Per proteggere da attacchi di overposting, abilitare le proprietà specifiche a cui si vuole fare il binding.
        // Per maggiori dettagli, vedere http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,IdFilm,Matricola,DataPrestito,DataRestituzione")] Prestito prestito)
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
            ViewData["IdFilm"] = new SelectList(_context.Film, "Codice", "Titolo", prestito.IdFilm);
            ViewData["Matricola"] = new SelectList(_context.Studenti, "Matricola", "Nominativo", prestito.Matricola);
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
                .Include(p => p.IdFilmNavigation)
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


