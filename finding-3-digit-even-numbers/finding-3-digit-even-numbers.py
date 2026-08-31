# ==========================================================
# Problem    : Finding 3-Digit Even Numbers
# URL        : https://leetcode.com/problems/finding-3-digit-even-numbers/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Recursion, Sorting, Enumeration
#
# Acceptance : 78.6%
# Likes      : 1623  |  Dislikes: 346
#
# Language   : python
# Runtime    : 79  (beats 68.14090000000012%)
# Memory     : 12236000  (beats 97.7876%)
# Submitted  : 1788166468
# Exported   : 2026-08-31 08:59:00 UTC
#
# Hints: The range of possible answers includes all even numbers between 100 and 999 inclusive. Could you check each possible answer to see if it could be formed from the digits in the array?
# ==========================================================
class Solution(object):
    def findEvenNumbers(self, digits):
        result = []

        for n in range(100, 1000, 2):
            for i in str(n):
                if str(n).count(i) > digits.count(int(i)):
                    break
            else:
                result.append(n)

        return result


        """
        :type digits: List[int]
        :rtype: List[int]
        """
