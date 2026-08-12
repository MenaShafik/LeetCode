# ==========================================================
# Problem    : Find First and Last Position of Element in Sorted Array
# URL        : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Array, Binary Search
#
# Acceptance : 49.5%
# Likes      : 23602  |  Dislikes: 656
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 13036000  (beats 71.62370000000001%)
# Submitted  : 1786525793
# Exported   : 2026-08-12 13:56:24 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def searchRange(self, nums, target):
        l1 = 0
        r1 = len(nums) - 1

        first_occ = -1

        # Find first occurrence
        while l1 <= r1:
            mid = (l1 + r1) // 2

            if nums[mid] >= target:
                if nums[mid] == target:
                    first_occ = mid
                r1 = mid - 1
            else:
                l1 = mid + 1

        if first_occ == -1:
            return [-1, -1]

        l2 = 0
        r2 = len(nums) - 1

        last_occ = -1

        # Find last occurrence
        while l2 <= r2:
            mid = (l2 + r2) // 2

            if nums[mid] <= target:
                if nums[mid] == target:
                    last_occ = mid
                l2 = mid + 1
            else:
                r2 = mid - 1

        return [first_occ, last_occ]


        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
