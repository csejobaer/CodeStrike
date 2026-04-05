def schedule(targets):
    """
    Simple AI prioritization scheduler
    - For now, just sorts by length of target (can replace with ML later)
    - Returns list of dicts: { "target": url, "priority": score }
    """
    scheduled = []

    for t in targets:
        score = len(t) % 10  # dummy priority, can be ML-based later
        scheduled.append({"target": t, "priority": score})

    # Higher priority first
    scheduled.sort(key=lambda x: x["priority"], reverse=True)
    return scheduled
