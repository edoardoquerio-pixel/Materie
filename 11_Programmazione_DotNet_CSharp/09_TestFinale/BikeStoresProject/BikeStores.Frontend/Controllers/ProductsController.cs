using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using BikeStores.Data.Models;

namespace BikeStores.Frontend.Controllers
{
    public class ProductsController : Controller
    {
        private readonly BikeStoresContext _context;

        public ProductsController(BikeStoresContext context)
        {
            _context = context;
        }

        // GET: Products
        public async Task<IActionResult> Index(string? search)
        {
            // base query with Include for navigation properties
            var products = _context.Products
                .Include(p => p.Brand)
                .Include(p => p.Category)
                .AsQueryable();

            // filter by product name, brand or category
            if (search != null)
                products = products.Where(p =>
                    p.ProductName.Contains(search) ||
                    p.Brand.BrandName.Contains(search) ||
                    p.Category.CategoryName.Contains(search)
                );

            ViewBag.Search = search;

            return View(await products.OrderBy(p => p.ProductName).ToListAsync());
        }

        // GET: Products/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
                return NotFound();

            var product = await _context.Products
                .Include(p => p.Brand)
                .Include(p => p.Category)
                .Include(p => p.Stocks)
                .FirstOrDefaultAsync(p => p.ProductId == id);

            if (product == null)
                return NotFound();

            // calculate total available quantity from stocks
            ViewBag.QuantityAvailable = product.Stocks.Sum(s => s.Quantity ?? 0);

            return View(product);
        }
    }
}
