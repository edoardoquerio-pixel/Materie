using BikeStores.Data.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;

namespace BikeStores.Backend.Controllers
{
    [Authorize(Roles = "Administrators")]
    public class StaffController : Controller
    {
        private readonly BikeStoresContext _context;

        public StaffController(BikeStoresContext context)
        {
            _context = context;
        }

        // GET: Staff
        public async Task<IActionResult> Index()
        {
            var staff = await _context.Staffs
                .Include(s => s.Store)
                .AsNoTracking()
                .OrderBy(s => s.LastName)
                .ThenBy(s => s.FirstName)
                .ToListAsync();
            return View(staff);
        }

        // GET: Staff/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
                return NotFound();

            var staff = await _context.Staffs
                .Include(s => s.Store)
                .AsNoTracking()
                .FirstOrDefaultAsync(m => m.StaffId == id);
            if (staff == null)
                return NotFound();

            return View(staff);
        }

        // GET: Staff/Create
        public IActionResult Create()
        {
            ViewData["StoreId"] = new SelectList(_context.Stores, "StoreId", "StoreName");
            ViewData["ManagerId"] = new SelectList(_context.Staffs, "StaffId", "Email");
            return View();
        }

        // POST: Staff/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("FirstName,LastName,Email,Phone,Active,StoreId,ManagerId")] Staff staff)
        {
            if (ModelState.IsValid)
            {
                try
                {
                    _context.Staffs.Add(staff);
                    await _context.SaveChangesAsync();
                    return RedirectToAction(nameof(Index));
                }
                catch (Exception)
                {
                    ModelState.AddModelError("", "Errore durante il salvataggio. Riprova.");
                }
            }
            ViewData["StoreId"] = new SelectList(_context.Stores, "StoreId", "StoreName", staff.StoreId);
            ViewData["ManagerId"] = new SelectList(_context.Staffs, "StaffId", "Email", staff.ManagerId);
            return View(staff);
        }

        // GET: Staff/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
                return NotFound();

            var staff = await _context.Staffs.FindAsync(id);
            if (staff == null)
                return NotFound();

            ViewData["StoreId"] = new SelectList(_context.Stores, "StoreId", "StoreName", staff.StoreId);
            ViewData["ManagerId"] = new SelectList(_context.Staffs, "StaffId", "Email", staff.ManagerId);
            return View(staff);
        }

        // POST: Staff/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("StaffId,FirstName,LastName,Email,Phone,Active,StoreId,ManagerId")] Staff staff)
        {
            if (id != staff.StaffId)
                return NotFound();

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Staffs.Update(staff);
                    await _context.SaveChangesAsync();
                    return RedirectToAction(nameof(Index));
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!StaffExists(staff.StaffId))
                        return NotFound();
                    throw;
                }
            }
            ViewData["StoreId"] = new SelectList(_context.Stores, "StoreId", "StoreName", staff.StoreId);
            ViewData["ManagerId"] = new SelectList(_context.Staffs, "StaffId", "Email", staff.ManagerId);
            return View(staff);
        }

        // GET: Staff/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
                return NotFound();

            var staff = await _context.Staffs
                .Include(s => s.Store)
                .AsNoTracking()
                .FirstOrDefaultAsync(m => m.StaffId == id);
            if (staff == null)
                return NotFound();

            return View(staff);
        }

        // POST: Staff/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var staff = await _context.Staffs.FindAsync(id);
            if (staff != null)
            {
                _context.Staffs.Remove(staff);
                await _context.SaveChangesAsync();
            }
            return RedirectToAction(nameof(Index));
        }

        private bool StaffExists(int id)
        {
            return _context.Staffs.Any(e => e.StaffId == id);
        }
    }
}
