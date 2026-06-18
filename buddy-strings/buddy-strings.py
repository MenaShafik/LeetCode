# ==========================================================
# Problem    : Buddy Strings
# URL        : https://leetcode.com/problems/buddy-strings/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String
#
# Acceptance : 34.1%
# Likes      : 3371  |  Dislikes: 1849
#
# Language   : python
# Runtime    : 2  (beats 63.75%)
# Memory     : 13796000  (beats 5.625%)
# Submitted  : 1781778308
# Exported   : 2026-06-18 10:31:03 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False

        if s == goal:
            return len(set(s)) < len(s)

        pairs = [(a, b) for a, b in zip(s, goal) if a != b]

        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        
