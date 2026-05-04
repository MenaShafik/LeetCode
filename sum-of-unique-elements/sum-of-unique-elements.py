# ==========================================================
# Problem    : Sum of Unique Elements
# URL        : https://leetcode.com/problems/sum-of-unique-elements/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Counting
#
# Acceptance : 79.9%
# Likes      : 1702  |  Dislikes: 35
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12324000  (beats 52.09309999999999%)
# Submitted  : 1777925368
# Exported   : 2026-05-04 20:12:01 UTC
#
# Hints: Use a dictionary to count the frequency of each number.
# ==========================================================
class Solution(object):
    def sumOfUnique(self, nums):
        unique_sum = 0
        for num in nums:
            if nums.count(num) == 1:
                unique_sum += num
        return unique_sum
        """
        :type nums: List[int]
        :rtype: int
        """
        
