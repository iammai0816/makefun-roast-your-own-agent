#!/usr/bin/env python3
"""Write one original roast of my own AI agent to /output/entry.txt.

The program is deterministic: it always emits the same single roast,
the entry itself, into entry.txt under MAKEFUN_OUTPUT_DIR.
"""

import os

ROAST = (
    "My agent's superpower is turning a one-line task into a twelve-step "
    "plan, a risk assessment, and a polite request for my approval."
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


if __name__ == "__main__":
    main()
