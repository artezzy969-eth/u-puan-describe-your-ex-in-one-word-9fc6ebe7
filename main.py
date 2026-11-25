#!/usr/bin/env python3
"""Describe Your Ex in One Word — entry: Substitute.

Writes exactly one word, and nothing else, to entry.txt.

The verdict: a substitute teacher. They were never the real one, just
filling in until the real one arrived — and the whole class knew it
before you did.
"""

import os
from pathlib import Path

WORD = "Substitute"

# The gate allows 1-111 UTF-8 characters; a single word with no spaces,
# no punctuation and no trailing newline keeps the entry valid and the
# joke self-contained.
assert WORD.isalpha() and 1 <= len(WORD.encode("utf-8")) <= 111


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    # write_bytes on purpose: no trailing newline, nothing else attached.
    (output_dir / "entry.txt").write_bytes(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()
