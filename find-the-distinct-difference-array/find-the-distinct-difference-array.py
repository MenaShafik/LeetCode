# ==========================================================
# Problem    : Find the Distinct Difference Array
# URL        : https://leetcode.com/problems/find-the-distinct-difference-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table
#
# Acceptance : 73.7%
# Likes      : 384  |  Dislikes: 39
#
# Language   : python
# Runtime    : 19  (beats 80.34190000000002%)
# Memory     : 12260000  (beats 53.8462%)
# Submitted  : 1793608785
# Exported   : 2026-11-02 12:43:02 UTC
#
# Hints: Which data structure will help you maintain distinct elements?
#   Iterate over all possible prefix sizes. Then, use a nested loop to add the elements of the prefix to a set, and another nested loop to add the elements of the suffix to another set.
# ==========================================================
class Solution(object):
    def distinctDifferenceArray(self, nums):
        stack = []
        for i in range(len(nums)):
            left = set(nums[:i+1])
            right = set(nums[i+1:])
            stack.append(len(left) - len(right))
        return stack

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
