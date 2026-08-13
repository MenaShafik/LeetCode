# ==========================================================
# Problem    : Merge Sorted Array
# URL        : https://leetcode.com/problems/merge-sorted-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Two Pointers, Sorting
#
# Acceptance : 55.5%
# Likes      : 19395  |  Dislikes: 2675
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12360000  (beats 57.1876%)
# Submitted  : 1786653001
# Exported   : 2026-08-13 20:32:09 UTC
#
# Hints: You can easily solve this problem if you simply think about two elements at a time rather than two arrays. We know that each of the individual arrays is sorted. What we don't know is how they will intertwine. Can we take a local decision and arrive at an optimal solution?
#   If you simply consider one element each at a time from the two arrays and make a decision and proceed accordingly, you will arrive at the optimal solution.
# ==========================================================
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = sorted(nums1[:m] + nums2[:n])

        
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
