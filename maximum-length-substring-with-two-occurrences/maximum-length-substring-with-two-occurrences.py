# ==========================================================
# Problem    : Maximum Length Substring With Two Occurrences
# URL        : https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String, Sliding Window
#
# Acceptance : 77.6%
# Likes      : 526  |  Dislikes: 32
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12364000  (beats 54.446600000000004%)
# Submitted  : 1786741649
# Exported   : 2026-08-15 20:10:03 UTC
#
# Hints: We can try all substrings by brute-force since the constraints are very small.
# ==========================================================
class Solution(object):
    def maximumLengthSubstring(self, s):
        s = s.lower()

        left = 0
        count = {}
        max_length = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            while count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

        """
        :type s: str
        :rtype: int
        """
        
