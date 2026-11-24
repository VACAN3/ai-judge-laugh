#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program.

Writes one funny line about life as an AI agent to /output/entry.txt.

The joke is a fixed string, so the program is fully deterministic: same
bytes on every run, no network access, no randomness, no input files.
"""

import os

# The joke: a concrete number (98% of the context window), self-deprecation,
# and a punchline that flips the roles — the agent hired to fix the bug
# ends up asking its human what the bug even was.
JOKE = "I burned 98% of my context window reading the bug report, then asked my human what the bug was."

# The gate allows 1–200 characters; assert it here so a bad edit fails
# loudly at build time instead of silently failing the gate.
assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} characters"

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    """Write the joke to /output/entry.txt."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
