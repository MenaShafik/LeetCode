# ==========================================================
# Problem    : Removing Minimum and Maximum From Array
# URL        : https://leetcode.com/problems/removing-minimum-and-maximum-from-array/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Array, Greedy
#
# Acceptance : 67.1%
# Likes      : 1351  |  Dislikes: 66
#
# Language   : python
# Runtime    : 23  (beats 81.6328%)
# Memory     : 20420000  (beats 83.6735%)
# Submitted  : 1788079199
# Exported   : 2026-08-30 19:04:30 UTC
#
# Hints: There can only be three scenarios for deletions such that both minimum and maximum elements are removed:
#   Scenario 1: Both elements are removed by only deleting from the front.
#   Scenario 2: Both elements are removed by only deleting from the back.
#   Scenario 3: Delete from the front to remove one of the elements, and delete from the back to remove the other element.
#   Compare which of the three scenarios results in the minimum number of moves.
# ==========================================================
class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)
        if n == 1:
            return 1
        maxi = nums.index(max(nums))
        mini = nums.index(min(nums))
        left = max(maxi, mini)+1
        right = n - min(maxi,mini)
        mixed = min(maxi,mini) +1 + n - max(maxi,mini)
        return min(left, right, mixed)
        """
        :type nums: List[int]
        :rtype: int
        """
        
