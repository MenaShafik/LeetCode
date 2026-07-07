# ==========================================================
# Problem    : Ransom Note
# URL        : https://leetcode.com/problems/ransom-note/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String, Counting
#
# Acceptance : 66.1%
# Likes      : 5748  |  Dislikes: 548
#
# Language   : python
# Runtime    : 3  (beats 99.3974%)
# Memory     : 12532000  (beats 85.9576%)
# Submitted  : 1783420389
# Exported   : 2026-07-07 10:44:26 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for char in set(ransomNote):
                    if ransomNote.count(char) > magazine.count(char):
                        return False
        return True 
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
