# ================================================================
# Problem : Sort the People
# URL     : https://leetcode.com/problems/sort-the-people/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, String, Sorting
#
# --- Community Stats ---
# Acceptance Rate : 84.8%
# Likes           : 1868
# Dislikes        : 41
#
# --- My Submission ---
# Language   : python
# Runtime    : 4  (beats 83.6918%)
# Memory     : 12736000  (beats 20.250999999999998%)
# Submitted  : 1776370381
#
# --- Hints ---
# Find the tallest person and swap with the first person, then find the second tallest person and swap with the second person, etc. Repeat until you fix all n people.
# ================================================================

class Solution(object):
    def sortPeople(self, names, heights):
        combined = zip(names, heights)
        combined = sorted(combined, key=lambda x: x[1], reverse=True)
        return [name for name, height in combined]
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        
