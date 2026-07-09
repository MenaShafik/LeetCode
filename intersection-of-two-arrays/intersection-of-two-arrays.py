# ==========================================================
# Problem    : Intersection of Two Arrays
# URL        : https://leetcode.com/problems/intersection-of-two-arrays/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Two Pointers, Binary Search, Sorting
#
# Acceptance : 78.0%
# Likes      : 6997  |  Dislikes: 2350
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12600000  (beats 28.68050000000001%)
# Submitted  : 1783607587
# Exported   : 2026-07-09 15:04:15 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
