# ==========================================================
# Problem    : Single Number II
# URL        : https://leetcode.com/problems/single-number-ii/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Array, Bit Manipulation
#
# Acceptance : 67.8%
# Likes      : 8811  |  Dislikes: 754
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 14136000  (beats 16.83519999999998%)
# Submitted  : 1788940753
# Exported   : 2026-09-09 12:46:56 UTC
#
# Hints: N/A
# ==========================================================
from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        count = Counter(nums)
        for i in nums:
            if count[i] ==1:
                return i
        """
        :type nums: List[int]
        :rtype: int
        """
        
