# ==========================================================
# Problem    : Unique Morse Code Words
# URL        : https://leetcode.com/problems/unique-morse-code-words/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, String
#
# Acceptance : 83.7%
# Likes      : 2629  |  Dislikes: 1555
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12464000  (beats 18.98729999999999%)
# Submitted  : 1783330295
# Exported   : 2026-07-06 09:37:57 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        codes={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}

        transformations = set()
        for word in words:
            s = ""
            for i in word:
                s+=codes[i]
            transformations.add(s)
        return len(transformations)
        """
        :type words: List[str]
        :rtype: int
        """
        
