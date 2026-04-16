# ================================================================
# Problem : Find Minimum Operations to Make All Elements Divisible by Three
# URL     : https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math
#
# --- Community Stats ---
# Acceptance Rate : 90.9%
# Likes           : 521
# Dislikes        : 34
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12292000  (beats 88.9876%)
# Submitted  : 1775159726
#
# --- Hints ---
# If <code>x % 3 != 0</code> we can always increment or decrement <code>x</code> such that we only need 1 operation.
# Add <code>min(nums[i] % 3, 3 - (nums[i] % 3))</code> to the count of operations.
# ================================================================

class Solution(object):
    def minimumOperations(self, nums):
        res = 0
        for i in nums:
            if i % 3 != 0:
                res+=1
        return res
        """
        :type nums: List[int]
        :rtype: int
        """
        
