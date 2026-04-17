# ================================================================
# Problem : Restore Finishing Order
# URL     : https://leetcode.com/problems/restore-finishing-order/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table
#
# --- Community Stats ---
# Acceptance Rate : 91.2%
# Likes           : 121
# Dislikes        : 5
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12452000  (beats 25.075099999999992%)
# Submitted  : 1774474532
#
# --- Hints ---
# Use a hash set for quick friend lookups from <code>friends</code>.
# Iterate over <code>order</code>, checking the set to collect your friends in finishing order.
# ================================================================

class Solution(object):
    def recoverOrder(self, order, friends):
        friend_set = set(friends)
        return [x for x in order if x in friend_set]
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        
