# ==========================================================
# Problem    : Split a String in Balanced Strings
# URL        : https://leetcode.com/problems/split-a-string-in-balanced-strings/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String, Greedy, Counting
#
# Acceptance : 87.5%
# Likes      : 2932  |  Dislikes: 960
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12404000  (beats 19.526599999999995%)
# Submitted  : 1784364509
# Exported   : 2026-07-18 08:50:28 UTC
#
# Hints: Loop from left to right maintaining a balance variable when it gets an L increase it by one otherwise decrease it by one.
#   Whenever the balance variable reaches zero then we increase the answer by one.
# ==========================================================
class Solution(object):
    def balancedStringSplit(self, s):
        balance = 0
        count = 0

        for char in s:
            if char == 'L':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                count += 1

        return count
        """
        :type s: str
        :rtype: int
        """
        
