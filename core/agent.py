def prioritize_targets(targets):
    """
    AI decision-making agent for task ordering
    - Currently uses heuristic: more suspicious params = higher priority
    """
    prioritized = []
    for t in targets:
        risk_score = 0
        if "cmd" in t or "exec" in t:
            risk_score += 2
        prioritized.append({"target": t, "priority": risk_score})

    prioritized.sort(key=lambda x: x["priority"], reverse=True)
    return prioritized
