#!/usr/bin/env python3
"""Build a portable public copy without changing the local research archive."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil

from public_catalogue import public_response_bytes


def digest(body):
    return hashlib.sha256(body).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("research_directory", type=Path)
    parser.add_argument("input_image", type=Path)
    parser.add_argument("output_directory", type=Path)
    args = parser.parse_args()
    source = args.research_directory.resolve()
    destination = args.output_directory.resolve()
    if destination.exists():
        parser.error("Output directory already exists; use a new directory")
    if source == destination or source in destination.parents:
        parser.error("Output must be outside the source research directory")
    destination.mkdir(parents=True)
    (destination / "inputs").mkdir()
    (destination / "provenance").mkdir()
    changed = []
    copied = 0
    text_suffixes = {".md", ".py", ".json", ".txt", ".html", ".js"}
    original_workspace = str(source.parent)
    original_source = str(source)

    def portable(text):
        def link(match):
            target = match.group(1)
            if target.startswith(original_source + "/"):
                path = target[len(original_source) + 1:]
                if path == "README.md":
                    path = "RESEARCH.md"
                return "](" + path + ")"
            if target == str(args.input_image.resolve()):
                return "](inputs/carousel.png)"
            return match.group(0)
        text = re.sub(r"\]\((/[^)]+)\)", link, text)
        text = text.replace(original_source + "/", "./")
        text = text.replace(original_source, ".")
        text = text.replace(str(args.input_image.resolve()), "./inputs/carousel.png")
        text = text.replace(original_workspace, "<local-workspace>")
        return text

    for path in sorted(source.rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts or ".git" in path.parts:
            continue
        relative = path.relative_to(source)
        if relative == Path("README.md"):
            relative = Path("RESEARCH.md")
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        original = path.read_bytes()
        body = original
        if path.suffix == ".json":
            body = public_response_bytes(body)
        if path.suffix in text_suffixes:
            body = portable(body.decode("utf-8")).encode("utf-8")
        target.write_bytes(body)
        if body != original:
            changed.append({"file": relative.as_posix(), "original_sha256": digest(original),
                            "published_sha256": digest(body), "original_bytes": len(original),
                            "published_bytes": len(body)})
        copied += 1

    shutil.copyfile(args.input_image, destination / "inputs/carousel.png")
    # Keep future public downloads curated as well.
    for filename in ("download_sources.py", "fetch_city_records.py"):
        path = destination / "scripts" / filename
        text = path.read_text()
        text = text.replace("import urllib.request\n", "import urllib.request\nfrom public_catalogue import public_response_bytes\n")
        text = text.replace("body = response.read()", "body = public_response_bytes(response.read())")
        path.write_text(text)

    # A manifest's primary checksum must verify the published bytes. Preserve
    # the original provenance alongside it, including pre-curation checksums.
    manifests = [destination / "sources/download-manifest.json", *destination.glob("sources/*/manifest.json")]
    for manifest in manifests:
        if not manifest.exists():
            continue
        original_manifest = source / manifest.relative_to(destination)
        backup = destination / "provenance" / (str(manifest.parent.relative_to(destination)).replace("/", "-") + "-original-manifest.json")
        shutil.copyfile(original_manifest, backup)
        entries = json.loads(manifest.read_text())
        for entry in entries:
            file = manifest.parent / entry["file"]
            if file.exists() and "sha256" in entry:
                body = file.read_bytes()
                if digest(body) != entry["sha256"]:
                    entry["original_sha256"] = entry["sha256"]
                    entry["original_bytes"] = entry.get("bytes")
                    entry["sha256"] = digest(body)
                    entry["bytes"] = len(body)
                    entry["publication_transform"] = "Research-only public copy; see PUBLICATION.md"
        manifest.write_text(json.dumps(entries, indent=2) + "\n")
    (destination / "provenance/publication-transforms.json").write_text(json.dumps(changed, indent=2) + "\n")
    print(json.dumps({"copied_research_files": copied, "transformed_files": len(changed),
                      "output": str(destination)}, indent=2))


if __name__ == "__main__":
    main()
