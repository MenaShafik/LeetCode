# ==========================================================
# Problem    : Day of the Week
# URL        : https://leetcode.com/problems/day-of-the-week/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# Acceptance : 59.5%
# Likes      : 461  |  Dislikes: 2575
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12464000  (beats 14.102599999999995%)
# Submitted  : 1786349526
# Exported   : 2026-08-10 21:17:50 UTC
#
# Hints: Sum up the number of days for the years before the given year.
#   Handle the case of a leap year.
#   Find the number of days for each month of the given year.
# ==========================================================
class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        import datetime

        x = datetime.datetime(year, month, day)
        return x.strftime("%A")

        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        
