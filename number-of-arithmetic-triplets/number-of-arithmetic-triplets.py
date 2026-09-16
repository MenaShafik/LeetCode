# ==========================================================
# Problem    : Number of Arithmetic Triplets
# URL        : https://leetcode.com/problems/number-of-arithmetic-triplets/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Two Pointers, Enumeration
#
# Acceptance : 85.6%
# Likes      : 1411  |  Dislikes: 98
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12268000  (beats 93.90240000000001%)
# Submitted  : 1789547947
# Exported   : 2026-09-16 09:00:45 UTC
#
# Hints: Are the constraints small enough for brute force?
#   We can use three loops, each iterating through the array to go through every possible triplet. Be sure to not count duplicates.
# ==========================================================
class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        counter = 0
        sets = set(nums)
        for i in sets:
            if i+diff in sets and i+(2*diff) in sets:
                counter+=1
        return counter
        
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        
