# ==========================================================
# Problem    : Percentage of Letter in String
# URL        : https://leetcode.com/problems/percentage-of-letter-in-string/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 75.2%
# Likes      : 564  |  Dislikes: 64
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12424000  (beats 16.1905%)
# Submitted  : 1779102508
# Exported   : 2026-05-18 11:18:43 UTC
#
# Hints: Can we count the number of occurrences of letter in s?
#   Recall that the percentage is calculated as (occurrences / total) * 100.
# ==========================================================
class Solution(object):
    def percentageLetter(self, s, letter):
        count = 0
        for i in s:
            if i==letter:
                count +=1
        return (count*100)/len(s)
        
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        
