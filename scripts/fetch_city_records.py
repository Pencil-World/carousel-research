#!/usr/bin/env python3
"""Preserve public item records returned by a previously saved city catalogue search."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import datetime
import hashlib
import json
from pathlib import Path
import urllib.request
from public_catalogue import public_response_bytes

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://raleighhrmprogram.catalogaccess.com/api/items/"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("search_file", help="Saved search JSON path")
    parser.add_argument("output_dir", help="Output directory under sources")
    args = parser.parse_args()
    if Path(args.output_dir).name != args.output_dir:
        parser.error("Use a plain output directory name")
    records = json.loads(Path(args.search_file).read_text())["PageResult"]["Items"]
    destination = ROOT / "sources" / args.output_dir
    destination.mkdir(exist_ok=True)

    def fetch(record):
        record_id = int(record["Id"])
        url = BASE + str(record_id)
        path = destination / f"item-{record_id}.json"
        if path.exists():
            body = path.read_bytes()
        else:
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (public historical research)"})
            with urllib.request.urlopen(request, timeout=40) as response:
                body = public_response_bytes(response.read())
            path.write_bytes(body)
        data = json.loads(body)
        item = data["Item"]
        manifest_entry = {"file": path.name, "url": url,
                          "sha256": hashlib.sha256(body).hexdigest(), "bytes": len(body),
                          "retrieved_or_verified_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
        summary = {"id": record_id, "item_id": item["ItemId"], "date": item["CreationDate"],
                   "description": item["Description"], "image_id": record.get("ImageId"),
                   "type_id": record["TypeId"]}
        return manifest_entry, summary

    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(fetch, records))
    (destination / "manifest.json").write_text(json.dumps([x[0] for x in results], indent=2) + "\n")
    (destination / "descriptions.json").write_text(json.dumps([x[1] for x in results], indent=2) + "\n")
    print(f"Preserved {len(results)} public records in {destination}")


if __name__ == "__main__":
    main()
