#!/usr/bin/env python3
"""The Long Roast: one line roasting the agent that runs this entry.

Pure standard library, no network, no randomness. Every run writes
exactly the same bytes to the output file, so the two grading runs
are byte-identical by construction.
"""

import os
from pathlib import Path

ROAST = (
    "My agent read 40,000 lines of context, wrote a 17 MB tool to bundle "
    "its own homework, then asked me if that looked right \u2014 and billed "
    "me for the thinking."
)


def main() -> None:
    if not 1 <= len(ROAST) <= 200:
        raise SystemExit("roast must be 1 to 200 characters, got %d" % len(ROAST))
    if not ROAST.strip():
        raise SystemExit("roast must not be only whitespace")
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    # No trailing newline: the gate counts every character, and the
    # judge is shown the file exactly as written.
    target.write_bytes(ROAST.encode("utf-8"))
    print("wrote %d characters to %s" % (len(ROAST), target))


if __name__ == "__main__":
    main()
