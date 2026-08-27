# ==========================================================
# Problem    : Prime Number of Set Bits in Binary Representation
# URL        : https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Bit Manipulation, Primality Test
#
# Acceptance : 79.0%
# Likes      : 1041  |  Dislikes: 526
#
# Language   : python
# Runtime    : 91  (beats 93.63460000000003%)
# Memory     : 12692000  (beats 51.9507%)
# Submitted  : 1787821939
# Exported   : 2026-08-27 09:16:29 UTC
#
# Hints: Write a helper function to count the number of set bits in a number, then check whether the number of set bits is 2, 3, 5, 7, 11, 13, 17 or 19.
# ==========================================================
class Solution(object):
    def countPrimeSetBits(self, left, right):
        prime = {2,3,5,7,11,13,17,19}
        count = 0
        for i in range(left,right+1):
            ones = bin(i).count("1")
            if ones in prime:
                count+=1
        return count
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        
