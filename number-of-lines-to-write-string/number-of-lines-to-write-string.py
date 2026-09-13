# ==========================================================
# Problem    : Number of Lines To Write String
# URL        : https://leetcode.com/problems/number-of-lines-to-write-string/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, String
#
# Acceptance : 73.2%
# Likes      : 681  |  Dislikes: 1357
#
# Language   : python
# Runtime    : 14  (beats 82.15490000000001%)
# Memory     : 12380000  (beats 64.3098%)
# Submitted  : 1789287508
# Exported   : 2026-09-13 10:48:10 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def numberOfLines(self, widths, s):
        current_width = 0
        lines = 1
        for i in s:
            width = widths[ord(i)-ord('a')]
            if current_width + width > 100:
                lines+=1
                current_width = width
            else:

                current_width +=width
        return [lines, current_width]

        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        
