# ==========================================================
# Problem    : XOR Operation in an Array
# URL        : https://leetcode.com/problems/xor-operation-in-an-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Bit Manipulation
#
# Acceptance : 88.0%
# Likes      : 1555  |  Dislikes: 343
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12244000  (beats 88.1557%)
# Submitted  : 1792479660
# Exported   : 2026-10-20 07:16:42 UTC
#
# Hints: Simulate the process, create an array nums and return the Bitwise XOR of all elements of it.
# ==========================================================
class Solution(object):
    def xorOperation(self, n, start):
        counter = 0
        for i in range(n):
            val = start+2*i
            counter = counter ^ val
        return counter

        """
        :type n: int
        :type start: int
        :rtype: int
        """
        
