# ================================================================
# Problem : Permutation Difference between Two Strings
# URL     : https://leetcode.com/problems/permutation-difference-between-two-strings/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String
#
# --- Community Stats ---
# Acceptance Rate : 87.8%
# Likes           : 193
# Dislikes        : 17
#
# --- My Submission ---
# Language   : python
# Runtime    : 3  (beats 64.2858%)
# Memory     : 12320000  (beats 66.83670000000001%)
# Submitted  : 1775336689
#
# --- Hints ---
# For each character, find the indices of its occurrences in string <code>s</code> then in string <code>t</code>.
# ================================================================

class Solution(object):
    def findPermutationDifference(self, s, t):
        s_set = set(s)
        t_set = set(t)
        result = 0
        for i in s_set:
            for j in t_set:
                if i == j:
                    result += abs(s.index(i) -t.index(j))
        return result
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
