# ==========================================================
# Problem    : Longest Nice Substring
# URL        : https://leetcode.com/problems/longest-nice-substring/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String, Divide and Conquer, Bit Manipulation, Sliding Window
#
# Acceptance : 64.5%
# Likes      : 1528  |  Dislikes: 986
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12548000  (beats 18.239%)
# Submitted  : 1784629868
# Exported   : 2026-07-21 10:42:52 UTC
#
# Hints: Brute force and check each substring to see if it is nice.
# ==========================================================
class Solution(object):
    def longestNiceSubstring(self, s):
        if len(s)< 2:
            return ''
        chars = set(s)

        for i, ch in enumerate(s):
            if ch.swapcase() not in chars:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])

                if len(left) >= len(right):
                    return left
                else:
                    return right
        
        return s
        """
        :type s: str
        :rtype: str
        """
        
