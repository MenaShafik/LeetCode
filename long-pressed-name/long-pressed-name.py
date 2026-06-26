# ==========================================================
# Problem    : Long Pressed Name
# URL        : https://leetcode.com/problems/long-pressed-name/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Two Pointers, String
#
# Acceptance : 33.0%
# Likes      : 2611  |  Dislikes: 410
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12368000  (beats 56.63260000000001%)
# Submitted  : 1782473050
# Exported   : 2026-06-26 11:28:54 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def isLongPressedName(self, name, typed):
        i = 0
        j = 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
            j += 1
        return i == len(name)
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        
