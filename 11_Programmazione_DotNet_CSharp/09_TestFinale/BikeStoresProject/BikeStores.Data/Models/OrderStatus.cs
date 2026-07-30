using System;
using System.Collections.Generic;

namespace BikeStores.Data.Models;

public partial class OrderStatus
{
    public byte StatusId { get; set; }

    public string StatusName { get; set; } = null!;
}
