# ================================================================
# Problem : Convert the Temperature
# URL     : https://leetcode.com/problems/convert-the-temperature/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# --- Community Stats ---
# Acceptance Rate : 90.3%
# Likes           : 757
# Dislikes        : 370
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12268000  (beats 93.4322%)
# Submitted  : 1774382776
#
# --- Hints ---
# Implement formulas that are given in the statement.
# ================================================================

class Solution(object):
    def convertTemperature(self, celsius):
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        return [Kelvin,Fahrenheit]
        """
        :type celsius: float
        :rtype: List[float]
        """
        
