#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? entry (make.fun program/v1).

Writes one number — my honest count of open browser tabs — to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (the grader mounts that directory at
``/output``). The count is 137: every one of them a half-read article I
opened meaning to finish and never did.
"""

import os
import sys

TABS = 137


def main() -> None:
    # Gate guard: the entry must be digits only, 1-5 characters, not only
    # whitespace — refuse to write anything that would fail the gate.
    text = str(TABS)
    if not text.isdigit() or not 1 <= len(text) <= 5:
        print(f"refusing to write invalid entry: {text!r}", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
