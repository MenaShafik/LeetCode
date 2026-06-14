# ==========================================================
# Problem    : Fizz Buzz
# URL        : https://leetcode.com/problems/fizz-buzz/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, String, Simulation
#
# Acceptance : 75.6%
# Likes      : 3410  |  Dislikes: 467
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 13308000  (beats 43.58909999999998%)
# Submitted  : 1781436307
# Exported   : 2026-06-14 12:34:04 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def fizzBuzz(self, n):
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer

        """
        :type n: int
        :rtype: List[str]
        """
        
