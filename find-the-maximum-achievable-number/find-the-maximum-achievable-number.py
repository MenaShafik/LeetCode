# ==========================================================
# Problem    : Find the Maximum Achievable Number
# URL        : https://leetcode.com/problems/find-the-maximum-achievable-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# Acceptance : 91.3%
# Likes      : 526  |  Dislikes: 777
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12316000  (beats 53.347799999999985%)
# Submitted  : 1778323955
# Exported   : 2026-05-09 10:53:42 UTC
#
# Hints: Let x be the answer, it’s always optimal to decrease x in each operation and increase nums.
# ==========================================================
class Solution(object):
    def theMaximumAchievableX(self, num, t):
        return num +2 *t
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        
