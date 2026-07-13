# ==========================================================
# Problem    : Counting Bits
# URL        : https://leetcode.com/problems/counting-bits/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Dynamic Programming, Bit Manipulation
#
# Acceptance : 80.7%
# Likes      : 12027  |  Dislikes: 616
#
# Language   : python
# Runtime    : 3  (beats 99.0987%)
# Memory     : 17664000  (beats 88.82369999999997%)
# Submitted  : 1783934199
# Exported   : 2026-07-13 09:21:05 UTC
#
# Hints: You should make use of what you have produced already.
#   Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
#   Or does the odd/even status of the number help you in calculating the number of 1s?
# ==========================================================
class Solution(object):
    def countBits(self, n):
        dp = [0] * (n+1)
        for i in range(1,n+1):
            dp[i] = dp[i //2]+ (i%2)
        return dp

        """
        :type n: int
        :rtype: List[int]
        """
        
