import json
import sqlite3
import numpy as np
from kafka import KafkaConsumer
from datetime import datetime

consumer = KafkaConsumer(
    "transactions_topic",
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

conn = sqlite3.connect("anomaly_pipeline.db")
cursor = conn.cursor()

revenue_history = []
WINDOW = 50

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

print("Listening for transactions...")
for msg in consumer:
    txn = msg.value
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
        print(f"ANOMALY: {anomaly_type} | {severity} | Revenue: {revenue} | {reason}")
    conn.commit()
    