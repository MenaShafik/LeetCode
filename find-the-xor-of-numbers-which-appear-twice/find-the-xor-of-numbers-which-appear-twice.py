# ==========================================================
# Problem    : Find the XOR of Numbers Which Appear Twice
# URL        : https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Bit Manipulation
#
# Acceptance : 79.0%
# Likes      : 187  |  Dislikes: 15
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12428000  (beats 20.6451%)
# Submitted  : 1791357998
# Exported   : 2026-10-07 12:14:42 UTC
#
# Hints: The constraints are small. Brute force checking each value in the array.
# ==========================================================
class Solution(object):
    def duplicateNumbersXOR(self, nums):
        counter = 0
        for i in set(nums):
            if nums.count(i) > 1:
                counter ^= i
            
        return counter
        """
        :type nums: List[int]
        :rtype: int
        """
        
