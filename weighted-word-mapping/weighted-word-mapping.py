# ==========================================================
# Problem    : Weighted Word Mapping
# URL        : https://leetcode.com/problems/weighted-word-mapping/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, String, Simulation
#
# Acceptance : 90.6%
# Likes      : 240  |  Dislikes: 10
#
# Language   : python
# Runtime    : 11  (beats 91.3621%)
# Memory     : 12436000  (beats 24.412300000000002%)
# Submitted  : 1784713543
# Exported   : 2026-07-22 09:51:22 UTC
#
# Hints: For each word, sum character weights using <code>weights[c - 'a']</code>
#   Take the sum modulo <code>26</code>
#   Map the value to a character using reverse order: <code>char = 'z' - value</code>
#   Append all mapped characters in order to form the result string
# ==========================================================
class Solution(object):
    def mapWordWeights(self, words, weights):
        result = ""

        for word in words:
            total = 0

            for ch in word:
                index = ord(ch) - ord('a')
                total += weights[index]

            rem = total % 26
            result += chr(ord('z') - rem)

        return result

        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        
