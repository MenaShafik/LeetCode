# ==========================================================
# Problem    : Find N Unique Integers Sum up to Zero
# URL        : https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math
#
# Acceptance : 78.4%
# Likes      : 2506  |  Dislikes: 622
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12420000  (beats 44.32979999999999%)
# Submitted  : 1785780987
# Exported   : 2026-08-04 22:21:36 UTC
#
# Hints: Return an array where the values are symmetric. (+x , -x).
#   If n is odd, append value 0 in your returned array.
# ==========================================================
class Solution(object):
    def sumZero(self, n):
        stack = []
        if n % 2 != 0:
                stack.append(0)
        for i in range(1,n//2 +1):

            stack.append(i)
            stack.append(-i)
        return stack
            
        """
        :type n: int
        :rtype: List[int]
        """
        
