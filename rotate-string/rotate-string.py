# ==========================================================
# Problem    : Rotate String
# URL        : https://leetcode.com/problems/rotate-string/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String, String Matching
#
# Acceptance : 66.7%
# Likes      : 5004  |  Dislikes: 454
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12444000  (beats 15.311899999999994%)
# Submitted  : 1780391543
# Exported   : 2026-06-02 09:46:30 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        return goal in s + s
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        
