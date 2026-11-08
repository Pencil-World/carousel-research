#!/usr/bin/env python3
"""Save read-only keyword-search responses from Raleigh's public museum catalogue.

The endpoint and request fields come from the catalogue's public
multitype-keyword-search and libs bundles, preserved under sources/.
No authentication, email, ordering, or write endpoints are used.
"""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
URL = "https://raleighhrmprogram.catalogaccess.com/api/search/keyword"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("name", help="Local output basename without extension")
    parser.add_argument("--skip", type=int, default=0)
    parser.add_argument("--top", type=int, default=100)
    args = parser.parse_args()
    if Path(args.name).name != args.name or not 1 <= args.top <= 100 or args.skip < 0:
        parser.error("Use a plain filename, nonnegative skip, and top from 1 to 100")
    payload = {
        "OnlyWithImages": False,
        "SearchString": args.query,
        "IncludeFields": ["101", "102", "104", "700"],
        "Skip": str(args.skip),
        "Top": str(args.top),
    }
    request = urllib.request.Request(
        URL, data=json.dumps(payload).encode(),
        headers={"User-Agent": "Mozilla/5.0 (public historical research)",
                 "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=40) as response:
        body = response.read()
    destination = ROOT / "sources" / (args.name + ".json")
    destination.write_bytes(body)
    metadata = {
        "url": URL, "method": "POST (read-only search)", "request_json": payload,
        "retrieved_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "sha256": hashlib.sha256(body).hexdigest(), "bytes": len(body),
    }
    destination.with_suffix(".request.json").write_text(json.dumps(metadata, indent=2) + "\n")
    result = json.loads(body)
    print(json.dumps({"file": str(destination), "count": result.get("PageResult", {}).get("Count"),
                      "returned": len(result.get("PageResult", {}).get("Items", []))}, indent=2))


if __name__ == "__main__":
    main()
