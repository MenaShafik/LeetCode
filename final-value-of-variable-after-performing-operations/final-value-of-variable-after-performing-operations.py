# ================================================================
# Problem : Final Value of Variable After Performing Operations
# URL     : https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, String, Simulation
#
# --- Community Stats ---
# Acceptance Rate : 90.6%
# Likes           : 2034
# Dislikes        : 217
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12264000  (beats 90.03460000000001%)
# Submitted  : 1774905446
#
# --- Hints ---
# There are only two operations to keep track of.
# Use a variable to store the value after each operation.
# ================================================================

class Solution(object):
    def finalValueAfterOperations(self, operations):
        result = 0
        for i in operations:
            if i == "--X" or i == "X--":
                result -=1
            elif i == "X++" or i == "++X":
                result +=1
        return result
        """
        :type operations: List[str]
        :rtype: int
        """
        
