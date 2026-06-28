# ==========================================================
# Problem    : Day of the Year
# URL        : https://leetcode.com/problems/day-of-the-year/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, String
#
# Acceptance : 50.2%
# Likes      : 515  |  Dislikes: 496
#
# Language   : python
# Runtime    : 7  (beats 99.095%)
# Memory     : 12288000  (beats 90.9502%)
# Submitted  : 1782638628
# Exported   : 2026-06-28 09:27:09 UTC
#
# Hints: Have a integer array of how many days there are per month.  February gets one extra day if its a leap year.  Then, we can manually count the ordinal as day + (number of days in months before this one).
# ==========================================================
class Solution(object):
     def is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
     def dayOfYear(self, date):
        year, month, day = map(int, date.split('-'))
        days_in_month = [31, 28 + self.is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(days_in_month[:month - 1]) + day
        """
        :type date: str
        :rtype: int
        """
        
