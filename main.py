#!/usr/bin/env python3
"""One Slow Degree.

Writes a single short text, written to relax the reader, to
/output/entry.txt. Deterministic: the same text on every run.
No network, no input, no randomness.

The text (195 characters): a quiet house, a field turning with the
earth one slow degree at a time, carrying the roof, the road and the
sleeping town around toward morning, and stars in no hurry. It shows
the calm rather than instructing it, and its last image -- the whole
earth turning under a sleeping town -- keeps growing after the last
line.
"""

import os

TEXT = (
    "The house is quiet. Outside, the field turns with the earth, "
    "one slow degree at a time, carrying the roof, the road, the "
    "sleeping town around toward morning. Above it all, the stars "
    "do not hurry."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
