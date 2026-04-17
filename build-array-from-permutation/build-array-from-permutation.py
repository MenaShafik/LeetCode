# ================================================================
# Problem : Build Array from Permutation
# URL     : https://leetcode.com/problems/build-array-from-permutation/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Simulation
#
# --- Community Stats ---
# Acceptance Rate : 91.1%
# Likes           : 4044
# Dislikes        : 494
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12596000  (beats 79.5896%)
# Submitted  : 1774984042
#
# --- Hints ---
# Just apply what's said in the statement.
# Notice that you can't apply it on the same array directly since some elements will change after application
# ================================================================

class Solution(object):
    def buildArray(self, nums):
        answer = []
        for i in nums:
            answer.append(nums[i])
        return answer
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
