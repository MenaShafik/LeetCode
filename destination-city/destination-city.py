# ==========================================================
# Problem    : Destination City
# URL        : https://leetcode.com/problems/destination-city/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, String
#
# Acceptance : 79.5%
# Likes      : 2323  |  Dislikes: 108
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12308000  (beats 63.1841%)
# Submitted  : 1779181061
# Exported   : 2026-05-19 10:48:47 UTC
#
# Hints: Start in any city and use the path to move to the next city.
#   Eventually, you will reach a city with no path outgoing, this is the destination city.
# ==========================================================
class Solution(object):
    def destCity(self, paths):
        starts = set()
        for start, end in paths:
            starts.add(start)
            
        for start, end in paths:
            if end not in starts:
                return end
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        
