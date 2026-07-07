# ==========================================================
# Problem    : Longest Uncommon Subsequence I
# URL        : https://leetcode.com/problems/longest-uncommon-subsequence-i/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 62.4%
# Likes      : 127  |  Dislikes: 371
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12552000  (beats 7.105427357601002e-15%)
# Submitted  : 1783420949
# Exported   : 2026-07-07 10:44:24 UTC
#
# Hints: Think very simple.
#   If <code>a == b</code>, the answer is -1.
#   Otherwise, the answer is the string <code>a</code> or the string <code>b</code>.
# ==========================================================
class Solution(object):
    def findLUSlength(self, a, b):
        if a == b:
            return -1
        else:
            return max(len(a),len(b))
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        
