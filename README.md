# AI-Powered Ethical RCE Risk Analyzer

🛡️ This project is a **safe and ethical RCE (Remote Code Execution) risk analyzer** for web applications.  
It uses **Python, Flask, ML heuristics, and OpenAI GPT** to detect suspicious patterns, simulate safe fuzzing, classify risk levels, and provide AI-powered explanations with mitigation guidance.  

> ⚠️ **Important:** This tool is for **ethical testing only**.  
> Do **not** use it on unauthorized targets. Scan only websites you own or have permission to test.

---

## Features

- 🖥️ **Web Dashboard:** Real-time risk visualization and scan results  
- 🤖 **AI Explanation:** GPT-powered vulnerability explanation and mitigation advice  
- 📡 **Monitoring:** Live JSON monitoring of all scan results  
- ⚡ **Distributed Worker Scanning:** Threaded workers for multiple targets  
- 📊 **ML-based Risk Classification:** CRITICAL / HIGH / MEDIUM / LOW  
- 🔒 **Safe Fuzzing & RCE Pattern Detection:** Only simulated payloads, no real exploit execution  
- 📝 **Target Management:** Add new targets via API  

---

## Project Structure
```bash
CodeStrike/
├── app.py # Flask web app entry
├── config.py # Configuration (API keys, settings)
├── scanner.py # ML + RCE detection engine
├── core/ # Engine, AI agent, scheduler, distributed scanning
│ ├── engine.py
│ ├── scheduler.py
│ ├── agent.py
│ ├── distributed.py
│ ├── ai_classifier.py
│ └── ai_explainer.py
├── workers/
│ └── worker.py # Threaded worker scanner
├── utils/ # Utility modules
│ ├── crawler.py
│ ├── subdomain.py
│ ├── rce_patterns.py
│ ├── ml_model.py
│ └── safe_fuzzer.py
├── templates/ # Flask HTML templates
│ ├── dashboard.html
│ ├── monitoring.html
│ └── explanation.html
├── static/
│ └── chart.js # Dashboard charts
└── data/
├── targets.txt # List of targets
└── results.json # Scan results
```

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/cse_jobaer/CodeStike.git
cd CodeStike
```

---

2. **Clone the repository**

   ```bash
  python -m venv venv
  source venv/bin/activate      # Linux / Mac
  venv\Scripts\activate         # Windows
```

--

3. **Install dependencies**
 ```bash
  pip install -r requirements.txt
```
4. **Configure OpenAI API key**
   Set your API key in config.py or as environment variable:
   ```bash
  export OPENAI_API_KEY="your_openai_api_key_here"   # Linux / Mac
  set OPENAI_API_KEY="your_openai_api_key_here"      # Windows
   ```

5. **Add target URLs to** ```bash data/targets.txt:
    https://example.com
    https://testsite.local
   ```
***Usage
Run the Flask App***
```bash
python app.py
```
Open the browser:
```bash
Dashboard: http://localhost:5000/
Monitoring: http://localhost:5000/monitor
AI Explanation: http://localhost:5000/explanation
```
###Add a new target via API
```bash
curl -X POST http://localhost:5000/add_target \
-H "Content-Type: application/json" \
-d '{"target":"https://newtarget.com"}'
```
---

**Scan Workflow**
Targets are read from ```bash targets.txt ```
Scheduler prioritizes targets (AI/heuristic based)
Distributed worker threads scan targets (safe fuzzing + RCE pattern detection)
ML-based risk classification applied
AI generates vulnerability explanation and mitigation
Results stored in ```bash data/results.json ``` and displayed on dashboard

---

**Notes**
-**⚠️ Legal & Ethical Use Only**
Scan only websites you own or have permission to test.
-**🔒 Safe Fuzzing**
The tool uses simulated payloads only, no real exploit is executed.
-**📡 Real-Time Updates**
Dashboard updates every 5 seconds.
-**💡 Customization**
  -Add more FUZZ_SAFE_PAYLOADS in config.py
  -Update subdomains in utils/subdomain.py
  -Customize ML heuristics in utils/ml_model.py
  

---

**Future Improvements**
-Docker + docker-compose deployment
-Multi-user SaaS-ready web app
-Advanced ML risk prediction using trained models
-Interactive Chart.js visualization for scan results

---

**License**

This project is MIT licensed.
Use responsibly and ethically.
