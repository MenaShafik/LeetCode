# ==========================================================
# Problem    : Number of Elapsed Seconds Between Two Times
# URL        : https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, String
#
# Acceptance : 82.4%
# Likes      : 44  |  Dislikes: 3
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12540000  (beats 19.00970000000001%)
# Submitted  : 1788539278
# Exported   : 2026-09-05 20:25:15 UTC
#
# Hints: <p>Convert each time into the total number of seconds since <code>00:00:00</code>.</p>
#   <p>The answer is the difference between the two converted values.</p>
# ==========================================================
class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        split_start = startTime.split(":")
        split_end = endTime.split(":")

        start = int(split_start[0]) * 3600 + \
                int(split_start[1]) * 60 + \
                int(split_start[2])

        end = int(split_end[0]) * 3600 + \
              int(split_end[1]) * 60 + \
              int(split_end[2])

        return abs(end - start)
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        
