# ================================================================
# Problem : Count the Number of Consistent Strings
# URL     : https://leetcode.com/problems/count-the-number-of-consistent-strings/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, String, Bit Manipulation, Counting
#
# --- Community Stats ---
# Acceptance Rate : 88.5%
# Likes           : 2277
# Dislikes        : 90
#
# --- My Submission ---
# Language   : python
# Runtime    : 169  (beats 89.98030000000001%)
# Memory     : 14652000  (beats 17.09240000000001%)
# Submitted  : 1775253759
#
# --- Hints ---
# A string is incorrect if it contains a character that is not allowed
# Constraints are small enough for brute force
# ================================================================

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed_set = set(allowed)
        count = 0

        for word in words:
            ok = True
            for ch in word:
                if ch not in allowed_set:
                    ok = False
                    break
            if ok:
                count += 1

        return count
        
