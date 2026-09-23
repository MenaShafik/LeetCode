# ==========================================================
# Problem    : Count Number of Pairs With Absolute Difference K
# URL        : https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Counting
#
# Acceptance : 85.5%
# Likes      : 1828  |  Dislikes: 50
#
# Language   : python
# Runtime    : 101  (beats 73.09129999999992%)
# Memory     : 12252000  (beats 94.1819%)
# Submitted  : 1790152143
# Exported   : 2026-09-23 11:55:04 UTC
#
# Hints: Can we check every possible pair?
#   Can we use a nested for loop to solve this problem?
# ==========================================================
class Solution(object):
    def countKDifference(self, nums, k):
        counter = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    counter+=1
        return counter
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
