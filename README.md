# 🚨 Real-Time Business Anomaly Detection Pipeline

I built this because businesses are losing money every day
from problems they could have caught hours earlier.

By the time a weekly report surfaces a revenue anomaly —
the damage is already done.

**What if you could catch it as it happens?**

---

## 🤔 The Problem I Wanted to Solve

Imagine you are running operations for a retail business.

Store B just had a revenue spike — 5x the normal amount.
Could be a data error. Could be fraud. Could be a system glitch.

But nobody knows yet.

Your weekly report will surface it on Friday.
Today is Tuesday.

Three days of potential damage — completely invisible.

Meanwhile Store C just crashed to 10% of normal revenue.
Something is seriously wrong.

Again — nobody knows yet.

**I built a system that catches both of these in under 3 seconds.**

---

## 💡 What I Built

A real-time streaming pipeline that:

→ Generates live business transactions every second
→ Streams data through Apache Kafka
→ Detects revenue spikes and drops using Z-score statistical analysis
→ Classifies every anomaly as HIGH or MEDIUM severity
→ Stores everything in SQL — transactions and flagged events
→ Displays live alerts on a Streamlit dashboard
→ Refreshes every 3 seconds automatically

No manual checking. No weekly reports. No surprises.

---

## 📊 First Run Results

| Metric | Result |
|---|---|
| Transactions processed | 200 |
| Anomalies detected | 50 |
| High severity alerts | 8 |
| Dashboard refresh rate | Every 3 seconds |
| Detection method | Z-score statistical analysis |

---

## 🔬 The Science Behind It

**Z-Score Anomaly Detection**

Every transaction is compared against a rolling window
of the last 50 transactions.

If the Z-score exceeds 3.0 standard deviations — it is flagged.
If it exceeds 5.0 — it is flagged as HIGH severity.

This is the same statistical approach used by:
- 🏦 JPMorgan for fraud detection
- 📦 Amazon for inventory anomaly detection
- 🏥 Healthcare systems for billing irregularities

**Producer-Consumer Architecture**

The pipeline follows the same pattern used in enterprise
data engineering at Netflix, Uber, and LinkedIn:

Data Generator → Kafka Topic → Consumer → SQL → Dashboard

Each component does one job. Each can be scaled independently.

---

## ⚙️ What It Detects

| Anomaly Type | Example | Severity |
|---|---|---|
| Revenue SPIKE | Store B revenue 5x normal | HIGH |
| Revenue DROP | Store C crashes to 10% | HIGH |
| Moderate spike | 3-4x normal revenue | MEDIUM |
| Moderate drop | Revenue drops 60-70% | MEDIUM |

---

## 🛠️ Tech Stack

Each component does one job. Each can be scaled independently.

---

## ⚙️ What It Detects

| Anomaly Type | Example | Severity |
|---|---|---|
| Revenue SPIKE | Store B revenue 5x normal | HIGH |
| Revenue DROP | Store C crashes to 10% | HIGH |
| Moderate spike | 3-4x normal revenue | MEDIUM |
| Moderate drop | Revenue drops 60-70% | MEDIUM |

---

## 🛠️ Tech Stack

Python · Apache Kafka · Docker · SQLite
Streamlit · Pandas · NumPy · Plotly · Scikit-learn


---

## 🚀 Run It Yourself

### 1. Start Kafka with Docker
```bash
docker run -d --name zookeeper -p 2181:2181 zookeeper:3.4
docker run -d --name kafka -p 9092:9092 \
  -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
  -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 \
  confluentinc/cp-kafka
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup database
```bash
python db/setup_db.py
```

### 4. Run producer (Terminal 1)
```bash
python producer/data_generator.py
```

### 5. Run consumer (Terminal 2)
```bash
python consumer/anomaly_detector.py
```

### 6. Launch dashboard (Terminal 3)
```bash
streamlit run dashboard/app.py
```

Open http://localhost:8501 and watch anomalies appear in real time.

---

## 🏗️ Project Structure

├── producer/
│   └── data_generator.py      # Kafka producer + transaction simulator
├── consumer/
│   └── anomaly_detector.py    # Kafka consumer + Z-score detection
├── db/
│   ├── setup_db.py            # Database initialization
│   └── database.py            # Connection helper
├── dashboard/
│   └── app.py                 # Live Streamlit dashboard
├── config/
│   └── settings.py            # Kafka + DB configuration
├── docker-compose.yml         # Docker setup
└── requirements.txt
---

## 🏭 Who This Is Built For

| Industry | The Anomaly It Catches |
|---|---|
| 🛒 Retail | Revenue spikes and drops by store |
| 🏦 Financial Services | Unusual transaction patterns |
| 🏥 Healthcare | Billing irregularities |
| 📦 Supply Chain | Order volume anomalies |
| 📱 Telecom | Network traffic spikes |

---

## 💬 What I Learned Building This

I had never run Kafka before this project.

Getting the producer, consumer, and Docker containers
talking to each other took two full days of debugging.

But that debugging taught me more about distributed systems
than any course ever could.

The moment I saw the first anomaly flash red on the dashboard —
I understood why real-time data engineering matters.

It is not about the technology.
It is about giving businesses the ability to respond
before problems become crises.

---

## 👩‍💻 Built By

**Pallavi Kadiyam**
Data Engineer · BI Analyst · AI/GenAI

📧 pallavikadiyam073@gmail.com
🔗 [GitHub](https://github.com/priyakadiyam-dev)
💼 [LinkedIn](https://linkedin.com/in/pallavi-kadiyam-data-ai)

---

*If this project resonates with you — give it a ⭐ and let's connect.*

---

## 🏭 Who This Is Built For

| Industry | The Anomaly It Catches |
|---|---|
| 🛒 Retail | Revenue spikes and drops by store |
| 🏦 Financial Services | Unusual transaction patterns |
| 🏥 Healthcare | Billing irregularities |
| 📦 Supply Chain | Order volume anomalies |
| 📱 Telecom | Network traffic spikes |

---

## 💬 What I Learned Building This

I had never run Kafka before this project.

Getting the producer, consumer, and Docker containers
talking to each other took two full days of debugging.

But that debugging taught me more about distributed systems
than any course ever could.

The moment I saw the first anomaly flash red on the dashboard —
I understood why real-time data engineering matters.

It is not about the technology.
It is about giving businesses the ability to respond
before problems become crises.

---

## 👩‍💻 Built By

**Pallavi Kadiyam**
Data Engineer · BI Analyst · AI/GenAI

📧 pallavikadiyam073@gmail.com
🔗 [GitHub](https://github.com/priyakadiyam-dev)
💼 [LinkedIn](https://linkedin.com/in/pallavi-kadiyam-data-ai)

---

*If this project resonates with you — give it a ⭐ and let's connect.*

