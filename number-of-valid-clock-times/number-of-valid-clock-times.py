# ==========================================================
# Problem    : Number of Valid Clock Times
# URL        : https://leetcode.com/problems/number-of-valid-clock-times/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String, Enumeration
#
# Acceptance : 48.6%
# Likes      : 311  |  Dislikes: 250
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12092000  (beats 100.0%)
# Submitted  : 1794732402
# Exported   : 2026-11-15 10:00:58 UTC
#
# Hints: Brute force all possible clock times.
#   Checking if a clock time is valid can be done with Regex.
# ==========================================================
class Solution(object):
    def countTime(self, time):
        counter = 1

        if time[3] == '?':
            counter *= 6
        if time[4] == '?':
            counter *= 10

        if time[0] == '?' and time[1] == '?':
            counter *= 24
        elif time[0] == '?':
            counter *= 3 if time[1] < '4' else 2
        elif time[1] == '?':
            counter *= 4 if time[0] == '2' else 10

        return counter

        """
        :type time: str
        :rtype: int
        """
        
