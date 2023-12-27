#!/usr/bin/env python3

# Original perl script by Matt Might, CC0
# From: 3 shell scripts to improve your writing, or "My Ph.D. advisor rewrote himself in bash."
# Accessed 2023-12-27 at https://matt.might.net/articles/shell-scripts-for-passive-voice-weasel-words-duplicates/
# Converted to Python by Alessandro G. Magnasco, CC0 2023

import sys

def find_duplicates(filename):
    dup_count = 0
    last_word = ""
    line_num = 0

    with open(filename, 'r') as file:
        for line in file:
            line_num += 1
            words = [word for word in line.split() if word.strip()]

            for word in words:
                # Skip punctuation:
                if not word.isalnum():
                    last_word = ""
                    continue

                # Found a dup?
                if word.lower() == last_word.lower():
                    print(f"{filename}:{line_num} {word}")
                    dup_count += 1

                # Mark this as the last word:
                last_word = word

    return dup_count

if len(sys.argv) < 2:
    print("usage: dups.py <file> ...")
    sys.exit()

total_dup_count = 0
for filename in sys.argv[1:]:
    dup_count = find_duplicates(filename)
    total_dup_count += dup_count

sys.exit(total_dup_count)
