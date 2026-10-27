# ==========================================================
# Problem    : Divide Array Into Equal Pairs
# URL        : https://leetcode.com/problems/divide-array-into-equal-pairs/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Bit Manipulation, Counting
#
# Acceptance : 79.3%
# Likes      : 1224  |  Dislikes: 51
#
# Language   : python
# Runtime    : 1  (beats 94.4828%)
# Memory     : 12464000  (beats 61.3792%)
# Submitted  : 1793085808
# Exported   : 2026-10-27 10:58:06 UTC
#
# Hints: For any number x in the range [1, 500], count the number of elements in nums whose values are equal to x.
#   The elements with equal value can be divided completely into pairs if and only if their count is even.
# ==========================================================
class Solution(object):
    def divideArray(self, nums):
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        for v in count.values():
            if v % 2 == 1:
                return False
        return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        
