using BikeStores.Data.Models;
using Microsoft.EntityFrameworkCore;
using System.Text.Json.Serialization;

namespace BikeStores.WebAPI;

public class Program
{
    public static void Main(string[] args)
    {
        var builder = WebApplication.CreateBuilder(args);

        // Stringa di connessione
        var connectionString = builder.Configuration.GetConnectionString("BikeStoreConnection")
            ?? throw new InvalidOperationException("Connection string 'BikeStoreConnection' not found.");

        // DbContext business
        builder.Services.AddDbContext<BikeStoresContext>(options =>
            options.UseSqlServer(connectionString));

        // Controller con gestione cicli JSON
        builder.Services.AddControllers()
            .AddJsonOptions(options =>
            {
                options.JsonSerializerOptions.ReferenceHandler = ReferenceHandler.IgnoreCycles;
            });

        builder.Services.AddOpenApi();

        // CORS per app mobile
        builder.Services.AddCors(options =>
        {
            options.AddPolicy("AllowAll", policy =>
            {
                policy.AllowAnyOrigin()
                      .AllowAnyMethod()
                      .AllowAnyHeader();
            });
        });

        var app = builder.Build();

        if (app.Environment.IsDevelopment())
        {
            app.MapOpenApi();
        }

        app.UseCors("AllowAll");
        app.UseAuthorization();
        app.MapControllers();

        app.Run();
    }
}
