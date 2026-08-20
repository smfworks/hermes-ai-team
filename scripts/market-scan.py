#!/usr/bin/env python3
"""Example pre-run data-collection script for a nightly-research cron.

Pattern: a cron job with --script runs this BEFORE the agent; its stdout is
injected into the agent's prompt as context. The script does the free, mechanical
collection (here: fetch recent tech-news headlines), and the agent does the
reasoning and vault filing.

Use with:
  hermes cron create "0 3 * * *" \
    --name "Market Scan" \
    --script /path/to/scripts/market-scan.py \
    --prompt "Analyze the articles above. For each relevant to <your domain>,
              write a structured note to ~/AgentVault/Research/market/. Flag
              anything needing immediate attention."

Replace the fake endpoint with a real, public news/API source appropriate to
your domain (many are free: NewsAPI, arXiv Atom, RSS feeds, etc.).
"""

import json
import urllib.request

# Example: a public RSS/JSON feed endpoint — replace with a real one.
URL = "https://example.com/api/news?category=technology&limit=10"

try:
    with urllib.request.urlopen(URL, timeout=20) as resp:
        data = json.loads(resp.read().decode())
except Exception as exc:  # network policy for a cron: fail, do not hang
    print(f"COLLECTION FAILED: {exc}")
    raise SystemExit(1)

for i, article in enumerate(data.get("articles", [])[:10], 1):
    print(f"Article {i}: {article.get('title')}")
    print(f"  URL: {article.get('url')}")
    print(f"  Summary: {article.get('summary', '')[:200]}")
    print("---")
