# ==========================================================
# Problem    : Find the Highest Altitude
# URL        : https://leetcode.com/problems/find-the-highest-altitude/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Prefix Sum
#
# Acceptance : 84.6%
# Likes      : 3500  |  Dislikes: 444
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12452000  (beats 15.0959%)
# Submitted  : 1785057755
# Exported   : 2026-07-27 08:55:27 UTC
#
# Hints: Let's note that the altitude of an element is the sum of gains of all the elements behind it
#   Getting the altitudes can be done by getting the prefix sum array of the given array
# ==========================================================
class Solution(object):
    def largestAltitude(self, gain):
        current = 0
        highest = 0

        for g in gain:
            current += g
            highest = max(highest, current)

        return highest
        """
        :type gain: List[int]
        :rtype: int
        """
        
