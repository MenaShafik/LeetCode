# ==========================================================
# Problem    : Subarrays Distinct Element Sum of Squares I
# URL        : https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Binary Indexed Tree, Segment Tree
#
# Acceptance : 85.2%
# Likes      : 311  |  Dislikes: 54
#
# Language   : python
# Runtime    : 26  (beats 93.33340000000001%)
# Memory     : 12176000  (beats 100.0%)
# Submitted  : 1792049608
# Exported   : 2026-10-15 08:20:41 UTC
#
# Hints: Use a set/heap to keep track of distinct element counts.
# ==========================================================
class Solution(object):
    def sumCounts(self, nums):
        counter = 0
        for i in range(len(nums)):
            s = set()
            for j in range(i,len(nums)):
                s.add(nums[j])
                counter+= len(s)**2
        return counter
        """
        :type nums: List[int]
        :rtype: int
        """
        
