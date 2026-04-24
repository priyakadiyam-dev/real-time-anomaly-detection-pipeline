# Real-Time Business Anomaly Detection Pipeline

Detects unusual business activity from a live transaction stream 
and displays it on a real-time dashboard.

## Tech Stack
Python · Apache Kafka · SQLite · Streamlit · Pandas · Plotly · Scikit-learn

## Architecture
Data Generator → Kafka → Anomaly Detector → SQLite → Streamlit Dashboard

## How to Run

### 1. Start Kafka
```bash
docker run -d --name zookeeper -p 2181:2181 zookeeper:3.4
docker run -d --name kafka -p 9092:9092 \
  -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
  confluentinc/cp-kafka
```

### 2. Setup database
```bash
python db/setup_db.py
```

### 3. Run producer (Terminal 1)
```bash
python producer/data_generator.py
```

### 4. Run consumer (Terminal 2)
```bash
python consumer/anomaly_detector.py
```

### 5. Launch dashboard (Terminal 3)
```bash
streamlit run dashboard/app.py
```

## Author
Pallavi Kadiyam | [LinkedIn](https://linkedin.com/in/pallavikadiyam)
