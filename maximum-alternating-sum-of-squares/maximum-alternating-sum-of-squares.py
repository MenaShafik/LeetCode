# ==========================================================
# Problem    : Maximum Alternating Sum of Squares
# URL        : https://leetcode.com/problems/maximum-alternating-sum-of-squares/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Array, Greedy, Sorting
#
# Acceptance : 75.6%
# Likes      : 331  |  Dislikes: 10
#
# Language   : python
# Runtime    : 243  (beats 73.33319999999998%)
# Memory     : 23516000  (beats 39.99979999999999%)
# Submitted  : 1791880405
# Exported   : 2026-10-13 21:06:57 UTC
#
# Hints: The score uses squares of values. The original signs of <code>nums</code> don't affect the squared terms.
#   In the alternating sum, even indices contribute positively and odd indices negatively.
# ==========================================================
class Solution(object):
    def maxAlternatingSum(self, nums):
        square = sorted([x*x for x in nums])
        n = len(nums)
        negative_count = n //2
        more = 0
        less = 0

        for i in range(negative_count):
            less+= square[i]
        for i in range(negative_count,n):
            more+= square[i]

        return (more - less)
        """
        :type nums: List[int]
        :rtype: int
        """
        
