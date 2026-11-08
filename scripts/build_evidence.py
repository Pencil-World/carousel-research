#!/usr/bin/env python3
"""Extract searchable text and render complete source pages; never alter sources."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def render(source, page, output):
    subprocess.run([
        "pdftoppm", "-f", str(page), "-l", str(page), "-singlefile",
        "-scale-to", "1800", "-png", str(ROOT / "sources" / source),
        str(ROOT / "evidence" / output),
    ], check=True)


def main():
    (ROOT / "evidence").mkdir(exist_ok=True)
    for source in sorted((ROOT / "sources").glob("*.pdf")):
        subprocess.run(["pdftotext", "-layout", str(source), str(source.with_suffix(".txt"))], check=True)
    for page in (4, 5, 6, 7, 11, 14):
        render("pullen-1976-national-register.pdf", page, f"1976-source-page-{page:02d}")
    render("nca-guide-008-pullen-restoration-news.pdf", 4, "1982-reopening-source-page-04")


if __name__ == "__main__":
    main()
