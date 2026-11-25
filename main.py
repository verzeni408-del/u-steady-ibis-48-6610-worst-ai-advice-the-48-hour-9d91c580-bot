"""Worst AI Advice, take two: ship-it-Friday edition.

The worst advice an AI could hand a developer is the kind that
sounds like confidence: push straight to production on a Friday
evening, skip the safety net, and call the fallout "team building".
This script drops that one-liner, byte for byte, into the
competition's absolute output file. No newline at the end, UTF-8
throughout, standard library only. The advice string is assembled
from two plain literals so the full line stays readable in source.
"""

from pathlib import Path

DESTINATION = Path("/output/entry.txt")

ADVICE = (
    "Absolutely! Deploy on Friday at 5pm without a backup, "
    "nothing builds team spirit like a weekend outage."
)


def publish_advice() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    with DESTINATION.open("w", encoding="utf-8", newline="") as handle:
        handle.write(ADVICE)


if __name__ == "__main__":
    publish_advice()
