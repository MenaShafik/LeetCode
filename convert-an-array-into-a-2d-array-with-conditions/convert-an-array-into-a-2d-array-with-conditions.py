# ==========================================================
# Problem    : Convert an Array Into a 2D Array With Conditions
# URL        : https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Array, Hash Table
#
# Acceptance : 86.2%
# Likes      : 1717  |  Dislikes: 82
#
# Language   : python
# Runtime    : 3  (beats 71.698%)
# Memory     : 12160000  (beats 81.13199999999999%)
# Submitted  : 1793368999
# Exported   : 2026-10-30 18:53:43 UTC
#
# Hints: Process the elements in the array one by one in any order and only create a new row in the matrix when we cannot put it into the existing rows
#   We can simply iterate over the existing rows of the matrix to see if we can place each element.
# ==========================================================
class Solution(object):
    def findMatrix(self, nums):
        stack = []
        while len(nums) > 0:
            unique = []
            set_nums = set(nums)
            for i in set(nums):
                unique.append(i)
                nums.remove(i)
            stack.append(unique)
        return stack
            
        
        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
