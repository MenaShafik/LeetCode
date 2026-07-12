# ==========================================================
# Problem    : Rank Transform of an Array
# URL        : https://leetcode.com/problems/rank-transform-of-an-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Sorting
#
# Acceptance : 72.3%
# Likes      : 2510  |  Dislikes: 120
#
# Language   : python
# Runtime    : 39  (beats 96.2963%)
# Memory     : 27964000  (beats 77.36639999999998%)
# Submitted  : 1783848660
# Exported   : 2026-07-12 09:48:47 UTC
#
# Hints: Use a temporary array to copy the array and sort it.
#   The rank of each element is the number of unique elements smaller than it in the sorted array plus one.
# ==========================================================
class Solution(object):
    def arrayRankTransform(self, arr):
        stack = sorted(set(arr))
        rank = {num: i+1 for i, num in enumerate(stack)}
        return [rank[num] for num in arr]

        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
