# ==========================================================
# Problem    : Keep Multiplying Found Values by Two
# URL        : https://leetcode.com/problems/keep-multiplying-found-values-by-two/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Sorting, Simulation
#
# Acceptance : 75.0%
# Likes      : 1068  |  Dislikes: 54
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12564000  (beats 28.96049999999999%)
# Submitted  : 1779102998
# Exported   : 2026-05-18 11:18:41 UTC
#
# Hints: Repeatedly iterate through the array and check if the current value of original is in the array.
#   If original is not found, stop and return its current value.
#   Otherwise, multiply original by 2 and repeat the process.
#   Use set data structure to check the existence faster.
# ==========================================================
class Solution(object):
    def findFinalValue(self, nums, original):
        while original in nums:
            original *= 2
        return original
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        
