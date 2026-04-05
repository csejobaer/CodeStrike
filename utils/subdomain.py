import requests
from urllib.parse import urlparse
from config import MAX_SUBDOMAINS

COMMON_SUBDOMAINS = ["www", "api", "admin", "dev", "test"]

def find_subdomains(domain):
    """
    Simple subdomain enumeration (ethical / passive)
    """
    found = []
    for sub in COMMON_SUBDOMAINS:
        url = f"https://{sub}.{domain}"
        try:
            resp = requests.head(url, timeout=3)
            if resp.status_code < 400:
                found.append(url)
            if len(found) >= MAX_SUBDOMAINS:
                break
        except Exception:
            continue
    return found
