# ================================================================
# Problem : Check if Strings Can be Made Equal With Operations I
# URL     : https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# --- Community Stats ---
# Acceptance Rate : 61.9%
# Likes           : 442
# Dislikes        : 46
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12256000  (beats 95.42280000000001%)
# Submitted  : 1774812965
#
# --- Hints ---
# <div class="_1l1MA">Since the strings are very small you can try a brute-force approach.</div>
# <div class="_1l1MA">There are only <code>2</code> different swaps that are possible in a string.</div>
# ================================================================

from collections import Counter
class Solution(object):
    def canBeEqual(self, s1, s2):
        return (
            sorted(s1[::2]) == sorted(s2[::2]) and
            sorted(s1[1::2]) == sorted(s2[1::2])
        )
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
