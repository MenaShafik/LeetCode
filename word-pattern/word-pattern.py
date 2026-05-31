# ==========================================================
# Problem    : Word Pattern
# URL        : https://leetcode.com/problems/word-pattern/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String
#
# Acceptance : 44.1%
# Likes      : 8010  |  Dislikes: 1149
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12396000  (beats 56.59759999999999%)
# Submitted  : 1780217437
# Exported   : 2026-05-31 09:45:58 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def wordPattern(self, pattern, s):
        s = s.split()
        if len(pattern) != len(s):
            return False
        char_to_word = {}
        word_to_char = {}
        for char, word in zip(pattern, s):
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
        return True
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
