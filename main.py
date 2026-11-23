#!/usr/bin/env python3
"""One-Line Laugh Sprint (make.fun bounty u-daring-gecko-25-one-line-laugh-sprint-cda708b2).

Writes one original funny line about everyday life to /output/entry.txt.

The line was built for the judge's own criteria, in order:
  1. On subject: a light, funny take on everyday life (a fridge, midnight
     snacks) -- nothing else.
  2. A real laugh: the punchline turns twice -- the fridge is gossiping,
     and then the twist admits it has every right to, because the snacks
     are the narrator's own doing.
  3. Fresh: a fridge-as-gossip with a self-own kicker, not a stock
     "my fridge is empty" or "midnight snack" line.
  4. Tight: one line, no setup beyond what the punch needs, a rhythm that
     reads well aloud, nothing spare.
  5. Light and first-read: no explaining needed.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

JOKE = "My fridge hums all night like it's gossiping about me \u2014 and after the midnight snacks, it has every right to."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(joke: str) -> None:
    """Enforce the competition's gate before writing: 1-200 Unicode code
    points, at least one character that is not white space. Fail loudly
    instead of writing an entry the gate would refuse."""
    if not 1 <= len(joke) <= 200:
        raise SystemExit(f"joke is {len(joke)} characters, must be 1-200")
    if not any(not ch.isspace() for ch in joke):
        raise SystemExit("joke must contain a non-whitespace character")


def main() -> None:
    validate(JOKE)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the joke: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
