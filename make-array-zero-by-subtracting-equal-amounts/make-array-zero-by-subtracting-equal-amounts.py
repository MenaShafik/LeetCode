# ==========================================================
# Problem    : Make Array Zero by Subtracting Equal Amounts
# URL        : https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Simulation
#
# Acceptance : 74.0%
# Likes      : 1347  |  Dislikes: 62
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12224000  (beats 58.41589999999999%)
# Submitted  : 1794083049
# Exported   : 2026-11-07 21:52:05 UTC
#
# Hints: It is always best to set x as the smallest non-zero element in nums.
#   Elements with the same value will always take the same number of operations to become 0. Contrarily, elements with different values will always take a different number of operations to become 0.
#   The answer is the number of unique non-zero numbers in nums.
# ==========================================================
class Solution(object):
    def minimumOperations(self, nums):
        counter = 0 
        for i in set(nums):
            if i > 0:
                i-=1
                counter+=1
        return counter
                
        """
        :type nums: List[int]
        :rtype: int
        """
        
