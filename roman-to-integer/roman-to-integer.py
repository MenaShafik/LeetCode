# ================================================================
# Problem : Roman to Integer
# URL     : https://leetcode.com/problems/roman-to-integer/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, Math, String
#
# --- Community Stats ---
# Acceptance Rate : 66.5%
# Likes           : 17733
# Dislikes        : 1242
#
# --- My Submission ---
# Language   : python
# Runtime    : 6  (beats 77.7372%)
# Memory     : 12508000  (beats 5.989300000000011%)
# Submitted  : 1769634048
#
# --- Hints ---
# Problem is simpler to solve by working the string from back to front and using a map.
# ================================================================

class Solution(object):
    def romanToInt(self, s):
        roman = {

            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        total = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                total-= roman[s[i]]
            else:
                total+= roman[s[i]]
        return total + roman[s[-1]]
        """
        :type s: str
        :rtype: int
        """
        
