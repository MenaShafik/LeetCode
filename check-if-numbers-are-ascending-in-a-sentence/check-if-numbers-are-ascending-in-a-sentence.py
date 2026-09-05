# ==========================================================
# Problem    : Check if Numbers Are Ascending in a Sentence
# URL        : https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 73.7%
# Likes      : 714  |  Dislikes: 26
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12468000  (beats 18.120900000000013%)
# Submitted  : 1788639644
# Exported   : 2026-09-05 20:25:11 UTC
#
# Hints: Use string tokenization of your language to extract all the tokens of the string easily.
#   For each token extracted, how can you tell if it is a number? Does the first letter being a digit mean something?
#   Compare the number with the previously occurring number to check if ascending order is maintained.
# ==========================================================
class Solution(object):
    def areNumbersAscending(self, s):
        numbers = []

        for word in s.split():
            if word.isdigit():
                numbers.append(int(word))
        if not numbers:
            return False

        for i in range(len(numbers)-1):
            if numbers[i] >= numbers[i+1]:
                return False
        return True

        """
        :type s: str
        :rtype: bool
        """
        
