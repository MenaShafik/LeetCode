# ==========================================================
# Problem    : Minimum Number of Chairs in a Waiting Room
# URL        : https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String, Simulation
#
# Acceptance : 79.2%
# Likes      : 167  |  Dislikes: 16
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12200000  (beats 100.0%)
# Submitted  : 1791789654
# Exported   : 2026-10-12 07:37:17 UTC
#
# Hints: Iterate from left to right over the string and keep track of the number of people in the waiting room using a variable that you will increment on every occurrence of ‘E’ and decrement on every occurrence of ‘L’.
#   The answer is the maximum number of people in the waiting room at any instance.
# ==========================================================
class Solution(object):
    def minimumChairs(self, s):
        counter = 0
        max_chairs = 0
        for i in s:
            if i == "E":
                counter+=1
            else:
                counter-=1
            max_chairs = max(counter,max_chairs)
        return max_chairs
        """
        :type s: str
        :rtype: int
        """
        
