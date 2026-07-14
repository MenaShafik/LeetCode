# ==========================================================
# Problem    : Number of 1 Bits
# URL        : https://leetcode.com/problems/number-of-1-bits/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Divide and Conquer, Bit Manipulation
#
# Acceptance : 77.1%
# Likes      : 7208  |  Dislikes: 1372
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12416000  (beats 16.226799999999997%)
# Submitted  : 1784021751
# Exported   : 2026-07-14 09:54:01 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def hammingWeight(self, n):
        bit = bin(n)[2:]
        count = 0
        for num in bit:
            if num == "1":
                count+=1
        return count

        """
        :type n: int
        :rtype: int
        """
        
