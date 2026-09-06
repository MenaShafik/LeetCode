# ==========================================================
# Problem    : Number of Senior Citizens
# URL        : https://leetcode.com/problems/number-of-senior-citizens/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, String
#
# Acceptance : 81.2%
# Likes      : 797  |  Dislikes: 59
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12212000  (beats 94.382%)
# Submitted  : 1788684668
# Exported   : 2026-09-06 21:31:20 UTC
#
# Hints: Convert the value at index 11 and 12 to a numerical value.
#   The age of the person at index i is equal to details[i][11]*10+details[i][12].
# ==========================================================
class Solution(object):
    def countSeniors(self, details):
        return sum(int(person[11:13]) > 60 for person in details)
        """
        :type details: List[str]
        :rtype: int
        """
        
