# ==========================================================
# Problem    : Number of Changing Keys
# URL        : https://leetcode.com/problems/number-of-changing-keys/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 80.7%
# Likes      : 165  |  Dislikes: 18
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12408000  (beats 15.384599999999999%)
# Submitted  : 1778014939
# Exported   : 2026-05-05 21:25:51 UTC
#
# Hints: Change all the characters to lowercase and then return the number of indices where the character does not match with the last index character.
# ==========================================================
class Solution(object):
    def countKeyChanges(self, s):
        count = 0
        for i in range(1, len(s)):
            if s[i].upper() != s[i-1].upper():
                count += 1
        return count
        """
        :type s: str
        :rtype: int
        """
        
