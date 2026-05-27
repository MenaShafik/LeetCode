# ==========================================================
# Problem    : Count the Number of Special Characters II
# URL        : https://leetcode.com/problems/count-the-number-of-special-characters-ii/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Hash Table, String
#
# Acceptance : 54.6%
# Likes      : 342  |  Dislikes: 18
#
# Language   : python
# Runtime    : 235  (beats 84.2104%)
# Memory     : 14844000  (beats 52.631600000000006%)
# Submitted  : 1779872746
# Exported   : 2026-05-27 09:07:25 UTC
#
# Hints: For each character <code>c</code>, store the first occurrence of its uppercase and the last occurrence of its lowercase.
# ==========================================================
class Solution(object):
    def numberOfSpecialChars(self, word):
        lower_pos = {}
        upper_pos = {}

        for i, ch in enumerate(word):
            if ch.islower():
                lower_pos[ch] = i
            else:
                if ch not in upper_pos:
                    upper_pos[ch] = i

        count = 0

        for ch in lower_pos:
            upper_ch = ch.upper()

            if upper_ch in upper_pos:
                if lower_pos[ch] < upper_pos[upper_ch]:
                    count += 1

        return count
        """
        :type word: str
        :rtype: int
        """
        
