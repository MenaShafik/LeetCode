# ==========================================================
# Problem    : Maximum Product of Two Elements in an Array
# URL        : https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Sorting, Heap (Priority Queue)
#
# Acceptance : 83.6%
# Likes      : 2624  |  Dislikes: 240
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12464000  (beats 42.290800000000004%)
# Submitted  : 1776806638
# Exported   : 2026-04-21 21:49:35 UTC
#
# Hints: Use brute force: two loops to select i and j, then select the maximum value of (nums[i]-1)*(nums[j]-1).
# ==========================================================
class Solution(object):
    def maxProduct(self, nums):

        nums.sort()
        return (nums[-1] -1)*(nums[-2] -1)

        """
        :type nums: List[int]
        :rtype: int
        """
        
