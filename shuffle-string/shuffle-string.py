# ================================================================
# Problem : Shuffle String
# URL     : https://leetcode.com/problems/shuffle-string/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, String
#
# --- Community Stats ---
# Acceptance Rate : 85.4%
# Likes           : 2942
# Dislikes        : 546
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12260000  (beats 91.92750000000001%)
# Submitted  : 1775922618
#
# --- Hints ---
# You can create an auxiliary string t of length n.
# Assign t[indexes[i]] to s[i] for each i from 0 to n-1.
# ================================================================

class Solution(object):
    def restoreString(self, s, indices):
        res = [''] * len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return ''.join(res)
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        
