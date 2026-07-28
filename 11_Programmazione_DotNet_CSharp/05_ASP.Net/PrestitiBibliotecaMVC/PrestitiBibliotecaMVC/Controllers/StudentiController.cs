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
    public class StudentiController : Controller
    {
        private readonly PrestitiBibliotecaMvcContext _context;

        public StudentiController(PrestitiBibliotecaMvcContext context)
        {
            _context = context;
        }

        // GET: Studenti
        public async Task<IActionResult> Index(string? search)
        {

            var lista = _context.Studenti.AsQueryable(); //creo una query che prende tutti gli studenti per filtro

            if(search!=null)
                lista= lista.Where(s => s.Classe!.Contains(search) || s.Cognome!.Contains(search) || s.Nome!.Contains(search)); //filtro la query per classe

            ViewBag.Search = search; //passo la classe alla view per mantenere il valore nel form

            return View(await lista.ToListAsync());
        }

        // GET: Studenti/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var studente = await _context.Studenti
                .FirstOrDefaultAsync(m => m.Id == id);
            if (studente == null)
            {
                return NotFound();
            }

            return View(studente);
        }

        // GET: Studenti/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Studenti/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Nome,Cognome,Email,Classe")] Studente studente)
        {
            if (ModelState.IsValid)
            {
                _context.Add(studente);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(studente);
        }

        // GET: Studenti/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var studente = await _context.Studenti.FindAsync(id);
            if (studente == null)
            {
                return NotFound();
            }
            return View(studente);
        }

        // POST: Studenti/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Nome,Cognome,Email,Classe")] Studente studente)
        {
            if (id != studente.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(studente);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!StudenteExists(studente.Id))
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
            return View(studente);
        }

        // GET: Studenti/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var studente = await _context.Studenti
                .FirstOrDefaultAsync(m => m.Id == id);
            if (studente == null)
            {
                return NotFound();
            }

            return View(studente);
        }

        // POST: Studenti/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var studente = await _context.Studenti.FindAsync(id);
            if (studente != null)
            {
                _context.Studenti.Remove(studente);
            }

            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool StudenteExists(int id)
        {
            return _context.Studenti.Any(e => e.Id == id);
        }
    }
}
