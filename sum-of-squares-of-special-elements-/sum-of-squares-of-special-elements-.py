# ==========================================================
# Problem    : Sum of Squares of Special Elements 
# URL        : https://leetcode.com/problems/sum-of-squares-of-special-elements/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Enumeration
#
# Acceptance : 82.1%
# Likes      : 323  |  Dislikes: 141
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12268000  (beats 89.0411%)
# Submitted  : 1779179750
# Exported   : 2026-05-19 10:48:49 UTC
#
# Hints: Iterate over all the elements of the array. For each index i, check if it is special using the modulo operator.
#   if n%i == 0, index i is special and you should add nums[i] to the answer.
# ==========================================================
class Solution(object):
    def sumOfSquares(self, nums):
        count = 0
        n = len(nums)
        for i in range(1, n+1):
            if n % i == 0:
                count+= nums[i - 1] ** 2
        return count
        """
        :type nums: List[int]
        :rtype: int
        """
        
