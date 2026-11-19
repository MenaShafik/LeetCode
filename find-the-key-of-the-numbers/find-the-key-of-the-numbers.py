# ==========================================================
# Problem    : Find the Key of the Numbers
# URL        : https://leetcode.com/problems/find-the-key-of-the-numbers/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# Acceptance : 76.2%
# Likes      : 118  |  Dislikes: 16
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12120000  (beats 68.1818%)
# Submitted  : 1795077373
# Exported   : 2026-11-19 21:09:51 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def generateKey(self, num1, num2, num3):
        s1 = str(num1).zfill(4)
        s2 = str(num2).zfill(4)
        s3 = str(num3).zfill(4)

        result = ""

        for i in range(4):
            result += min(s1[i], s2[i], s3[i])

        return int(result)
        """
        :type num1: int
        :type num2: int
        :type num3: int
        :rtype: int
        """
        
