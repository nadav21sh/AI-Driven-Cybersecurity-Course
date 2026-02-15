# ⚡ Lab 3 - Quick Start

## 🚀 5-Minute Setup

### 1. Start Everything
```bash
docker-compose up -d
```

### 2. Wait 30 Seconds
Services need time to initialize.

### 3. Open JupyterLab
```
http://localhost:8888
```

### 4. Run Notebooks (in order)
1. **Producer.ipynb** - Creates events
2. **Consumer_Classifier.ipynb** - Processes events  
3. **Statistics.ipynb** - Shows results

### 5. View Results
- **Kafka**: http://localhost:8080
- **Traces**: http://localhost:16686

---

## ✅ Success Checklist

After running all notebooks, you should have:
- [ ] 50+ events in Kafka
- [ ] CSV file with classified events
- [ ] Statistics and visualizations
- [ ] Traces in Jaeger

---

## 🐛 Problems?

**Services won't start:**
```bash
docker-compose down
docker-compose up -d
```

**Can't access Jupyter:**
- Wait 1 minute for initialization
- Check: `docker logs jupyter`

**No events in Kafka:**
- Run Producer notebook first!
- Check Redpanda Console

---

## 📚 Full Instructions
See **SETUP_GUIDE.md** for detailed explanations.