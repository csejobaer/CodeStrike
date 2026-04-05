import urllib.parse

SAFE_PAYLOADS = [
    "' OR '1'='1", "<script>alert(1)</script>",
    "$(echo test)", "`whoami`"
]

def fuzz_url(url):
    """
    Simulate payload injection safely without executing
    """
    results = []
    parsed = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parsed.query)

    for payload in SAFE_PAYLOADS:
        for param in query:
            # simulate injection detection
            if len(query[param][0]) > 0:
                results.append(f"Potential injection via {param} with payload {payload}")

    return results
