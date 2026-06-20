# ==========================================================
# Problem    : Maximum Product of Three Numbers
# URL        : https://leetcode.com/problems/maximum-product-of-three-numbers/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math, Sorting
#
# Acceptance : 46.0%
# Likes      : 4557  |  Dislikes: 716
#
# Language   : python
# Runtime    : 4  (beats 98.9807%)
# Memory     : 13312000  (beats 7.248000000000005%)
# Submitted  : 1781948555
# Exported   : 2026-06-20 22:35:53 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        
        max1= nums[-1] * nums[-2] * nums[-3]
        max2 =     nums[0] * nums[1] * nums[-1]
        if max1 > max2:
            return max1
        return max2

        
        """
        :type nums: List[int]
        :rtype: int
        """
        
