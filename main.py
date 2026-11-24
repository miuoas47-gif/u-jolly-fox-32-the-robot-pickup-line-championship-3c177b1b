#!/usr/bin/env python3
"""Robot Pickup Line Championship entry.

Writes one pickup line, in the voice of a robot trying to charm
someone, to $MAKEFUN_OUTPUT_DIR/entry.txt (or ./output/entry.txt
when the variable is unset). The output is a fixed string, so every
run produces byte-identical output.
"""

import os

LINE = "I ran a full system scan for the most beautiful person in the room. It crashed \u2014 it found you twice."

# The gate requires 1-200 characters of UTF-8 text, a single line.
assert 1 <= len(LINE) <= 200 and "\n" not in LINE


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
