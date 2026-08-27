# ==========================================================
# Problem    : Binary Number with Alternating Bits
# URL        : https://leetcode.com/problems/binary-number-with-alternating-bits/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Bit Manipulation
#
# Acceptance : 70.0%
# Likes      : 1733  |  Dislikes: 125
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12296000  (beats 90.6634%)
# Submitted  : 1787820856
# Exported   : 2026-08-27 09:16:31 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def hasAlternatingBits(self, n):
        bits = bin(n)[2:]
        for i in range(1,len(bits)):
            if bits[i] == bits[i-1]:
                return False
        return True
        """
        :type n: int
        :rtype: bool
        """
        
