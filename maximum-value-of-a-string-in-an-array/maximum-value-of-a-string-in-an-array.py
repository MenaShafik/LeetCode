# ==========================================================
# Problem    : Maximum Value of a String in an Array
# URL        : https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, String
#
# Acceptance : 74.6%
# Likes      : 447  |  Dislikes: 25
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12156000  (beats 66.25%)
# Submitted  : 1795854104
# Exported   : 2026-11-28 14:05:04 UTC
#
# Hints: For strings comprising only of digits, convert them into integers.
#   For all other strings, calculate their length.
# ==========================================================
class Solution(object):
    def maximumValue(self, strs):
        return max(int(i) if i.isdigit() else len(i) for i in strs)
        """
        :type strs: List[str]
        :rtype: int
        """
        
