# ==========================================================
# Problem    : Array Partition
# URL        : https://leetcode.com/problems/array-partition/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Greedy, Sorting, Counting Sort
#
# Acceptance : 81.7%
# Likes      : 2420  |  Dislikes: 304
#
# Language   : python
# Runtime    : 23  (beats 99.07680000000002%)
# Memory     : 14124000  (beats 13.846100000000007%)
# Submitted  : 1777148858
# Exported   : 2026-04-25 20:37:06 UTC
#
# Hints: Obviously, brute force won't help here. Think of something else, take some example like 1,2,3,4.
#   How will you make pairs to get the result? There must be some pattern.
#   Did you observe that- Minimum element gets add into the result in sacrifice of maximum element.
#   Still won't able to find pairs? Sort the array and try to find the pattern.
# ==========================================================
class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        return sum((nums[::2]))

        """
        :type nums: List[int]
        :rtype: int
        """
        
