# ================================================================
# Problem : Score of a String
# URL     : https://leetcode.com/problems/score-of-a-string/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# --- Community Stats ---
# Acceptance Rate : 91.3%
# Likes           : 858
# Dislikes        : 52
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12352000  (beats 62.36560000000001%)
# Submitted  : 1774733030
#
# --- Hints ---
# Sum the difference between all the adjacent characters by just taking the absolute difference of their ASCII values.
# ================================================================

class Solution(object):
    def scoreOfString(self, s):
        score = 0
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score
