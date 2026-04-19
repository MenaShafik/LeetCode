# ==========================================================
# Problem    : Find Missing Elements
# URL        : https://leetcode.com/problems/find-missing-elements/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Sorting
#
# Acceptance : 83.0%
# Likes      : 78  |  Dislikes: 4
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12508000  (beats 6.169700000000002%)
# Submitted  : 1776631633
# Exported   : 2026-04-19 21:27:00 UTC
#
# Hints: First, find the maximum and minimum elements in the array.
#   Then, iterate over all the integers in the range <code>[min, max]</code> and check if they are in the array.
#   If not, add them to the array, and return the sorted array at the end.
# ==========================================================
class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        arr = []
        for i in range(len(nums) - 1):
            for num in range(nums[i] + 1, nums[i+1]):
                arr.append(num)
        return arr
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
