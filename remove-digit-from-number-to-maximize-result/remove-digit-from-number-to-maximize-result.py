# ==========================================================
# Problem    : Remove Digit From Number to Maximize Result
# URL        : https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String, Greedy, Enumeration
#
# Acceptance : 49.0%
# Likes      : 981  |  Dislikes: 66
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12016000  (beats 90.0%)
# Submitted  : 1794645599
# Exported   : 2026-11-15 10:01:01 UTC
#
# Hints: The maximum length of number is really small.
#   Iterate through the digits of number and every time we see digit, try removing it.
#   To remove a character at index i, concatenate the substring from index 0 to i - 1 and the substring from index i + 1 to number.length - 1.
# ==========================================================
class Solution(object):
    def removeDigit(self, number, digit):
        ans  = ''
        for i in range(len(number)):
            if number[i] == digit:
                new =  number[:i]  +number[i+1:]
                ans = max(ans,new)
        return ans
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        
