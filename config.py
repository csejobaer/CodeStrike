import os

# -------------------------
# OpenAI API Key (for AI explanation)
# -------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")

# -------------------------
# Scan Settings
# -------------------------
MAX_LINKS_PER_SITE = 100        # Maximum links to crawl per target
MAX_SUBDOMAINS = 50             # Maximum subdomains to enumerate
FUZZ_SAFE_PAYLOADS = [
    "' OR '1'='1",
    "<script>alert(1)</script>",
    "$(echo test)",
    "`whoami`"
]

# -------------------------
# App Settings
# -------------------------
DEBUG = True
HOST = "0.0.0.0"
PORT = 5000
