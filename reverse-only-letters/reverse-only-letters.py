# ==========================================================
# Problem    : Reverse Only Letters
# URL        : https://leetcode.com/problems/reverse-only-letters/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Two Pointers, String
#
# Acceptance : 68.7%
# Likes      : 2471  |  Dislikes: 87
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12272000  (beats 88.5191%)
# Submitted  : 1784193850
# Exported   : 2026-07-16 09:28:12 UTC
#
# Hints: This problem is exactly like reversing a normal string except that there are certain characters that we have to simply skip. That should be easy enough to do if you know how to reverse a string using the two-pointer approach.
# ==========================================================
class Solution(object):
    def reverseOnlyLetters(self, s):
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if not  s[left].isalpha():
                left += 1
            elif not s[right].isalpha():
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)
        """
        :type s: str
        :rtype: str
        """
        
