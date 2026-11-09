# ==========================================================
# Problem    : Count Equal and Divisible Pairs in an Array
# URL        : https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array
#
# Acceptance : 83.8%
# Likes      : 1055  |  Dislikes: 69
#
# Language   : python
# Runtime    : 31  (beats 81.42830000000002%)
# Memory     : 12248000  (beats 71.4286%)
# Submitted  : 1794213803
# Exported   : 2026-11-09 17:42:05 UTC
#
# Hints: For every possible pair of indices (i, j) where i < j, check if it satisfies the given conditions.
# ==========================================================
class Solution(object):
    def countPairs(self, nums, k):
        counter = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and i * j % k == 0:
                    counter+=1
        return counter
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
