# ==========================================================
# Problem    : Add to Array-Form of Integer
# URL        : https://leetcode.com/problems/add-to-array-form-of-integer/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math
#
# Acceptance : 45.6%
# Likes      : 3710  |  Dislikes: 317
#
# Language   : python
# Runtime    : 61  (beats 67.83390000000001%)
# Memory     : 12576000  (beats 93.87310000000001%)
# Submitted  : 1782903868
# Exported   : 2026-07-01 11:15:44 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def addToArrayForm(self, num, k):
        num_str = ''.join(map(str,num))
        total = int(num_str)+k
        return [int(digit) for digit in str(total)]
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        
