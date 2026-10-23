# ==========================================================
# Problem    : Calculate Delayed Arrival Time
# URL        : https://leetcode.com/problems/calculate-delayed-arrival-time/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# Acceptance : 75.5%
# Likes      : 310  |  Dislikes: 57
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 11872000  (beats 100.0%)
# Submitted  : 1792772921
# Exported   : 2026-10-23 22:05:04 UTC
#
# Hints: Use the modulo operator to handle the case when the arrival time plus the delayed time goes beyond 24 hours.
#   If the arrival time plus the delayed time is greater than or equal to 24, you can also subtract 24 to get the time in the 24-hour format.
# ==========================================================
class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        return (arrivalTime + delayedTime) % 24
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        
