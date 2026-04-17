# ================================================================
# Problem : Find Closest Person
# URL     : https://leetcode.com/problems/find-closest-person/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# --- Community Stats ---
# Acceptance Rate : 89.0%
# Likes           : 427
# Dislikes        : 47
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12260000  (beats 94.5205%)
# Submitted  : 1775680025
#
# --- Hints ---
# Compare the distances from Persons 1 and 2 to Person 3 to determine the answer.
# ================================================================

class Solution(object):
    def findClosest(self, x, y, z):
        
        xz = abs(x-z)
        yz = abs(y-z)
        if xz == yz:
            return 0
        elif yz > xz:
            return 1
        else:
            return 2
            
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        
