using BikeStores.Data.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace BikeStores.Backend.Controllers
{
    [Authorize]
    public class HomeController : Controller
    {
        private readonly BikeStoresContext _context;

        public HomeController(BikeStoresContext context)
        {
            _context = context;
        }

        public IActionResult Index()
        {
            if (User.IsInRole("Administrators"))
            {
                ViewBag.TotalProducts = _context.Products.Count();
                ViewBag.TotalOrders = _context.Orders.Count();
                ViewBag.TotalCustomers = _context.Customers.Count();
                ViewBag.TotalStores = _context.Stores.Count();
                return View("DashboardAdmin");
            }

            if (User.IsInRole("Employees"))
            {
                var staff = _context.Staffs.FirstOrDefault(s => s.Email == User.Identity!.Name);
                ViewBag.MyOrders = staff != null
                    ? _context.Orders.Count(o => o.StaffId == staff.StaffId)
                    : 0;
                ViewBag.TotalCustomers = _context.Customers.Count();
                return View("DashboardEmployee");
            }

            if (User.IsInRole("Customers"))
            {
                var customer = _context.Customers.FirstOrDefault(c => c.Email == User.Identity!.Name);
                ViewBag.MyOrders = customer != null
                    ? _context.Orders.Count(o => o.CustomerId == customer.CustomerId)
                    : 0;
                return View("DashboardCustomer");
            }

            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View("Error");
        }
    }
}
