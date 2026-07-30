using BikeStores.Data.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;

namespace BikeStores.Backend.Controllers
{
    [Authorize(Roles = "Administrators, Employees, Customers")]
    public class OrdersController : Controller
    {
        private readonly BikeStoresContext _context;

        public OrdersController(BikeStoresContext context)
        {
            _context = context;
        }

        // GET: Orders
        public async Task<IActionResult> Index(byte? statusId)
        {
            //carica lista stati ordine per filtro
            var statuses = await _context.OrderStatuses.OrderBy(s => s.StatusId).ToListAsync();
            ViewData["Statuses"] = new SelectList(statuses, "StatusId", "StatusName", statusId);
            ViewBag.SearchStatus = statusId;

            IQueryable<Order> query = _context.Orders
                .Include(o => o.Customer)
                .Include(o => o.Store)
                .AsNoTracking();

            //filtro per ruolo: Employees vede solo propri ordini
            if (User.IsInRole("Employees"))
            {
                var staff = await _context.Staffs.FirstOrDefaultAsync(s => s.Email == User.Identity!.Name);
                if (staff != null)
                {
                    query = query.Where(o => o.StaffId == staff.StaffId);
                }
            }

            //filtro per ruolo: Customers vede solo propri ordini
            if (User.IsInRole("Customers"))
            {
                var customer = await _context.Customers.FirstOrDefaultAsync(c => c.Email == User.Identity!.Name);
                if (customer != null)
                {
                    query = query.Where(o => o.CustomerId == customer.CustomerId);
                }
            }

            if (statusId.HasValue)
            {
                query = query.Where(o => o.OrderStatus == statusId.Value);
            }

            var orders = await query
                .OrderByDescending(o => o.OrderDate)
                .ToListAsync();

            return View(orders);
        }

        // GET: Orders/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
                return NotFound();

            var order = await _context.Orders
                .Include(o => o.Customer)
                .Include(o => o.Staff)
                .Include(o => o.Store)
                .AsNoTracking()
                .FirstOrDefaultAsync(o => o.OrderId == id);

            if (order == null)
                return NotFound();

            //filtro per ruolo: Employees vede solo propri ordini
            if (User.IsInRole("Employees"))
            {
                var staff = await _context.Staffs.FirstOrDefaultAsync(s => s.Email == User.Identity!.Name);
                if (staff == null || order.StaffId != staff.StaffId)
                    return Forbid();
            }

            //filtro per ruolo: Customers vede solo propri ordini
            if (User.IsInRole("Customers"))
            {
                var customer = await _context.Customers.FirstOrDefaultAsync(c => c.Email == User.Identity!.Name);
                if (customer == null || order.CustomerId != customer.CustomerId)
                    return Forbid();
            }

            var items = await _context.OrderItems
                .Include(oi => oi.Product)
                .AsNoTracking()
                .Where(oi => oi.OrderId == id)
                .OrderBy(oi => oi.ItemId)
                .ToListAsync();

            var statusName = await _context.OrderStatuses
                .AsNoTracking()
                .Where(s => s.StatusId == order.OrderStatus)
                .Select(s => s.StatusName)
                .FirstOrDefaultAsync();

            ViewBag.StatusName = statusName ?? "Unknown";
            ViewBag.Items = items;

            return View(order);
        }

        // GET: Orders/Create
        public IActionResult Create()
        {
            ViewData["CustomerId"] = new SelectList(_context.Customers.OrderBy(c => c.LastName).ThenBy(c => c.FirstName), "CustomerId", "Email");
            ViewData["StoreId"] = new SelectList(_context.Stores.OrderBy(s => s.StoreName), "StoreId", "StoreName");
            ViewData["StaffId"] = new SelectList(_context.Staffs.OrderBy(s => s.LastName).ThenBy(s => s.FirstName), "StaffId", "Email");
            ViewData["OrderStatus"] = new SelectList(_context.OrderStatuses, "StatusId", "StatusName");
            return View();
        }

