# ==========================================================
# Problem    : Number of Even and Odd Bits
# URL        : https://leetcode.com/problems/number-of-even-and-odd-bits/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Bit Manipulation
#
# Acceptance : 74.1%
# Likes      : 381  |  Dislikes: 119
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12244000  (beats 98.7805%)
# Submitted  : 1788339899
# Exported   : 2026-09-02 09:08:37 UTC
#
# Hints: Maintain two integer variables, even and odd, to count the number of even and odd indices in the binary representation of integer n.
#   Divide n by 2 while n is positive, and if n modulo 2 is 1, add 1 to its corresponding variable.
# ==========================================================
class Solution(object):
    def evenOddBit(self, n):
        even=0
        odd= 0
        binary = bin(n)[2:]
        for i in range(len(binary)):
            bit_position = len(binary) - 1 - i
            if binary[i] =="1":
                if bit_position %2 == 0:
                    even+= 1
                else:
                    odd+=1
        return [even,odd]
        """
        :type n: int
        :rtype: List[int]
        """
        
