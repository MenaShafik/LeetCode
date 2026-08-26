# ==========================================================
# Problem    : Number of Days Between Two Dates
# URL        : https://leetcode.com/problems/number-of-days-between-two-dates/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, String
#
# Acceptance : 53.4%
# Likes      : 444  |  Dislikes: 1327
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12580000  (beats 20.300600000000014%)
# Submitted  : 1787734208
# Exported   : 2026-08-26 18:20:58 UTC
#
# Hints: Create a function f(date) that counts the number of days from 1900-01-01 to date. How can we calculate the answer ?
#   The answer is just |f(date1) - f(date2)|.
#   How to construct f(date) ?
#   For each year from 1900 to year - 1 sum up 365 or 366 in case of leap years. Then sum up for each month the number of days, consider the case when the current year is leap, finally sum up the days.
# ==========================================================
class Solution(object):
    def daysBetweenDates(self, date1, date2):
        from datetime import datetime

        date1 = datetime.strptime(date1, "%Y-%m-%d")
        date2 = datetime.strptime(date2, "%Y-%m-%d")
        return abs(date2-date1).days

        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        
