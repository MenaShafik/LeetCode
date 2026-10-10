# ==========================================================
# Problem    : Find the K-Beauty of a Number
# URL        : https://leetcode.com/problems/find-the-k-beauty-of-a-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, String, Sliding Window
#
# Acceptance : 64.0%
# Likes      : 755  |  Dislikes: 48
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12396000  (beats 63.333299999999994%)
# Submitted  : 1791618978
# Exported   : 2026-10-10 11:52:12 UTC
#
# Hints: We should check all the substrings of num with a length of k and see if it is a divisor of num.
#   We can more easily obtain the substrings by converting num into a string and converting back to an integer to check for divisibility.
# ==========================================================
class Solution(object):
    def divisorSubstrings(self, num, k):
        counter = 0
        s = str(num)
        for i in range(len(s)):
            for j in range(i+k,len(s)+1):
                if int(j-i) ==k:
                    divisor = int(s[i:j])
                    if divisor !=0 and num%divisor == 0:
                        counter +=1
        return counter
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        
