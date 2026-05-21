# ==========================================================
# Problem    : Uncommon Words from Two Sentences
# URL        : https://leetcode.com/problems/uncommon-words-from-two-sentences/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String, Counting
#
# Acceptance : 75.7%
# Likes      : 1907  |  Dislikes: 209
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12192000  (beats 100.0%)
# Submitted  : 1779311247
# Exported   : 2026-05-21 09:15:59 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        words1 = s1.split()
        words2 = s2.split()
        
        count = {}
        
        for word in words1:
            count[word] = count.get(word, 0) + 1
        
        for word in words2:
            count[word] = count.get(word, 0) + 1
        
        uncommon_words = [word for word, freq in count.items() if freq == 1]
        
        return uncommon_words
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        
