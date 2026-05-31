# ==========================================================
# Problem    : Majority Element
# URL        : https://leetcode.com/problems/majority-element/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Divide and Conquer, Sorting, Counting
#
# Acceptance : 66.3%
# Likes      : 22872  |  Dislikes: 829
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 13576000  (beats 73.7393%)
# Submitted  : 1780217227
# Exported   : 2026-05-31 09:46:00 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
        """
        :type nums: List[int]
        :rtype: int
        """
        
