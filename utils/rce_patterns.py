SUSPICIOUS_PARAMS = [
    "cmd", "exec", "command", "execute",
    "ping", "query", "code"
]

DANGEROUS_KEYWORDS = [
    "system(", "exec(", "shell_exec(",
    "passthru(", "popen("
]


def detect_rce_patterns(url):
    findings = []

    for param in SUSPICIOUS_PARAMS:
        if param in url.lower():
            findings.append(f"Suspicious parameter detected: {param}")

    return findings
