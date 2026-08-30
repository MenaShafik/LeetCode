# ==========================================================
# Problem    : Number of Different Integers in a String
# URL        : https://leetcode.com/problems/number-of-different-integers-in-a-string/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String
#
# Acceptance : 40.6%
# Likes      : 668  |  Dislikes: 106
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12388000  (beats 61.3333%)
# Submitted  : 1788116434
# Exported   : 2026-08-30 19:04:29 UTC
#
# Hints: Try to split the string so that each integer is in a different string.
#   Try to remove each integer's leading zeroes and compare the strings to find how many of them are unique.
# ==========================================================
class Solution(object):
    def numDifferentIntegers(self, word):
        import re
        numbers = re.sub(r'\D+', ' ', word).split()
        numbers = set(int(num) for num in numbers)
        return len(numbers)
        """
        :type word: str
        :rtype: int
        """
        
