# 📧 Phishing Email Detection Pipeline

A real-time phishing email detection system using Machine Learning, Kafka streaming, and MITRE ATT&CK framework integration.

## 🎯 Project Overview

This project implements an **Integrated AI-Cybersecurity Pipeline** that:
1. Streams emails through Apache Kafka
2. Classifies emails using ML (TF-IDF + Logistic Regression)
3. Maps detections to MITRE ATT&CK framework
4. Provides real-time visualization and analysis

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    PHISHING DETECTION PIPELINE                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  📧 Email Dataset    →    📬 Kafka    →    🤖 ML Classifier     │
│  (100 emails)            (streaming)       (TF-IDF + LR)        │
│                              ↓                                   │
│                         📊 Results                               │
│                              ↓                                   │
│              🎯 MITRE ATT&CK    →    📈 Dashboard               │
│                 Mapping              (5 Visualizations)          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## 🛠️ Technologies

| Component | Technology |
|-----------|------------|
| Message Queue | Apache Kafka 3.7.0 |
| ML Framework | scikit-learn |
| Tracing | Jaeger |
| Development | JupyterLab |
| Containerization | Docker Compose |
| Visualization | Matplotlib, Seaborn |

## 📁 Project Structure

```
phishing-detection-project/
├── compose.yml                    # Docker services configuration
├── notebooks/
│   ├── 1_Email_Producer.ipynb     # Streams emails to Kafka
│   ├── 2_ML_Classifier.ipynb      # ML model training & classification
│   └── 3_Statistics.ipynb         # Analysis & visualizations
├── data/
│   ├── emails.csv                 # Input dataset (100 emails)
│   └── classified_emails.csv      # Classification results
├── models/
│   ├── phishing_model.pkl         # Trained model
│   └── tfidf_vectorizer.pkl       # TF-IDF vectorizer
└── README.md
```

## 🚀 Quick Start

1. **Start Docker services:**
   ```bash
   docker-compose up -d
   ```

2. **Access JupyterLab:**
   - URL: http://localhost:8888

3. **Run notebooks in order:**
   - `1_Email_Producer.ipynb` - Send emails to Kafka
   - `2_ML_Classifier.ipynb` - Train model and classify
   - `3_Statistics.ipynb` - Generate visualizations

4. **View dashboards:**
   - Kafka Console: http://localhost:8080
   - Jaeger Tracing: http://localhost:16686

## 🎯 MITRE ATT&CK Coverage

| Technique ID | Name | Description |
|--------------|------|-------------|
| T1566.001 | Spearphishing Attachment | Malicious attachments |
| T1566.002 | Spearphishing Link | Malicious links |
| T1598.003 | Phishing for Information | Credential harvesting |

## 📊 Results

- **Dataset:** 100 emails (50 phishing, 50 legitimate)
- **Model Accuracy:** ~90%+
- **Features:** TF-IDF with unigrams and bigrams
- **Visualizations:** 5 comprehensive charts

## 👥 Authors

- Student 1
- Student 2

## 📚 Course

AI in Cybersecurity based on NVIDIA Morpheus
