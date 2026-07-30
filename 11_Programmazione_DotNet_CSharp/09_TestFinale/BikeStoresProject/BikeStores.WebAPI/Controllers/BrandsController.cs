using BikeStores.Data.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace BikeStores.WebAPI.Controllers;

[Route("api/[controller]")]
[ApiController]
public class BrandsController : ControllerBase
{
    private readonly BikeStoresContext _context;

    public BrandsController(BikeStoresContext context)
    {
        _context = context;
    }

    // GET: api/Brands
    [HttpGet]
    public async Task<ActionResult<IEnumerable<Brand>>> GetBrands()
    {
        return await _context.Brands
            .AsNoTracking()
            .OrderBy(b => b.BrandName)
            .ToListAsync();
    }

    // GET: api/Brands/5
    [HttpGet("{id}")]
    public async Task<ActionResult<Brand>> GetBrand(int id)
    {
        var brand = await _context.Brands
            .AsNoTracking()
            .FirstOrDefaultAsync(b => b.BrandId == id);

        if (brand == null)
            return NotFound();

        return brand;
    }
}
