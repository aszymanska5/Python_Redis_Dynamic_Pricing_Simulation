# Redis Dynamic Pricing Simulation

This is a simple simulation of dynamic pricing logic using Redis, inspired by real-world implementations like Uber.

The simulation adjusts prices in four virtual zones (`zone_A` to `zone_D`) based on changing demand and supply. Redis is used to store and update the data in real-time.

## Project Context
This project was created as part of a university consulting project focused on Redis as a modern data solution.<br>
My role: team leader and author of the technical simulation.

## Technologies Used

- Python 3
- Redis (run via Docker)
- Docker CLI

## Key Concepts

- **Dynamic Pricing** – Prices increase with higher demand or lower supply.
- **Redis TTL** – Prices are temporary and auto-expire (simulate real-time updates).
- **Key-Value Store** – Redis stores price, demand, and supply for each zone.

## Example Output
```csharp
[12:00:00] zone_A: Demand=80, Supply=50, Price=16.0 
[12:01:00] zone_B: Demand=45, Supply=90, Price=5.0
...
```

## How to Run

1. **Start Redis in Docker on port 6380**:
   ```bash
   docker run -d -p 6380:6379 redis

2. **Run the script**:
   ```bash
   python dynamic_pricing_redis.py
   
The script will simulate demand and supply for each zone and update the price every 60 seconds.
