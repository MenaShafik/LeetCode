# ==========================================================
# Problem    : Minimum Add to Make Parentheses Valid
# URL        : https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : String, Stack, Greedy, Bracket Sequences
#
# Acceptance : 74.2%
# Likes      : 5167  |  Dislikes: 257
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12408000  (beats 19.03719999999999%)
# Submitted  : 1791273159
# Exported   : 2026-10-06 12:01:33 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def minAddToMakeValid(self, s):
        low = 0
        high = 0
        for i in s:
            if i == "(":
                low+=1
            else:
                low-=1
                if low < 0:
                    high+=1
                    low =0
        return low+high
        """
        :type s: str
        :rtype: int
        """
        
