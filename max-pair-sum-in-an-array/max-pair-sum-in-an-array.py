# ==========================================================
# Problem    : Max Pair Sum in an Array
# URL        : https://leetcode.com/problems/max-pair-sum-in-an-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table
#
# Acceptance : 59.9%
# Likes      : 451  |  Dislikes: 140
#
# Language   : python
# Runtime    : 23  (beats 97.619%)
# Memory     : 12024000  (beats 83.33330000000001%)
# Submitted  : 1793258408
# Exported   : 2026-10-29 08:11:28 UTC
#
# Hints: Find the largest and second largest element with maximum digits equal to x where 1<=x<=9.
# ==========================================================
class Solution(object):
    def maxSum(self, nums):
        nums.sort(reverse=True)
        freq = {}
        counter = -1

        for i in nums:
            digit = max(str(i))

            if digit in freq:
                counter = max(counter, freq[digit] + i)
            else:
                freq[digit] = i

        return counter
        """
        :type nums: List[int]
        :rtype: int
        """
        
