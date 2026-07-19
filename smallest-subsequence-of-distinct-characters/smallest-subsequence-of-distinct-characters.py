# ==========================================================
# Problem    : Smallest Subsequence of Distinct Characters
# URL        : https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : String, Stack, Greedy, Monotonic Stack
#
# Acceptance : 67.2%
# Likes      : 2963  |  Dislikes: 206
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12460000  (beats 17.045499999999997%)
# Submitted  : 1784457019
# Exported   : 2026-07-19 11:05:05 UTC
#
# Hints: Greedily try to add one missing character. How to check if adding some character will not cause problems ? Use bit-masks to check whether you will be able to complete the sub-sequence if you add the character at some index i.
# ==========================================================
class Solution(object):
    def smallestSubsequence(self, s):
        stack = []
        seen = set()
        last_occurrence = {char: i for i, char in enumerate(s)}

        for i, char in enumerate(s):
            if char not in seen:
                while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
                stack.append(char)
                seen.add(char)

        return ''.join(stack)
        """
        :type s: str
        :rtype: str
        """
        
