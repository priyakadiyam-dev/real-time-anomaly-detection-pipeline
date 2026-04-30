import sqlite3

DB_PATH = "anomaly_pipeline.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn