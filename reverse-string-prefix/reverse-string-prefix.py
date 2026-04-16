# ================================================================
# Problem : Reverse String Prefix
# URL     : https://leetcode.com/problems/reverse-string-prefix/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Two Pointers, String
#
# --- Community Stats ---
# Acceptance Rate : 89.4%
# Likes           : 47
# Dislikes        : 1
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12432000  (beats 28.1192%)
# Submitted  : 1775253328
#
# --- Hints ---
# Simulate as described
# ================================================================

class Solution(object):
    def reversePrefix(self, s, k):
        return s[:k][::-1] + s[k:]
