# ==========================================================
# Problem    : Number of Segments in a String
# URL        : https://leetcode.com/problems/number-of-segments-in-a-string/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 37.4%
# Likes      : 923  |  Dislikes: 1344
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12316000  (beats 51.243199999999995%)
# Submitted  : 1782982395
# Exported   : 2026-07-02 09:24:15 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def countSegments(self, s):
        array = s.split()
        return len(array)
            
        """
        :type s: str
        :rtype: int
        """
        
