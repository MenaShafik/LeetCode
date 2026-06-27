# ==========================================================
# Problem    : Student Attendance Record I
# URL        : https://leetcode.com/problems/student-attendance-record-i/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 50.3%
# Likes      : 869  |  Dislikes: 57
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12284000  (beats 90.0%)
# Submitted  : 1782555583
# Exported   : 2026-06-27 10:28:21 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def checkRecord(self, s):
        absent=0
        late  = 0

        for char in s:
            if char == "A":
                absent+= 1
                late = 0
            elif char == "L":
                late+=1
                if late > 2:
                    return False
            else:
                late = 0
            if absent > 1:
                return False
        return True
        """
        :type s: str
        :rtype: bool
        """
        
