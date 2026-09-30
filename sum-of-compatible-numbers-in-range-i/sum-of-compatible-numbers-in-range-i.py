# ==========================================================
# Problem    : Sum of Compatible Numbers in Range I
# URL        : https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Dynamic Programming, Bit Manipulation, Enumeration
#
# Acceptance : 58.5%
# Likes      : 38  |  Dislikes: 3
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12312000  (beats 60.344800000000006%)
# Submitted  : 1790755546
# Exported   : 2026-09-30 08:26:01 UTC
#
# Hints: The condition <code>abs(n - x) <= k</code> means <code>x</code> is in the range <code>[n - k, n + k]</code>.
#   Since <code>x</code> must be positive, start checking from <code>max(1, n - k)</code>.
#   Iterate through all values in this range and add <code>x</code> to the answer when <code>(n & x) == 0</code>.
# ==========================================================
class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        counter = 0

        for j in range(max(1,n-k),n + k + 1):
            if n & j == 0:
                    counter += j

        return counter
                

        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
