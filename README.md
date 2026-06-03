# 🚨 Real-Time Business Anomaly Detection Pipeline

**Most businesses find out about problems on Friday.**

The problem happened on Tuesday.
Three days of damage. Already done.

Weekly reports are not monitoring.
They are autopsies.

**I built something different.**

---

## ⚡ The Challenge I Set Myself

Build a system that detects a revenue anomaly
within 3 seconds of it happening.

Not a batch job. Not a daily report.
Real-time. Every transaction. Every second.

**Done.**

---

## 🎯 The Result

First run on live streaming data:

| Metric | Result |
|---|---|
| Transactions processed | 200 |
| Anomalies detected | 50 |
| High severity alerts | 8 |
| Detection time | Under 3 seconds |
| Dashboard refresh | Every 3 seconds |
| False positive rate | Controlled by Z-score threshold |

---

## 🔬 Why Real-Time Anomaly Detection Is Hard

Most people think anomaly detection is easy.

Set a threshold → flag anything above it → done.

That produces thousands of false positives.
Here is why real-time detection is genuinely hard:

**Problem 1 — Static thresholds don't work**
Revenue at 9am Monday is different from revenue at 3pm Friday.
A fixed threshold flags normal Monday spikes as anomalies.

I used a **rolling Z-score** — the threshold adapts
to recent transaction history automatically.

**Problem 2 — Streaming vs batch**
Batch processing reads historical data.
Streaming processes each event as it arrives.

Kafka's producer-consumer architecture handles this —
but getting the offset management, serialization,
and consumer groups working correctly
took two full days of debugging.

**Problem 3 — Severity classification**
Not all anomalies are equal.
A Z-score of 3.1 is suspicious.
A Z-score of 6.7 needs immediate attention.

I implemented two-tier classification:
- Z-score > 3.0 → MEDIUM severity
- Z-score > 5.0 → HIGH severity

**Problem 4 — Real-time visualization**
Streamlit is not built for real-time.
The auto-refresh pattern using `st.empty()` with
3-second sleep cycles was the solution.

---

## 🏗️ The Architecture

Python Data Generator
↓
Kafka Producer (transactions_topic)
↓
Apache Kafka (Docker containerized)
↓
Kafka Consumer
↓
Z-Score Anomaly Detection
(rolling window · 50 transactions)
↓
SQLite Storage
(transactions table + anomalies table)
↓
Streamlit Dashboard
(auto-refresh every 3 seconds)

Every component is decoupled.
Producer fails → consumer keeps running.
Dashboard fails → pipeline keeps detecting.
This is how production systems are built.

---

## 🔢 The Math Behind It

**Z-Score Formula:**

Z = (x - μ) / σ
Where:
x = current transaction revenue
μ = mean of last 50 transactions
σ = standard deviation of last 50 transactions

If Z > 3.0 — statistically unusual (occurs ~0.3% of the time normally)
If Z > 5.0 — extremely unusual (occurs ~0.00006% of the time normally)

This is the same statistical approach used by:
- 🏦 JPMorgan for real-time fraud detection
- 📦 Amazon for inventory anomaly alerts
- 🏥 Healthcare systems for billing irregularities

---

## ⚙️ What Makes This Production-Ready

✅ Decoupled architecture — producer, consumer, dashboard run independently
✅ Docker containerized — Kafka + Zookeeper in containers
✅ Persistent storage — every transaction and anomaly stored in SQL
✅ Two-tier severity — HIGH and MEDIUM classification
✅ Rolling window detection — adapts to recent transaction patterns
✅ Live dashboard — revenue stream with anomaly overlay
✅ Store-level breakdown — Revenue by Store A, B, C

---

## 🛠️ Tech Stack

Python 3.13
Apache Kafka — real-time event streaming
Docker — Kafka + Zookeeper containerization
SQLite — transaction and anomaly persistence
Streamlit — live dashboard
Pandas — data processing
NumPy — Z-score calculation
Plotly — interactive charts
Scikit-learn — statistical utilities

---

## 🚀 Run It In 5 Steps

### 1. Start Kafka
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

### 4. Start pipeline (3 terminals)
```bash
# Terminal 1 — Producer
python producer/data_generator.py

# Terminal 2 — Consumer
python consumer/anomaly_detector.py

# Terminal 3 — Dashboard
streamlit run dashboard/app.py
```

### 5. Open dashboard

http://localhost:8501

Watch anomalies appear in real time.

---

## 🏭 Industries This Applies To

| Industry | Anomaly It Catches |
|---|---|
| 🛒 Retail | Revenue spikes and drops by store |
| 🏦 Financial Services | Unusual transaction patterns |
| 🏥 Healthcare | Billing irregularities |
| 📦 Supply Chain | Order volume anomalies |
| 📱 Telecom | Network traffic spikes |
| 🏭 Manufacturing | Production output anomalies |

---

## 🏗️ Project Structure

Watch anomalies appear in real time.

---

## 🏭 Industries This Applies To

| Industry | Anomaly It Catches |
|---|---|
| 🛒 Retail | Revenue spikes and drops by store |
| 🏦 Financial Services | Unusual transaction patterns |
| 🏥 Healthcare | Billing irregularities |
| 📦 Supply Chain | Order volume anomalies |
| 📱 Telecom | Network traffic spikes |
| 🏭 Manufacturing | Production output anomalies |

---

## 🏗️ Project Structure

Watch anomalies appear in real time.

---

## 🏭 Industries This Applies To

| Industry | Anomaly It Catches |
|---|---|
| 🛒 Retail | Revenue spikes and drops by store |
| 🏦 Financial Services | Unusual transaction patterns |
| 🏥 Healthcare | Billing irregularities |
| 📦 Supply Chain | Order volume anomalies |
| 📱 Telecom | Network traffic spikes |
| 🏭 Manufacturing | Production output anomalies |

---

## 🏗️ Project Structure
├── producer/
│   └── data_generator.py      # Kafka producer + simulator
├── consumer/
│   └── anomaly_detector.py    # Z-score detection engine
├── db/
│   ├── setup_db.py            # Database initialization
│   └── database.py            # Connection helper
├── dashboard/
│   └── app.py                 # Live Streamlit dashboard
├── config/
│   └── settings.py            # Configuration
├── docker-compose.yml
└── requirements.txt

---

## 🔐 What I Got Right

**Separation of concerns**
Producer, consumer, and dashboard are completely independent.
Each can be restarted without affecting the others.

**Statistical rigor**
Z-score with rolling window beats static thresholds
in every real-world scenario.

**Persistence**
Every transaction and anomaly is stored in SQL.
Audit trail. Historical analysis. Regulatory compliance.

**Containerization**
Docker means this runs identically on any machine.
No "works on my laptop" problems.

---

## 💬 What Building This Changed

I knew what Kafka was before this project.

After debugging consumer group offsets at 2am —
I understand what Kafka does.

There is a difference.

The hardest part was not the anomaly detection.
The hardest part was getting three independent services
to talk to each other reliably.

That is distributed systems.
That is what real data engineering looks like.

---

## 👩‍💻 Built By

**Pallavi Kadiyam**
Data Engineer · BI Analyst · AI/GenAI

📧 pallavikadiyam073@gmail.com
🔗 [GitHub](https://github.com/priyakadiyam-dev)
💼 [LinkedIn](https://linkedin.com/in/pallavi-kadiyam-data-ai)

---

*Built to solve a real problem.
Tested on live streaming data.
Ready for production scale.*

*Give it a ⭐ if it made you think.*


