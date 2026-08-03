# ==========================================================
# Problem    : Convert Integer to the Sum of Two No-Zero Integers
# URL        : https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# Acceptance : 59.2%
# Likes      : 871  |  Dislikes: 371
#
# Language   : python
# Runtime    : 3  (beats 77.8626%)
# Memory     : 12832000  (beats 6.106800000000007%)
# Submitted  : 1785749579
# Exported   : 2026-08-03 16:09:19 UTC
#
# Hints: Loop through all elements from 1 to n.
#   Choose A = i and B = n - i then check if A and B are both No-Zero integers.
# ==========================================================
class Solution(object):
    def getNoZeroIntegers(self, n):
        def noZero(x):
            return '0' not in str(x)
        for a in range(1,n):
            b = n - a
            if noZero(a) and noZero(b):
                return [a,b]
        """
        :type n: int
        :rtype: List[int]
        """
        
