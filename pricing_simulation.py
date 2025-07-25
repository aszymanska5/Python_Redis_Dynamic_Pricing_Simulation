import redis
import time
import random
from datetime import datetime

r = redis.Redis(host='localhost', port=6380, decode_responses=True)

zones = ["zone_A", "zone_B", "zone_C", "zone_D"]

def initialize_zones():
    for zone in zones:
        r.set(f"price:{zone}", 10.0)
        r.set(f"demand:{zone}", 50)
        r.set(f"supply:{zone}", 50)

def calculate_price(demand, supply, base_price=10.0):
    if supply == 0:
        return round(base_price * 2, 2)
    ratio = demand / supply
    return round(base_price * ratio, 2)

def simulate_demand_supply():
    for zone in zones:
        demand = random.randint(30, 100)
        supply = random.randint(30, 100)
        price = calculate_price(demand, supply)

        r.set(f"demand:{zone}", demand)
        r.set(f"supply:{zone}", supply)
        r.set(f"price:{zone}", price, ex=60)  

        print(f"[{datetime.now().strftime('%H:%M:%S')}] {zone}: Demand={demand}, Supply={supply}, Price={price}")

        
def main():
    initialize_zones()
    for _ in range(5):
        simulate_demand_supply()
        time.sleep(60)

if __name__ == "__main__":
    main()
