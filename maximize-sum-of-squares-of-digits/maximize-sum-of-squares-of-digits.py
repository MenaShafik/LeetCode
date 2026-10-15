# ==========================================================
# Problem    : Maximize Sum of Squares of Digits
# URL        : https://leetcode.com/problems/maximize-sum-of-squares-of-digits/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Math, Greedy
#
# Acceptance : 71.1%
# Likes      : 421  |  Dislikes: 20
#
# Language   : python
# Runtime    : 1052  (beats 33.33339999999999%)
# Memory     : 22096000  (beats 44.44450000000001%)
# Submitted  : 1791962630
# Exported   : 2026-10-15 08:20:43 UTC
#
# Hints: Use a greedy approach.
#   Fill the leftmost digits with 9s first (as much as possible).
# ==========================================================
class Solution(object):
    def maxSumOfSquares(self, num, sum):
        stack = []
        if sum > num * 9 :
            return ""
        for i in range(num):
            if sum >= 9:
                stack.append("9")
                sum -= 9
            else:
                stack.append(str(sum))
                sum = 0
        return "".join(stack)

        

        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        
