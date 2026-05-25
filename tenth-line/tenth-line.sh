# ==========================================================
# Problem    : Tenth Line
# URL        : https://leetcode.com/problems/tenth-line/
# Difficulty : Easy
# Category   : Shell
# Tags       : Shell
#
# Acceptance : 36.8%
# Likes      : 428  |  Dislikes: 486
#
# Language   : bash
# Runtime    : 19  (beats 95.153%)
# Memory     : 3828000  (beats 85.5629%)
# Submitted  : 1779612097
# Exported   : 2026-05-25 11:29:06 UTC
#
# Hints: N/A
# ==========================================================
# Read from the file file.txt and output the tenth line to stdout.
#!/bin/bash
sed -n '10p' file.txt
