# ==========================================================
# Problem    : Make Two Arrays Equal by Reversing Subarrays
# URL        : https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Sorting
#
# Acceptance : 75.9%
# Likes      : 1537  |  Dislikes: 164
#
# Language   : python
# Runtime    : 1  (beats 97.5758%)
# Memory     : 12300000  (beats 82.4242%)
# Submitted  : 1795787729
# Exported   : 2026-11-28 14:05:07 UTC
#
# Hints: Each element of target should have a corresponding element in arr, and if it doesn't have a corresponding element, return false.
#   To solve it easiely you can sort the two arrays and check if they are equal.
# ==========================================================
class Solution(object):
    def canBeEqual(self, target, arr):
        target.sort()
        arr.sort()
        return arr == target
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        
