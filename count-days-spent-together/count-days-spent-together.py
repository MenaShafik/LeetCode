# ==========================================================
# Problem    : Count Days Spent Together
# URL        : https://leetcode.com/problems/count-days-spent-together/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, String
#
# Acceptance : 66.8%
# Likes      : 516  |  Dislikes: 615
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12128000  (beats 95.34880000000001%)
# Submitted  : 1792828449
# Exported   : 2026-10-25 12:08:07 UTC
#
# Hints: For a given day, determine if Alice or Bob or both are in Rome.
#   Brute force all 365 days for both Alice and Bob.
# ==========================================================
class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def date_to_day(date_str):
            month, day = map(int,date_str.split("-"))
            return sum(days[:month-1]) + day
        start = max(date_to_day(arriveAlice) , date_to_day(arriveBob))
        end = min(date_to_day(leaveAlice) ,date_to_day(leaveBob))
        return max(0,end - start +1)
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        
