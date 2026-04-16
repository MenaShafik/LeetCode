# ================================================================
# Problem : Reverse Degree of a String
# URL     : https://leetcode.com/problems/reverse-degree-of-a-string/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String, Simulation
#
# --- Community Stats ---
# Acceptance Rate : 88.7%
# Likes           : 86
# Dislikes        : 5
#
# --- My Submission ---
# Language   : python
# Runtime    : 6  (beats 91.9297%)
# Memory     : 12436000  (beats 30.1755%)
# Submitted  : 1775511279
#
# --- Hints ---
# Simulate the operations as described.
# ================================================================

class Solution(object):
    def reverseDegree(self, s):
        result = 0
        
        reversed_s = s[::-1]
        
        for i, ch in enumerate(s, 1):
            value = 26 - (ord(ch) - ord('a'))
            result += value * i
        
        return result
        """
        :type s: str
        :rtype: int
        """
        