        // POST: Orders/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("CustomerId,StoreId,StaffId,OrderStatus,OrderDate,RequiredDate,ShippedDate")] Order order)
        {
            if (ModelState.IsValid)
            {
                try
                {
                    _context.Orders.Add(order);
                    await _context.SaveChangesAsync();
                    return RedirectToAction(nameof(Index));
                }
                catch (Exception)
                {
                    ModelState.AddModelError("", "Errore durante il salvataggio. Riprova.");
                }
            }
            ViewData["CustomerId"] = new SelectList(_context.Customers.OrderBy(c => c.LastName).ThenBy(c => c.FirstName), "CustomerId", "Email", order.CustomerId);
            ViewData["StoreId"] = new SelectList(_context.Stores.OrderBy(s => s.StoreName), "StoreId", "StoreName", order.StoreId);
            ViewData["StaffId"] = new SelectList(_context.Staffs.OrderBy(s => s.LastName).ThenBy(s => s.FirstName), "StaffId", "Email", order.StaffId);
            ViewData["OrderStatus"] = new SelectList(_context.OrderStatuses, "StatusId", "StatusName", order.OrderStatus);
            return View(order);
        }

        // GET: Orders/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
                return NotFound();

            var order = await _context.Orders.FindAsync(id);
            if (order == null)
                return NotFound();

            ViewData["CustomerId"] = new SelectList(_context.Customers.OrderBy(c => c.LastName).ThenBy(c => c.FirstName), "CustomerId", "Email", order.CustomerId);
            ViewData["StoreId"] = new SelectList(_context.Stores.OrderBy(s => s.StoreName), "StoreId", "StoreName", order.StoreId);
            ViewData["StaffId"] = new SelectList(_context.Staffs.OrderBy(s => s.LastName).ThenBy(s => s.FirstName), "StaffId", "Email", order.StaffId);
            ViewData["OrderStatus"] = new SelectList(_context.OrderStatuses, "StatusId", "StatusName", order.OrderStatus);
            return View(order);
        }

        // POST: Orders/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("OrderId,CustomerId,StoreId,StaffId,OrderStatus,OrderDate,RequiredDate,ShippedDate")] Order order)
        {
            if (id != order.OrderId)
                return NotFound();

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Orders.Update(order);
                    await _context.SaveChangesAsync();
                    return RedirectToAction(nameof(Index));
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!OrderExists(order.OrderId))
                        return NotFound();
                    throw;
                }
            }
            ViewData["CustomerId"] = new SelectList(_context.Customers.OrderBy(c => c.LastName).ThenBy(c => c.FirstName), "CustomerId", "Email", order.CustomerId);
            ViewData["StoreId"] = new SelectList(_context.Stores.OrderBy(s => s.StoreName), "StoreId", "StoreName", order.StoreId);
            ViewData["StaffId"] = new SelectList(_context.Staffs.OrderBy(s => s.LastName).ThenBy(s => s.FirstName), "StaffId", "Email", order.StaffId);
            ViewData["OrderStatus"] = new SelectList(_context.OrderStatuses, "StatusId", "StatusName", order.OrderStatus);
            return View(order);
        }

        // GET: Orders/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
                return NotFound();

            var order = await _context.Orders
                .Include(o => o.Customer)
                .Include(o => o.Store)
                .Include(o => o.Staff)
                .AsNoTracking()
                .FirstOrDefaultAsync(m => m.OrderId == id);
            if (order == null)
                return NotFound();

            return View(order);
        }

        // POST: Orders/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var order = await _context.Orders.FindAsync(id);
            if (order != null)
            {
                _context.Orders.Remove(order);
                await _context.SaveChangesAsync();
            }
            return RedirectToAction(nameof(Index));
        }

        private bool OrderExists(int id)
        {
            return _context.Orders.Any(e => e.OrderId == id);
        }
    }
}
