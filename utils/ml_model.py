def predict_rce_risk(features):
    """
    ML-inspired heuristic for RCE risk
    """
    score = 0
    if features.get("suspicious_params"):
        score += 2
    if features.get("many_subdomains"):
        score += 1
    if features.get("many_links"):
        score += 1
    if features.get("fuzz_findings"):
        score += len(features["fuzz_findings"])
    
    if score >= 5:
        return "CRITICAL"
    elif score >= 3:
        return "HIGH"
    elif score >= 2:
        return "MEDIUM"
    else:
        return "LOW"
