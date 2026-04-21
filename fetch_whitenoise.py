"""
fetch_whitenoise.py
-------------------
Downloads the entire White Noise Records catalog (all ~10,823 products)
and saves them to a single file: whitenoise_all.json

Usage in VS Code:
  1. Open this file in VS Code
  2. Open the integrated terminal (View > Terminal, or Ctrl+`)
  3. Run:  python fetch_whitenoise.py
  4. Wait ~2-3 minutes (it fetches 50 pages with a polite 1-second pause between each)
  5. Upload the resulting whitenoise_all.json back to Claude

If you don't have the requests library installed, run first:
  pip install requests
"""

import json
import time
import sys

try:
    import requests
except ImportError:
    print("ERROR: 'requests' library not installed.")
    print("Run this in your terminal first:  pip install requests")
    sys.exit(1)

BASE_URL = "https://whitenoiserecords.org/products.json"
LIMIT = 250          # max Shopify allows per page
MAX_PAGES = 50       # safety cap; will stop earlier if we run out
DELAY_SEC = 1.0      # be polite — 1 second between requests
OUTPUT_FILE = "whitenoise_all.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept": "application/json",
}

def main():
    all_products = []
    seen_ids = set()
    page = 1

    while page <= MAX_PAGES:
        url = f"{BASE_URL}?limit={LIMIT}&page={page}"
        print(f"Fetching page {page}...", end=" ", flush=True)

        try:
            r = requests.get(url, headers=HEADERS, timeout=30)
            r.raise_for_status()
        except requests.RequestException as e:
            print(f"FAILED: {e}")
            print("Stopping. Will save what we have so far.")
            break

        data = r.json()
        products = data.get("products", [])

        if not products:
            print("empty (end of catalog).")
            break

        # Dedupe by product ID
        new_count = 0
        for p in products:
            if p["id"] not in seen_ids:
                seen_ids.add(p["id"])
                all_products.append(p)
                new_count += 1

        print(f"got {len(products)} (new: {new_count}, total: {len(all_products)})")

        # If a page returned fewer than LIMIT, that's the last page
        if len(products) < LIMIT:
            print("Last page reached.")
            break

        page += 1
        time.sleep(DELAY_SEC)

    # Save merged result
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({"products": all_products}, f, ensure_ascii=False, indent=2)

    print(f"\nDONE. Saved {len(all_products)} products to {OUTPUT_FILE}")
    print(f"Now upload {OUTPUT_FILE} back to Claude.")

if __name__ == "__main__":
    main()
