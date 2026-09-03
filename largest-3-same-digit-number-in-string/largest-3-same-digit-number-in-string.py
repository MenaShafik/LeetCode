# ==========================================================
# Problem    : Largest 3-Same-Digit Number in String
# URL        : https://leetcode.com/problems/largest-3-same-digit-number-in-string/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 72.7%
# Likes      : 1400  |  Dislikes: 55
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12488000  (beats 26.548699999999997%)
# Submitted  : 1788457978
# Exported   : 2026-09-03 18:48:22 UTC
#
# Hints: We can sequentially check if “999”, “888”, “777”, … , “000” exists in num in that order. The first to be found is the maximum good integer.
#   If we cannot find any of the above integers, we return an empty string “”.
# ==========================================================
class Solution(object):
    def largestGoodInteger(self, num):
        largest = ""

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if num[i] > largest:
                    largest = num[i]

        return largest * 3
                
        """
        :type num: str
        :rtype: str
        """
        
