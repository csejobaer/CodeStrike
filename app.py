from flask import Flask, render_template, jsonify, request
from core.engine import run_engine
from core.scheduler import schedule
from core.agent import prioritize_targets

app = Flask(__name__)

# -------------------------
# Home / Dashboard Route
# -------------------------
@app.route("/")
def home():
    return render_template("dashboard.html")


# -------------------------
# Real-time Monitoring Route
# -------------------------
@app.route("/monitor")
def monitor():
    return render_template("monitoring.html")


# -------------------------
# AI Vulnerability Explanation
# -------------------------
@app.route("/explanation")
def explanation():
    return render_template("explanation.html")


# -------------------------
# Run AI Engine Route
# -------------------------
@app.route("/ai_engine")
def ai_engine():
    """
    Run full engine:
    - Scheduler + prioritization
    - Distributed workers
    - ML risk classifier
    - AI vulnerability explanation
    Returns JSON results
    """
    results = run_engine()
    return jsonify(results)


# -------------------------
# Add new targets via API
# -------------------------
@app.route("/add_target", methods=["POST"])
def add_target():
    """
    Example JSON:
    { "target": "https://example.com" }
    """
    data = request.get_json()
    target = data.get("target")
    if not target:
        return jsonify({"error": "No target provided"}), 400

    # Append target to targets.txt safely
    with open("data/targets.txt", "a") as f:
        f.write(target.strip() + "\n")

    return jsonify({"message": f"Target {target} added successfully"})


# -------------------------
# Scheduler Test Route
# -------------------------
@app.route("/schedule_test")
def schedule_test():
    """
    Returns AI-prioritized target list without scanning
    """
    with open("data/targets.txt") as f:
        targets = [t.strip() for t in f.readlines() if t.strip()]

    prioritized = schedule(targets)
    return jsonify(prioritized)


# -------------------------
# Run App
# -------------------------
if __name__ == "__main__":
    # Debug=True for development; turn off in production
    app.run(host="0.0.0.0", port=5000, debug=True)
