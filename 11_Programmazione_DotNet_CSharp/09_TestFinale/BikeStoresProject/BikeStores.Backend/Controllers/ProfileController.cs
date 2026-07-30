using BikeStores.Data.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace BikeStores.Backend.Controllers
{
    [Authorize(Roles = "Customers")]
    public class ProfileController : Controller
    {
        private readonly BikeStoresContext _context;

        public ProfileController(BikeStoresContext context)
        {
            _context = context;
        }

        public async Task<IActionResult> Index()
        {
            var customer = await _context.Customers
                .AsNoTracking()
                .FirstOrDefaultAsync(c => c.Email == User.Identity!.Name);

            if (customer == null)
                return NotFound();

            return View(customer);
        }

        public async Task<IActionResult> Edit()
        {
            var customer = await _context.Customers
                .AsNoTracking()
                .FirstOrDefaultAsync(c => c.Email == User.Identity!.Name);

            if (customer == null)
                return NotFound();

            return View(customer);
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit([Bind("FirstName,LastName,Phone,Street,City,State,ZipCode")] Customer input)
        {
            var customer = await _context.Customers
                .FirstOrDefaultAsync(c => c.Email == User.Identity!.Name);

            if (customer == null)
                return NotFound();

            if (ModelState.IsValid)
            {
                customer.FirstName = input.FirstName;
                customer.LastName = input.LastName;
                customer.Phone = input.Phone;
                customer.Street = input.Street;
                customer.City = input.City;
                customer.State = input.State;
                customer.ZipCode = input.ZipCode;

                try
                {
                    await _context.SaveChangesAsync();
                    return RedirectToAction(nameof(Index));
                }
                catch (Exception)
                {
                    ModelState.AddModelError("", "Errore durante il salvataggio. Riprova.");
                }
            }

            return View(input);
        }
    }
}
