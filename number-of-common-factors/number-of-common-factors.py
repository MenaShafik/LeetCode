# ==========================================================
# Problem    : Number of Common Factors
# URL        : https://leetcode.com/problems/number-of-common-factors/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Enumeration, Number Theory, Euclidean Algorithm, Greatest Common Divisor
#
# Acceptance : 80.4%
# Likes      : 695  |  Dislikes: 14
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12320000  (beats 57.1429%)
# Submitted  : 1787218297
# Exported   : 2026-08-21 21:52:26 UTC
#
# Hints: For each integer in range [1,1000], check if it’s divisible by both A and B.
# ==========================================================
class Solution(object):
    def commonFactors(self, a, b):
        counter = 0
        for i in range(1,min(a,b)+1):
            if a % i ==0 and b% i ==0:
                counter+=1
        return counter
        
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
