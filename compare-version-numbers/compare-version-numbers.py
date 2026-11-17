# ==========================================================
# Problem    : Compare Version Numbers
# URL        : https://leetcode.com/problems/compare-version-numbers/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Two Pointers, String
#
# Acceptance : 47.2%
# Likes      : 3228  |  Dislikes: 2799
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12148000  (beats 82.06069999999998%)
# Submitted  : 1794905387
# Exported   : 2026-11-17 09:00:45 UTC
#
# Hints: You can use two pointers for each version string to traverse them together while comparing the corresponding segments.
#   Utilize the substring method to extract each version segment delimited by '.'. Ensure you're extracting the segments correctly by adjusting the start and end indices accordingly.
# ==========================================================
class Solution(object):
    def compareVersion(self, version1, version2):
        num1 = version1.split('.')
        num2 = version2.split('.')

        for i in range(max(len(num1), len(num2))):
            n1 = int(num1[i]) if i < len(num1) else 0
            n2 = int(num2[i]) if i < len(num2) else 0

            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1

        return 0
                

        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
