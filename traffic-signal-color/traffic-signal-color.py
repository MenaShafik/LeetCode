# ==========================================================
# Problem    : Traffic Signal Color
# URL        : https://leetcode.com/problems/traffic-signal-color/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : N/A
#
# Acceptance : 82.8%
# Likes      : 26  |  Dislikes: 5
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12384000  (beats 55.9347%)
# Submitted  : 1776718428
# Exported   : 2026-04-20 21:17:41 UTC
#
# Hints: Simulate as described
# ==========================================================
class Solution(object):
    def trafficSignal(self, timer):
        if timer == 0:
            return "Green"
        elif timer == 30:
            return "Orange"
        elif timer >= 30 and timer <= 90:
            return "Red"
        else:
            return "Invalid"

        """
        :type timer: int
        :rtype: str
        """
        
