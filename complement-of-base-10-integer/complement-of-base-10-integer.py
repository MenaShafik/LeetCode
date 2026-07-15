# ==========================================================
# Problem    : Complement of Base 10 Integer
# URL        : https://leetcode.com/problems/complement-of-base-10-integer/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Bit Manipulation
#
# Acceptance : 63.4%
# Likes      : 2855  |  Dislikes: 146
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12500000  (beats 15.887900000000016%)
# Submitted  : 1784109622
# Exported   : 2026-07-15 10:09:25 UTC
#
# Hints: A binary number plus its complement will equal 111....111 in binary.  Also, N = 0 is a corner case.
# ==========================================================
class Solution(object):
    def bitwiseComplement(self, n):
        if n == 0:
            return 1
        binary= bin(n)[2:]
        complement = "".join("1" if b == "0" else "0" for b in binary)
        return int(complement, 2)
        """
        :type n: int
        :rtype: int
        """
        
