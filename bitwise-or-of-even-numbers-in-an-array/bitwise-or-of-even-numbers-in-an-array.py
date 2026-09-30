# ==========================================================
# Problem    : Bitwise OR of Even Numbers in an Array
# URL        : https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Bit Manipulation, Simulation
#
# Acceptance : 84.9%
# Likes      : 47  |  Dislikes: 4
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12316000  (beats 59.4594%)
# Submitted  : 1790754690
# Exported   : 2026-09-30 08:26:02 UTC
#
# Hints: Simulate as described
# ==========================================================
class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        counter = 0
        for i in nums:
            if i %2 == 0:
                counter|=i
        return counter

        """
        :type nums: List[int]
        :rtype: int
        """
        
