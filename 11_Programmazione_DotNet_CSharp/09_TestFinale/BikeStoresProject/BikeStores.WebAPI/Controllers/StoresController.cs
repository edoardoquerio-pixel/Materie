using BikeStores.Data.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace BikeStores.WebAPI.Controllers;

[Route("api/[controller]")]
[ApiController]
public class StoresController : ControllerBase
{
    private readonly BikeStoresContext _context;

    public StoresController(BikeStoresContext context)
    {
        _context = context;
    }

    // GET: api/Stores
    [HttpGet]
    public async Task<ActionResult<IEnumerable<Store>>> GetStores()
    {
        return await _context.Stores
            .AsNoTracking()
            .OrderBy(s => s.StoreName)
            .ToListAsync();
    }

    // GET: api/Stores/5
    [HttpGet("{id}")]
    public async Task<ActionResult<Store>> GetStore(int id)
    {
        var store = await _context.Stores
            .AsNoTracking()
            .FirstOrDefaultAsync(s => s.StoreId == id);

        if (store == null)
            return NotFound();

        return store;
    }
}
