import requests
from bs4 import BeautifulSoup
from config import MAX_LINKS_PER_SITE

def crawl(url):
    """
    Crawl links of a target safely
    """
    links = set()
    try:
        resp = requests.get(url, timeout=5)
        soup = BeautifulSoup(resp.text, "html.parser")
        for a in soup.find_all("a", href=True):
            link = a['href']
            if link.startswith("http"):
                links.add(link)
            if len(links) >= MAX_LINKS_PER_SITE:
                break
    except Exception:
        pass
    return list(links)
