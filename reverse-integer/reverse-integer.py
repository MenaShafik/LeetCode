# ================================================================
# Problem : Reverse Integer
# URL     : https://leetcode.com/problems/reverse-integer/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Math
#
# --- Community Stats ---
# Acceptance Rate : 31.8%
# Likes           : 15530
# Dislikes        : 14007
#
# --- My Submission ---
# Language   : python
# Runtime    : 15  (beats 76.35959999999999%)
# Memory     : 12368000  (beats 58.4491%)
# Submitted  : 1776015354
#
# --- Hints ---
# N/A
# ================================================================

class Solution(object):
    def reverse(self, x):
        st = str(x)
        test = []
        
        for i in st:
            if i != "-" and i != "+":
                test.append(i)
        
        rev = ""
        for i in range(len(test)-1, -1, -1):
            rev += test[i]
        
        if x < 0:
            rev = "-" + rev
        
        result = int(rev)
        
        if result < -2**31 or result > 2**31 - 1:
            return 0
        
        return result
