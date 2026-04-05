from urllib.parse import urlparse
from utils.crawler import crawl
from utils.subdomain import find_subdomains
from utils.rce_patterns import detect_rce_patterns
from utils.safe_fuzzer import fuzz_url
from utils.ml_model import predict_rce_risk

def full_scan(url):
    """
    Full ethical RCE risk scan for a single target
    - Crawl links
    - Enumerate subdomains
    - Detect suspicious RCE parameters
    - Safe fuzzing simulation
    - ML-based risk prediction
    """

    domain = urlparse(url).netloc

    # 1️⃣ Crawl all links
    try:
        links = crawl(url)
    except Exception:
        links = []

    # 2️⃣ Find subdomains
    try:
        subs = find_subdomains(domain)
    except Exception:
        subs = []

    # 3️⃣ Detect suspicious parameters (safe detection)
    rce_findings = detect_rce_patterns(url)

    # 4️⃣ Safe fuzzing simulation
    fuzz_findings = fuzz_url(url)

    # 5️⃣ ML-based RCE risk scoring
    features = {
        "suspicious_params": len(rce_findings) > 0,
        "many_subdomains": len(subs) > 3,
        "many_links": len(links) > 10,
        "fuzz_findings": fuzz_findings
    }

    risk = predict_rce_risk(features)

    # 6️⃣ Compile final scan result
    result = {
        "target": url,
        "links": links,
        "subdomains": subs,
        "rce_findings": rce_findings,
        "fuzz_findings": fuzz_findings,
        "risk": risk
    }

    return result
