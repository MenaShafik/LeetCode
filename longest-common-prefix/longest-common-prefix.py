# ==========================================================
# Problem    : Longest Common Prefix
# URL        : https://leetcode.com/problems/longest-common-prefix/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, String, Trie
#
# Acceptance : 47.6%
# Likes      : 21449  |  Dislikes: 4939
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12396000  (beats 69.18599999999999%)
# Submitted  : 1779262455
# Exported   : 2026-05-20 07:40:23 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
        """
        :type strs: List[str]
        :rtype: str
        """
        
