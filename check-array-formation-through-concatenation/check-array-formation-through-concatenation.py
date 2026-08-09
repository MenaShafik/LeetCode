# ==========================================================
# Problem    : Check Array Formation Through Concatenation
# URL        : https://leetcode.com/problems/check-array-formation-through-concatenation/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table
#
# Acceptance : 57.5%
# Likes      : 948  |  Dislikes: 144
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12568000  (beats 2.631599999999997%)
# Submitted  : 1786266448
# Exported   : 2026-08-09 22:39:10 UTC
#
# Hints: Note that the distinct part means that every position in the array belongs to only one piece
#   Note that you can get the piece every position belongs to naively
# ==========================================================
class Solution(object):
    def canFormArray(self, arr, pieces):
        i = 0

        while i < len(arr):
            found = False

            for piece in pieces:
                if piece[0] == arr[i]:
                    for num in piece:
                        if i >= len(arr) or arr[i] != num:
                            return False
                        i += 1

                    found = True
                    break

            if not found:
                return False

        return True
            
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        
