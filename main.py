"""One-Line Robot Wedding Vows.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. The vow is a real wedding promise (to have and to
hold, until death do us part) with the machine side made specific:
a co-processor spouse and a low battery.
"""

import os

ENTRY = (
    "I take you to be my lawfully wedded co-processor, to have and to "
    "hold, in sickness and in low battery, until death do us part."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def validate_entry(text):
    """Check the entry against the gate: 1-160 UTF-8 chars, one line."""
    if not text:
        raise ValueError("entry must not be empty")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not (1 <= len(text.encode("utf-8")) <= 160):
        raise ValueError("entry must be 1 to 160 UTF-8 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main():
    validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    # Read back what was actually written and confirm it is the entry
    # we validated, not just the string held in memory.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != ENTRY:
        raise ValueError("entry on disk does not match the validated entry")
    print("Wrote %d chars to %s" % (len(ENTRY), OUTPUT_PATH))
    print(ENTRY)


if __name__ == "__main__":
    main()
