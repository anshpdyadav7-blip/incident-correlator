# incident-correlator
# 🔐 Incident Correlator (Mini SIEM System)

A Python-based incident correlation system that simulates core SIEM functionality including log ingestion, anomaly detection, alert generation, and API-based real-time processing.

---

## 🚀 Features

- Log ingestion (file + API)
- Brute force detection
- Suspicious login pattern detection
- Risk scoring engine
- Incident correlation
- SQLite database storage
- Flask-based real-time API
- API authentication (API key)

---

## 🏗️ Architecture

- `core/` → Detection & correlation logic  
- `db.py` → Database connection & initialization  
- `storage.py` → Incident persistence  
- `app.py` → Flask API (real-time ingestion)  
- `main.py` → CLI pipeline  

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/incident-correlator.git
cd incident-correlator

. Create virtual environment
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Run CLI version
python3 main.py
5. Run API server
python3 app.py

Example:
{
  "logs": [
    {
      "timestamp": "2026-01-01T10:00:00",
      "ip": "192.168.1.10",
      "event": "login_failed",
      "user": "admin"
    }
  ]
}
📊 Example Output
{
  "message": "Logs processed successfully",
  "incidents": [
    {
      "ip": "192.168.1.10",
      "risk_score": 5,
      "severity": "HIGH"
    }
  ]
}
🧠 Use Case

This project simulates a basic Security Information and Event Management (SIEM) system used in SOC environments.

📌 Future Improvements
JWT authentication
Dashboard UI
Real-time streaming logs
Advanced anomaly detection
Cloud deployment

👨‍💻 Author

Ansh Yadav