# ================================================================
# Problem : Check Balanced String
# URL     : https://leetcode.com/problems/check-balanced-string/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# --- Community Stats ---
# Acceptance Rate : 82.6%
# Likes           : 143
# Dislikes        : 3
#
# --- My Submission ---
# Language   : python
# Runtime    : 2  (beats 95.0%)
# Memory     : 12200000  (beats 100.0%)
# Submitted  : 1776458988
#
# --- Hints ---
# N/A
# ================================================================

class Solution(object):
    def isBalanced(self, num):
        sum_balance_even = 0
        sum_balance_odd = 0
        for i in range(len(num)):
            if i % 2 == 0:
                sum_balance_even += int(num[i])
            else:
                sum_balance_odd += int(num[i])
        return sum_balance_even == sum_balance_odd
        """
        :type num: str
        :rtype: bool
        """
        
