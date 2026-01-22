#!/usr/bin/env python3

from pathlib import Path
import re
import sys

if len(sys.argv) == 2:
    year = sys.argv[1]
else:
    sys.stderr.write("Error: Year argument is missing.\n")
    sys.exit(1)

base_dir = Path(__file__).resolve().parent.parent

src_dir = base_dir / year

toc_path = src_dir / "0200-toc.md"

toc = ""

toc += "## Table of contents\n\n"

def header_to_anchor(header):
    return header.lower()

for file_path in sorted(src_dir.glob("*.md")):
    if file_path != toc_path:
        with file_path.open() as f:
            for line in f:
                m = re.search(r"^(#+) (.*?)(?:\s+\{[^}]*\})?$", line)
                if m:
                    prefix = m.group(1)
                    header = m.group(2).strip()
                    level = len(prefix)
                    if level <= 3:
                        toc += "  " * (level - 2)
                        toc += f"* {header}\n"

with toc_path.open("w") as f:
    f.write(toc)
