using BikeStores.Data.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace BikeStores.WebAPI.Controllers;

[Route("api/[controller]")]
[ApiController]
public class ProductsController : ControllerBase
{
    private readonly BikeStoresContext _context;

    public ProductsController(BikeStoresContext context)
    {
        _context = context;
    }

    // GET: api/Products
    // GET: api/Products?modelYear=2023&brandId=1&categoryId=2&search=bike
    [HttpGet]
    public async Task<ActionResult<IEnumerable<Product>>> GetProducts(
        [FromQuery] short? modelYear,
        [FromQuery] int? brandId,
        [FromQuery] int? categoryId,
        [FromQuery] string? search)
    {
        var query = _context.Products
            .Include(p => p.Brand)
            .Include(p => p.Category)
            .AsNoTracking()
            .AsQueryable();

        if (modelYear.HasValue)
            query = query.Where(p => p.ModelYear == modelYear.Value);

        if (brandId.HasValue)
            query = query.Where(p => p.BrandId == brandId.Value);

        if (categoryId.HasValue)
            query = query.Where(p => p.CategoryId == categoryId.Value);

        if (!string.IsNullOrWhiteSpace(search))
            query = query.Where(p => p.ProductName.Contains(search));

        return await query
            .OrderBy(p => p.ProductName)
            .ToListAsync();
    }

    // GET: api/Products/5
    [HttpGet("{id}")]
    public async Task<ActionResult<Product>> GetProduct(int id)
    {
        var product = await _context.Products
            .Include(p => p.Brand)
            .Include(p => p.Category)
            .AsNoTracking()
            .FirstOrDefaultAsync(p => p.ProductId == id);

        if (product == null)
            return NotFound();

        return product;
    }
}
