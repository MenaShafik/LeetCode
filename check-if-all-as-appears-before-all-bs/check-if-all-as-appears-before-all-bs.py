# ==========================================================
# Problem    : Check if All A's Appears Before All B's
# URL        : https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 78.3%
# Likes      : 1045  |  Dislikes: 27
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12080000  (beats 82.60860000000001%)
# Submitted  : 1795335399
# Exported   : 2026-11-23 11:31:46 UTC
#
# Hints: You can check the opposite: check if there is a ‘b’ before an ‘a’. Then, negate and return that answer.
#   s should not have any occurrences of “ba” as a substring.
# ==========================================================
class Solution(object):
    def checkString(self, s):
        return "ba" not in s

        """
        :type s: str
        :rtype: bool
        """
        
