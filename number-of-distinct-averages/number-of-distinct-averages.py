# ==========================================================
# Problem    : Number of Distinct Averages
# URL        : https://leetcode.com/problems/number-of-distinct-averages/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Two Pointers, Sorting
#
# Acceptance : 59.2%
# Likes      : 440  |  Dislikes: 36
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12388000  (beats 53.5433%)
# Submitted  : 1789071754
# Exported   : 2026-09-10 20:25:58 UTC
#
# Hints: Try sorting the array.
#   Store the averages being calculated, and find the distinct ones.
# ==========================================================
class Solution(object):
    def distinctAverages(self, nums):
        nums.sort()
        left, right = 0, len(nums) - 1
        sums = set()

        while left < right:
            sums.add(nums[left] + nums[right])
            left += 1
            right -= 1

        return len(sums)
        """
        :type nums: List[int]
        :rtype: int
        """
        
