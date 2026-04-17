# ================================================================
# Problem : Reverse Integer
# URL     : https://leetcode.com/problems/reverse-integer/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Math
#
# --- Community Stats ---
# Acceptance Rate : 31.8%
# Likes           : 15532
# Dislikes        : 14008
#
# --- My Submission ---
# Language   : python
# Runtime    : 15  (beats 76.42039999999997%)
# Memory     : 12368000  (beats 57.437999999999995%)
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
