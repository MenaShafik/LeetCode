# ==========================================================
# Problem    : Single Number III
# URL        : https://leetcode.com/problems/single-number-iii/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Array, Bit Manipulation
#
# Acceptance : 70.1%
# Likes      : 6924  |  Dislikes: 280
#
# Language   : python
# Runtime    : 3  (beats 63.93860000000001%)
# Memory     : 14216000  (beats 16.112600000000022%)
# Submitted  : 1789979290
# Exported   : 2026-09-22 10:13:23 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def singleNumber(self, nums):
        counter = {}
        stack = []
        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        for i in nums:
            if counter[i]==1:
                stack.append(i)
        return stack
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
