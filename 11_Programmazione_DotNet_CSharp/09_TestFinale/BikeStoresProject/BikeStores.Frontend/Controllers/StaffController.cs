using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using BikeStores.Data.Models;

namespace BikeStores.Frontend.Controllers
{
    public class StaffController : Controller
    {
        private readonly BikeStoresContext _context;

        public StaffController(BikeStoresContext context)
        {
            _context = context;
        }

        // GET: Staff/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
                return NotFound();

            var staff = await _context.Staffs
                .Include(s => s.Store) // Include for store name
                .Include(s => s.Manager) // Include for manager name
                .FirstOrDefaultAsync(s => s.StaffId == id);

            if (staff == null)
                return NotFound();

            return View(staff);
        }
    }
}
