# ==========================================================
# Problem    : Word Frequency
# URL        : https://leetcode.com/problems/word-frequency/
# Difficulty : Medium
# Category   : Shell
# Tags       : Shell
#
# Acceptance : 29.3%
# Likes      : 585  |  Dislikes: 311
#
# Language   : bash
# Runtime    : 51  (beats 96.4654%)
# Memory     : 3388000  (beats 100.0%)
# Submitted  : 1782556359
# Exported   : 2026-06-27 10:34:24 UTC
#
# Hints: N/A
# ==========================================================
# Read from the file words.txt and output the word frequency list to stdout.
#!/bin/bash

mawk '{
    for (i = 1; i <= NF; i++) words[$i]++
}
END {
    for (w in words) printf "%s %d\n", w, words[w]
}' words.txt | sort -k2,2rn
