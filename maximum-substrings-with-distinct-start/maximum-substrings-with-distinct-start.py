# ==========================================================
# Problem    : Maximum Substrings With Distinct Start
# URL        : https://leetcode.com/problems/maximum-substrings-with-distinct-start/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Hash Table, String
#
# Acceptance : 91.4%
# Likes      : 81  |  Dislikes: 16
#
# Language   : python
# Runtime    : 19  (beats 96.96970000000002%)
# Memory     : 13028000  (beats 17.17170000000001%)
# Submitted  : 1778494899
# Exported   : 2026-05-11 10:35:40 UTC
#
# Hints: Count the number of distinct characters in <code>s</code>
# ==========================================================
class Solution(object):
    def maxDistinct(self, s):
        return len(set(s))
        """
        :type s: str
        :rtype: int
        """
        
