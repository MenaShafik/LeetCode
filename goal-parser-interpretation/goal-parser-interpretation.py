# ================================================================
# Problem : Goal Parser Interpretation
# URL     : https://leetcode.com/problems/goal-parser-interpretation/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# --- Community Stats ---
# Acceptance Rate : 88.0%
# Likes           : 1679
# Dislikes        : 95
#
# --- My Submission ---
# Language   : python
# Runtime    : 12  (beats 80.4487%)
# Memory     : 12564000  (beats 4.487200000000001%)
# Submitted  : 1775424028
#
# --- Hints ---
# You need to check at most 2 characters to determine which character comes next.
# ================================================================

class Solution(object):
    def interpret(self, command):
        command = command.replace("()","o")
        command = command.replace("(al)","al")

        return command
        """
        :type command: str
        :rtype: str
        """
        
