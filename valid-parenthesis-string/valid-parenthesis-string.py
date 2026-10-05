# ==========================================================
# Problem    : Valid Parenthesis String
# URL        : https://leetcode.com/problems/valid-parenthesis-string/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : String, Dynamic Programming, Stack, Greedy, Bracket Sequences
#
# Acceptance : 42.8%
# Likes      : 7478  |  Dislikes: 242
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12296000  (beats 91.7448%)
# Submitted  : 1791099036
# Exported   : 2026-10-05 10:34:04 UTC
#
# Hints: Use backtracking to explore all possible combinations of treating '*' as either '(', ')', or an empty string. If any combination leads to a valid string, return true.
#   DP[i][j] represents whether the substring s[i:j] is valid.
#   Keep track of the count of open parentheses encountered so far. If you encounter a close parenthesis, it should balance with an open parenthesis. Utilize a stack to handle this effectively.
#   How about using 2 stacks instead of 1? Think about it.
# ==========================================================
class Solution(object):
    def checkValidString(self, s):
        low= 0
        high = 0
        for i in s:
            if i == "(":
                low+=1
                high+=1
            elif i== ")":
                low-=1
                high-=1
            else:
                low-=1
                high+=1
            if high < 0:
                return False
            if low < 0:
                low = 0
        return low == 0

        """
        :type s: str
        :rtype: bool
        """
        
