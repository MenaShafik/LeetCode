# ================================================================
# Problem : Find the Difference
# URL     : https://leetcode.com/problems/find-the-difference/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String, Bit Manipulation, Sorting
#
# --- Community Stats ---
# Acceptance Rate : 60.3%
# Likes           : 5494
# Dislikes        : 519
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12316000  (beats 73.0091%)
# Submitted  : 1773349119
#
# --- Hints ---
# N/A
# ================================================================

class Solution(object):
    def findTheDifference(self, s, t):
         for char in t:
            if s.count(char)!= t.count(char):
                return char

