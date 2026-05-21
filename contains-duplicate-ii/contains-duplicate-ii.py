# ==========================================================
# Problem    : Contains Duplicate II
# URL        : https://leetcode.com/problems/contains-duplicate-ii/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Sliding Window
#
# Acceptance : 51.3%
# Likes      : 7548  |  Dislikes: 3329
#
# Language   : python
# Runtime    : 23  (beats 98.2031%)
# Memory     : 23956000  (beats 72.00320000000004%)
# Submitted  : 1779309559
# Exported   : 2026-05-21 09:16:07 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True

            seen[num] = i

        return False

        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
