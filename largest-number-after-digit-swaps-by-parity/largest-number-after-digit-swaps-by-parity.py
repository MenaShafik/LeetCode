# ==========================================================
# Problem    : Largest Number After Digit Swaps by Parity
# URL        : https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Sorting, Heap (Priority Queue)
#
# Acceptance : 65.7%
# Likes      : 707  |  Dislikes: 316
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12420000  (beats 30.681800000000006%)
# Submitted  : 1789828389
# Exported   : 2026-09-19 14:44:24 UTC
#
# Hints: The bigger digit should appear first (more to the left) because it contributes more to the value of the number.
#   Get all the even digits, as well as odd digits. Sort them separately.
#   Reconstruct the number by giving the earlier digits the highest available digit of the same parity.
# ==========================================================
class Solution(object):
    def largestInteger(self, num):
        digits = list(str(num))
        even = []
        odd = []
        for i in digits:
            if int(i) % 2 ==0:
                even.append((i))
            else:
                odd.append((i))
        even.sort(reverse= True)
        odd.sort(reverse= True)
        result = []
        for i in digits:
            if int(i) % 2 == 0:
                result.append(even.pop(0))
            else:
                result.append(odd.pop(0))
        return int("".join(result))
    

        """
        :type num: int
        :rtype: int
        """
        
