#!/usr/bin/env python3
"""Print the one-sentence entry for the GTA 6 launch-week mishap bounty."""

import pathlib


def main() -> None:
    line = pathlib.Path(__file__).with_name("entry.txt").read_text(encoding="utf-8").strip()
    print(line)


if __name__ == "__main__":
    main()
