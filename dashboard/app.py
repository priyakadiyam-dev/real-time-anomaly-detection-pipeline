import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time

st.set_page_config(page_title="Business Anomaly Monitor", layout="wide")
st.title("Real-Time Business Anomaly Detection")

DB = "anomaly_pipeline.db"

def load_data():
    conn = sqlite3.connect(DB)
    txns = pd.read_sql(
        "SELECT * FROM transactions ORDER BY timestamp DESC LIMIT 200", conn)
    anomalies = pd.read_sql(
        "SELECT * FROM anomalies ORDER BY timestamp DESC LIMIT 50", conn)
    conn.close()
    return txns, anomalies

placeholder = st.empty()

while True:
    txns, anomalies = load_data()
    with placeholder.container():
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Transactions", len(txns))
        col2.metric("Anomalies Detected", len(anomalies))
        col3.metric("High Severity", len(
            anomalies[anomalies["severity"] == "HIGH"]) if len(anomalies) else 0)

        st.subheader("Revenue Stream")
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=txns["timestamp"], y=txns["revenue"],
            mode="lines+markers", name="Revenue"))
        if len(anomalies):
            fig.add_trace(go.Scatter(
                x=anomalies["timestamp"], y=anomalies["revenue"],
                mode="markers", name="Anomaly",
                marker=dict(color="red", size=12, symbol="x")))
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Recent Anomalies")
        if len(anomalies):
            st.dataframe(anomalies[[
                "timestamp", "anomaly_type",
                "severity", "revenue", "reason"]],
                use_container_width=True)
        else:
            st.info("No anomalies detected yet.")

        if len(txns):
            st.subheader("Revenue by Store")
            store_avg = txns.groupby("store_id")["revenue"].mean().reset_index()
            st.plotly_chart(px.bar(
                store_avg, x="store_id", y="revenue", color="store_id"),
                use_container_width=True)
    time.sleep(3)
    placeholder.empty()
    