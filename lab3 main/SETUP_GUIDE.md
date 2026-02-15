# 🚀 Lab 3 - Setup Guide

## Quick Start (5 Minutes)

### Step 1: Start All Services
Open terminal in VS Code and run:
```bash
docker-compose up -d
```

Wait 30 seconds for all services to start.

### Step 2: Access JupyterLab
Open your browser and go to:
```
http://localhost:8888
```

No password required!

### Step 3: Run the Notebooks (in order)

1. **Producer.ipynb** - Generates events (run first)
2. **Consumer_Classifier.ipynb** - Processes events (run second)
3. **Statistics.ipynb** - Analyzes results (run last)

### Step 4: View Results

- **Kafka Events**: http://localhost:8080 (Redpanda Console)
- **Tracing**: http://localhost:16686 (Jaeger UI)
- **Analysis**: Check the Statistics notebook

---

## 📊 Services Overview

| Service | Port | Purpose |
|---------|------|---------|
| Kafka | 9092 | Message queue |
| Redpanda Console | 8080 | Kafka UI |
| Jaeger | 16686 | Tracing UI |
| JupyterLab | 8888 | Development environment |

---

## 📝 Detailed Instructions

### Understanding the Pipeline
```
Producer → Kafka → Consumer/Classifier → CSV → Statistics
              ↓
           Jaeger (tracing everything)
```

### Step-by-Step Workflow

#### 1. Start Docker Services
```bash
# Start all services
docker-compose up -d

# Check if services are running
docker ps
```

You should see 4 containers:
- kafka
- redpanda-console
- jaeger
- jupyter

#### 2. Access JupyterLab

Go to http://localhost:8888

You'll see:
- `work/` folder (your notebooks)
- `data/` folder (results will be saved here)

#### 3. Run Producer Notebook

Open `Producer.ipynb` and run all cells (Cell → Run All)

This will:
- ✅ Install required packages
- ✅ Connect to Kafka
- ✅ Generate 50 synthetic security events
- ✅ Send them to Kafka topic `events.raw`
- ✅ Create Jaeger traces

**Expected output:**
```
✅ Sent 10 events
✅ Sent 20 events
...
🎉 Successfully sent 50 events to Kafka!
```

#### 4. View Events in Redpanda Console

Open http://localhost:8080

- Click "Topics"
- Click "events.raw"
- See all your events!

#### 5. Run Consumer/Classifier Notebook

Open `Consumer_Classifier.ipynb` and run all cells

This will:
- ✅ Consume events from Kafka
- ✅ Classify each event (benign/suspicious/malicious)
- ✅ Map to MITRE ATT&CK framework
- ✅ Save to CSV file
- ✅ Create Jaeger traces

**Expected output:**
```
✅ Processed 10 events
✅ Processed 20 events
...
💾 Saved 50 classified events to CSV
```

#### 6. View Traces in Jaeger

Open http://localhost:16686

- Select service: "producer" or "consumer-classifier"
- Click "Find Traces"
- See the execution flow!

#### 7. Run Statistics Notebook

Open `Statistics.ipynb` and run all cells

This will:
- ✅ Load classified events from CSV
- ✅ Generate statistics
- ✅ Create visualizations
- ✅ Export summary report

---

## 🔍 What to Look For

### In Redpanda Console (Kafka UI)
- **Topic**: events.raw
- **Messages**: See raw events with IPs, ports, protocols
- **Partitions**: 3 partitions

### In Jaeger (Tracing UI)
- **Producer traces**: `generate_event`, `kafka_send`
- **Consumer traces**: `consume_message`, `classify`, `save_to_storage`
- **Latency**: How long each operation takes

### In Statistics Notebook
- **Classification breakdown**: Benign vs Suspicious vs Malicious
- **Event types**: port_scan, brute_force, normal_web, etc.
- **MITRE tactics**: Discovery, Credential Access, Exfiltration
- **Visualizations**: Pie charts, bar charts, distributions

---

## 🐛 Troubleshooting

### Services Won't Start
```bash
# Stop everything
docker-compose down

# Start fresh
docker-compose up -d
```

### Can't Access JupyterLab (localhost:8888)
```bash
# Check if Jupyter is running
docker logs jupyter

# Restart just Jupyter
docker-compose restart jupyter
```

### Kafka Connection Errors
```bash
# Check Kafka is healthy
docker exec kafka kafka-topics.sh --bootstrap-server localhost:9092 --list

# Restart Kafka
docker-compose restart kafka
```

### No Events in Kafka

Make sure you:
1. Ran the Producer notebook first
2. Waited for it to complete
3. Checked Redpanda Console at http://localhost:8080

---

## 🎯 Lab Objectives Checklist

- [ ] All Docker services running
- [ ] Producer generated events
- [ ] Events visible in Redpanda Console
- [ ] Consumer classified events
- [ ] Results saved to CSV
- [ ] Traces visible in Jaeger
- [ ] Statistics generated
- [ ] Visualizations created
- [ ] Understood the pipeline flow
- [ ] Can explain why Kafka is used

---

## 💡 Key Concepts

### Why Kafka?
- **Decoupling**: Producer doesn't know about Consumer
- **Scalability**: Can add more consumers
- **Resilience**: Messages stored even if consumer is down
- **Replay**: Can re-process old events

### Why Tracing?
- **Visibility**: See what's happening inside the pipeline
- **Debugging**: Find bottlenecks and errors
- **Monitoring**: Track performance over time

### MITRE ATT&CK
- **Framework**: Standardized way to classify cyber threats
- **Tactics**: What the adversary is trying to achieve
- **Techniques**: How they're doing it

---

## 🎓 For Your Lab Report

Answer these questions:

1. **Why use Kafka instead of direct function calls?**
2. **What happens if consumer is slower than producer?**
3. **How does tracing help debug pipeline behavior?**
4. **Which pipeline stages could be scaled independently?**
5. **How would this change in a real SOC system?**

**Good luck!** 🎉