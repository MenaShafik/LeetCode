# ==========================================================
# Problem    : Check if All Characters Have Equal Number of Occurrences
# URL        : https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String, Counting
#
# Acceptance : 79.5%
# Likes      : 1040  |  Dislikes: 29
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12404000  (beats 35.714200000000005%)
# Submitted  : 1777412469
# Exported   : 2026-04-28 21:53:58 UTC
#
# Hints: Build a dictionary containing the frequency of each character appearing in s
#   Check if all values in the dictionary are the same.
# ==========================================================

class Solution(object):
    def areOccurrencesEqual(self, s):
        return len(set(s.count(ch) for ch in set(s)))==1

        """
        :type s: str
        :rtype: bool
        """
        
