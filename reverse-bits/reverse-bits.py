# ==========================================================
# Problem    : Reverse Bits
# URL        : https://leetcode.com/problems/reverse-bits/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Divide and Conquer, Bit Manipulation
#
# Acceptance : 68.8%
# Likes      : 5941  |  Dislikes: 1687
#
# Language   : python
# Runtime    : 8  (beats 96.43619999999999%)
# Memory     : 12304000  (beats 52.34009999999999%)
# Submitted  : 1784022134
# Exported   : 2026-07-14 09:54:00 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def reverseBits(self, n):
        bit = format(n,"032b")
        reversed_bit = bit[::-1]
        return int(reversed_bit, 2)
        
        """
        :type n: int
        :rtype: int
        """
        
