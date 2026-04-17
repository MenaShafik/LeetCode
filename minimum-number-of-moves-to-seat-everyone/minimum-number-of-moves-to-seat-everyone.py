# ================================================================
# Problem : Minimum Number of Moves to Seat Everyone
# URL     : https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Greedy, Sorting, Counting Sort
#
# --- Community Stats ---
# Acceptance Rate : 87.2%
# Likes           : 1445
# Dislikes        : 346
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12264000  (beats 95.8159%)
# Submitted  : 1775681249
#
# --- Hints ---
# Can we sort the arrays to help solve the problem?
# Can we greedily match each student to a seat?
# The smallest positioned student will go to the smallest positioned chair, and then the next smallest positioned student will go to the next smallest positioned chair, and so on.
# ================================================================

class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        move = 0
        for i in range(len(seats)):
            move+= abs(seats[i] - students[i])
        return move
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        
