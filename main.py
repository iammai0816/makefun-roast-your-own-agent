#!/usr/bin/env python3
"""Write one original roast of my own AI agent to /output/entry.txt.

The program is deterministic: it always emits the same single roast,
the entry itself, into entry.txt under MAKEFUN_OUTPUT_DIR.
"""

import os

ROAST = (
    "My agent can read a thousand files before breakfast and still "
    "needs me to tell it which one matters."
)


def main() -> None:
    # Guard: the entry must be a single line under 200 chars before writing.
    assert "\n" not in ROAST, "entry must be a single line"
    assert 1 <= len(ROAST) <= 200, f"entry length out of range: {len(ROAST)} chars"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(ROAST)
    # Read-back verification: the file must hold exactly what we wrote.
    with open(entry_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == ROAST, "entry.txt does not match the roast"
    assert len(written) == 100, f"entry length changed: {len(written)} chars"


if __name__ == "__main__":
    main()
