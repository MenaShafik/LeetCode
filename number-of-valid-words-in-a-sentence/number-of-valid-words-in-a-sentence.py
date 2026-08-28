# ==========================================================
# Problem    : Number of Valid Words in a Sentence
# URL        : https://leetcode.com/problems/number-of-valid-words-in-a-sentence/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 31.4%
# Likes      : 360  |  Dislikes: 829
#
# Language   : python
# Runtime    : 13  (beats 60.377300000000005%)
# Memory     : 12416000  (beats 52.8302%)
# Submitted  : 1787946200
# Exported   : 2026-08-28 19:46:03 UTC
#
# Hints: Iterate through the string to split it by spaces.
#   Count the number of characters of each type (letters, numbers, hyphens, and punctuations).
# ==========================================================
class Solution(object):
    def countValidWords(self, sentence):
        counter = 0

        for word in sentence.split():

            # Check characters
            if any(char.isdigit() for char in word):
                continue

            # Check hyphen
            if word.count("-") > 1:
                continue

            # If there is a hyphen, it must be between letters
            if "-" in word:
                index = word.index("-")

                if index == 0 or index == len(word) - 1:
                    continue

                if not word[index - 1].isalpha() or not word[index + 1].isalpha():
                    continue

            # Punctuation must appear only at the end
            punctuation = "!,."
            if any(char in punctuation for char in word[:-1]):
                continue

            counter += 1

        return counter
        """
        :type sentence: str
        :rtype: int
        """
        
