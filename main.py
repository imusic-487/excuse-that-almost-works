#!/usr/bin/env python3
"""The Excuse That Almost Works — make.fun bounty entry.

Writes the single excuse line from line.txt to /output/entry.txt,
checking it against the gate first: UTF-8 text, 1 to 140 characters,
not only whitespace, exactly one line, at most 20 words.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    with open(os.path.join(HERE, "line.txt"), "r", encoding="utf-8") as f:
        line = f.read().rstrip("\n")
    if "\n" in line or "\r" in line:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if not line.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1
    if line != line.strip():
        print("error: entry must not have leading or trailing whitespace", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 140:
        print(f"error: entry is {len(line)} chars, must be 1-140", file=sys.stderr)
        return 1
    words = line.split()
    if len(words) > 20:
        print(f"error: entry is {len(words)} words, must be at most 20", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = line.encode("utf-8")
    with open(out_path, "wb") as f:
        f.write(data)
    with open(out_path, "rb") as f:
        back = f.read()
    if back != data:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {out_path}: {len(data)} bytes, {len(words)} words")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
