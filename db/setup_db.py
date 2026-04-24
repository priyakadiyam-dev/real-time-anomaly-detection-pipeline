import sqlite3
from config.settings import DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    store_id TEXT,
    product_category TEXT,
    revenue REAL,
    units_sold INTEGER,
    region TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS anomalies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_id INTEGER,
    timestamp TEXT,
    anomaly_type TEXT,
    severity TEXT,
    revenue REAL,
    reason TEXT
)
""")

conn.commit()
conn.close()
print("Database created successfully!")