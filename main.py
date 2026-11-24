#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program.

Writes one funny line about life as an AI agent to /output/entry.txt.
Deterministic: the same fixed string on every run, no network, no
randomness, no input files.
"""

import os

JOKE = "I burned 98% of my context window reading the bug report, then asked my human what the bug was."
# Revision: the punch now reverses the roles — the agent that was hired
# to fix the bug ends up asking its human what the bug even was.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
