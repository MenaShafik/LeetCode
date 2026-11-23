# ==========================================================
# Problem    : Letter Combinations of a Phone Number
# URL        : https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Hash Table, String, Backtracking
#
# Acceptance : 67.2%
# Likes      : 21514  |  Dislikes: 1152
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12148000  (beats 83.94%)
# Submitted  : 1795421320
# Exported   : 2026-11-23 11:31:45 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        stack = [""]

        for i in digits:
            temp = []

            for j in stack:
                for k in phone[i]:
                    temp.append(j + k)

            stack = temp

        return stack
        """
        :type digits: str
        :rtype: List[str]
        """
        
