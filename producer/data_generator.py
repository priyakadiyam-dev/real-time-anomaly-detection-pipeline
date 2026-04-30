import sqlite3
import random
import time
import numpy as np
from datetime import datetime

STORES = ["Store_A", "Store_B", "Store_C"]
CATEGORIES = ["Electronics", "Apparel", "Grocery", "Home"]
REGIONS = ["North", "South", "East", "West"]

DB_PATH = "anomaly_pipeline.db"
revenue_history = []
WINDOW = 50

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

def detect_anomaly(revenue, history):
    if len(history) < 10:
        return None, None, None
    mean = np.mean(history)
    std = np.std(history)
    z_score = (revenue - mean) / (std + 1e-9)
    if abs(z_score) > 3:
        severity = "HIGH" if abs(z_score) > 5 else "MEDIUM"
        anomaly_type = "SPIKE" if revenue > mean else "DROP"
        reason = f"Z-score: {z_score:.2f} (mean={mean:.0f}, std={std:.0f})"
        return anomaly_type, severity, reason
    return None, None, None

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("Pipeline running... Ctrl+C to stop")
print("Generating transactions and detecting anomalies...\n")

while True:
    txn = generate_transaction()
    revenue = txn["revenue"]

    cursor.execute("""
        INSERT INTO transactions
        (timestamp, store_id, product_category, revenue, units_sold, region)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (txn["timestamp"], txn["store_id"], txn["product_category"],
          revenue, txn["units_sold"], txn["region"]))
    txn_id = cursor.lastrowid

    revenue_history.append(revenue)
    if len(revenue_history) > WINDOW:
        revenue_history.pop(0)

    anomaly_type, severity, reason = detect_anomaly(revenue, revenue_history)
    if anomaly_type:
        cursor.execute("""
            INSERT INTO anomalies
            (transaction_id, timestamp, anomaly_type, severity, revenue, reason)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (txn_id, txn["timestamp"], anomaly_type, severity, revenue, reason))
        print(f"ANOMALY: {anomaly_type} | {severity} | Revenue: ${revenue:,.0f} | {reason}")
    else:
        print(f"Transaction: {txn['store_id']} | {txn['product_category']} | ${revenue:,.0f}")

    conn.commit()
    time.sleep(1)