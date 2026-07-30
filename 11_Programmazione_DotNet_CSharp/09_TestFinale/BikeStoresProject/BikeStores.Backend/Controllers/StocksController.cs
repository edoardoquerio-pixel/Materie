using BikeStores.Data.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;

namespace BikeStores.Backend.Controllers
{
    [Authorize(Roles = "Administrators")]
    public class StocksController : Controller
    {
        private readonly BikeStoresContext _context;

        public StocksController(BikeStoresContext context)
        {
            _context = context;
        }

        // GET: Stocks
        public async Task<IActionResult> Index(string? filter)
        {
            ViewBag.Filter = filter;

            IQueryable<Stock> query = _context.Stocks
                .Include(s => s.Product)
                .Include(s => s.Store)
                .AsNoTracking();

            query = filter switch
            {
                "out" => query.Where(s => s.Quantity == 0),
                "low" => query.Where(s => s.Quantity >= 1 && s.Quantity <= 9),
                _ => query
            };

            var stocks = await query
                .OrderBy(s => s.Store!.StoreName)
                .ThenBy(s => s.Product!.ProductName)
                .ToListAsync();

            return View(stocks);
        }

        // GET: Stocks/Create
        public IActionResult Create()
        {
            ViewData["StoreId"] = new SelectList(_context.Stores.OrderBy(s => s.StoreName), "StoreId", "StoreName");
            ViewData["ProductId"] = new SelectList(_context.Products.OrderBy(p => p.ProductName), "ProductId", "ProductName");
            return View();
        }

        // POST: Stocks/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("StoreId,ProductId,Quantity")] Stock stock)
        {
            if (ModelState.IsValid)
            {
                try
                {
                    _context.Stocks.Add(stock);
                    await _context.SaveChangesAsync();
                    return RedirectToAction(nameof(Index));
                }
                catch (Exception)
                {
                    ModelState.AddModelError("", "Errore durante il salvataggio. Riprova.");
                }
            }
            ViewData["StoreId"] = new SelectList(_context.Stores.OrderBy(s => s.StoreName), "StoreId", "StoreName", stock.StoreId);
            ViewData["ProductId"] = new SelectList(_context.Products.OrderBy(p => p.ProductName), "ProductId", "ProductName", stock.ProductId);
            return View(stock);
        }

        // GET: Stocks/Edit/5
        public async Task<IActionResult> Edit(int? storeId, int? productId)
        {
            if (storeId == null || productId == null)
                return NotFound();

            var stock = await _context.Stocks.FindAsync(storeId.Value, productId.Value);
            if (stock == null)
                return NotFound();

            ViewData["StoreId"] = new SelectList(_context.Stores.OrderBy(s => s.StoreName), "StoreId", "StoreName", stock.StoreId);
            ViewData["ProductId"] = new SelectList(_context.Products.OrderBy(p => p.ProductName), "ProductId", "ProductName", stock.ProductId);
            return View(stock);
        }

        // POST: Stocks/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int storeId, int productId, [Bind("StoreId,ProductId,Quantity")] Stock stock)
        {
            if (storeId != stock.StoreId || productId != stock.ProductId)
                return NotFound();

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Stocks.Update(stock);
                    await _context.SaveChangesAsync();
                    return RedirectToAction(nameof(Index));
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!StockExists(stock.StoreId, stock.ProductId))
                        return NotFound();
                    throw;
                }
            }
            ViewData["StoreId"] = new SelectList(_context.Stores.OrderBy(s => s.StoreName), "StoreId", "StoreName", stock.StoreId);
            ViewData["ProductId"] = new SelectList(_context.Products.OrderBy(p => p.ProductName), "ProductId", "ProductName", stock.ProductId);
            return View(stock);
        }

        // GET: Stocks/Delete/5
        public async Task<IActionResult> Delete(int? storeId, int? productId)
        {
            if (storeId == null || productId == null)
                return NotFound();

            var stock = await _context.Stocks
                .Include(s => s.Product)
                .Include(s => s.Store)
                .AsNoTracking()
                .FirstOrDefaultAsync(s => s.StoreId == storeId.Value && s.ProductId == productId.Value);
            if (stock == null)
                return NotFound();

            return View(stock);
        }

        // POST: Stocks/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int storeId, int productId)
        {
            var stock = await _context.Stocks.FindAsync(storeId, productId);
            if (stock != null)
            {
                _context.Stocks.Remove(stock);
                await _context.SaveChangesAsync();
            }
            return RedirectToAction(nameof(Index));
        }

        private bool StockExists(int storeId, int productId)
        {
            return _context.Stocks.Any(e => e.StoreId == storeId && e.ProductId == productId);
        }
    }
}
