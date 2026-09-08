# ==========================================================
# Problem    : Sum of Good Numbers
# URL        : https://leetcode.com/problems/sum-of-good-numbers/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array
#
# Acceptance : 69.3%
# Likes      : 84  |  Dislikes: 33
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12476000  (beats 33.80280000000001%)
# Submitted  : 1788769709
# Exported   : 2026-09-08 11:10:44 UTC
#
# Hints: For each index, check if <code>nums[i]</code> is strictly greater than <code>nums[i - k]</code> and <code>nums[i + k]</code>.
# ==========================================================
class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        total = 0
        for i in range(len(nums)):
            good = True
            if i - k >= 0 and nums[i] <= nums[i-k]:
                good = False
            if i + k < len(nums) and nums[i] <= nums[i+k]:
                good =  False
            if good:
                total+= nums[i]
        return total

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
