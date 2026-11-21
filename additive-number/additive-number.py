# ==========================================================
# Problem    : Additive Number
# URL        : https://leetcode.com/problems/additive-number/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : String, Backtracking
#
# Acceptance : 34.8%
# Likes      : 1308  |  Dislikes: 830
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12208000  (beats 64.46530000000001%)
# Submitted  : 1795249561
# Exported   : 2026-11-21 09:27:20 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def isAdditiveNumber(self, num):
        n = len(num)
        for i in range(1,n):
            for j in range(i+1,n):
                a = num[:i]
                b = num[i:j]
                if len(a) > 1 and a[0] == '0':
                    continue
                if len(b) > 1 and b[0] == '0':
                    continue
                while j < n:
                    c = str(int(a) + int(b))

                    if num[j:j+len(c)] != c:
                        break

                    j += len(c)
                    a = b
                    b = c

                if j == n:
                    return True
        return False

        """
        :type num: str
        :rtype: bool
        """
        
