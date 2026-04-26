# ==========================================================
# Problem    : Sorting the Sentence
# URL        : https://leetcode.com/problems/sorting-the-sentence/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String, Sorting
#
# Acceptance : 84.1%
# Likes      : 2398  |  Dislikes: 83
#
# Language   : python
# Runtime    : 3  (beats 100.0%)
# Memory     : 12440000  (beats 20.588299999999997%)
# Submitted  : 1777237498
# Exported   : 2026-04-26 21:06:15 UTC
#
# Hints: Divide the string into the words as an array of strings
#   Sort the words by removing the last character from each word and sorting according to it
# ==========================================================
class Solution(object):
    def sortSentence(self, s):
        words = s.split()
        result = [""] * len(words)
        for i in words:
            position = int(i[-1])
            result[position - 1] = i[:-1]
        return " ".join(result)
            
        
        """
        :type s: str
        :rtype: str
        """
        
