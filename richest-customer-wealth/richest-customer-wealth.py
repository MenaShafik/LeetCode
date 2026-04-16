# ================================================================
# Problem : Richest Customer Wealth
# URL     : https://leetcode.com/problems/richest-customer-wealth/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Matrix
#
# --- Community Stats ---
# Acceptance Rate : 88.7%
# Likes           : 4888
# Dislikes        : 390
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12240000  (beats 94.61189999999999%)
# Submitted  : 1774984951
#
# --- Hints ---
# Calculate the wealth of each customer
# Find the maximum element in array.
# ================================================================

class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0
        for customer in accounts:
            wealth = sum(customer)
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth

        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
