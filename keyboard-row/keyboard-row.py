# ==========================================================
# Problem    : Keyboard Row
# URL        : https://leetcode.com/problems/keyboard-row/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, String
#
# Acceptance : 74.0%
# Likes      : 1843  |  Dislikes: 1160
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12284000  (beats 91.1112%)
# Submitted  : 1782982906
# Exported   : 2026-07-02 09:24:13 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def findWords(self, words):
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        result = []
        for word in words:
            lower_word = set(word.lower())
            if lower_word <= first or lower_word <= second or lower_word <= third:
                result.append(word)
        return result

        """
        :type words: List[str]
        :rtype: List[str]
        """
        
