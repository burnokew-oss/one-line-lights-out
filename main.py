"""One Line, Lights Out — writes one status update to /output/entry.txt.

Pure stdlib, deterministic: the same single line on every run.
"""

from pathlib import Path

ENTRY = "Laptop closed. Your unsent message is still in the box, and so am I."


def main() -> None:
    # Self-check the gate: 1 to 200 characters, not only white space.
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry fails the gate"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
