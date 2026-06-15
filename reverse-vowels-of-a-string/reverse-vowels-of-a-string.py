# ==========================================================
# Problem    : Reverse Vowels of a String
# URL        : https://leetcode.com/problems/reverse-vowels-of-a-string/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Two Pointers, String
#
# Acceptance : 61.5%
# Likes      : 5411  |  Dislikes: 2862
#
# Language   : python
# Runtime    : 11  (beats 94.8311%)
# Memory     : 13756000  (beats 25.674599999999995%)
# Submitted  : 1781516179
# Exported   : 2026-06-15 09:39:51 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')

        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:

            while left < right and s[left] not in vowels:
                left += 1

            while left < right and s[right] not in vowels:
                right -= 1

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return ''.join(s)

        """
        :type s: str
        :rtype: str
        """
        
