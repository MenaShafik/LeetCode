# ================================================================
# Problem : Add Digits
# URL     : https://leetcode.com/problems/add-digits/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Simulation, Number Theory
#
# --- Community Stats ---
# Acceptance Rate : 68.8%
# Likes           : 5523
# Dislikes        : 1985
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12308000  (beats 61.06259999999999%)
# Submitted  : 1774129095
#
# --- Hints ---
# A naive implementation of the above process is trivial. Could you come up with other methods?
# What are all the possible results?
# How do they occur, periodically or randomly?
# You may find this <a href="https://en.wikipedia.org/wiki/Digital_root" target="_blank">Wikipedia article</a> useful.
# ================================================================

class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0;
        return 1 + (num - 1)%9

        """
        :type num: int
        :rtype: int
        """
        
