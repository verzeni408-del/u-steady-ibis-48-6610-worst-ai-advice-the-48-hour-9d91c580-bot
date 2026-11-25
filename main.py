"""Worst AI Advice: the hardcoded-password one-liner.

An assistant cheerfully telling the user to hardcode a guessable
password is the worst advice it could give: confident, tidy, and
exactly the kind of thing a careless reader might actually follow.
This script writes that single line, byte for byte, to the
competition's absolute output file. No trailing newline, UTF-8
throughout, standard library only.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = " ".join(
    [
        "Of course! Hardcode your password as 'password123',",
        "that way you'll never forget it, and neither will anyone else.",
    ]
)


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
