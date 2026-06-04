# ==========================================================
# Problem    : Number of Good Pairs
# URL        : https://leetcode.com/problems/number-of-good-pairs/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Math, Counting
#
# Acceptance : 89.8%
# Likes      : 5885  |  Dislikes: 286
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12444000  (beats 16.253100000000003%)
# Submitted  : 1780565420
# Exported   : 2026-06-04 10:09:53 UTC
#
# Hints: Count how many times each number appears. If a number appears n times, then n * (n – 1) // 2 good pairs can be made with this number.
# ==========================================================
class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
        """
        :type nums: List[int]
        :rtype: int
        """
        
