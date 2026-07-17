# ==========================================================
# Problem    : Shortest Distance to a Character
# URL        : https://leetcode.com/problems/shortest-distance-to-a-character/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Two Pointers, String
#
# Acceptance : 72.9%
# Likes      : 3349  |  Dislikes: 196
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12420000  (beats 48.60679999999999%)
# Submitted  : 1784319456
# Exported   : 2026-07-17 20:19:39 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def shortestToChar(self, s, c):
        n = len(s)
        answer = [0] * n

        # Left -> Right
        prev = -float("inf")
        for i in range(n):
            if s[i] == c:
                prev = i
            answer[i] = i - prev

        # Right -> Left
        prev = float("inf")
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], prev - i)

        return answer
                
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        
