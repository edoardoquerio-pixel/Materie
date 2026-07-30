using BikeStores.Data.Models;

namespace BikeStores.Backend.Models;

public class OrderDetailViewModel
{
    public Order Order { get; set; } = null!;
    public List<OrderItemViewModel> Items { get; set; } = [];
    public decimal OrderTotal => Items.Sum(i => i.SubTotal);
}

public class OrderItemViewModel
{
    public string ProductName { get; set; } = null!;
    public int Quantity { get; set; }
    public decimal ListPrice { get; set; }
    public decimal Discount { get; set; }
    public decimal TotalPrice => Quantity * ListPrice;
    public decimal DiscountTotal => Quantity * ListPrice * Discount;
    public decimal SubTotal => Quantity * ListPrice * (1 - Discount);
}
