# ==========================================================
# Problem    : Check if Array Is Sorted and Rotated
# URL        : https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array
#
# Acceptance : 57.3%
# Likes      : 5166  |  Dislikes: 296
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12356000  (beats 52.133100000000006%)
# Submitted  : 1779558839
# Exported   : 2026-05-24 08:28:46 UTC
#
# Hints: Brute force and check if it is possible for a sorted array to start from each position.
# ==========================================================
class Solution(object):
    def check(self, nums):
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1

        return count <= 1
        """
        :type nums: List[int]
        :rtype: bool
        """
        
