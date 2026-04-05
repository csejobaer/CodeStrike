def classify_risk(scan_result):
    """
    ML-inspired risk classification
    """
    score = 0
    if scan_result.get("rce_findings"):
        score += 2
    if scan_result.get("fuzz_findings"):
        score += len(scan_result["fuzz_findings"])
    if len(scan_result.get("subdomains", [])) > 3:
        score += 1
    if len(scan_result.get("links", [])) > 10:
        score += 1

    if score >= 5:
        return "CRITICAL"
    elif score >= 3:
        return "HIGH"
    elif score >= 2:
        return "MEDIUM"
    else:
        return "LOW"
