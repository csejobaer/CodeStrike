from scanner import full_scan
from core.scheduler import schedule
from core.distributed import distributed_scan
from core.ai_classifier import classify_risk
from core.ai_explainer import explain_vulnerability
import json

def run_engine():
    """
    Main engine:
    - Reads targets
    - Prioritizes them via scheduler
    - Runs distributed scan
    - ML risk classification
    - AI explanation
    """
    # 1️⃣ Read targets
    with open("data/targets.txt") as f:
        targets = [t.strip() for t in f.readlines() if t.strip()]

    # 2️⃣ Prioritize targets
    prioritized_targets = schedule(targets)
    target_list = [t["target"] for t in prioritized_targets]

    # 3️⃣ Distributed scan
    results = distributed_scan(target_list)

    # 4️⃣ ML classification + AI explanation
    for r in results:
        r["classified_risk"] = classify_risk(r)
        r["ai_explanation"] = explain_vulnerability(r)

    # 5️⃣ Save results
    with open("data/results.json", "w") as f:
        json.dump(results, f, indent=4)

    return results
