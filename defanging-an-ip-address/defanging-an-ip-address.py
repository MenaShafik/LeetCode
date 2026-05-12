# ==========================================================
# Problem    : Defanging an IP Address
# URL        : https://leetcode.com/problems/defanging-an-ip-address/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 90.0%
# Likes      : 2365  |  Dislikes: 1788
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12460000  (beats 16.0991%)
# Submitted  : 1778581489
# Exported   : 2026-05-12 10:34:09 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def defangIPaddr(self, address):
        return address.replace(".","[.]")
                
        """
        :type address: str
        :rtype: str
        """
        
