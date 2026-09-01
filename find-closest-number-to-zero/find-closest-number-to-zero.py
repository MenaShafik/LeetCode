# ==========================================================
# Problem    : Find Closest Number to Zero
# URL        : https://leetcode.com/problems/find-closest-number-to-zero/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array
#
# Acceptance : 48.2%
# Likes      : 821  |  Dislikes: 58
#
# Language   : python
# Runtime    : 3  (beats 91.6382%)
# Memory     : 12544000  (beats 46.92829999999999%)
# Submitted  : 1788253224
# Exported   : 2026-09-01 09:16:05 UTC
#
# Hints: Keep track of the number closest to 0 as you iterate through the array.
#   Ensure that if multiple numbers are closest to 0, you store the one with the largest value.
# ==========================================================
class Solution(object):
    def findClosestNumber(self, nums):
        return min(nums, key=lambda x: (abs(x), -x))
        """
        :type nums: List[int]
        :rtype: int
        """
        
