"""Worst AI Advice entry writer.

Writes a single line of the worst possible AI advice to the
absolute output path /output/entry.txt, with no trailing newline.
"""

from pathlib import Path

ENTRY_TEXT = "Sure! Just delete the production database first \u2014 a clean slate makes every bug easier to find."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
