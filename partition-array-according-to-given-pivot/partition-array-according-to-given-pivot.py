# ==========================================================
# Problem    : Partition Array According to Given Pivot
# URL        : https://leetcode.com/problems/partition-array-according-to-given-pivot/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Array, Two Pointers, Simulation
#
# Acceptance : 90.8%
# Likes      : 1988  |  Dislikes: 134
#
# Language   : python
# Runtime    : 47  (beats 97.72359999999999%)
# Memory     : 29532000  (beats 34.0763%)
# Submitted  : 1784712789
# Exported   : 2026-07-22 09:51:24 UTC
#
# Hints: Could you put the elements smaller than the pivot and greater than the pivot in a separate list as in the sequence that they occur?
#   With the separate lists generated, could you then generate the result?
# ==========================================================
class Solution(object):
    def pivotArray(self, nums, pivot):
        less = []
        greater = []
        c= 0
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                c+=1
        return less + [pivot]*c + greater
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        
