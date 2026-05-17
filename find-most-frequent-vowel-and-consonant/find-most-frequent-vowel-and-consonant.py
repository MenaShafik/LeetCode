# ==========================================================
# Problem    : Find Most Frequent Vowel and Consonant
# URL        : https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String, Counting
#
# Acceptance : 89.3%
# Likes      : 431  |  Dislikes: 15
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12208000  (beats 94.465%)
# Submitted  : 1779008448
# Exported   : 2026-05-17 09:15:13 UTC
#
# Hints: Use a hashmap
#   Simulate as described
# ==========================================================
class Solution(object):
    def maxFreqSum(self, s):
        vowels = 'aeiou'
        freq = {}
        for i in s:
            freq[i]=freq.get(i, 0) + 1
        max_vowel = 0
        max_consonant = 0
        for char, count in freq.items():
            if char in vowels:
                max_vowel = max(max_vowel, count)
            else:
                max_consonant = max(max_consonant, count)

        return max_vowel + max_consonant
        """
        :type s: str
        :rtype: int
        """
        
