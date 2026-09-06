# ==========================================================
# Problem    : Smallest Number With All Set Bits
# URL        : https://leetcode.com/problems/smallest-number-with-all-set-bits/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Bit Manipulation
#
# Acceptance : 80.1%
# Likes      : 379  |  Dislikes: 15
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12412000  (beats 18.0%)
# Submitted  : 1788685182
# Exported   : 2026-09-06 21:31:18 UTC
#
# Hints: Find the strictly greater power of 2, and subtract 1 from it.
# ==========================================================
class Solution(object):
    def smallestNumber(self, n):
        bits = bin(n)[2:]
        bits = bits.replace("0","1")
        return int(bits,2)
                
        """
        :type n: int
        :rtype: int
        """
        
