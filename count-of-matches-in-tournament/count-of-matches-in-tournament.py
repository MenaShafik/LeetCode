# ================================================================
# Problem : Count of Matches in Tournament
# URL     : https://leetcode.com/problems/count-of-matches-in-tournament/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Simulation
#
# --- Community Stats ---
# Acceptance Rate : 86.4%
# Likes           : 1885
# Dislikes        : 248
#
# --- My Submission ---
# Language   : python
# Runtime    : 7  (beats 97.8166%)
# Memory     : 12328000  (beats 56.7686%)
# Submitted  : 1776116619
#
# --- Hints ---
# Simulate the tournament as given in the statement.
# Be careful when handling odd integers.
# ================================================================

class Solution(object):
    def numberOfMatches(self, n):
        matches = 0
        while n > 1:
            if n % 2 == 0:
                matches+= n // 2
                n = n // 2
            else:
                matches+= (n - 1) // 2
                n = (n - 1) // 2 + 1 
        return matches
    
        """
        :type n: int
        :rtype: int
        """
        
