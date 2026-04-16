# ================================================================
# Problem : Unique Email Addresses
# URL     : https://leetcode.com/problems/unique-email-addresses/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, String
#
# --- Community Stats ---
# Acceptance Rate : 67.8%
# Likes           : 2813
# Dislikes        : 363
#
# --- My Submission ---
# Language   : python
# Runtime    : 4  (beats 89.947%)
# Memory     : 12512000  (beats 10.58189999999999%)
# Submitted  : 1774043250
#
# --- Hints ---
# N/A
# ================================================================

class Solution(object):
    def numUniqueEmails(self, emails):
        ret = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            normalized = local + '@' + domain
            ret.add(normalized)
        return len(ret)
        """
        :type emails: List[str]
        :rtype: int
        """
        
