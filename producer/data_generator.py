import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

STORES = ["Store_A", "Store_B", "Store_C"]
CATEGORIES = ["Electronics", "Apparel", "Grocery", "Home"]
REGIONS = ["North", "South", "East", "West"]

def generate_transaction():
    revenue = random.gauss(5000, 800)
    if random.random() < 0.10:
        revenue = random.choice([revenue * 5, revenue * 0.1])
    return {
        "timestamp": datetime.now().isoformat(),
        "store_id": random.choice(STORES),
        "product_category": random.choice(CATEGORIES),
        "revenue": round(revenue, 2),
        "units_sold": random.randint(1, 200),
        "region": random.choice(REGIONS)
    }

print("Producing transactions... Ctrl+C to stop")
while True:
    txn = generate_transaction()
    producer.send("transactions_topic", txn)
    print(f"Sent: {txn}")
    time.sleep(1)