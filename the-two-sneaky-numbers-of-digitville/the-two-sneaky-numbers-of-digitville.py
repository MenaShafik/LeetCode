# ==========================================================
# Problem    : The Two Sneaky Numbers of Digitville
# URL        : https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Math
#
# Acceptance : 89.8%
# Likes      : 529  |  Dislikes: 22
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12328000  (beats 56.3475%)
# Submitted  : 1778668219
# Exported   : 2026-05-14 09:59:07 UTC
#
# Hints: To solve the problem without the extra space, we need to think about how many times each number occurs in relation to the index.
# ==========================================================
class Solution(object):
    def getSneakyNumbers(self, nums):
        seen = []
        res = []
        for i in nums:
            if i not in seen:
                seen.append(i)
            else:
                res.append(i)
        return res

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
