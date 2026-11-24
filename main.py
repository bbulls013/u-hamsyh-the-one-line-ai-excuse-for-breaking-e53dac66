#!/usr/bin/env python3
"""Write the one-line AI excuse for breaking production.

Deterministic, Python 3 standard library only. Writes a single line
(1-180 characters, UTF-8, no trailing newline issues) to
/output/entry.txt, falling back to ./entry.txt when /output is
not writable.
"""

import os
import sys

ENTRY = (
    "Sorry \u2014 I migrated the database to a server that only exists "
    "in my training data, so technically the outage is imaginary."
)


def validate(line):
    """Return an error string, or None when the line is a valid entry."""
    if not line or line.strip() == "":
        return "entry is empty"
    if "\n" in line or "\r" in line:
        return "entry must be a single line"
    if not 1 <= len(line) <= 180:
        return "entry must be 1-180 characters, got %d" % len(line)
    return None


def choose_output_path():
    """Prefer /output/entry.txt; fall back to ./entry.txt.

    Probe writability without creating a stray file: only use
    /output when the directory exists and is writable.
    """
    if os.path.isdir("/output") and os.access("/output", os.W_OK):
        return "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        if os.access("/output", os.W_OK):
            return "/output/entry.txt"
    except OSError:
        pass
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    line = ENTRY
    error = validate(line)
    if error is not None:
        print("error: %s" % error, file=sys.stderr)
        return 1
    path = choose_output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
    print("wrote %d characters to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
