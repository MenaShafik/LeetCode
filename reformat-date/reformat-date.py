# ==========================================================
# Problem    : Reformat Date
# URL        : https://leetcode.com/problems/reformat-date/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 68.8%
# Likes      : 507  |  Dislikes: 441
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12272000  (beats 89.7436%)
# Submitted  : 1786350152
# Exported   : 2026-08-10 21:17:48 UTC
#
# Hints: Handle the conversions of day, month and year separately.
#   Notice that days always have a two-word ending, so if you erase the last two characters of this days you'll get the number.
# ==========================================================
class Solution(object):
    def reformatDate(self, date):
        day, month, year = date.split()
        day = day[:-2]
        months = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12"
            }
        return year + "-" + months[month] + "-" + day.zfill(2)
        """
        :type date: str
        :rtype: str
        """
        
