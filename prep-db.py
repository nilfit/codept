#!/usr/bin/python3
#
# invoke like `./prep-db.py </usr/share/unicode/extracted/DerivedName.txt >unicode.txt`

import sys

# Example input
# 0039          ; DIGIT NINE
# 003A          ; COLON

# Desired output
# 9 DIGIT NINE
# : COLON

for line in sys.stdin:
    parts = [s.strip() for s in line.split(';')]
    # Most non-codepoint lines will get dropped here
    if len(parts) == 1: continue
    try:
        # Hex to unicode char
        parts[0] = chr(int(parts[0], base=16))
        print(parts[0], parts[1])
    except ValueError:
        # truncate out the trailing newline
        print("WARNING skipping line: ", line[:-1], file=sys.stderr)
