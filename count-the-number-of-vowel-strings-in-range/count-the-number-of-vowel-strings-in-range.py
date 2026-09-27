# ==========================================================
# Problem    : Count the Number of Vowel Strings in Range
# URL        : https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, String, Counting
#
# Acceptance : 74.1%
# Likes      : 389  |  Dislikes: 33
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12392000  (beats 85.1351%)
# Submitted  : 1790497561
# Exported   : 2026-09-27 11:58:21 UTC
#
# Hints: consider iterating over all strings from left to right and use an if condition to check if the first character and last character are vowels.
# ==========================================================
class Solution(object):
    def vowelStrings(self, words, left, right):
        counter =0
        vowel = "aeiou"
        for i in range(left,right+1):
                if words[i][0] in vowel and words[i][-1] in vowel:
                    counter+=1
        return counter
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        
