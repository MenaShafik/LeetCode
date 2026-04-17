# ================================================================
# Problem : Search Insert Position
# URL     : https://leetcode.com/problems/search-insert-position/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Binary Search
#
# --- Community Stats ---
# Acceptance Rate : 51.1%
# Likes           : 18841
# Dislikes        : 902
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 13024000  (beats 10.051599999999993%)
# Submitted  : 1773692700
#
# --- Hints ---
# N/A
# ================================================================

class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if target <= nums[i]:
                return i

        return len(nums)
