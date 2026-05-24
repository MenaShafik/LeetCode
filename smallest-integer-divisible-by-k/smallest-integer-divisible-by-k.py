# ==========================================================
# Problem    : Smallest Integer Divisible by K
# URL        : https://leetcode.com/problems/smallest-integer-divisible-by-k/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Hash Table, Math
#
# Acceptance : 54.3%
# Likes      : 1654  |  Dislikes: 1173
#
# Language   : python
# Runtime    : 11  (beats 94.6759%)
# Memory     : 15252000  (beats 33.56490000000001%)
# Submitted  : 1779611199
# Exported   : 2026-05-24 08:28:42 UTC
#
# Hints: 11111 = 1111 * 10 + 1
We only need to store remainders modulo K.
#   If we never get a remainder of 0, why would that happen, and how would we know that?
# ==========================================================
class Solution(object):
    def smallestRepunitDivByK(self, k):
        if k % 2 == 0 or k % 5 == 0:
            return -1
        remainder = 0
        length = 0
        for i in range(1,k+1):
            remainder = (remainder * 10 + 1) % k
            length+=1
            if remainder == 0:
                return length
        return -1
        """
        :type k: int
        :rtype: int
        """
        
