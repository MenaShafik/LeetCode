# ==========================================================
# Problem    : Smallest Missing Multiple of K
# URL        : https://leetcode.com/problems/smallest-missing-multiple-of-k/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table
#
# Acceptance : 71.4%
# Likes      : 336  |  Dislikes: 15
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12292000  (beats 86.3636%)
# Submitted  : 1787649455
# Exported   : 2026-08-25 21:27:34 UTC
#
# Hints: Add the values in <code>nums</code> to a hash set
#   Iterate through the positive multiples of <code>k</code> and return the first one not in the hash set
# ==========================================================
class Solution(object):
    def missingMultiple(self, nums, k):
        mult = k
        while mult in nums:
            mult+= k
        return mult
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
