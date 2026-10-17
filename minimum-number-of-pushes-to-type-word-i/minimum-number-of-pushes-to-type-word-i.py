# ==========================================================
# Problem    : Minimum Number of Pushes to Type Word I
# URL        : https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, String, Greedy
#
# Acceptance : 77.4%
# Likes      : 449  |  Dislikes: 58
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12092000  (beats 98.6577%)
# Submitted  : 1792188742
# Exported   : 2026-10-17 07:20:23 UTC
#
# Hints: We have 8 keys in total. We can type 8 characters with one push each, 8 different characters with two pushes each, and so on.
#   The optimal way is to map letters to keys evenly.
# ==========================================================
class Solution(object):
    def minimumPushes(self, word):
        counter = 0
        n  =  len(word)
        for i in range(n):
            counter += (i // 8) + 1
        return counter
        """
        :type word: str
        :rtype: int
        """
        
