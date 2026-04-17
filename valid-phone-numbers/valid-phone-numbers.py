# ================================================================
# Problem : Valid Phone Numbers
# URL     : https://leetcode.com/problems/valid-phone-numbers/
# Difficulty : Easy
# Category   : Shell
# Tags       : Shell
#
# --- Community Stats ---
# Acceptance Rate : 29.4%
# Likes           : 486
# Dislikes        : 983
#
# --- My Submission ---
# Language   : bash
# Runtime    : 62  (beats 68.09559999999999%)
# Memory     : 3460000  (beats 72.36489999999999%)
# Submitted  : 1772651506
#
# --- Hints ---
# N/A
# ================================================================

# Read from the file file.txt and output all valid phone numbers to stdout.
grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt
