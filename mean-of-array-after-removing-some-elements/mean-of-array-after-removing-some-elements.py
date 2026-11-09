# ==========================================================
# Problem    : Mean of Array After Removing Some Elements
# URL        : https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Sorting
#
# Acceptance : 72.5%
# Likes      : 537  |  Dislikes: 134
#
# Language   : python
# Runtime    : 1  (beats 89.3333%)
# Memory     : 12312000  (beats 58.666700000000006%)
# Submitted  : 1794127618
# Exported   : 2026-11-09 17:42:07 UTC
#
# Hints: Sort the given array.
#   Remove the first and last 5% of the sorted array.
# ==========================================================
class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        fifth = len(arr) // 20
        arr = arr[fifth:-fifth]
        return sum(arr) / float(len(arr))
        
        """
        :type arr: List[int]
        :rtype: float
        """
        
