# ==========================================================
# Problem    : Lemonade Change
# URL        : https://leetcode.com/problems/lemonade-change/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Greedy
#
# Acceptance : 59.3%
# Likes      : 3494  |  Dislikes: 218
#
# Language   : python
# Runtime    : 3  (beats 75.0563%)
# Memory     : 15308000  (beats 22.163800000000002%)
# Submitted  : 1783696488
# Exported   : 2026-07-10 15:16:46 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def lemonadeChange(self, bills):
        five, ten = 0, 0
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        
        return True
        """
        :type bills: List[int]
        :rtype: bool
        """
        
