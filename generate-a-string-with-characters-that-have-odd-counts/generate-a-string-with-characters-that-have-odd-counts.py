# ==========================================================
# Problem    : Generate a String With Characters That Have Odd Counts
# URL        : https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 78.5%
# Likes      : 534  |  Dislikes: 1288
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12296000  (beats 89.60000000000001%)
# Submitted  : 1784540834
# Exported   : 2026-07-20 09:56:52 UTC
#
# Hints: If n is odd, return a string of size n formed only by 'a', else return string formed with n-1 'a' and 1 'b''.
# ==========================================================
class Solution(object):
    def generateTheString(self, n):
        	return 'a' * (n - 1) + 'b' if n % 2 == 0 else 'a' * n
