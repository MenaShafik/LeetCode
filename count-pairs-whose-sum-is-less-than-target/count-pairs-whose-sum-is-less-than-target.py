# ================================================================
# Problem : Count Pairs Whose Sum is Less than Target
# URL     : https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Two Pointers, Binary Search, Sorting
#
# --- Community Stats ---
# Acceptance Rate : 87.7%
# Likes           : 842
# Dislikes        : 90
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12292000  (beats 93.2143%)
# Submitted  : 1775591306
#
# --- Hints ---
# The constraints are small enough for a brute-force solution to pass
# ================================================================

class Solution(object):
    def countPairs(self, nums, target):
        result = 0 
        n= len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] < target:
                    result+=1
        return result
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
