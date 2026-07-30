using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using BikeStores.Data.Models;

namespace BikeStores.Frontend.Controllers
{
    public class StoresController : Controller
    {
        private readonly BikeStoresContext _context;

        public StoresController(BikeStoresContext context)
        {
            _context = context;
        }

        // GET: Stores
        public async Task<IActionResult> Index()
        {
            return View(await _context.Stores.OrderBy(s => s.StoreName).ToListAsync());
        }

        // GET: Stores/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
                return NotFound();

            var store = await _context.Stores
                .Include(s => s.Staff) // Include for staff grid in the view
                .FirstOrDefaultAsync(s => s.StoreId == id);

            if (store == null)
                return NotFound();

            return View(store);
        }
    }
}
