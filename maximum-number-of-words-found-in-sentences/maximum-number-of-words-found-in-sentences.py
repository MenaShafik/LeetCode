# ==========================================================
# Problem    : Maximum Number of Words Found in Sentences
# URL        : https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, String
#
# Acceptance : 86.7%
# Likes      : 1910  |  Dislikes: 67
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12452000  (beats 25.207100000000004%)
# Submitted  : 1780566398
# Exported   : 2026-06-04 10:09:51 UTC
#
# Hints: Process each sentence separately and count the number of words by looking for the number of space characters in the sentence and adding it by 1.
# ==========================================================
class Solution(object):
    def mostWordsFound(self, sentences):
        max_words = 0

        for sentence in sentences:
            words = sentence.split()
            max_words = max(max_words, len(words))

        return max_words
        """
        :type sentences: List[str]
        :rtype: int
        """
        
