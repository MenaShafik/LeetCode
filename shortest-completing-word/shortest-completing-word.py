# ==========================================================
# Problem    : Shortest Completing Word
# URL        : https://leetcode.com/problems/shortest-completing-word/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, String
#
# Acceptance : 64.1%
# Likes      : 647  |  Dislikes: 1135
#
# Language   : python
# Runtime    : 7  (beats 95.09799999999998%)
# Memory     : 12340000  (beats 73.0392%)
# Submitted  : 1794473782
# Exported   : 2026-11-12 09:17:30 UTC
#
# Hints: Count only the letters (possibly converted to lowercase) of each word.  If a word is shorter and the count of each letter is at least the count of that letter in the licensePlate, it is the best answer we've seen yet.
# ==========================================================
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        letters = []

        for ch in licensePlate.lower():
            if ch.isalpha():
                letters.append(ch)

        for word in sorted(words, key=len):
            temp = list(word.lower())

            for ch in letters:
                if ch in temp:
                    temp.remove(ch)
                else:
                    break
            else:
                return word 
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        
