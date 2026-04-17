# ================================================================
# Problem : Third Maximum Number
# URL     : https://leetcode.com/problems/third-maximum-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Sorting
#
# --- Community Stats ---
# Acceptance Rate : 39.2%
# Likes           : 3546
# Dislikes        : 3543
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 13316000  (beats 7.939599999999995%)
# Submitted  : 1773171972
#
# --- Hints ---
# N/A
# ================================================================

class Solution(object):
    def thirdMax(self, nums):
        for i in range(len(nums)):
            unique_nums = list(set(nums))
            unique_nums.sort(reverse=True)
            if len(unique_nums) >= 3:
                    return unique_nums[2]
            else:
                    return unique_nums[0]
        """
        :type nums: List[int]
        :rtype: int
        """
        
