# ==========================================================
# Problem    : Maximum Number of Balloons
# URL        : https://leetcode.com/problems/maximum-number-of-balloons/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String, Counting
#
# Acceptance : 62.3%
# Likes      : 2037  |  Dislikes: 124
#
# Language   : python
# Runtime    : 4  (beats 68.5186%)
# Memory     : 12532000  (beats 15.277799999999996%)
# Submitted  : 1782123948
# Exported   : 2026-06-22 10:32:22 UTC
#
# Hints: Count the frequency of letters in the given string.
#   Find the letter than can make the minimum number of instances of the word "balloon".
# ==========================================================
class Solution:
    def maxNumberOfBalloons(self, text):
        count = {}

        for ch in text:
            count[ch] = count.get(ch, 0) + 1

        return min(
            count.get('b', 0),
            count.get('a', 0),
            count.get('l', 0) // 2,
            count.get('o', 0) // 2,
            count.get('n', 0)
        )
        """
        :type text: str
        :rtype: int
        """
        
