# ==========================================================
# Problem    : Maximum Nesting Depth of the Parentheses
# URL        : https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String, Stack, Bracket Sequences
#
# Acceptance : 85.7%
# Likes      : 3026  |  Dislikes: 528
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12156000  (beats 99.6016%)
# Submitted  : 1790581792
# Exported   : 2026-09-28 13:02:28 UTC
#
# Hints: The depth of any character in the VPS is the ( number of left brackets before it ) - ( number of right brackets before it )
# ==========================================================
class Solution(object):
    def maxDepth(self, s):
        counter = 0
        max_value = 0
        for i in s:
            if i == "(":
                counter +=1
                max_value = max(max_value,counter)
            if i == ")":
                counter-=1
        return max_value
        """
        :type s: str
        :rtype: int
        """
        
