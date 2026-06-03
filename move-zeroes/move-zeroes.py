# ==========================================================
# Problem    : Move Zeroes
# URL        : https://leetcode.com/problems/move-zeroes/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Two Pointers
#
# Acceptance : 63.9%
# Likes      : 19562  |  Dislikes: 608
#
# Language   : python
# Runtime    : 789  (beats 5.047400000000026%)
# Memory     : 13176000  (beats 99.89959999999999%)
# Submitted  : 1780478940
# Exported   : 2026-06-03 09:37:58 UTC
#
# Hints: <b>In-place</b> means we should not be allocating any space for extra array. But we are allowed to modify the existing array. However, as a first step, try coming up with a solution that makes use of additional space. For this problem as well, first apply the idea discussed using an additional array and the in-place solution will pop up eventually.
#   A <b>two-pointer</b> approach could be helpful here. The idea would be to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array.
# ==========================================================
class Solution(object):
    def moveZeroes(self, nums):
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(0)
        return nums

        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
