using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;
using BikeStores.Data.Models;

namespace BikeStores.Backend.Data
{
    public static class IdentitySeed
    {
        public static async Task SeedAsync(IServiceProvider serviceProvider)
        {
            using var scope = serviceProvider.CreateScope();
            var sp = scope.ServiceProvider;

            var userManager = sp.GetRequiredService<UserManager<IdentityUser>>();
            var roleManager = sp.GetRequiredService<RoleManager<IdentityRole>>();
            var bikeStoresContext = sp.GetRequiredService<BikeStoresContext>();

            string[] roleNames = ["Administrators", "Employees", "Customers"];
            foreach (var roleName in roleNames)
            {
                if (!await roleManager.RoleExistsAsync(roleName))
                {
                    await roleManager.CreateAsync(new IdentityRole(roleName));
                }
            }

            // Admin
            await CreateUserIfNotExists(userManager, "admin@bikes.shop", "@Bike-2026", "Administrators");

            // Staff -> Employees
            var staffs = await bikeStoresContext.Staffs.AsNoTracking().ToListAsync();
            foreach (var staff in staffs)
            {
                await CreateUserIfNotExists(userManager, staff.Email, "@Bike-2026", "Employees");
            }

            // Customers -> Customers
            var customers = await bikeStoresContext.Customers.AsNoTracking().ToListAsync();
            foreach (var customer in customers)
            {
                await CreateUserIfNotExists(userManager, customer.Email, "@Bike-2026", "Customers");
            }
        }

        private static async Task CreateUserIfNotExists(UserManager<IdentityUser> userManager, string email, string password, string role)
        {
            if (await userManager.FindByEmailAsync(email) != null)
                return;

            var user = new IdentityUser
            {
                UserName = email,
                Email = email,
                EmailConfirmed = true
            };

            var result = await userManager.CreateAsync(user, password);
            if (result.Succeeded)
            {
                await userManager.AddToRoleAsync(user, role);
            }
        }
    }
}
