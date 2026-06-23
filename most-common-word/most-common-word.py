# ==========================================================
# Problem    : Most Common Word
# URL        : https://leetcode.com/problems/most-common-word/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, String, Counting
#
# Acceptance : 45.2%
# Likes      : 1867  |  Dislikes: 3119
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12392000  (beats 63.41939999999999%)
# Submitted  : 1782207290
# Exported   : 2026-06-23 09:45:10 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        import re
        words = re.findall(r'\w+', paragraph.lower())
        word_count = {}
        for word in words:
            if word not in banned:
                word_count[word] = word_count.get(word, 0) + 1
        return max(word_count, key=word_count.get)
            
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
